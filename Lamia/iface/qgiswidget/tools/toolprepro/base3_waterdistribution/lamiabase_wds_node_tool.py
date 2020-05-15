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


class BaseWaterdistributionNodeTool(BaseNodeTool):


    def __init__(self, **kwargs):
        super(BaseWaterdistributionNodeTool, self).__init__(**kwargs)

    """
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
    """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Noeud' : {'linkfield' : 'id_noeud',
                                            'widgets' : {
                                                        'categorie': self.toolwidgetmain.comboBox_cat,
                                                        'fonction': self.toolwidgetmain.comboBox_fonction,
                                                        'ss_type_equipement': self.toolwidgetmain.comboBox_soustype,
                                                        'acces': self.toolwidgetmain.comboBox_acces,
                                                        'forme_acces': self.toolwidgetmain.comboBox_formeaccess,
                                                        'diametre_entree': self.toolwidgetmain.doubleSpinBox_diam,
                                                        'diametre_sortie': self.toolwidgetmain.doubleSpinBox_diamsor,
                                                        'profondeur' : self.toolwidgetmain.doubleSpinBox_prof,
                                                        'nature_reseau': self.toolwidgetmain.comboBox_nature_reseau,
                                                    'pres_echelon': self.toolwidgetmain.comboBox_echelon,
                                                        #ventouse
                                                            'altimetrie': self.toolwidgetmain.doubleSpinBox_altim,
                                                        #vanne
                                                        'localisation': [self.toolwidgetmain.comboBox_localisation,
                                                                        self.toolwidgetmain.comboBox_localisation2],
                                                        'accessibilite': [self.toolwidgetmain.comboBox_accessibilite,
                                                                        self.toolwidgetmain.comboBox_accessibilite2],
                                                    'manipulable': self.toolwidgetmain.comboBox_manipulable,
                                                        'position': self.toolwidgetmain.comboBox_position,
                                                #vidange
                                                'exutoire': self.toolwidgetmain.lineEdit_exutoire,
                                                #reg pression
                                                'consigne_aval': self.toolwidgetmain.doubleSpinBox_cons_av,
                                                'consigne_amont': self.toolwidgetmain.doubleSpinBox_cons_am,

                                                # hydrant
                                                'id_cana_sig_sdis': self.toolwidgetmain.spinBox_idsdis,
                                                'marque': [self.toolwidgetmain.lineEdit_marque,
                                                        self.toolwidgetmain.lineEdit_marque2],
                                                'type': self.toolwidgetmain.lineEdit_type,
                                                'conformite': self.toolwidgetmain.comboBox_conformite,

                                                #compteur"
                                                'dimensions': self.toolwidgetmain.doubleSpinBox_dimensions,
                                                'tete_emettrice': self.toolwidgetmain.comboBox_tete_emettrice,
                                                'numero': self.toolwidgetmain.spinBox_numero,
                                                'equipable': self.toolwidgetmain.comboBox_equipable,
                                                #'localisation': self.toolwidgetmain.comboBox_localisation2,
                                                #'accessibilite': self.toolwidgetmain.comboBox_accessibilite2,
                                                # 'marque': self.toolwidgetmain.lineEdit_marque2,
                                                # 'type': self.toolwidgetmain.lineEdit_type2,
                                                'entreprise': [self.toolwidgetmain.lineEdit_entreprise,
                                                            self.toolwidgetmain.lineEdit_entreprise2],
                                                'telerelevage': [self.toolwidgetmain.comboBox_telerelevage,
                                                                self.toolwidgetmain.comboBox_telerelevage2],
                                                'organes_associes': self.toolwidgetmain.lineEdit_organes_associes,

                                                #chloration
                                                #'entreprise': self.toolwidgetmain.lineEdit_entreprise2,
                                                #'telerelevage': self.toolwidgetmain.comboBox_telerelevage2,
                                                # robinet de prise en charge
                                                'collier': self.toolwidgetmain.comboBox_collier,

                                                'X': self.toolwidgetmain.doubleSpinBox_X,
                                                'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                'dZ': self.toolwidgetmain.doubleSpinBox_dZ


                                                        }},
                            'Objet' : {'linkfield' : 'id_objet',
                                        'widgets' : {'commentaire': self.toolwidgetmain.textBrowser_comm}},
                            'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                    'widgets' : {  'enservice': self.toolwidgetmain.comboBox_enservice,
                                                                    'annee_fin_pose': self.toolwidgetmain.dateEdit_anneepose}}}


        self.toolwidgetmain.toolButton_diam.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diam))
        self.toolwidgetmain.toolButton_diamsor.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diamsor))
        self.toolwidgetmain.toolButton_prof.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_prof))

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

        self.dbasechildwdgfield.append(self.propertieswdgDesordre)


        self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

        self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
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


    # def postInitFeatureProperties(self, feat): 
    def postSelectFeature(self):

        dbasetable = self.dbase.dbasetables['Noeud']

        if self.currentFeaturePK is not None:
            lid_dessys = self.dbase.getValuesFromPk('Noeud_qgis',['lid_descriptionsystem_1'],self.currentFeaturePK)
            if lid_dessys is not None:
                self.toolwidgetmain.comboBox_acces.setEnabled(False)
            else:
                self.toolwidgetmain.comboBox_acces.setEnabled(True)
        else:
            self.toolwidgetmain.comboBox_acces.setEnabled(True)


        if (self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None
                and self.parentWidget.DBASETABLENAME == 'Equipement'):

            type_ouvrage = self.dbase.getValuesFromPk('Equipement_qgis',
                                                        ['type_ouvrage'],
                                                        self.parentWidget.currentFeaturePK)

            if type_ouvrage == 'CHE':

                dbasetable['fields']['acces'] = OrderedDict([('PGtype', 'VARCHAR(255'),('ParFldCst','categorie'),('Cst',[[u'Chambre enterrée/regard', 'CHE',['','VEN','VAN','VID','REG','HYD','COM','CHL','RPC','SPE']]])])

                self.toolwidgetmain.comboBox_cat.currentIndexChanged.emit(self.toolwidgetmain.comboBox_cat.currentIndex())
                self.toolwidgetmain.comboBox_acces.setEnabled(False)

            else:
                if dbasetable['fields']['acces'] != self.allaccessfields:
                    dbasetable['fields']['acces'] = self.allaccessfields
                    self.toolwidgetmain.comboBox_cat.currentIndexChanged.emit(self.toolwidgetmain.comboBox_cat.currentIndex())
        else:
            if dbasetable['fields']['acces'] != self.allaccessfields:
                dbasetable['fields']['acces'] = self.allaccessfields
                self.toolwidgetmain.comboBox_cat.currentIndexChanged.emit(self.toolwidgetmain.comboBox_cat.currentIndex())


    def postSaveFeature(self, savedfeaturepk=None):

        # save a disorder on first creation
        #if self.savingnewfeature and not self.savingnewfeatureVersion:

        if self.currentFeaturePK is None:
            self.propertieswdgDesordre.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('Noeud_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)

            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
            qgsgeomfordesordre = [qgsgeom,qgsgeom]

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
            """




    def changeCategorie(self, intcat):

        typeeqt = self.toolwidgetmain.comboBox_cat.itemText(intcat)
        rawtypeeqt = self.dbase.getConstraintRawValueFromText('Noeud', 'categorie', typeeqt)
        pagecount = self.toolwidgetmain.stackedWidget.count()
        for pageindex in range(pagecount):
            wdgname = self.toolwidgetmain.stackedWidget.widget(pageindex).objectName()
            if wdgname == rawtypeeqt:
                self.toolwidgetmain.stackedWidget.setCurrentIndex(pageindex)
                return
        self.toolwidgetmain.stackedWidget.setCurrentIndex(pagecount)


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








class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_wds_node_tool_ui.ui')
        uic.loadUi(uipath, self)

