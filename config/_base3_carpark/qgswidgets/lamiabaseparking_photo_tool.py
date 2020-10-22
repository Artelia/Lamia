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

from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_photo_tool import BasePhotoTool
import os
import datetime
import glob
import sys




class BaseParkingPhotoTool(BasePhotoTool):

    LOADFIRST = False
    dbasetablename = 'Photo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseParkingPhotoTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)


