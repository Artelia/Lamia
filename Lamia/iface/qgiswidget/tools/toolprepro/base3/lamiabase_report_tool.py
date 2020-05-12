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



import os, sys, datetime
from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget)

from ...lamia_abstractformtool import AbstractLamiaFormTool

def tr(msg):
    return QtCore.QCoreApplication.translate('BaseReportTool',msg)

class BaseReportTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'report'
    LOADFIRST = False

    tooltreewidgetCAT = tr('Resources')
    tooltreewidgetSUBCAT = tr('Report')
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_report_tool_icon.png')

    tempparentjoin = {}
    linkdict = {'colparent': 'id_object',
                'colthistable': 'id_resource',
                    'tctable': 'Tcobjectresource',
                    'tctablecolparent':'lid_object',
                    'tctablecolthistable':'lid_resource'}
    for tablename in ['observation', 'node', 'edge', 'equipment']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin


    def __init__(self, **kwargs):
        super(BaseReportTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs



    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.chooseFile)
        self.toolwidgetmain.pushButton_openph.clicked.connect(self.openFile)

        self.formtoolwidgetconfdictmain = {'report' : {'linkfield' : 'id_rapport',
                                                            'widgets' : { }},
                                            'object' : {'linkfield' : 'id_objet',
                                                        'widgets' : {'name' : self.toolwidgetmain.lineEdit_nom}},
                                            'resource' : {'linkfield' : 'id_resource',
                                                        'widgets' : {'file': self.toolwidgetmain.lineEdit_file,
                                                                    'description': self.toolwidgetmain.lineEdit_description,
                                                                    'datetimeresource': self.toolwidgetmain.dateTimeEdit}}}




    def openFile(self):
        if self.currentFeaturePK is not None:
            sql = "SELECT file FROM report_qgis  WHERE pk_report = " + str(self.currentFeaturePK)
            query = self.dbase.query(sql)
            #result = [row[0] for row in query]
            resultfile = query[0][0]
            if os.path.isfile(self.dbase.completePathOfFile(resultfile)):
                filepath = self.dbase.completePathOfFile(resultfile)
                os.startfile(filepath)


    def chooseFile(self):

        file , extension= self.mainifacewidget.qfiledlg.getOpenFileName(None, 'Choose the file', self.mainifacewidget.imagedirectory,
                                                                    'All (*.*)', '')

        if file:
            self.toolwidget.lineEdit_file.setText(os.path.normpath(file))


    #def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict({'datetimeresource': datecreation}, False)




    def postSaveFeature(self, boolnewfeature):
        pass



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_report_tool_ui.ui')
        uic.loadUi(uipath, self)