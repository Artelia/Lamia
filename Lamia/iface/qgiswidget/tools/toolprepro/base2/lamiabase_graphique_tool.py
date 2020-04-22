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






class BaseGraphiqueTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'Graphique'
    LOADFIRST = False

    tooltreewidgetCAT = 'Ressources'
    tooltreewidgetSUBCAT = 'Graphique'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), '..', 'base', 'lamiabase_graphique_tool_icon.png')

    PARENTJOIN = {'Profil' : {'colparent': 'id_objet',
                                    'colthistable': 'id_ressource',
                                        'tctable': 'Tcobjetressource',
                                        'tctablecolparent': 'lid_objet',
                                        'tctablecolthistable': 'lid_ressource'}
                }


    def __init__(self, **kwargs):
        super(BaseGraphiqueTool, self).__init__(**kwargs)
        self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111)
        self.mplfigure = FigureCanvas(self.figuretype)


    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Graphique'
        self.dbasetablename = 'Graphique'
        self.visualmode = [1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                           'idsource' : 'id_ressource',
                                       'idtcsource' : 'lid_ressource',
                                           'iddest' : 'id_objet',
                                       'idtcdest' : 'lid_objet',
                                           'desttable' : ['Profil']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lid_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']}}
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), '..', 'base', 'lamiabase_graphique_tool_icon.png')


        # ****************************************************************************************
        #properties ui
    """

    def initMainToolWidget(self):
        # ****************************************************************************************
        #   userui Field

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Graphique' : {'linkfield' : 'id_graphique',
                                                        'widgets' : {'typegraphique': self.toolwidgetmain.comboBox_graphtype}},
                                                'Objet' : {'linkfield' : 'id_objet',
                                                            'widgets' : {}},
                                                'Ressource' : {'linkfield' : 'id_ressource',
                                                            'widgets' : {}}}

        self.graphspec = {'SIM': OrderedDict([('x','X'),
                                                ('y','X')]),
                            'PTR': OrderedDict([('x','X'),
                                                ('y','X'),
                                                ('index1', 'Position'),
                                                ('index2',  'Nature'),
                                                ('index3', 'Materiau'),
                                                ('index4', 'Cote') ])
                                    }

        self.toolwidgetmain.pushButton_addline.clicked.connect(self.addrow)
        self.toolwidgetmain.pushButton_delline.clicked.connect(self.removerow)
        self.enableTypeComboBox()

        if True:
            #self.figuretype = plt.figure()
            #self.axtype = self.figuretype.add_subplot(111)
            #self.mplfigure = FigureCanvas(self.figuretype)
            self.toolwidgetmain.frame_graph.layout().addWidget(self.mplfigure)
            self.toolbar = NavigationToolbar(self.mplfigure, self.toolwidgetmain.frame_graph)
            self.toolwidgetmain.frame_graph.layout().addWidget(self.toolbar)

        if False:
            # Tools tab - temporal graph
            self.pyqtgraphwdg = pg.PlotWidget()
            #layout = QtGui.QVBoxLayout()
            #layout.addWidget(self.pyqtgraphwdg)
            self.vb = self.pyqtgraphwdg.getViewBox()
            #self.userwdg.frame_graph.setLayout(layout)
            self.toolwidgetmain.frame_graph.layout().addWidget(self.pyqtgraphwdg)
            self.plotitem = []



    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass
    """

    def addrow(self):
        introw = self.toolwidgetmain.tableWidget.currentRow()
        self.toolwidgetmain.tableWidget.insertRow(introw + 1)
        if self.currentFeaturePK is None:
            typetext = self.toolwidgetmain.comboBox_graphtype.currentText()
            typegraph = self.dbase.getConstraintRawValueFromText(self.DBASETABLENAME,'typegraphique',typetext)
        else:
            typegraph = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                                    'typegraphique',
                                                    self.currentFeaturePK)
        if typegraph in self.graphspec.keys():
            for i, field in enumerate(self.graphspec[typegraph]):
                graphiquedataelemfields = self.dbase.dbasetables['Graphiquedata']['fields'][field]
                if 'Cst' in graphiquedataelemfields.keys():
                    combobox = QComboBox()
                    itemlist = [elem[0] for elem in graphiquedataelemfields['Cst']]
                    combobox.addItems(itemlist)
                    self.toolwidgetmain.tableWidget.setCellWidget(introw + 1, i, combobox)
                elif graphiquedataelemfields['PGtype'] == 'NUMERIC':
                    spinbox = QDoubleSpinBox()
                    spinbox.setSingleStep(0.5)
                    spinbox.setRange(-9999, 9999)
                    self.toolwidgetmain.tableWidget.setCellWidget(introw + 1, i, spinbox)
                elif graphiquedataelemfields['PGtype'] == 'INTEGER':
                    spinbox = QSpinBox()
                    spinbox.setRange(-9999, 9999)
                    self.toolwidgetmain.tableWidget.setCellWidget(introw + 1, i, spinbox)

        header = self.toolwidgetmain.tableWidget.horizontalHeader()
        header.resizeSections(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        self.enableTypeComboBox()


    def removerow(self):
        introw = self.toolwidgetmain.tableWidget.currentRow()
        self.toolwidgetmain.tableWidget.removeRow(introw)

        self.enableTypeComboBox()

        if False and introw != 0 and introw != (self.toolwidgetmain.tableWidget.rowCount()):
            self.toolwidgetmain.tableWidget.setItem(introw, 1, QTableWidgetItem(self.toolwidgetmain.tableWidget.item(introw - 1, 2)))


    def enableTypeComboBox(self):
        if self.toolwidgetmain.tableWidget.rowCount() == 0:
            self.toolwidgetmain.comboBox_graphtype.setEnabled(True)
        else:
            self.toolwidgetmain.comboBox_graphtype.setEnabled(False)



    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):

        if False:
            self.pyqtgraphwdg.clear()
        """
        if len(self.plotitem)>0:
            for plot in self.plotitem:
                self.pyqtgraphwdg.removeItem(plot[0])
        self.plotitem = []
        """


        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict({'datetimeressource' : datecreation},checkifinforgottenfield=False)

            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            ##self.initFeatureProperties(feat, 'Ressource', 'date', datecreation)
            #self.formutils.applyResultDict({'date': datecreation},,checkifinforgottenfield=False)
            self.toolwidgetmain.tableWidget.setRowCount(0)

        else :

            #type = self.currentFeature['typegraphique']
            grapthtype = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                                    'typegraphique',
                                                    self.currentFeaturePK)
            typetext =  self.dbase.getConstraintTextFromRawValue(self.DBASETABLENAME,'typegraphique',grapthtype)
            self.toolwidgetmain.comboBox_graphtype.setCurrentIndex(self.toolwidgetmain.comboBox_graphtype.findText(typetext))

            result = self.getGraphData(self.currentFeaturePK)

            self.toolwidgetmain.tableWidget.setRowCount(0)
            if result is not None :
                graphiquedatafields = self.dbase.dbasetables['Graphiquedata']['fields']

                for i in range(len(result['x'])):
                    self.addrow()
                    lastrow = self.toolwidgetmain.tableWidget.rowCount() - 1
                    self.toolwidgetmain.tableWidget.setCurrentCell(lastrow, 0)
                    # print('init',lastrow,elem)
                    for field in self.graphspec[grapthtype].keys():
                        order = list(self.graphspec[grapthtype].keys()).index(field)
                        if 'Cst' in graphiquedatafields[field].keys():
                            combo = self.toolwidgetmain.tableWidget.cellWidget(lastrow, order)
                            indexcombo = combo.findText(result[field][i])
                            combo.setCurrentIndex(indexcombo)
                        elif (graphiquedatafields[field]['PGtype'] == 'INT'
                              or graphiquedatafields[field]['PGtype'] == 'NUMERIC'):
                            self.toolwidgetmain.tableWidget.cellWidget(lastrow, order).setValue(result[field][i])

                self.showGraph(grapthtype, result)

        self.enableTypeComboBox()


    def getGraphData(self,graphpk):
        #print('getGraphData')


        sql = "SELECT * FROM Graphiquedata WHERE lpk_graphique = " + str(graphpk)
        sql += " ORDER BY id_graphiquedata"
        query = self.dbase.query(sql)

        if not query:
            return

        result = [list(row) for row in query]
        graphiquedatafields = self.dbase.dbasetables['Graphiquedata']['fields']
        lenrowresult = len(graphiquedatafields)
        resultfinal = []

        resultnp = None

        if len(result) > 0:
            for elem in result:
                resultfinal.append([None]*lenrowresult)
                #print(resultfinal)

                for i, field in enumerate(graphiquedatafields.keys()):
                    #if field in self.graphspec[type].keys():
                        #order = list(self.graphspec[type].keys()).index(field)
                    if 'Cst' in graphiquedatafields[field].keys():
                        if elem[i] is None:
                            valuetoset = ''
                        else:
                            valuetoset = elem[i]
                        resultfinal[-1][i] = self.dbase.getConstraintTextFromRawValue('Graphiquedata', field, valuetoset)
                    elif (graphiquedatafields[field]['PGtype'] == 'INT'
                            or graphiquedatafields[field]['PGtype'] == 'NUMERIC'):
                        if elem[i] is not None:
                            resultfinal[-1][i] = round(elem[i], 2)
                        else:
                            resultfinal[-1][i] = None

            resultnp = {}
            graphiquedatafields = self.dbase.dbasetables['Graphiquedata']['fields']
            for i, field in enumerate(graphiquedatafields):
                resultnp[field] = np.array(resultfinal)[:,i]

        #print(resultfinal)
        return resultnp




    def showGraph(self,type, graphdata):

        #typetext = self.toolwidgetmain.comboBox_graphtype.currentText()
        ##type = self.dbase.getConstraintRawValueFromText(self.DBASETABLENAME,'typegraphique',typetext)
        #typegraph = self.dbase.getValuesFromPk(self.DBASETABLENAME,
        #                                            'typegraphique',
        #                                            self.currentFeaturePK)
        #graphspec = self.graphspec[type]
        result={}

        result = graphdata

        if True:
            Xgraph = [0.0]
            Zgraph = [0.0]
            grapthtype = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                        'typegraphique',
                                        self.currentFeaturePK)
            
            if grapthtype in ['SIM', 'PTR']:
                for i in range(len(result['x'])):
                    Xgraph.append(Xgraph[-1] + float(result['x'][i]))
                    Zgraph.append(Zgraph[-1] + float(result['y'][i]))

            self.axtype.clear()
            self.axtype.plot(Xgraph, Zgraph)
            self.axtype.grid()
            self.figuretype.canvas.draw()


        if False:
            if self.currentFeature['typegraphique'] == 'SIM':
                self.plotitem.append([self.pyqtgraphwdg.plot(result['x'], result['y'], pen=pg.mkPen('b', width=2)), result['x'], result['y']])
                self.pyqtgraphwdg.autoRange()

            if self.currentFeature['typegraphique'] == 'PTR':
                Xgraph = [0.0]
                Zgraph = [0.0]

                for i in range(len(result['x'])):
                    Xgraph.append(Xgraph[-1] + float(result['x'][i]))
                    Zgraph.append(Zgraph[-1] + float(result['y'][i]))

                self.plotitem.append([self.pyqtgraphwdg.plot(Xgraph, Zgraph, pen=pg.mkPen('b', width=2)), Xgraph, Zgraph])
                self.pyqtgraphwdg.autoRange()
                # '<div style="text-align: center"><span style="color: #FFF;">This is the</span><br><span style="color: #FF0; font-size: 16pt;">PEAK</span></div>'
                for i in range(len(Xgraph) -1):
                    #txtitem =  pg.TextItem('Test')
                    # print(i,result['index1'][i])
                    # txtitem = pg.TextItem(result['index1'][i],anchor = (Xgraph[i],Zgraph[i]))

                    html = '<div style="text-align: center"><span style="color:  #000000; font-size: 12pt;">' + result['index2'][i]
                    html +=      '</span><br><span style="color:  #000000; font-size: 12pt;">' + result['index3'][i] + '</span></div>'
                    #txtitem = pg.TextItem(result['index2'][i] + '\n' + result['index3'][i])
                    txtitem = pg.TextItem()
                    txtitem.setHtml(html)
                    txtitem.setPos(Xgraph[i],Zgraph[i])
                    #txtitem.setTextWidth(10)
                    #txtitem.setHtml('<div style="text-align: center"><span style="color:  #000000;">This is the</span><br><span style="color:  #000000; font-size: 16pt;">PEAK</span></div>')
                    self.pyqtgraphwdg.addItem( txtitem)



    def exportgraph(self,typegrap, graphdata,exportfile,width,height):
        #print(type, graphdata)
        #resfile = None
        #return resfile

        if typegrap == 'PTR':
            Xgraph = [0.0]
            Zgraph = [0.0]
            #typepartie = ['']
            typepartie = []
            for i in range(len(graphdata['x'])):
                Xgraph.append(Xgraph[-1] + float(graphdata['x'][i]))
                Zgraph.append(Zgraph[-1] + float(graphdata['y'][i]))
                typepartie.append(graphdata['index2'][i] + ' - ' + graphdata['index3'][i])


            #print(Xgraph,Zgraph)
            self.axtype.cla()
            self.figuretype.set_size_inches(width / 25.4, height / 25.4)

            # print('res',Xgraph, Zgraph, typepartie )

            if True:
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

                    # print('res1',[Xgraph[i],Xgraph[i+1]], [Zgraph[i], Zgraph[i+1]], typep )

                    if typep not in label:
                        label.append(typep)
                    else:
                        typep = None

                    self.axtype.plot([Xgraph[i],Xgraph[i+1]], [Zgraph[i], Zgraph[i+1]], label=typep, color=graphcolor,
                                     linewidth=graphlinewidth, linestyle=graphlinestyle)




            #legend = self.axtype.legend(bbox_to_anchor=(1.04, 0), loc="lower left", borderaxespad=0, prop={'size': 8}, shadow=False)
            #legend = self.axtype.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,prop={'size': 8})
            legend = self.axtype.legend(bbox_to_anchor=(0., 1.), loc="lower left", bbox_transform=self.figuretype.transFigure, prop={'size': 8})
            self.axtype.annotate('TERRE', xy=(0.05, 1.05), xycoords='axes fraction',horizontalalignment='left')
            self.axtype.annotate('EAU', xy=(0.95, 1.05), xycoords='axes fraction',horizontalalignment='right')

            #plt.ylabel('Z (m)', fontsize=8)
            self.axtype.set_ylabel('Z (m)', fontsize=8)
            #self.figuretype.set_size_inches(width / 25.4, height / 25.4)
            self.figuretype.savefig(exportfile, bbox_inches='tight', dpi=150)


        #return resfile

    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:

            # lastrevision = self.dbase.maxrevision
            datecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')

        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sql = "INSERT INTO Ressource (id_ressource, lpk_objet) "
        sql += "VALUES(" + str(lastressourceid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pkres = self.dbase.getLastRowId('Ressource')

        pkgraph = self.currentFeaturePK
        lastidgraph = self.dbase.getLastId('Graphique') + 1
        sql = "UPDATE Graphique SET id_graphique = " + str(lastidgraph)  + ","
        sql += "lpk_ressource = " + str(pkres)
        sql += " WHERE pk_graphique = " + str(pkgraph) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Profil':

                # get parent id_objet
                sql = " SELECT id_objet FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
                sql += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
                currentparentlinkfield = self.dbase.query(sql)[0][0]

                # currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                sql = "INSERT INTO Tcobjetressource(id_tcobjet,lpk_revision_begin, id_tcressource) "
                sql += " VALUES(" + str(currentparentlinkfield) + ", " + str(self.dbase.maxrevision) + ',' + str(lastressourceid) + ");"
                query = self.dbase.query(sql)
                self.dbase.commit()

                """

    def postSaveFeature(self, savedfeaturepk=None):


        #idgraphique = self.currentFeature.id()
        pkgraphique = savedfeaturepk

        sql = "DELETE FROM Graphiquedata WHERE lpk_graphique = " + str(pkgraphique)
        self.dbase.query(sql)

        if False:
            self.dbase.vacuum('Graphiquedata')
            self.dbase.commit()

        for i, row in enumerate(range(self.toolwidgetmain.tableWidget.rowCount() )):
            # get values
            typetext = self.toolwidgetmain.comboBox_graphtype.currentText()
            graphtype = self.dbase.getConstraintRawValueFromText(self.DBASETABLENAME, 'typegraphique', typetext)
            listchamp = ','.join(self.graphspec[graphtype].keys())
            values=[]
            for column, field in enumerate(self.graphspec[graphtype]):
                if self.toolwidgetmain.tableWidget.cellWidget(row, column) is not None:
                    columnwdg = self.toolwidgetmain.tableWidget.cellWidget(row, column)
                    if isinstance(columnwdg,QComboBox):
                        value = "'" + self.dbase.getConstraintRawValueFromText('Graphiquedata',
                                                                          field,
                                                                          columnwdg.currentText()) + "'"
                    elif isinstance(columnwdg,QDoubleSpinBox) or isinstance(columnwdg,QSpinBox):
                        value = str(columnwdg.value())
                        if value is None:
                            value = '0.0'
                    else:
                        value = 'NULL'
                values.append(value)

            sql = "INSERT INTO Graphiquedata (" + listchamp + ",lpk_graphique, id_graphiquedata) "
            sql += " VALUES(" + ",".join(values) + "," + str(pkgraphique) + ',' +  str(i +1) + ");"
            self.dbase.query(sql)




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_graphique_tool_ui.ui')
        uic.loadUi(uipath, self)

