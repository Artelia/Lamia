# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui, QtWidgets
import os, sys
import qgis.core, qgis.utils
import logging, datetime, time, shutil

from qgis.PyQt.QtWidgets import (
    QWidget,
    QDialog,
    QMainWindow,
    QApplication,
    QTreeWidgetItem,
    QMenu,
    QSpinBox,
    QDoubleSpinBox,
    QHeaderView,
    QLineEdit,
    QTextBrowser,
    QTreeWidgetItemIterator,
    QComboBox,
    QLabel,
    QInputDialog,
    QPushButton,
    QToolButton,
    QStatusBar,
)

# Import custom button
from .qToolButtonPlus import QPushButtonPlus

# from ....main.DBaseParser import DBaseParser
import Lamia
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

import pandas as pd
from pprint import pprint
import json, re
import inspect
import numpy as np


class AMCWindow(QDialog):
    # def __init__(self, parent=None, dbase=None, jsonpath=None, mcacore=None):
    def __init__(
        self, parent=None, dbase=None, confname=None, mcacore=None, qgiscanvas=None
    ):
        super(AMCWindow, self).__init__(parent=parent)

        uipath = os.path.join(os.path.dirname(__file__), "amcwindow_ui.ui")
        uic.loadUi(uipath, self)

        # * DEBUG
        self.isDebug = False

        # * init part
        self.dbase = dbase
        self.mcacore = mcacore
        self.dict = {}
        self.confname = confname
        self.jsonPath = self.mcacore.getConfFilePath(confname)
        self.qgiscanvas = qgiscanvas

        # * ui conf
        self.treeWidget.setColumnCount(5)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.openMenu)

        self.maintreewdgitem = QTreeWidgetItem(
            self.treeWidget.invisibleRootItem(), ["note"]
        )
        # Visualisation
        buttonVisualisation = QPushButton()
        self.treeWidget.setItemWidget(self.maintreewdgitem, 5, buttonVisualisation)
        buttonVisualisation.setProperty("widgetitem", self.maintreewdgitem)
        buttonVisualisation.clicked.connect(self.visualisationPressed)

        headerlist = ["Criteria", "Select", "Bareme", "Type", "Value", "Vis."]
        self.treeWidget.setHeaderItem(QTreeWidgetItem(headerlist))

        self.treeWidget.header().setStretchLastSection(False)
        self.treeWidget.header().resizeSection(1, 125)
        self.treeWidget.header().resizeSection(2, 75)
        self.treeWidget.header().resizeSection(3, 125)
        self.treeWidget.header().resizeSection(4, 100)
        self.treeWidget.header().resizeSection(5, 75)
        self.treeWidget.header().setResizeMode(0, QHeaderView.Stretch)

        self.treeWidget.itemDoubleClicked.connect(self.itemdoubleclicked)
        self.treeWidget.itemChanged.connect(self.treeitemChanged)

        # Right click on criteria
        self.menu = QMenu()
        self.menu.addAction(self.tr("Add criteria"))
        self.menu.addAction(self.tr("Remove criteria"))
        self.menu.triggered.connect(self.menuAction)

        # Click on Test SQL
        # self.toolButton_testsql.clicked.connect(self.testSQL)
        self.dbtested = False
        self.menuitem = None
        self.itemnameediting = None

        if qgis.utils.iface is None:
            self.menuitem = self.maintreewdgitem
            # self.lineEdit_sqlfinal.setText("FROM #lamia.noeud INNER JOIN #lamia.descriptionsystem ON descriptionsystem.pk_descriptionsystem = noeud.lpk_descriptionsystem")
            self.textBrowser_sqlfinal.setPlainText(
                "FROM #lamia.node INNER JOIN #lamia.descriptionsystem ON descriptionsystem.pk_descriptionsystem = node.lpk_descriptionsystem"
            )

        # * Load json file
        self.mcacore.mcavirtualayerFactory.setConfName(self.confname)
        if self.jsonPath is not None and os.stat(self.jsonPath).st_size > 0:
            self.jsonToTreeWidget()

        # Results
        self.df = None  # the mainsql request result
        self.route = []
        self.result = pd.DataFrame()  # the mainsql request processed with bareme
        self.starttime = None

        # Click on save
        self.pushButton_save.clicked.connect(self.saveClicked)
        self.toolButton_updatedb.clicked.connect(self.createDataFrame)
        self.toolButton_testdb.clicked.connect(self.testDB)
        self.toolButton_stop.clicked.connect(self.stopThread)

        # jsonname = os.path.basename(os.path.splitext(self.jsonPath)[0])
        # self.filevirtuallayer = os.path.join(
        #     self.dbase.dbaseressourcesdirectory,
        #     "config",
        #     "amctools",
        #     jsonname + ".sqlite",
        # )
        # self.filevirtuallayer = self.mcacore.getSqliteFileFromConf(self.confname)

        # virtual layer process
        # self.createdataframe = MCAVirtualLayer(
        #     mcacore=self.mcacore, confname=self.confname
        # )
        # self.createdataframe = self.mcacore.mcavirtualayerFactory
        # self.thread = QtCore.QThread()
        # self.createdataframe.moveToThread(self.thread)
        # self.createdataframe.finished.connect(self.postVLayerProcessed)
        # self.createdataframe.finished.connect(self.thread.quit)
        # self.createdataframe.dbasestatus.connect(self.showStatus)
        # self.createdataframe.message.connect(self.appendMessage)
        # self.thread.started.connect(self.createdataframe.processVLayer)

        # inform about status
        # self.createdataframe.filename = self.filevirtuallayer
        # self.createdataframe.projectcrs = self.dbase.crsnumber

        # self.toolButton_updatedb.setEnabled(False)
        self.treeWidget.expandAll()
        self.textBrowser_sqlfinal.textChanged.connect(self.updateUiWithDbStatus)
        self.updateUiWithDbStatus()

    def ________________uiBehaviour(self):
        pass

    def treeitemChanged(self, itemchanged, column):
        self.treeWidget.closePersistentEditor(self.itemnameediting, 0)
        self.itemnameediting = None

    def itemdoubleclicked(self, itemclicked):
        # print(itemclicked.text(0))
        if itemclicked == self.maintreewdgitem:
            return
        self.itemnameediting = itemclicked
        self.treeWidget.openPersistentEditor(itemclicked, 0)

    # +--------------------------------------------+
    # |---------- CREATE QTREEWIDGETITEM ----------|
    # +--------------------------------------------+

    def openMenu(self, position):
        self.menuitem = self.treeWidget.currentItem()
        self.menu.exec_(self.treeWidget.viewport().mapToGlobal(position))

    def menuAction(self, actionname):
        # Add new item
        # if hasattr(self, "createdataframe"):
        #     self.createdataframe.setStatus("False")
        # else:
        #     self.createdataframe2.setStatus("False")
        self.mcacore.mcavirtualayerFactory.setStatus("False")

        if actionname.text() == self.tr("Add criteria"):

            # Create empty item from parent item
            qtreewidgetitm = QTreeWidgetItem(self.menuitem, ["New criteria"])

            # Add widgets to new item
            self.widgetsToNewItem(qtreewidgetitm)

            # Disable QLineEdit and QPushButtonPlus
            """if qtreewidgetitm.parent() != self.maintreewdgitem:
                selectWidget = self.treeWidget.itemWidget(qtreewidgetitm.parent(), 1)
                selectWidget.setStyleSheet("QLineEdit { background-color : gray; }")
                selectWidget.setReadOnly(True)

                baremeButton = self.treeWidget.itemWidget(qtreewidgetitm.parent(), 2)
                baremeButton.setEnabled(False)"""
            self.blockNode(qtreewidgetitm)

            return qtreewidgetitm

        # Delete current row
        elif actionname.text() == self.tr("Remove criteria"):

            # Enable QLineEdit and QPushButtonPlus
            """if self.menuitem.parent().childCount() <= 1 and self.menuitem.parent() != self.maintreewdgitem:
                selectWidget = self.treeWidget.itemWidget(self.menuitem.parent(), 1)
                selectWidget.setStyleSheet("QLineEdit { background-color : white; }")
                selectWidget.setReadOnly(False)

                baremeButton = self.treeWidget.itemWidget(self.menuitem.parent(), 2)
                baremeButton.setEnabled(True)"""
            self.unblockNode()

            self.menuitem.parent().removeChild(self.menuitem)

    def blockNode(self, node):
        """
        Disable QLineEdit and QPushButtonPlus
        :param node: qtreewidgetitm
        """
        if node.parent() != self.maintreewdgitem:
            selectWidget = self.treeWidget.itemWidget(node.parent(), 1)
            selectWidget.setStyleSheet("QLineEdit { background-color : gray; }")
            selectWidget.setReadOnly(True)

            baremeButton = self.treeWidget.itemWidget(node.parent(), 2)
            baremeButton.setEnabled(False)

    def unblockNode(self):
        """
        Enable QLineEdit and QPushButtonPlus
        """
        if (
            self.menuitem.parent().childCount() <= 1
            and self.menuitem.parent() != self.maintreewdgitem
        ):
            selectWidget = self.treeWidget.itemWidget(self.menuitem.parent(), 1)
            selectWidget.setStyleSheet("QLineEdit { background-color : white; }")
            selectWidget.setReadOnly(False)

            baremeButton = self.treeWidget.itemWidget(self.menuitem.parent(), 2)
            baremeButton.setEnabled(True)

    def widgetsToNewItem(self, qtreewidgetitm):
        """
        Add widgets to new item
        :param qtreewidgetitm: qTreeWidgetItem, row where to insert new widgets
        """
        # Select
        lineEditSelect = QLineEdit()
        lineEditSelect.textChanged.connect(self.updateUiWithDbStatus)
        lineEditSelect.setMaximumHeight(25)
        self.treeWidget.setItemWidget(qtreewidgetitm, 1, lineEditSelect)

        # Bareme
        buttonBareme = QPushButtonPlus(self, qtreewidgetitm)
        self.treeWidget.setItemWidget(qtreewidgetitm, 2, buttonBareme)
        buttonBareme.setProperty("widgetitem", qtreewidgetitm)
        # buttonBareme.clicked.connect(lambda: self.baremeButtonPressed(qtreewidgetitm))

        # Type
        qComboBox = QComboBox()
        qComboBox.addItems(["Ponderation", "Classe"])
        self.treeWidget.setItemWidget(qtreewidgetitm, 3, qComboBox)
        qComboBox.currentIndexChanged.connect(
            lambda: self.onComboBoxTypeChanged(qComboBox, qtreewidgetitm)
        )

        # Value
        spinbox = QDoubleSpinBox()
        spinbox.setValue(1.0)
        self.treeWidget.setItemWidget(qtreewidgetitm, 4, spinbox)
        # self.menuitem.setExpanded(True)

        # Visualisation
        buttonVisualisation = QPushButton()
        self.treeWidget.setItemWidget(qtreewidgetitm, 5, buttonVisualisation)
        buttonVisualisation.setProperty("widgetitem", qtreewidgetitm)
        buttonVisualisation.clicked.connect(self.visualisationPressed)

        self.blockNode(qtreewidgetitm)

    def onComboBoxTypeChanged(self, comboBoxType, qtreewidgetitm):
        """
        Change treeWidget fourth column given comboBoxType value
        :param comboBoxType: comboBox, comboBox to test
        :param qtreewidgetitm: qTreeWidgetItem, current selected row
        """
        print(
            "|____ Enter {fct}".format(fct=inspect.stack()[0][3])
        ) if self.isDebug else None

        if comboBoxType.currentText() == "Ponderation":
            # Value
            spinbox = QDoubleSpinBox()
            self.treeWidget.setItemWidget(qtreewidgetitm, 4, spinbox)
            # self.menuitem.setExpanded(True)
        else:
            # Class value
            comboBoxClass = QComboBox()
            comboBoxClass.addItems(["Max", "Min", "Avg"])
            self.treeWidget.setItemWidget(qtreewidgetitm, 4, comboBoxClass)

        # print(
        #     "|____ Exit {fct}".format(fct=inspect.stack()[0][3])
        # ) if self.isDebug else None

    def updateUiWithDbStatus(self):
        jsondict = self.getJsonDict()
        fromup, selectup = self.mcacore.mcavirtualayerFactory.checkVLayerUpdate(
            jsondict
        )
        if fromup and selectup:
            self.toolButton_updatedb.setEnabled(True)
            self.toolButton_testdb.setEnabled(False)
            self.label_rawdbasestate.setText("DB up to date")
            self.label_rawdbasestate.setStyleSheet("QLabel { background-color : green}")
            self._enableordisableQtreeWidgetButtons(boolenable=True)
        else:
            self.dbtested = False
            self.toolButton_updatedb.setEnabled(False)
            self.toolButton_testdb.setEnabled(True)
            self.label_rawdbasestate.setText("DB need to be tested and updated")
            self.label_rawdbasestate.setStyleSheet("QLabel { background-color : red}")
            self._enableordisableQtreeWidgetButtons(boolenable=False)

        # if self.dbtested:
        #     self.toolButton_testdb.setEnabled(True)
        # else:
        #     self.toolButton_testdb.setEnabled(False)

    def _enableordisableQtreeWidgetButtons(self, boolenable=True):

        node = self.treeWidget.invisibleRootItem()
        iterator = QtWidgets.QTreeWidgetItemIterator(self.treeWidget)
        while iterator.value():
            item = iterator.value()
            iterator += 1
            for colidx in range(self.treeWidget.columnCount()):
                if self.treeWidget.itemWidget(
                    item, colidx
                ).__class__.__name__.startswith("QPushButton"):
                    self.treeWidget.itemWidget(item, colidx).setEnabled(boolenable)

    def __________________actions(self):
        pass

    def testDB(self):
        jsondict = self.getJsonDict()
        success, message = self.mcacore.testDB(self.confname, jsondict)
        if success:
            self.toolButton_updatedb.setEnabled(True)
        else:
            self.toolButton_updatedb.setEnabled(False)
        self.appendMessage(message)
        # self.updateUiWithDbStatus()

    def createDataFrame(self):
        res, lay = self.mcacore.createMcaDB(self.confname, self.getJsonDict())
        self.df = res
        self.updateUiWithDbStatus()
        # print(self.df)

    def visualisationPressed(self):
        debug = False

        # if debug:
        #     print("> Visualisation button pressed")

        # Reset self.result
        self.result = pd.DataFrame()

        # Evaluate all entries from selects
        # self.result = self.evaluate()
        # if node is None:
        node = self.treeWidget.currentItem()
        nodeid = self.getNodeId(node)

        self.result = self.mcacore.computeNodeScore(
            self.confname, self.getJsonDict(), nodeid
        )

        self.mcacore.joinResultToQgslayer(self.confname, self.result)

        return

        if debug:
            logging.getLogger("Lamia").debug("sqlsict %s", str(self.result))

        # getpk
        maintable, pkmaintable = self.getMainTable()
        maintablepks = self.df[maintable + "." + pkmaintable]
        qgislayer = self.dbase.dbasetables[maintable.split("_")[0]]["layerqgis"]

        # create memory qgis layer
        self.dbase.templayer = qgis.core.QgsVectorLayer("None", "result", "memory")

        self.dbase.templayer.startEditing()
        provider = self.dbase.templayer.dataProvider()
        provider.addAttributes(
            [
                qgis.core.QgsField("amc_pk", QtCore.QVariant.Double),
                qgis.core.QgsField("amc_val", QtCore.QVariant.Double),
            ]
        )
        self.dbase.templayer.updateFields()

        featstosave = []
        for i, pk in enumerate(maintablepks):
            feat = qgis.core.QgsFeature(self.dbase.templayer.fields())
            feat.setAttributes([pk, float(self.result[i])])
            featstosave.append(feat)
        self.dbase.templayer.addFeatures(featstosave)
        self.dbase.templayer.commitChanges()

        if debug:
            compt = 0
            for elem in self.dbase.templayer.getFeatures():
                compt += 1
                if compt > 10:
                    break
                logging.getLogger("Lamia").debug("sqlsict %s", str(elem.attributes()))

        # perform join
        # first clean
        for join in qgislayer.vectorJoins():
            qgislayer.removeJoin(join)

        joinObject = qgis.core.QgsVectorLayerJoinInfo()
        joinObject.setJoinFieldName("amc_pk")
        joinObject.setTargetFieldName(pkmaintable)
        joinObject.setJoinLayerId(self.dbase.templayer.id())
        joinObject.setUsingMemoryCache(True)
        joinObject.setJoinLayer(self.dbase.templayer)

        self.dbase.dbasetables[maintable.split("_")[0]]["layerqgis"].addJoin(joinObject)

        if debug:
            compt = 0
            for elem in self.dbase.dbasetables[maintable.split("_")[0]][
                "layerqgis"
            ].getFeatures():
                compt += 1
                if compt > 10:
                    break
                logging.getLogger("Lamia").debug(
                    "sqlsict %s %s",
                    str(elem.attributes()[0]),
                    str(elem.attributes()[-1]),
                )

        target_field = "result_amc_val"
        myRangeList = []

        myRenderer = qgis.core.QgsGraduatedSymbolRenderer()
        # symbol
        if qgislayer.geometryType() == qgis.core.QgsWkbTypes.PointGeometry:
            symbol = qgis.core.QgsMarkerSymbol()
            symbol.setSize(0.5)
        elif qgislayer.geometryType() == qgis.core.QgsWkbTypes.LineGeometry:
            symbol = qgis.core.QgsLineSymbol()
            symbol.setWidth(0.5)
        elif qgislayer.geometryType() == qgis.core.QgsWkbTypes.PolygonGeometry:
            symbol = qgis.core.QgsFillSymbol()

        myRenderer.setSourceSymbol(symbol.clone())

        myStyle = qgis.core.QgsStyle().defaultStyle()
        defaultColorRampNames = myStyle.colorRampNames()
        ramp = myStyle.colorRamp("Spectral")
        ramp.invert()

        myRenderer.updateColorRamp(ramp)
        myRenderer.setClassAttribute("result_amc_val")
        if sys.version_info.major == 2:
            myRenderer.updateClasses(qgislayer, myRenderer.EqualInterval, 5)
        elif sys.version_info.major == 3:
            if qgis.core.Qgis.QGIS_VERSION_INT < 31000:
                myRenderer.updateClasses(qgislayer, myRenderer.EqualInterval, 5)
            else:
                myRenderer.setClassificationMethod(
                    qgis.core.QgsClassificationEqualInterval()
                )
                myRenderer.updateClasses(qgislayer, 5)

        qgislayer.setRenderer(myRenderer)
        qgislayer.repaintRequested.emit()

    def saveClicked(self):
        """
        Save file to directory with filename chosen from user
        """

        self.dict.clear()
        # self.dict["mainsql"] = self.textBrowser_sqlfinal.toPlainText()
        # # Fill self.dict
        # self.visitTree(self.maintreewdgitem, self.dict)
        # Creates file and writes queryDict as json
        self.dict = self.getJsonDict()
        with open(self.jsonPath, "w") as file:
            json.dump(self.dict, file)

        # print(
        #     "| Exit {fct}".format(fct=inspect.stack()[0][3])
        # ) if self.isDebug else None

    # +-------------------------------+
    # |---------- LOAD JSON ----------|
    # +-------------------------------+

    def jsonToTreeWidget(self):
        """
        Load self.jsonFile in treeWidget
        """
        # Open json file
        with open(self.jsonPath, "r") as file:
            # Clear current data and load json file
            self.dict.clear()
            self.dict = json.load(file)

        # Create qTreeWidget
        self.loadFromJson(self.maintreewdgitem, self.dict)

        # loadmainsql
        if "mainsql" in self.dict.keys():
            # self.lineEdit_sqlfinal.setText(self.dict['mainsql'])
            self.textBrowser_sqlfinal.setPlainText(self.dict["mainsql"])

    def loadFromJson(self, node, dct):
        """
        Load json file into qTreeWidget
        :param node: qTreeWidgetItem, current "row"
        :param dct: dict, current "row" data containing values and children
        """
        # dct's legit children
        realChildren = self.legitChildren(dct)

        # Loop through legit children
        for child in realChildren:
            # Create new item
            qtreewidgetitm = QTreeWidgetItem(node, [dct[child]["name"]])

            # Add widgets to item
            self.widgetsToNewItem(qtreewidgetitm)

            # Load widgets' properties
            self.loadWidgetProperties(
                qtreewidgetitm,
                dct[child]["select"],
                dct[child]["bareme"],
                dct[child]["type"],
                dct[child]["value"],
            )

            # Recursive call
            self.loadFromJson(qtreewidgetitm, dct[child])

    def loadWidgetProperties(self, qtreewidgetitm, select, bareme, typeValue, value):
        """
        Load widget properties for each row
        :param qtreewidgetitm: qTreeWidgetItem, current "row"
        :param select: str, database query
        :param bareme: dict, bareme as json file
        :param typeValue: str, qComboBox value
        :param value: str, qDoubleSpinBox value, qComboBox value otherwise
        """
        # print(
        #     "|____ Enter {fct}".format(fct=inspect.stack()[0][3])
        # ) if self.isDebug else None

        # Set select lineEdit
        lineEditSelect = self.treeWidget.itemWidget(qtreewidgetitm, 1)
        lineEditSelect.setText(select)

        # Set button bareme
        pushButtonPlus = self.treeWidget.itemWidget(qtreewidgetitm, 2)
        pushButtonPlus.baremeWidget.dict = bareme

        # Set valueType comboBox
        valueType = self.treeWidget.itemWidget(qtreewidgetitm, 3)
        indexValueType = valueType.findText(typeValue)
        if indexValueType >= 0:
            valueType.setCurrentIndex(indexValueType)

        # Check fourth column type and set value
        fourthColumn = self.treeWidget.itemWidget(qtreewidgetitm, 4)
        # # Fourth column is spinBox
        if isinstance(fourthColumn, QDoubleSpinBox):
            fourthColumn.setValue(value)
        # # Fourth column is comboBox
        else:
            indexclass = fourthColumn.findText(value)
            if indexclass >= 0:
                fourthColumn.setCurrentIndex(indexclass)

        # print(
        #     "|____ Exit {fct}".format(fct=inspect.stack()[0][3])
        # ) if self.isDebug else None

    # |---------- GET DATAFRAME ----------|

    # |---------- GET BAREME ----------|

    def getBareme_old(self, node):
        """
        Retrieve route to bareme from current node
        :return: dict, bareme
        """
        # Clear self.route
        self.route = []
        # Independent children from current node to root as list in inverse order
        self.reverseListToBareme(node)
        # Route to bareme as key dict
        route = self.routeToBareme()
        # Fetch bareme
        bareme = self.fetchBareme(route)
        return bareme

    def reverseListToBareme_old(self, node):
        """
        Independent children from current node to root as list in inverse order
        :param node: qTreeWidgetItem, current selected node
        """

        if node.parent():
            # Get parent
            parent = node.parent()

            # Get parent's children number
            childNr = parent.childCount()

            # Loop through parent's children
            for childItem in range(childNr):
                child = parent.child(childItem)

                # Append self.route and recursive call to parent if current child is node
                if child == node:
                    self.route.append(childItem + 1)
                    self.reverseListToBareme(parent)

    def routeToBareme_old(self):
        """
        Route to bareme as key dict
        :return: list, dict keys from root to selected bareme
        """

        # Reverse self.route
        self.route = self.route[::-1]

        current = ""
        route = []

        # Append parent path
        for item in self.route:
            current += str(item)
            route.append(current)

        return route

    def fetchBareme_old(self, route):
        """
        Fetch bareme
        :param route: dict keys from root to selected bareme
        :return: dict, bareme
        """

        data = self.dict

        for key in route:
            data = data[key]

        return data["bareme"]

    def _________________utils(self):
        pass

    def getJsonDict(self):
        jsondict = {}
        jsondict["mainsql"] = self.textBrowser_sqlfinal.toPlainText()
        self.visitTree(self.maintreewdgitem, jsondict)
        return jsondict

    def appendMessage(self, messagetxt):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.textBrowser_errors.append(now + " : " + messagetxt)

    def stopThread(self):
        if self.thread.isRunning():
            # self.label_errormessage.setText('thread runs !!')
            self.thread.terminate()
            self.thread.wait()

    @staticmethod
    def legitChildren(dct):
        """
        Return dct's child that are dict
        :param dct: dict, current node values and children
        :return: list, only item from dct that are dict
        """
        legitChildren = []
        # Loop through dct and append legitChildren if (element is dict and != "bareme")
        for element in list(dct.keys()):
            if isinstance(dct[element], dict) and element != "bareme":
                legitChildren.append(element)
        return legitChildren

    def getNodeId(self, node):
        nodeid = ""
        while node.parent() is not None:
            parent = node.parent()
            childidx = parent.indexOfChild(node) + 1
            nodeid = str(childidx) + nodeid
            node = node.parent()

        # print("okok", nodeid)
        return nodeid

    def visitTree(self, node, dct, parentKey=""):
        """
        Iterate over the tree and build dct
        :param node: QTreeWidgetItem, current node
        :param dct: dict, contain elements from current node
        :param parentKey: str, current looped key. Init at "" for root
        """
        if node.parent():
            # Retrieve data from current node
            qComboBox = self.treeWidget.itemWidget(node, 3)
            valueType = qComboBox.currentText()

            # TODO: value = fourthColumn.value() // fourthColumn.currentText()
            # Check fourth column type
            fourthColumn = self.treeWidget.itemWidget(node, 4)
            if isinstance(fourthColumn, QDoubleSpinBox):
                spinbox = self.treeWidget.itemWidget(node, 4)
                value = spinbox.value()
            else:
                comboBoxClass = self.treeWidget.itemWidget(node, 4)
                value = comboBoxClass.currentText()

            # Set default dict values
            dct.setdefault("name", node.text(0))
            dct.setdefault("select", None)
            dct.setdefault("bareme", None)
            dct.setdefault("type", valueType)
            dct.setdefault("value", value)

        # Get number of child
        childNr = node.childCount()

        # If node is leaf
        if childNr == 0:

            # print("|____", node.text(0), "has no child") if self.isDebug else None

            # Get select
            lineEditSelect = self.treeWidget.itemWidget(node, 1)
            select = lineEditSelect.text()

            # Get qPushButtonPlus
            pushButtonPlus = self.treeWidget.itemWidget(node, 2)
            bareme = pushButtonPlus.baremeWidget.dict

            # Set default dict values
            dct["select"] = select
            dct["bareme"] = bareme
            # dct["bareme"] = "TBD"

        # If node has children
        else:
            # print("|____", node.text(0), "has children") if self.isDebug else None
            # Loop through children and add them to dct
            for childItem in range(childNr):

                # Define currentKey
                currentKey = str(parentKey) + str(childItem + 1)

                # Define current node
                child = node.child(childItem)
                dct.setdefault(currentKey, {})

                # Loop through children recursively
                self.visitTree(child, dct[currentKey], currentKey)
