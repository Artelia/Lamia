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

import os, inspect, datetime
from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import QWidget

from Lamia.api.libslamia.lamiareport.lamiareport import ReportCore

from ...base3.qgswidgets.lamia_form_deficiency import BaseDeficiencyTool
from .lamia_form_observation import BaseConstructionsiteObservationTool
from .lamia_form_delivery import BaseConstructionsiteDeliveryTool

# from .lamiabasechantier_lidchooser import LidChooserWidget
from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_lidchooser import (
    LidChooserWidget,
)
from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_tcmanytomany import (
    TcmanytomanyChooserWidget,
)


class BaseConstructionsiteDeficiencyTool(BaseDeficiencyTool):

    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate(
        "base3_cs", "Non-compliance"
    )

    def __init__(self, **kwargs):
        super(BaseConstructionsiteDeficiencyTool, self).__init__(**kwargs)
        # nclist : [...[displayname, observationcategory,signing  ]...]
        self.nclist = [
            # ['Généralités',None,False],
            [QtCore.QCoreApplication.translate("base3_cs", "Description"), "NCA", True],
            [
                QtCore.QCoreApplication.translate("base3_cs", "Proposal\nnotice"),
                "NCB",
                True,
            ],
            [QtCore.QCoreApplication.translate("base3_cs", "Checking"), "NCC", True],
            [
                QtCore.QCoreApplication.translate("base3_cs", "Reservation\nremoval"),
                "NCD",
                True,
            ],
            [
                QtCore.QCoreApplication.translate("base3_cs", "Recherche\ndes causes"),
                "NCE",
                False,
            ],
        ]

        self.iconinterv1 = QtGui.QIcon(
            os.path.join(os.path.dirname(__file__), "interv1.png")
        )
        self.iconinterv2 = QtGui.QIcon(
            os.path.join(os.path.dirname(__file__), "interv1.png")
        )
        self.iconinterv3 = QtGui.QIcon(
            os.path.join(os.path.dirname(__file__), "interv3.png")
        )

    def initMainToolWidget(self):

        if self.dbase.variante in [None, "Lamia"]:

            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {
                "deficiency": {
                    "linkfield": "id_deficiency",
                    "widgets": {
                        #'groupedesordre': self.toolwidgetmain.comboBox_groupedes,
                        "deficiencyobservatortype": self.toolwidgetmain.comboBox_detecteur,
                        # 'detecteur_com': self.toolwidgetmain.lineEdit_detecteur,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.lineEdit_detecteur,},
                },
            }

            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
            self.TABLEFILTERFIELD = {"deficiencycategory": "NCO"}

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self
            self.lamiawidgets = []

            for i, (displayname, observationcategory, signing) in enumerate(
                self.nclist
            ):
                # print(i, displayname, typeobservation,signing)
                varname = "self.propertieswdgOBSERVATION{}".format(observationcategory)
                temppropertieswdgOBSERVATION = BaseConstructionsiteObservationTool(
                    **self.instancekwargs
                )
                temppropertieswdgOBSERVATION.TABLEFILTERFIELD = {
                    "observationcategory": observationcategory
                }
                temppropertieswdgOBSERVATION.tooltreewidgetSUBCAT = displayname
                exec(
                    "self.propertieswdgOBSERVATION{} = temppropertieswdgOBSERVATION".format(
                        observationcategory
                    )
                )
                exec(
                    "self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION{} )".format(
                        observationcategory
                    )
                )

            self.tcsubwidget = TcmanytomanyChooserWidget(
                parentwdg=self,
                tcmanytomanyname="tcdeliveryobject",
                childtablename="delivery",
                parentmanytomanyfield="id_object",
                childmanytomanyfield="id_delivery",
                childdisplayfields=["id_delivery", "name"],
                tcmanytomanydisplayfields=[],
                parentframe=self.toolwidgetmain.frame_numarche,
            )

            self.lamiawidgets.append(self.tcsubwidget)
        elif self.dbase.variante in ["Orange"]:
            self.toolwidgetmain = UserUI_Orange()
            self.formtoolwidgetconfdictmain = {
                "deficiency": {
                    "linkfield": "id_deficiency",
                    "widgets": {
                        #'groupedesordre': self.toolwidgetmain.comboBox_groupedes,
                        "sector1": self.toolwidgetmain.lineEdit_commune,
                        "sector2": self.toolwidgetmain.lineEdit_rue,
                        "sector3": self.toolwidgetmain.comboBox_zasro,
                        # 'datedebuttravaux': self.toolwidgetmain.dateEdit_debuttrav,
                        # 'datefincontractuelle': self.toolwidgetmain.dateEdit_fintrav,
                    },
                },
                "object": {"linkfield": "id_object", "widgets": {}},
            }

            self.TABLEFILTERFIELD = {"deficiencycategory": "CON"}

            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self
            self.lamiawidgets = []

            self.propertieswdgDelivery = BaseConstructionsiteDeliveryTool(
                **self.instancekwargs
            )
            self.propertieswdgDelivery.TABLEFILTERFIELD = {"deliverycategory": "WOR"}
            self.dbasechildwdgfield.append(self.propertieswdgDelivery)

            for i, (displayname, observationcategory, signing) in enumerate(
                self.nclist
            ):
                temppropertieswdgOBSERVATION = BaseConstructionsiteObservationTool(
                    **self.instancekwargs
                )
                temppropertieswdgOBSERVATION.TABLEFILTERFIELD = {
                    "observationcategory": observationcategory
                }
                temppropertieswdgOBSERVATION.tooltreewidgetSUBCAT = displayname
                exec(
                    "self.propertieswdgOBSERVATION{} = temppropertieswdgOBSERVATION".format(
                        observationcategory
                    )
                )
                exec(
                    "self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION{} )".format(
                        observationcategory
                    )
                )

    def magicFunction(self):
        self.featureSelected()
        self.addGPSPoint()
        self.saveFeature()
        for wdgobservation in self.dbasechildwdgfield:
            if hasattr(wdgobservation, "OBSTYPE") and wdgobservation.OBSTYPE == "NCA":
                wdgobservation.featureSelected()
                wdgobservation.saveFeature()

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super().postSelectFeature()

        self.updateListSymbols()

        # if self.currentFeaturePK is None:
        #     #self.toolwidgetmain.listWidget_nonconf.setCurrentRow(0)

        #     if self.dbase.variante in ['Orange']:
        #         datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        #         self.formutils.applyResultDict({'datedebuttravaux' : datecreation},checkifinforgottenfield=False)
        #         self.formutils.applyResultDict({'datefincontractuelle' : datecreation},checkifinforgottenfield=False)

    def itemChangedNonConformite(self, itemcurrent, itemprevious):
        currentrow = self.toolwidgetmain.listWidget_nonconf.row(itemcurrent)
        if currentrow == 0:
            self.toolwidgetmain.stackedWidget_nonconf.setCurrentIndex(0)
        else:
            self.toolwidgetmain.stackedWidget_nonconf.setCurrentIndex(1)
            obstype = self.nclist[currentrow][1]
            signaturebool = self.nclist[currentrow][2]
            self.propertieswdgOBSERVATION.setOBSTYPE(obstype, signaturebool)

            self.currentFeatureChanged.emit()
            self.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_2.setCurrentIndex(
                currentrow - 1
            )

    def updateListSymbols(self):
        # for i, elem in enumerate(self.nclist):
        for i, (itemname, observationcategory, fieldsign) in enumerate(self.nclist):
            if fieldsign and self.currentFeaturePK is not None:
                exec(
                    "obswdg = self.propertieswdgOBSERVATION{} ".format(
                        observationcategory
                    ),
                    locals(),
                    globals(),
                )
                iddes = self.dbase.getValuesFromPk(
                    "deficiency", "id_deficiency", self.currentFeaturePK
                )
                signatureswdgs = [
                    wdg
                    for wdg in obswdg.lamiawidgets
                    if wdg.__class__.__name__ == "SignatureWidget"
                ]
                intervid = []
                for sigwdg in signatureswdgs:
                    intervid.append(sigwdg.intervenantid)
                if len(intervid) > 0:
                    obsname = obswdg.tooltreewidgetSUBCAT
                    goodtab = self.tabWidget.findChild(QWidget, obsname)
                    goodtabindex = self.tabWidget.indexOf(goodtab)
                    self.tabWidget.setTabIcon(goodtabindex, self.iconinterv1)

                    sql = (
                        "SELECT {} FROM observation WHERE observationcategory = '{}' "
                        " AND lid_deficiency = {} ".format(
                            ", ".join(intervid), observationcategory, iddes
                        )
                    )
                    res = self.dbase.query(sql)
                    if res:
                        test = [
                            re[0]
                            for re in res
                            if self.dbase.utils.isAttributeNull(re[0])
                        ]
                        if len(test) == 0:
                            self.tabWidget.setTabIcon(goodtabindex, self.iconinterv3)
                # self.tabWidget.repaint()

    def printWidget(self):

        # manage pdffile
        pdfdirectory = os.path.join(self.dbase.dbaseressourcesdirectory, "print")
        if not os.path.isdir(pdfdirectory):
            os.mkdir(pdfdirectory)

        currentid = self.dbase.getValuesFromPk(
            "deficiency", "id_deficiency", self.currentFeaturePK
        )
        date = str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
        filename = str(currentid) + "_desordre_" + date + ".pdf"
        pdffilename = os.path.join(pdfdirectory, filename)

        # manage wich report conf to choose
        # choose phaseA report or phase C report
        sql = (
            "SELECT observationcategory FROM  observation_now WHERE observation_now.lid_deficiency = "
            + str(currentid)
        )
        sql = self.dbase.sqlNow(sql)
        res = self.dbase.query(sql)

        if (
            res is not None
            and len(res) > 0
            and not self.dbase.utils.isAttributeNull(res[0][0])
        ):
            if res[0][0] == "PVA":
                reporttype = "procesverbalmiseadisposition"

            elif res[0][0][0:2] == "NC":
                # sql = "SELECT id_observation FROM observation_now WHERE observation_now.observationcategory = 'NCB'"
                # sql += " AND observation_now.lid_deficiency = " + str(currentid)
                # sql = self.dbase.updateQueryTableNow(sql)
                # res = self.dbase.query(sql)
                if self.dbase.variante in [None, "Lamia"]:
                    reporttype = "TRAMnonconformitephaseA"

                    # if res is not None and len(res) > 0 and not self.dbase.utils.isAttributeNull(res[0][0]):
                    #     # reporttype = 'TRAMnonconformite'
                    #     reporttype = 'TRAMnonconformitephaseA'
                    # else:
                    #     reporttype = 'TRAMnonconformitephaseA'
                elif self.dbase.variante in ["Orange"]:
                    # print('*********ORANGEnonconformitephaseA')
                    reporttype = "ORANGEnonconformitephaseA"

        else:
            return

        # run report
        self.reporttool = ReportCore(
            dbaseparser=self.dbase, messageinstance=self.mainifacewidget.connector
        )
        self.reporttool.runReport(
            destinationfile=pdffilename,
            reportconffilename=reporttype,
            pklist={0: [self.currentFeaturePK]},
        )


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_deficiency_ui.ui")
        uic.loadUi(uipath, self)


class UserUI_Orange(QWidget):
    def __init__(self, parent=None):
        super(UserUI_Orange, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_deficiency_orange_ui.ui"
        )
        uic.loadUi(uipath, self)
