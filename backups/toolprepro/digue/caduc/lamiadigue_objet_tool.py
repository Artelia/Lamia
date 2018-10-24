# -*- coding: utf-8 -*-


import os

from qgis.PyQt import uic

from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '..', '..','dialog', 'InspectionDigue_propertieswidget.ui'))


class objetTool(AbstractInspectionDigueTool, FORM_CLASS):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None,parentwidget=None, parent=None):
        super(objetTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Description'
        self.NAME = 'Objet'
        self.dbasetablename = 'OBJET'
        self.visualmode = [1, 2]

    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postInitFeatureProperties(self, feat):
        pass

    def postSaveFeature(self, boolnewfeature):
        pass
