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


from collections import OrderedDict
import os
import datetime
import numpy as np
import sys
import csv
import pandas as pd
import math

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

base3 = QtCore.QObject()

class BaseGraphcsvTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'graph'
    LOADFIRST = False

    tooltreewidgetCAT =QtCore.QCoreApplication.translate('base3','Resources')
    tooltreewidgetSUBCAT =QtCore.QCoreApplication.translate('base3','Graph_csv')
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_graph_tool_icon.png')

    tempparentjoin = {}
    linkdict = {'colparent': 'id_object',
                'colthistable': 'id_resource',
                    'tctable': 'tcobjectresource',
                    'tctablecolparent': 'lid_object',
                    'tctablecolthistable': 'lid_resource'}
    for tablename in ['profile','edge','node', 'surface']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin

    TABLEFILTERFIELD = {'graphtype': 'CSV' }



    def __init__(self, **kwargs):
        super(BaseGraphcsvTool, self).__init__(**kwargs)
        self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111)
        self.mplfigure = FigureCanvas(self.figuretype)

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

        self.graphspec = {'SIM': {'x': [],
                                  'y':[],
                                },
                          'RAD': {'var': [],
                                  'value':[],
                                },
                          'PTR': {'x': [],
                                  'y':[],
                                  'Position': ['/',
                                                'Crete',
                                                'Talus digue',
                                                'Sommet risberme',
                                                'Talus risberme',
                                                'Talus risberme - pied',
                                                'Pied de digue',
                                                'Franc-bord',
                                                'Berge',
                                                'Pied de berge',
                                                'Hors digue',
                                                'Plusieurs parties',
                                                'Indefini'],
                                  'Nature': ['/',
                                            'Abscence de revetement',
                                            'Dispositif fusible',
                                            'Enrochement',
                                            'Fondation meuble',
                                            'Fondation rocheuse',
                                            'Contre fosse(cote terre)',
                                            'Gabion',
                                            'Indefini',
                                            'Mur de soutenement',
                                            'Ouvrage parafouille',
                                            'Palplanche',
                                            'Paroi etanche',
                                            'Perre',
                                            'Pieux',
                                            'Remblais',
                                            'Ouvrage de revanche',
                                            'Revetement',
                                            'Seuil, deversoir',
                                            'Zone de dissipation',
                                            'Zone urbanisee'],
                                  'Materiau': ['/',
                                                'Acier',
                                                'Bentonite-ciment',
                                                'Beton',
                                                'Bois',
                                                'Concasse 0/80',
                                                'Dechet carriere 0/400',
                                                'Enrobe',
                                                'Fraisat recycle',
                                                'Galets 0/100',
                                                'Geotextile',
                                                'Geomembrane',
                                                'Graviers 0/33',
                                                'Grillage',
                                                'Indefini',
                                                'Limons',
                                                'Limons et sables',
                                                'Moellons',
                                                'Lit naturel du fosse',
                                                'Paves',
                                                'Plaques beton joitives',
                                                'Panneaux JK',
                                                'Pierres maconnees',
                                                'Pierres seches',
                                                'Remblais',
                                                'Roches appareilles',
                                                'Roches betonnees',
                                                'Roches deversee',
                                                'Sables',
                                                'Schistes 0/100',
                                                'Silts',
                                                'Terre vegetale',
                                                'Tuyau drain',
                                                'Tout venant brut',
                                                'Vegetalise enherbe',
                                                'Vegetalise arbustif',
                                                'Vegetalise boise'],
                                  'Cote': ['/',
                                            'Eau',
                                            'Terre',
                                            'Crête'],
                                },      
                         }       

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

    def postSelectFeature(self):
        self.toolwidgetmain.tableWidget.setRowCount(0)
        self.axtype.clear()
        self.figuretype.canvas.draw()
        
        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict({'datetimeresource' : datecreation},checkifinforgottenfield=False)
        else :
            graphtype = self._getGraphType()
            typetext =  self.dbase.getConstraintTextFromRawValue(self.DBASETABLENAME,'graphsubtype',graphtype)
            self.toolwidgetmain.comboBox_graphtype.setCurrentIndex(self.toolwidgetmain.comboBox_graphtype.findText(typetext))
            graphdatas = self.loadGraphinCsv(self.currentFeaturePK )
            if graphdatas is None:
                return
            self._fillTableWidgetWithDatas(graphdatas)
            self.showGraphCsv(self.currentFeaturePK)

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
        else:
            filegraphique = self.dbase.getValuesFromPk(self.DBASETABLENAME + '_qgis',
                                                        'file',
                                                        self.currentFeaturePK )

        self.saveGraphinCsv(self.dbase.completePathOfFile(filegraphique))


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


    def showGraphCsv(self, featurepk):

        graphtype = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                    'graphsubtype',
                                    featurepk)
        graphdatas=self.loadGraphinCsv(featurepk)
        pdgraphdatas= pd.DataFrame(graphdatas)
        headersname = list(self.graphspec[graphtype].keys())
        if len(pdgraphdatas.columns) == len(headersname):
            pdgraphdatas.columns = headersname

        # self.axtype.clear()
        self.figuretype.clf(keep_observers=True)
        if graphtype in ['SIM']:
            self._makeSIMGraph(pdgraphdatas)
        elif graphtype in [ 'PTR']:
            self._makePTRGraph(pdgraphdatas)
        elif graphtype in [ 'RAD']:
            self._makeRADGraph(pdgraphdatas)

        self.figuretype.canvas.draw()


    def _makeSIMGraph(self,graphdatas):
        print('sim')
        # self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111, polar=False, label='plotgraph')
        try:
            graphdatas.plot(kind='line', x=0, y=1, ax=self.axtype)
            self.axtype.grid()
        except (TypeError,IndexError) as e:
            print('grapherror', e)

    def _makeRADGraph(self,pdgraphdatas):
        print('rad')
        # https://jingwen-z.github.io/data-viz-with-matplotlib-series8-radar-chart/

        # self.figuretype = plt.figure()
        # self.axtype = self.figuretype.add_subplot(111)

        # self.axtype = plt.subplot(111, polar=True)
        # self.figuretype.add_subplot(111)
        self.axtype = self.figuretype.add_subplot(111, polar=True, label='radgraph')

        # print(pdgraphdatas)
        # print(pdgraphdatas.columns.values.tolist())
        if not pdgraphdatas.columns.values.tolist():
            return
        datas = pdgraphdatas['value'].tolist()
        # print('*',datas, datas[:1])
        datas = datas + datas[:1]    #to close graph
        # print(datas)
        categories = pdgraphdatas['var'].values
        # print(categories)

        # categories = list(df)[1:]
        # values = df.mean().values.flatten().tolist()
        # values += values[:1] # repeat the first value to close the circular graph
        angles = [n / float(len(categories)) * 2 * math.pi for n in range(len(categories))]
        angles += angles[:1]

        # print(angles)
        # self.axtype = plt.subplot(111, polar=True)
        # # self.figuretype.add_subplot(111)
        # self.axtype = self.figuretype.add_subplot(111, polar=True)

        # fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8),
        #                     subplot_kw=dict(polar=True))

        # plt.xticks(angles[:-1], categories, color='grey', size=12)
        self.axtype.set_xticks(angles[:-1])
        self.axtype.set_xticklabels(categories)

        # setxticksvalues
        maxdatasvalue = max(datas)
        log10value = int(math.log10(maxdatasvalue))
        step = 10**log10value
        maxstep = 10**log10value * (int(maxdatasvalue/step) + 1)
        # print(step, maxstep)
        valuerange = range(step, maxstep, step)
        valuerangestr = [str(elem) for elem in valuerange]
        # print(valuerange,valuerangestr )

        self.axtype.set_yticks(valuerange)
        self.axtype.set_yticklabels(valuerangestr)

        # plt.yticks(np.arange(1, 6), ['1', '2', '3', '4', '5'],
        #         color='grey', size=12)
        # plt.yticks(valuerange, valuerangestr,
        #         color='grey', size=12)
        # plt.ylim(0, 5)
        self.axtype.set_rlabel_position(30)
        
        self.axtype.plot(angles, datas, linewidth=1, linestyle='solid')
        self.axtype.fill(angles, datas, 'skyblue', alpha=0.4)

        # plt.show()
        # self.axtype = ax



        if False:
            print(pdgraphdatas)
            datas = pdgraphdatas['value'].values
            # values += values[0]    #to close graph
            print(datas)
            categories = pdgraphdatas['var'].values
            print(categories)

            angles=np.linspace(0, 2*math.pi, len(categories), endpoint=False)
            # close the plot
            stats=np.concatenate((datas,[datas[0]]))
            angles=np.concatenate((angles,[angles[0]]))
            if False:
                # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
                N = len(categories)
                angles = [n / float(N) * 2 * math.pi for n in range(N)]
                angles += angles[0]

            print(datas)
            print(angles)
            print(categories)

            # fig=sns.plt.figure()
            ax = self.figuretype.add_subplot(111, polar=True)
            ax.plot(angles, datas, 'o-', linewidth=2)
            ax.fill(angles, datas, alpha=0.25)
            ax.set_thetagrids(angles * 180/math.pi, categories)
            ax.set_title('popo')
            ax.grid(True)

            if False:

                plt.xticks(angles[:-1], categories, color='grey', size=8)
                # self.axtype.set_rlabel_position(0)
                plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
                plt.ylim(0,40)


                self.axtype.plot(angles, values, linewidth=1, linestyle='solid')
                self.axtype.fill(angles, values, 'b', alpha=0.1)







    def _makePTRGraph(self,graphdatas):

        # self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111)

        Xgraph = [0.0]
        Zgraph = [0.0]
        typepartie = []

        for i in range(len(graphdatas)):
            try:
                Xgraph.append(Xgraph[-1] + float(graphdatas['x'][i]))
                Zgraph.append(Zgraph[-1] + float(graphdatas['y'][i]))
                typepartie.append(graphdatas['Nature'][i] + ' - ' + graphdatas['Materiau'][i])
            except (ValueError, KeyError) as e:
                return

        label = []
        for i in range(len(Xgraph)-1):
            typep = typepartie[i]
            graphcolor = 'black'
            graphlinestyle = '-'
            graphlinewidth = 3.0
            if 'Vegetalise enherbe' in typep:
                graphcolor = 'lightgreen'
            elif 'Vegetalise arbustif' in typep:
                graphcolor = 'seagreen'
            elif 'Vegetalise boise' in typep:
                graphcolor = 'darkgreen'
            elif 'Gabion' in typep:
                graphcolor = 'gray'
                graphlinestyle = '-'
                graphlinewidth = 5.
            elif 'Gravier 0/33' in typep:
                graphcolor = 'darkgray'
                graphlinestyle = '--'
            elif 'Enrobe' in typep:
                graphcolor = 'black'
                graphlinewidth = 4.
            elif 'Beton' in typep:
                graphcolor = 'gray'
            elif 'Pierre maconnees' in typep:
                graphcolor = 'gray'
                graphlinestyle = '--'
            elif 'Roches appareillees' in typep:
                graphcolor = 'gray'
                graphlinestyle = '-.'
            elif 'Abscence de revetement' in typep:
                graphcolor = 'saddlebrown'

            if typep not in label:
                label.append(typep)
            else:
                typep = None

            self.axtype.plot([Xgraph[i],Xgraph[i+1]], [Zgraph[i], Zgraph[i+1]], label=typep, color=graphcolor,
                                linewidth=graphlinewidth, linestyle=graphlinestyle)

        legend = self.axtype.legend(bbox_to_anchor=(0., 1.), loc="lower left", bbox_transform=self.figuretype.transFigure, prop={'size': 8})
        self.axtype.annotate('TERRE', xy=(0.05, 1.05), xycoords='axes fraction',horizontalalignment='left')
        self.axtype.annotate('EAU', xy=(0.95, 1.05), xycoords='axes fraction',horizontalalignment='right')

        #plt.ylabel('Z (m)', fontsize=8)
        self.axtype.set_ylabel('Z (m)', fontsize=8)

    def exportgraphCsv(self,featurepk,exportfile,width,height):
        self.showGraphCsv(featurepk)
        self.figuretype.set_size_inches(width / 25.4, height / 25.4)
        self.figuretype.savefig(exportfile, bbox_inches='tight', dpi=150)



    def loadGraphinCsv(self,graphpk=None):
        if graphpk is not None:
            filegraphique = self.dbase.getValuesFromPk(self.DBASETABLENAME + '_qgis',
                                                        'file',
                                                        graphpk )
        else:
            filegraphique = self.toolwidgetmain.lineEdit_csv.text()
        if filegraphique is None or filegraphique == '':
            return None
        filegraphique = self.dbase.completePathOfFile(filegraphique)
        datas=[]
        with open(filegraphique, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in csvreader:
                datas.append([])
                for elem in row :
                    if self.isfloat(elem):
                        datas[-1].append(float(elem))
                    else:
                        datas[-1].append(elem)

        return datas

    def saveGraphinCsv(self,csvpath):
        """Lit le QTableWidget et enregistre son contenu dans un fichier csv
        """
        with open(csvpath, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
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
                csvwriter.writerow(ligne)

    def isfloat(self,txt):
        try:
            float(txt)
            return True 
        except:
            return False


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_graphcsv_tool_ui.ui')
        uic.loadUi(uipath, self)

