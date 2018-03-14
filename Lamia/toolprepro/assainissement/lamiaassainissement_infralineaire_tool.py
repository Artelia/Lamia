# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_infralineaire_tool import AbstractInfraLineaireTool
from .lamiaassainissement_photos_tool import PhotosTool

from .lamiaassainissement_croquis_tool import CroquisTool

# from ..InspectionDigue_graphique_tool import GraphiqueTool
# from .InspectionDigue_profiltravers_tool  import ProfilTraversTool
from ...toolpostpro.InspectionDigue_path_tool import PathTool

from ..abstract.lamia_photoviewer import PhotoViewer
import os
import datetime
import logging
import time
debugtime = False



class InfraLineaireTool(AbstractInfraLineaireTool):

    LOADFIRST = True
    dbasetablename = 'Infralineaire'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(InfraLineaireTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        timestart = time.clock()
        if debugtime: logging.getLogger('Lamia').debug('Start init %s',str(round(time.clock() - timestart, 3)))

        self.CAT = 'Description'
        self.NAME = 'Troncon'
        self.dbasetablename = 'Infralineaire'
        # self.visualmode = [0, 1, 2]
        # self.PointEnabled = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_objet',
                                            'idtcsource' : 'id_tcobjet',
                                           'iddest' : 'id_intervenant',
                                           'idtcdest' : 'id_tcintervenant',
                                           'desttable' : ['Intervenant']}
                                            }
        self.pickTable = {'LkZoneGeo': {'ZONEGEO': 'ID'}}
        self.debug = False


        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            self.userwdgfield = UserUIField()

            self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                       'widgets': {'materiau': self.userwdgfield.comboBox_materiau,
                                                                   'diametreNominal': self.userwdgfield.spinBox_diametreNominal,
                                                                   'enService': self.userwdgfield.comboBox_enService,
                                                                   'typeReseau': self.userwdgfield.comboBox_typeReseau,
                                                                   'altAmont': self.userwdgfield.doubleSpinBox_altAmont,
                                                                   'altAmont': self.userwdgfield.doubleSpinBox_altAval,
                                                                   'profamont': self.userwdgfield.doubleSpinBox_profamont,
                                                                   'profaval': self.userwdgfield.doubleSpinBox_profaval,
                                                                   'lk_noeud1': self.userwdgfield.spinBox_lk_noeud1,
                                                                   'lk_noeud2': self.userwdgfield.spinBox_lk_noeud2,



                                                                   }},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {}},
                                     'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                           'widgets': {}}}

            self.dbasechildwdgfield = []

            self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')

        if self.currentFeature is None:
            pass
        else:
            pass



class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiaassainissement_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)
