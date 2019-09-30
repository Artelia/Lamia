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


# -*- coding: utf-8 -*-

import qgis
import os
#from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal
import logging, sys
import numpy as np
from collections import OrderedDict

from .importtools.InspectionDigue_Import import ImportObjetDialog

try:
    from qgis.PyQt.QtGui import (QInputDialog,QTableWidgetItem,QComboBox,QAction,QProgressBar,QApplication,QWidget,QToolButton,
                                 QDialog, QGridLayout)
except ImportError:
    from qgis.PyQt.QtWidgets import (QInputDialog,QTableWidgetItem,QComboBox,QAction,QProgressBar,QApplication,QWidget,QToolButton,
                                     QDialog, QGridLayout)

from ...libs.pyqtgraph.flowchart import Flowchart, Node
from ...libs.pyqtgraph.flowchart.library.common import CtrlNode
# import ...libs.pyqtgraph.flowchart.library as fclib
from ...libs.pyqtgraph.flowchart import library as fclib
from ...libs.pyqtgraph.flowchart.library.Data import EvalNode
from ...libs.pyqtgraph import configfile as configfile

from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool


class ImportTool(AbstractLamiaTool):
    TOOLNAME = 'Importtools'
    DBASES = ['digue', 'base_digue', 'base2_digue', 'base2_parking']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(ImportTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
        self.postInit()
        self.dialog = QDialog()
        layout = QGridLayout()
        self.dialog.setLayout(layout)

        self.library = fclib.LIBRARY.copy()  # start with the default node set
        self.library.nodeList = OrderedDict()
        self.library.nodeTree = OrderedDict()
        self.library.addNodeType(EvalNode, [()])
        self.library.addNodeType(AttributeReaderNode, [()])
        # Add the unsharp mask node to two locations in the menu to demonstrate
        # that we can create arbitrary menu structures
        # self.library.addNodeType(UnsharpMaskNode, [('Image',),('Submenu_test', 'submenu2', 'submenu3')])
        self.qfiledlg = self.windowdialog.qfiledlg




    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Import/export'
        self.NAME = 'Import'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)

        self.iconpath = os.path.join(os.path.dirname(__file__), 'Lamia_import_tool_icon.png')
        #self.qtreewidgetfields = ['libelle']

        # ****************************************************************************************
        # properties ui
        self.groupBox_elements.setParent(None)
        self.frame_editing.setParent(None)




    def postInit(self):
        pass

    def initFieldUI(self):
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            self.userwdgfield.toolButton_update.clicked.connect(self.updateTable)

            items = [ "Infralineaire", 'Noeud', 'Equipement', 'Photo']
            self.userwdgfield.comboBox_typeimport.addItems(items)

            # methode 1
            self.userwdgfield.pushButton_import.clicked.connect(self.showTable)
            self.userwdgfield.pushButton_importer.clicked.connect(self.work)

            #flowchart
            self.userwdgfield.pushButton_flowchart.clicked.connect(self.showFlowChart)



            self.dialogui = DialogUI()



    def postOnActivation(self):
        self.updateTable()

    def updateTable(self):

        self.userwdgfield.comboBox_tableimport.clear()

        if self.dbase.qgsiface is not None:
            if sys.version_info.major == 2:
                layers = self.dbase.qgsiface.legendInterface().layers()
            elif sys.version_info.major == 3:
                layers = [tree_layer.layer() for tree_layer in qgis.core.QgsProject.instance().layerTreeRoot().findLayers()]
            layqgis=[]
            for tablename in self.dbase.dbasetables.keys():
                layqgis.append(self.dbase.dbasetables[tablename]['layerqgis'])

            for lay in layers:
                if not lay in layqgis:
                    self.userwdgfield.comboBox_tableimport.addItems([lay.name()])


    def fcSaveAs(self):
        if self.fc.widget().currentFileName is None:

            startdir = os.path.join(self.dbase.dbaseressourcesdirectory,'importtools')
            conffile = self.qfiledlg.getSaveFileName(self,
                                                       'Lamia - import conf',
                                                       startdir,
                                                       'PDF (*.fc)')
            if conffile:
                if isinstance(conffile, tuple):  # qt5
                    conffile = conffile[0]
                #self.userwdgfield.lineEdit_nom.setText(conffile)
            #self.fc.widget().saveAsClicked()
        else:
            conffile = self.fc.widget().currentFileName

        conffile = unicode(conffile)
        configfile.writeConfigFile(self.fc.saveState(), conffile)
        self.fc.sigFileSaved.emit(conffile)

    def fcLoad(self):
        startdir = os.path.join(self.dbase.dbaseressourcesdirectory, 'importtools')
        fileName, extension = self.windowdialog.qfiledlg.getOpenFileNameAndFilter(None,
                                                                              'Choose the file',
                                                                              startdir,
                                                                             'flowChart (*.fc)', '')
        if fileName:
            fileName = unicode(fileName)
            state = configfile.readConfigFile(fileName)
            self.fc.setLibrary(self.library)
            self.fc.sigChartChanged.connect(self.fcNodeAdded)
            self.restoreState(state, clear=True)
            self.fc.viewBox.autoRange()
            # self.emit(QtCore.SIGNAL('fileLoaded'), fileName)
            self.fc.sigFileLoaded.emit(fileName)

    def restoreState(self, state, clear=False):
        #self.blockSignals(True)
        try:
            if clear:
                self.fc.clear()
            Node.restoreState(self.fc, state)
            nodes = state['nodes']
            nodes.sort(key=lambda a: a['pos'][0])
            for n in nodes:
                if n['name'] in self.fc._nodes:
                    # self._nodes[n['name']].graphicsItem().moveBy(*n['pos'])
                    self.fc._nodes[n['name']].restoreState(n['state'])
                    continue
                try:
                    node = self.fc.createNode(n['class'], name=n['name'])
                    node.restoreState(n['state'])
                except:
                    pass
                    #printExc("Error creating node %s: (continuing anyway)" % n['name'])
                # node.graphicsItem().moveBy(*n['pos'])

            self.fc.inputNode.restoreState(state.get('inputNode', {}))
            self.fc.outputNode.restoreState(state.get('outputNode', {}))

            # self.restoreTerminals(state['terminals'])
            connectionstoloadafter = []
            for n1, t1, n2, t2 in state['connects']:
                if n1 in ['Output', 'Input'] or n2 in ['Output', 'Input'] :
                    self.fc.connectTerminals(self.fc._nodes[n1][t1], self.fc._nodes[n2][t2])
                else:
                    connectionstoloadafter.append([n1, t1, n2, t2 ])
            for n1, t1, n2, t2 in connectionstoloadafter:
                self.fc.connectTerminals(self.fc._nodes[n1][t1], self.fc._nodes[n2][t2])

                """
                try:
                    print("*** connecting terminals %s.%s - %s.%s:" % (n1, t1, n2, t2))
                    self.fc.connectTerminals(self.fc._nodes[n1][t1], self.fc._nodes[n2][t2])
                except:
                    print(self.fc._nodes[n1].terminals)
                    print(self.fc._nodes[n2].terminals)
                    print("Error connecting terminals %s.%s - %s.%s:" % (n1, t1, n2, t2))
                    #printExc("Error connecting terminals %s.%s - %s.%s:" % (n1, t1, n2, t2))
                """

        finally:
            pass
            #self.fc.blockSignals(False)

        self.fc.sigChartLoaded.emit()
        self.fc.outputChanged()
        self.fc.sigStateChanged.emit()
        # self.fc.sigOutputChanged.emit()




    def showFlowChart(self):
        debug = False

        # get dest fields
        item = self.userwdgfield.comboBox_typeimport.currentText()
        parentstable = [item] + self.dbase.getParentTable(item)
        if debug: logging.getLogger('Lamia').debug('start %s', str(parentstable))
        fields = self.getAllFields(parentstable)
        if debug: logging.getLogger('Lamia').debug('fields %s', str(fields))

        #get fromfields
        fromlayerfields = self.getFromFields()
        if debug: logging.getLogger('Lamia').debug('fromfields %s', str(fromlayerfields))


        #get from valuues
        fromattributes = []
        for fet in self.currentlayer.getFeatures():
            fromattributes.append( np.array(fet.attributes()))
        fromattributesnp = np.array(fromattributes)
        if debug: logging.getLogger('Lamia').debug('npaatributes %s', str(fromattributesnp))


        # initflowchart
        terminalindict = OrderedDict()
        for field in fields:
            terminalindict[field] = {'io': 'out'}
        for field in fromlayerfields:
            terminalindict[field] = {'io': 'in'}

        self.fc = Flowchart(terminals=terminalindict)
        self.fc.setLibrary(self.library)

        #print(len(fromlayerfields), len(fromattributesnp[:,1]))
        for i, field in enumerate(fromlayerfields):
            if field != '':
                stringtoeval = 'self.fc.setInput(' + field + '=list(fromattributesnp[:,' + str(i) + ']))'
                eval(stringtoeval)

        self.fc.outputNode.graphicsItem().bounds = QtCore.QRectF(0, 0, 200, len(fields)*15)
        self.fc.outputNode .graphicsItem().updateTerminals()
        self.fc.outputNode .graphicsItem().update()

        self.fc.inputNode  .graphicsItem().bounds = QtCore.QRectF(0, 0, 200, len(fromlayerfields)*15)
        self.fc.inputNode  .graphicsItem().updateTerminals()
        self.fc.inputNode  .graphicsItem().update()

        self.fc.sigChartChanged.connect(self.fcNodeAdded)

        if True:
            self.fc.widget().ui.loadBtn.clicked.disconnect()
            self.fc.widget().ui.saveBtn.clicked.disconnect()
            self.fc.widget().ui.saveAsBtn.clicked.disconnect()

            self.fc.widget().ui.saveAsBtn.clicked.connect(self.fcSaveAs)
            self.fc.widget().ui.loadBtn.clicked.connect(self.fcLoad)


        if self.dbase.qgsiface is None:
            fNode = self.fc.createNode('AttributeReaderNode', pos=(0, 10))
            fNode2 = self.fc.createNode('AttributeReaderNode', pos=(0, 20))
            #fNode.setLayers(self.currentlayer)



        if False:
            self.fc = Flowchart(terminals={
                'dataIn': {'io': 'in'},
                'dataOut': {'io': 'out'}
            })
        wdg = self.fc.widget()
        wdg1 = self.fc.widget().chartWidget
        wdg1.selDock.setVisible(False)
        self.dialog.layout().addWidget(wdg, 0, 0, 2, 1)
        self.dialog.layout().addWidget(wdg1, 1, 1, 1, 2)


        self.dialog.exec_()
        output = self.fc.output()
        # print(output)

    def fcNodeAdded(self,flowchart, action, node):
        if node.nodeName == 'AttributeReaderNode':
            node.setLayers(self.currentlayer)
            node.setDbase(self.dbase)



    def getAllFields(self, tables):
        result=[]
        for tablename in tables:
            if tablename in self.dbase.dbasetables.keys():
                dbasetable = self.dbase.dbasetables[tablename]
                for field in dbasetable['fields'].keys():
                    result.append(tablename + '.' + field)
        return result



    def getFromFields(self):
        self.defineCurrentLayer()
        currentlayerfields = self.currentlayer .fields()
        currentlayerfieldsname = [field.name() for field in currentlayerfields]
        return currentlayerfieldsname



    def defineCurrentLayer(self):
        item = self.userwdgfield.comboBox_typeimport.currentText()

        if self.dbase.qgsiface is not None:
            self.currentlayer = None

            if sys.version_info.major == 2:
                layers = self.dbase.qgsiface.legendInterface().layers()
            elif sys.version_info.major == 3:
                layers = [tree_layer.layer() for tree_layer in qgis.core.QgsProject.instance().layerTreeRoot().findLayers()]


            # if not self.dbase.standalone:
            for lay in layers:
                if self.userwdgfield.comboBox_tableimport.currentText() == lay.name():
                    self.currentlayer = lay
                    break

            if self.currentlayer  is None:
                return
        else:  # debug outside qgis
            pass
            if False:
                layerpath = os.path.join(os.path.dirname(__file__), '..','..','..','test','importtool','testshape.shp')
                self.currentlayer = qgis.core.QgsVectorLayer(layerpath, 'test', 'ogr')
            # currentlayerfieldsname = ['', 'ALTINGF', 'typ']



    def showTable(self):
        self.defineCurrentLayer()

        if False:
            item = self.userwdgfield.comboBox_typeimport.currentText()
            self.currentlayer = None
            if self.dbase.qgsiface is not None:
                # if not self.dbase.standalone:
                if sys.version_info.major == 2:
                    layers = self.dbase.qgsiface.legendInterface().layers()
                elif sys.version_info.major == 3:
                    layers = [tree_layer.layer() for tree_layer in qgis.core.QgsProject.instance().layerTreeRoot().findLayers()]


                for lay in layers:
                    if self.userwdgfield.comboBox_tableimport.currentText() == lay.name():
                        self.currentlayer = lay
                        break


                if self.currentlayer  is None:
                    return
            else:  # debug outside qgis
                layerpath = os.path.join(os.path.dirname(__file__), '..','..','..','test','importtool','testshape.shp')
                self.currentlayer = qgis.core.QgsVectorLayer(layerpath, 'test', 'ogr')
                # currentlayerfieldsname = ['', 'ALTINGF', 'typ']

        currentlayerfields = self.currentlayer.fields()
        currentlayerfieldsname = [''] + [field.name() for field in currentlayerfields]
        # combofield = QComboBox([''] + currentlayerfieldsname)

        item = self.userwdgfield.comboBox_typeimport.currentText()
        if item == "Points topo":
            # print('ok')
            templinkuserwgd = self.dbase.dbasetables['Topographie']['widget'][0].propertieswdgPOINTTOPO.linkuserwdg
        if item == "Infralineaire":
            templinkuserwgd = self.dbase.dbasetables['Infralineaire']['widget'][0].linkuserwdg
        if item == "Desordre":
            templinkuserwgd = self.dbase.dbasetables['Desordre']['widget'][0].linkuserwdg
        if item == "Observation":
            templinkuserwgd = self.dbase.dbasetables['Observation']['widget'][0].linkuserwdg
        if item == "Noeud":
            templinkuserwgd = self.dbase.dbasetables['Noeud']['widget'][0].linkuserwdg
        if item == "Equipement":
            templinkuserwgd = self.dbase.dbasetables['Equipement']['widget'][0].linkuserwdg
        if item == "Travaux":
            templinkuserwgd = self.dbase.dbasetables['Travaux']['widget'][0].linkuserwdg
        if item == "Environnement":
            templinkuserwgd = self.dbase.dbasetables['Environnement']['widget'][0].linkuserwdg
        if item == "Photos":
            templinkuserwgd = self.dbase.dbasetables['Photos']['widget'][0].linkuserwdg

        self.userwdgfield.tableWidget.setRowCount(0)
        self.userwdgfield.tableWidget.setColumnCount(3)
        for tablename in templinkuserwgd:
            if tablename in self.dbase.dbasetables.keys():
                dbasetable = self.dbase.dbasetables[tablename]
                for field in dbasetable['fields'].keys():
                    # print(field)
                    rowPosition = self.userwdgfield.tableWidget.rowCount()
                    self.userwdgfield.tableWidget.insertRow(rowPosition)
                    itemfield = QTableWidgetItem(tablename + '.' + field)
                    itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.userwdgfield.tableWidget.setItem(rowPosition, 0, itemfield)
                    # item.setFlags()
                    #if field[0:2] != 'id' and field[0:2] != 'pk':
                    if field.split('_')[0] not in ['pk','lpk']:
                        combofield = QComboBox()
                        combofield.addItems(currentlayerfieldsname)
                        self.userwdgfield.tableWidget.setCellWidget(rowPosition, 1, combofield)

                        pushbutton = QToolButton()
                        pushbutton.setText('...')
                        pushbutton.setObjectName(tablename + '.' + field)
                        self.userwdgfield.tableWidget.setCellWidget(rowPosition, 2, pushbutton)
                        pushbutton.clicked.connect(self.editFields)

                    else:
                        itemfield = QTableWidgetItem('')
                        self.userwdgfield.tableWidget.setItem(rowPosition, 1, itemfield)

        #self.importobjetdialog.exec_()
        #tableview = self.importobjetdialog.dialogIsFinished()
        if False:
            if tableview is not None:
                result = []
                for row in range(self.userwdgfield.tableWidget.rowCount()):
                    if self.userwdgfield.tableWidget.cellWidget(row, 1) is not None:
                        result.append([self.userwdgfield.tableWidget.item(row, 0).text(),
                                       self.userwdgfield.tableWidget.cellWidget(row, 1).currentText()])
                    else:
                        result.append([self.userwdgfield.tableWidget.item(row, 0).text(),
                                       self.userwdgfield.tableWidget.item(row, 1).text()])

                self.work(result)


    def editFields(self):
        pushbuttonsender = self.sender()
        pushbuttonname = pushbuttonsender.objectName()
        # print(pushbuttonname)

        self.dialogui.tableWidget_from.clear()
        self.dialogui.tableWidget_to.clear()



        #fill tableWidget_from in dialog
        for  row in range(self.userwdgfield.tableWidget.rowCount()):
            # print('cell',self.userwdgfield.tableWidget.cellWidget(row, 2))
            if self.userwdgfield.tableWidget.cellWidget(row, 2) == pushbuttonsender:
                layerfromfield = self.userwdgfield.tableWidget.cellWidget(row, 1).currentText()
                layerfromfieldindex = self.userwdgfield.tableWidget.cellWidget(row, 1).currentIndex() -1
                # print(layerfromfield)
                break
        uniquevalues = self.currentlayer.uniqueValues(layerfromfieldindex)
        # print('uniquevalues',uniquevalues)
        # print([type(uniquevalue) for uniquevalue in uniquevalues])
        nullinlist=False
        for uniquevalue in uniquevalues:
            if self.dbase.isAttributeNull(uniquevalue):
                nullinlist = True
        if not nullinlist:
            uniquevalues.insert(0, 'NULL')

        self.dialogui.tableWidget_from.setRowCount(0)
        self.dialogui.tableWidget_from.setColumnCount(1)
        self.dialogui.tableWidget_from.horizontalHeader().setStretchLastSection(True)
        for uniquevalue in uniquevalues:
            # print(field)
            rowPosition = self.dialogui.tableWidget_from.rowCount()
            self.dialogui.tableWidget_from.insertRow(rowPosition)
            itemfield = QTableWidgetItem(str(uniquevalue))
            itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.dialogui.tableWidget_from.setItem(rowPosition, 0, itemfield)

        # fill tableWidget_to in dialog
        table, field = pushbuttonname.split('.')
        self.dialogui.tableWidget_to.setRowCount(0)
        self.dialogui.tableWidget_to.setColumnCount(1)
        self.dialogui.tableWidget_to.horizontalHeader().setStretchLastSection(True)

        if 'Cst' in self.dbase.dbasetables[table]['fields'][field].keys():
            constraints = self.dbase.dbasetables[table]['fields'][field]['Cst']
            for elem in constraints:
                rowPosition = self.dialogui.tableWidget_to.rowCount()
                self.dialogui.tableWidget_to.insertRow(rowPosition)
                itemfield = QTableWidgetItem(str(elem[0]))
                itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.dialogui.tableWidget_to.setItem(rowPosition, 0, itemfield)



        self.dialogui.exec_()
        res = self.dialogui.dialogIsFinished()





    def work(self,layer=None,linktable=None):
        """

        :param linktable: une liste qui correspond au tableau du dialog :
                         [...[colonne1;colonne2]...]
        :param layer:  pour le debug - possibilite de passer un layer autre
        :return:
        """
        debug = False


        self.results = []
        if linktable is None:
            for row in range(self.userwdgfield.tableWidget.rowCount()):
                if self.userwdgfield.tableWidget.cellWidget(row, 1) is not None:
                    self.results.append([self.userwdgfield.tableWidget.item(row, 0).text(),
                                   self.userwdgfield.tableWidget.cellWidget(row, 1).currentText()])
                else:
                    self.results.append([self.userwdgfield.tableWidget.item(row, 0).text(),
                                   self.userwdgfield.tableWidget.item(row, 1).text()])
        else:
            self.results = linktable

        if debug: logging.getLogger('Lamia').debug('start %s', str(self.results))

        self.importtable = self.userwdgfield.comboBox_typeimport.currentText()

        tablestemp = [result[0].split('.')[0] for result in self.results]

        # print(tables)

        # print(self.results)



        uniquetables = list(set(tablestemp))
        tables = [result[0].split('.')[0] for result in self.results]
        fields = [result[0].split('.')[1] for result in self.results]
        tablefield = [result[0] for result in self.results]
        values = [result[1] for result in self.results]

        if debug: logging.getLogger('Lamia').debug('start %s', str(self.importtable))
        if debug: logging.getLogger('Lamia').debug('tables %s', str(tables))
        if debug: logging.getLogger('Lamia').debug('fields %s', str(fields))

        if layer is None or isinstance(layer, bool):   # come from qqis app
            # layer = self.dbase.qgsiface.activeLayer()
            layer = self.currentlayer
        else:
            layer = layer

            # qgis.core.QgsVectorLayer('C://001_travail_BM//testtopo//toposijalag1.shp', 'test', "ogr")
        progress = self.initProgressBar(len([fet for fet in layer.getFeatures()]))
        layerfromfieldsname = [field.name() for field in layer.fields()]
        #print('layerfromfieldsname',layerfromfieldsname)
        if sys.version_info.major == 2:
            self.xform = qgis.core.QgsCoordinateTransform(layer.crs(), self.dbase.qgiscrs)
        elif sys.version_info.major == 3:
            self.xform = qgis.core.QgsCoordinateTransform(layer.crs(), self.dbase.qgiscrs,qgis.core.QgsProject.instance())

        if len(layer.selectedFeatures()) == 0:
            feats  = layer.getFeatures()
        else:
            feats = layer.selectedFeatures()

        if debug: logging.getLogger('Lamia').debug('selected feat %s', [fet.id() for fet in feats])


        # cas des couches enfant de descriptionsystem
        if 'Objet' in tables and 'Descriptionsystem' in uniquetables:
            if debug: logging.getLogger('Lamia').debug('Descriptionsystem')
            for compt, layerfeat in enumerate(layer.getFeatures()):

                if debug: logging.getLogger('Lamia').debug('feat %s', layerfeat.attributes())
                self.setLoadingProgressBar(progress, compt)
                #create objet
                if False:
                    lastrevision = self.dbase.maxrevision
                    datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
                    lastobjetid = self.dbase.getLastId('Objet') + 1
                    sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
                    sql += "VALUES(" + str(lastobjetid) + "," + str(lastrevision) + ",'" + datecreation + "');"
                    query = self.dbase.query(sql)
                    #self.dbase.commit()
                    pkobjet = self.dbase.getLastRowId('Objet')
                pkobjet = self.dbase.createNewObjet()

                for i, table in enumerate(tables):
                    if table == 'Objet' and values[i] != '':
                        #sql = "UPDATE Objet SET " + fields[i] + " = " + str(layerfeat[values[i]])
                        sql = "UPDATE Objet SET " + fields[i] + " = " + self.convertDataType(table,fields[i], layerfeat[values[i]])
                        sql += " WHERE pk_objet = " + str(pkobjet)

                        query = self.dbase.query(sql, docommit=False)
                self.dbase.commit()

                lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
                if False:
                    sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, id_revisionbegin, id_objet) "
                    sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(lastrevision) + "," + str(lastobjetid) + ");"
                sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet) "
                sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(pkobjet) + ");"

                query = self.dbase.query(sql)
                #self.dbase.commit()
                pkdessys= self.dbase.getLastRowId('Descriptionsystem')

                for i, table in enumerate(tables):
                    if table == 'Descriptionsystem' and values[i] != '':
                        #sql = "UPDATE Descriptionsystem SET " + fields[i] + " = " + str(layerfeat[values[i]])
                        sql = "UPDATE Descriptionsystem SET " + fields[i] + " = " + self.convertDataType(table,fields[i], layerfeat[values[i]])
                        sql += " WHERE pk_descriptionsystem = " + str(pkdessys)
                        query = self.dbase.query(sql, docommit=False)
                self.dbase.commit()

                lastsubdescriptionsystemid = self.dbase.getLastId(self.importtable) + 1
                #geom
                featgeom = layerfeat.geometry()
                success = featgeom.transform(self.xform)
                if sys.version_info.major == 2:
                    featgeomwkt = featgeom.exportToWkt()
                elif sys.version_info.major == 3:
                    featgeomwkt = featgeom.asWkt()
                geomsql = "CastToXY(ST_GeomFromText('"
                geomsql += featgeomwkt
                geomsql += "', " + str(self.dbase.crsnumber) + "))"
                if False:
                    sql = "INSERT INTO " + self.importtable + " (id_objet, id_descriptionsystem, id_revisionbegin, id_" + self.importtable.lower() + ", geom )"
                    sql += " VALUES(" + str(lastobjetid) + "," + str(lastdescriptionsystemid) +',' + str(lastrevision) + "," + str(lastsubdescriptionsystemid) + ","
                    sql += geomsql + ');'


                sql = "INSERT INTO " + self.importtable + " ( lpk_descriptionsystem,  id_" + self.importtable.lower() + ", geom )"
                sql += " VALUES("  + str(pkdessys) +',' + str(lastsubdescriptionsystemid) + ","
                sql += geomsql + ');'
                query = self.dbase.query(sql)
                #self.dbase.commit()
                pksubdessys= self.dbase.getLastRowId(self.importtable)

                for i, table in enumerate(tables):
                    if table == self.importtable and values[i] != '':
                        sql = "UPDATE " + self.importtable + " SET " + fields[i] + " = " + self.convertDataType(table,fields[i], layerfeat[values[i]])
                        sql += " WHERE pk_" + self.importtable + " = " + str(pksubdessys)
                        query = self.dbase.query(sql, docommit=False)
                self.dbase.commit()


                self.postImport(layerfeat,pkobjet, pkdessys, pksubdessys )







        if False and self.importtable == 'Points topo':
            table = 'Pointtopo'
            fielddestination=['typepointtopo', 'x', 'y', 'zgps', 'zwgs84', 'raf09', 'zmngf', 'precision', 'dx', 'dy', 'dz', 'hauteurperche',
                    'id_topographie','geom']


            linktable = {}
            for i, result in enumerate(self.results):
                for j, field in enumerate(fielddestination):
                    if table + '.' + field in result:
                        linktable[j] = i

            # print(linktable)




            for layerfeat in feats:
                sql = "INSERT INTO Pointtopo (" + ', '.join(fielddestination) + ") "
                sql += "VALUES("
                featvalues = []
                for i, field in enumerate(fielddestination):
                    # print('values',field,featvalues)
                    if field == 'geom':
                        featgeom = layerfeat.geometry()
                        success = featgeom.transform(self.xform)
                        featgeomwkt = featgeom.exportToWkt()

                        geomsql = "ST_GeomFromText('"
                        geomsql += featgeomwkt
                        geomsql += "', " + str(self.dbase.crsnumber) + ")"
                        featvalues.append(geomsql)
                    else:
                        valuefieldtemp = values[linktable[i]]
                        # print(valuefieldtemp, layerfromfieldsname)
                        if valuefieldtemp == '':
                            featvalues.append('NULL')
                        else:


                            if valuefieldtemp in layerfromfieldsname:
                                valuefieldtemp = layerfeat[valuefieldtemp]
                                # print(valuefieldtemp)
                                if valuefieldtemp is None:
                                    featvalues.append('NULL')
                                else:
                                    # print(type(valuefieldtemp))
                                    if isinstance(valuefieldtemp, unicode):
                                        featvalues.append("'" + str(valuefieldtemp) + "'")
                                    else:
                                        featvalues.append(str(valuefieldtemp))
                            else:
                                featvalues.append(str(valuefieldtemp))


                sql += ', '.join(featvalues)
                sql += ");"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()






        if progress is not None: self.dbase.qgsiface.messageBar().clearWidgets()
        if debug: logging.getLogger('Lamia').debug('end')



    def convertDataType(self, table,field, value):
        typevalue = self.dbase.dbasetables[table]['fields'][field]['PGtype']
        if 'VARCHAR' in typevalue:
            returnvalue = "'" + str(value) + "'"
        elif 'TIMESTAMP' in typevalue:
            returnvalue = "'" + str(value) + "'"
        elif 'TEXT' in typevalue:
            returnvalue = "'" + str(value) + "'"
        else:
            returnvalue = str(value)

        return returnvalue


    def postImport(self,layerfeat, pkobjet=None, pkdessys=None, pksubdessys=None):
        pass

    def initProgressBar(self, lenprogress):
        """
        Initialise la progress bar d'avancement de la generation du rapport
        :param idsforreportdict:
        :return:
        """
        if self.dbase.qgsiface is not None :
            progressMessageBar = self.dbase.qgsiface.messageBar().createMessage("import ...")
            progress = QProgressBar()

            progress.setMaximum(lenprogress)
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, self.dbase.qgsiface.messageBar().INFO)
            else:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
        else:
            progress = None

        return progress

    def setLoadingProgressBar(self, progressbar, val):
        if progressbar is not None:
            progressbar.setValue(val)
        else:
            if self.dbase.qgsiface is None:
                if val%100 == 0:
                    logging.getLogger('Lamia').info('Import de l item %d', val )
        QApplication.processEvents()



class AttributeReaderNode(CtrlNode):
    """Return the input data passed through an unsharp mask."""
    nodeName = "AttributeReaderNode"
    uiTemplate = []
    """
    uiTemplate = [
        ('sigma', 'spin', {'value': 1.0, 'step': 1.0, 'bounds': [0.0, None]}),
        ('strength', 'spin', {'value': 1.0, 'dec': True, 'step': 0.5, 'minStep': 0.01, 'bounds': [0.0, None]}),
    ]
    """

    def __init__(self, name):
        ## Define the input / output terminals available on this node
        #self.someQWidget = None
        terminals = {
            'dataIn': dict(io='in'),  # each terminal needs at least a name and
            'dataOut': dict(io='out'),  # to specify whether it is input or output
        }  # other more advanced options are available
        # as well..

        CtrlNode.__init__(self, name, terminals=terminals)
        self.stopconnect = False
        self.currentlayer = None
        self.currentlayerindex = None
        self.uniquevalues = None


    def process(self, display=True, **args):
        # CtrlNode has created self.ctrls, which is a dict containing {ctrlName: widget}
        debug = False

        results={}

        if debug: logging.getLogger("Lamia").debug('***  process ***')
        if debug: logging.getLogger("Lamia").debug( 'nodename : %s', self.name())
        if debug: logging.getLogger("Lamia").debug('args : %s', str(args))
        if debug: logging.getLogger("Lamia").debug('inputs : %s', str(self.inputs().keys()))
        if debug: logging.getLogger("Lamia").debug('outputs : %s', str(self.outputs().keys()))


        if list(self.inputs().keys())[0] == 'dataIn':

            if debug: logging.getLogger("Lamia").debug('dataIn type')
            for termname in self.outputs().keys():
                results[termname] = []
                if args['dataIn'] is not None:
                    for data in args['dataIn']:
                        if data == termname:
                            results[termname].append(data)
                        else:
                            results[termname].append(None)



            #return results

        #elif list(self.outputs().keys())[0] == 'dataOut' and len(list(self.inputs().keys())) > 0:
        elif list(self.outputs().keys())[0] == 'dataOut':
            if debug: logging.getLogger("Lamia").debug('dataOut type')
            results['dataOut'] = []
            datainput = {}
            #print('***datain', dataIn)
            leninput = None
            for termname in self.inputs().keys():
                if args[termname] is not None:
                    leninput = len(args[termname])
                    datainput[termname] = args[termname]
            if leninput is not None:
                for i in range(leninput):
                    tempres=None
                    for termname in datainput.keys():
                        if datainput[termname][i] is not None:
                            #tempres = datainput[termname][i]
                            tempres = termname
                            break
                    results['dataOut'].append(tempres)
                

        if debug: logging.getLogger("Lamia").debug('Results : %s', str(results))
        return results



        if False:
            print(self.someQWidget.comboBox_type.currentText() )
            if self.someQWidget.comboBox_type.currentText() == 'popo':
                output = [datai*10 for datai in dataIn]
            elif self.someQWidget.comboBox_type.currentText() == 'tet':
                output = [datai*1000 for datai in dataIn]

            if False:
                sigma = self.ctrls['sigma'].value()
                strength = self.ctrls['strength'].value()
                output = dataIn - (strength * pg.gaussianFilter(dataIn, (sigma, sigma)))
        #return {'dataOut': output}

    def setLayers(self, currentlayer):
        self.currentlayer = currentlayer

    def setDbase(self, dbase):
        self.dbase = dbase




    def connected(self,localTerm, remoteTerm ):
        debug = False

        if debug : logging.getLogger("Lamia").debug('***  connected ***' )
        if debug: logging.getLogger("Lamia").debug('%s, %s, %s',self.name(), str(localTerm), str(remoteTerm))

        remotetermname = remoteTerm.node().name()
        #localtermname = remoteTerm.node().name()
        if remotetermname in  ['Input', 'Output']:
            if not self.stopconnect:
                self.clearTerminals()
                self.stopconnect = True
            else:
                self.stopconnect = False
                self.update()
                return
        else:
            if debug: logging.getLogger("Lamia").debug('update')
            self.update()

        if remoteTerm.node().name() == 'Output':
            if debug: logging.getLogger("Lamia").debug('connecttype : Output')
            self.clearTerminals()

            #print(self.outputs().keys())
            termname = remoteTerm.name()
            table, field = termname.split('.')
            # print(table, field)
            fullcst = self.dbase.dbasetables[table]['fields'][field]['Cst']
            values = [elem[0] for elem in fullcst]
            for value in values:
                self.addInput(name=str(value))
            self.graphicsItem().bounds = QtCore.QRectF(0, 0, 200, len(values) * 15)
            self.graphicsItem().update()

            self.addOutput(name='dataOut')
            output = self.outputs()['dataOut']
            output.connectTo(remoteTerm)
            #self.update()


        elif remoteTerm.node().name() == 'Input':
            if debug: logging.getLogger("Lamia").debug('connecttype : Input')
            self.clearTerminals()
            termfieldname = remoteTerm.name()
            #uniquevalues
            self.uniquevalues=None
            for i, fieldname in enumerate([field.name() for field in self.currentlayer.fields()]):
                if fieldname == termfieldname:
                    self.uniquevalues = self.currentlayer.uniqueValues(i)
                    self.currentlayerindex = i
                    break
            if len(self.uniquevalues)<20:
                for uniquevalue in self.uniquevalues:
                    self.addOutput(name=str(uniquevalue))
                self.graphicsItem().bounds = QtCore.QRectF(0, 0, 200, len(self.uniquevalues) * 15)
                self.graphicsItem().update()
                #fc.outputNode.graphicsItem().updateTerminals()
                #fc.outputNode.graphicsItem().update()
                #self.addOutput(name='test')
                #self.addOutput(name='test1')

            self.addInput(name='dataIn')

            input = self.inputs()['dataIn']
            input.connectTo(remoteTerm)

            #self.update()




    """
    def ctrlWidget(self):  # this method is optional
        self.someQWidget = UserUI()
        self.someQWidget.comboBox_type.currentIndexChanged.connect(self.update)
        return self.someQWidget
    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_import_tool.ui')
        uic.loadUi(uipath, self)


class DialogUI(QDialog):
    def __init__(self, parent=None):
        super(DialogUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_import_tool_dialog.ui')
        uic.loadUi(uipath, self)

    def dialogIsFinished(self):
        return None