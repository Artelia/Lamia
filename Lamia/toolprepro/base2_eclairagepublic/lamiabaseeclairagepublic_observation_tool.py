# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_observation_tool import BaseObservationTool
#from ..base.lamiabase_photo_tool import BasePhotoTool
from .lamiabaseeclairagepublic_photo_tool import BaseEclairagePublicPhotoTool as BasePhotoTool
from .lamiabaseeclairagepublic_croquis_tool import BaseCroquisTool
import os
import datetime


class BaseEclairagePublicObservationTool(BaseObservationTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseEclairagePublicObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.dbase.variante in [None, 'Lamia']:
            if self.userwdgfield is None:
                # ****************************************************************************************
                # userui
                self.userwdgfield = UserUI()
                if False:
                    self.linkuserwdgfield = {'Observation': {'linkfield': 'id_observation',
                                                             'widgets': {
                                                                 'datetimeobservation': self.userwdgfield.dateTimeEdit,
                                                                 'nombre': self.userwdgfield.spinBox_nombre,
                                                                 'longueurdes': self.userwdgfield.doubleSpinBox_longueur,
                                                                 'gravite': self.userwdgfield.comboBox_urgence,

                                                                 'oh_etatgeneral': self.userwdgfield.comboBox_etatgen,
                                                                 'oh_etatgeneralcom': self.userwdgfield.textBrowser_etatgencom,

                                                                 'oh_etatvantellerie': self.userwdgfield.comboBox_etatvantellerie,
                                                                 'oh_etatvantelleriecom': self.userwdgfield.textBrowser_vanteleriecom,
                                                                 'oh_etatgeniecivil': [self.userwdgfield.comboBox_etatGC,
                                                                                       self.userwdgfield.comboBox_etatGC_2],
                                                                 'oh_etatgeniecivilcom': [
                                                                     self.userwdgfield.textBrowser_etatGC,
                                                                     self.userwdgfield.textBrowser_etatGC_2],
                                                                 'oh_testmanoeuvre': self.userwdgfield.comboBox_manoeuvre,
                                                                 'oh_testmanoeuvrecom': self.userwdgfield.textBrowser_manoeuvre,
                                                                 'oh_etancheite': self.userwdgfield.checkBox_etancheite,
                                                                 'oh_etancheitecom': self.userwdgfield.textBrowser__etancheite,
                                                                 'oh_ecoulement': [self.userwdgfield.comboBox_envas,
                                                                                   self.userwdgfield.comboBox_envas2],
                                                                 'oh_ecoulementcom': [
                                                                     self.userwdgfield.textBrowser_envascom,
                                                                     self.userwdgfield.textBrowser_envascom2],

                                                                 'evolution': self.userwdgfield.textEdit_evolution,
                                                                 'typesuite': self.userwdgfield.comboBox_typesuite,
                                                                 'commentairesuite': self.userwdgfield.textEdit_suite}},
                                             'Objet': {'linkfield': 'id_objet',
                                                       'widgets': {'commentaire': self.userwdgfield.textEdit_comm}}}





                    self.userwdgfield.toolButton_calc_nb.clicked.connect(
                        lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nombre))
                    self.userwdgfield.toolButton_longueur.clicked.connect(
                        lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_longueur))

                self.linkuserwdgfield = {'Observation': {'linkfield': 'id_observation',
                                                         'widgets': {
                                                             'datetimeobservation': self.userwdgfield.dateTimeEdit,
                                                             'nombre': self.userwdgfield.spinBox_nombre,
                                                             #'longueurdes': self.userwdgfield.doubleSpinBox_longueur,
                                                             'gravite': self.userwdgfield.comboBox_urgence,

                                                              #infralin
                                                             'etatgeneral': [self.userwdgfield.comboBox_etatgen,
                                                                             self.userwdgfield.comboBox_etatgen2],

                                                             #node
                                                             'etatsupport': self.userwdgfield.comboBox_etatsupport,
                                                             'etatraccordement': self.userwdgfield.comboBox_etatraccordement,
                                                             'etatcrosse': self.userwdgfield.comboBox_etatcrosse,

                                                             #eqp
                                                             #'etatgeneral': self.userwdgfield.comboBox_etatgen2,




                                                             'evolution': self.userwdgfield.textEdit_evolution,
                                                             'typesuite': self.userwdgfield.comboBox_typesuite,
                                                             'commentairesuite': self.userwdgfield.textEdit_suite}},
                                         'Objet': {'linkfield': 'id_objet',
                                                   'widgets': {'commentaire': self.userwdgfield.textEdit_comm}}}


                # ****************************************************************************************
                # child widgets
                self.dbasechildwdgfield=[]
                # if self.parentWidget is not None:
                if self.parentWidget is None or self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase,gpsutil=self.gpsutil, parentwidget=self)
                    self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def postInitFeatureProperties(self, feat):
        super(BaseEclairagePublicObservationTool, self).postInitFeatureProperties(feat)
        self.updateObservationStackedWidget()

    def updateObservationStackedWidget(self):

        if ('groupedesordre' in self.dbase.dbasetables['Desordre']['fields'].keys()  ):
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
                grpdes = self.parentWidget.currentFeature['groupedesordre']
                grpdescst = [elem[1] for elem in self.dbase.dbasetables['Desordre']['fields']['groupedesordre']['Cst']]
                indexgrp = grpdescst.index(grpdes)
                try:
                    self.userwdgfield.stackedWidget.setCurrentIndex(indexgrp)
                except:
                    pass
                if grpdes == 'EQP' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeature is not None:
                    if self.parentWidget.parentWidget.dbasetablename == 'Equipement':
                        #typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        currenttext = self.parentWidget.parentWidget.userwdgfield.comboBox_cat.currentText()
                        # typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        typeeqp = self.dbase.getConstraintRawValueFromText('Equipement', 'categorie', currenttext)

                        if typeeqp in ['FOY']:
                            self.userwdgfield.stackedWidget_2.setCurrentIndex(0)
                        else:
                            self.userwdgfield.stackedWidget_2.setCurrentIndex(1)








                if grpdes == 'NOD' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeature is not None:
                    if self.parentWidget.parentWidget.dbasetablename == 'Noeud':
                        #typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        currenttext = self.parentWidget.parentWidget.userwdgfield.comboBox_typenoeud.currentText()
                        # typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        typenoeud = self.dbase.getConstraintRawValueFromText('Noeud', 'typenoeud', currenttext)

                        if typenoeud in ['LOC']:
                            self.userwdgfield.stackedWidget_3.setCurrentIndex(0)
                        else:
                            self.userwdgfield.stackedWidget_3.setCurrentIndex(1)







class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeclairagepublic_observation_tool_ui.ui')
        uic.loadUi(uipath, self)


