# -*- coding: utf-8 -*-

"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """


from pathlib import Path
import os, importlib, tempfile, pprint, shutil
from collections import OrderedDict
import sys, glob, inspect, logging, textwrap
import Lamia
from ..abstractlibslamia import AbstractLibsLamia

import qgis
from qgis.PyQt import QtGui, uic, QtCore, QtXml

from .exfiltration_indicators import all_exfiltration_indicators
from .infiltration_indicators import all_infiltration_indicators
from .ensablement_indicators import all_ensablement_indicators
# from .effondrement_indicators import all_effondrement_indicators
# from .bouchage_indicators import all_bouchage_indicators
from .red_cap_hydraulique_indicators import all_red_cap_hyfraulique_indicators

import pandas as pd
import numpy as np

ITVMATERIAL = {
    "AA": "amiante-ciment",
    "AB": "bitume",
    "AC": "fibres projetées",
    "AD": "briquetage",
    "AE": "grès",
    "AF": "mortier de ciment",
    "AG": "béton",
    "Ah": "béton armé",
    "AI": "béton projeté",
    "AJ": "segements de béton",
    "AK": "fibres-ciment",
    "AL": "plastiques renforcés de fibres",
    "AM": "fonte",
    "AN": "fonte grise",
    "AO": "fonte ductile",
    "AP": "acier",
    "AQ": "type non identifié de fer ou d'acier",
    "AR": "maçonnerie (appareillée)",
    "AS": "maçonnerie (non appareillée)",
    "AT": "époxy",
    "AU": "polyester",
    "AV": "polyéthylène",
    "AW": "polypropylène",
    "AX": "PVC-U",
    "AY": "type non identifié de plastique",
    "AZ": "matériau non identifié",
    "Z": "autre (cf remarque)",
}

ITVCOLUMNS = {
    "id": int,  # 0
    "regard_1": str,
    "regard_2": str,
    "reg_depart": str,
    "sens": str,
    "adresse": str,
    "ville": str,
    "foncier": str,
    "emplacemnt": str,
    "date_ins": str,
    "nom_ins": str,  # 10
    "entreprise": str,
    "norme": str,
    "methode": str,
    "objet": str,
    "nettoyage": str,
    "forme": str,
    "hauteur": float,
    "materiau": str,
    "prof_reg_1": float,
    "prof_reg_2": float,  # 20
    "type": str,
    "utilisat": str,
    "precipit": str,
    "debit": str,
    "encodage": str,
    "dist_reg_1": float,
    "code": str,
    "carac_1": str,
    "carac_2": str,
    "remarque": str,  # 30
}


class ITVImportCore(AbstractLibsLamia):

    POSTPROTOOLNAME = "lamiaITVimport"
    SHOWSQL = False
    fileext = ".csv"

    def __init__(self, dbaseparser, messageinstance=None):
        super(ITVImportCore, self).__init__(dbaseparser, messageinstance)

    def computeNotation(self, conffile, itvpks):
        # * prepare source df : pdnotation as notation   and resdf as sourcedata
        conffile = self.getConfFilePath(conffile)
        pdnotation = pd.read_csv(
            conffile, sep=";", encoding="iso-8859-1"
        )  # iso-8859-1   utf-8
        pdnotation.index = pdnotation["Code"].values.tolist()
        pdnotation = pdnotation.transpose()
        pdnotation = pdnotation.drop(["Code"])
        subnotestitle = pdnotation.index.tolist()[1:]
        subnotestitle2 = [elem + "_l" for elem in subnotestitle]

        resfiles = []
        for itvpk in itvpks:
            tempfiles = self.dbase.lamiaorm["itv"].read(itvpk)["file"].split(";")
            tempfiles = [self.dbase.completePathOfFile(fl.strip()) for fl in tempfiles]
            resfiles += tempfiles

        resdf = self.readITVs(resfiles)
        uniquedf = self.getUniquesValuesbyEdge(resfiles)

        # remove uniquedf column not in notation
        notationcol = pdnotation.columns
        rescols = uniquedf.columns[2:]
        for column in rescols:
            if column not in notationcol:
                uniquedf = uniquedf.drop(columns=[column])

        # prepare result df
        readitvfields = ["ville", "adresse", "materiau", "hauteur"]
        sigfield = ["id_SIG", "longueur"]
        finalfd = pd.DataFrame(
            columns=["regard_1", "regard_2"]
            + readitvfields
            + sigfield
            + notationcol.tolist()
            + subnotestitle
            + subnotestitle2  # notation divided by lenght
        )

        # compute final notes
        for idx, row in uniquedf.iterrows():
            resdict = {"regard_1": row["regard_1"], "regard_2": row["regard_2"]}
            # readitvfields
            resdfrow = resdf[
                (resdf["regard_1"] == row["regard_1"])
                & (resdf["regard_2"] == row["regard_2"])
            ]
            resitvfields = dict(
                zip(readitvfields, resdfrow[readitvfields].iloc[0].values.tolist())
            )
            resdict = {**resdict, **resitvfields}

            # SIG field
            upnode = self.dbase.lamiaorm["node"][
                f"name = '{row['regard_1']}' AND lpk_revision_end IS NULL "
            ]
            downnode = self.dbase.lamiaorm["node"][
                f"name = '{row['regard_2']}' AND lpk_revision_end IS NULL "
            ]
            if upnode and downnode:
                edge = self.dbase.lamiaorm["edge"][
                    f"(lid_descriptionsystem_1 = {upnode[0]['id_descriptionsystem']} \
                    AND  lid_descriptionsystem_2 = {downnode[0]['id_descriptionsystem']}) \
                        or (lid_descriptionsystem_1 = {upnode[0]['id_descriptionsystem']} \
                            AND  lid_descriptionsystem_2 = {downnode[0]['id_descriptionsystem']})"
                ]

                if edge:
                    print(edge)
                    resdict["id_SIG"] = edge[0]["id_edge"]
                    resdict["longueur"] = self.dbase.query(
                        f"SELECT ST_Length(geom) FROM edge WHERE pk_edge = {edge[0]['pk_edge']}"
                    )[0][0]

            # subnotestitle fields
            remove_nan = row.dropna()[2:]
            for restype in subnotestitle:
                goodpondrow = pdnotation.loc[restype]
                finalnote = 0
                for idx, row in remove_nan.iteritems():
                    resdict[idx] = row
                    finalnote += row * goodpondrow[idx]
                resdict[restype] = finalnote

                if "longueur" in resdict.keys():
                    resdict[restype + "_l"] = finalnote / resdict["longueur"]
            finalfd = finalfd.append(resdict, ignore_index=True)

        pprint.pprint(finalfd)
        return finalfd

    def getComputeNotationCsvFile(self, conffile, itvpks):
        dataframeres = self.computeNotation(conffile, itvpks)
        self.getCsvFile(dataframeres)

    def readITVs(self, itvfiles):
        if not isinstance(itvfiles, list):
            itvfiles = [itvfiles]
        # self.dlg.progress.show()
        # Affichage d'une barre de message
        # type de barre : pushCritical, pushInfo, pushSuccess, pushWarning
        # msgbar = self.iface.messageBar()
        # msgbar.pushMessage(u"Geo Inspection : ", u"Démarrage du traitement.", Qgis.Info,1)

        # ******************************************************************************************************************************************************
        # Dépouillement des CSV/TXT
        # ******************************************************************************************************************************************************

        # Définition du nombre total de rapports ITV à traiter
        # total = self.dlg.selection.count()
        # countfile = 0

        # Recuperer l arborescence du dossier temporaire
        # self.dossier_temp = tempfile.gettempdir()

        # Création d'un CSV output
        # date = QDate().currentDate().toString('yyyy/MM/dd') # date forme us
        # date = date.replace(u"/", u"")
        # heure = QTime().currentTime().toString('hh:mm:ss') # heure:minutes:secondes
        # heure = heure.replace(u":", u"")
        # t_output = str(self.dossier_temp+"\\rapport_ITV_"+date+"_"+heure+".csv")

        # Ouvrir le CSV output en ecriture
        # t_export_result = codecs.open(t_output, "w", encoding="utf-8")
        # t_export_result.writelines("AAD;AAF;AAB;AAK;AAJ;AAN;AAQ;AAL;ABF;ABH;var_entreprise;ABA;ABE;ABP;ACM;ACA;ACB;ACD;ACH;ACI;ACJ;ACK;ADA;ADC;var_encode"+"\n")
        # t_export_result.writelines(
        #     u"id;regard_1;regard_2;reg_depart;sens;adresse;ville;foncier;emplacemnt;date_ins;nom_ins;entreprise;norme;methode;objet;nettoyage;forme;hauteur;materiau;prof_reg_1;prof_reg_2;type;utilisat;precipit;debit;encodage;dist_reg_1;code;carac_1;carac_2;remarque"
        #     + u"\n"
        # )

        var_entreprise = "Artelia"
        idline = 1

        resdataframe = pd.DataFrame(columns=list(ITVCOLUMNS.keys()))

        # print(resdataframe)
        # return

        # Boucle sur le(s) fichier(s) à traiter
        # while countfile <= total-1:
        for itvfile in itvfiles:
            logging.getLogger("Lamia_itvcore").debug("file : %s", itvfile)
            # Déclaration de valeurs par défaut de variables
            step1 = 0
            step2 = 0
            step3 = 0
            step4 = 0
            step5 = 0
            step6 = 0
            iAAB = 9999
            iAAD = 9999
            iAAF = 9999
            iAAJ = 9999
            iAAK = 9999
            iAAL = 9999
            iAAN = 9999
            iAAQ = 9999
            iABE = 9999
            iABF = 9999
            iABH = 9999
            iABP = 9999
            iABA = 9999
            iACM = 9999
            iACA = 9999
            iACB = 9999
            iACD = 9999
            iACH = 9999
            iACI = 9999
            iACJ = 9999
            iACK = 9999
            iADA = 9999
            iADC = 9999
            iI = 9999
            iA = 9999
            iB = 9999
            iC = 9999
            iF = 9999

            countline = 0
            # QMessageBox.warning(None, u"Attention", self.dlg.selection.item(countfile).text(), QMessageBox.Ok)
            # Ouverture du fichier courant à traiter
            # file = codecs.open(self.dlg.selection.item(countfile).text(), "r", encoding = 'latin-1')
            # itvfileread = codecs.open(itvfile, "r", encoding="latin-1")

            with open(itvfile, "r", encoding="latin-1") as myfile:
                # datas=myfile.readlines()

                # Boucle sur le(s) ligne(s) à traiter
                for line in myfile.readlines():
                    if line[:2] == "#Z":
                        step5 = 0
                        step6 = 1
                        iI = 9999
                        iA = 9999
                        iB = 9999
                        iC = 9999
                        iF = 9999

                    if step1 == 1:
                        col = line.split(";")
                        if iAAB != 9999:
                            AAB = col[iAAB].replace('"', "").strip()
                        else:
                            AAB = ""
                        if iAAD != 9999:
                            AAD = col[iAAD].replace('"', "").strip()
                        else:
                            AAD = ""
                        if iAAF != 9999:
                            AAF = col[iAAF].replace('"', "").strip()
                        else:
                            AAF = ""
                        if iAAJ != 9999:
                            AAJ = col[iAAJ].replace('"', "").strip()
                        else:
                            AAJ = ""
                        if iAAK != 9999:
                            AAK = col[iAAK].replace('"', "").strip()
                        else:
                            AAK = ""
                        if iAAL != 9999:
                            AAL = col[iAAL].replace('"', "").strip()
                        else:
                            AAL = ""
                        if iAAN != 9999:
                            AAN = col[iAAN].replace('"', "").strip()
                        else:
                            AAN = ""
                        if iAAQ != 9999:
                            AAQ = col[iAAQ].replace('"', "").strip()
                        else:
                            AAQ = ""
                        step1 = 0
                        iAAB = 9999
                        iAAD = 9999
                        iAAF = 9999
                        iAAJ = 9999
                        iAAK = 9999
                        iAAL = 9999
                        iAAN = 9999
                        iAAQ = 9999
                    if step2 == 1:
                        col = line.split(";")
                        if iABE != 9999:
                            ABE = col[iABE].replace('"', "").strip()
                        else:
                            ABE = ""
                        if iABF != 9999:
                            ABF = col[iABF].replace('"', "").strip()
                        else:
                            ABF = ""
                        if iABH != 9999:
                            ABH = col[iABH].replace('"', "").strip()
                        else:
                            ABH = ""
                        if iABP != 9999:
                            ABP = col[iABP].replace('"', "").strip()
                        else:
                            ABP = ""
                        if iABA != 9999:
                            ABA = col[iABA].replace('"', "").strip()
                        else:
                            ABA = ""
                        step2 = 0
                        iABE = 9999
                        iABF = 9999
                        iABH = 9999
                        iABP = 9999
                        iABA = 9999
                    if step3 == 1:
                        col = line.split(";")
                        if iACM != 9999:
                            ACM = col[iACM].replace('"', "").strip()
                        else:
                            ACM = ""
                        if iACA != 9999:
                            ACA = col[iACA].replace('"', "").strip()
                        else:
                            ACA = ""
                        if iACB != 9999:
                            ACB = col[iACB].replace('"', "").strip()
                        else:
                            ACB = ""
                        if iACD != 9999:
                            ACD = col[iACD].replace('"', "").strip()
                        else:
                            ACD = ""
                        if iACH != 9999:
                            ACH = col[iACH].replace('"', "").strip()
                        else:
                            ACH = ""
                        if iACI != 9999:
                            ACI = col[iACI].replace('"', "").strip()
                        else:
                            ACI = ""
                        if iACJ != 9999:
                            ACJ = col[iACJ].replace('"', "").strip()
                        else:
                            ACJ = ""
                        if iACK != 9999:
                            ACK = col[iACK].replace('"', "").strip()
                        else:
                            ACK = ""
                        step3 = 0
                        iACM = 9999
                        iACA = 9999
                        iACB = 9999
                        iACD = 9999
                        iACH = 9999
                        iACI = 9999
                        iACJ = 9999
                        iACK = 9999
                    if step4 == 1:
                        col = line.split(";")
                        if iADA != 9999:
                            ADA = col[iADA].replace('"', "").strip()
                        else:
                            ADA = ""
                        if iADC != 9999:
                            ADC = col[iADC].replace('"', "").strip()
                        else:
                            ADC = ""
                        step4 = 0
                        iADA = 9999
                        iADC = 9999
                    if step5 == 1:
                        col = line.split(";")
                        if iI != 9999:
                            I = col[iI].replace('"', "").strip()
                        else:
                            I = ""
                        if iA != 9999:
                            A = col[iA].replace('"', "").strip()
                        else:
                            A = ""
                        if iB != 9999:
                            B = col[iB].replace('"', "").strip()
                        else:
                            B = ""
                        if iC != 9999:
                            C = col[iC].replace('"', "").strip()
                        else:
                            C = ""
                        if iF != 9999:
                            F = col[iF].replace('"', "").strip()
                        else:
                            F = ""

                        newrow = [
                            idline,
                            AAD,
                            AAF,
                            AAB,
                            AAK,
                            AAJ,
                            AAN,
                            AAQ,
                            AAL,
                            ABF,
                            ABH,
                            var_entreprise,
                            ABA,
                            ABE,
                            ABP,
                            ACM,
                            ACA,
                            ACB,
                            ACD,
                            ACH,
                            ACI,
                            ACJ,
                            ACK,
                            ADA,
                            ADC,
                            var_encode,
                            I,
                            A,
                            B,
                            C,
                            F,
                        ]
                        """
                        newrow = (
                            str(idline)
                            + u";"
                            + AAD
                            + u";"
                            + AAF
                            + u";"
                            + AAB
                            + u";"
                            + AAK
                            + u";"
                            + AAJ
                            + u";"
                            + AAN
                            + u";"
                            + AAQ
                            + u";"
                            + AAL
                            + u";"
                            + ABF
                            + u";"
                            + ABH
                            + u";"
                            + var_entreprise
                            + u";"
                            + ABA
                            + u";"
                            + ABE
                            + u";"
                            + ABP
                            + u";"
                            + ACM
                            + u";"
                            + ACA
                            + u";"
                            + ACB
                            + u";"
                            + ACD
                            + u";"
                            + ACH
                            + u";"
                            + ACI
                            + u";"
                            + ACJ
                            + u";"
                            + ACK
                            + u";"
                            + ADA
                            + u";"
                            + ADC
                            + u";"
                            + var_encode
                            + u";"
                            + I
                            + u";"
                            + A
                            + u";"
                            + B
                            + u";"
                            + C
                            + u";"
                            + F
                            + u";"
                            + u"\n"
                        )
                        """
                        # QMessageBox.warning(None, u"Attention", str(newrow), QMessageBox.Ok)
                        # t_export_result.writelines(newrow)
                        # logging.getLogger("Lamia_itvcore").debug(
                        #     "row : %s", str(newrow.split(";"))
                        # )
                        # logging.getLogger("Lamia_itvcore").debug(
                        #     "row : %s", str(ITVCOLUMNS)
                        # )
                        # logging.getLogger("Lamia_itvcore").debug(
                        #     "row : %s %s", len(newrow.split(";")), len(ITVCOLUMNS)
                        # )

                        newr = pd.DataFrame([newrow], columns=list(ITVCOLUMNS.keys()))
                        # logging.getLogger("Lamia_itvcore").debug(
                        #     "dede : %s", str(newr.values.tolist())
                        # )
                        resdataframe = resdataframe.append(newr)
                        # logging.getLogger("Lamia_itvcore").debug(
                        #     "row : %s", str(resdataframe.values.tolist())
                        # )
                        # return
                        idline = idline + 1

                    if line[:4] == "#A1=":
                        var_encode = line[4:].replace("\n", "").strip()
                    if line[:5] == "#B01=":
                        step1 = 1
                        line = line.replace("#B01=", "")
                        col = line.split(";")
                        index = 0
                        for c in col:
                            if c == "AAB":
                                iAAB = index
                            if c == "AAD":
                                iAAD = index
                            if c == "AAF":
                                iAAF = index
                            if c == "AAJ":
                                iAAJ = index
                            if c == "AAK":
                                iAAK = index
                            if c == "AAL":
                                iAAL = index
                            if c == "AAN":
                                iAAN = index
                            if c == "AAQ":
                                iAAQ = index
                            index = index + 1
                    if line[:5] == "#B02=":
                        step2 = 1
                        line = line.replace("#B02=", "")
                        col = line.split(";")
                        index = 0
                        for c in col:
                            if c == "ABE":
                                iABE = index
                            if c == "ABF":
                                iABF = index
                            if c == "ABH":
                                iABH = index
                            if c == "ABP":
                                iABP = index
                            if c == "ABA":
                                iABA = index
                            index = index + 1
                    if line[:5] == "#B03=":
                        step3 = 1
                        line = line.replace("#B03=", "")
                        col = line.split(";")
                        index = 0
                        for c in col:
                            if c == "ACM":
                                iACM = index
                            if c == "ACA":
                                iACA = index
                            if c == "ACB":
                                iACB = index
                            if c == "ACD":
                                iACD = index
                            if c == "ACH":
                                iACH = index
                            if c == "ACI":
                                iACI = index
                            if c == "ACJ":
                                iACJ = index
                            if c == "ACK":
                                iACK = index
                            index = index + 1
                    if line[:5] == "#B04=":
                        step4 = 1
                        line = line.replace("#B04=", "")
                        col = line.split(";")
                        index = 0
                        for c in col:
                            if c == "ADA":
                                iADA = index
                            if c == "ADC":
                                iADC = index
                            index = index + 1
                    if line[:3] == "#C=":
                        step5 = 1
                        line = line.replace("#C=", "")
                        col = line.split(";")
                        index = 0
                        for c in col:
                            if c == "I":
                                iI = index
                            if c == "A":
                                iA = index
                            if c == "B":
                                iB = index
                            if c == "C":
                                iC = index
                            if c == "F":
                                iF = index
                            index = index + 1

                    countline = countline + 1
                # QMessageBox.warning(None, u"Attention", str(countline)+u" lignes lues", QMessageBox.Ok)

                # itvfileread.close()

                # countfile = countfile + 1
                # avancement = ((countfile*100)/total)/10
                # self.dlg.progress.setProperty(u"value", avancement)

        # Stopper l edition du CSV output
        # t_export_result.close()

        # Affichage d'une barre de message
        # type de barre : pushCritical, pushInfo, pushSuccess, pushWarning
        # msgbar = self.iface.messageBar()
        # msgbar.pushMessage(u"Geo Inspection : ", u"Traitement du(es) rapport(s) ITV terminé.", Qgis.Info,1)

        #         "id",
        # "regard_1",
        # "regard_2",
        # "reg_depart",
        # for colname in ["id", "regard_1", "regard_2", "reg_depart"]:
        #     resdataframe[colname] = resdataframe[colname].astype(int)
        return resdataframe

    def checkNodesExistInLamia(self, itvfiles):
        resdataframe = self.readITVs(itvfiles)

        lamianodes = self.dbase.lamiaorm["node"]["lpk_revision_end IS NULL"]
        nodesdataframe = pd.DataFrame(
            lamianodes, columns=self.dbase.lamiaorm["node"].columns
        )

        itvids = set(resdataframe["reg_depart"].unique().astype(str).tolist())
        lamiaids = set(nodesdataframe["name"].astype(str))

        noidinlamia = itvids.difference(lamiaids)
        totalid = len(resdataframe["reg_depart"].unique())
        return noidinlamia, totalid

    def getITVCsvFile(self, itvfiles):
        dataframeres = self.readITVs(itvfiles)
        print(type(dataframeres))
        return self.getCsvFile(dataframeres)

    def getCsvFile(self, dataframeres, destdir=None):
        # dataframeres = self.readITVs(itvfiles)
        currentdate = (
            self.dbase.utils.getCurrentDateTime()
            .replace("-", "")
            .replace(":", "")
            .replace(" ", "")
        )

        if destdir:
            csvfile = os.path.join(destdir, f"itv_{currentdate}.csv")
            dataframeres.to_csv(csvfile, sep=";")
            return csvfile
        else:
            csvfile = tempfile.NamedTemporaryFile(
                prefix=f"itv_{currentdate}", suffix=".csv"
            )
            csvfile.close()
            # with csvfile as temp:
            #     print("*", temp.name)
            dataframeres.to_csv(os.path.normpath(csvfile.name), sep=";")
            return os.path.normpath(csvfile.name)

    def getQgsLayer(self, itvfiles):
        resdataframe = self.readITVs(itvfiles)
        for colmunname in ["reg_depart", "regard_1", "regard_2"]:
            resdataframe[colmunname] = resdataframe[colmunname].astype(str)

        # ******************************************************************************************************************************************************
        # Traitement GEO
        # ******************************************************************************************************************************************************

        total = 0
        countline = 0
        countadd = 0

        # file = codecs.open(t_output, "r", encoding="utf-8")
        # # Détermination du nombre de ligne dans le CSV à traiter
        # for line in file:
        #     total = total + 1

        # Création d'un SHP temporaire pour le stockage des points de défaut identifiés
        temp_layer = qgis.core.QgsVectorLayer(
            f"Point?crs=epsg:{self.dbase.crsnumber}", "localisation_ITV", "memory"
        )
        pr = temp_layer.dataProvider()
        # Entrer en mode édition
        temp_layer.startEditing()

        qgsfields = qgis.core.QgsFields()
        for fieldname, typefield in ITVCOLUMNS.items():
            if typefield == int:
                qgsfields.append(qgis.core.QgsField(fieldname, QtCore.QVariant.Int))
            elif typefield == str:
                qgsfields.append(qgis.core.QgsField(fieldname, QtCore.QVariant.String))
            elif typefield == float:
                qgsfields.append(qgis.core.QgsField(fieldname, QtCore.QVariant.Double))

        pr.addAttributes(qgsfields)
        """
        pr.addAttributes(
            [
                QgsField("id", QVariant.Int),
                QgsField("regard_1", QVariant.String),
                QgsField("regard_2", QVariant.String),
                QgsField("reg_depart", QVariant.String),
                QgsField("sens", QVariant.String),
                QgsField("adresse", QVariant.String),
                QgsField("ville", QVariant.String),
                QgsField("foncier", QVariant.String),
                QgsField("emplacemnt", QVariant.String),
                QgsField("date_ins", QVariant.String),
                QgsField("nom_ins", QVariant.String),
                QgsField("entreprise", QVariant.String),
                QgsField("norme", QVariant.String),
                QgsField("methode", QVariant.String),
                QgsField("objet", QVariant.String),
                QgsField("nettoyage", QVariant.String),
                QgsField("forme", QVariant.String),
                QgsField("hauteur", QVariant.Double),
                QgsField("materiau", QVariant.String),
                QgsField("prof_reg_1", QVariant.Double),
                QgsField("prof_reg_2", QVariant.Double),
                QgsField("type", QVariant.String),
                QgsField("utilisat", QVariant.String),
                QgsField("precipit", QVariant.String),
                QgsField("debit", QVariant.String),
                QgsField("encodage", QVariant.String),
                QgsField("dist_reg_1", QVariant.Double),
                QgsField("code", QVariant.String),
                QgsField("carac_1", QVariant.String),
                QgsField("carac_2", QVariant.String),
                QgsField("remarque", QVariant.String),
            ]
        )
        """

        # Détermination du crs en entrée et définition d'une transformation en cas de différence avec le crs de sortie en L93
        # input_crs = self.layer.crs()
        # output_crs = QgsCoordinateReferenceSystem(2154)
        # tr_crs = QgsCoordinateTransform(input_crs, output_crs, QgsProject.instance())

        # file = codecs.open(t_output, "r", encoding="utf-8")
        # # Boucle sur le(s) ligne(s) à traiter
        # for line in file:
        for index, row in resdataframe.iterrows():
            print(row.values.tolist())

            # col = line.split(";")
            # Détermination des regards de départ et d'arrivée
            # var_amont = col[3]
            # if col[1] == var_amont:
            #     var_aval = col[2]
            # elif col[2] == var_amont:
            #     var_aval = col[1]
            # else:
            #     var_aval = ""
            var_amont = row["reg_depart"]
            if row["regard_1"] == var_amont:
                var_aval = row["regard_2"]
            elif row["regard_2"] == var_amont:
                var_aval = row["regard_1"]
            else:
                var_aval = ""

            # Détermination des noms de champs dans le SHP réseau contenant les regards amont et aval de chaque tronçon
            # field_amont = '"' + self.dlg.amont.currentText() + '"'
            # field_aval = '"' + self.dlg.aval.currentText() + '"'

            nodeupstream = self.dbase.lamiaorm["node"][
                f"name = '{var_amont}' and lpk_revision_end IS NULL"
            ]
            nodedownstream = self.dbase.lamiaorm["node"][
                f"name = '{var_aval}' and lpk_revision_end IS NULL"
            ]

            if nodeupstream and nodedownstream:
                nodeupstream = nodeupstream[0]
                nodedownstream = nodedownstream[0]

                print(qgis.core.QgsGeometry.fromWkt(nodeupstream["geom"]).asPoint())

                edgegeom = qgis.core.QgsGeometry.fromPolylineXY(
                    [
                        qgis.core.QgsGeometry.fromWkt(nodeupstream["geom"]).asPoint(),
                        qgis.core.QgsGeometry.fromWkt(nodedownstream["geom"]).asPoint(),
                    ]
                )
                insert_feat = qgis.core.QgsFeature(qgsfields)
                insert_feat.setAttributes(row.values.tolist())

                dist = float(row["dist_reg_1"])
                insert_geom = edgegeom.interpolate(dist)
                insert_feat.setGeometry(insert_geom)

                pr.addFeatures([insert_feat])
                countadd = countadd + 1

            """
            # Pour tous les objets du SHP réseau, recherche du tronçon avec les regards correspondants à la ligne du CSV en cours de traitement
            for feature in self.layer.getFeatures():

                # MAJ LTA 20181214 - Faire en sorte de traiter les champs regards amont et aval du SHP de référence indifférement quelquesoit le format (str, int ou float)
                
                try:
                    val_shp_amont = str(int(feature[self.dlg.amont.currentText()]))
                except:
                    val_shp_amont = feature[self.dlg.amont.currentText()]

                try:
                    val_shp_aval = str(int(feature[self.dlg.aval.currentText()]))
                except:
                    val_shp_aval = feature[self.dlg.aval.currentText()]
                # FIN LTA 20181214

                if val_shp_amont == var_amont and val_shp_aval == var_aval:

                    dist = float(col[26])

                    if input_crs.authid() != output_crs.authid():
                        feature.geometry().transform(tr_crs)

                    insert_geom = feature.geometry().interpolate(dist)
                    insert_feat = QgsFeature()
                    insert_feat.setGeometry(insert_geom)
                    insert_feat.setAttributes(row.values.tolist())

                        # [
                        #     col[0],
                        #     col[1],
                        #     col[2],
                        #     col[3],
                        #     col[4],
                        #     col[5],
                        #     col[6],
                        #     col[7],
                        #     col[8],
                        #     col[9],
                        #     col[10],
                        #     col[11],
                        #     col[12],
                        #     col[13],
                        #     col[14],
                        #     col[15],
                        #     col[16],
                        #     col[17],
                        #     col[18],
                        #     col[19],
                        #     col[20],
                        #     col[21],
                        #     col[22],
                        #     col[23],
                        #     col[24],
                        #     col[25],
                        #     col[26],
                        #     col[27],
                        #     col[28],
                        #     col[29],
                        #     col[30],
                        # ]
                    # )

                    pr.addFeatures([insert_feat])
                    countadd = countadd + 1

                    break

                elif val_shp_amont == var_aval and val_shp_aval == var_amont:

                    dist = float(col[26])

                    if input_crs.authid() != output_crs.authid():
                        feature.geometry().transform(tr_crs)

                    # Inversion du sens de la géométrie courante
                    nodes = feature.geometry().asPolyline()
                    nodes.reverse()
                    invert_line = QgsGeometry.fromPolylineXY(nodes)

                    insert_geom = invert_line.interpolate(dist)
                    insert_feat = QgsFeature()
                    insert_feat.setGeometry(insert_geom)
                    insert_feat.setAttributes(
                        [
                            col[0],
                            col[1],
                            col[2],
                            col[3],
                            col[4],
                            col[5],
                            col[6],
                            col[7],
                            col[8],
                            col[9],
                            col[10],
                            col[11],
                            col[12],
                            col[13],
                            col[14],
                            col[15],
                            col[16],
                            col[17],
                            col[18],
                            col[19],
                            col[20],
                            col[21],
                            col[22],
                            col[23],
                            col[24],
                            col[25],
                            col[26],
                            col[27],
                            col[28],
                            col[29],
                            col[30],
                        ]
                    )

                    pr.addFeatures([insert_feat])
                    countadd = countadd + 1

                    break
            """
            countline = countline + 1
            # avancement = (((countline * 100) / total) * 0.9) + 10
            # self.dlg.progress.setProperty("value", avancement)

        path_file = os.path.join(os.path.dirname(Lamia.__file__), "config/base3_urbandrainage/lamiaITVimport/Anomalies_ITV.qml")
        temp_layer.loadNamedStyle(path_file)
        temp_layer.commitChanges()

        return temp_layer

        # file.close()

        # if countadd > 0:

        #     # Choisir un dossier de destination
        #     folder = ""
        #     folder = str(
        #         QFileDialog.getExistingDirectory(
        #             None, "Sélection du répertoire de destination"
        #         )
        #     )
        #     if folder != "":
        #         # Déplacer le CSV
        #         shutil.move(t_output, folder)
        #         # Exporter le SHP
        #         writer = QgsVectorFileWriter.writeAsVectorFormat(
        #             temp_layer,
        #             folder + "//localisation_ITV_" + date + "_" + heure + ".shp",
        #             "utf-8",
        #             temp_layer.crs(),
        #             "ESRI Shapefile",
        #         )
        #         # Ajouter SHP dans le canvas
        #         export_shp = QgsVectorLayer(
        #             folder + "//localisation_ITV_" + date + "_" + heure + ".shp",
        #             "localisation_ITV_" + date + "_" + heure,
        #             "ogr",
        #         )
        #         QgsProject.instance().addMapLayer(export_shp)
        #         # Ouvrir le CSV dans le mapcanvas
        #         export_table = QgsVectorLayer(
        #             folder + "//rapport_ITV_" + date + "_" + heure + ".csv",
        #             "rapport_ITV_" + date + "_" + heure,
        #             "ogr",
        #         )
        #         QgsProject.instance().addMapLayer(export_table)

        #         # Affichage d'une barre de message
        #         # type de barre : pushCritical, pushInfo, pushSuccess, pushWarning
        #         msgbar = self.iface.messageBar()
        #         msgbar.pushMessage(
        #             "Geo Inspection : ",
        #             "Le traitement s'est déroulé avec succès !",
        #             Qgis.Success,
        #             10,
        #         )
        #     else:
        #         # Ajouter SHP temp dans le canvas
        #         QgsProject.instance().addMapLayer(temp_layer)
        #         # Ouvrir le CSV temp dans le mapcanvas
        #         export_table = QgsVectorLayer(t_output, "rapport_ITV", "ogr")
        #         QgsProject.instance().addMapLayer(export_table)

        #         # Affichage d'une barre de message
        #         # type de barre : pushCritical, pushInfo, pushSuccess, pushWarning
        #         msgbar = self.iface.messageBar()
        #         msgbar.pushMessage(
        #             "Geo Inspection : ",
        #             "Le traitement s'est déroulé avec succès !",
        #             Qgis.Success,
        #             10,
        #         )
        #         msgbar = self.iface.messageBar()
        #         msgbar.pushMessage(
        #             "Geo Inspection : ",
        #             "Les couches en sortie sont temporaires et n'ont pas été enregistrées !",
        #             Qgis.Warning,
        #             3,
        #         )
        # else:
        #     # Affichage d'une barre de message
        #     # type de barre : pushCritical, pushInfo, pushSuccess, pushWarning
        #     msgbar = self.iface.messageBar()
        #     msgbar.pushMessage(
        #         "Geo Inspection : ",
        #         "L'exécution de l'outil a échoué, aucun fichier en sortie n'a été généré. Vérifier les données d'entrée ou le paramétrage de l'outil.",
        #         Qgis.Critical,
        #         10,
        #     )

        # self.dlg.company.setEnabled(False)
        # self.dlg.config.setEnabled(False)
        # self.dlg.shp.setEnabled(False)
        # self.dlg.addshp.setEnabled(False)
        # self.dlg.amont.setEnabled(False)
        # self.dlg.aval.setEnabled(False)
        # self.dlg.addfile.setEnabled(False)
        # self.dlg.clearfile.setEnabled(False)
        # self.dlg.selection.setEnabled(False)

        # self.dlg.exit.show()
        # self.dlg.exit.setEnabled(True)
        # self.dlg.ok.hide()
        # self.dlg.cancel.hide()

    def setQgsEgde(self, dataframe, itv_name):
        """create or update edges with rereau indicators values

        Args:
            dataframe with indications about regard, indicators, and localisation
        """

        # ******************************************************************************************************************************************************
        # Traitement GEO
        # ******************************************************************************************************************************************************

        indicators_list = []
        # result_df = pd.DataFrame(index=dataframe.index, columns=["id_edge"])
        for indicator in all_exfiltration_indicators.keys():
            indicators_list.append('score_' + indicator)
            indicators_list.append('result_' + indicator)
            # result_df[indicator] = np.nan
        for indicator in all_infiltration_indicators:
            indicators_list.append('score_' + indicator)
            indicators_list.append('result_' + indicator)
            # result_df[indicator] = np.nan
        for indicator in all_ensablement_indicators:
            indicators_list.append('score_' + indicator)
            indicators_list.append('result_' + indicator)
            # result_df[indicator] = np.nan
        for indicator in all_red_cap_hyfraulique_indicators:
            indicators_list.append('score_' + indicator)
            indicators_list.append('result_' + indicator)
            # result_df[indicator] = np.nan

        # create qgis layer to put ITV result
        temp_layer = qgis.core.QgsVectorLayer(
            f"NoGeometry?crs=epsg:{self.dbase.crsnumber}", itv_name, "memory"
        )

        pr = temp_layer.dataProvider()

        # open editing mode
        temp_layer.startEditing()

        qgsfields = qgis.core.QgsFields()

        qgsfields.append(qgis.core.QgsField("id_edge", QtCore.QVariant.String))
        for ind in indicators_list:
            qgsfields.append(qgis.core.QgsField(ind, QtCore.QVariant.Double))
        pr.addAttributes(qgsfields)


        edges = self.getAllEdges()
        # for each edges in dataframe,
        for i, row in dataframe.iterrows():
            edge_is_find = 0
            insert_feat = qgis.core.QgsFeature(qgsfields)
            element_list = []
            # we look for asociated points,
            for id_edge, id_reg_1, id_reg_2 in edges:

                # if we find the edge, we add informations
                if (str(row["k_reg_1"]) == id_reg_1 and str(row["k_reg_2"]) == id_reg_2) or (str(row["k_reg_1"]) == id_reg_2 and str(row["k_reg_2"]) == id_reg_1):
                    element_list.append(id_edge)
                    edge_is_find = 1
                    for ind in indicators_list:
                        ind_value = row[ind]
                        if row["length"] > 0:
                            element_list.append(ind_value)
                        else:
                            element_list.append(float(None))
                            self.dbase.lamiaorm['edge'].update(
                                pkedge,
                                {
                                    ind:ind_value
                                }
                            )
                    insert_feat.setAttributes(element_list)
                    pr.addFeatures([insert_feat])
                    break
            if edge_is_find == 0 and row["k_reg_1"] != np.nan and row["k_reg_2"] != np.nan:
                X1 = row["X1"]
                Y1 = row["Y1"]
                X2 = row["X2"]
                Y2 = row["Y2"]
                pkedge = self.dbase.lamiaorm['edge'].create()
                self.dbase.lamiaorm['edge'].update(
                    pkedge,
                    {
                        "lid_descriptionsystem_1":row["k_reg_1"],
                        "lid_descriptionsystem_2":row["k_reg_2"],
                        "geom":f"LINESTRING({X1} {Y1},{X2} {Y2})"
                    }
                )
                element_list.append(self.dbase.query(f'SELECT id_edge FROM edge_qgis WHERE pk_edge IS {pkedge}')[0][0])
                for ind in indicators_list:
                    ind_value = row[ind]
                    if row["length"] > 0:
                        element_list.append(ind_value)
                    else:
                        element_list.append(None)
                insert_feat.setAttributes(element_list)
                pr.addFeatures([insert_feat])

        temp_layer.commitChanges()

        return temp_layer


    def getUniquesValuesbyEdge(self, itvfiles):
        resdataframe = self.readITVs(itvfiles)

        #         "code": str,
        # "carac_1": str,
        # "carac_2": str,

        resdataframe["finalcode"] = (
            resdataframe["code"] + resdataframe["carac_1"] + resdataframe["carac_2"]
        )

        globaluniquecode = resdataframe["finalcode"].unique()
        sortedglobaluniquecode = sorted(globaluniquecode.tolist())
        sortedglobaluniquecode = ["regard_1", "regard_2"] + sortedglobaluniquecode
        finaldf = pd.DataFrame(columns=sortedglobaluniquecode)

        groupedname = (
            resdataframe[["regard_1", "regard_2"]]
            .groupby(["regard_1", "regard_2"])
            .size()
            .reset_index()
        )

        # inspect reverse edge

        reversegroupedname = (
            resdataframe[["regard_1", "regard_2"]]
            .groupby(["regard_2", "regard_1"])
            .size()
            .reset_index()
        )

        setgroupedname = set(
            tuple(x) for x in groupedname[["regard_1", "regard_2"]].values.tolist()
        )
        setreversegroupedname = set(
            tuple(x) for x in groupedname[["regard_2", "regard_1"]].values.tolist()
        )
        intersectingedge = setgroupedname.intersection(setreversegroupedname)
        for intersec in intersectingedge:
            rowmaindf = resdataframe[
                (resdataframe["regard_1"] == intersec[1])
                & (resdataframe["regard_2"] == intersec[0])
            ]
            for idx, row in rowmaindf.iterrows():
                print(resdataframe.iloc[idx])

        for idx, row in groupedname.iterrows():
            # print(row["regard_1"])
            rowmaindf = resdataframe[
                (resdataframe["regard_1"] == row["regard_1"])
                & (resdataframe["regard_2"] == row["regard_2"])
            ]

            valcount = rowmaindf["finalcode"].value_counts()
            residx = valcount.index.tolist()
            residx = ["regard_1", "regard_2"] + residx
            resval = valcount.values.tolist()
            resval = [row["regard_1"], row["regard_2"]] + resval

            res = dict(zip(residx, resval))
            finaldf = finaldf.append(res, ignore_index=True)

        return finaldf

    def getAllPoints(self):
        """return for all Points : name, id_point, x coordinate, y coordinates
        """
        nodes = self.dbase.query('SELECT name, id_descriptionsystem, ST_X(geom), ST_Y(geom) FROM node_qgis WHERE lpk_revision_end IS NULL')
        return nodes

    def getAllEdges(self):
        """return for all Edges : id_edge, id_point_1, id_point_2
        """
        edges = self.dbase.query('SELECT id_edge, lid_descriptionsystem_1, lid_descriptionsystem_2 FROM edge_qgis WHERE lpk_revision_end IS NULL')
        return edges

    def computeOneIndicator(self, result_df, indicator, alpha, P, dict_of_indictors):
        """return result_df with a new column indicator, with the grade of the edge for that indicator
        """
        result_df[indicator] = 0.
        for col in result_df.columns:
            # if a defaut is in this indicator and in this edge:
            if col in dict_of_indictors[indicator].keys():
                # if it depends of P:
                if dict_of_indictors[indicator][col][1] is "P":
                    # if it is not a treshold
                    if type(dict_of_indictors[indicator][col][0]) == type(1):
                        result_df[indicator] = result_df[indicator].values + result_df[col].values * (alpha ** dict_of_indictors[indicator][col][0]) * P
                    else:
                        under_limit = 0.
                        for treshold in dict_of_indictors[indicator][col][0]:
                            result_df[indicator][np.logical_and(under_limit <= result_df[indicator].values, result_df[indicator].values < treshold[0])] = result_df[indicator][np.logical_and(under_limit <= result_df[indicator].values, result_df[indicator].values < treshold[0])].values + result_df[col][np.logical_and(under_limit <= result_df[indicator].values, result_df[indicator].values < treshold[0])].values * (alpha ** treshold[1]) * P
                            under_limit = treshold[0]
                # if depend of observated length:
                elif dict_of_indictors[indicator][col][1] is "L":
                    if type(dict_of_indictors[indicator][col][0]) == type(1):
                        result_df[indicator] = result_df[indicator].values + result_df[col].values * (alpha ** dict_of_indictors[indicator][col][0])
                    else:
                        under_limit = 0.
                        for treshold in dict_of_indictors[indicator][col][0]:
                            result_df[indicator][np.logical_and(under_limit <= result_df[indicator].values, result_df[indicator].values < treshold[0])] = result_df[indicator][np.logical_and(under_limit <= result_df[indicator].values, result_df[indicator].values < treshold[0])].values + result_df[col][np.logical_and(under_limit <= result_df[indicator].values, result_df[indicator].values < treshold[0])].values * (alpha ** treshold[1])
                            under_limit = treshold[0]
        # we divide total score by total length of the edge
        result_df['score_' + indicator] = result_df[indicator] / result_df["length"]
        result_df['result_' + indicator] = result_df[indicator] / result_df["length"]
        threshold_result = [1., 2., 3., 4.]
        if indicator in ["EXF4", "INF4"]:
            for i, treshold in enumerate([0., 0.5, 2., 7.]):
                result_df.loc[result_df['result_' + indicator] >= treshold, 'score_' + indicator] = threshold_result[i]
        elif indicator in ["HYD3", "ENS4"]:
            for i, treshold in enumerate([0., 1., 4., 14.]):
                result_df.loc[result_df['result_' + indicator] >= treshold, 'score_' + indicator] = threshold_result[i]
        result_df.drop(indicator, axis='columns', inplace=True)
        return result_df

    def computeIndicators(self, pks, alpha=2, P=5, itv_name="ITV"):
        """compute all available indicators on those edge

        Args:
            pks (list): [itv path]
            alpha (int, optional). Defaults to 2.
            P (int, optional):. Defaults to 5.

        Returns:
            dataframe (DataFrame): [itv files with indicator grades]
        """
        # take for all nodes name, id, and coordinates
        nodes = self.getAllPoints()
        # ETL for itv
        dataframe = self.getUniquesValuesbyEdge(pks)
        dataframe["k_reg_1"] = ""
        dataframe["k_reg_2"] = ""
        dataframe["X1"] = np.nan
        dataframe["Y1"] = np.nan
        dataframe["X2"] = np.nan
        dataframe["Y2"] = np.nan
        # find points in nodes and compute length of the edge
        for i, row in dataframe.iterrows():
            for name, id_point, X, Y in nodes:
                if str(row["regard_1"]) == name:
                    dataframe["k_reg_1"][i] = id_point
                    dataframe["X1"][i] = X
                    dataframe["Y1"][i] = Y
                elif str(row["regard_2"]) == name:
                    dataframe["k_reg_2"][i] = id_point
                    dataframe["X2"][i] = X
                    dataframe["Y2"][i] = Y
                if dataframe["k_reg_1"][i] != "" and dataframe["k_reg_2"][i] != "":
                    break
        dataframe["length"] = ((dataframe["X1"] - dataframe["X2"]) ** 2 + (dataframe["Y1"] - dataframe["Y2"]) ** 2) ** 0.5
        dataframe = dataframe.fillna(0)
        # add one column for each indicator
        for indicator in all_exfiltration_indicators.keys():
            dataframe = self.computeOneIndicator(dataframe, indicator, alpha, P, all_exfiltration_indicators)
        for indicator in all_infiltration_indicators:
            dataframe = self.computeOneIndicator(dataframe, indicator, alpha, P, all_infiltration_indicators)
        for indicator in all_ensablement_indicators:
            dataframe = self.computeOneIndicator(dataframe, indicator, alpha, P, all_ensablement_indicators)
        for indicator in all_red_cap_hyfraulique_indicators:
            dataframe = self.computeOneIndicator(dataframe, indicator, alpha, P, all_red_cap_hyfraulique_indicators)
        return self.setQgsEgde(dataframe, itv_name)
