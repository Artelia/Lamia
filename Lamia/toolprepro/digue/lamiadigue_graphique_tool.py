# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QComboBox, QDoubleSpinBox, QSpinBox, QHeaderView,
                                 QTableWidgetItem)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QComboBox, QDoubleSpinBox, QSpinBox, QHeaderView,
                                     QTableWidgetItem)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import datetime
import numpy as np
from ...libs import pyqtgraph as pg
pg.setConfigOption('background', 'w')
from collections import OrderedDict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

"""
ne permettre de la renseigner qu en etant une classe fille de leve topo - sinon pas de datecreation
ca fout la merde....

"""


class GraphiqueTool(AbstractInspectionDigueTool):

    LOADFIRST = False
    dbasetablename = 'Graphique'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(GraphiqueTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

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
                                       'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                       'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Profil']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lk_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']}}
        # self.pickTable = None


        # ****************************************************************************************
        #properties ui

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Graphique' : {'linkfield' : 'id_graphique',
                                             'widgets' : {'typegraphique': self.userwdgfield.comboBox_graphtype}},
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
                                                  ('index3', 'Materiau')])
                                      }

            self.userwdgfield.pushButton_addline.clicked.connect(self.addrow)
            self.userwdgfield.pushButton_delline.clicked.connect(self.removerow)
            self.enableTypeComboBox()

            # Tools tab - temporal graph
            self.pyqtgraphwdg = pg.PlotWidget()
            #layout = QtGui.QVBoxLayout()
            #layout.addWidget(self.pyqtgraphwdg)
            self.vb = self.pyqtgraphwdg.getViewBox()
            #self.userwdg.frame_graph.setLayout(layout)
            self.userwdgfield.frame_graph.layout().addWidget(self.pyqtgraphwdg)
            self.plotitem = []

            self.figuretype = plt.figure()
            self.axtype = self.figuretype.add_subplot(111)


            # ****************************************************************************************
            # child widgets
            pass


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def addrow(self):
        introw = self.userwdgfield.tableWidget.currentRow()
        self.userwdgfield.tableWidget.insertRow(introw + 1)
        typetext = self.userwdgfield.comboBox_graphtype.currentText()
        type = self.dbase.getConstraintRawValueFromText(self.dbasetablename,'typegraphique',typetext)
        if type in self.graphspec.keys():
            for i, field in enumerate(self.graphspec[type]):
                graphiquedataelemfields = self.dbase.dbasetables['Graphiquedata']['fields'][field]
                if 'Cst' in graphiquedataelemfields.keys():
                    combobox = QComboBox()
                    itemlist = [elem[0] for elem in graphiquedataelemfields['Cst']]
                    combobox.addItems(itemlist)
                    self.userwdgfield.tableWidget.setCellWidget(introw + 1, i, combobox)
                elif graphiquedataelemfields['PGtype'] == 'NUMERIC':
                    spinbox = QDoubleSpinBox()
                    spinbox.setSingleStep(0.5)
                    spinbox.setRange(-9999, 9999)
                    self.userwdgfield.tableWidget.setCellWidget(introw + 1, i, spinbox)
                elif graphiquedataelemfields['PGtype'] == 'INTEGER':
                    spinbox = QSpinBox()
                    spinbox.setRange(-9999, 9999)
                    self.userwdgfield.tableWidget.setCellWidget(introw + 1, i, spinbox)

        header = self.userwdgfield.tableWidget.horizontalHeader()
        header.setResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        self.enableTypeComboBox()


    def removerow(self):
        introw = self.userwdgfield.tableWidget.currentRow()
        self.userwdgfield.tableWidget.removeRow(introw)

        self.enableTypeComboBox()

        if False and introw != 0 and introw != (self.userwdgfield.tableWidget.rowCount()):
            self.userwdgfield.tableWidget.setItem(introw, 1, QTableWidgetItem(self.userwdgfield.tableWidget.item(introw - 1, 2)))


    def enableTypeComboBox(self):
        if self.userwdgfield.tableWidget.rowCount() == 0:
            self.userwdgfield.comboBox_graphtype.setEnabled(True)
        else:
            self.userwdgfield.comboBox_graphtype.setEnabled(False)



    def postInitFeatureProperties(self, feat):

        self.pyqtgraphwdg.clear()
        """
        if len(self.plotitem)>0:
            for plot in self.plotitem:
                self.pyqtgraphwdg.removeItem(plot[0])
        self.plotitem = []
        """


        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Ressource', 'date', datecreation)
            self.userwdgfield.tableWidget.setRowCount(0)

        if self.currentFeature is not None:

            type = self.currentFeature['typegraphique']
            typetext =  self.dbase.getConstraintTextFromRawValue(self.dbasetablename,'typegraphique',type)
            self.userwdgfield.comboBox_graphtype.setCurrentIndex(self.userwdgfield.comboBox_graphtype.findText(typetext))
            if False:
                sql = "SELECT * FROM Graphiquedata WHERE id_graphique = " + str(self.currentFeature['id_graphique'])
                sql += " ORDER BY id_graphiquedata"
                query = self.dbase.query(sql)

                result = [list(row) for row in query]

            result = self.getGraphData(self.currentFeature['id_graphique'])

            # print(result)

            # print('resgraph', len(query), query)
            self.userwdgfield.tableWidget.setRowCount(0)
            if True:
                graphiquedatafields = self.dbase.dbasetables['Graphiquedata']['fields']

                for i in range(len(result['x'])):
                    self.addrow()
                    lastrow = self.userwdgfield.tableWidget.rowCount() - 1
                    self.userwdgfield.tableWidget.setCurrentCell(lastrow, 0)
                    # print('init',lastrow,elem)
                    for field in self.graphspec[type].keys():
                        order = list(self.graphspec[type].keys()).index(field)
                        if 'Cst' in graphiquedatafields[field].keys():
                            combo = self.userwdgfield.tableWidget.cellWidget(lastrow, order)
                            indexcombo = combo.findText(result[field][i])
                            combo.setCurrentIndex(indexcombo)
                        elif (graphiquedatafields[field]['PGtype'] == 'INT'
                              or graphiquedatafields[field]['PGtype'] == 'NUMERIC'):
                            self.userwdgfield.tableWidget.cellWidget(lastrow, order).setValue(result[field][i])

                    if False:
                        for i, field in enumerate(graphiquedatafields.keys()):
                            if field in self.graphspec[type].keys():
                                order = list(self.graphspec[type].keys()).index(field)
                                if 'Cst' in graphiquedatafields[field].keys():
                                    combo = self.userwdgfield.tableWidget.cellWidget(lastrow, order)
                                    indexcombo = combo.findText(elem[i])
                                    combo.setCurrentIndex(indexcombo)
                                elif (graphiquedatafields[field]['PGtype'] == 'INT'
                                      or graphiquedatafields[field]['PGtype'] == 'NUMERIC'):
                                    self.userwdgfield.tableWidget.cellWidget(lastrow, order).setValue(elem[i])


                        if False:
                            if field in self.graphspec[type].keys():
                                order = list(self.graphspec[type].keys()).index(field)
                                if 'Cst' in graphiquedatafields[field].keys():
                                    combo = self.userwdgfield.tableWidget.cellWidget(lastrow, order)
                                    if elem[i] is None:
                                        valuetoset = ''
                                    else:
                                        valuetoset = elem[i]
                                    indexcombo = combo.findText(
                                        self.dbase.getConstraintTextFromRawValue('Graphiquedata', field, valuetoset))
                                    combo.setCurrentIndex(indexcombo)
                                elif (graphiquedatafields[field]['PGtype'] == 'INT'
                                      or graphiquedatafields[field]['PGtype'] == 'NUMERIC'):
                                    # print('numeric',field,lastrow, order,elem[i])
                                    self.userwdgfield.tableWidget.cellWidget(lastrow, order).setValue(round(elem[i], 2))
            if False:
                if len(result) >0:
                    for elem in result:
                        self.addrow()
                        lastrow = self.userwdgfield.tableWidget.rowCount() - 1
                        self.userwdgfield.tableWidget.setCurrentCell(lastrow,0)
                        # print('init',lastrow,elem)
                        graphiquedatafields = self.dbase.dbasetables['Graphiquedata']['fields']
                        for i, field in enumerate(graphiquedatafields.keys()):
                            if field in self.graphspec[type].keys():
                                order = list(self.graphspec[type].keys()).index(field)
                                if 'Cst' in graphiquedatafields[field].keys():
                                    combo = self.userwdgfield.tableWidget.cellWidget(lastrow,order)
                                    if elem[i] is None:
                                        valuetoset = ''
                                    else:
                                        valuetoset = elem[i]
                                    indexcombo = combo.findText(self.dbase.getConstraintTextFromRawValue('Graphiquedata',field, valuetoset ))
                                    combo.setCurrentIndex(indexcombo)
                                elif (graphiquedatafields[field]['PGtype'] == 'INT'
                                        or graphiquedatafields[field]['PGtype'] == 'NUMERIC'):
                                    # print('numeric',field,lastrow, order,elem[i])
                                    self.userwdgfield.tableWidget.cellWidget(lastrow,order).setValue(round(elem[i],2))


        self.showGraph(type, result)

        self.enableTypeComboBox()


    def getGraphData(self,graphid):
        #print('getGraphData')


        sql = "SELECT * FROM Graphiquedata WHERE id_graphique = " + str(graphid)
        sql += " ORDER BY id_graphiquedata"
        query = self.dbase.query(sql)

        result = [list(row) for row in query]
        graphiquedatafields = self.dbase.dbasetables['Graphiquedata']['fields']
        lenrowresult = len(graphiquedatafields)
        resultfinal = []

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
        # print('showGraph')

        typetext = self.userwdgfield.comboBox_graphtype.currentText()
        type = self.dbase.getConstraintRawValueFromText(self.dbasetablename,'typegraphique',typetext)
        graphspec = self.graphspec[type]
        result={}
        if False:
            for field in self.graphspec[type].keys():
                result[field]=[]
        if False:
            graphiquedatafields = self.dbase.dbasetables['Graphiquedata']['fields']
            for i, field in enumerate(graphiquedatafields):
                result[field] = np.array(graphdata)[:,i]

        result = graphdata

        if False:
            for row in range(self.userwdgfield.tableWidget.rowCount()):
                for i, field in enumerate(self.graphspec[type].keys()):
                    graphiquedatafields = self.dbase.dbasetables['Graphiquedata']['fields']
                    if 'Cst' in graphiquedatafields[field].keys():
                        combo = self.userwdgfield.tableWidget.cellWidget(row, i)
                        result[field].append(combo.currentText())
                    elif (graphiquedatafields[field]['PGtype'] == 'INT'
                          or graphiquedatafields[field]['PGtype'] == 'NUMERIC'):
                        # print('numeric',field,lastrow, order,elem[i])
                        # self.userwdgfield.tableWidget.cellWidget(lastrow, order).setValue(round(elem[i], 2))
                        result[field].append(self.userwdgfield.tableWidget.cellWidget(row, i).value())


        # print(result)

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

            if False:
                #group by typepartie
                # print('typepartie', typepartie)
                nptypepartie = np.array(typepartie)
                indexunique = np.unique(nptypepartie)
                # print(indexunique)
                # print('typepartie',typepartie)
                #uniquepartie = nptypepartie[indexunique]
                #print(uniquepartie)
                #for i in range
                graphtodo = {}
                for typep in indexunique:

                    if typep != u'':
                        # print(typep, type(typep))
                        graphtodo[typep]={'x':[],'y':[]}
                        for i in range(len(Xgraph)):
                            #print(typepartie[i],typep)
                            if typepartie[i] == typep  :
                                graphtodo[typep]['x'].append(Xgraph[i-1])
                                graphtodo[typep]['x'].append(Xgraph[i])
                                graphtodo[typep]['y'].append(Zgraph[i-1])
                                graphtodo[typep]['y'].append(Zgraph[i])

                print('graphtodo', graphtodo)

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



            if False:
                for typep in graphtodo.keys():
                    graphcolor = 'black'
                    graphlinestyle = '-'
                    graphlinewidth = 3.0
                    if 'Vegetalise enherbe' in typep  :
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
                    elif 'Beton' in typep :
                        graphcolor = 'gray'
                    elif 'Pierre maconnees' in typep :
                        graphcolor = 'gray'
                        graphlinestyle = '--'
                    elif 'Roches appareillees' in typep :
                        graphcolor = 'gray'
                        graphlinestyle = '-.'
                    elif 'Abscence de revetement' in typep :
                        graphcolor = 'saddlebrown'

                    self.axtype.plot(graphtodo[typep]['x'], graphtodo[typep]['y'], label=typep, color = graphcolor,
                                     linewidth = graphlinewidth, linestyle = graphlinestyle)

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

    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        sql = "INSERT INTO Ressource (id_objet) VALUES(" + str(idobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idres = self.dbase.getLastRowId('Ressource')

        idgraphique = self.currentFeature.id()

        sql = "UPDATE Graphique SET id_objet = " + str(idobjet) + ",id_ressource = " + str(idres) + " WHERE id_graphique = " + str( idgraphique) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Profil':
                currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                sql = "INSERT INTO Tcobjetressource(id_tcobjet, id_tcressource) VALUES(" +  str(currentparentlinkfield) + ", " +  str(idres) + ");"
                # print('createparent',sql)

                query = self.dbase.query(sql)
                self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):


        idgraphique = self.currentFeature.id()

        sql = "DELETE FROM Graphiquedata WHERE id_graphique = " + str(idgraphique)
        # print(sql)
        self.dbase.query(sql)
        self.dbase.commit()

        self.dbase.vacuum('Graphiquedata')
        self.dbase.commit()

        for row in range(self.userwdgfield.tableWidget.rowCount() ):
            # get values
            typetext = self.userwdgfield.comboBox_graphtype.currentText()
            type = self.dbase.getConstraintRawValueFromText(self.dbasetablename, 'typegraphique', typetext)
            listchamp = ','.join(self.graphspec[type].keys())
            values=[]
            for column, field in enumerate(self.graphspec[type]):
                if self.userwdgfield.tableWidget.cellWidget(row, column) is not None:
                    columnwdg = self.userwdgfield.tableWidget.cellWidget(row, column)
                    if isinstance(columnwdg,QComboBox):
                        value = "'" + self.dbase.getConstraintRawValueFromText('Graphiquedata',
                                                                          field,
                                                                          columnwdg.currentText()) + "'"
                    elif isinstance(columnwdg,QDoubleSpinBox) or isinstance(columnwdg,QSpinBox):
                        value = str(columnwdg.value())
                values.append(value)

            sql = "INSERT INTO Graphiquedata (" + listchamp + ",id_graphique) "
            sql += " VALUES(" + ",".join(values) + "," + str(self.currentFeature['id_graphique']) + ");"
            # print(sql)
            self.dbase.query(sql)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiadigue_graphique_tool_ui.ui')
        uic.loadUi(uipath, self)

