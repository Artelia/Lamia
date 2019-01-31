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
#from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
#from .lamiabaseassainissement_croquis_tool import BaseAssainissementCroquisTool as BaseCroquisTool

from .lamiabaseparking_photo_tool import BaseParkingPhotoTool as BasePhotoTool
from .lamiabaseparking_croquis_tool import BaseParkingCroquisTool as BaseCroquisTool

import os
import datetime


class BaseParkingObservationTool(BaseObservationTool):

    dbasetablename = 'Observation'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseParkingObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initTool(self):
        super(BaseParkingObservationTool, self).initTool()
        #self.NAME = 'Campagne de reconnaissance'
        #self.qtreewidgetfields = ['libelle']
        #self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
        self.NAME = 'Observation immat'
        self.visualmode = [0,1]

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
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Observation' : {'linkfield' : 'id_observation',
                                             'widgets' : {'immatriculation' : self.userwdgfield.spinBox_immat,
                                                          'illicite' : self.userwdgfield.checkBox_illicite,
                                                         'datetimeobservation' : self.userwdgfield.dateTimeEdit,
                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}

            self.userwdgfield.toolButton_immat.clicked.connect(
                lambda: self.showNumPad(self.userwdgfield.spinBox_immat))


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield=[]
            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)



    def postInitFeatureProperties(self, feat):

        if self.currentFeature is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, self.dbasetablename, 'datetimeobservation', datecreation)






    def postSaveFeature(self, boolnewfeature):
        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Desordre':
                self.parentWidget.updateDateCampagne()

    def showNumPad(self, finalwdg):
        # print('ok', finalwdg)

        self.windowdialog.numpaddialog.exec_()
        number = self.windowdialog.numpaddialog.dialogIsFinished()
        # print(number)
        if number:
            finalwdg.setValue(number)
            self.saveFeature()






class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseparking_observation_tool_ui.ui')
        uic.loadUi(uipath, self)
