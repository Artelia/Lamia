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



import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import numpy as np
import shutil
import io
import glob

from ..base2.Lamia_exportshp_tool import ExportShapefileTool


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class DigueExportShapefileTool(ExportShapefileTool):

    def __init__(self, **kwargs):
        super(DigueExportShapefileTool, self).__init__(**kwargs)




