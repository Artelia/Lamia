# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseAssainissementNoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)



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
        self.iconpath = os.path.join(os.path.dirname(__file__),'..','base', 'lamiabase_noeud_tool_icon.svg')
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



    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            """
            self.linkuserwdgfield = {'Noeud' : {'linkfield' : 'id_noeud',
                                             'widgets' : {
                                                         'typeReseau': self.userwdgfield.comboBox_typeReseau,
                                                        'environnement' : self.userwdgfield.comboBox_environnement,
                                                         'typeOuvrageAss': self.userwdgfield.comboBox_typeOuvrageAss,
                                                        'formetampon': self.userwdgfield.comboBox_Formetampon,
                                                         'accessibilite': self.userwdgfield.comboBox_accessibilite,

                                                        #regard
                                                        'presenceechelon' : self.userwdgfield.comboBox_echelon,
                                                        'presencecrosse': self.userwdgfield.comboBox_crosse,
                                                         'presencecunette': self.userwdgfield.comboBox_cunette,
                                                        'formeregard': self.userwdgfield.comboBox_formeregard,

                                                        #branchement
                                                         'cloisonsiphoide': self.userwdgfield.comboBox_cloisonsiphoide,
                                                         'couvercle': self.userwdgfield.comboBox_couvercle,

                                                        #PR
                                                        'PRcloture': self.userwdgfield.comboBox_cloture,
                                                        'PRverouille': self.userwdgfield.comboBox_verouille,

                                                        'PRarmoireelec': self.userwdgfield.comboBox_posteelec,
                                                         'PRarmoireelecverouillee': self.userwdgfield.comboBox_armoire_verouille,
                                                        'PRtelegestion': [self.userwdgfield.comboBox_telegestion,self.userwdgfield.comboBox_DSHalarme],
                                                       'PRtelegestioncommentaire': self.userwdgfield.textBrowser_telegestioncom,
                                                       'PRpermutautopompe': self.userwdgfield.comboBox_permut_pompes,

                                                        'PRmateriau': [self.userwdgfield.comboBox_PRmateriau,self.userwdgfield.comboBox_DSH_materiau],
                                                        'PRgrilleantichute': self.userwdgfield.comboBox_antichute,
                                                       'PRpanierdegrilleur': self.userwdgfield.comboBox_panierdegrileur,

                                                         'PRtypeasservissementpompe': self.userwdgfield.comboBox_typeasservissement,
                                                         'PRnbrepoires': self.userwdgfield.spinBox_poires,
                                                         'PRsurverse': self.userwdgfield.comboBox_surverse,

                                                        'PRpompebarreguidage': self.userwdgfield.comboBox_barrresguidage,
                                                      'PRpompechainerelevage': self.userwdgfield.comboBox_pompe_relevage,
                                                         'PRnbrepompes': self.userwdgfield.spinBox_pompes,

                                                       'PRclapet': self.userwdgfield.comboBox_vanne_clapet,
                                                      'PRvannes': self.userwdgfield.comboBox_vanne_vanne,
                                                      'PRprisepression': self.userwdgfield.comboBox_vanne_prisepression,

                                                        #DSH
                                                        # DSH materiau : self.userwdgfield_2.comboBox_DSH_materiau cf PR
                                                        #'DSHpresencealarme': self.userwdgfield_2.comboBox_DSHalarme,
                                                         'presenceautomate': self.userwdgfield.comboBox_automate,


                                                        # autre
                                                        'profradierouvrage': self.userwdgfield.doubleSpinBox_profradierouvrage,
                                                         'largeur': self.userwdgfield.doubleSpinBox_largeur,
                                                         'longueur': self.userwdgfield.doubleSpinBox_longueur,

                                                         'X': self.userwdgfield.doubleSpinBox_X,
                                                         'dX': self.userwdgfield.doubleSpinBox_dX,
                                                         'Y': self.userwdgfield.doubleSpinBox_Y,
                                                         'dY': self.userwdgfield.doubleSpinBox_dY,
                                                         'Z': self.userwdgfield.doubleSpinBox_Z,
                                                         'dZ': self.userwdgfield.doubleSpinBox_dZ,


                                                        }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire' : self.userwdgfield.textBrowser_commentaire}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}
            """

            self.linkuserwdgfield = {'Noeud' : {'linkfield' : 'id_noeud',
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

                                                          'profondeur': self.userwdgfield.doubleSpinBox_prof

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

        if False:
            self.dbase.dbasetables['Noeud']['fields']['typeOuvrageAss']['Cst'] = self.initialtypeohassdict






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
            if  hasattr(self, 'userwdgfield_2') and self.userwdg == self.userwdgfield_2:
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
                self.userwdgfield_2.lineEdit_libelle.setText(libelle)




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



    def postInitFeatureProperties(self, feat):
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

