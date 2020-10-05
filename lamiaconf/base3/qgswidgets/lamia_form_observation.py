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


import os
import datetime

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget

from Lamia.iface.qgiswidget.tools.lamia_abstractformtool import AbstractLamiaFormTool
from .lamia_form_camera import BaseCameraTool
from .lamia_form_sketch import BaseSketchTool

base3 = QtCore.QObject()


class BaseObservationTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "observation"
    DBASETABLENAME = "observation"
    # LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Condition")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Observation")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_observation_icon.png"
    )

    PARENTJOIN = {
        "deficiency": {
            "colparent": "id_deficiency",
            "colthistable": "lid_deficiency",
            "tctable": None,
            "tctablecolparent": None,
            "tctablecolthistable": None,
        }
    }
    # CHOOSERTREEWDG_COLSHOW
    CHOOSERTREEWDGSPEC = {
        "colshow": ["datetimeobservation"],
        "sort": ["datetimeobservation", "DESC"],
    }

    def __init__(self, **kwargs):
        super(BaseObservationTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "Observation": {
                "linkfield": "id_observation",
                "widgets": {
                    "datetimeobservation": self.toolwidgetmain.dateTimeEdit,
                    "number": self.toolwidgetmain.spinBox_nombre,
                    "gravity": self.toolwidgetmain.comboBox_urgence,
                    "progression": self.toolwidgetmain.textEdit_evolution,
                    "nextactiontype": self.toolwidgetmain.comboBox_typesuite,
                    "nextactioncomment": self.toolwidgetmain.textEdit_suite,
                },
            },
            "Objet": {
                "linkfield": "id_objet",
                "widgets": {"comment": self.toolwidgetmain.textEdit_comm},
            },
        }

        self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre)
        )

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        # if self.parentWidget is not None:
        self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
        self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    def postSelectFeature(self):

        if self.currentFeaturePK is None:

            if (
                self.parentWidget is not None
                and self.parentWidget.currentFeaturePK is not None
            ):  # copy last obs text
                iddesordre = self.dbase.getValuesFromPk(
                    "deficiency", "id_deficiency", self.parentWidget.currentFeaturePK
                )
                sql = (
                    "SELECT pk_observation FROM observation_now WHERE lid_deficiency = {iddesordre}"
                    " AND datetimeobservation = (SELECT MAX(datetimeobservation) FROM observation_now WHERE lid_deficiency = {iddesordre} )".format(
                        iddesordre=iddesordre
                    )
                )

                sql = self.dbase.sqlNow(sql)
                query = self.dbase.query(sql)
                if query:
                    result = [row[0] for row in query]
                    if len(result) > 0:
                        pklastobservation = result[0]
                        dictvalues = self.formutils.getDictValuesForWidget(
                            featurepk=pklastobservation
                        )
                        self.formutils.applyResultDict(dictvalues)

            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict(
                {"datetimeobservation": datecreation}, checkifinforgottenfield=False
            )

        if (
            "deficiencycategory"
            in self.dbase.dbasetables["deficiency"]["fields"].keys()
        ):
            if (
                self.parentWidget is not None
                and self.parentWidget.currentFeaturePK is not None
            ):
                grpdes = self.dbase.getValuesFromPk(
                    self.parentWidget.DBASETABLENAME,
                    "deficiencycategory",
                    self.parentWidget.currentFeaturePK,
                )
                if grpdes is not None:
                    grpdescst = [
                        elem[1]
                        for elem in self.dbase.dbasetables["deficiency"]["fields"][
                            "deficiencycategory"
                        ]["Cst"]
                    ]
                    indexgrp = grpdescst.index(grpdes)
                    try:
                        self.toolwidgetmain.stackedWidget.setCurrentIndex(indexgrp)
                    except:
                        pass

    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:


            # lastrevision = self.dbase.maxrevision
            # datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid) + "," + str(self.dbase.maxrevision) + ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')


        # idnoeud = self.currentFeature.id()
        pkobs = self.currentFeaturePK
        lastidobs = self.dbase.getLastId('Observation') + 1
        sql = "UPDATE Observation SET id_observation = " + str(lastidobs) + ","
        sql += "lpk_objet = " + str(pkobjet)
        sql += " WHERE pk_observation = " + str(pkobs) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:

            if self.parentWidget.dbasetablename == 'Desordre':
                #currentparentlinkfield = self.parentWidget.currentFeature['id_desordre']
                #parent iddesordre
                sql = " SELECT id_desordre FROM Desordre WHERE pk_desordre = " + str(self.parentWidget.currentFeaturePK)
                iddesordre = self.dbase.query(sql)[0][0]

                sql = "UPDATE Observation SET lid_desordre = " + str(iddesordre)
                sql += " WHERE pk_observation = " + str(self.currentFeaturePK)
                query = self.dbase.query(sql)
                self.dbase.commit()
    """

    def postSaveFeature(self, savedfeaturepk=None):
        if self.currentFeaturePK is None:  # new feature
            (
                pk_objet,
                datetimecreation,
                datetimeobservation,
            ) = self.dbase.getValuesFromPk(
                "observation_qgis",
                ["pk_object", "datetimecreation", "datetimeobservation"],
                savedfeaturepk,
            )
            if isinstance(datetimecreation, str):
                datetimecreation = datetime.datetime.strptime(
                    str(datetimecreation), "%Y-%m-%d %H:%M:%S"
                )
                datetimeobservation = datetime.datetime.strptime(
                    str(datetimeobservation), "%Y-%m-%d %H:%M:%S"
                )
            if datetimecreation > datetimeobservation:
                sql = (
                    "UPDATE object SET datetimecreation = '"
                    + str(datetimeobservation)
                    + "'"
                )
                sql += " WHERE pk_object = " + str(pk_objet)
                self.dbase.query(sql)

            if (
                self.parentWidget is not None
                and self.parentWidget.currentFeaturePK is not None
            ):
                if self.parentWidget.DBASETABLENAME == "deficiency":
                    pk_objet, datetimecreation = self.dbase.getValuesFromPk(
                        "deficiency_qgis",
                        ["pk_object", "datetimecreation"],
                        self.parentWidget.currentFeaturePK,
                    )
                    if isinstance(datetimecreation, str):
                        datetimecreation = datetime.datetime.strptime(
                            str(datetimecreation), "%Y-%m-%d %H:%M:%S"
                        )
                    if datetimecreation > datetimeobservation:
                        sql = (
                            "UPDATE object SET datetimecreation = '"
                            + str(datetimeobservation)
                            + "'"
                        )
                        sql += " WHERE pk_object = " + str(pk_objet)
                        self.dbase.query(sql)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_observation_ui.ui")
        uic.loadUi(uipath, self)
