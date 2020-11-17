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
    from qgis.PyQt.QtGui import ( QFileDialog , QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import ( QFileDialog, QWidget )
import os, inspect, glob, textwrap
from qgis.PyQt import uic, QtGui, QtCore


class AbstractFileManager(QWidget):

    projectcharacter = '_'

    def __init__(self,  mainwindows=None, toolclass=None, fileext=None):
        super(AbstractFileManager, self).__init__()

        uipath = os.path.join(os.path.dirname(__file__), 'abstractfilemanager.ui')
        uic.loadUi(uipath, self)

        self.toolclass = toolclass
        self.mainwindows = mainwindows
        self.fileext = fileext
        self.dbase = mainwindows.dbase
        self.qfiledialog = self.mainwindows.qfiledlg

        if hasattr(self.toolclass, 'confdataplugin'):
            self.confdataplugin = self.toolclass.confdataplugin
        else:
            self.confdataplugin = os.path.join(os.path.dirname(inspect.getsourcefile(self.toolclass.__class__)), self.dbase.worktype)
        
        if hasattr(self.toolclass, 'confdataproject'):
            self.confdataproject = self.toolclass.confdataproject
        else:
            self.confdataproject = os.path.join(self.dbase.dbaseressourcesdirectory, 'config', self.toolclass.POSTPROTOOLNAME)

        self.comboBox_files.currentIndexChanged.connect(self.comboChanged)
        self.toolButton_new.clicked.connect(self.new)
        self.toolButton_edit.clicked.connect(self.edit)
        self.toolButton_delete.clicked.connect(self.delete)


    def reset(self):
        self.comboBox_files.clear()
        for workdir in [self.confdataplugin, self.confdataproject]:
            for filename in glob.glob(os.path.join(workdir, '*' + self.fileext)):
                basename = os.path.basename(filename).split('.')[0]
                if basename != 'README':
                    #self.exportshapefiledialog.comboBox_type.addItems([basename])
                    if workdir == self.confdataproject:
                        basename = self.projectcharacter + basename
                    self.comboBox_files.addItems([basename])


    def edit(self):
        currentfile = self.comboBox_files.currentText()
        currentfilepath = self.getCompletPath(currentfile)

        if currentfilepath != '':
            os.startfile(currentfilepath)



    def new(self):
        pass

    def delete(self):
        currentxt = self.getCurrentText()
        if currentxt[0] == self.projectcharacter:
            os.remove(self.getCurrentPath())
            self.reset()



    def comboChanged(self, comboindex):
        filename = self.comboBox_files.itemText(comboindex)
        filepath = self.getCompletPath(filename)

        if filename and len(filename) > 0:
            if filename[0] == self.projectcharacter:
                boolenabled = True
            else:
                boolenabled = False

            self.toolButton_edit.setEnabled(boolenabled)
            self.toolButton_delete.setEnabled(boolenabled)


    def getCurrentText(self):
        return self.comboBox_files.currentText()

    def getCurrentPath(self):
        comboext = self.comboBox_files.currentText()
        combopath = self.getCompletPath(comboext)
        return combopath



    def getCompletPath(self, filename):
        currentfilepath = None
        if filename is not None and len(filename) > 0 :
            if filename[0] == self.projectcharacter:
                currentfilepath = os.path.join(self.confdataproject,filename[1:] +  self.fileext)
            else:
                currentfilepath = os.path.join(self.confdataplugin, filename + self.fileext )

        return currentfilepath


