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




import qgis
from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_equipement_tool import BaseEquipementTool

# from ..base.lamiabase_photo_tool import BasePhotoTool
# from ..base.lamiabase_croquis_tool import BaseCroquisTool
from .lamiabaseeaupotable_noeud_tool import BaseEaupotableNoeudTool
from .lamiabaseeaupotable_photo_tool import BaseEaupotablePhotoTool as BasePhotoTool
from .lamiabaseeaupotable_croquis_tool import BaseEaupotableCroquisTool as BaseCroquisTool
from .lamiabaseeaupotable_desordre_tool import BaseEaupotableDesordreTool

import os
import datetime
from collections import OrderedDict



class BaseEaupotableEquipementTool(BaseEquipementTool):

    LOADFIRST = True
    dbasetablename = 'Equipement'



    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseEaupotableEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)



    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Ouvrages'
        self.dbasetablename = 'Equipement'
        self.visualmode = [0, 1, 2]
        self.PointENABLED = True
        # self.LineENABLED = False
        # self.PolygonENABLED = True
        self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_noeud_tool_icon.png')
        # self.linkedgeom = [['Equipement', 'lid_descriptionsystem'],['Desordre', 'lid_descriptionsystem']]

        self.linkagespec = {'Descriptionsystem': {'tabletc': None,
                                           'idsource': 'lid_descriptionsystem_1',
                                           'idtcsource': None,
                                           'iddest': 'id_descriptionsystem',
                                           'idtcdest': None,
                                           'desttable': ['Equipement','Noeud']}}



        # ****************************************************************************************
        #properties ui
        pass



    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()

            self.linkuserwdgfield = {'Equipement' : {'linkfield' : 'id_equipement',
                                             'widgets' : {'type_ouvrage' : self.userwdgfield.comboBox_typeouvrage,
                                                          'ss_type_ouv' :  self.userwdgfield.comboBox_sstype,

                                                          'h_mano_tot' : self.userwdgfield.doubleSpinBox_hmano,

                                                          'volume': self.userwdgfield.doubleSpinBox_volume,
                                                          'nbre_cuves': self.userwdgfield.spinBox_nbrecuves,
                                                          'cote_sql': self.userwdgfield.doubleSpinBox_cotesql,
                                                          'cote_radier': self.userwdgfield.doubleSpinBox_coteradier,
                                                          'cote_trop_plein': self.userwdgfield.doubleSpinBox_cotetp,

                                                          'diametre': self.userwdgfield.doubleSpinBox_diam,
                                                          'nb_compteur': self.userwdgfield.doubleSpinBox_nbrecompteur,
                                                          'fonctionnement': self.userwdgfield.comboBox_fonct,

                                                          'profondeur': self.userwdgfield.doubleSpinBox_prof,

                                                          'X': self.userwdgfield.doubleSpinBox_X,
                                                          'dX': self.userwdgfield.doubleSpinBox_dX,
                                                          'Y': self.userwdgfield.doubleSpinBox_Y,
                                                          'dY': self.userwdgfield.doubleSpinBox_dY,
                                                          'Z': self.userwdgfield.doubleSpinBox_Z,
                                                          'dZ': self.userwdgfield.doubleSpinBox_dZ,


                                                          }},
                                        'Objet': {'linkfield': 'id_objet',
                                                  'widgets': {
                                                      'commentaire': self.userwdgfield.textBrowser_commentaire,
                                                        'libelle': self.userwdgfield.lineEdit_nom}},
                                        'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                              'widgets': {
                                                                    'enservice': self.userwdgfield.comboBox_enservice,
                                                                  'annee_fin_pose': self.userwdgfield.dateEdit_anneepose
                                                                          }}}


            self.userwdgfield.toolButton_hmano.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_hmano))

            self.userwdgfield.toolButton_volume.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_volume))
            self.userwdgfield.toolButton_nbrecuve.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nbrecuves))

            self.userwdgfield.toolButton_cotesql.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_cotesql))
            self.userwdgfield.toolButton_coteradier.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_coteradier))
            self.userwdgfield.toolButton_cotetp.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_cotetp))

            self.userwdgfield.toolButton_diam.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_diam))
            self.userwdgfield.toolButton_nbrecompteur.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_nbrecompteur))

            self.userwdgfield.toolButton_prof.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_prof))



            self.userwdgfield.comboBox_typeouvrage.currentIndexChanged.connect(self.fielduiTypeOhChanged)

            self.userwdgfield.pushButton_getGPS.clicked.connect(self.getGPSValue)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            self.propertieswdgDesordre = BaseEaupotableDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil,
                                                                        parentwidget=self)
            self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            self.propertieswdgDesordre.userwdgfield.stackedWidget.setVisible(False)
            self.propertieswdgDesordre.groupBox_elements.setParent(None)
            self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)

            self.propertieswdgNoeud = BaseEaupotableNoeudTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgNoeud)

            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)






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






    def fielduiTypeOhChanged(self, comboindex):
        #print(self.userwdgfield.comboBox_typeOuvrageAss.currentText())
        currenttext = self.userwdgfield.comboBox_typeouvrage.currentText()

        if currenttext in ['Station de pompage']:
            self.userwdgfield.stackedWidget.setCurrentIndex(0)
        elif currenttext in [u'Réservoir']:
            self.userwdgfield.stackedWidget.setCurrentIndex(1)
        elif currenttext in ['Chambre de comptage']:
            self.userwdgfield.stackedWidget.setCurrentIndex(2)
        elif currenttext in [u'Chambre enterrée/regard']:
            self.userwdgfield.stackedWidget.setCurrentIndex(3)
        else:
            self.userwdgfield.stackedWidget.setCurrentIndex(4)


        #self.propertieswdgDesordre.propertieswdgOBSERVATION2.updateObservationStackedWidget()





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


    def postSaveFeature(self, boolnewfeature):



        self.dbase.dbasetables['Infralineaire']['layerqgis'].triggerRepaint()
        # save a disorder on first creation
        if True and self.savingnewfeature and not self.savingnewfeatureVersion:
            pkobjet = self.dbase.createNewObjet()
            lastiddesordre = self.dbase.getLastId('Desordre') + 1
            geomtext, iddessys = self.dbase.getValuesFromPk('Equipement_qgis',
                                                            ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                            self.currentFeaturePK)
            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                newgeom = qgis.core.QgsGeometry.fromPolyline([qgsgeom.asPoint(), qgsgeom.asPoint()])
                newgeomwkt = newgeom.exportToWkt()
            else:
                #newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPointXY(), qgsgeom.asPointXY()])
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
                                                    listofrawvalues=[lastiddesordre, pkobjet, 'EQP',
                                                                     iddessys, newgeomwkt])
            self.dbase.query(sql)






class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)