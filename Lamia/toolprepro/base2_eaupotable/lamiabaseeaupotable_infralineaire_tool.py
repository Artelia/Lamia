"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """


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
from .lamiabaseeaupotable_photo_tool import BaseEaupotablePhotoTool as BasePhotoTool
from .lamiabaseeaupotable_croquis_tool import BaseEaupotableCroquisTool as BaseCroquisTool
from ..base2.lamiabase_photoviewer import PhotoViewer
if False:
    from .lamiabasedigue_graphique_tool import BaseGraphiqueTool as GraphiqueTool
    from .lamiabasedigue_profil_tool import BaseDigueProfilTool as ProfilTool
from collections import OrderedDict



class BaseEaupotableInfraLineaireTool(BaseInfraLineaireTool):


    LOADFIRST = True
    dbasetablename = 'Infralineaire'
    # specialfieldui=['2']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseEaupotableInfraLineaireTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

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






    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.dbase.variante in [None, 'Lamia']:
            if self.userwdgfield is None:
                self.userwdgfield = UserUIField()

                self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                           'widgets': OrderedDict([('type_eau', self.userwdgfield.comboBox_typeeau),
                                                                                   ('branchement', self.userwdgfield.comboBox_branchement),
                                                                                   ('domaine', self.userwdgfield.comboBox_domaine),

                                                                                   ('diametre_ext', self.userwdgfield.doubleSpinBox_diametre),
                                                                                   ('profondeur_generatrice', self.userwdgfield.doubleSpinBox_gene),
                                                                                   ('materiau', self.userwdgfield.comboBox_materiau),
                                                                                   ('joint', self.userwdgfield.comboBox_joint),

                                                                                   ('protection_catodique',self.userwdgfield.comboBox_protectioncatho),
                                                                                   ('mode_circulation', self.userwdgfield.comboBox_modecircu),
                                                                                   ('fonction_cana',self.userwdgfield.comboBox_fonctioncan)
                                                                                   ])},
                                         'Objet': {'linkfield': 'id_objet',
                                                   'widgets': {
                                                               'commentaire':self.userwdgfield.textBrowser_commentaire}},
                                         'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                               'widgets': {}}}

                self.userwdgfield.toolButton_diametre.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_diametre))
                self.userwdgfield.toolButton_gene.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_gene))


                self.dbasechildwdgfield = []

                if self.parentWidget is None:
                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        elif self.dbase.variante in ['Reseau_chaleur']:
            if self.userwdgfield is None:
                self.userwdgfield = UserUIField2()

                self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                           'widgets': OrderedDict(
                                                               [('type_eau', self.userwdgfield.comboBox_typeeau),
                                                                ('branchement', self.userwdgfield.comboBox_branchement),
                                                                ('domaine', self.userwdgfield.comboBox_domaine),

                                                                ('diametre_ext',self.userwdgfield.doubleSpinBox_diametre),
                                                                ('diametre_int',self.userwdgfield.doubleSpinBox_diamint),
                                                                ('profondeur_generatrice',self.userwdgfield.doubleSpinBox_gene),
                                                                ('materiau', self.userwdgfield.comboBox_materiau),
                                                                ('joint', self.userwdgfield.comboBox_joint),

                                                                ('calorifugeage',self.userwdgfield.comboBox_calor),
                                                                ('calorif_typ',self.userwdgfield.comboBox_calortype),
                                                                ('calorif_ep', self.userwdgfield.spinBox_calorep),

                                                                ('protection_catodique',self.userwdgfield.comboBox_protectioncatho),
                                                                ('mode_circulation', self.userwdgfield.comboBox_modecircu),
                                                                (
                                                                'fonction_cana', self.userwdgfield.comboBox_fonctioncan)
                                                                ])},
                                         'Objet': {'linkfield': 'id_objet',
                                                   'widgets': {
                                                       'commentaire': self.userwdgfield.textBrowser_commentaire}},
                                         'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                               'widgets': {}}}

                self.userwdgfield.toolButton_diametre.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_diametre))
                self.userwdgfield.toolButton_diamint.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_diamint))
                self.userwdgfield.toolButton_gene.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_gene))
                self.userwdgfield.toolButton_calorep.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_calorep))

                self.dbasechildwdgfield = []

                if self.parentWidget is None:
                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil,
                                                                   parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)








class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUIField2(QWidget):
    def __init__(self, parent=None):
        super(UserUIField2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_infralineaire_tool_ui_reseauchaleur.ui')
        uic.loadUi(uipath, self)