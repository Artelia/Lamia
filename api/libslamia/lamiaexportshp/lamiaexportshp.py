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


import os, importlib
from collections import OrderedDict
import sys, glob, inspect, logging, textwrap
import Lamia
from ..abstractlibslamia import AbstractLibsLamia

import qgis
from qgis.PyQt import QtGui, uic, QtCore, QtXml


class ExportShapefileCore(AbstractLibsLamia):

    POSTPROTOOLNAME = "lamiaexportshp"
    SHOWSQL = False
    fileext = ".txt"

    def __init__(self, dbaseparser, messageinstance=None):
        super(ExportShapefileCore, self).__init__(dbaseparser, messageinstance)
        # super(ExportShapefileTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
        # self.dbase = dbaseparser
        # self.messageinstance = messageinstance
        # if self.dbase.base3version:
        #     self.tooldir = os.path.join(
        #         os.path.dirname(Lamia.__file__),
        #         "worktypeconf",
        #         self.dbase.worktype.lower(),
        #         "lamiaexportshp",
        #     )
        # else:
        #     self.tooldir = os.path.join(
        #         os.path.dirname(__file__), self.dbase.worktype.lower()
        #     )

        # self.confdataplugin = self.tooldir
        # self.confdataproject = os.path.join(
        #     self.dbase.dbaseressourcesdirectory, "config", self.POSTPROTOOLNAME
        # )

    def runExport(
        self,
        destinationshapefile,
        exportconffilepath,
        pkzonegeos=[],
        removeemptycolumns=True,
    ):

        debug = False
        tabletypepath = self.getConfFilePath(exportconffilepath)
        self.champs = self.readChamp(tabletypepath)

        self.fieldsforshp = self.buildQgsFields(self.champs)
        sql = self.buildSql(self.champs, pkzonegeos)

        if debug or self.SHOWSQL:
            logging.getLogger("Lamia").debug("sql %s", sql)

        query = self.dbase.query(sql)
        if query is None:
            return

        self.result = [list(row) for row in query]
        if debug:
            logging.getLogger("Lamia").debug("result %s", str(self.result))

        if self.dbase.base3version:
            strtoexec = f"Lamia.config.{self.dbase.worktype.lower()}.lamiaexportshp.lamiaexportshpworktypefunc"
        else:
            strtoexec = f"..{self.dbase.worktype.lower()}.lamiaexportshpworktypefunc"

        mymodule = importlib.import_module(strtoexec, package=self.__module__)
        mymodule.exportMethod(self)

        if debug:
            logging.getLogger("Lamia").debug("result post : %s", str(self.result))
        geomtype = qgis.core.QgsWkbTypes.NoGeometry
        for table in self.champs:
            if "main" == table["table"]:
                champmain = table["sql"]

        for table in self.champs:
            if "geom" in table["table"]:
                sqlgeom = table["fields"]["geom"]["value"]
                if "ST_AsText(" in sqlgeom:
                    geomval = sqlgeom.split("ST_AsText(")[1][:-1]
                else:
                    geomval = "geom"

                try:
                    sql = (
                        " SELECT ST_GeometryType(St_MakeValid("
                        + geomval
                        + ")) "
                        + champmain
                    )
                    sql = self.dbase.updateQueryTableNow(sql)
                    res = self.dbase.query(sql)[0][0]
                except (TypeError, IndexError) as e:
                    sql = " SELECT ST_GeometryType(" + geomval + ") " + champmain
                    sql = self.dbase.updateQueryTableNow(sql)
                    print(e)
                    res = self.dbase.query(sql)
                    if res:
                        res = res[0][0]

                if res == "LINESTRING":
                    geomtype = qgis.core.QgsWkbTypes.LineString
                elif res == "POINT":
                    geomtype = qgis.core.QgsWkbTypes.Point

        self.fillShapefile(
            destinationshapefile,
            geomtype,
            self.fieldsforshp,
            self.champs,
            self.result,
            removeemptycolumns,
        )

    def new(self, confpath):

        if not os.path.exists(self.confdataproject):
            os.mkdir(self.confdataproject)

        conf_file = open(confpath, "w", encoding="utf-8")
        conftxt = """
                    # les lignes de commentaires commencent par #
                    
                    # la requete sql créée est formée ainsi :
                    #   SELECT [enumération des valeursql]
                    #   FROM [requete ecrite dans le ###main]
                    
                    # Le choix des champs à selectionner pour l'export se fait ainsi :
                    # ex :
                    # ###Noeud 
                    # #nom              ;type (Int, Double, String);  cst (nom du champ pour convertion trigamme); valeursql                    
                    # id_noeud;          Int;                      ;               id_noeud
                    
                    # avec :
                    # ###Noeud : nom de la table utilisée par convertir les trigrammes vers valeur texte
                    # nom : le nom du champ dans le shp
                    # type : le type dans le shp  : Int, Double, String
                    # champ de convertion : le nom du champ pour la convertion du trigramme vers du texte
                    # valeursql : la valeur (en sql) à prendre : peut etre un champ de la table, ou une requete sql
                    
                    # Pour choisir la géométrie considérée pour le shp 
                    # ###geom
                    # geom;         Int;               ;                  ST_AsText(Noeud_now.geom)
                    
                    # Enfin décrirer la requete FROM ..
                    # ###main 
                    # FROM Noeud_now
                    
                    # ici la requete utilisée pour la création du shp est 
                    # SELECT id_noeud FROM Noeud_now 
                    
                    # ex :

                    ###Noeud 
                    #nom              ;type     ;champ de convertion trigramme ? ; valeursql
                    id_noeud         ; Int      ;                                ; id_noeud
                    
                    ###geom
                    geom;         Int;               ;                  ST_AsText(Noeud_now.geom)
                    
                    ###main 
                    FROM Noeud_now
                    """
        conf_file.write(textwrap.dedent(conftxt))
        conf_file.close()

    def readChamp(self, table):
        """

        :param table:
        :return: list : [           {'table' : tablename,
                                    {'sql' : lien sql
                                     {'fields' : ordereddic{... {fieldname : {type,
                                                                                cst,
                                                                                value}
                                                    ...]
        """

        debug = False

        champs = []
        filename = table

        file = open(filename, "r", encoding="utf-8")
        compt = 0
        actualtable = None
        for line in file:
            if len(line.strip()) == 0:
                continue
            if line[0:3] == "###":  # new field
                line = line[3:].strip()
                if debug:
                    logging.getLogger("Lamia").debug("fieldname %s", line)
                actualtable = line
                champs.append({})
                champs[-1]["table"] = actualtable
                champs[-1]["sql"] = ""
                champs[-1]["fields"] = OrderedDict()
            elif line[0:2] == "##":  # parent field constraint name
                champs[-1]["sql"] = [ssline.strip() for ssline in line[2:].split(";")]
            elif line[0] == "#":  # comment - pass
                continue
            else:  # field constraint
                if actualtable not in ["main", "with"]:
                    linesplit = line.split(";")
                    champs[-1]["fields"][linesplit[0].strip()] = {}
                    if linesplit[1].strip() != "":
                        champs[-1]["fields"][linesplit[0].strip()]["type"] = linesplit[
                            1
                        ].strip()
                    else:
                        champs[-1]["fields"][linesplit[0].strip()]["type"] = None
                    if linesplit[2].strip() != "":
                        champs[-1]["fields"][linesplit[0].strip()]["cst"] = linesplit[
                            2
                        ].strip()
                    else:
                        champs[-1]["fields"][linesplit[0].strip()]["cst"] = None
                    if linesplit[3].strip() != "":
                        champs[-1]["fields"][linesplit[0].strip()]["value"] = linesplit[
                            3
                        ].strip()
                    else:
                        champs[-1]["fields"][linesplit[0].strip()]["value"] = None

                    if len(linesplit) == 5 and linesplit[4].strip() != "":
                        champs[-1]["fields"][linesplit[0].strip()]["as"] = linesplit[
                            4
                        ].strip()
                    else:
                        champs[-1]["fields"][linesplit[0].strip()]["as"] = None
                else:
                    champs[-1]["sql"] += line.strip() + " "
            compt += 1

        file.close()
        return champs

    def testIfZonegeoPk(self, **kwargs):
        champs = kwargs.get("champs", None)
        champsfile = kwargs.get("champsfile", None)

        if champs is None and champsfile is not None:
            champs = self.readChamp(champsfile)
        pkzonegeoinchamps = False
        for dictchamp in champs:
            if "zonegeo" in dictchamp["table"].lower():
                if "pk_zonegeo" in dictchamp["fields"].keys():
                    pkzonegeoinchamps = True
                    break

        return pkzonegeoinchamps

    def buildSql(self, champs, pkzonegeos):

        debug = False

        sql = ""

        for i, table in enumerate(champs):
            if table["table"] in ["with"]:
                sql += champs["with"]

        sql += " SELECT "
        for table in champs:
            if table["table"] not in ["main", "with"]:
                for i, name in enumerate(table["fields"].keys()):
                    attr = table["fields"][name]
                    if attr["value"] is None:
                        sql += "NULL, "
                    else:
                        # if table["sql"] is None:
                        if not table["sql"]:
                            sql += attr["value"] + ", "
                        else:
                            sql += "( SELECT "
                            sql += attr["value"] + " "
                            sql += table["sql"][0]
                            if len(table["sql"]) > 1:
                                sql += " " + table["sql"][1]
                            sql += "), "
                    if table["fields"][name]["as"] is not None:
                        sql = sql[:-2] + " AS " + table["fields"][name]["as"] + ", "

        sql = sql[:-2]

        for i, table in enumerate(champs):
            if table["table"] in ["main"]:
                sql += " " + table["sql"]
                champmain = table

        if debug:
            logging.getLogger("Lamia").debug("sql before now : %s ", sql)
        sql = self.dbase.updateQueryTableNow(sql)
        if debug:
            logging.getLogger("Lamia").debug("sql after  now : %s ", sql)

        # export by zonegeo
        # boundinggeom = None
        if False:
            if (
                len(self.dbase.dbasetables["Zonegeo"]["layerqgis"].selectedFeatures())
                >= 1
            ):
                fetids = []
                currentfeats = self.dbase.dbasetables["Zonegeo"][
                    "layerqgis"
                ].selectedFeatures()
                for fet in currentfeats:
                    fetids.append(str(fet.id()))

                if "WHERE" in champmain["sql"]:
                    sql += " AND pk_zonegeo IN (" + ",".join(fetids) + ")"
                else:
                    sql += " WHERE pk_zonegeo IN (" + ",".join(fetids) + ")"

        if len(pkzonegeos) > 0 and self.testIfZonegeoPk(champs=champs):
            pkzonegeos_str = [str(pk) for pk in pkzonegeos]
            if "WHERE" in champmain["sql"]:
                sql += " AND pk_zonegeo IN (" + ",".join(pkzonegeos_str) + ")"
            else:
                sql += " WHERE pk_zonegeo IN (" + ",".join(pkzonegeos_str) + ")"

        return sql

    def buildQgsFields(self, champs):
        fields = qgis.core.QgsFields()
        for i, table in enumerate(champs):
            if table["table"] not in ["geom", "main", "with"]:
                for j, name in enumerate(table["fields"].keys()):
                    typefield = eval("QtCore.QVariant." + table["fields"][name]["type"])
                    if name in [field.name() for field in fields]:
                        self.messageinstance.showErrorMessage(
                            "ATTENTION Champ " + name + " deja utilise"
                        )
                        fields.append(qgis.core.QgsField(name + str(i), typefield))
                    else:
                        # typefield = eval("QtCore.QVariant." + table["fields"][name]["type"])
                        fields.append(qgis.core.QgsField(name, typefield))

        return fields

    def fillShapefile(
        self, filename, typegeom, fields, champs, result, removeemptycolumns
    ):

        debug = False

        dbaseqgiscrs = qgis.core.QgsCoordinateReferenceSystem()
        dbaseqgiscrs.createFromString("EPSG:" + str(self.dbase.crsnumber))

        writer = qgis.core.QgsVectorFileWriter(
            filename,
            "utf-8",
            fields,
            typegeom,
            # qgis.core.QGis.WKBPoint,
            # qgis.core.QGis.WKBLineString,
            dbaseqgiscrs,
            driverName="ESRI Shapefile",
        )

        for row in result:
            if debug:
                logging.getLogger("Lamia").debug("res %s", str(row))
            feat = qgis.core.QgsFeature(fields)

            if typegeom != qgis.core.QgsWkbTypes.NoGeometry:
                if row[-1] is not None:
                    feat.setGeometry(qgis.core.QgsGeometry.fromWkt(row[-1]))
                else:
                    continue

            compteur = -1
            for table in champs:
                if (
                    table["table"] not in ["geom", "main", "with"]
                    and "postpro" not in table["table"]
                ):
                    for i, name in enumerate(table["fields"].keys()):
                        compteur += 1
                        if table["fields"][name]["cst"] is not None:
                            csttext = self.dbase.getConstraintTextFromRawValue(
                                table["table"],
                                table["fields"][name]["cst"],
                                row[compteur],
                            )
                            if not self.dbase.utils.isAttributeNull(csttext):
                                feat[compteur] = csttext
                            else:
                                feat[compteur] = qgis.core.NULL
                        else:
                            feat[compteur] = row[compteur]
                elif "postpro" in table["table"]:
                    compteur += 1
                    feat[compteur] = row[compteur]

            if debug:
                logging.getLogger("Lamia").debug(
                    "fet %s -  %s", str(feat.id()), str(feat.attributes())
                )
            success = writer.addFeature(feat)

        del writer

        if removeemptycolumns:
            self.cleanShapefile(filename)

        if self.messageinstance is not None:
            self.messageinstance.showNormalMessage("Export termine")

    def cleanShapefile(self, filename):
        vl = qgis.core.QgsVectorLayer(filename, "cleaning", "ogr")
        coltoremove = []
        for i, field in enumerate(vl.fields()):
            uniquevalues = vl.uniqueValues(i)
            if self.dbase.utils.isAttributeNull(list(uniquevalues)[0]):
                coltoremove.append(i)
        vl.startEditing()
        res = vl.dataProvider().deleteAttributes(coltoremove)
        vl.updateFields()
        vl.commitChanges()

