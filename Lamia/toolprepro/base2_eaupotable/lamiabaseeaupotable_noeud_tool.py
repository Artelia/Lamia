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



from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QPushButton)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_noeud_tool import BaseNoeudTool

import os
import qgis
from collections import OrderedDict
import datetime
# from ..base.lamiabase_photo_tool import BasePhotoTool
from .lamiabaseeaupotable_photo_tool import BaseEaupotablePhotoTool as BasePhotoTool
from .lamiabaseeaupotable_croquis_tool import BaseEaupotableCroquisTool as BaseCroquisTool
#from ..base.lamiabase_croquis_tool import BaseCroquisTool
#from .lamiabaseeaupotable_desordre_tool import BaseAssainissementDesordreTool
# from .lamiabaseeaupotable_equipement_tool import BaseEaupotableEquipementTool
from .lamiabaseeaupotable_desordre_tool import BaseEaupotableDesordreTool
import sys



class BaseEaupotableNoeudTool(BaseNoeudTool):

    LOADFIRST = True
    dbasetablename = 'Noeud'
    #specialfieldui = ['2']
    #workversionmin = '0_1'
    #workversionmax = '0_1'


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseEaupotableNoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)


    def initTool(self):
        super(BaseEaupotableNoeudTool, self).initTool()
        self.NAME = 'Organes'
        self.magicfunctionENABLED = True

        self.linkagespec = {'Equipement': {'tabletc': None,
                                           'idsource': 'lid_descriptionsystem_1',
                                           'idtcsource': None,
                                           'iddest': 'id_descriptionsystem',
                                           'idtcdest': None,
                                           'desttable': ['Equipement','Infralineaire']}}


    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Noeud' : {'linkfield' : 'id_noeud',
                                             'widgets' : {
                                                            'categorie': self.userwdgfield.comboBox_cat,
                                                            'fonction': self.userwdgfield.comboBox_fonction,
                                                            'ss_type_equipement': self.userwdgfield.comboBox_soustype,
                                                            'acces': self.userwdgfield.comboBox_acces,
                                                            'forme_acces': self.userwdgfield.comboBox_formeaccess,
                                                            'diametre_entree': self.userwdgfield.doubleSpinBox_diam,
                                                            'diametre_sortie': self.userwdgfield.doubleSpinBox_diamsor,
                                                           'profondeur' : self.userwdgfield.doubleSpinBox_prof,
                                                            'nature_reseau': self.userwdgfield.comboBox_nature_reseau,
                                                        'pres_echelon': self.userwdgfield.comboBox_echelon,
                                                            #ventouse
                                                             'altimetrie': self.userwdgfield.doubleSpinBox_altim,
                                                            #vanne
                                                          'localisation': [self.userwdgfield.comboBox_localisation,
                                                                           self.userwdgfield.comboBox_localisation2],
                                                         'accessibilite': [self.userwdgfield.comboBox_accessibilite,
                                                                           self.userwdgfield.comboBox_accessibilite2],
                                                        'manipulable': self.userwdgfield.comboBox_manipulable,
                                                           'position': self.userwdgfield.comboBox_position,
                                                 #vidange
                                                 'exutoire': self.userwdgfield.lineEdit_exutoire,
                                                 #reg pression
                                                 'consigne_aval': self.userwdgfield.doubleSpinBox_cons_av,
                                                 'consigne_amont': self.userwdgfield.doubleSpinBox_cons_am,

                                                 # hydrant
                                                 'id_cana_sig_sdis': self.userwdgfield.spinBox_idsdis,
                                                 'marque': [self.userwdgfield.lineEdit_marque,
                                                            self.userwdgfield.lineEdit_marque2],
                                                 'type': self.userwdgfield.lineEdit_type,
                                                 'conformite': self.userwdgfield.comboBox_conformite,

                                                 #compteur"
                                                 'dimensions': self.userwdgfield.doubleSpinBox_dimensions,
                                                 'tete_emettrice': self.userwdgfield.comboBox_tete_emettrice,
                                                 'numero': self.userwdgfield.spinBox_numero,
                                                 'equipable': self.userwdgfield.comboBox_equipable,
                                                 #'localisation': self.userwdgfield.comboBox_localisation2,
                                                 #'accessibilite': self.userwdgfield.comboBox_accessibilite2,
                                                 # 'marque': self.userwdgfield.lineEdit_marque2,
                                                 # 'type': self.userwdgfield.lineEdit_type2,
                                                 'entreprise': [self.userwdgfield.lineEdit_entreprise,
                                                                self.userwdgfield.lineEdit_entreprise2],
                                                 'telerelevage': [self.userwdgfield.comboBox_telerelevage,
                                                                  self.userwdgfield.comboBox_telerelevage2],
                                                 'organes_associes': self.userwdgfield.lineEdit_organes_associes,

                                                 #chloration
                                                 #'entreprise': self.userwdgfield.lineEdit_entreprise2,
                                                 #'telerelevage': self.userwdgfield.comboBox_telerelevage2,
                                                 # robinet de prise en charge
                                                 'collier': self.userwdgfield.comboBox_collier,

                                                 'X': self.userwdgfield.doubleSpinBox_X,
                                                 'dX': self.userwdgfield.doubleSpinBox_dX,
                                                 'Y': self.userwdgfield.doubleSpinBox_Y,
                                                 'dY': self.userwdgfield.doubleSpinBox_dY,
                                                 'Z': self.userwdgfield.doubleSpinBox_Z,
                                                 'dZ': self.userwdgfield.doubleSpinBox_dZ


                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire': self.userwdgfield.textBrowser_comm}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                      'widgets' : {  'enservice': self.userwdgfield.comboBox_enservice,
                                                                     'annee_fin_pose': self.userwdgfield.dateEdit_anneepose}}}


            self.userwdgfield.toolButton_diam.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_diam))
            self.userwdgfield.toolButton_diamsor.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_diamsor))
            self.userwdgfield.toolButton_prof.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_prof))

            self.userwdgfield.toolButton_altim.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_altim))

            self.userwdgfield.toolButton_cons_am.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_cons_am))
            self.userwdgfield.toolButton_cons_av.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_cons_av))



            self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
            self.userwdgfield.pushButton_getGPS.clicked.connect(self.getGPSValue)

            self.allaccessfields = OrderedDict(self.dbasetable['fields']['acces'])


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            self.propertieswdgDesordre = BaseEaupotableDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil,
                                                                        parentwidget=self)
            self.propertieswdgDesordre.NAME = None
            self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            self.propertieswdgDesordre.userwdgfield.stackedWidget.setVisible(False)
            self.propertieswdgDesordre.groupBox_elements.setParent(None)
            self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.userwdgfield.tabWidget_2.widget(1).layout().addWidget(self.propertieswdgDesordre)

            self.dbasechildwdgfield.append(self.propertieswdgDesordre)


            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            if False and self.parentWidget is None:
                self.pushButton_addFeature.setEnabled(False)

        self.gpswidget = {'x' : {'widget' : self.userwdgfield.label_X,
                                 'gga' : 'Xcrs'},
                          'y': {'widget': self.userwdgfield.label_Y,
                                'gga': 'Ycrs'},
                          'zmngf': {'widget': self.userwdgfield.label_Z,
                                'gga': 'zmNGF'},
                          'dx': {'widget': self.userwdgfield.label_dX,
                                'gst': 'xprecision'},
                          'dy': {'widget': self.userwdgfield.label_dY,
                                'gst': 'yprecision'},
                          'dz': {'widget': self.userwdgfield.label_dZ,
                                'gst': 'zprecision'},
                          'zgps': {'widget': self.userwdgfield.label_zgps,
                                 'gga': 'elevation'},
                          'zwgs84': {'widget': self.userwdgfield.label_zwgs84,
                                   'gga': 'deltageoid'},
                          'raf09': {'widget': self.userwdgfield.label_raf09,
                                   'gga': 'RAF09'},
                          'hauteurperche': {'widget': self.userwdgfield.label_hautperche,
                                    'gga': 'hauteurperche'}
                          }


    def postInitFeatureProperties(self, feat):

        if self.currentFeaturePK is not None:
            lid_dessys = self.dbase.getValuesFromPk('Noeud_qgis',['lid_descriptionsystem_1'],self.currentFeaturePK)
            if lid_dessys is not None:
                self.userwdgfield.comboBox_acces.setEnabled(False)
            else:
                self.userwdgfield.comboBox_acces.setEnabled(True)
        else:
            self.userwdgfield.comboBox_acces.setEnabled(True)


        if (self.parentWidget is not None and self.parentWidget.currentFeature is not None
                and self.parentWidget.dbasetablename == 'Equipement'):

            type_ouvrage = self.dbase.getValuesFromPk('Equipement_qgis',
                                                        ['type_ouvrage'],
                                                        self.parentWidget.currentFeaturePK)

            if type_ouvrage == 'CHE':

                self.dbase.dbasetables['Noeud']['fields']['acces'] = OrderedDict([('PGtype', 'VARCHAR(255'),('ParFldCst','categorie'),('Cst',[[u'Chambre enterrée/regard', 'CHE',['','VEN','VAN','VID','REG','HYD','COM','CHL','RPC','SPE']]])])

                self.userwdgfield.comboBox_cat.currentIndexChanged.emit(self.userwdgfield.comboBox_cat.currentIndex())
                self.userwdgfield.comboBox_acces.setEnabled(False)

            else:
                if self.dbasetable['fields']['acces'] != self.allaccessfields:
                    self.dbasetable['fields']['acces'] = self.allaccessfields
                    self.userwdgfield.comboBox_cat.currentIndexChanged.emit(self.userwdgfield.comboBox_cat.currentIndex())
        else:
            if self.dbasetable['fields']['acces'] != self.allaccessfields:
                self.dbasetable['fields']['acces'] = self.allaccessfields
                self.userwdgfield.comboBox_cat.currentIndexChanged.emit(self.userwdgfield.comboBox_cat.currentIndex())


    def postSaveFeature(self, boolnewfeature):

        # save a disorder on first creation
        if self.savingnewfeature and not self.savingnewfeatureVersion:
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
                #newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
                # print('geom',qgsgeom.asWkt() )
                if qgsgeom.type() == 0: #point
                    newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
                elif qgsgeom.type() == 1: #line
                    aspoint = qgsgeom.asPolyline()[0]
                    newgeom = qgis.core.QgsGeometry.fromPolylineXY([aspoint, aspoint])
                newgeomwkt = newgeom.asWkt()

            sql = self.dbase.createSetValueSentence(type='INSERT',
                                                    tablename='Desordre',
                                                    listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                  'lid_descriptionsystem', 'geom'],
                                                    listofrawvalues=[lastiddesordre, pkobjet, 'NOD',
                                                                     iddessys, newgeomwkt])
            self.dbase.query(sql)





    def changeCategorie(self, intcat):
        if self.dbase.variante in [None, 'Lamia']:
            pagecount = self.userwdg.stackedWidget.count()
            if intcat >= pagecount -1 :
                self.userwdg.stackedWidget.setCurrentIndex(pagecount -1)
            else:
                self.userwdg.stackedWidget.setCurrentIndex(intcat)
        elif self.dbase.variante in ['Reseau_chaleur']:
            pagecount = self.userwdg.stackedWidget.count()
            currentindex = self.userwdgfield.comboBox_cat.currentIndex()
            if currentindex >= 2:
                self.userwdg.stackedWidget.setCurrentIndex(pagecount - 1)
            else:
                self.userwdg.stackedWidget.setCurrentIndex(intcat)


    def magicFunction(self):
        self.featureSelected()
        #self.lastPhoto()
        self.addGPSPoint()
        self.saveFeature()


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
        self.assignValue(self.userwdgfield.label_X, self.userwdgfield.doubleSpinBox_X)
        self.assignValue(self.userwdgfield.label_dX, self.userwdgfield.doubleSpinBox_dX)
        self.assignValue(self.userwdgfield.label_Y, self.userwdgfield.doubleSpinBox_Y)
        self.assignValue(self.userwdgfield.label_dY, self.userwdgfield.doubleSpinBox_dY)
        self.assignValue(self.userwdgfield.label_Z, self.userwdgfield.doubleSpinBox_Z)
        self.assignValue(self.userwdgfield.label_dZ, self.userwdgfield.doubleSpinBox_dZ)


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
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)

