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

import sys
from collections import OrderedDict
import datetime
import os

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget, QPushButton)

from ..base3.lamiabase_node_tool import BaseNodeTool
from .lamiabase_wds_camera_tool import BaseWaterdistributionCameraTool as BaseCameraTool
from .lamiabase_wds_sketch_tool import BaseWaterdistributionSketchTool as BaseSketchTool
from .lamiabase_wds_deficiency_tool import BaseWaterdistributionDeficiencyTool
from ..subwidgets.subwidget_topologicnode import TopologicNodeWidget
from ..subwidgets.subwidget_gpsvalues import GpsValuesWidget
from ..subwidgets.subwidget_createsubfeature import CreateSubFeatureWidget

class BaseWaterdistributionNodeTool(BaseNodeTool):


    PARENTJOIN = {'equipment' : {'colparent': 'id_descriptionsystem',
                                'colthistable': 'lid_descriptionsystem_1',
                                 'tctable': None,
                                 'tctablecolparent':None,
                                 'tctablecolthistable':None}
                 }

    def __init__(self, **kwargs):
        super(BaseWaterdistributionNodeTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'node' : {'linkfield' : 'id_node',
                                            'widgets' : {
                                                        'nodetype': self.toolwidgetmain.comboBox_cat,
                                                        'nodefunction': self.toolwidgetmain.comboBox_fonction,
                                                        'nodesubtype': self.toolwidgetmain.comboBox_soustype,
                                                        'access': self.toolwidgetmain.comboBox_acces,
                                                        'accessshape': self.toolwidgetmain.comboBox_formeaccess,
                                                        'diameterinlet': self.toolwidgetmain.doubleSpinBox_diam,
                                                        'diameteroutlet': self.toolwidgetmain.doubleSpinBox_diamsor,
                                                        'nodedepth' : self.toolwidgetmain.doubleSpinBox_prof,
                                                        
                                                    'presencestep': self.toolwidgetmain.comboBox_echelon,
                                                        #ventouse
                                                            'nodeelevation': self.toolwidgetmain.doubleSpinBox_altim,
                                                        #vanne
                                                        'localisation': [self.toolwidgetmain.comboBox_localisation,
                                                                        self.toolwidgetmain.comboBox_localisation2],
                                                        'accessibility': [self.toolwidgetmain.comboBox_accessibilite,
                                                                        self.toolwidgetmain.comboBox_accessibilite2],
                                                    'manipulability': self.toolwidgetmain.comboBox_manipulable,
                                                        'nodeposition': self.toolwidgetmain.comboBox_position,
                                                #vidange
                                                'presenceoutlet': self.toolwidgetmain.lineEdit_exutoire,
                                                #reg pression
                                                'valvedownstreamsetting': self.toolwidgetmain.doubleSpinBox_cons_av,
                                                'valveupstreamsetting': self.toolwidgetmain.doubleSpinBox_cons_am,

                                                # hydrant
                                                'hydrantfiredepartmentid': self.toolwidgetmain.spinBox_idsdis,
                                                'brandname': [self.toolwidgetmain.lineEdit_marque,
                                                        self.toolwidgetmain.lineEdit_marque2],
                                                'brandref': self.toolwidgetmain.lineEdit_type,
                                                'hydrantconformity': self.toolwidgetmain.comboBox_conformite,

                                                #compteur"
                                                'nodesize': self.toolwidgetmain.doubleSpinBox_dimensions,
                                                'nodeemitter': self.toolwidgetmain.comboBox_tete_emettrice,
                                                'nodecountervalue': self.toolwidgetmain.spinBox_numero,
                                                'retrofitable': self.toolwidgetmain.comboBox_equipable,
                                                #'localisation': self.toolwidgetmain.comboBox_localisation2,
                                                #'accessibilite': self.toolwidgetmain.comboBox_accessibilite2,
                                                # 'marque': self.toolwidgetmain.lineEdit_marque2,
                                                # 'type': self.toolwidgetmain.lineEdit_type2,
                                                'maintenancefirm': [self.toolwidgetmain.lineEdit_entreprise,
                                                            self.toolwidgetmain.lineEdit_entreprise2],
                                                'remotemonitoring': [self.toolwidgetmain.comboBox_telerelevage,
                                                                self.toolwidgetmain.comboBox_telerelevage2],
                                                'linkedfacilities': self.toolwidgetmain.lineEdit_organes_associes,

                                                #chloration
                                                #'entreprise': self.toolwidgetmain.lineEdit_entreprise2,
                                                #'telerelevage': self.toolwidgetmain.comboBox_telerelevage2,
                                                # robinet de prise en charge
                                                'clamp': self.toolwidgetmain.comboBox_collier,

                                                'X': self.toolwidgetmain.doubleSpinBox_X,
                                                'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                'dZ': self.toolwidgetmain.doubleSpinBox_dZ


                                                        }},
                            'object' : {'linkfield' : 'id_object',
                                        'widgets' : {'comment': self.toolwidgetmain.textBrowser_comm}},
                            'descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                    'widgets' : {  'operational': self.toolwidgetmain.comboBox_enservice,
                                                                    'dateoperationalcreation': self.toolwidgetmain.dateEdit_anneepose,
                                                                    'networktype': self.toolwidgetmain.comboBox_nature_reseau,
                                                                    }}}


        self.toolwidgetmain.toolButton_diam.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diam))
        self.toolwidgetmain.toolButton_diamsor.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diamsor))
        self.toolwidgetmain.toolButton_prof.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_prof))

        self.toolwidgetmain.toolButton_idsdis.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.spinBox_idsdis))

        self.toolwidgetmain.toolButton_altim.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_altim))

        self.toolwidgetmain.toolButton_cons_am.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_cons_am))
        self.toolwidgetmain.toolButton_cons_av.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_cons_av))



        self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
        self.toolwidgetmain.pushButton_getGPS.clicked.connect(self.getGPSValue)

        self.allaccessfields = OrderedDict(self.dbase.dbasetables[self.DBASETABLENAME]['fields']['access'])


        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        self.propertieswdgDesordre = BaseWaterdistributionDeficiencyTool(**self.instancekwargs)
        #self.propertieswdgDesordre.NAME = None
        #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
        #self.propertieswdgDesordre.userwdgfield.stackedWidget.setVisible(False)
        #self.propertieswdgDesordre.groupBox_elements.setParent(None)
        #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
        #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
        #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
        #self.propertieswdgDesordre.groupBox_geom.setParent(None)
        #self.propertieswdgDesordre.frame_editing.setVisible(False)
        #self.toolwidgetmain.tabWidget_2.widget(2).layout().addWidget(self.propertieswdgDesordre)
        self.propertieswdgDesordre.SKIP_LOADING_UI = True
        self.propertieswdgDesordre.TABLEFILTERFIELD = {'deficiencycategory': 'NOD' }
        # self.propertieswdgDesordre.initMainToolWidget()
        # self.propertieswdgDesordre.formtoolwidgetconfdictmain['deficiency']['widgets']['deficiencycategory'] = 'NOD'
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)


        self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

        self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)



        self.topologicnode = TopologicNodeWidget(self)
        self.lamiawidgets.append(self.topologicnode)
        self.createdeficiencywdg = CreateSubFeatureWidget(self,self.propertieswdgDesordre)
        self.lamiawidgets.append(self.createdeficiencywdg)
        #* gpswidget
        self.gpswidget = GpsValuesWidget(parentwdg=self,  
                                        parentframe=self.toolwidgetmain.frame_gps)
        self.lamiawidgets.append(self.gpswidget)


    # def postInitFeatureProperties(self, feat): 
    def postSelectFeature(self):
        dbasetable = self.dbase.dbasetables['node']
        if self.currentFeaturePK is not None:
            lid_dessys = self.dbase.getValuesFromPk('node_qgis',['lid_descriptionsystem_1'],self.currentFeaturePK)
            if lid_dessys is not None:
                self.toolwidgetmain.comboBox_acces.setEnabled(False)
            else:
                self.toolwidgetmain.comboBox_acces.setEnabled(True)
        else:
            self.toolwidgetmain.comboBox_acces.setEnabled(True)


        if (self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None
                and self.parentWidget.DBASETABLENAME == 'equipment'):

            type_ouvrage = self.dbase.getValuesFromPk('equipment_qgis',
                                                        ['equipmenttype'],
                                                        self.parentWidget.currentFeaturePK)

            if type_ouvrage == 'CHE':
                # dbasetable['fields']['acces'] = OrderedDict([('PGtype', 'VARCHAR(255'),('ParFldCst','categorie'),('Cst',[[u'Chambre enterrée/regard', 'CHE',['','VEN','VAN','VID','REG','HYD','COM','CHL','RPC','SPE']]])])
                #                                                                                                                                              #  ['','VEN','VAN','VID','REG','HYD','COM','DEB','CHL','RPC','SPE','AUT','IND']
                rawval = [elem[1] for elem in dbasetable['fields']['access']['Cst']] 
                cheindex = rawval.index('CHE')
                dbasetable['fields']['access']['Cst'][cheindex][2] = ['','VEN','VAN','VID','REG','HYD','COM','CHL','RPC','SPE']

                self.toolwidgetmain.comboBox_cat.currentIndexChanged.emit(self.toolwidgetmain.comboBox_cat.currentIndex())
                self.toolwidgetmain.comboBox_acces.setEnabled(False)

            else:
                if dbasetable['fields']['access'] != self.allaccessfields:
                    dbasetable['fields']['access'] = self.allaccessfields
                    self.toolwidgetmain.comboBox_cat.currentIndexChanged.emit(self.toolwidgetmain.comboBox_cat.currentIndex())
        else:
            if dbasetable['fields']['access'] != self.allaccessfields:
                dbasetable['fields']['access'] = self.allaccessfields
                self.toolwidgetmain.comboBox_cat.currentIndexChanged.emit(self.toolwidgetmain.comboBox_cat.currentIndex())


    def postSaveFeature(self, savedfeaturepk=None):
        pass
        """
        if self.currentFeaturePK is None:
            self.propertieswdgDesordre.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('node_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)

            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
            qgsgeomfordesordre = [qgsgeom,qgsgeom]

            self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)

            self.currentFeaturePK = savedfeaturepk
            self.propertieswdgDesordre.toolbarSave()
            pkdesordre = self.propertieswdgDesordre.currentFeaturePK
            # sql = "UPDATE deficiency SET deficiencycategory = 'NOD' WHERE pk_deficiency = {}".format(pkdesordre)
            # self.dbase.query(sql)
        """


    def changeCategorie(self, intcat):
        typeeqt = self.toolwidgetmain.comboBox_cat.itemText(intcat)
        rawtypeeqt = self.dbase.getConstraintRawValueFromText('node', 'nodetype', typeeqt)
        pagecount = self.toolwidgetmain.stackedWidget.count()
        for pageindex in range(pagecount):
            wdgname = self.toolwidgetmain.stackedWidget.widget(pageindex).objectName()
            if wdgname == rawtypeeqt:
                self.toolwidgetmain.stackedWidget.setCurrentIndex(pageindex)
                return
        self.toolwidgetmain.stackedWidget.setCurrentIndex(pagecount)
        


    def toolbarMagic(self):
        self.mainifacewidget.toolbarNew()
        self.toolbarGeomAddGPS()
        self.getGPSValue()
        self.mainifacewidget.toolbarSave()


        # self.featureSelected()
        # #self.lastPhoto()
        # self.addGPSPoint()
        # self.saveFeature()


    def addGPSPoint(self):
        if self.gpsutil is None:
            return
        if self.gpsutil.currentpoint is None:
            self.windowdialog.errorMessage('GPS non connecte')
            return

        self.createorresetRubberband(0)

        layerpoint = self.gpsutil.currentpoint


        self.setTempGeometry([layerpoint],False)

        self.getGPSValue()


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








class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_wds_node_tool_ui.ui')
        uic.loadUi(uipath, self)

