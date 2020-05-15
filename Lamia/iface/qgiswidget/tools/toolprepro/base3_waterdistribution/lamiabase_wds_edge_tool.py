# -*- coding: utf-8 -*-

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

import os
import logging
from collections import OrderedDict

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)


from ..base3.lamiabase_edge_tool import BaseEdgeTool
from .lamiabase_wds_camera_tool import BaseWaterdistributionCameraTool as BaseCameraTool
from .lamiabase_wds_sketch_tool import BaseWaterdistributionSketchTool as BaseSketchTool



class BaseWaterdistributionEdgeTool(BaseEdgeTool):



    def __init__(self, **kwargs):
        super(BaseWaterdistributionEdgeTool, self).__init__(**kwargs)





    def initMainToolWidget(self):
        # ****************************************************************************************
        #   userui Field
        if self.dbase.variante in [None, 'Lamia']:
            self.toolwidgetmain = UserUIField()

            self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                        'widgets': OrderedDict([('type_eau', self.toolwidgetmain.comboBox_typeeau),
                                                                                ('branchement', self.toolwidgetmain.comboBox_branchement),
                                                                                ('domaine', self.toolwidgetmain.comboBox_domaine),

                                                                                ('diametre_ext', self.toolwidgetmain.doubleSpinBox_diametre),
                                                                                ('profondeur_generatrice', self.toolwidgetmain.doubleSpinBox_gene),
                                                                                ('materiau', self.toolwidgetmain.comboBox_materiau),
                                                                                ('joint', self.toolwidgetmain.comboBox_joint),

                                                                                ('protection_catodique',self.toolwidgetmain.comboBox_protectioncatho),
                                                                                ('mode_circulation', self.toolwidgetmain.comboBox_modecircu),
                                                                                ('fonction_cana',self.toolwidgetmain.comboBox_fonctioncan)
                                                                                ])},
                                                'Objet': {'linkfield': 'id_objet',
                                                        'widgets': {
                                                                    'commentaire':self.toolwidgetmain.textBrowser_commentaire}},
                                                'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                                    'widgets': {}}}

            self.toolwidgetmain.toolButton_diametre.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diametre))
            self.toolwidgetmain.toolButton_gene.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_gene))


            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self

            #if self.parentWidget is None:
            self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        elif self.dbase.variante in ['Reseau_chaleur']:
            self.toolwidgetmain = UserUIField2()

            self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                        'widgets': OrderedDict(
                                                            [('type_eau', self.toolwidgetmain.comboBox_typeeau),
                                                            ('branchement', self.toolwidgetmain.comboBox_branchement),
                                                            ('domaine', self.toolwidgetmain.comboBox_domaine),

                                                            ('diametre_ext',self.toolwidgetmain.doubleSpinBox_diametre),
                                                            ('diametre_int',self.toolwidgetmain.doubleSpinBox_diamint),
                                                            ('profondeur_generatrice',self.toolwidgetmain.doubleSpinBox_gene),
                                                            ('materiau', self.toolwidgetmain.comboBox_materiau),
                                                            ('joint', self.toolwidgetmain.comboBox_joint),

                                                            ('calorifugeage',self.toolwidgetmain.comboBox_calor),
                                                            ('calorif_typ',self.toolwidgetmain.comboBox_calortype),
                                                            ('calorif_ep', self.toolwidgetmain.spinBox_calorep),

                                                            ('protection_catodique',self.toolwidgetmain.comboBox_protectioncatho),
                                                            ('mode_circulation', self.toolwidgetmain.comboBox_modecircu),
                                                            (
                                                            'fonction_cana', self.toolwidgetmain.comboBox_fonctioncan)
                                                            ])},
                                        'Objet': {'linkfield': 'id_objet',
                                                'widgets': {
                                                    'commentaire': self.toolwidgetmain.textBrowser_commentaire}},
                                        'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                            'widgets': {}}}

            self.toolwidgetmain.toolButton_diametre.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diametre))
            self.toolwidgetmain.toolButton_diamint.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diamint))
            self.toolwidgetmain.toolButton_gene.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_gene))
            self.toolwidgetmain.toolButton_calorep.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_calorep))

            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self


            self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_wds_edge_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUIField2(QWidget):
    def __init__(self, parent=None):
        super(UserUIField2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasewds_edge_tool_ui_heatingnetwork.ui')
        uic.loadUi(uipath, self)