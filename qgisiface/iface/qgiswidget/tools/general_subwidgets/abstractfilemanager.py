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

try:
    from qgis.PyQt.QtGui import QFileDialog, QWidget
except ImportError:
    from qgis.PyQt.QtWidgets import QFileDialog, QWidget
import os, inspect, glob, textwrap
from qgis.PyQt import uic, QtGui, QtCore


class AbstractFileManager(QWidget):
    """QWidget for interacting with  AbstractLibsLamia inherited classes :
        * a combobox with all the conf names
        * edit/new buttons
    """

    def __init__(self, mainwindows=None, toolclass=None):
        """Constructor
        :param mainwindows: the qt mainwindows, essentially used for accessing to filedialog
        :param toolclass: the toolclass (inheriting AbstractLibsLamia) linked with this file manager
        """
        super(AbstractFileManager, self).__init__()

        uipath = os.path.join(os.path.dirname(__file__), "abstractfilemanager.ui")
        uic.loadUi(uipath, self)

        self.toolclass = toolclass
        self.mainwindows = mainwindows

        self.dbase = mainwindows.dbase
        self.qfiledialog = self.mainwindows.qfiledlg

        self.comboBox_files.currentIndexChanged.connect(self.comboChanged)
        self.toolButton_new.clicked.connect(self.new)
        self.toolButton_edit.clicked.connect(self.edit)
        self.toolButton_delete.clicked.connect(self.delete)

    def reset(self):
        self.toolclass.getNamePathFiles()
        self.comboBox_files.clear()
        for filename in self.toolclass.names_files:
            self.comboBox_files.addItems([filename])

    def edit(self):
        currentfile = self.comboBox_files.currentText()
        currentfilepath = self.toolclass.names_files[currentfile]
        if currentfilepath != "":
            os.startfile(currentfilepath)

    def new(self):
        pass

    def delete(self):
        currentxt = self.getCurrentText()
        if currentxt[0] == self.toolclass.projectcharacter:
            currentfilepath = self.toolclass.names_files[currentxt]
            os.remove(currentfilepath)
            self.reset()

    def comboChanged(self, comboindex):
        filename = self.comboBox_files.itemText(comboindex)
        if filename and len(filename) > 0:
            if filename[0] == self.toolclass.projectcharacter:
                boolenabled = True
            else:
                boolenabled = False

            self.toolButton_edit.setEnabled(boolenabled)
            self.toolButton_delete.setEnabled(boolenabled)

    def getCurrentText(self):
        return self.comboBox_files.currentText()

    # def getCurrentPath(self):
    #     comboext = self.comboBox_files.currentText()
    #     combopath = self.getCompletPath(comboext)
    #     return combopath

    # def getCompletPath(self, filename):
    #     currentfilepath = None
    #     if filename is not None and len(filename) > 0:
    #         if filename[0] == self.toolclass.projectcharacter:
    #             currentfilepath = os.path.join(
    #                 self.confdataproject, filename[1:] + self.toolclass.fileext
    #             )
    #         else:
    #             currentfilepath = os.path.join(
    #                 self.confdataplugin, filename + self.toolclass.fileext
    #             )

    #     return currentfilepath

