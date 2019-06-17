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
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView,QComboBox)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView,QComboBox)

from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
if False:
    from ..toolprepro.InspectionDigue_photos_tool import PhotosTool
    from ..toolprepro.InspectionDigue_observation_tool import ObservationTool
    from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
if True:
    from ...toolprepro.base.lamiabase_photo_tool  import BasePhotoTool
    from ...toolprepro.base.lamiabase_observation_tool import BaseObservationTool
    #from ...toolabstract.inspectiondigue_abstractworker import AbstractWorker
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from ..Base.Lamia_synth_zonegeo_tool import SyntheseZonegeoTool


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class SyntheseDigueZonegeoTool(SyntheseZonegeoTool):

    DBASES = ['base_digue']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(SyntheseDigueZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

 