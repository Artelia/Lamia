# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QPushButton)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QPushButton)

from ..base2.lamiabase_noeud_tool import BaseNoeudTool

import os
import qgis
from collections import OrderedDict
import datetime

from .lamiabaseeclairagepublic_photo_tool import BaseEclairagePublicPhotoTool as BasePhotoTool
from .lamiabaseeclairagepublic_croquis_tool import BaseEclairagePublicCroquisTool as BaseCroquisTool
from .lamiabaseeclairagepublic_equipement_tool import BaseEclairagePublicEquipementTool
from .lamiabaseeclairagepublic_desordre_tool import BaseEclairagePublicDesordreTool



class BaseEclairagePublicNoeudTool(BaseNoeudTool):

    LOADFIRST = True
    dbasetablename = 'Noeud'
    #specialfieldui = ['2']
    #workversionmin = '0_1'
    #workversionmax = '0_1'


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseEclairagePublicNoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)



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


    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.dbase.variante in [None, 'Lamia']:
            if self.userwdgfield is None:


                # ****************************************************************************************
                # userui
                self.userwdgfield = UserUI()

                self.linkuserwdgfield = {'Noeud': {'linkfield': 'id_noeud',
                                                   'widgets': OrderedDict([
                                                       ('typenoeud', self.userwdgfield.comboBox_typenoeud),

                                                       ('contrat', self.userwdgfield.lineEdit_contrat),
                                                       ('pdl', self.userwdgfield.lineEdit_achemin),
                                                       ('typalim', self.userwdgfield.comboBox_typealim),

                                                       ('cptind', self.userwdgfield.comboBox_coff_indep),
                                                       ('typecpt', self.userwdgfield.comboBox_typecompt),
                                                       ('numcomp', self.userwdgfield.lineEdit_numcompt),
                                                       ('ttprtcpt', self.userwdgfield.comboBox_type_protect),
                                                       ('calprtcpt', self.userwdgfield.lineEdit_calibre_compt),

                                                       ('difdjbr', self.userwdgfield.comboBox_diffcomptbranch),
                                                       ('modposen', self.userwdgfield.comboBox_modeposeenv),
                                                       ('typen', self.userwdgfield.comboBox_typeenv),

                                                       ('fermen', self.userwdgfield.comboBox_ferenv),
                                                       ('prtgen', self.userwdgfield.comboBox_typeprogen),
                                                       ('calprtgen', self.userwdgfield.lineEdit_calprogen),
                                                       ('difdjgen', self.userwdgfield.comboBox_difprogen),
                                                       ('presur', self.userwdgfield.comboBox_prespara),
                                                       ('pre', self.userwdgfield.lineEdit_valpristerre),
                                                       ('miseter', self.userwdgfield.comboBox_misterrearmoire),

                                                       ('var', self.userwdgfield.comboBox_presvar),
                                                       ('typvar', self.userwdgfield.lineEdit_typevar),
                                                       ('puisvar', self.userwdgfield.spinBox_puissvar),
                                                       ('foncall', self.userwdgfield.comboBox_fonceclai),
                                                       ('typall', self.userwdgfield.comboBox_typeallu),
                                                       ('refall', self.userwdgfield.lineEdit_refallu),

                                                       ('valcon', self.userwdgfield.spinBox_valcontcompt),
                                                       ('unicon', self.userwdgfield.comboBox_unicon),
                                                       ('tempcon', self.userwdgfield.spinBox_tempcon),
                                                       ('nomtour', self.userwdgfield.spinBox_nomtour),
                                                       ('valcow', self.userwdgfield.doubleSpinBox_valcow),
                                                       ('valcova', self.userwdgfield.doubleSpinBox_valconva),

                                                       ('p1_v', self.userwdgfield.doubleSpinBox_p1v),
                                                       ('p1_i', self.userwdgfield.doubleSpinBox_p1i),
                                                       ('p1_p', self.userwdgfield.doubleSpinBox_p1p),
                                                       ('p1_pva', self.userwdgfield.doubleSpinBox_p1va),
                                                       ('p1_cos', self.userwdgfield.doubleSpinBox_p1cos),

                                                       ('p2_v', self.userwdgfield.doubleSpinBox_p2v),
                                                       ('p2_i', self.userwdgfield.doubleSpinBox_p2i),
                                                       ('p2_p', self.userwdgfield.doubleSpinBox_p2p),
                                                       ('p2_pva', self.userwdgfield.doubleSpinBox_p2va),
                                                       ('p2_cos', self.userwdgfield.doubleSpinBox_p2cos),

                                                       ('p3_v', self.userwdgfield.doubleSpinBox_p3v),
                                                       ('p3_i', self.userwdgfield.doubleSpinBox_p3i),
                                                       ('p3_p', self.userwdgfield.doubleSpinBox_p3p),
                                                       ('p3_pva', self.userwdgfield.doubleSpinBox_p3va),
                                                       ('p3_cos', self.userwdgfield.doubleSpinBox_p3cos),



                                                       ('multip', self.userwdgfield.comboBox_multip),
                                                       ('sp_type', self.userwdgfield.comboBox_sp_type),
                                                       ('sp_materiau', self.userwdgfield.comboBox_sp_materiau),
                                                       ('sp_forme', self.userwdgfield.comboBox_sp_forme),
                                                       ('sp_couleur', self.userwdgfield.lineEdit_sp_couleur),
                                                       ('sp_diam', self.userwdgfield.doubleSpinBox_sp_diam),
                                                       ('sp_haut', self.userwdgfield.doubleSpinBox_sp_haut),
                                                       ('sp_typmonc', self.userwdgfield.comboBox_sp_typmonc),
                                                       ('sp_depcro', self.userwdgfield.doubleSpinBox_sp_depcro),

                                                       ('sp_boitbran', self.userwdgfield.comboBox_sp_boitbran),
                                                       ('sp_appmat', self.userwdgfield.comboBox_sp_appmat),
                                                       ('sp_typbr', self.userwdgfield.comboBox_sp_typbr),
                                                       ('sp_typprot', self.userwdgfield.comboBox_sp_typprot),
                                                       ('sp_appmat', self.userwdgfield.comboBox_sp_appmat),
                                                       ('sp_calprot', self.userwdgfield.lineEdit_sp_calprot),
                                                       ('sp_barette', self.userwdgfield.comboBox_sp_barette),
                                                       ('sp_preter', self.userwdgfield.comboBox_sp_preter),
                                                       ('sp_terracc', self.userwdgfield.comboBox_sp_terracc),
                                                       ('sp_liaisoneq', self.userwdgfield.comboBox_sp_liaisoneq),
                                                       ('sp_eq', self.userwdgfield.comboBox_sp_eq),






                                                       ('X', self.userwdgfield.doubleSpinBox_X),
                                                       ('dX', self.userwdgfield.doubleSpinBox_dX),
                                                       ('Y', self.userwdgfield.doubleSpinBox_Y),
                                                       ('dY', self.userwdgfield.doubleSpinBox_dY),
                                                       ('Z', self.userwdgfield.doubleSpinBox_Z),
                                                       ('dZ', self.userwdgfield.doubleSpinBox_dZ),

                                                   ])},
                                         'Objet': {'linkfield': 'id_objet',
                                                   'widgets': {
                                                       'commentaire': self.userwdgfield.textBrowser_commentaire}},
                                         'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                               'widgets': {}}}

                self.userwdgfield.toolButton_sp_haut.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_sp_haut))
                self.userwdgfield.toolButton_sp_diam.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_sp_diam))
                self.userwdgfield.toolButton_sp_depcro.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_sp_depcro))

                self.userwdgfield.toolButton_p1v.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p1v))
                self.userwdgfield.toolButton_p1i.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p1i))
                self.userwdgfield.toolButton_p1p.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p1p))
                self.userwdgfield.toolButton_p1va.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p1va))
                self.userwdgfield.toolButton_p1cos.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p1cos))

                self.userwdgfield.toolButton_p2v.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p2v))
                self.userwdgfield.toolButton_p2i.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p2i))
                self.userwdgfield.toolButton_p2p.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p2p))
                self.userwdgfield.toolButton_p2va.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p2va))
                self.userwdgfield.toolButton_p2cos.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p2cos))


                self.userwdgfield.toolButton_p3v.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p3v))
                self.userwdgfield.toolButton_p3i.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p3i))
                self.userwdgfield.toolButton_p3p.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p3p))
                self.userwdgfield.toolButton_p3va.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p3va))
                self.userwdgfield.toolButton_p3cos.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_p3cos))



                self.userwdgfield.comboBox_typenoeud.currentIndexChanged.connect(self.fielduiTypeChanged)
                self.userwdgfield.pushButton_getGPS.clicked.connect(self.getGPSValue)


                # ****************************************************************************************
                # child widgets
                self.dbasechildwdgfield = []

                self.propertieswdgEQUIPEMENT = BaseEclairagePublicEquipementTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

                self.propertieswdgDesordre = BaseEclairagePublicDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil,
                                                                            parentwidget=self)
                self.propertieswdgDesordre.NAME = None
                self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
                self.propertieswdgDesordre.groupBox_elements.setParent(None)
                self.propertieswdgDesordre.userwdgfield.stackedWidget.setParent(None)
                self.propertieswdgDesordre.frame_editing.setParent(None)
                self.userwdgfield.frame_desordre.layout().addWidget(self.propertieswdgDesordre)
                self.dbasechildwdgfield.append(self.propertieswdgDesordre)



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

            #self.dbase.dbasetables['Noeud']['fields']['typeOuvrageAss']['Cst'] = self.initialtypeohassdict








    def fielduiTypeChanged(self, comboindex):
        self.userwdgfield.stackedWidget.setCurrentIndex(comboindex)

        if False:
            if self.userwdgfield.comboBox_typenoeud.currentText() == 'Armoire':
                self.propertieswdgEQUIPEMENT.userwdgfield.comboBox_cat.setCurrentIndex(2)
                self.propertieswdgEQUIPEMENT.userwdgfield.comboBox_cat.setEnabled(False)
            elif self.userwdgfield.comboBox_typenoeud.currentText() == 'Support':
                self.propertieswdgEQUIPEMENT.userwdgfield.comboBox_cat.setCurrentIndex(1)
                self.propertieswdgEQUIPEMENT.userwdgfield.comboBox_cat.setEnabled(True)




        if False:
            #print(self.userwdgfield.comboBox_typeOuvrageAss.currentText())
            currenttext = self.userwdgfield.comboBox_typenoeud.currentText()

            if currenttext in ['Regard','Avaloir', 'Grille','Regard mixte EP EU']:
                self.userwdgfield.stackedWidget.setCurrentIndex(0)
            elif currenttext in ['Branchement']:
                self.userwdgfield.stackedWidget.setCurrentIndex(1)
            elif currenttext in ['Poste de refoulement']:
                self.userwdgfield.stackedWidget.setCurrentIndex(2)
                """
                elif sys.version_info < (3, 0) and currenttext in ['Débourbeur/déshuileur'.decode('utf8')]:
                    self.userwdgfield.stackedWidget.setCurrentIndex(3)
                elif sys.version_info > (3, 0) and currenttext in ['Débourbeur/déshuileur']:
                    self.userwdgfield.stackedWidget.setCurrentIndex(3)
                """
            elif currenttext in ['Débourbeur/déshuileur']:
                self.userwdgfield.stackedWidget.setCurrentIndex(3)
            else:
                self.userwdgfield.stackedWidget.setCurrentIndex(4)


            self.propertieswdgDesordre.propertieswdgOBSERVATION2.updateObservationStackedWidget()





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
                newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
                newgeomwkt = newgeom.asWkt()

            sql = self.dbase.createSetValueSentence(type='INSERT',
                                                    tablename='Desordre',
                                                    listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                  'lid_descriptionsystem', 'geom'],
                                                    listofrawvalues=[lastiddesordre, pkobjet, 'NOD',
                                                                     iddessys, newgeomwkt])
            self.dbase.query(sql)











class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeclairagepublic_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)
