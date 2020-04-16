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
from .lamiabaseeaupotable_equipement_tool import BaseEaupotableEquipementTool
from .lamiabaseeaupotable_desordre_tool import BaseEaupotableDesordreTool
import sys



class BaseAssainissementNoeudTool(BaseNoeudTool):

    LOADFIRST = True
    dbasetablename = 'Noeud'
    #specialfieldui = ['2']
    #workversionmin = '0_1'
    #workversionmax = '0_1'


    def __init__(self, **kwargs):
        super(BaseAssainissementNoeudTool, self).__init__(**kwargs)



    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Ouvrages'
        self.dbasetablename = 'Noeud'
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

        if False:
            self.initialtypeohassdict = list(self.dbase.dbasetables['Noeud']['fields']['typeOuvrageAss']['Cst'])
            self.modifiedtypeohassdict = []
            for cst in self.initialtypeohassdict:
                if cst[1] in ['','60', '70', '71','74', '21','22', '10', '40','51','00']:
                    self.modifiedtypeohassdict.append(cst)

        # ****************************************************************************************
        #properties ui
        pass



    def initMainToolWidget(self):
        # ****************************************************************************************
        # userui Desktop
        if self.toolwidgetmain is None:

            # ****************************************************************************************
            # userui
            self.toolwidgetmain = UserUI()
            """
            self.formtoolwidgetconfdictmain = {'Noeud' : {'linkfield' : 'id_noeud',
                                             'widgets' : {
                                                         'typeReseau': self.toolwidgetmain.comboBox_typeReseau,
                                                        'environnement' : self.toolwidgetmain.comboBox_environnement,
                                                         'typeOuvrageAss': self.toolwidgetmain.comboBox_typeOuvrageAss,
                                                        'formetampon': self.toolwidgetmain.comboBox_Formetampon,
                                                         'accessibilite': self.toolwidgetmain.comboBox_accessibilite,

                                                        #regard
                                                        'presenceechelon' : self.toolwidgetmain.comboBox_echelon,
                                                        'presencecrosse': self.toolwidgetmain.comboBox_crosse,
                                                         'presencecunette': self.toolwidgetmain.comboBox_cunette,
                                                        'formeregard': self.toolwidgetmain.comboBox_formeregard,

                                                        #branchement
                                                         'cloisonsiphoide': self.toolwidgetmain.comboBox_cloisonsiphoide,
                                                         'couvercle': self.toolwidgetmain.comboBox_couvercle,

                                                        #PR
                                                        'PRcloture': self.toolwidgetmain.comboBox_cloture,
                                                        'PRverouille': self.toolwidgetmain.comboBox_verouille,

                                                        'PRarmoireelec': self.toolwidgetmain.comboBox_posteelec,
                                                         'PRarmoireelecverouillee': self.toolwidgetmain.comboBox_armoire_verouille,
                                                        'PRtelegestion': [self.toolwidgetmain.comboBox_telegestion,self.toolwidgetmain.comboBox_DSHalarme],
                                                       'PRtelegestioncommentaire': self.toolwidgetmain.textBrowser_telegestioncom,
                                                       'PRpermutautopompe': self.toolwidgetmain.comboBox_permut_pompes,

                                                        'PRmateriau': [self.toolwidgetmain.comboBox_PRmateriau,self.toolwidgetmain.comboBox_DSH_materiau],
                                                        'PRgrilleantichute': self.toolwidgetmain.comboBox_antichute,
                                                       'PRpanierdegrilleur': self.toolwidgetmain.comboBox_panierdegrileur,

                                                         'PRtypeasservissementpompe': self.toolwidgetmain.comboBox_typeasservissement,
                                                         'PRnbrepoires': self.toolwidgetmain.spinBox_poires,
                                                         'PRsurverse': self.toolwidgetmain.comboBox_surverse,

                                                        'PRpompebarreguidage': self.toolwidgetmain.comboBox_barrresguidage,
                                                      'PRpompechainerelevage': self.toolwidgetmain.comboBox_pompe_relevage,
                                                         'PRnbrepompes': self.toolwidgetmain.spinBox_pompes,

                                                       'PRclapet': self.toolwidgetmain.comboBox_vanne_clapet,
                                                      'PRvannes': self.toolwidgetmain.comboBox_vanne_vanne,
                                                      'PRprisepression': self.toolwidgetmain.comboBox_vanne_prisepression,

                                                        #DSH
                                                        # DSH materiau : self.toolwidgetmain_2.comboBox_DSH_materiau cf PR
                                                        #'DSHpresencealarme': self.toolwidgetmain_2.comboBox_DSHalarme,
                                                         'presenceautomate': self.toolwidgetmain.comboBox_automate,


                                                        # autre
                                                        'profradierouvrage': self.toolwidgetmain.doubleSpinBox_profradierouvrage,
                                                         'largeur': self.toolwidgetmain.doubleSpinBox_largeur,
                                                         'longueur': self.toolwidgetmain.doubleSpinBox_longueur,

                                                         'X': self.toolwidgetmain.doubleSpinBox_X,
                                                         'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                         'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                         'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                         'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                         'dZ': self.toolwidgetmain.doubleSpinBox_dZ,


                                                        }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire' : self.toolwidgetmain.textBrowser_commentaire}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}
            """

            self.formtoolwidgetconfdictmain = {'Noeud' : {'linkfield' : 'id_noeud',
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

            self.propertieswdgEquipement = BaseEaupotableEquipementTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgEquipement)

            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




            if False:
                self.propertieswdgDesordre = BaseAssainissementDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
                self.propertieswdgDesordre.groupBox_elements.setParent(None)
                self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
                self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
                self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
                self.propertieswdgDesordre.groupBox_geom.setParent(None)
                self.dbasechildwdgfield.append(self.propertieswdgDesordre)

                self.propertieswdgEquipement = BaseAssainissementEquipementTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgEquipement)


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

        if False:
            self.dbase.dbasetables['Noeud']['fields']['typeOuvrageAss']['Cst'] = self.initialtypeohassdict






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


    def postSaveFeature(self, boolnewfeature):


        #adapt linked infralin geoemtry
        if False and self.currentFeature is not None:
            nodeiddessys = self.dbase.getValuesFromPk('Noeud_qgis','id_descriptionsystem',self.currentFeaturePK )
            nodegeom = self.currentFeature.geometry().asPoint()

        if False:

            # iterate on lid_descriptionsystem_1 and lid_descriptionsystem_2
            valuetoiterate = [1, 2]
            for indexnode in valuetoiterate:
                sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_qgis "
                sql += "WHERE lid_descriptionsystem_" + str(indexnode ) + " = " + str(nodeiddessys)
                sql += " AND "
                sql += self.dbase.dateVersionConstraintSQL()
                result = self.dbase.query(sql)
                if indexnode == 1 :
                    indexgeom = 0
                elif indexnode == 2:
                    indexgeom = -1

                for fetpk, fetid in result:
                    infrafet = self.dbase.getLayerFeatureByPk('Infralineaire', fetpk)
                    infrafetgeom = infrafet.geometry().asPolyline()

                    if not self.dbase.areNodesEquals(infrafetgeom[indexgeom], nodegeom):
                        self.dbase.createNewLineVersion('Infralineaire', fetpk)
                        fetpk = self.dbase.getLayerFeatureById('Infralineaire', fetid).id()
                        infrafetgeom[indexgeom] = nodegeom
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            newgeom = qgis.core.QgsGeometry.fromPolyline(infrafetgeom)
                        else:
                            newgeom = qgis.core.QgsGeometry.fromPolylineXY(infrafetgeom)
                        dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                        dbasetablelayer.startEditing()
                        success = dbasetablelayer.changeGeometry(fetpk, newgeom)
                        dbasetablelayer.commitChanges()
                        # move branchement
                        self.moveBranchement(fetpk, newgeom)






            if False:
                # sql = "SELECT id_infralineaire, lk_descriptionsystem1 FROM Infralineaire WHERE lk_descriptionsystem1 = " + str(nodedesys)
                sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_qgis WHERE lid_descriptionsystem_1 = " + str(nodeiddessys)
                sql += " AND "
                sql += self.dbase.dateVersionConstraintSQL()
                #query = self.dbase.query(sql)
                #result = [row[0] for row in query]
                result = self.dbase.query(sql)
                #for fetid,lknoeud1 in result:
                for fetpk, fetid in result:
                    # infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid)
                    infrafet = self.dbase.getLayerFeatureByPk('Infralineaire', fetpk)
                    infrafetgeom = infrafet.geometry().asPolyline()


                    #if infrafetgeom[0] != nodegeom :
                    if not self.dbase.areNodesEquals(infrafetgeom[0], nodegeom):
                        self.dbase.createNewLineVersion('Infralineaire', fetpk)
                        fetpk = self.dbase.getLayerFeatureById('Infralineaire', fetid).id()

                        infrafetgeom[0] = nodegeom

                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            newgeom = qgis.core.QgsGeometry.fromPolyline(infrafetgeom)
                        else:
                            newgeom = qgis.core.QgsGeometry.fromPolylineXY(infrafetgeom)

                        dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                        dbasetablelayer.startEditing()
                        success = dbasetablelayer.changeGeometry(fetpk, newgeom)
                        dbasetablelayer.commitChanges()

                        #move branchement
                        self.moveBranchement(fetpk, newgeom)
                        if False:
                            if False:
                                sql = " SELECT id_descriptionsystem FROM Infralineaire_qgis WHERE pk_infralineaire = " + str(fetpk)
                                sql += " AND "
                                sql += self.dbase.dateVersionConstraintSQL()
                                fetiddessys = self.dbase.query(sql)[0][0]
                            fetiddessys = self.dbase.getValuesFromPk('Infralineaire_qgis','id_descriptionsystem', fetpk )

                            # sql = "SELECT id_infralineaire FROM Infralineaire WHERE lk_descriptionsystem2 = " + str(infrafet['id_descriptionsystem'])
                            sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_qgis WHERE lid_descriptionsystem_2 = " + str(fetiddessys)
                            sql += " AND "
                            sql += self.dbase.dateVersionConstraintSQL()
                            #query = self.dbase.query(sql)
                            #result2 = [row[0] for row in query]
                            result2 = self.dbase.query(sql)
                            #for fetid2 in result2:
                            for fetpk2, fetid2 in result2:
                                #infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid2)
                                infrafet = self.dbase.getLayerFeatureByPk('Infralineaire', fetpk2)
                                infrafetpoint1 = qgis.core.QgsGeometry().fromPoint(infrafet.geometry().asPolyline()[0])
                                # newgeom2 = newgeom.shortestLine(infrafetpoint1)
                                newgeom2 = infrafetpoint1.shortestLine(newgeom)
                                dbasetablelayer.startEditing()
                                success = dbasetablelayer.changeGeometry(fetpk2, newgeom2)
                                if False:
                                    if not self.dbase.revisionwork:
                                        success = dbasetablelayer.changeGeometry(fetid2, newgeom2)
                                    else:
                                        success = dbasetablelayer.changeGeometry(infrafet.id(), newgeom2)
                                dbasetablelayer.commitChanges()




                    movebranchement = True
                    # print('lk1', success, fetid, newgeom.asPolyline())

                # sql = "SELECT id_infralineaire, lk_descriptionsystem2 FROM Infralineaire WHERE lk_descriptionsystem2 = " + str(nodedesys)
                sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_qgis WHERE lid_descriptionsystem_2 = " + str(nodeiddessys)
                sql += " AND "
                sql += self.dbase.dateVersionConstraintSQL()
                query = self.dbase.query(sql)
                result = [row[0] for row in query]

                #for fetid,lknoeud2 in result:
                for fetpk, fetid in result:
                    # infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid)
                    infrafet = self.dbase.getLayerFeatureByPk('Infralineaire', fetpk)
                    infrafetgeom = infrafet.geometry().asPolyline()
                    # infrafetgeom[1] = nodegeom


                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        newgeom = qgis.core.QgsGeometry.fromPolyline(infrafetgeom)
                    else:
                        newgeom = qgis.core.QgsGeometry.fromPolylineXY(infrafetgeom)

                    if not self.dbase.areNodesEquals(infrafetgeom[1], nodegeom):
                        self.dbase.createNewLineVersion('Infralineaire', fetpk)
                        fetpk = self.dbase.getLayerFeatureById('Infralineaire', fetid).id()

                        infrafetgeom[1] = nodegeom

                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            newgeom = qgis.core.QgsGeometry.fromPolyline(infrafetgeom)
                        else:
                            newgeom = qgis.core.QgsGeometry.fromPolylineXY(infrafetgeom)

                        dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                        dbasetablelayer.startEditing()
                        success = dbasetablelayer.changeGeometry(fetpk, newgeom)
                        dbasetablelayer.commitChanges()

                        #move branchement
                        self.moveBranchement(fetpk, newgeom)

                    if False:
                        dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                        dbasetablelayer.startEditing()
                        success = dbasetablelayer.changeGeometry(fetpk, newgeom)
                        if False:
                            if not self.dbase.revisionwork:
                                success = dbasetablelayer.changeGeometry(fetid, newgeom)
                            else:
                                success = dbasetablelayer.changeGeometry(infrafet.id(), newgeom)
                        dbasetablelayer.commitChanges()

                        #move branchement
                        self.moveBranchement(fetpk, newgeom)
                        if False:

                            sql = " SELECT id_descriptionsystem FROM Infralineaire_qgis WHERE pk_infralineaire = " + str(fetpk)
                            sql += " AND "
                            sql += self.dbase.dateVersionConstraintSQL()
                            fetiddessys = self.dbase.query(sql)[0][0]

                            #sql = "SELECT id_infralineaire FROM Infralineaire WHERE lk_descriptionsystem2 = " + str(infrafet['id_descriptionsystem'])
                            sql = "SELECT pk_infralineaire FROM Infralineaire_qgis WHERE lid_descriptionsystem_2 = " + str(fetiddessys)
                            sql += " AND "
                            sql += self.dbase.dateVersionConstraintSQL()

                            query = self.dbase.query(sql)
                            result2 = [row[0] for row in query]
                            #for fetid2 in result2:
                            for fetpk2 in result2:
                                #infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid2)
                                infrafet = self.dbase.getLayerFeatureByPk('Infralineaire', fetpk2)
                                infrafetpoint1 = qgis.core.QgsGeometry().fromPoint(infrafet.geometry().asPolyline()[0])
                                # newgeom2 = newgeom.shortestLine(infrafetpoint1)
                                newgeom2 = infrafetpoint1.shortestLine(newgeom)
                                dbasetablelayer.startEditing()
                                success = dbasetablelayer.changeGeometry(fetpk2, newgeom2)
                                if False:
                                    if not self.dbase.revisionwork:
                                        success = dbasetablelayer.changeGeometry(fetid2, newgeom2)
                                    else:
                                        success = dbasetablelayer.changeGeometry(infrafet.id(), newgeom2)
                                dbasetablelayer.commitChanges()

                # self.linkedgeom = [{'Equipement': 'lid_descriptionsystem'}]
                if False:
                    #sql = "SELECT id_equipement FROM Equipement WHERE lk_descriptionsystem = " + str(nodedesys)
                    sql = "SELECT pk_equipement FROM Equipement_qgis WHERE lid_descriptionsystem = "  + str(nodeiddessys)
                    sql += " AND "
                    sql += self.dbase.dateVersionConstraintSQL()
                    query = self.dbase.query(sql)
                    result = [row[0] for row in query]

                    #for fetid in result:
                    for fetpk in result:
                        # equipfet = self.dbase.getLayerFeatureById('Equipement', fetid)
                        equipfet = self.dbase.getLayerFeatureByPk('Equipement', fetpk)
                        #infrafetgeom = equipfet.geometry().asPoint()
                        #infrafetgeom[1] = nodegeom


                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            newgeom = qgis.core.QgsGeometry.fromPolyline([nodegeom,nodegeom])
                        else:
                            newgeom = qgis.core.QgsGeometry.fromPolylineXY([nodegeom,nodegeom])

                        dbasetablelayer = self.dbase.dbasetables['Equipement']['layer']
                        dbasetablelayer.startEditing()
                        success = dbasetablelayer.changeGeometry(fetpk, newgeom)
                        if False:
                            if not self.dbase.revisionwork:
                                success = dbasetablelayer.changeGeometry(fetid, newgeom)
                            else:
                                success = dbasetablelayer.changeGeometry(equipfet.id(), newgeom)
                        dbasetablelayer.commitChanges()

                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        self.canvas.refresh()
                    else:
                        self.canvas.refreshAllLayers()



        self.dbase.dbasetables['Infralineaire']['layerqgis'].triggerRepaint()
        # save a disorder on first creation
        if True and self.savingnewfeature and not self.savingnewfeatureVersion:
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

        if False and self.currentFeature is not None:
            if  hasattr(self, 'userwdgfield_2') and self.userwdg == self.toolwidgetmain_2:
                libelle=''
                sql = "SELECT typeOuvrageAss,typeReseau ,id_noeud  FROM Noeud WHERE pk_noeud = " + str(self.currentFeaturePK)
                typeouvrage, typereseau, idnoeud = self.dbase.query(sql)[0]
                if typeouvrage in ['60', '70', '71']:
                    libelle += "R"
                    if typereseau == 'PLU':
                        libelle += "P"
                    elif typereseau == 'USE':
                        libelle += "V"
                    elif typereseau == 'UNI':
                        libelle += "U"
                    elif typereseau == 'IND':
                        libelle += "I"

                elif typeouvrage in ['10']:
                    libelle += "POR"

                elif typeouvrage in ['22']:
                    libelle += "FOS"
                elif typeouvrage in ['51']:
                    libelle += "PUI"

                elif typeouvrage in ['21']:
                    libelle += "DSH"

                else:
                    libelle += "DIV"

                libelle += '_' + str(self.dbase.getValuesFromPk('Noeud_qgis','id_noeud',self.currentFeaturePK ))

                pkobjet = self.dbase.getValuesFromPk('Noeud_qgis','pk_objet',self.currentFeaturePK )

                sql = "UPDATE Objet SET libelle = '" + libelle + "' WHERE pk_objet = " + str(pkobjet)
                self.dbase.query(sql)
                self.toolwidgetmain_2.lineEdit_libelle.setText(libelle)




    def moveBranchement(self, pkinfralin, newgeom):

        fetiddessys = self.dbase.getValuesFromPk('Infralineaire_qgis', 'id_descriptionsystem', pkinfralin)
        dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
        print('moveBranchement1', pkinfralin, fetiddessys)
        # sql = "SELECT id_infralineaire FROM Infralineaire WHERE lk_descriptionsystem2 = " + str(infrafet['id_descriptionsystem'])
        sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_qgis WHERE lid_descriptionsystem_2 = " + str( fetiddessys)
        sql += " AND "
        sql += self.dbase.dateVersionConstraintSQL()
        # query = self.dbase.query(sql)
        # result2 = [row[0] for row in query]
        result2 = self.dbase.query(sql)
        # for fetid2 in result2:
        for fetpk2, fetid2 in result2:
            print('moveBranchement2',fetpk2,fetid2 )
            # infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid2)
            self.dbase.createNewLineVersion('Infralineaire', fetpk2)
            fetpk2 = self.dbase.getLayerFeatureById('Infralineaire', fetid2).id()
            infrafet = self.dbase.getLayerFeatureByPk('Infralineaire', fetpk2)
            infrafetpoint1 = qgis.core.QgsGeometry().fromPoint(infrafet.geometry().asPolyline()[0])
            # newgeom2 = newgeom.shortestLine(infrafetpoint1)
            newgeom2 = infrafetpoint1.shortestLine(newgeom)
            dbasetablelayer.startEditing()
            success = dbasetablelayer.changeGeometry(fetpk2, newgeom2)
            dbasetablelayer.commitChanges()


    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    # def postInitFeatureProperties(self, feat): 
def postSelectFeature(self):
        pass

    def createParentFeature(self):
        lastrevision = self.dbase.maxrevision
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idobjet = self.dbase.getLastRowId('Objet')



        #sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, id_revisionbegin, id_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(lastrevision) +  "," + str(lastobjetid) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idsys = self.dbase.getLastRowId('Descriptionsystem')

        idnoeud = self.currentFeature.id()
        lastidnoeud = self.dbase.getLastId('Noeud') + 1


        sql = "UPDATE Noeud SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_descriptionsystem = " + str(lastdescriptionsystemid)   + ","
        sql += "id_noeud = " + str(lastidnoeud)  + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_noeud = " + str(idnoeud) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()




    def postSaveFeature(self, boolnewfeature):
        pass


    def postDeleteFeature(self):
        pass

    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']
        # idnoeud= self.currentFeature['id_noeud']


        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        return True
    """







class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)

