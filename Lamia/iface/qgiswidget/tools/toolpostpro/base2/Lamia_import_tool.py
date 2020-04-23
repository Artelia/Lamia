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
from collections import OrderedDict
import datetime
import decimal
import logging, sys, re
import numpy as np
from collections import OrderedDict
from pprint import pprint

import qgis, qgis.utils
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from qgis.PyQt.QtWidgets import (QInputDialog,QTableWidgetItem,QComboBox,QAction,QProgressBar,QApplication,QWidget,QToolButton,
                                     QDialog, QGridLayout, QSplitter, QLabel, QFrame, QVBoxLayout)


#from .importtools.InspectionDigue_Import import ImportObjetDialog
from ...lamia_abstracttool import AbstractLamiaTool
#from Lamia.iface.qgiswidget.tools.lamia_abstracttool  import AbstractLamiaTool 
from Lamia.libslamia.lamiaimport.lamiaimport import ImportCore
from Lamia.main.DBaseParser import DBaseParser

from .Lamia_import_tool_flowchart import FlowChartWidget


class ImportTool(AbstractLamiaTool):


    POSTPROTOOLNAME = ImportCore.POSTPROTOOLNAME

    tooltreewidgetCAT = 'Import/export'
    tooltreewidgetSUBCAT = 'Import'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'Lamia_import_tool_icon.png')

    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(ImportTool, self).__init__(**kwargs)

        # self.importtool = ImportCore(dbaseparser=self.dbase,
        #                             messageinstance=self.mainifacewidget.connector)
        self.qfiledlg = self.mainifacewidget.qfiledlg
        self.flowchartdlg = FlowChartWidget(dbase=self.dbase, 
                                            messageinstance=self.mainifacewidget.connector,
                                            mainifacewidget=self.mainifacewidget)

        #self.postInit()

        # self.dialog = QDialog()
        # layout = QGridLayout()
        # self.dialog.setLayout(layout)

        self.flowqlabelmessage = None
        self.currentlayer = None


    def initMainToolWidget(self):


        self.toolwidgetmain = UserUI()
        #self.toolwidgetmain.toolButton_update.clicked.connect(self.updateShowedTable)

        items = [ "Infralineaire", 'Noeud', 'Equipement', 'Photo']
        self.toolwidgetmain.comboBox_typeimport.addItems(items)

        # methode 1
        #self.toolwidgetmain.pushButton_import.clicked.connect(self.showTable)
        #self.toolwidgetmain.pushButton_importer.clicked.connect(self.work)
        #self.toolwidgetmain.pushButton_validimport.clicked.connect(self.validImport)
        #self.toolwidgetmain.pushButton_rollback.clicked.connect(self.rollbackImport)

        #flowchart
        self.toolwidgetmain.pushButton_flowchart.clicked.connect(self.showFlowChart)
        #self.dialogui = DialogUI()

    def postToolTreeWidgetCurrentItemChanged(self):
        self._updateFromTables()



    def _updateFromTables(self):

        self.toolwidgetmain.comboBox_tableimport.clear()
        if qgis.utils.iface is not None:
            layers = [tree_layer.layer() for tree_layer in qgis.core.QgsProject.instance().layerTreeRoot().findLayers()]
            layqgis=[]
            for tablename in self.dbase.dbasetables.keys():
                layqgis.append(self.dbase.dbasetables[tablename]['layerqgis'])

            for lay in layers:
                if not lay in layqgis:
                    self.toolwidgetmain.comboBox_tableimport.addItems([lay.name()])

    def ___________________________________flowchartpart(self):
        pass





    def showFlowChart(self, qgslayer=None):
        self._defineCurrentLayer()

        tolayername = self.toolwidgetmain.comboBox_typeimport.currentText()
        fromqgslayer = self.currentlayer
        self.flowchartdlg.initFromandToLayers(fromqgslayer, tolayername)


        if qgis.utils.iface is not None:
            self.flowchartdlg.setWindowModality(QtCore.Qt.NonModal)
            self.flowchartdlg.show()
        else:
            self.flowchartdlg.exec_()


    def _defineCurrentLayer(self):
        item = self.toolwidgetmain.comboBox_typeimport.currentText()

        if qgis.utils.iface is not None:
            self.currentlayer = None
            layers = [tree_layer.layer() for tree_layer in qgis.core.QgsProject.instance().layerTreeRoot().findLayers()]
            for lay in layers:
                if self.toolwidgetmain.comboBox_tableimport.currentText() == lay.name():
                    self.currentlayer = lay
                    break

            if self.currentlayer  is None:
                return
        else:  # debug outside qgis
            if self.currentlayer is None:
                import Lamia
                lamiapath = os.path.dirname(Lamia.__file__)
                layerpath = os.path.join(lamiapath,'..', 'test','shpforimporttest', 'TRONCONS_TEST.shp' )
                print('*********layerpath', layerpath)
                #layerpath = os.path.join(os.path.dirname(__file__), '..','..','..','test','99_import_test_files','reseau_L93.shp.shp')
                self.currentlayer = qgis.core.QgsVectorLayer(layerpath, 'test', 'ogr')
                print(self.currentlayer.featureCount())












    """
    def ___________________________________simpletablepart(self):
        pass

    def showTable(self):
        self._defineCurrentLayer()

        if False:
            item = self.toolwidgetmain.comboBox_typeimport.currentText()
            self.currentlayer = None
            if qgis.utils.iface is not None:
                # if not self.dbase.standalone:
                if sys.version_info.major == 2:
                    layers = qgis.utils.iface.legendInterface().layers()
                elif sys.version_info.major == 3:
                    layers = [tree_layer.layer() for tree_layer in qgis.core.QgsProject.instance().layerTreeRoot().findLayers()]


                for lay in layers:
                    if self.toolwidgetmain.comboBox_tableimport.currentText() == lay.name():
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

        item = self.toolwidgetmain.comboBox_typeimport.currentText()
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

        self.toolwidgetmain.tableWidget.setRowCount(0)
        self.toolwidgetmain.tableWidget.setColumnCount(3)
        for tablename in templinkuserwgd:
            if tablename in self.dbase.dbasetables.keys():
                dbasetable = self.dbase.dbasetables[tablename]
                for field in dbasetable['fields'].keys():
                    # print(field)
                    rowPosition = self.toolwidgetmain.tableWidget.rowCount()
                    self.toolwidgetmain.tableWidget.insertRow(rowPosition)
                    itemfield = QTableWidgetItem(tablename + '.' + field)
                    itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.toolwidgetmain.tableWidget.setItem(rowPosition, 0, itemfield)
                    # item.setFlags()
                    #if field[0:2] != 'id' and field[0:2] != 'pk':
                    if field.split('_')[0] not in ['pk','lpk']:
                        combofield = QComboBox()
                        combofield.addItems(currentlayerfieldsname)
                        self.toolwidgetmain.tableWidget.setCellWidget(rowPosition, 1, combofield)

                        pushbutton = QToolButton()
                        pushbutton.setText('...')
                        pushbutton.setObjectName(tablename + '.' + field)
                        self.toolwidgetmain.tableWidget.setCellWidget(rowPosition, 2, pushbutton)
                        pushbutton.clicked.connect(self.editFields)

                    else:
                        itemfield = QTableWidgetItem('')
                        self.toolwidgetmain.tableWidget.setItem(rowPosition, 1, itemfield)

        #self.importobjetdialog.exec_()
        #tableview = self.importobjetdialog.dialogIsFinished()
        if False:
            if tableview is not None:
                result = []
                for row in range(self.toolwidgetmain.tableWidget.rowCount()):
                    if self.toolwidgetmain.tableWidget.cellWidget(row, 1) is not None:
                        result.append([self.toolwidgetmain.tableWidget.item(row, 0).text(),
                                       self.toolwidgetmain.tableWidget.cellWidget(row, 1).currentText()])
                    else:
                        result.append([self.toolwidgetmain.tableWidget.item(row, 0).text(),
                                       self.toolwidgetmain.tableWidget.item(row, 1).text()])

                self.work(result)


    def editFields(self):
        pushbuttonsender = self.sender()
        pushbuttonname = pushbuttonsender.objectName()
        # print(pushbuttonname)

        self.dialogui.tableWidget_from.clear()
        self.dialogui.tableWidget_to.clear()



        #fill tableWidget_from in dialog
        for  row in range(self.toolwidgetmain.tableWidget.rowCount()):
            # print('cell',self.toolwidgetmain.tableWidget.cellWidget(row, 2))
            if self.toolwidgetmain.tableWidget.cellWidget(row, 2) == pushbuttonsender:
                layerfromfield = self.toolwidgetmain.tableWidget.cellWidget(row, 1).currentText()
                layerfromfieldindex = self.toolwidgetmain.tableWidget.cellWidget(row, 1).currentIndex() -1
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

    """




    
    def initProgressBar(self, lenprogress):
        """
        Initialise la progress bar d'avancement de la generation du rapport
        :param idsforreportdict:
        :return:
        """
        if qgis.utils.iface is not None :
            progressMessageBar = qgis.utils.iface.messageBar().createMessage("import ...")
            progress = QProgressBar()

            progress.setMaximum(lenprogress)
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.utils.iface.messageBar().pushWidget(progressMessageBar, qgis.utils.iface.messageBar().INFO)
            else:
                qgis.utils.iface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
        else:
            progress = None

        return progress

    def setLoadingProgressBar(self, progressbar, val):
        if progressbar is not None:
            progressbar.setValue(val)
        else:
            if qgis.utils.iface is None:
                if val%100 == 0:
                    logging.getLogger('Lamia').info('Import de l item %d', val )
        QApplication.processEvents()


    def validImport(self):
        self.dbase.forcenocommit = False
        sql = "COMMIT"
        self.dbase.query(sql)


    def rollbackImport(self):
        self.dbase.forcenocommit = False
        sql = "ROLLBACK"
        self.dbase.query(sql)


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



    """
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



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_import_tool.ui')
        uic.loadUi(uipath, self)



