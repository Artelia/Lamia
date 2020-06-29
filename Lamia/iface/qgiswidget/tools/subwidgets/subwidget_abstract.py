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
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget,QVBoxLayout)

class AbstractSubWidget(QWidget):

    UIPATH = None

    def __init__(self, parentwdg = None,**kwargs):
        super(AbstractSubWidget, self).__init__(parent=parentwdg)
        self.parentwdg = parentwdg
        self.parentframe = kwargs.get('parentframe',None)
        
        self.loadUIFile()
        self._loadInParentFrame()

    def postSelectFeature(self):
        pass

    def postSaveFeature(self, parentfeaturepk=None):
        pass

    def loadUIFile(self):
        if self.UIPATH:
            uic.loadUi(self.UIPATH, self)

    def _loadInParentFrame(self):
        if self.parentframe:
            if self.parentframe.layout() is not None:
                self.parentframe.layout().addWidget(self)
            else:
                vlayout = QVBoxLayout()
                vlayout.addWidget(self)
                self.parentframe.setLayout(vlayout)
