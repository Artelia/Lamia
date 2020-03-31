# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
import qgis.utils, qgis.core
from qgis.PyQt.QtWidgets import (QApplication)

from ..ifaceabstractconnector import LamiaIFaceAbstractConnectors

class QgisConnector(LamiaIFaceAbstractConnectors):

    def __init__(self):
        LamiaIFaceAbstractConnectors.__init__(self)
        self.widget = None
        self.canvas = None


    def showNormalMessage(self, text):
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().pushMessage("Lamia " ,text, qgis.core.Qgis.Info)
        else:
            print('normalMessage', text)
        QApplication.processEvents()


    def showErrorMessage(self,msg):
        pass

    def createProgressBar(self):
        pass

    def updateProgressBar(self,int):
        pass

    def closeProgressBar(self,int):
        pass