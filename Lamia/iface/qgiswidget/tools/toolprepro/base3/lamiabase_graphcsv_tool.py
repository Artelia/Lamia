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


import os
import datetime
import sys


import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
font = {'family' : 'normal','weight' : 'bold','size'   : 8}
matplotlib.rc('font', **font)
#matplotlib.rc('xtick', labelsize=20)
#matplotlib.rc('ytick', labelsize=20)
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget,QComboBox, QDoubleSpinBox, QSpinBox, QHeaderView,
                                     QTableWidgetItem)

from ...lamia_abstractformtool import AbstractLamiaFormTool
from .lamiabase_graph_tool import BaseGraphTool
from Lamia.libslamia.lamiagraph.lamiagraphcsv import GraphMakerCsv

base3 = QtCore.QObject()

class BaseGraphcsvTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = 'graphcsv'
    DBASETABLENAME = 'graph'
    LOADFIRST = False

    tooltreewidgetCAT =QtCore.QCoreApplication.translate('base3','Resources')
    tooltreewidgetSUBCAT =QtCore.QCoreApplication.translate('base3','Graph_csv')
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_graph_tool_icon.png')

    tempparentjoin = {}
    linkdict = {'colparent': 'id_object',
                'colthistable': 'id_resource',
                    'tctable': 'Tcobjectresource',
                    'tctablecolparent':'lid_object',
                    'tctablecolthistable':'lid_resource'}
    for tablename in ['profile', 'node', 'edge', 'surface','facility']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin

    TABLEFILTERFIELD = {'graphtype': 'CSV' }



    def __init__(self, **kwargs):
        super(BaseGraphcsvTool, self).__init__(**kwargs)
        # self.figuretype = plt.figure()
        # self.axtype = self.figuretype.add_subplot(111)
        # self.mplfigure = FigureCanvas(self.figuretype)

        self.graphmaker = GraphMakerCsv(self.dbase)
        self.figuretype = self.graphmaker.figuretype
        self.mplfigure = FigureCanvas(self.figuretype)
        self.graphspec = self.graphmaker.graphspec

    def initMainToolWidget(self):
        # ****************************************************************************************
        #   userui Field

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'graph' : {'linkfield' : 'id_graph',
                                                        'widgets' : {'graphsubtype': self.toolwidgetmain.comboBox_graphtype}},
                                                'object' : {'linkfield' : 'id_object',
                                                            'widgets' : {}},
                                                'resource' : {'linkfield' : 'id_resource',
                                                            'widgets' : {'file': self.toolwidgetmain.lineEdit_csv}}}
 
        self.toolwidgetmain.pushButton_addline.clicked.connect(self.addrow)
        self.toolwidgetmain.pushButton_delline.clicked.connect(self.removerow)

        self.toolwidgetmain.toolButton_choosecsv.clicked.connect(self.chooseCsvFile)

        self.enableTypeComboBox()

        self.toolwidgetmain.frame_graph.layout().addWidget(self.mplfigure)
        self.toolbar = NavigationToolbar(self.mplfigure, self.toolwidgetmain.frame_graph)
        self.toolwidgetmain.frame_graph.layout().addWidget(self.toolbar)


    def chooseCsvFile(self):
        file = None
        file , extension= self.mainifacewidget.qfiledlg.getOpenFileName(None, 'Choose the csv file', self.mainifacewidget.imagedirectory,
                                                                    'Image (*.csv)', '')
        if file:
            self.toolwidgetmain.lineEdit_csv.setText(os.path.normpath(file))
            datas = self.loadGraphinCsv()
            self._fillTableWidgetWithDatas(datas)

    def enableTypeComboBox(self):
        if self.toolwidgetmain.tableWidget.rowCount() == 0:
            self.toolwidgetmain.comboBox_graphtype.setEnabled(True)
        else:
            self.toolwidgetmain.comboBox_graphtype.setEnabled(False)

    def _disableSubtypeNotInSpec(self):
        # self.toolwidgetmain.comboBox_graphtype
        subtypes = self.dbase.dbasetables[self.DBASETABLENAME]['fields']['graphsubtype']['Cst']
        for i, elem in enumerate(subtypes):
            if elem[1] not in list(self.graphspec.keys()):
                self.toolwidgetmain.comboBox_graphtype.model().item(i).setEnabled(False)
            else:
                self.toolwidgetmain.comboBox_graphtype.model().item(i).setEnabled(True)

    def postSelectFeature(self):
        self._disableSubtypeNotInSpec()
        self.toolwidgetmain.tableWidget.setRowCount(0)
        
        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict({'datetimeresource' : datecreation},checkifinforgottenfield=False)
        else :
            graphtype = self._getGraphType()
            typetext =  self.dbase.getConstraintTextFromRawValue(self.DBASETABLENAME,'graphsubtype',graphtype)
            self.toolwidgetmain.comboBox_graphtype.setCurrentIndex(self.toolwidgetmain.comboBox_graphtype.findText(typetext))
            # graphdatas = self.loadGraphinCsv(self.currentFeaturePK )
            graphdatas = self.graphmaker.getGraphData(self.currentFeaturePK)

            if graphdatas is None:
                return
            self._fillTableWidgetWithDatas(graphdatas)
            # self.showGraphCsv(self.currentFeaturePK)
        self.graphmaker.showGraph(self.currentFeaturePK)

        self.enableTypeComboBox()


    def postSaveFeature(self, savedfeaturepk=None):

        pkgraphique = savedfeaturepk

        if self.currentFeaturePK is None:   #first creation
            idgraph, pkres = self.dbase.getValuesFromPk(self.DBASETABLENAME.lower() + '_qgis',
                                                 ['id_' + self.DBASETABLENAME.lower(),'pk_resource'],
                                                 savedfeaturepk)
            datecreation = datetime.datetime.now().strftime("%Y-%m-%d")
            datetimecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            filegraphique = os.path.join('.', self.DBASETABLENAME, ''.join(datecreation.split('-')),
                                    str(pkgraphique) + '.csv')
            if not os.path.exists(os.path.dirname(self.dbase.completePathOfFile(filegraphique))):
                os.makedirs(os.path.dirname(self.dbase.completePathOfFile(filegraphique)))

            sql = "UPDATE resource SET  file = '" + filegraphique + "', datetimeresource = '" + datetimecreation + "'"
            sql += " WHERE pk_resource = " + str(pkres)
            query = self.dbase.query(sql)

        self.saveGraphinCsv(savedfeaturepk)


    def _getGraphType(self):
        if self.currentFeaturePK is not None:
            graphtype = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                                    'graphsubtype',
                                                    self.currentFeaturePK)
        else:
            typetext = self.toolwidgetmain.comboBox_graphtype.currentText()
            graphtype = self.dbase.getConstraintRawValueFromText(self.DBASETABLENAME, 'graphsubtype', typetext)
        return graphtype


    def _getGraphFile(self):
        if self.currentFeaturePK is not None:
            filegraphique = self.dbase.getValuesFromPk(self.DBASETABLENAME + '_qgis',
                                                'file',
                                                self.currentFeaturePK )
        else:
            filegraphique = self.toolwidgetmain.lineEdit_csv.text()
        return filegraphique

    def _fillTableWidgetWithDatas(self,graphdatas):
        self.toolwidgetmain.tableWidget.setRowCount(0)
        graphtype = self._getGraphType()
        header = list(self.graphspec[graphtype].keys())
        self.toolwidgetmain.tableWidget.setHorizontalHeaderLabels(header)
        
        for row in graphdatas:
            self.addrow()
            lastrow = self.toolwidgetmain.tableWidget.rowCount() - 1
            self.toolwidgetmain.tableWidget.setCurrentCell(lastrow, 0)
            for col, (index, ilist) in enumerate(self.graphspec[graphtype].items()):
                if col > len(row)-1:
                    break
                if ilist :
                    combo = self.toolwidgetmain.tableWidget.cellWidget(lastrow, col)
                    indexcombo = combo.findText(row[col])
                    if indexcombo >=0:
                        combo.setCurrentIndex(indexcombo)
                else:
                    item = QTableWidgetItem(str(row[col]))
                    self.toolwidgetmain.tableWidget.setItem(lastrow, col, item)



    def addrow(self):
        introw = self.toolwidgetmain.tableWidget.currentRow()
        self.toolwidgetmain.tableWidget.insertRow(introw + 1)
        typegraph = self._getGraphType()
        self.toolwidgetmain.tableWidget.setColumnCount(len(self.graphspec[typegraph]))

        if typegraph in self.graphspec.keys():
            for i, (index, ilist) in enumerate(self.graphspec[typegraph].items()):
                if ilist :
                    combobox = QComboBox()
                    combobox.addItems(ilist)
                    self.toolwidgetmain.tableWidget.setCellWidget(introw + 1, i, combobox)
                else:
                    pass
                
        header = self.toolwidgetmain.tableWidget.horizontalHeader()
        header.resizeSections(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        self.enableTypeComboBox()


    def removerow(self):
        introw = self.toolwidgetmain.tableWidget.currentRow()
        self.toolwidgetmain.tableWidget.removeRow(introw)

        self.enableTypeComboBox()
    
 
    def saveGraphinCsv(self,savedfeaturepk):
        """Lit le QTableWidget et enregistre son contenu dans un fichier csv
        """
        valuestosave=[]
        for row in range(0, self.toolwidgetmain.tableWidget.rowCount()):
                ligne = []
                for column in range(0, self.toolwidgetmain.tableWidget.columnCount()):
                    if self.toolwidgetmain.tableWidget.cellWidget(row, column) is not None:
                        columnwdg = self.toolwidgetmain.tableWidget.cellWidget(row, column)
                        if isinstance(columnwdg,QComboBox):
                            value =  columnwdg.currentText()
                        elif isinstance(columnwdg,QDoubleSpinBox) or isinstance(columnwdg,QSpinBox):
                            value = str(columnwdg.value())
                            if value is None:
                                value = '0.0'
                        else:
                            value = 'NULL'
                    elif self.toolwidgetmain.tableWidget.item(row, column) is not None:
                        value = self.toolwidgetmain.tableWidget.item(row, column).text().strip()
                    else:
                        value=''
                    
                    ligne.append(value)
                valuestosave.append(ligne)

        self.graphmaker.saveGraphData(savedfeaturepk, valuestosave)




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_graphcsv_tool_ui.ui')
        uic.loadUi(uipath, self)

