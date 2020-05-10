# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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

from .lamiabaseeclairagepublic_photo_tool import BaseEclairagePublicPhotoTool as BasePhotoTool
from .lamiabaseeclairagepublic_croquis_tool import BaseEclairagePublicCroquisTool as BaseCroquisTool
from .lamiabaseeclairagepublic_desordre_tool import BaseEclairagePublicDesordreTool

import os
import datetime
from collections import OrderedDict



class BaseEclairagePublicEquipementTool(BaseEquipementTool):

    LOADFIRST = True
    dbasetablename = 'Equipement'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseEclairagePublicEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)


    def initTool(self):
        super(BaseEclairagePublicEquipementTool, self).initTool()
        self.visualmode = [1, 2]


    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Equipement' : {'linkfield' : 'id_equipement',
                                             'widgets' : {
                                                            'categorie': self.userwdgfield.comboBox_cat,

                                                                # depart
                                                             'dep_nom': self.userwdgfield.comboBox_dep_nom,
                                                             'dep_foncall': self.userwdgfield.comboBox_dep_foncall,
                                                              'dep_typprot': self.userwdgfield.comboBox_dep_typprot,
                                                             'dep_calprot': self.userwdgfield.lineEdit_dep_calprot,
                                                             'dep_diffdj': self.userwdgfield.lineEdit_dep_diffdj,
                                                             'dep_neutsec': self.userwdgfield.comboBox_dep_neutsec,

                                                             # foyer
                                                             'fo_codlant': self.userwdgfield.lineEdit_fo_codlant,
                                                             'fo_typelum': self.userwdgfield.comboBox_fo_typelum,
                                                             'fo_marque': self.userwdgfield.lineEdit_fo_marque,
                                                             'fo_ref': self.userwdgfield.lineEdit_fo_ref,
                                                             'fo_classe': self.userwdgfield.comboBox_fo_classe,
                                                             'fo_couleur': self.userwdgfield.lineEdit_fo_couleur,
                                                             'fo_hautfeu': self.userwdgfield.doubleSpinBox_fo_hautfeu,
                                                             'fo_typevas': self.userwdgfield.comboBox_fo_typevas,
                                                             'fo_typapp': self.userwdgfield.comboBox_fo_typapp,
                                                             'fo_famlamp': self.userwdgfield.comboBox_fo_famlamp,
                                                             'fo_puilamp': self.userwdgfield.doubleSpinBox_fo_puilamp,


                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire': self.userwdgfield.textBrowser_comm}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                      'widgets' : {  }}}


            self.userwdgfield.toolButton_fo_hautfeu.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_fo_hautfeu))
            self.userwdgfield.toolButton_fo_puilamp.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_fo_puilamp))



            self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)

            #self.userwdgfield.pushButton_getGPS.clicked.connect(self.getGPSValue)

            #self.allaccessfields = OrderedDict(self.dbasetable['fields']['acces'])


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            if False:
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

            self.propertieswdgDesordre = BaseEclairagePublicDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil,
                                                                        parentwidget=self)
            self.propertieswdgDesordre.NAME = None
            self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            self.propertieswdgDesordre.groupBox_elements.setParent(None)
            self.propertieswdgDesordre.userwdgfield.stackedWidget.setParent(None)
            self.propertieswdgDesordre.frame_editing.setParent(None)
            self.userwdgfield.frame_desordre.layout().addWidget(self.propertieswdgDesordre)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)


    def postInitFeatureProperties(self, feat):

        if (self.parentWidget is not None and self.parentWidget.currentFeature is not None
                and self.parentWidget.dbasetablename == 'Noeud'):
            self.userwdgfield.comboBox_cat.setEnabled(False)

            typeparent = self.parentWidget.userwdgfield.comboBox_typenoeud.currentText()
            if typeparent == 'Armoire':
                self.userwdgfield.comboBox_cat.setCurrentIndex(2)
                # get geom
                noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeaturePK)
                neudfetgeom = noeudfet.geometry().asPoint()
                self.createorresetRubberband(1)
                self.setTempGeometry([neudfetgeom,neudfetgeom], False, False)

            elif typeparent == 'Support':
                self.userwdgfield.comboBox_cat.setCurrentIndex(1)
                # get geom
                noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeaturePK)
                neudfetgeom = noeudfet.geometry().asPoint()
                self.createorresetRubberband(1)
                self.setTempGeometry([neudfetgeom,neudfetgeom], False, False)

        else:
            self.userwdgfield.comboBox_cat.setEnabled(True)











        if False:
            if self.currentFeaturePK is not None:
                lid_dessys = self.dbase.getValuesFromPk('Equipement_qgis',['lid_descriptionsystem_1'],self.currentFeaturePK)
                if lid_dessys is not None:
                    self.userwdgfield.comboBox_acces.setEnabled(False)
                else:
                    self.userwdgfield.comboBox_acces.setEnabled(True)
            else:
                self.userwdgfield.comboBox_acces.setEnabled(True)


            if (self.parentWidget is not None and self.parentWidget.currentFeature is not None
                    and self.parentWidget.dbasetablename == 'Noeud'):
                type_ouvrage = self.dbase.getValuesFromPk('Noeud_qgis',
                                                            ['type_ouvrage'],
                                                            self.parentWidget.currentFeaturePK)
                if type_ouvrage == 'CHE':

                    self.dbase.dbasetables['Equipement']['fields']['acces'] = OrderedDict([('PGtype', 'VARCHAR(255'),('ParFldCst','categorie'),('Cst',[[u'Chambre enterrée/regard', 'CHE',['','VEN','VAN','VID','REG','HYD','COM','CHL','RPC','SPE']]])])

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
        if True:
            # save a disorder on first creation
            if self.savingnewfeature and not self.savingnewfeatureVersion:
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
                                                        listofrawvalues=[lastiddesordre, pkobjet, 'EQP',
                                                                         iddessys, newgeomwkt])
                self.dbase.query(sql)





    def changeCategorie(self, intcat):
        if self.dbase.variante in [None, 'Lamia']:
            pagecount = self.userwdg.stackedWidget.count()
            if intcat >= pagecount -1 :
                self.userwdg.stackedWidget.setCurrentIndex(pagecount -1)
            else:
                self.userwdg.stackedWidget.setCurrentIndex(intcat)






class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeclairagepublic_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)