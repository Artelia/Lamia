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


import datetime, os

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget)

from ...lamia_abstractformtool import AbstractLamiaFormTool
from .lamiabase_report_tool import BaseReportTool
from .lamiabase_camera_tool import BaseCameraTool
from .lamiabase_sketch_tool import BaseSketchTool
from .lamiabase_topography_tool import BaseTopographyTool
from .lamiabase_actor_tool import BaseActorTool

base3 = QtCore.QObject()

class BaseDeliveryTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'delivery'
    LOADFIRST = False

    tooltreewidgetCAT =QtCore.QCoreApplication.translate('base3','Management')
    tooltreewidgetSUBCAT =QtCore.QCoreApplication.translate('base3','Delivery')
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_delivery_tool_icon.png')
    

    tempparentjoin = {}
    linkdict = {'colparent': 'id_object',
                'colthistable': 'id_actor',
                    'tctable': 'tcobjectactor',
                    'tctablecolparent':'lid_object',
                    'tctablecolthistable':'lid_actor'}
    for tablename in ['actor']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin


    def __init__(self, **kwargs):
        super(BaseDeliveryTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'delivery' : {'linkfield' : 'id_delivery',
                                            'widgets' : {
                                                        'datetimecontract' : self.toolwidgetmain.dateEdit_date,
                                                        'contractref': self.toolwidgetmain.lineEdit_nummarche,
                                            }},
                            'object' : {'linkfield' : 'id_object',
                                        'widgets' : {'name': self.toolwidgetmain.lineEdit_nom}}}
        self.toolwidgetmain.pushButton_currentPrestation.clicked.connect(self.defineCurrentPrestation)
        #self.toolwidgetmain.pushButton_defineinter.clicked.connect(self.manageLinkage)

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        self.propertieswdgRAPPORT = BaseReportTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgRAPPORT)

        self.propertieswdgPHOTO = BaseCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTO)

        self.propertieswdgTOPOGRAPHIE = BaseTopographyTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgTOPOGRAPHIE)

        self.propertieswdgACTORS= BaseActorTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgACTORS)



    def defineCurrentPrestation(self):
        self.windowdialog.currentprestationlabel.setText('Prestation : ' + str(self.currentFeature.id()) + " - " +str(self.currentFeature['nommarche'] ))
        self.dbase.currentprestationid = self.currentFeature.id()


    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass
    """

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict({'datemarche' : datecreation},checkifinforgottenfield=False)

        else:
            try:
                idobjet = self.dbase.getValuesFromPk(self.DBASETABLENAME + '_qgis', 
                                                    'id_object',
                                                    self.currentFeaturePK)
                sql = "SELECT tcobjectactor.role, actor.actorname, actor.society  FROM tcobjectactor "
                sql += " INNER JOIN actor ON tcobjectactor.lid_actor = actor.id_actor "
                sql += "WHERE lid_object = " + str(idobjet)
                query = self.dbase.query(sql)

                result = "\n".join([str(row) for row in query])
                self.toolwidgetmain.textBrowser_intervenants.clear()
                self.toolwidgetmain.textBrowser_intervenants.append(result)
            except KeyError as e:
                print('postInitFeatureProperties', e)



    def postSaveFeature(self, boolnewfeature):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_delivery_tool_ui.ui')
        uic.loadUi(uipath, self)