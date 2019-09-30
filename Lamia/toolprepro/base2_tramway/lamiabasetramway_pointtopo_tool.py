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

from qgis.PyQt import uic, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_pointtopo_tool import BasePointtopoTool
import os
import qgis





class BaseTramwayPointtopoTool(BasePointtopoTool):

    LOADFIRST = False
    dbasetablename = 'Pointtopo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseTramwayPointtopoTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)


    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()

            self.linkuserwdgfield = {'Pointtopo' : {'linkfield' : 'id_pointtopo',
                                             'widgets' : {'typepointtopo': self.userwdgfield.comboBox_position,
                                                          'valeur1': self.userwdgfield.doubleSpinBox_valeur1,
                                                          'valeur2': self.userwdgfield.doubleSpinBox_valeur2,

                                                            'x': self.userwdgfield.doubleSpinBox_X,
                                                            'y': self.userwdgfield.doubleSpinBox_Y,
                                                            'zmngf': self.userwdgfield.doubleSpinBox_Zngf,
                                                            'dx': self.userwdgfield.doubleSpinBox_dX,
                                                            'dy': self.userwdgfield.doubleSpinBox_dY,
                                                            'dz': self.userwdgfield.doubleSpinBox_dZ,
                                                            'zwgs84': self.userwdgfield.doubleSpinBox_Zwgs84,
                                                            'zgps': self.userwdgfield.doubleSpinBox_Zgps,
                                                            'raf09': self.userwdgfield.doubleSpinBox_raf09,
                                                            'hauteurperche': self.userwdgfield.doubleSpinBox_hautperche}}
                                                          }
            if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Topographie':
                self.pushButton_addFeature.setEnabled(True)
            else:
                self.pushButton_addFeature.setEnabled(False)

            self.userwdgfield.pushButton_catchvalues.clicked.connect(self.getGPSValues)

            self.gpswidget = {'x' : {'widget' : self.userwdgfield.label_X,
                                     'gga' : 'Xcrs'},
                              'y': {'widget': self.userwdgfield.label_Y,
                                    'gga': 'Ycrs'},
                              'zmngf': {'widget': self.userwdgfield.label_Z,
                                    'gga': 'zmNGF'},
                              'dx': {'widget': self.userwdgfield.label_dX,
                                    'gst': 'xprecision'},
                              'dy': {'widget': self.userwdgfield.label_dY,
                                    'gst': 'yprecision'},
                              'dz': {'widget': self.userwdgfield.label_dZ,
                                    'gst': 'zprecision'},
                              'zgps': {'widget': self.userwdgfield.label_zgps,
                                     'gga': 'elevation'},
                              'zwgs84': {'widget': self.userwdgfield.label_zwgs84,
                                       'gga': 'deltageoid'},
                              'raf09': {'widget': self.userwdgfield.label_raf09,
                                       'gga': 'RAF09'},
                              'hauteurperche': {'widget': self.userwdgfield.label_hautperche,
                                        'gga': 'hauteurperche'}
                              }


        
class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiatramway_pointtopo_tool_ui.ui')
        uic.loadUi(uipath, self)