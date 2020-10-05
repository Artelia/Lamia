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

from ..base2.lamiabase_equipement_tool import BaseEquipementTool
from .lamiabaseeaupotable_noeud_tool import BaseEaupotableNoeudTool
from .lamiabaseeaupotable_photo_tool import BaseEaupotablePhotoTool as BasePhotoTool
from .lamiabaseeaupotable_croquis_tool import BaseEaupotableCroquisTool as BaseCroquisTool
from .lamiabaseeaupotable_desordre_tool import BaseEaupotableDesordreTool





class BaseEaupotableEquipementTool(BaseEquipementTool):


    def __init__(self, **kwargs):
        super(BaseEaupotableEquipementTool, self).__init__(**kwargs)


    """
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
    """


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {'Equipement' : {'linkfield' : 'id_equipement',
                                            'widgets' : {'type_ouvrage' : self.toolwidgetmain.comboBox_typeouvrage,
                                                        'ss_type_ouv' :  self.toolwidgetmain.comboBox_sstype,

                                                        'h_mano_tot' : self.toolwidgetmain.doubleSpinBox_hmano,

                                                        'volume': self.toolwidgetmain.doubleSpinBox_volume,
                                                        'nbre_cuves': self.toolwidgetmain.spinBox_nbrecuves,
                                                        'cote_sql': self.toolwidgetmain.doubleSpinBox_cotesql,
                                                        'cote_radier': self.toolwidgetmain.doubleSpinBox_coteradier,
                                                        'cote_trop_plein': self.toolwidgetmain.doubleSpinBox_cotetp,

                                                        'diametre': self.toolwidgetmain.doubleSpinBox_diam,
                                                        'nb_compteur': self.toolwidgetmain.doubleSpinBox_nbrecompteur,
                                                        'fonctionnement': self.toolwidgetmain.comboBox_fonct,

                                                        'profondeur': self.toolwidgetmain.doubleSpinBox_prof,

                                                        'X': self.toolwidgetmain.doubleSpinBox_X,
                                                        'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                        'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                        'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                        'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                        'dZ': self.toolwidgetmain.doubleSpinBox_dZ,


                                                        }},
                                    'Objet': {'linkfield': 'id_objet',
                                                'widgets': {
                                                    'commentaire': self.toolwidgetmain.textBrowser_commentaire,
                                                    'libelle': self.toolwidgetmain.lineEdit_nom}},
                                    'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                            'widgets': {
                                                                'enservice': self.toolwidgetmain.comboBox_enservice,
                                                                'annee_fin_pose': self.toolwidgetmain.dateEdit_anneepose
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

        self.propertieswdgDesordre = BaseEaupotableDesordreTool(**self.instancekwargs)
        #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
        #self.propertieswdgDesordre.userwdgfield.stackedWidget.setVisible(False)
        #self.propertieswdgDesordre.groupBox_elements.setParent(None)
        #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
        #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
        #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
        #self.propertieswdgDesordre.groupBox_geom.setParent(None)
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)

        self.propertieswdgNoeud = BaseEaupotableNoeudTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgNoeud)

        self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


        self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)






        self.gpswidget = {'x' : {'widget' : self.toolwidgetmain.label_X,
                                    'gga' : 'Xcrs'},
                            'y': {'widget': self.toolwidgetmain.label_Y,
                                'gga': 'Ycrs'},
                            'zmngf': {'widget': self.toolwidgetmain.label_Z,
                                'gga': 'zmNGF'},
                            'dx': {'widget': self.toolwidgetmain.label_dX,
                                'gst': 'xprecision'},
                            'dy': {'widget': self.toolwidgetmain.label_dY,
                                'gst': 'yprecision'},
                            'dz': {'widget': self.toolwidgetmain.label_dZ,
                                'gst': 'zprecision'},
                            'zgps': {'widget': self.toolwidgetmain.label_zgps,
                                    'gga': 'elevation'},
                            'zwgs84': {'widget': self.toolwidgetmain.label_zwgs84,
                                    'gga': 'deltageoid'},
                            'raf09': {'widget': self.toolwidgetmain.label_raf09,
                                    'gga': 'RAF09'},
                            'hauteurperche': {'widget': self.toolwidgetmain.label_hautperche,
                                    'gga': 'hauteurperche'}
                            }






    def fielduiTypeOhChanged(self, comboindex):
        #print(self.toolwidgetmain.comboBox_typeOuvrageAss.currentText())
        currenttext = self.toolwidgetmain.comboBox_typeouvrage.currentText()

        if currenttext in ['Station de pompage']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
        elif currenttext in [u'Réservoir']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)
        elif currenttext in ['Chambre de comptage']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(2)
        elif currenttext in [u'Chambre enterrée/regard']:
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



        #self.dbase.dbasetables['Infralineaire']['layerqgis'].triggerRepaint()
        # save a disorder on first creation
        #if True and self.savingnewfeature and not self.savingnewfeatureVersion:
        if self.currentFeaturePK is None:
            self.propertieswdgDesordre.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('Equipement_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)

            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
            qgsgeomfordesordre = qgsgeom

            self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)

            self.currentFeaturePK = savedfeaturepk
            self.propertieswdgDesordre.toolbarSave()
            pkdesordre = self.propertieswdgDesordre.currentFeaturePK
            sql = "UPDATE Desordre SET groupedesordre = 'EQP' WHERE pk_desordre = {}".format(pkdesordre)
            self.dbase.query(sql)


            """
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
            """





class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)