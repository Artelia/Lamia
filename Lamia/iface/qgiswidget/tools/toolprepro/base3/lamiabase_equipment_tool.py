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
from qgis.PyQt.QtWidgets import (QWidget)

from ...lamia_abstractformtool import AbstractLamiaFormTool
from .lamiabase_camera_tool import BaseCameraTool
from .lamiabase_sketch_tool import BaseSketchTool

base3 = QtCore.QObject()

class BaseEquipmentTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = 'equipment'
    DBASETABLENAME = 'equipment'
    LOADFIRST = True

    tooltreewidgetCAT =QtCore.QCoreApplication.translate('base3','Facilities')
    tooltreewidgetSUBCAT =QtCore.QCoreApplication.translate('base3','Equipment')
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_equipment_tool_icon.svg')


    tempparentjoin = {}
    linkdict = {'colparent': 'id_descriptionsystem',
                'colthistable': 'lid_descriptionsystem_1',
                    'tctable': None,
                    'tctablecolparent':None,
                    'tctablecolthistable':None}
    for tablename in ['node', 'edge', 'equipment']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin


    def __init__(self, **kwargs):
        super(BaseEquipmentTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs
        
       

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'equipment' : {'linkfield' : 'id_equipment',
                                            'widgets' : {'equipmenttype': self.toolwidgetmain.comboBox_cat}},
                                            'object' : {'linkfield' : 'id_object',
                                                        'widgets' : {
                                                                        'comment': self.toolwidgetmain.textBrowser_comm}},
                                            'descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                        'widgets' : {}}}
        self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)


        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []

        if self.parentWidget is None:
            self.instancekwargs['parentwidget'] = self
            
            self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def changeCategorie(self,intcat):

        pagecount = self.toolwidget.stackedWidget.count()
        if intcat >= pagecount -1 :
            self.toolwidget.stackedWidget.setCurrentIndex(pagecount -1)
        else:
            self.toolwidget.stackedWidget.setCurrentIndex(intcat)



    def postSelectFeature(self):
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

        # sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pksys = self.dbase.getLastRowId('Descriptionsystem')

        # idnoeud = self.currentFeature.id()
        pkequip = self.currentFeaturePK
        lastidequip = self.dbase.getLastId('Equipement') + 1
        sql = "UPDATE Equipement SET id_equipement = " + str(lastidequip) + ","
        sql += "lpk_descriptionsystem = " + str(pksys)
        sql += " WHERE pk_equipement = " + str(pkequip) + ";"
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
                sql = "UPDATE Equipement SET lid_descriptionsystem_1 = " + str(parentid)
                sql += " WHERE pk_equipement = " + str(pkequip)
                self.dbase.query(sql)
                self.dbase.commit()
    """






    def postSaveFeature(self, savedfeaturepk=None):
        pass

   


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_equipment_tool_ui.ui')
        uic.loadUi(uipath, self)