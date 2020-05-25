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
import os, logging

from qgis.PyQt.QtWidgets import (QWidget, QVBoxLayout)
from qgis.PyQt import uic, QtCore

from .subwidget_abstract import AbstractSubWidget

class GpsValuesWidget(AbstractSubWidget):

    UIPATH = os.path.join(os.path.dirname(__file__), 'subwidget_gpsvalues_ui.ui')

    def __init__(self, 
                parentwdg=None,  
                parentframe=None, 
                searchdbase='', 
                searchfieldtoshow=[],
                parentlidfield=None):
        super(GpsValuesWidget, self).__init__(parent=parentwdg,parentframe=parentframe)


    
