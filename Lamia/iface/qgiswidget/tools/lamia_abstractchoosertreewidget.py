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


import qgis
import qgis.utils
from qgis.PyQt import uic, QtCore, QtGui

debugconnector = False


class AbstractChooserTreeWidget(QtCore.QObject):

    def __init__(self, **kwargs):
        super(AbstractChooserTreeWidget, self).__init__()
        self.dbase = kwargs.get('dbaseparser', None)
        self.mainifacewidget = kwargs.get('mainifacewidget', None)
        self.treewidget = self.mainifacewidget.ElemtreeWidget

    def selectFeature(self,pk=None):
        raise NotImplementedError

    def toolbarNew(self):
        raise NotImplementedError

    def toolbarUndo(self):
        raise NotImplementedError

    def toolbarDelete(self):
        raise NotImplementedError


    def toolbarSave(self):
        raise NotImplementedError
    

    def onActivation(self):
        raise NotImplementedError

    def onDesactivation(self):
        raise NotImplementedError

    def qtreeitemSelected(self):
        raise NotImplementedError

    def disconnectTreewidget(self):
        raise NotImplementedError


    def connectTreewidget(self):
        raise NotImplementedError
    