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
import xlrd

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget, QTabWidget, QHeaderView, QTableWidgetItem, QComboBox,
                                     QTextBrowser)

from ..base2.lamiabase_observation_tool import BaseObservationTool




class BaseChantierSousObservationTool(BaseObservationTool):

    tooltreewidgetSUBCAT = None
    tempparentjoin = {}
    PARENTJOIN = {'Observation': {'colparent': 'id_observation',
                'colthistable': 'lid_observation',
                    'tctable': None,
                    'tctablecolparent':None,
                    'tctablecolthistable':None}}




    def __init__(self, **kwargs):
        super(BaseChantierSousObservationTool, self).__init__(**kwargs)
        self.sousfichesdict = self.createDictionnary()

    """
    def initTool(self):
        super(BaseChantierSousObservationTool, self).initTool()
        # ****************************************************************************************
        # Main spec

        self.linkagespec = {'Observation' : {'tabletc' : None,
                                           'idsource' : 'lid_observation',
                                       'idtcsource' : None,
                                           'iddest' : 'id_observation',
                                       'idtcdest' : None,
                                           'desttable' : ['Observation']},
                             }

        self.sousfichesdict = self.createDictionnary()
    """

    def initMainToolWidget(self):

        if self.dbase.variante in ['Orange']:

            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {'Observation' : {'linkfield' : 'id_observation',
                                                'widgets' : {
                                                            'datetimeobservation' : self.toolwidgetmain.dateTimeEdit_datetimeobservation,

                                                            }},
                                'Objet' : {'linkfield' : 'id_objet',
                                            'widgets' : {}}}
            listcomboitems = []
            for fichekey in self.sousfichesdict.keys():
                listcomboitems.append(fichekey + ' ' + self.sousfichesdict[fichekey]['name'])
            #typessousfiches = self.sousfichesdict.keys()
            self.toolwidgetmain.comboBox_fichetype.addItems(listcomboitems)
            self.toolwidgetmain.comboBox_fichetype.currentIndexChanged.connect(self.SousFicheTypeChanged)
            self.toolwidgetmain.comboBox_fichetype.currentIndexChanged.emit(0)

            # self.frame_editing.setVisible(False)
            #self.frame_editing.setParent(None)



    def SousFicheTypeChanged(self, comboindex):
        currentcombotext = self.toolwidgetmain.comboBox_fichetype.currentText()
        currentdict = self.sousfichesdict[currentcombotext.split(' ')[0]]


        self.toolwidgetmain.tableWidget.setRowCount(0)
        self.toolwidgetmain.tableWidget.clear()
        self.toolwidgetmain.tableWidget.setColumnCount(4)

        self.toolwidgetmain.tableWidget.setHorizontalHeaderLabels(['N°', 'Critere', 'Contrôle', 'Observation'])

        header = self.toolwidgetmain.tableWidget.horizontalHeader()

        for dataindex in currentdict['datas'].keys():
            rowPosition = self.toolwidgetmain.tableWidget.rowCount()
            self.toolwidgetmain.tableWidget.insertRow(rowPosition)

            if currentdict['datas'][dataindex]['description'] is not None:    #it is not a comment
                item = QTableWidgetItem(dataindex)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.toolwidgetmain.tableWidget.setItem(rowPosition, 0, item)

                item = QTableWidgetItem(currentdict['datas'][dataindex]['description'])
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.toolwidgetmain.tableWidget.setItem(rowPosition, 1, item)

                if currentdict['datas'][dataindex]['type'] is None:
                    wdg = QComboBox()
                    wdg.addItems(['Avec réserve', 'sans réserve', 'sans objet'])
                    self.toolwidgetmain.tableWidget.setCellWidget(rowPosition, 2, wdg)
                else:
                    item = QTableWidgetItem()
                    self.toolwidgetmain.tableWidget.setItem(rowPosition, 2, item)
                    item.setBackground(QtCore.Qt.gray)
                    item.setFlags(QtCore.Qt.NoItemFlags)

                wdg = QTextBrowser()
                wdg.setMinimumHeight(30)
                wdg.setMaximumHeight(50)
                wdg.setReadOnly(False)
                self.toolwidgetmain.tableWidget.setCellWidget(rowPosition, 3, wdg)
            else:
                item = QTableWidgetItem(dataindex)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.toolwidgetmain.tableWidget.setItem(rowPosition, 1, item)

            self.toolwidgetmain.tableWidget.setWordWrap(True)
            self.toolwidgetmain.tableWidget.resizeColumnToContents(0)
            self.toolwidgetmain.tableWidget.setColumnWidth(1, 200)
            self.toolwidgetmain.tableWidget.resizeRowsToContents()
            header.setStretchLastSection(True)


    def createDictionnary(self):
        """
        dict : { ..., 1.1 : {'name' : 'Tranchée,
                            'datas' : {..., index : {'description' :  description
                                                    , 'type' : type
                                                    }
                                      }
                            }
                }

        :return:
        """


        pathxls = os.path.join(os.path.dirname(__file__), 'sousfiches', 'Orange.xlsx')
        xlsbook = xlrd.open_workbook(pathxls)

        sousfichesdict = {}
        firstcolcode = None

        sheet = xlsbook.sheets()[0]
        for row in range(sheet.nrows):
            firstcol =  sheet.cell_value(row, 0)

            if firstcol == '':
                if sheet.cell_value(row, 1) == '' and sheet.cell_value(row, 2) == '':
                    break

            else:
                firstcolname = firstcol
                firstcolcode = firstcolname.split(' ')[0]
                sousfichesdict[firstcolcode] = {}
                sousfichesdict[firstcolcode]['name'] = ' '.join(firstcolname.split(' ')[1:])
                sousfichesdict[firstcolcode]['datas'] = {}

            sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)] = {}
            #sousfichesdict[firstcolcode]['datas'].append([sheet.cell_value(row, 1) , sheet.cell_value(row, 2), sheet.cell_value(row, 3)])

            if sheet.cell_value(row, 2) != '':
                sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)]['description'] = sheet.cell_value(row, 2)
            else:
                sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)]['description'] = None

            if sheet.cell_value(row, 3) != '':
                sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)]['type'] = sheet.cell_value(row,3)
            else:
                sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)]['type'] = None

        return sousfichesdict






    def createDictionnary_caduc(self):
        pathxls = os.path.join(os.path.dirname(__file__), 'sousfiches', 'Orange.xlsx')
        xlsbook = xlrd.open_workbook(pathxls)

        sousfichesdict = {}
        firstcolname = None

        sheet = xlsbook.sheets()[0]
        for row in range(sheet.nrows):
            firstcol =  sheet.cell_value(row, 0)
            if firstcol == '':
                if sheet.cell_value(row, 1) == '' and sheet.cell_value(row, 2) == '':
                    break

            else:
                firstcolname = firstcol
                sousfichesdict[firstcolname]=[]

            sousfichesdict[firstcolname].append([sheet.cell_value(row, 1) , sheet.cell_value(row, 2)])

        return sousfichesdict


    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        if self.currentFeaturePK is None:
            self.toolwidgetmain.comboBox_fichetype.setEnabled(True)
            self.toolwidgetmain.comboBox_fichetype.setCurrentIndex(0)
            self.toolwidgetmain.comboBox_fichetype.currentIndexChanged.emit(0)
            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:  #copy last obs text
                #datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                #self.initFeatureProperties(feat, self.DBASETABLENAME, 'datetimeobservation', datecreation)
                datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.formutils.applyResultDict({'datetimeobservation': datecreation}, checkifinforgottenfield=False)

        else:
            self.toolwidgetmain.comboBox_fichetype.setEnabled(False)
            self.loadTableFeature()


    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        # idnoeud = self.currentFeature.id()
        pkobs = self.currentFeaturePK
        lastidobs = self.dbase.getLastId('Observation') + 1
        sql = "UPDATE Observation SET id_observation = " + str(lastidobs) + ","
        sql += "lpk_objet = " + str(pkobjet)
        sql += " WHERE pk_observation = " + str(pkobs) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:

            if self.parentWidget.DBASETABLENAME == 'Observation':
                #currentparentlinkfield = self.parentWidget.currentFeature['id_desordre']
                #parent iddesordre
                sql = " SELECT id_observation FROM Observation WHERE pk_observation = " + str(self.parentWidget.currentFeaturePK)
                idobservation = self.dbase.query(sql)[0][0]

                sql = "UPDATE Observation SET lid_observation = " + str(idobservation)
                sql += " WHERE pk_observation = " + str(self.currentFeaturePK)
                query = self.dbase.query(sql)
                self.dbase.commit()
    """

    def postSaveFeature(self, savedfeaturepk=None):
        self.saveTableFeature(savedfeaturepk)

        #self.dbase.dbasetables['Desordre']['layerqgis'].triggerRepaint()
        self.mainifacewidget.qgiscanvas.layers['Desordre']['layerqgis'].triggerRepaint()



    def loadTableFeature(self):
        # get typeobservation
        sql = "SELECT typeobservation FROM Observation WHERE pk_observation = " + str(self.currentFeaturePK)
        res = self.dbase.query(sql)[0][0]

        # for nomsousfiche in self.sousfichesdict.keys():
        #     if nomsousfiche.split(' ')[0] == res:
        #         self.toolwidgetmain.comboBox_fichetype.setCurrentText(nomsousfiche)
        #         break

        if res not in self.sousfichesdict.keys():
            return

        self.toolwidgetmain.comboBox_fichetype.setCurrentText(res + ' ' + self.sousfichesdict[res]['name'])

        for i in range(self.toolwidgetmain.tableWidget.rowCount() ):

            item = self.toolwidgetmain.tableWidget.item(i, 0)
            if item is not None:
                itemtext0 = item.text().split('.')[-1]
                sql = "SELECT item_type_" + str(itemtext0) + " , item_obs_" + str(itemtext0) + " FROM Observation "
                sql += " WHERE pk_observation = " + str(self.currentFeaturePK)

                itemtype, itemobs = self.dbase.query(sql)[0]
                if not self.dbase.utils.isAttributeNull(itemtype):
                    self.toolwidgetmain.tableWidget.cellWidget(i, 2).setCurrentIndex(itemtype)
                self.toolwidgetmain.tableWidget.cellWidget(i, 3).setPlainText(itemobs)




    def saveTableFeature(self, featurepk):
        sqlupdate = []

        #typeobservation
        sqlupdate.append("typeobservation = '" + self.toolwidgetmain.comboBox_fichetype.currentText().split(' ')[0] + "'")

        #table values
        for i in range(self.toolwidgetmain.tableWidget.rowCount() ):
            item = self.toolwidgetmain.tableWidget.item(i, 0)
            if item is not None:
                itemtext0 = item.text().split('.')[-1]
                indexitem = int(itemtext0)

                if self.toolwidgetmain.tableWidget.cellWidget(i, 2) is not None:
                    columname = 'item_type_' + str(indexitem)
                    value = self.toolwidgetmain.tableWidget.cellWidget(i, 2).currentIndex()
                    sqlupdate.append(columname + ' = ' + str(value))

                columname = 'item_obs_' + str(indexitem)
                value = self.toolwidgetmain.tableWidget.cellWidget(i, 3).toPlainText()
                sqlupdate.append(columname + " = '" + str(value) + "'")

        sql = " UPDATE Observation SET " + ', '.join(sqlupdate)
        sql += " WHERE pk_observation = " + str(featurepk)

        self.dbase.query(sql)






class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantier_sousobservation_tool_ui.ui')
        uic.loadUi(uipath, self)






