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
import statistics
from collections import Counter
import json
import io
import sys
from functools import partial
import random
import datetime
import pandas as pd
import numpy as np
import pprint
from pprint import pprint
import inspect
import os
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

from qgis.PyQt import QtGui, uic, QtCore
from qgis.PyQt.QtWidgets import (
    QWidget,
    QTableWidgetItem,
    QHeaderView,
    QSizePolicy,
    QFileDialog,
    QVBoxLayout,
    QFrame,
    QLabel,
    QInputDialog,
    QMessageBox,
    QColorDialog,
    QPushButton,
)


from lamiaqgisiface.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool


class StatTool(AbstractLamiaTool):

    POSTPROTOOLNAME = "stattool"

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Overview")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Statistics")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamiabase_sketch_tool_icon.png"
    )

    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(StatTool, self).__init__(**kwargs)

        # Class' attributes
        self.variable = ["Troncon", "ZoneGeo"]
        # Raw data & clean data
        self.result = None
        self.resultClean = None
        self.counter = None

        # Save query options as dict & path as string
        self.queryToSave = {}
        self.loadedQueryPath = None

        self.currentQuery = {}
        self.colorsDF = []
        self.colorsDFT = []

        # Query load
        # True = setDefaultColor not necessary
        # False = setDefaultColor necessary
        self.hasColor = False

        # Misc.
        self.tablesList = None
        self.validQuery = None
        self.abbv = {
            "AER": "Aérien",
            "CLA": "Clapet",
            "DIG": "Digue",
            "ENT": "Enterré",
            "NC": "Non-connu",
            "REM": "Remarque",
            "VAN": "Vanne",
        }

        # Multi-graph
        self.dates = []
        self.dictGraphs = []
        self.dataFrame = None
        self.df = None

        # Debugging stage
        self.isDebug = False

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Synthese'
        self.NAME = 'Statistiques'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        self.multipleselection = True

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)

        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_croquis_tool_icon.png')
        self.qtreewidgetfields = ['libelle']
    """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        # ComboBox's lists
        graphTypeList = ["Camembert", "Hist.", "Hist. cum."]
        # graphTypeList = ["Hist.", "Hist. cum."]
        # self.tablesList = list(self.dbase.dbasetables.keys())
        self.tablesList = ["edge", "equipment", "node"]

        # Clear comboBox
        self.toolwidgetmain.comboBoxTable.clear()
        self.toolwidgetmain.comboBoxField.clear()
        self.toolwidgetmain.comboBoxGraphType.clear()

        # Fill comboBox with lists
        self.toolwidgetmain.comboBoxTable.addItems(sorted(self.tablesList))
        self.toolwidgetmain.comboBoxGraphType.addItems(sorted(graphTypeList))

        # Fill queries list comboBox
        self.updatesQueriesList()

        # Updates field combobox given the currentText
        self.toolwidgetmain.comboBoxTable.currentIndexChanged.connect(self.updateFields)

        # Load field combobox on load
        self.toolwidgetmain.comboBoxTable.currentIndexChanged.emit(0)

        # Display first element
        self.toolwidgetmain.comboBoxField.setCurrentIndex(0)
        self.toolwidgetmain.comboBoxGraphType.setCurrentIndex(1)

        # Updates stats labels given tables currentText and fields currentText
        self.toolwidgetmain.pushButtonExecute.clicked.connect(self.updateGUI)
        self.toolwidgetmain.pushButtonExecuteAdv.clicked.connect(self.updateGUI)

        # Load query from memory
        self.connectComboSavedQueries()

        # Modify query
        self.toolwidgetmain.pushButtonMod.clicked.connect(self.modifyTextFile)

        # Save query
        self.toolwidgetmain.pushButtonSave.clicked.connect(self.createNewTextFile)

        # Delete query
        self.toolwidgetmain.pushButtonDel.clicked.connect(self.deleteTextFile)

        # Update graphs
        # self.toolwidgetmain.comboBoxGraphType.currentIndexChanged.connect(self.plotGraph)

        # self.figuretype, self.axtype = plt.subplots()
        self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111)
        self.graphwdg = Label()
        self.toolwidgetmain.frame_chart.layout().addWidget(self.graphwdg)

        # self.postOnActivation()

    def disconnectComboSavedQueries(self):
        try:
            self.toolwidgetmain.comboBoxSavedQueries.currentIndexChanged.disconnect(
                self.loadTextFile
            )
        except:
            print("Disconnect loadTextFile failed") if self.isDebug else None

    def connectComboSavedQueries(self):
        try:
            self.toolwidgetmain.comboBoxSavedQueries.currentIndexChanged.connect(
                self.loadTextFile
            )
        except:
            print("Connect loadTextFile failed") if self.isDebug else None

    def updateFields(self):
        """
        Clear current comboBoxField and fill it with fields fetched from comboBoxTable
        """

        fieldsList = []
        parentTables = []
        # Fetch current table
        currentTable = self.toolwidgetmain.comboBoxTable.currentText()
        try:
            # Fetch table's fields
            fieldsList = list(self.dbase.dbasetables[currentTable]["fields"].keys())

            # Fetch all related tables and add related fields to fields' list
            parentTables = self.dbase.getParentTable(currentTable)

        except KeyError as e:
            QMessageBox.about(
                self,
                "Erreur".upper(),
                "Table {table} non-trouvée".format(
                    table=self.toolwidgetmain.comboBoxTable.currentText().upper()
                ),
            )
            print(
                "{type}: {exception} raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), exception=e, fct="updateFields"
                )
            )

        for element in parentTables:
            fieldsList.extend(list(self.dbase.dbasetables[element]["fields"].keys()))

        # Remove duplicates if necessary
        fieldsList = list(set(fieldsList))

        # TODO: Pourquoi cela fonctionne sans disconnect/connect?????????????????????????
        # Clear comboBoxField and add items from fieldsList
        self.toolwidgetmain.comboBoxField.clear()
        self.toolwidgetmain.comboBoxField.addItems(sorted(fieldsList))

        # Display first element
        self.toolwidgetmain.comboBoxField.setCurrentIndex(0)

    def getDataFrame(self):
        """
        Fetch data given SQL query
        :return: dataframe of values per dates and items
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        selectFrom = str()
        # Detects which button is called
        sender = self.sender()
        self.dates = []

        # ----- CLASSIQUE -----
        # Create SQL query from table and field comboBox
        if sender.objectName() == "pushButtonExecute":
            selectFrom = "SELECT {slct} FROM {frm}_now".format(
                slct=self.toolwidgetmain.comboBoxField.currentText(),
                frm=self.toolwidgetmain.comboBoxTable.currentText(),
            )

        # ----- ADVANCED -----
        # Fetch SQL query from lineEditQuery
        else:
            if self.checkText():
                selectFrom = self.toolwidgetmain.lineEditQuery.text() + "_now"

                # Extract dates from lineEditDates and add today's date
                self.dates = self.toolwidgetmain.lineEditDates.text().split(", ")

        # Reset self.dictGraphs and fill in with len(self.dates) lists
        self.dictGraphs.clear()
        # Add current date and remove empty string if necessary
        self.dates.append(datetime.date.today().strftime("%d/%m/%Y"))
        self.dates = [i for i in self.dates if i]
        self.dictGraphs = {k: {} for k in self.dates}

        print(">", selectFrom, self.dates)

        for date in self.dates:
            sql = self.dbase.updateQueryTableNow(selectFrom, date)
            pprint(sql)
            pprint(self.dbase.query(sql))
            # Query DB, clean results and add to self.dictGraphs with date as key
            self.dictGraphs[date] = dict(
                Counter(self.cleanData(self.dbase.query(sql), 0))
            )

        # Reset and fill in self.dataFrame
        pprint(self.dictGraphs)
        try:
            self.df = pd.DataFrame(self.dictGraphs)
        except TypeError as e:
            print(e)

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        return self.df

    def checkText(self):
        """
        Check whether a query is authorized or not
        :return: False if unauthorized query, True otherwise
        """
        # Strings that cannot exist in a query
        bannedQuery = ["delete", "drop", "insert", "update"]
        queryList = self.toolwidgetmain.lineEditQuery.text().split()

        # Loop through the query and check if authorized or not
        for element in queryList:
            if element.lower() in bannedQuery:
                QMessageBox.about(
                    self,
                    "Erreur".upper(),
                    "Commande {operation} non-autorisée".format(
                        operation=element.upper()
                    ),
                )
                print(">>> UNAUTHORIZED QUERY")
                return False

        return True

    def cleanData(self, listItems, index):
        """
        Given a list of tuples, return the list of the index'th element of each tuple or None otherwise
        :param listItems: list of tuples
        :param index: index at which to retrieve element
        :return: list of items, None otherwise
        """

        # print("Enter cleanData")

        try:
            asList = list(zip(*listItems))[index]
            # get type
            typeelem = None
            for elem in asList:
                if elem is not None:
                    typeelem = type(elem)
                    # print('***', typeelem)
                    if isinstance(elem, str) or isinstance(elem, unicode):
                        typeelem = "string"
                    else:
                        typeelem = "float"
                    break
            # print(asList)

            # asList = ["None" if element is None else element for element in asList]
            if typeelem == "string":
                asList = ["None" if element is None else element for element in asList]
            else:
                asList = [np.nan if element is None else element for element in asList]

            # print("Exit cleanData")
            return asList
        except (IndexError, TypeError) as e:
            print(
                "{type}: {exception} raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), exception=e, fct="cleanData"
                )
            )
            return None
        except:
            print(
                "{type}: raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), fct="cleanData"
                )
            )
            return None

        # sys.exit()

    # TODO: Not used at the moment ##############################################
    def addColors(self):
        """
        Add colors column to self.df
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Add a new column pre-filled with dummy values
        self.df["Colors"] = "Default Value"

        # Add random colors to each row at Color column
        rowNames = list(self.df.index.values)
        for row in range(len(rowNames)):
            self.df.iloc[row, self.df.columns.get_loc("Colors")] = self.oneRandomColor()

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def oneRandomColor(self):
        """
        Create a random hexadecimal color
        :return: str, random color as hex
        """
        return "#%02X%02X%02X" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    def sumAvgToLabel(self):
        """
        Update sum label via today's self.df column
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        rowNames = list(self.df.index.values)
        result = 0
        count = 0
        for element in rowNames:
            print("**", rowNames)
            # TODO: Attention isDigit() negatif / décimal
            if False:
                if element.isdigit():
                    # Fetch current row number of times it appeared
                    tmp = self.df.loc[
                        element, datetime.date.today().strftime("%d/%m/%Y")
                    ]

                    # Add to total (current row value times number of times it appeared)
                    result += float(element) * float(tmp)
                    count += float(tmp)
            try:
                # Fetch current row number of times it appeared
                tmp = self.df.loc[element, datetime.date.today().strftime("%d/%m/%Y")]

                # Add to total (current row value times number of times it appeared)
                result += float(element) * float(tmp)
                count += float(tmp)
            except Exception as e:
                print(e)

        self.toolwidgetmain.labelSum.setText(str(result))
        try:
            self.toolwidgetmain.labelAvg.setText(str(round(result / count, 2)))
        except ZeroDivisionError:
            self.toolwidgetmain.labelAvg.setText(str(0))

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def denumToLabel(self):
        """
        Update denum label via today's self.df column
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        try:
            # Fetch max value from today's column
            index = self.df[datetime.date.today().strftime("%d/%m/%Y")].idxmax()
            value = self.df.loc[index, datetime.date.today().strftime("%d/%m/%Y")]
            result = "{index}: {value}".format(index=index, value=value)
        except TypeError:
            result = "-"

        self.toolwidgetmain.labelOcc.setText(str(result))

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def dataFrameToTableWidget(self):
        """
        Update tableWidgetDetails from self.df
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Reset table widget
        self.toolwidgetmain.tableWidgetDetails.setRowCount(0)
        header = self.toolwidgetmain.tableWidgetDetails.horizontalHeader()

        # Columns and rows names
        colNames = list(self.df.columns.values)
        rowNames = list(self.df.index.values)

        # Set column's number to len(colNames) + 2 (Name and Color) and row's number to len(rowNames)
        self.toolwidgetmain.tableWidgetDetails.setColumnCount(len(colNames) + 2)
        self.toolwidgetmain.tableWidgetDetails.setRowCount(len(rowNames))

        # Fill tableWidget with elements from self.dataFrame
        for row in range(len(rowNames)):
            # Insert row name
            self.toolwidgetmain.tableWidgetDetails.setItem(
                row, 0, QTableWidgetItem(str(rowNames[row]))
            )

            # Insert row values for each date
            for col in range(len(colNames)):
                # Fetch value at self.df(row, col)
                valueTmp = self.df.iat[row, col]
                # Insert value
                self.toolwidgetmain.tableWidgetDetails.setItem(
                    row, col + 1, QTableWidgetItem(str(valueTmp))
                )
                # Resize column
                header.setSectionResizeMode(col + 1, QHeaderView.ResizeToContents)

            # Color pushButton
            # Create colorPushButton
            self.createColorPushButton(row, len(colNames) + 1, str(rowNames[row]))
            # Resize column
            # header.setSectionResizeMode(len(colNames) + 1, QHeaderView.ResizeToContents)

            # Rename headers
            self.renameHeaders(colNames)

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def createColorPushButton(self, row, col, key=None):
        """
        Add pushButton to choose a color
        :param row: int, current object selected
        :param col: int, current column in which to insert pushButton
        :param key: str, current object name
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        button = QPushButton("", self)
        self.toolwidgetmain.tableWidgetDetails.setCellWidget(row, col, button)
        # ####################### Utile pour les tests - A SUPPRIMER: if key != None:
        if key is not None:
            button.clicked.connect(partial(self.openColorDialog, key))

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def renameHeaders(self, colNames):
        """
        Rename columns headers
        :param colNames: list of columns' names
        """
        # Add description for first column and Couleur for last one
        headersName = ["Description"] + colNames + ["Couleur"]
        self.toolwidgetmain.tableWidgetDetails.setHorizontalHeaderLabels(headersName)

    def plotGraph(self):
        """
        Plot graph within frameChart
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Reset self.figuretype and self.axtype
        self.figuretype.clf()
        self.axtype = self.figuretype.add_subplot(111)

        # Inverse rows for columns and columns for rows
        dfT = self.df.T
        print(dfT)

        print(">", self.currentQuery)

        """"# Create random colors
        self.colorsDF = [self.oneRandomColor() for i in range(len(self.df))]
        self.colorsDFT = [self.oneRandomColor() for i in range(len(dfT))]
        # Fetch colors from self.currentQuery if exists
        if self.toolwidgetmain.tabResearch.currentIndex() == 1 and len(self.currentQuery) != 0:
            print("> Tab Advanced - Filled dict")
            self.colorsDF = list(self.currentQuery["colorsDF"].values())
            self.colorsDFT = list(self.currentQuery["colorsDFT"].values())"""

        """"# Query from Classique
        if self.toolwidgetmain.tabResearch.currentIndex() == 0:
            print("> Tab Classique")
            # Create random colors
            colorsDF = [self.oneRandomColor() for i in range(len(self.df))]
            colorsDFT = [self.oneRandomColor() for i in range(len(dfT))]

        # Query from Advanced
        else:
            # No specified colors
            if self.currentQuery == {}:
                print("> Tab Advanced - Empty dict")
                # Create random colors
                colorsDF = [self.oneRandomColor() for i in range(len(self.df))]
                colorsDFT = [self.oneRandomColor() for i in range(len(dfT))]
            # Fetch specified colors
            else:
                print("> Tab Advanced - Filled dict")
                # Retrieve colors from self.currentQuery
                colorsDF = list(self.currentQuery["colorsDF"].values())
                colorsDFT = list(self.currentQuery["colorsDFT"].values())

        print("> colorsDF:", colorsDF)
        print("> colorsDFT:", colorsDFT)"""

        # Get current graph type
        currentChartType = self.toolwidgetmain.comboBoxGraphType.currentText()

        # ----- Histogram -----
        if currentChartType == "Hist.":
            print("> Hist.")
            # self.df.plot(kind='bar', ax=self.axtype, color=colorsDFT)
            self.df.plot(kind="bar", ax=self.axtype)

        # ----- Cumulative histogram -----
        elif currentChartType == "Hist. cum.":
            print("> Hist. cum.")
            # dfT.plot(kind='bar', ax=self.axtype, stacked=True, color=colorsDF)
            dfT.plot(kind="bar", ax=self.axtype, stacked=True)

        # ----- Pie chart -----
        elif currentChartType == "Camembert":
            print("> Camembert")
            # Check if pie chart is allowed
            if self.allowPieChart():
                # dfT.T.plot(kind='pie', ax=self.axtype, subplots=True, autopct="%.0f%%", colors=colorsDF)
                dfT.T.plot(kind="pie", ax=self.axtype, subplots=True, autopct="%.0f%%")
            # If not allowed: pop-up messageBox and graphType is Hist.
            else:
                QMessageBox.about(
                    self,
                    "Erreur".upper(),
                    "Format de graphique non-compatible avec plusieurs dates",
                )
                print("> Hist.")
                self.toolwidgetmain.comboBoxGraphType.setCurrentIndex(1)
                # self.df.plot(kind='bar', ax=self.axtype, color=colorsDF)
                self.df.plot(kind="bar", ax=self.axtype)

        self.figuretype.canvas.draw()
        buf = io.BytesIO()
        self.figuretype.savefig(buf)
        buf.seek(0)
        pix = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(buf.getvalue()))
        self.graphwdg.setPixmap(pix)

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def updateGUI(self):
        """
        Fetch and clean data, calculate statistics
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Reset self.currentQuery
        self.currentQuery.clear()

        # Fetch data
        self.getDataFrame()
        print(self.df) if self.isDebug else None

        # Calculate statistics, update labels and tableWidget
        self.sumAvgToLabel()
        self.denumToLabel()
        self.dataFrameToTableWidget()

        # Plot graph
        self.plotGraph()

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def allowPieChart(self):
        """
        Disable pie chart when lineEditDates is filled
        :return: bool, True if pie chart is allowed, False otherwise
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Disable pie chart on Advanced tab with lineEditDates filled
        if (
            self.toolwidgetmain.tabResearch.currentIndex() == 1
            and self.toolwidgetmain.lineEditDates.text() != ""
        ):
            print(
                "Exit {fct}".format(fct=inspect.stack()[0][3])
            ) if self.isDebug else None
            return False
        else:
            print(
                "Exit {fct}".format(fct=inspect.stack()[0][3])
            ) if self.isDebug else None
            return True

    # ----- FILE MANAGEMENT -----
    def createNewTextFile(self):
        """
        Create new empty text file
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        newQuery = {
            "query": "",
            "graphType": "",
            "dates": "",
            "colorsDF": {},
            "colorsDFT": {},
        }

        # Ask query's name
        fileName = self.getName()

        # Cancel saving
        if fileName is None or fileName == "":
            return

        # Save query options
        directory = (
            self.dbase.dbaseressourcesdirectory + "/config/statsTools/" + fileName
        )

        # Creates file and writes queryDict as json
        with open(directory, "w") as file:
            json.dump(newQuery, file)

        # Fill queries list comboBox
        self.updatesQueriesList()

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def getName(self):
        text, ok = QInputDialog.getText(
            self, "Créer une nouvelle requête", "Nom du fichier"
        )
        if ok:
            return str(text + ".txt")
        return None

    def updatesQueriesList(self):
        """
        Updates comboBoxSavedQueries with new/removed files
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        self.disconnectComboSavedQueries()
        self.disconnectComboSavedQueries()

        # Fetches files from directory
        queriesList = self.listFiles(
            self.dbase.dbaseressourcesdirectory + "/config/statsTools"
        )
        print(">", queriesList) if self.isDebug else None

        # Clear and add files to comboBox
        self.toolwidgetmain.comboBoxSavedQueries.clear()
        self.toolwidgetmain.comboBoxSavedQueries.addItems(queriesList)

        self.connectComboSavedQueries()

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def listFiles(self, myPath):
        """
        Fetches all files within a specified directory
        :param myPath: str, path within which files should be saved
        :return: list, files within path
        """
        if os.path.isdir(myPath):
            return [
                f for f in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, f))
            ]
        else:
            return []

    def modifyTextFile(self):
        """
        Save current query at current comboBoxSavedQueries item
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Get data
        newQuery = {
            "query": self.toolwidgetmain.lineEditQuery.text(),
            "graphType": self.toolwidgetmain.comboBoxGraphType.currentText(),
            "dates": self.toolwidgetmain.lineEditDates.text(),
            "colorsDF": self.colorsDF,
            "colorsDFT": self.colorsDFT,
        }

        # Retrieve query's name
        fileName = self.toolwidgetmain.comboBoxSavedQueries.currentText()
        # Fetch complete path
        directory = (
            self.dbase.dbaseressourcesdirectory + "/config/statsTools/" + fileName
        )

        # Creates file and writes queryDict as json
        with open(directory, "w") as file:
            json.dump(newQuery, file)

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def loadTextFile(self):
        """
        Load text file and update labels and comboBox
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Retrieve query's name
        fileName = self.toolwidgetmain.comboBoxSavedQueries.currentText()
        # Save query options
        completePath = (
            self.dbase.dbaseressourcesdirectory + "/config/statsTools/" + fileName
        )

        # Creates file and writes queryDict as json
        with open(completePath, "r") as file:
            print("> Enter openFile")
            self.currentQuery.clear()
            self.currentQuery = json.load(file)
            pprint.pprint(self.currentQuery)

            # Update lineEdits and comboBox accordingly
            self.applyChanges(self.currentQuery)
            print("> Exit openFile")

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def applyChanges(self, loadedQuery):
        """
        Applies changes to lineEdit and comboBox
        :loadedQuery: dict, saved query and options
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        self.toolwidgetmain.lineEditQuery.setText(loadedQuery["query"])
        self.toolwidgetmain.comboBoxGraphType.setCurrentText(loadedQuery["graphType"])
        self.toolwidgetmain.lineEditDates.setText(loadedQuery["dates"])
        # self.getSavedColors()

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def deleteTextFile(self):
        """
        Check whether two queries' data are the same or not
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Query has not been modified
        if self.confirm():
            # Retrieve query's name
            fileName = self.toolwidgetmain.comboBoxSavedQueries.currentText()
            # Fetch complete path
            directory = (
                self.dbase.dbaseressourcesdirectory + "/config/statsTools/" + fileName
            )
            # Delete file
            os.remove(directory)

        # Update queries list comboBox and set index to first item
        self.updatesQueriesList()
        self.toolwidgetmain.comboBoxSavedQueries.setCurrentIndex(0)

        print("Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def confirm(self):
        """
        Confirmation pop-up with pre-filled title and text
        :return: bool, True if accepted, False otherwise
        """
        print("Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        confirm = QMessageBox.question(
            self,
            "Suppression",
            "Confirmez-vous la suppression de la requête?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if confirm == QMessageBox.Yes:
            print(
                "Enter {fct}".format(fct=inspect.stack()[0][3])
            ) if self.isDebug else None
            return True
        else:
            print(
                "Enter {fct}".format(fct=inspect.stack()[0][3])
            ) if self.isDebug else None
            return False

    # ---------- WRITE QUERY ----------
    def writeQuery(self):
        """
        Write data to query for potential future save
        :return: True if data are written, False otherwise
        """
        print("Enter writeQuery")
        try:
            self.queryToSave["query"] = self.toolwidgetmain.lineEditQuery.text()
            self.queryToSave[
                "graphType"
            ] = self.toolwidgetmain.comboBoxGraphType.currentText()
            self.queryToSave["dates"] = self.toolwidgetmain.lineEditDates.text()

            print("Exit writeQuery")
            return True
        except AttributeError as e:
            print(
                "{type}: {exception} raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), exception=e, fct="writeQuery"
                )
            )
            return False
        except:
            print(
                "{type}: raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), fct="writeQuery"
                )
            )
            return False

    def updateStats(self):
        """
        Updates Sum, average and denum labels/graph
        """

        print("\n\n========== NEW UPDATE ==========")
        print("Enter updateStats")
        # Fetch data
        # self.result = self.getData()
        self.updateGUI()
        print(self.df)

        # Update display if self.result is not empty and not None
        """if self.result is not None and len(self.result) > 0:

            # Clean data
            self.resultClean = self.cleanData(self.result, 0)

            # Dict of items' occurrences
            self.counter = Counter(self.resultClean)

            pprint.pprint(self.counter)

            # Colors
            # Random colors for Classique Tab (Tab index: 0)
            # if self.toolwidgetmain.tabResearch.currentIndex() == 0:
            if not self.hasColor:
                print("Does not have color")
                self.queryToSave.clear()

                for key in self.counter.keys():
                    self.queryToSave[key] = ""
                self.setDefaultColor()

            # Update labels and details
            self.updateSumAvg(self.resultClean)
            self.updateDetails(self.counter)
            self.updateMaxOccurence(self.counter)

            if self.toolwidgetmain.lineEditDates.text() == "":
                self.drawGraph()

        # Pop-up if request is valid but self.result is empty
        elif len(self.result) == 0 and self.validQuery:
            QMessageBox.about(self, "Erreur".upper(), "Aucune donnée trouvée")"""

        print("Exit updateStats")

    # ---------- GRAPH ----------
    def drawGraph(self):
        """
        Plot value from self.dataframe on a specified chart type and color
        """

        print("Enter drawGraph")
        print(self.dataFrame)
        self.dataFrame.plot(kind="bar", ax=self.axtype, stacked=True)
        self.figuretype.canvas.draw()
        buf = io.BytesIO()
        self.figuretype.savefig(buf)
        buf.seek(0)
        pix = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(buf.getvalue()))
        self.graphwdg.setPixmap(pix)

    # ---------- GRAPH ----------
    def drawGraph2(self):
        """
        Plot value from self.counter on a specified chart type and color
        """

        print("Enter drawGraph")

        # TODO: check load
        if not self.hasColor:
            print(self.queryToSave)
            self.setDefaultColor()
            print(self.queryToSave)

        # Reset figure and add axe
        try:
            self.figuretype.clf()
            self.axtype = self.figuretype.add_subplot(111)
        except (AttributeError, StopIteration) as e:
            print(
                "{type}: {exception} raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), exception=e, fct="drawGraph"
                )
            )
        except:
            print(
                "{type}: raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), fct="drawGraph"
                )
            )

        # Init graph's lists
        labels = list()
        sizes = list()
        colors = list()

        # Extract data to graph's lists
        try:
            data = self.extractData()
            labels = data[0]
            sizes = data[1]
            colors = self.getSavedColors()
            print(labels)
            print(sizes)
            print(colors)

            # Update chart type in self.queryToSave
            self.writeQuery()

        except (AttributeError, TypeError) as e:
            QMessageBox.about(self, "Erreur".upper(), "Aucune donnée trouvée")
            print(
                "{type}: {exception} raised at {fct}".format(
                    type=sys.exc_info()[0].upper(),
                    exception=e,
                    fct="drawGraph > dict(self.counter)",
                )
            )
            pass
        except:
            print(
                "{type}: raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), fct="drawGraph > dict(self.counter)"
                )
            )
            pass

        # Plot data per specified chart type and colors
        currentChartType = self.toolwidgetmain.comboBoxGraphType.currentText()
        try:
            # ----- Histogram -----
            if currentChartType == "Hist.":
                self.axtype.bar(labels, sizes, color=colors)

            # ----- Cumulative histogram -----
            elif currentChartType == "Hist. cum.":
                # bins: exemple age: [0, 5, 20, 100]
                # Plot value from data on top of each other
                height = 0
                for key, value in enumerate(sizes):
                    self.axtype.bar(
                        0,
                        value,
                        bottom=height,
                        edgecolor="white",
                        width=1,
                        color=colors[key],
                    )
                    height += value

            # ----- Pie chart -----
            elif currentChartType == "Camembert":
                self.axtype.pie(
                    sizes, labels=labels, autopct="%.0f%%", startangle=90, colors=colors
                )

            # ----- Scatter plot -----
            elif currentChartType == "Nuage":
                # Scatter plot requests colors' length to be of sizes'
                colors = colors[: len(sizes)]
                self.axtype.scatter(sizes, labels, color=colors)

        except (AttributeError, IndexError, TypeError, ValueError, StopIteration) as e:
            print(
                "{type}: {exception} raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), exception=e, fct="drawGraph"
                )
            )
            pass
        except:
            print(
                "{type}: raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), fct="drawGraph"
                )
            )

        self.figuretype.canvas.draw()
        buf = io.BytesIO()
        self.figuretype.savefig(buf)
        buf.seek(0)
        pix = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(buf.getvalue()))
        self.graphwdg.setPixmap(pix)

        # Reset self.hasColor
        self.hasColor = False

        print("Exit drawGraph")

    def setDefaultColor(self):
        """
        Set random colors to graph
        """
        print("Enter setDefaultColor")

        for key in self.queryToSave.keys():
            if self.queryToSave[key] == "" and key != "dates":
                newColor = "#%02X%02X%02X" % (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
                self.queryToSave[key] = "{color}".format(color=newColor)

        print("Exit setDefaultColor")

    def extractData(self):
        """
        Extract data from self.counter
        :return: tuple containing labels, sizes and colors
        """

        print("Enter extractData")

        data = dict(self.counter)
        labels = list(data.keys())
        sizes = list(data.values())
        colors = self.getSavedColors()

        print("Exit extractData")
        return labels, sizes, colors

    def getSavedColors(self):
        """
        Fetch colors from self.queryToSave
        :return: list of str, name of colors
        """
        colors = []
        for element in self.queryToSave.values():
            if element.startswith("#"):
                colors.append(element)
        return colors

    def getData(self):
        """
        Fetches data given SQL query
        :return: List of tuples
        """

        print("Enter getData")

        # TODO: bool, load FALSE
        self.hasColor = False
        sql = str()
        # Detects which button is called
        sender = self.sender()

        # ----- CLASSIQUE -----
        # Create SQL query from table and field comboBox
        if sender.objectName() == "pushButtonExecute":
            # selectFrom = "SELECT {slct} FROM {frm}".format(slct=self.toolwidgetmain.comboBoxField.currentText(), frm=self.toolwidgetmain.comboBoxTable.currentText() + "_now")
            selectFrom = "SELECT {slct} FROM {frm}_now".format(
                slct=self.toolwidgetmain.comboBoxField.currentText(),
                frm=self.toolwidgetmain.comboBoxTable.currentText(),
            )
            try:

                sql = self.dbase.updateQueryTableNow(selectFrom)
            except AttributeError as e:
                print(
                    "{type}: {exception} raised at {fct}".format(
                        type=sys.exc_info()[0].upper(),
                        exception=e,
                        fct="getData > updateQueryTableNow",
                    )
                )
            except:
                print(
                    "{type}: raised at {fct}".format(
                        type=sys.exc_info()[0].upper(),
                        fct="getData > updateQueryTableNow",
                    )
                )

        # ----- ADVANCED -----
        # Fetch SQL query from lineEditQuery
        else:
            self.validQuery = self.checkText()
            if self.validQuery:
                selectFrom = self.toolwidgetmain.lineEditQuery.text() + "_now"

                # Updates self.queryToSave with current query
                self.writeQuery()

                # Date lineEdit is filled: fetch dated data
                if self.toolwidgetmain.lineEditDates.text() != "":
                    # Extract dates from lineEditDates and add today's date
                    self.dates = self.toolwidgetmain.lineEditDates.text().split(", ")
                    self.dates.append(datetime.date.today().strftime("%d/%m/%Y"))

                    # Reset self.dictGraphs and fill in with len(self.dates) lists
                    self.dictGraphs.clear()
                    self.dictGraphs = {k: {} for k in self.dates}

                    for date in self.dates:
                        sql = self.dbase.updateQueryTableNow(selectFrom, date)
                        # Query DB, clean results and add to self.dictGraphs with date as key
                        self.dictGraphs[date] = dict(
                            Counter(self.cleanData(self.dbase.query(sql), 0))
                        )

                    # Reset and fill in self.dataFrame
                    self.dataFrame = pd.DataFrame(self.dictGraphs)
                    # print(self.dataFrame)

                    # A DEPLACER DANS drawGraph()
                    # self.dataFrame.plot(kind='bar', ax=self.axtype, stacked=True)
                    try:
                        """
                        # self.dataFrame.plot(kind="bar", stacked=True)
                        # print(self.dataFrame[self.dates[0]].tolist())
                        # plt.figure()
                        # graphData.plot()
                        # plt.show()

                        pos = np.arange(len(self.dates))
                        scores = []
                        currentAdd = 0
                        for key, date in enumerate(self.dates):
                            print(self.dataFrame[date].tolist())
                            currentAdd = np.add(currentAdd, scores[key])
                            scores.append(np.array(self.dataFrame[date].tolist()))
                            # self.axtype.bar(pos, currentAdd)
                            # self.axtype.bar(self.dates, list(map(float, scores[key])), align='edge', width=-0.4)

                        # self.axtype.bar(0, value, bottom=height, edgecolor="white", width=1, color=colors[key])
                        # self.axtype.bar(self.dataFrame[self.dates[0]].tolist(), height=[5, 5, 5], stacked=True)
                        # ########### NE FONCTIONNE PAS
                        # self.axtype.bar(labels, sizes, color=colors)
                        # self.axtype.set_canvas(self.dataFrame.loc[:, colNames].plot.bar(stacked=True))
                        # self.axtype.show()
                        """
                        print("Dessin multi-graph")
                    except (
                        AttributeError,
                        IndexError,
                        KeyError,
                        TypeError,
                        ValueError,
                    ) as e:
                        print(
                            "{type}: {exception} raised at {fct}".format(
                                type=sys.exc_info()[0].upper(),
                                exception=e,
                                fct="getData > plt.show()",
                            )
                        )
                    except:
                        print(
                            "{type}: raised at {fct}".format(
                                type=sys.exc_info()[0].upper(),
                                fct="getData > plt.show()",
                            )
                        )

                # Date lineEdit is not filled: fetch current data
                else:
                    sql = self.dbase.updateQueryTableNow(selectFrom)

        print(selectFrom)
        print(sql)
        try:
            print("Exit getData")
            return self.dbase.query(sql)
        except UnboundLocalError as e:
            print(
                "{type}: {exception} raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), exception=e, fct="getData"
                )
            )
            return []
        except:
            print(
                "{type}: raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), fct="getData"
                )
            )
            return []

    def updateSumAvg(self, lstItems):
        """
        Updates sum and average labels given a list of elements
        :param lstItems: list of elements
        """

        print("Enter updateSumAvg")
        try:
            self.toolwidgetmain.labelSum.setText(str(sum(lstItems)))
            self.toolwidgetmain.labelAvg.setText(
                str(round(statistics.mean(lstItems), 2))
            )
            print("Exit updateSumAvg")
        except TypeError:
            self.toolwidgetmain.labelSum.setText("-")
            self.toolwidgetmain.labelAvg.setText("-")

    def updateDetails(self, counter):
        """
        Update details tab with current data
        :param counter: Dict of items' occurrences
        """

        print("Enter updateDetails")
        # Reset table widget
        self.toolwidgetmain.tableWidgetDetails.setRowCount(0)
        header = self.toolwidgetmain.tableWidgetDetails.horizontalHeader()

        # On Classique or on (Advanced and lineEditDates is empty)
        if self.toolwidgetmain.tabResearch.currentIndex() == 0 or (
            self.toolwidgetmain.tabResearch.currentIndex() == 1
            and self.toolwidgetmain.lineEditDates.text() == ""
        ):
            print("> On Classique or on (Advanced and lineEditDates is empty)")
            print(self.queryToSave)
            try:
                self.toolwidgetmain.tableWidgetDetails.setColumnCount(3)
                self.toolwidgetmain.tableWidgetDetails.setRowCount(len(counter))

                # Fill tableWidget with elements from counter
                print("> Enter loop: create detailed tab")
                for row, key in enumerate(counter.keys()):
                    self.toolwidgetmain.tableWidgetDetails.setItem(
                        row, 0, QTableWidgetItem(str(key))
                    )
                    self.toolwidgetmain.tableWidgetDetails.setItem(
                        row, 1, QTableWidgetItem(str(counter[key]))
                    )

                    # Color dialog
                    button = QPushButton("", self)
                    self.toolwidgetmain.tableWidgetDetails.setCellWidget(row, 2, button)
                    button.clicked.connect(partial(self.openColorDialog, key))

                    try:
                        print("> Enter Try pushButtonColor")
                        # Push button background color to match key color
                        color = self.queryToSave[key]
                        button.setStyleSheet(
                            "background-color: {color}".format(color=color)
                        )
                    except Exception as e:
                        print("updateDetails Error:", e)
                    print("> Exit Try pushButtonColor")

                print("> Exit loop: create detailed tab")

                # Adapt display to content
                header.setSectionResizeMode(0, QHeaderView.Stretch)
                header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
                header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
                self.renameHeaders([datetime.date.today().strftime("%d/%m/%Y")])
            except (KeyError, TypeError) as e:
                print(
                    "{type}: {exception} raised at {fct}".format(
                        type=sys.exc_info()[0].upper(), exception=e, fct="updateDetails"
                    )
                )
                pass
            except:
                print(
                    "{type}: raised at {fct}".format(
                        type=sys.exc_info()[0].upper(), fct="updateDetails"
                    )
                )
                pass

        # On Advanced and lineEditDates is not empty
        else:
            print("> On Advanced and lineEditDates is not empty")
            # Columns and rows names
            colNames = list(self.dataFrame.columns.values)
            rowNames = list(self.dataFrame.index.values)
            # Set column's number to len(colNames) + 2 (Name, color) and row's number to len(rowNames)
            self.toolwidgetmain.tableWidgetDetails.setColumnCount(len(colNames) + 2)
            self.toolwidgetmain.tableWidgetDetails.setRowCount(len(rowNames))

            # Fill tableWidget with elements from self.dataFrame
            for row in range(len(rowNames)):
                # Insert row name
                self.toolwidgetmain.tableWidgetDetails.setItem(
                    row, 0, QTableWidgetItem(str(rowNames[row]))
                )

                # Insert row values for each date
                for col in range(len(colNames)):
                    valueTmp = self.dataFrame.iat[row, col]
                    self.toolwidgetmain.tableWidgetDetails.setItem(
                        row, col + 1, QTableWidgetItem(str(valueTmp))
                    )
                    # Resize column
                    header.setSectionResizeMode(col + 1, QHeaderView.ResizeToContents)

                # Create colorPushButton
                self.createColorPushButton(row, len(colNames) + 1, str(rowNames[row]))

                # Resize column
                header.setSectionResizeMode(
                    len(colNames) + 1, QHeaderView.ResizeToContents
                )

                # Rename headers
                self.renameHeaders(colNames)

        print("Exit updateDetails")

    def openColorDialog(self, key):
        """
        Open a colorDialog and return chosen color
        :return: str, name of the color
        """

        print("Enter openColorDialog")

        color = QColorDialog.getColor()

        if color.isValid():
            self.queryToSave[key] = color.name()

            # Push button background color to math key color
            sender = self.sender()
            try:
                sender.setStyleSheet(
                    "background-color: {color}".format(color=color.name())
                )
            except Exception as e:
                print("openColorDialog Error:", e)

            # Update graph after color selection
            if self.toolwidgetmain.lineEditDates.text() == "":
                # self.drawGraph()
                print(
                    "> {key}: Color changed to {color}".format(
                        key=key, color=color.name()
                    )
                )

        print("Exit openColorDialog")

    def updateMaxOccurence(self, counter):
        """
        Update max occurrence label
        :param counter: Dict of items' occurrences
        """

        print("Enter updateMaxOccurence")

        try:
            # Retrieves first most common element from counter
            maxi = self.findMax(counter)
            if maxi[0] in self.abbv.keys():
                text = "{name}: {count}".format(name=self.abbv[maxi[0]], count=maxi[1])
            else:
                text = "{name}: {count}".format(name=maxi[0], count=maxi[1])
            self.toolwidgetmain.labelOcc.setText(text)
        except IndexError as e:
            print(
                "{type}: {exception} raised at {fct}".format(
                    type=sys.exc_info()[0].upper(),
                    exception=e,
                    fct="updateMaxOccurence",
                )
            )
        except:
            print(
                "{type}: raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), fct="updateMaxOccurence"
                )
            )

        print("Exit updateMaxOccurence")

    # ---------- LOAD QUERY ----------
    def loadQuery(self):
        """
        Load query and affects lineEdit and comboBox
        """

        print("Enter loadQuery")

        # TODO: bool, load -> True
        # Existing colors to be used
        self.hasColor = True

        self.queryToSave.clear()
        # Load file and parse it from JSON to dict
        print("***", self.toolwidgetmain.comboBoxSavedQueries.currentText())
        fileName = self.toolwidgetmain.comboBoxSavedQueries.currentText()
        print(fileName)
        self.loadedQueryPath = os.path.join(
            self.dbase.dbaseressourcesdirectory, "config", "statsTools", fileName
        )
        print(self.loadedQueryPath)

        with open(self.loadedQueryPath, "r") as file:
            print("> Enter openFile")
            # self.loadedQueryPath = fileCompletePath
            self.queryToSave = json.load(file)
            # self.applyChanges()
            print("> Exit openFile")

        if False:
            try:
                self.queryToSave.clear()
                # Load file and parse it from JSON to dict
                fileName = self.toolwidgetmain.comboBoxSavedQueries.currentText()
                print(fileName)
                # fileCompletePath = self.dbase.dbaseressourcesdirectory + "/config/statsTools/" + fileName
                fileCompletePath = os.path.join(
                    self.dbase.dbaseressourcesdirectory,
                    "config",
                    "statsTools",
                    fileName,
                )
                print(fileCompletePath)
                with open(fileCompletePath, "r") as file:
                    print("> Enter openFile")
                    self.loadedQueryPath = fileCompletePath
                    self.queryToSave = json.load(file)
                    # self.applyChanges()
                    print("> Exit openFile")
            except (FileNotFoundError, KeyError, PermissionError) as e:
                print(
                    "{type}: {exception} raised at {fct}".format(
                        type=sys.exc_info()[0].upper(), exception=e, fct="loadQuery"
                    )
                )
                self.queryToSave = {}
            except Exception as e:
                print("loadQuery Error:", e)
                # print("{type}: raised at {fct}".format(type=sys.exc_info()[0].upper(), fct="loadQuery"))

        print("Exit loadQuery")

    # ---------- SAVE QUERY ----------
    def saveQuery(self):
        """
        Saves query and options as txt file
        """
        print("Enter saveQuery")
        try:
            # Retrieves data
            if True:
                fileName = self.getName()

                # Cancel saving
                if fileName is None or fileName == "":
                    return

                # Save query options
                directory = (
                    self.dbase.dbaseressourcesdirectory
                    + "/config/statsTools/"
                    + fileName
                )
                # Creates file and writes queryDict as json
                with open(directory, "w") as file:
                    json.dump(self.queryToSave, file)

                # Fill queries list comboBox
                self.updatesQueriesList()

                print("Exit saveQuery")
        except IOError:
            print(">>> UNSUCCESSFUL - QUERY NOT SAVED")
        except:
            print(
                "{type}: raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), fct="saveQuery"
                )
            )

    # ---------- MODIFY QUERY ----------
    def modifySavedQuery(self):
        """
        Updates current queries with self.queryToSave
        """
        try:
            # Retrieves data
            if self.modifyLoadedQuery():
                # Creates file and writes queryDict as json
                with open(self.loadedQueryPath, "w") as file:
                    json.dump(self.queryToSave, file)
        except IOError:
            print(">>> UNSUCCESSFUL - QUERY NOT SAVED")
        except:
            print(
                "{type}: raised at {fct}".format(
                    type=sys.exc_info()[0].upper(), fct="modifySavedQuery"
                )
            )
            return False

    def modifyLoadedQuery(self):
        """
        Updates self.queryToSave with current lineEdit and comboBox values
        """
        print("Enter modifyLoadedQuery")
        self.validQuery = self.checkText()
        if self.validQuery and self.result is not None:
            # Write data to query
            self.writeQuery()

            print("Exit modifyLoadedQuery")
            return True
        return False

    def confirmDetailled(self, title, text):
        """
        Confirmation pop-up with custom title and text
        :return: bool, True if accepted, False otherwise
        """
        confirm = QMessageBox.question(
            self, title, text, QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            return True
        else:
            return False

    def findMax(self, counter):
        """
        Get most commun element from counter
        :param counter: dict of denum
        :return: tuple, most commun element and its occurrence
        """
        maxOcc = counter.most_common(1)
        return maxOcc[0][0], maxOcc[0][1]


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)

        # Charge le widget associé
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_stat_ui.ui")
        uic.loadUi(uipath, self)

        class ObservationUserUI(QWidget):
            def __init__(self, parent=None):
                super(ObservationUserUI, self).__init__(parent=parent)
                path = os.path.join(
                    os.path.dirname(__file__),
                    "synthesedesordre",
                    "ObservationSyntheseToolUser.ui",
                )
                uic.loadUi(path, self)


class Label(QLabel):
    def __init__(self, img=None):
        super(Label, self).__init__()
        self.setFrameStyle(QFrame.StyledPanel)
        self.pixmap = QtGui.QPixmap(img)

    def paintEvent(self, event):
        size = self.size()
        painter = QtGui.QPainter(self)
        point = QtCore.QPoint(0, 0)
        if not self.pixmap.isNull():
            scaledPix = self.pixmap.scaled(
                size,
                QtCore.Qt.KeepAspectRatio,
                transformMode=QtCore.Qt.SmoothTransformation,
            )
            # start painting the label from left upper corner
            point.setX((size.width() - scaledPix.width()) / 2)
            point.setY((size.height() - scaledPix.height()) / 2)
            painter.drawPixmap(point, scaledPix)

    def setPixmap(self, img):
        self.pixmap = QtGui.QPixmap(img)
        self.repaint()

    def clear(self):
        self.pixmap = QtGui.QPixmap()
        self.repaint()
