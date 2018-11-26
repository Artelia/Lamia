# -*- coding: utf-8 -*-
"""


import datetime
import logging
import time
debugtime = False
"""

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
import os
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_infralineaire_tool import BaseInfraLineaireTool
import logging
# from ..base.lamiabase_photo_tool import BasePhotoTool
from .lamiabaseparking_photo_tool import BaseParkingPhotoTool as BasePhotoTool
from .lamiabaseparking_croquis_tool import BaseParkingCroquisTool as BaseCroquisTool
from .lamiabaseparking_desordre_tool import BaseParkingDesordreTool
from collections import OrderedDict




class BaseParkingInfraLineaireTool(BaseInfraLineaireTool):


    LOADFIRST = True
    dbasetablename = 'Infralineaire'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseParkingInfraLineaireTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    """
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
        self.qtreewidgetfields = ['revisionbegin']

        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_infralineaire_tool_icon.svg')


        # ****************************************************************************************
        #properties ui
        pass


    
    """

    def initTool(self):
        super(BaseParkingInfraLineaireTool, self).initTool()
        self.NAME = 'Zone de stationnement'
        self.qtreewidgetfields = ['libelle']
        self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]



    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            self.userwdgfield = UserUIField()

            self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                       'widgets': OrderedDict([('situation', self.userwdgfield.textBrowser_commentaire),
                                                                               ('typestationnement', self.userwdgfield.comboBox_typestationnement),
                                                                               ('zonage', self.userwdgfield.comboBox_zonage),
                                                                               ('zonageautre', self.userwdgfield.lineEdit_zonage),
                                                                               ('nbredeplaces', self.userwdgfield.spinBox_nbreplace)])},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {'libelle': self.userwdgfield.lineEdit_nom,
                                                           #'commentaire':self.userwdgfield.textBrowser_commentaire
                                                           }},
                                     'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                           'widgets': {}}}

            self.dbasechildwdgfield = []

            self.userwdgfield.toolButton_nbreplace.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nbreplace))

            if self.parentWidget is None:

                self.desordreswidget =BaseParkingDesordreTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.desordreswidget)

                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def postSaveFeature(self, boolnewfeature):

        # save a disorder on first creation
        if False:
            if self.savingnewfeature and self.savingnewfeatureVersion == False:
                # categorie
                pkobjet = self.dbase.createNewObjet()
                lastiddesordre = self.dbase.getLastId('Desordre') + 1
                geomtext, iddessys = self.dbase.getValuesFromPk('Infralineaire_qgis',
                                                                ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                                self.currentFeaturePK)
                sql = self.dbase.createSetValueSentence(type='INSERT',
                                                        tablename='Desordre',
                                                        listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                      'lid_descriptionsystem', 'geom'],
                                                        listofrawvalues=[lastiddesordre, pkobjet, 'INF', iddessys,
                                                                         geomtext])
                self.dbase.query(sql)





class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseparking_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)

