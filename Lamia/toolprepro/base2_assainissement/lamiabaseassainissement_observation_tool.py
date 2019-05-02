# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_observation_tool import BaseObservationTool
#from ..base.lamiabase_photo_tool import BasePhotoTool
# from ..base.lamiabase_croquis_tool import BaseCroquisTool
# from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
from .lamiabaseassainissement_croquis_tool import BaseAssainissementCroquisTool as BaseCroquisTool
import os
import datetime


class BaseAssainissementObservationTool(BaseObservationTool):
    
    #specialfieldui = ['2']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseAssainissementObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Observation'
        self.dbasetablename = 'Observation'
        #self.visualmode = [1, 2]
        self.visualmode = []
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Desordre' : {'tabletc' : None,
                                           'idsource' : 'lk_desordre',
                                       'idtcsource' : None,
                                           'iddest' : 'id_desordre',
                                       'idtcdest' : None,
                                           'desttable' : ['Desordre']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lk_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_observation_tool_icon.png')

        # ****************************************************************************************
        #properties ui
        pass
    
    """
    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop


        if self.dbase.variante in [None, 'Lamia']:
            if self.userwdgfield is None:
                # ****************************************************************************************
                # userui
                self.userwdgfield = UserUI()
                self.linkuserwdgfield = {'Observation' : {'linkfield' : 'id_observation',
                                                 'widgets' : {'datetimeobservation' : self.userwdgfield.dateTimeEdit,
                                                              #'nombre' : self.userwdgfield.spinBox_nombre,
                                                            'gravite': self.userwdgfield.comboBox_urgence,
    
                                                              # regard
                                                              'etattampon': [self.userwdgfield.comboBox_etattampon,
                                                                             self.userwdgfield.comboBox_PRetattampon],
                                                              'etatechelon': self.userwdgfield.comboBox_etatechelon,
                                                              'etatregard': self.userwdgfield.comboBox_etatregard,
                                                              'etatcunette': self.userwdgfield.comboBox_etatcunette,
                                                              'ECPPdepuisbranchement': self.userwdgfield.comboBox_ecpp,
                                                              'infiltration': self.userwdgfield.comboBox_infiltration,
                                                              'intrusionracine': self.userwdgfield.comboBox_racines,
    
                                                              'hdeuxs': self.userwdgfield.comboBox_h2s,
                                                              'depots': [self.userwdgfield.comboBox_depot,
                                                                         self.userwdgfield.comboBox_DSHencombrement],
                                                              'miseencharge': self.userwdgfield.comboBox_miseencharge,
                                                              'jugemententretien': self.userwdgfield.comboBox_entretiengeneral,
    
                                                              # DIV
                                                              'etatgeneral': self.userwdgfield.comboBox_DIVetatgeneral,
    
                                                              #'evolution': self.userwdgfield.textEdit_evolution,
                                                              #'commentaires': self.userwdgfield.textEdit_comm,
                                                              #'suite': self.userwdgfield.textEdit_suite,
                                                              'typesuite': self.userwdgfield.comboBox_typesuite,
                                                              'precisionsuite': self.userwdgfield.comboBox_precisionsuite
    
    
                                                              }},
                                    'Objet' : {'linkfield' : 'id_objet',
                                              'widgets' : {'commentaire': self.userwdgfield.textEdit_comm}}}
    
                self.userwdgfield.toolButton_calc_nb.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nombre))
    
                # ****************************************************************************************
                # child widgets
                self.dbasechildwdgfield=[]
                if self.parentWidget is not None:
                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
                    
        elif self.dbase.variante in ['2018_SNCF']:
            if self.userwdgfield is None:
                # ****************************************************************************************
                # userui
                self.userwdgfield = UserUI_2()
                self.linkuserwdgfield = {'Observation': {'linkfield': 'id_observation',
                                                           'widgets': {
                                                               'datetimeobservation': self.userwdgfield.dateTimeEdit,
                                                               # 'nombre' : self.userwdgfield.spinBox_nombre,
                                                               'gravite': self.userwdgfield.comboBox_urgence,

                                                               # regard
                                                               'etattampon': [self.userwdgfield.comboBox_etattampon,
                                                                              self.userwdgfield.comboBox_PRetattampon],
                                                               'etatechelon': self.userwdgfield.comboBox_etatechelon,
                                                               'etatregard': self.userwdgfield.comboBox_etatregard,
                                                               'etatcunette': self.userwdgfield.comboBox_etatcunette,
                                                               'hdeuxs': self.userwdgfield.comboBox_h2s,
                                                               'depots': [self.userwdgfield.comboBox_depot,
                                                                          self.userwdgfield.comboBox_DSHencombrement],
                                                               'miseencharge': self.userwdgfield.comboBox_miseencharge,
                                                               'jugemententretien': self.userwdgfield.comboBox_entretiengeneral,

                                                               # PR
                                                               # 'etattampon': self.userwdgfield.comboBox_PRetattampon,
                                                               'etatgeneral': [self.userwdgfield.comboBox_etatbache,
                                                                               self.userwdgfield.comboBox_DSHetageneral,
                                                                               self.userwdgfield.comboBox_DIVetatgeneral],
                                                               'etatasservissement': self.userwdgfield.comboBox_etatasservissement,

                                                               # DSH
                                                               # 'etatgeneral': self.userwdgfield.comboBox_DSHetageneral,
                                                               # 'ensablement': self.userwdgfield.comboBox_DSHencombrement,

                                                               # DIC
                                                               # 'etatgeneral': self.userwdgfield.comboBox_DIVetatgeneral,

                                                               }},
                                           'Objet': {'linkfield': 'id_objet',
                                                     'widgets': {'commentaire': self.userwdgfield.textEdit_comm}}}

                self.userwdgfield.toolButton_calc_nb.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nombre))

                self.dbasechildwdgfield = []
                if self.parentWidget is not None:
                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)


        elif self.dbase.variante in ['CD41']:
            if self.userwdgfield is None:
                # ****************************************************************************************
                # userui
                self.userwdgfield = UserUI_3()
                self.linkuserwdgfield = {'Observation': {'linkfield': 'id_observation',
                                                           'widgets': {
                                                               'datetimeobservation': self.userwdgfield.dateTimeEdit,
                                                               # 'nombre' : self.userwdgfield.spinBox_nombre,
                                                               'gravite': self.userwdgfield.comboBox_urgence,
                                                               'etatgeneral': self.userwdgfield.comboBox_etatgeneral,


                                                               # regard
                                                               'etattampon': self.userwdgfield.comboBox_etattampon,
                                                               'etatechelon': self.userwdgfield.comboBox_etatechelon,
                                                               'etatregard': self.userwdgfield.comboBox_etatregard,
                                                               'etatcunette': self.userwdgfield.comboBox_etatcunette,
                                                               'hdeuxs': self.userwdgfield.comboBox_h2s,
                                                               'depots': self.userwdgfield.comboBox_depot,
                                                               'miseencharge': self.userwdgfield.comboBox_miseencharge,
                                                               'jugemententretien': self.userwdgfield.comboBox_entretiengeneral,



                                                               }},
                                           'Objet': {'linkfield': 'id_objet',
                                                     'widgets': {'commentaire': self.userwdgfield.textEdit_comm}}}

                self.userwdgfield.toolButton_calc_nb.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nombre))

                self.dbasechildwdgfield = []
                if self.parentWidget is not None:
                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    """
    
    def postOnActivation(self):
            pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
            sqlin += " ORDER BY dateobservation DESC"
        return sqlin

        
    """

    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, self.dbasetablename, 'datetimeobservation', datecreation)

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

                #if self.userwdg == self.userwdgfield:
                if self.dbase.variante in [None, 'Lamia']:
                    if grpdes == 'NOD' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeature is not None:
                        if self.parentWidget.parentWidget.dbasetablename == 'Noeud':
                            #typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                            currenttext = self.parentWidget.parentWidget.userwdgfield.comboBox_typeOuvrageAss.currentText()
                            # typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                            typenoeud = self.dbase.getConstraintRawValueFromText('Noeud', 'typeOuvrageAss', currenttext)

                            if typenoeud in ['60','70', '71']:
                                self.userwdgfield.stackedWidget_2.setCurrentIndex(0)
                            elif typenoeud == '10':
                                self.userwdgfield.stackedWidget_2.setCurrentIndex(1)
                            else:
                                self.userwdgfield.stackedWidget_2.setCurrentIndex(3)

                #elif hasattr(self, 'userwdgfield_2') and self.userwdg == self.userwdgfield_2 :
                elif self.dbase.variante in ['2018_SNCF']:
                    if grpdes == 'NOD' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeature is not None:
                        if self.parentWidget.parentWidget.dbasetablename == 'Noeud':
                            currenttext = self.parentWidget.parentWidget.userwdgfield.comboBox_typeOuvrageAss.currentText()
                            # typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                            typenoeud = self.dbase.getConstraintRawValueFromText('Noeud', 'typeOuvrageAss', currenttext)
                            if typenoeud in ['60','70', '71']:
                                self.userwdgfield.stackedWidget_2.setCurrentIndex(0)
                            elif typenoeud == '10':
                                self.userwdgfield.stackedWidget_2.setCurrentIndex(1)
                            elif typenoeud == '21':
                                self.userwdgfield.stackedWidget_2.setCurrentIndex(2)
                            else:
                                self.userwdgfield.stackedWidget_2.setCurrentIndex(3)
                elif self.dbase.variante in ['CD41']:
                    if grpdes == 'NOD' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeature is not None:
                        if self.parentWidget.parentWidget.dbasetablename == 'Noeud':
                            currenttext = self.parentWidget.parentWidget.userwdgfield.comboBox_typeOuvrageAss.currentText()
                            # typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                            typenoeud = self.dbase.getConstraintRawValueFromText('Noeud', 'typeOuvrageAss', currenttext)
                            if typenoeud in ['60']:
                                self.userwdgfield.stackedWidget_2.setCurrentIndex(0)
                            else:
                                self.userwdgfield.stackedWidget_2.setCurrentIndex(1)





    """

    def createParentFeature(self):

        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idobjet = self.dbase.getLastRowId('Objet')

        pkobservation = self.currentFeature.id()
        lastidobservation = self.dbase.getLastId('Observation') + 1

        sql = "UPDATE Observation SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_observation = " + str(lastidobservation) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_observation = " + str(pkobservation) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Desordre':
                currentparentlinkfield = self.parentWidget.currentFeature['id_desordre']
                sql = "UPDATE Observation SET lk_desordre = " + str(currentparentlinkfield) + " WHERE pk_observation = " + str(pkobservation) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):
        pass



    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']

        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True

    """

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_observation_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUI_2(QWidget):
    def __init__(self, parent=None):
        super(UserUI_2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_observation_tool_ui_2018SNCF.ui')
        uic.loadUi(uipath, self)

class UserUI_3(QWidget):
    def __init__(self, parent=None):
        super(UserUI_3, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_observation_tool_ui_CD41.ui')
        uic.loadUi(uipath, self)