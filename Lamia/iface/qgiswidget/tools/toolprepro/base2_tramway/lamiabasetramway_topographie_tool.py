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




from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_topographie_tool import BaseTopographieTool
import os
import datetime

from .lamiabasetramway_pointtopo_tool import BaseTramwayPointtopoTool



"""
ne permettre de la renseigner qu en etant une classe fille de leve topo - sinon pas de datecreation
ca fout la merde....

"""


class BaseTramawayTopographieTool(BaseTopographieTool):


    def __init__(self, **kwargs):
        super(BaseTramawayTopographieTool, self).__init__(**kwargs)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Leves topographiques'
        self.dbasetablename = 'Topographie'
        # self.visualmode = [0, 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                           'idsource' : 'id_ressource',
                                       'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                       'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lk_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']}}
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_topographie_tool_icon.png')

        # ****************************************************************************************
        #properties ui


    """

    """
    def initTool(self):
        super(BaseTramawayTopographieTool, self).initTool()
        self.NAME = u"Relevés d'usure"
    """


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Topographie' : {'linkfield' : 'id_topographie',
                                                        'widgets' : {}},
                                        'Objet' : {'linkfield' : 'id_objet',
                                                    'widgets' : {}},
                                        'Ressource' : {'linkfield' : 'id_ressource',
                                                    'widgets' : {'file': self.toolwidgetmain.lineEdit_file,
                                                                'description': self.toolwidgetmain.lineEdit_nom,
                                                                'datetimeressource': self.toolwidgetmain.dateTimeEdit_date}}}
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.choosePhoto)
        self.toolwidgetmain.pushButton_open.clicked.connect(self.openFile)
        self.toolwidgetmain.pushButton_ajoutpointGPS.clicked.connect(self.ajoutPointGPS)
        self.toolwidgetmain.pushButton_importer.clicked.connect(self.importer)

        typpointlist = [elem[0] for elem in self.dbase.dbasetables['Pointtopo']['fields']['typepointtopo']['Cst']]
        self.toolwidgetmain.comboBox_typepoints.addItems(typpointlist)


        self.gpswidget = {'x' : {'widget' : self.toolwidgetmain.label_X,
                                    'gga' : 'Xcrs'},
                            'y': {'widget': self.toolwidgetmain.label_Y,
                                'gga': 'Ycrs'},
                            'zmngf': {'widget': self.toolwidgetmain.label_Z,
                                'gga': 'zmNGF'},
                            'dx': {'widget': self.toolwidgetmain.label_dX,
                                'gst': 'xprecision'},
                            'dy': {'widget': self.toolwidgetmain.label_dY,
                                'gst': 'yprecision'},
                            'dz': {'widget': self.toolwidgetmain.label_dZ,
                                'gst': 'zprecision'},
                            'zgps': {'widget': self.toolwidgetmain.label_zgps,
                                    'gga': 'elevation'},
                            'zwgs84': {'widget': self.toolwidgetmain.label_zwgs84,
                                    'gga': 'deltageoid'},
                            'raf09': {'widget': self.toolwidgetmain.label_raf09,
                                    'gga': 'RAF09'},
                            'hauteurperche': {'widget': self.toolwidgetmain.label_hautperche,
                                    'gga': 'hauteurperche'}
                            }


        self.toolwidgetmain.toolButton_valeurpoint1.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_valeurpoint1))
        self.toolwidgetmain.toolButton_valeurpoint2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_valeurpoint2))

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self
        self.propertieswdgPOINTTOPO= BaseTramwayPointtopoTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPOINTTOPO)
            
    def ajoutPointGPS(self):
        #self.propertieswdgPOINTTOPO.magicFunction()
        self.propertieswdgPOINTTOPO.featureSelected()
        #self.propertieswdgPOINTTOPO.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_position.findText('Crete'))
        self.propertieswdgPOINTTOPO.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_typepoints.currentIndex())
        self.propertieswdgPOINTTOPO.userwdg.doubleSpinBox_valeur1.setValue(self.userwdg.doubleSpinBox_valeurpoint1.value())
        self.propertieswdgPOINTTOPO.userwdg.doubleSpinBox_valeur2.setValue(self.userwdg.doubleSpinBox_valeurpoint2.value())
        success = self.propertieswdgPOINTTOPO.getGPSValues()
        if success:
            self.propertieswdgPOINTTOPO.saveFeature()





class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_topographie_tool_ui.ui')
        uic.loadUi(uipath, self)

