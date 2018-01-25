# -*- coding: utf-8 -*-

from ..toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool





class TronconEmpriseTool(AbstractInspectionDigueTool):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(TronconEmpriseTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Description'
        self.NAME = 'Emprise troncon'
        self.dbasetablename = 'Infralinemprise'
        self.visualmode = [1, 2]
        # self.PointEnabled = True
        # self.LineENABLED = True
        self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'InfralinEmpriseInfralin' : {'tabletc' : None,
                                           'idsource' : 'lk_infralineaire',
                                       'idtcsource' : None,
                                           'iddest' : 'id_infralineaire',
                                       'idtcdest' : None,
                                           'desttable' : ['Infralineaire']}}
        # self.pickTable = None

        # ****************************************************************************************
        #properties ui
        self.comboBox_featurelist.setEnabled(False)
        self.pushButton_addFeature.setEnabled(False)
        self.pushButton_delFeature.setEnabled(False)

        # ****************************************************************************************
        # userui

        # ****************************************************************************************
        # child widgets



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postInitFeatureProperties(self, feat):
        pass

    def postSaveFeature(self, boolnewfeature):
        pass

