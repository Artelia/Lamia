# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ..base2.lamiabase_desordre_tool import BaseDesordreTool
from .lamiabaseeclairagepublic_observation_tool import BaseEclairagePublicObservationTool as BaseObservationTool
import os


class BaseEclairagePublicDesordreTool(BaseDesordreTool):

    def __init__(self, **kwargs):
        super(BaseEclairagePublicDesordreTool, self).__init__(**kwargs)

    def initMainToolWidget(self):


        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {'Desordre': {'linkfield': 'id_desordre',
                                                        'widgets': {'groupedesordre': self.toolwidgetmain.comboBox_groupedes
                                                                    }},
                                            'Objet': {'linkfield': 'id_objet',
                                                    'widgets': {}}}
        #self.groupBox_attributes.setParent(None)
        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        #if self.parentWidget is None:
        self.propertieswdgOBSERVATION = BaseObservationTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)

        #self.propertieswdgOBSERVATION2 = BaseObservationTool(dbase=self.dbase, parentwidget=self)
        #self.propertieswdgOBSERVATION2.NAME = None
        #self.toolwidgetmain.tabWidget.widget(0).layout().addWidget(self.propertieswdgOBSERVATION2)
        #self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION2)

        #self.toolwidgetmain.tabWidget.widget(1).layout().addWidget(
        #    self.propertieswdgOBSERVATION2.propertieswdgPHOTOGRAPHIE)
        #self.toolwidgetmain.tabWidget.widget(2).layout().addWidget(
        #    self.propertieswdgOBSERVATION2.propertieswdgCROQUIS)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeclairagepublic_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)
