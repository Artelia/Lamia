import os
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import (QWidget)

class CostTool(AbstractLamiaTool):
    TOOLNAME = 'test_module'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(CostTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Synthese'
        self.NAME = 'Couts'
        self.visualmode = [4]

        self.groupBox_elements.setParent(None)
        self.frame_editing.setParent(None)

    def initFieldUI(self):
        if self.userwdgfield is None:
            self.userwdgfield = UserUI()

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'test_module.ui')
        uic.loadUi(uipath, self)