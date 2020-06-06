# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
from collections import OrderedDict

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget)

from ..base3.lamiabase_equipment_tool import BaseEquipmentTool
from .lamiabase_wds_node_tool import BaseWaterdistributionNodeTool
from .lamiabase_wds_camera_tool import BaseWaterdistributionCameraTool as BaseCameraTool
from .lamiabase_wds_sketch_tool import BaseWaterdistributionSketchTool as BaseSketchTool
from .lamiabase_wds_deficiency_tool import BaseWaterdistributionDeficiencyTool
from ..subwidgets.subwidget_gpsvalues import GpsValuesWidget
from ..subwidgets.subwidget_createsubfeature import CreateSubFeatureWidget

class BaseWaterdistributionEquipmentTool(BaseEquipmentTool):

    def __init__(self, **kwargs):
        super(BaseWaterdistributionEquipmentTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {'equipment' : {'linkfield' : 'id_equipment',
                                            'widgets' : {'equipmenttype' : self.toolwidgetmain.comboBox_typeouvrage,
                                                        'equipmentsubtype' :  self.toolwidgetmain.comboBox_sstype,

                                                        'totaldynamichead' : self.toolwidgetmain.doubleSpinBox_hmano,

                                                        'volume': self.toolwidgetmain.doubleSpinBox_volume,
                                                        'tanknumber': self.toolwidgetmain.spinBox_nbrecuves,
                                                        'elevationsql': self.toolwidgetmain.doubleSpinBox_cotesql,
                                                        'elevationculvert': self.toolwidgetmain.doubleSpinBox_coteradier,
                                                        'elevationoverflow': self.toolwidgetmain.doubleSpinBox_cotetp,

                                                        'diameter': self.toolwidgetmain.doubleSpinBox_diam,
                                                        'meternumber': self.toolwidgetmain.doubleSpinBox_nbrecompteur,
                                                        'metertype': self.toolwidgetmain.comboBox_fonct,

                                                        'depthequipment': self.toolwidgetmain.doubleSpinBox_prof,

                                                        'X': self.toolwidgetmain.doubleSpinBox_X,
                                                        'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                        'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                        'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                        'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                        'dZ': self.toolwidgetmain.doubleSpinBox_dZ,


                                                        }},
                                    'object': {'linkfield': 'id_object',
                                                'widgets': {
                                                    'comment': self.toolwidgetmain.textBrowser_commentaire,
                                                    'name': self.toolwidgetmain.lineEdit_nom}},
                                    'descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                            'widgets': {
                                                                'operational': self.toolwidgetmain.comboBox_enservice,
                                                                'dateoperationalcreation': self.toolwidgetmain.dateEdit_anneepose
                                                                        }}}


        self.toolwidgetmain.toolButton_hmano.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_hmano))

        self.toolwidgetmain.toolButton_volume.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_volume))
        self.toolwidgetmain.toolButton_nbrecuve.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.spinBox_nbrecuves))

        self.toolwidgetmain.toolButton_cotesql.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_cotesql))
        self.toolwidgetmain.toolButton_coteradier.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_coteradier))
        self.toolwidgetmain.toolButton_cotetp.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_cotetp))

        self.toolwidgetmain.toolButton_diam.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diam))
        self.toolwidgetmain.toolButton_nbrecompteur.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_nbrecompteur))

        self.toolwidgetmain.toolButton_prof.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_prof))

        self.toolwidgetmain.comboBox_typeouvrage.currentIndexChanged.connect(self.fielduiTypeOhChanged)
        self.toolwidgetmain.pushButton_getGPS.clicked.connect(self.getGPSValue)


        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        self.propertieswdgDesordre = BaseWaterdistributionDeficiencyTool(**self.instancekwargs)
        #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
        #self.propertieswdgDesordre.userwdgfield.stackedWidget.setVisible(False)
        #self.propertieswdgDesordre.groupBox_elements.setParent(None)
        #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
        #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
        #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
        #self.propertieswdgDesordre.groupBox_geom.setParent(None)
        self.propertieswdgDesordre.SKIP_LOADING_UI = True
        self.propertieswdgDesordre.TABLEFILTERFIELD = {'deficiencycategory': 'EQP' }

        # self.propertieswdgDesordre.initMainToolWidget()
        # self.propertieswdgDesordre.formtoolwidgetconfdictmain['deficiency']['widgets']['deficiencycategory'] = 'EQP'
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)

        self.propertieswdgNoeud = BaseWaterdistributionNodeTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgNoeud)

        self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


        self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        #* gpswidget
        self.gpswidget = GpsValuesWidget(parentwdg=self,  
                                        parentframe=self.toolwidgetmain.frame_gps)
        self.lamiawidgets.append(self.gpswidget)
        self.createdeficiencywdg = CreateSubFeatureWidget(self,self.propertieswdgDesordre)
        self.lamiawidgets.append(self.createdeficiencywdg)








    def fielduiTypeOhChanged(self, comboindex):
        currenttext = self.toolwidgetmain.comboBox_typeouvrage.currentText()
        currentrawvalue = typeeqp = self.dbase.getConstraintRawValueFromText('equipment', 'equipmenttype', currenttext)

        if currentrawvalue in ['SPO']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
        elif currentrawvalue in ['RES']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)
        elif currentrawvalue in ['CHA']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(2)
        elif currentrawvalue in [u'CHE']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(3)
        else:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(4)


        #self.propertieswdgDesordre.propertieswdgOBSERVATION2.updateObservationStackedWidget()





    def addGPSPoint(self):
        if self.gpsutil.currentpoint is None:
            self.windowdialog.errorMessage('GPS non connecte')
            return

        self.createorresetRubberband(0)

        layerpoint = self.gpsutil.currentpoint


        self.setTempGeometry([layerpoint],False)

        self.getGPSValue()



    # def magicFunction(self):
    #     self.featureSelected()
    #     #self.lastPhoto()
    #     self.addGPSPoint()
    #     self.saveFeature()

    def toolbarMagic(self):
        self.mainifacewidget.toolbarNew()
        self.toolbarGeomAddGPS()
        self.getGPSValue()
        self.mainifacewidget.toolbarSave()


    def getGPSValue(self):
        self.assignValue(self.gpswidget.label_X, self.toolwidgetmain.doubleSpinBox_X)
        self.assignValue(self.gpswidget.label_dX, self.toolwidgetmain.doubleSpinBox_dX)
        self.assignValue(self.gpswidget.label_Y, self.toolwidgetmain.doubleSpinBox_Y)
        self.assignValue(self.gpswidget.label_dY, self.toolwidgetmain.doubleSpinBox_dY)
        self.assignValue(self.gpswidget.label_Z, self.toolwidgetmain.doubleSpinBox_Z)
        self.assignValue(self.gpswidget.label_dZ, self.toolwidgetmain.doubleSpinBox_dZ)

    def assignValue(self,wdgfrom, wdgto):
        if self.isfloat(wdgfrom.text()):
            wdgto.setValue(float(wdgfrom.text()))

    def isfloat(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    def postSaveFeature(self, savedfeaturepk=None):
        pass
        """
        if self.currentFeaturePK is None:
            self.propertieswdgDesordre.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('equipment_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)

            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
            qgsgeomfordesordre = qgsgeom

            self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)

            self.currentFeaturePK = savedfeaturepk
            self.propertieswdgDesordre.toolbarSave()
            pkdesordre = self.propertieswdgDesordre.currentFeaturePK
            # sql = "UPDATE Desordre SET groupedesordre = 'EQP' WHERE pk_desordre = {}".format(pkdesordre)
            # self.dbase.query(sql)
        """

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_wds_equipment_tool_ui.ui')
        uic.loadUi(uipath, self)