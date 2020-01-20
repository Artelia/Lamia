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

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QTabWidget, QHeaderView, QTableWidgetItem, QComboBox,
                                 QTextBrowser)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QTabWidget, QHeaderView, QTableWidgetItem, QComboBox,
                                     QTextBrowser)

from ..base2.lamiabase_observation_tool import BaseObservationTool

import os, sys, datetime

if sys.version_info.major == 2:
    from ..libs import xlrd
else:
    try:
        import xlrd
    except:
        from ..libs import xlrd




class BaseChantierSousObservationTool(BaseObservationTool):

    dbasetablename = 'Observation'



    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseChantierSousObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)


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


    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.dbase.variante in ['Orange']:
            if self.userwdgfield is None:
                # ****************************************************************************************
                # userui
                self.userwdgfield = UserUI()
                self.linkuserwdgfield = {'Observation' : {'linkfield' : 'id_observation',
                                                 'widgets' : {
                                                                'datetimeobservation' : self.userwdgfield.dateTimeEdit_datetimeobservation,

                                                              }},
                                    'Objet' : {'linkfield' : 'id_objet',
                                              'widgets' : {}}}

                typessousfiches = self.sousfichesdict.keys()
                self.userwdgfield.comboBox_fichetype.addItems(typessousfiches)
                self.userwdgfield.comboBox_fichetype.currentIndexChanged.connect(self.SousFicheTypeChanged)
                self.userwdgfield.comboBox_fichetype.currentIndexChanged.emit(0)

                # self.frame_editing.setVisible(False)
                self.frame_editing.setParent(None)



    def SousFicheTypeChanged(self, comboindex):
        currentcombotext = self.userwdgfield.comboBox_fichetype.currentText()
        currentdict = self.sousfichesdict[currentcombotext]

        self.userwdgfield.tableWidget.setRowCount(0)
        self.userwdgfield.tableWidget.clear()
        self.userwdgfield.tableWidget.setColumnCount(4)

        self.userwdgfield.tableWidget.setHorizontalHeaderLabels(['N°', 'Critere', 'Contrôle', 'Observation'])

        header = self.userwdgfield.tableWidget.horizontalHeader()
        if False:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                header.setResizeMode(1, QHeaderView.Stretch)
                header.setResizeMode(0, QHeaderView.ResizeToContents)
            else:
                header.setSectionResizeMode(1, QHeaderView.Stretch)
                header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

        for number, name in currentdict:
            rowPosition = self.userwdgfield.tableWidget.rowCount()
            self.userwdgfield.tableWidget.insertRow(rowPosition)



            if name != '':
                item = QTableWidgetItem(number)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.userwdgfield.tableWidget.setItem(rowPosition, 0, item)

                item = QTableWidgetItem(name)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.userwdgfield.tableWidget.setItem(rowPosition, 1, item)

                wdg = QComboBox()
                wdg.addItems(['Avec réserve', 'sans réserve', 'sans objet'])
                self.userwdgfield.tableWidget.setCellWidget(rowPosition, 2, wdg)

                wdg = QTextBrowser()
                wdg.setMinimumHeight(30)
                wdg.setMaximumHeight(50)
                wdg.setReadOnly(False)
                self.userwdgfield.tableWidget.setCellWidget(rowPosition, 3, wdg)
            else:
                item = QTableWidgetItem(number)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.userwdgfield.tableWidget.setItem(rowPosition, 1, item)

            self.userwdgfield.tableWidget.setWordWrap(True)
            self.userwdgfield.tableWidget.resizeColumnToContents(0)
            self.tableWidget.setColumnWidth(1, 200)
            self.userwdgfield.tableWidget.resizeRowsToContents()
            header.setStretchLastSection(True)


    def createDictionnary(self):
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


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            self.userwdgfield.comboBox_fichetype.setEnabled(True)
            self.userwdgfield.comboBox_fichetype.setCurrentIndex(0)
            self.userwdgfield.comboBox_fichetype.currentIndexChanged.emit(0)
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:  #copy last obs text
                datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.initFeatureProperties(feat, self.dbasetablename, 'datetimeobservation', datecreation)


        else:
            self.userwdgfield.comboBox_fichetype.setEnabled(False)
            self.loadTableFeature()



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

            if self.parentWidget.dbasetablename == 'Observation':
                #currentparentlinkfield = self.parentWidget.currentFeature['id_desordre']
                #parent iddesordre
                sql = " SELECT id_observation FROM Observation WHERE pk_observation = " + str(self.parentWidget.currentFeaturePK)
                idobservation = self.dbase.query(sql)[0][0]

                sql = "UPDATE Observation SET lid_observation = " + str(idobservation)
                sql += " WHERE pk_observation = " + str(self.currentFeaturePK)
                query = self.dbase.query(sql)
                self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):
        self.saveTableFeature()

    def loadTableFeature(self):
        # get typeobservation
        sql = "SELECT typeobservation FROM Observation WHERE pk_observation = " + str(self.currentFeaturePK)
        res = self.dbase.query(sql)[0][0]
        for nomsousfiche in self.sousfichesdict.keys():
            if nomsousfiche.split(' ')[0] == res:
                self.userwdgfield.comboBox_fichetype.setCurrentText(nomsousfiche)
                break

        for i in range(self.userwdgfield.tableWidget.rowCount() ):
            item = self.userwdgfield.tableWidget.item(i, 0)
            item = self.userwdgfield.tableWidget.item(i, 0)
            if item is not None:
                itemtext0 = item.text().split('.')[-1]
                sql = "SELECT item_type_" + str(itemtext0) + " , item_obs_" + str(itemtext0) + " FROM Observation "
                sql += " WHERE pk_observation = " + str(self.currentFeaturePK)
                itemtype, itemobs = self.dbase.query(sql)[0]
                if self.dbase.isAttributeNull(itemtype):
                    self.userwdgfield.tableWidget.cellWidget(i, 3).setPlainText('ERROR READING')
                else:
                    self.userwdgfield.tableWidget.cellWidget(i, 2).setCurrentIndex(itemtype)
                    self.userwdgfield.tableWidget.cellWidget(i, 3).setPlainText(itemobs)




    def saveTableFeature(self):
        sqlupdate = []

        #typeobservation
        sqlupdate.append("typeobservation = '" + self.userwdgfield.comboBox_fichetype.currentText().split(' ')[0] + "'")

        #table values
        for i in range(self.userwdgfield.tableWidget.rowCount() ):
            item = self.userwdgfield.tableWidget.item(i, 0)
            if item is not None:
                itemtext0 = item.text().split('.')[-1]
                indexitem = int(itemtext0)
                columname = 'item_type_' + str(indexitem)
                value = self.userwdgfield.tableWidget.cellWidget(i, 2).currentIndex()
                sqlupdate.append(columname + ' = ' + str(value))

                columname = 'item_obs_' + str(indexitem)
                value = self.userwdgfield.tableWidget.cellWidget(i, 3).toPlainText()
                sqlupdate.append(columname + " = '" + str(value) + "'")

        sql = " UPDATE Observation SET " + ', '.join(sqlupdate)
        sql += " WHERE pk_observation = " + str(self.currentFeaturePK)

        self.dbase.query(sql)




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantier_sousobservation_tool_ui.ui')
        uic.loadUi(uipath, self)






