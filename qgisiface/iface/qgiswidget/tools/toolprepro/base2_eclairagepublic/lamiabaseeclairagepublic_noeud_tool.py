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
import qgis
from collections import OrderedDict
import datetime

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget, QPushButton)

from ..base2.lamiabase_noeud_tool import BaseNoeudTool
from .lamiabaseeclairagepublic_photo_tool import BaseEclairagePublicPhotoTool as BasePhotoTool
from .lamiabaseeclairagepublic_croquis_tool import BaseEclairagePublicCroquisTool as BaseCroquisTool
from .lamiabaseeclairagepublic_equipement_tool import BaseEclairagePublicEquipementTool
from .lamiabaseeclairagepublic_desordre_tool import BaseEclairagePublicDesordreTool



class BaseEclairagePublicNoeudTool(BaseNoeudTool):



    def __init__(self, **kwargs):
        super(BaseEclairagePublicNoeudTool, self).__init__(**kwargs)


    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Noeud'
        self.dbasetablename = 'Noeud'
        self.visualmode = [0, 1, 2]
        self.PointENABLED = True
        # self.LineENABLED = False
        # self.PolygonENABLED = True
        self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__),'..','base2', 'lamiabase_noeud_tool_icon.svg')
        self.linkedgeom = [['Equipement', 'lid_descriptionsystem_1'],['Desordre', 'lid_descriptionsystem']]


        # ****************************************************************************************
        #properties ui
        pass
        if True:
            self.deepcopy = [[u'Desordre', u'Observation'],
                             [u'Equipement',u'Desordre', u'Observation']]
        # self.deepcopy = [[u'Desordre','Observation']]
    """

    def initMainToolWidget(self):

        if self.dbase.variante in [None, 'Lamia']:
  
            self.toolwidgetmain = UserUI()

            self.formtoolwidgetconfdictmain = {'Noeud': {'linkfield': 'id_noeud',
                                                        'widgets': OrderedDict([
                                                            ('typenoeud', self.toolwidgetmain.comboBox_typenoeud),

                                                            ('contrat', self.toolwidgetmain.lineEdit_contrat),
                                                            ('pdl', self.toolwidgetmain.lineEdit_achemin),
                                                            ('typalim', self.toolwidgetmain.comboBox_typealim),

                                                            ('cptind', self.toolwidgetmain.comboBox_coff_indep),
                                                            ('typecpt', self.toolwidgetmain.comboBox_typecompt),
                                                            ('numcomp', self.toolwidgetmain.lineEdit_numcompt),
                                                            ('ttprtcpt', self.toolwidgetmain.comboBox_type_protect),
                                                            ('calprtcpt', self.toolwidgetmain.lineEdit_calibre_compt),

                                                            ('difdjbr', self.toolwidgetmain.comboBox_diffcomptbranch),
                                                            ('modposen', self.toolwidgetmain.comboBox_modeposeenv),
                                                            ('typen', self.toolwidgetmain.comboBox_typeenv),

                                                            ('fermen', self.toolwidgetmain.comboBox_ferenv),
                                                            ('prtgen', self.toolwidgetmain.comboBox_typeprogen),
                                                            ('calprtgen', self.toolwidgetmain.lineEdit_calprogen),
                                                            ('difdjgen', self.toolwidgetmain.comboBox_difprogen),
                                                            ('presur', self.toolwidgetmain.comboBox_prespara),
                                                            ('pre', self.toolwidgetmain.lineEdit_valpristerre),
                                                            ('miseter', self.toolwidgetmain.comboBox_misterrearmoire),

                                                            ('var', self.toolwidgetmain.comboBox_presvar),
                                                            ('typvar', self.toolwidgetmain.lineEdit_typevar),
                                                            ('puisvar', self.toolwidgetmain.spinBox_puissvar),
                                                            ('foncall', self.toolwidgetmain.comboBox_fonceclai),
                                                            ('typall', self.toolwidgetmain.comboBox_typeallu),
                                                            ('refall', self.toolwidgetmain.lineEdit_refallu),

                                                            ('valcon', self.toolwidgetmain.spinBox_valcontcompt),
                                                            ('unicon', self.toolwidgetmain.comboBox_unicon),
                                                            ('tempcon', self.toolwidgetmain.spinBox_tempcon),
                                                            ('nomtour', self.toolwidgetmain.spinBox_nomtour),
                                                            ('valcow', self.toolwidgetmain.doubleSpinBox_valcow),
                                                            ('valcova', self.toolwidgetmain.doubleSpinBox_valconva),

                                                            ('p1_v', self.toolwidgetmain.doubleSpinBox_p1v),
                                                            ('p1_i', self.toolwidgetmain.doubleSpinBox_p1i),
                                                            ('p1_p', self.toolwidgetmain.doubleSpinBox_p1p),
                                                            ('p1_pva', self.toolwidgetmain.doubleSpinBox_p1va),
                                                            ('p1_cos', self.toolwidgetmain.doubleSpinBox_p1cos),

                                                            ('p2_v', self.toolwidgetmain.doubleSpinBox_p2v),
                                                            ('p2_i', self.toolwidgetmain.doubleSpinBox_p2i),
                                                            ('p2_p', self.toolwidgetmain.doubleSpinBox_p2p),
                                                            ('p2_pva', self.toolwidgetmain.doubleSpinBox_p2va),
                                                            ('p2_cos', self.toolwidgetmain.doubleSpinBox_p2cos),

                                                            ('p3_v', self.toolwidgetmain.doubleSpinBox_p3v),
                                                            ('p3_i', self.toolwidgetmain.doubleSpinBox_p3i),
                                                            ('p3_p', self.toolwidgetmain.doubleSpinBox_p3p),
                                                            ('p3_pva', self.toolwidgetmain.doubleSpinBox_p3va),
                                                            ('p3_cos', self.toolwidgetmain.doubleSpinBox_p3cos),



                                                            ('multip', self.toolwidgetmain.comboBox_multip),
                                                            ('sp_type', self.toolwidgetmain.comboBox_sp_type),
                                                            ('sp_materiau', self.toolwidgetmain.comboBox_sp_materiau),
                                                            ('sp_forme', self.toolwidgetmain.comboBox_sp_forme),
                                                            ('sp_couleur', self.toolwidgetmain.lineEdit_sp_couleur),
                                                            ('sp_diam', self.toolwidgetmain.doubleSpinBox_sp_diam),
                                                            ('sp_haut', self.toolwidgetmain.doubleSpinBox_sp_haut),
                                                            ('sp_typmonc', self.toolwidgetmain.comboBox_sp_typmonc),
                                                            ('sp_depcro', self.toolwidgetmain.doubleSpinBox_sp_depcro),

                                                            ('sp_boitbran', self.toolwidgetmain.comboBox_sp_boitbran),
                                                            ('sp_appmat', self.toolwidgetmain.comboBox_sp_appmat),
                                                            ('sp_typbr', self.toolwidgetmain.comboBox_sp_typbr),
                                                            ('sp_typprot', self.toolwidgetmain.comboBox_sp_typprot),
                                                            ('sp_appmat', self.toolwidgetmain.comboBox_sp_appmat),
                                                            ('sp_calprot', self.toolwidgetmain.lineEdit_sp_calprot),
                                                            ('sp_barette', self.toolwidgetmain.comboBox_sp_barette),
                                                            ('sp_preter', self.toolwidgetmain.comboBox_sp_preter),
                                                            ('sp_terracc', self.toolwidgetmain.comboBox_sp_terracc),
                                                            ('sp_liaisoneq', self.toolwidgetmain.comboBox_sp_liaisoneq),
                                                            ('sp_eq', self.toolwidgetmain.comboBox_sp_eq),






                                                            ('X', self.toolwidgetmain.doubleSpinBox_X),
                                                            ('dX', self.toolwidgetmain.doubleSpinBox_dX),
                                                            ('Y', self.toolwidgetmain.doubleSpinBox_Y),
                                                            ('dY', self.toolwidgetmain.doubleSpinBox_dY),
                                                            ('Z', self.toolwidgetmain.doubleSpinBox_Z),
                                                            ('dZ', self.toolwidgetmain.doubleSpinBox_dZ),

                                                        ])},
                                                'Objet': {'linkfield': 'id_objet',
                                                        'widgets': {
                                                            'commentaire': self.toolwidgetmain.textBrowser_commentaire}},
                                                'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                                    'widgets': {}}}

            self.toolwidgetmain.toolButton_sp_haut.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_sp_haut))
            self.toolwidgetmain.toolButton_sp_diam.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_sp_diam))
            self.toolwidgetmain.toolButton_sp_depcro.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_sp_depcro))

            self.toolwidgetmain.toolButton_p1v.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p1v))
            self.toolwidgetmain.toolButton_p1i.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p1i))
            self.toolwidgetmain.toolButton_p1p.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p1p))
            self.toolwidgetmain.toolButton_p1va.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p1va))
            self.toolwidgetmain.toolButton_p1cos.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p1cos))

            self.toolwidgetmain.toolButton_p2v.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p2v))
            self.toolwidgetmain.toolButton_p2i.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p2i))
            self.toolwidgetmain.toolButton_p2p.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p2p))
            self.toolwidgetmain.toolButton_p2va.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p2va))
            self.toolwidgetmain.toolButton_p2cos.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p2cos))


            self.toolwidgetmain.toolButton_p3v.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p3v))
            self.toolwidgetmain.toolButton_p3i.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p3i))
            self.toolwidgetmain.toolButton_p3p.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p3p))
            self.toolwidgetmain.toolButton_p3va.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p3va))
            self.toolwidgetmain.toolButton_p3cos.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_p3cos))



            self.toolwidgetmain.comboBox_typenoeud.currentIndexChanged.connect(self.fielduiTypeChanged)
            self.toolwidgetmain.pushButton_getGPS.clicked.connect(self.getGPSValue)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self

            self.propertieswdgEQUIPEMENT = BaseEclairagePublicEquipementTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgDesordre = BaseEclairagePublicDesordreTool(**self.instancekwargs)
            #self.propertieswdgDesordre.NAME = None
            #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            #self.propertieswdgDesordre.groupBox_elements.setParent(None)
            #self.propertieswdgDesordre.userwdgfield.stackedWidget.setParent(None)
            #self.propertieswdgDesordre.frame_editing.setParent(None)
            #self.toolwidgetmain.frame_desordre.layout().addWidget(self.propertieswdgDesordre)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)






    def fielduiTypeChanged(self, comboindex):
        self.toolwidgetmain.stackedWidget.setCurrentIndex(comboindex)



    def addGPSPoint(self):
        if self.gpsutil.currentpoint is None:
            self.windowdialog.errorMessage('GPS non connecte')
            return

        self.createorresetRubberband(0)

        layerpoint = self.gpsutil.currentpoint


        self.setTempGeometry([layerpoint],False)

        self.getGPSValue()



    def magicFunction(self):
        self.featureSelected()
        #self.lastPhoto()
        self.addGPSPoint()
        self.saveFeature()


    def getGPSValue(self):
        self.assignValue(self.toolwidgetmain.label_X, self.toolwidgetmain.doubleSpinBox_X)
        self.assignValue(self.toolwidgetmain.label_dX, self.toolwidgetmain.doubleSpinBox_dX)
        self.assignValue(self.toolwidgetmain.label_Y, self.toolwidgetmain.doubleSpinBox_Y)
        self.assignValue(self.toolwidgetmain.label_dY, self.toolwidgetmain.doubleSpinBox_dY)
        self.assignValue(self.toolwidgetmain.label_Z, self.toolwidgetmain.doubleSpinBox_Z)
        self.assignValue(self.toolwidgetmain.label_dZ, self.toolwidgetmain.doubleSpinBox_dZ)


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


        # save a disorder on first creation
        # if self.savingnewfeature and not self.savingnewfeatureVersion:
        if self.currentFeaturePK is None:
            self.propertieswdgDesordre.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('Noeud_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)

            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
            qgsgeomfordesordre = [qgsgeom, qgsgeom]
            self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)

            self.currentFeaturePK = savedfeaturepk
            self.propertieswdgDesordre.toolbarSave()
            pkdesordre = self.propertieswdgDesordre.currentFeaturePK
            sql = "UPDATE Desordre SET groupedesordre = 'NOD' WHERE pk_desordre = {}".format(pkdesordre)
            self.dbase.query(sql)
            """
            pkobjet = self.dbase.createNewObjet()
            lastiddesordre = self.dbase.getLastId('Desordre') + 1
            geomtext, iddessys = self.dbase.getValuesFromPk('Noeud_qgis',
                                                            ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                            self.currentFeaturePK)
            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                newgeom = qgis.core.QgsGeometry.fromPolyline([qgsgeom.asPoint(), qgsgeom.asPoint()])
                newgeomwkt = newgeom.exportToWkt()
            else:
                #newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPointXY(), qgsgeom.asPointXY()])
                newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
                newgeomwkt = newgeom.asWkt()

            sql = self.dbase.createSetValueSentence(type='INSERT',
                                                    tablename='Desordre',
                                                    listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                  'lid_descriptionsystem', 'geom'],
                                                    listofrawvalues=[lastiddesordre, pkobjet, 'NOD',
                                                                     iddessys, newgeomwkt])
            self.dbase.query(sql)
            """










class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeclairagepublic_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)
