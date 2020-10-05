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

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget, QPushButton

from Lamia.iface.qgiswidget.tools.lamia_abstractformtool import AbstractLamiaFormTool
from .lamia_form_camera import BaseCameraTool
from .lamia_form_sketch import BaseSketchTool

base3 = QtCore.QObject()


class BaseNodeTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "node"
    DBASETABLENAME = "node"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Facilities")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Nodes")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_node_icon.svg"
    )

    PARENTJOIN = {
        "facility": {
            "colparent": "id_facility",
            "colthistable": "lid_facility",
            "tctable": None,
            "tctablecolparent": None,
            "tctablecolthistable": None,
        }
    }

    def __init__(self, **kwargs):
        super(BaseNodeTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs  # depreciated
        self.instancekwargsforchildwdg = kwargs
        self.instancekwargsforchildwdg["parentwidget"] = self

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "node": {"linkfield": "id_node", "widgets": {}},
            "object": {
                "linkfield": "id_object",
                "widgets": {"name": self.toolwidgetmain.lineEdit_libelle},
            },
            "descriptionsystem": {"linkfield": "id_descriptionsystem", "widgets": {}},
        }

        self.toolwidgetmain.comboBox_category.currentIndexChanged.connect(
            self.changeCategory
        )

        # ****************************************************************************************
        # child widgets

        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        if self.parentWidget is None:
            self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    def postSelectFeature(self):
        pass

    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:
            # lastrevision = self.dbase.maxrevision
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')



        #sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pksys = self.dbase.getLastRowId('Descriptionsystem')

        #idnoeud = self.currentFeature.id()
        pknoeud = self.currentFeaturePK
        lastidnoeud = self.dbase.getLastId('Noeud') + 1
        sql = "UPDATE Noeud SET id_noeud = " + str(lastidnoeud)  + ","
        sql += "lpk_descriptionsystem = " + str(pksys)
        sql += " WHERE pk_noeud = " + str(pknoeud) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if  self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            # if "lid_descriptionsystem" in self.dbase.dbasetables[self.parentWidget.dbasetablename]['fields'].keys():
            if 'Descriptionsystem' in self.dbase.getParentTable(self.parentWidget.dbasetablename):

                #parentid
                sql = "SELECT id_descriptionsystem FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
                sql += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
                parentid = self.dbase.query(sql)[0][0]
                #currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
                sql = "UPDATE Noeud SET lid_descriptionsystem_1 = " + str(parentid)
                sql += " WHERE pk_noeud = " + str(pknoeud)
                self.dbase.query(sql)
                self.dbase.commit()
    """

    def postSaveFeature(self, savedfeaturepk=None):
        pass

    def postDeleteFeature(self):
        pass

    def changeCategory(self, intcat):

        pagecount = self.toolwidget.stackedWidget_category.count()
        if intcat >= pagecount - 1:
            self.toolwidget.stackedWidget_category.setCurrentIndex(pagecount - 1)
        else:
            self.toolwidget.stackedWidget_category.setCurrentIndex(intcat)

    """
    def _createDeficiency(self, deficiencywdg,savedfeaturepk):
        if self.currentFeaturePK is None :  #very new equip, not newversion
            deficiencywdg.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('node_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)
            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
            qgsgeomfordesordre = [qgsgeom,qgsgeom]
            deficiencywdg.setTempGeometry(qgsgeomfordesordre)

            deficiencywdg.parentWidget.currentFeaturePK = savedfeaturepk
            deficiencywdg.toolbarSave()
            deficiencywdg.parentWidget.currentFeaturePK = None
    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_node_ui.ui")
        uic.loadUi(uipath, self)
