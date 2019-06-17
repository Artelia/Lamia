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
import os
# from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal
import numpy as np
import glob

#from .tools.Lamia_exportshpdialog import ExportShapefileDialog
from ..base.Lamiabase_import import importShapefileBaseWorker

#class exportShapefileWorker(AbstractWorker):


class importShapefileAssainissementWorker(importShapefileBaseWorker):


    def __init__(self, dbase=None, windowdialog=None, reporttype=None, pdffile=None):
        # AbstractWorker.__init__(self)

        super(importShapefileAssainissementWorker, self).__init__(dbase, windowdialog)

