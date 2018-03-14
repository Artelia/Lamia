# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QPushButton)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_noeud_tool import AbstractNoeudTool

import os
import datetime




class NoeudTool(AbstractNoeudTool):

    LOADFIRST = True
    dbasetablename = 'Noeud'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(NoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Noeud' : {'linkfield' : 'id_noeud',
                                             'widgets' : {'altradierouvrage': self.userwdgfield.doubleSpinBox_altradierouvrage,
                                                          'alttamponouvrage': self.userwdgfield.doubleSpinBox_alttamponouvrage,
                                                          'profradierouvrage': self.userwdgfield.doubleSpinBox_profradierouvrage,
                                                          'proftamponouvrage': self.userwdgfield.doubleSpinBox_proftamponouvrage,
                                                          'typeReseau': self.userwdgfield.comboBox_typeReseau,
                                                          'typeOuvrageAss': self.userwdgfield.comboBox_typeOuvrageAss,

                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}



            # ****************************************************************************************
            # child widgets

    pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiaassainissement_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)
