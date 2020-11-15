# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui
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

        uipath = os.path.join(os.path.dirname(__file__), "amcwindow2.ui")
        uic.loadUi(uipath, self)

        # DEBUG
        self.isDebug = False

        # self.mainrequestmodified = False

        self.dbase = dbase
        self.mcacore = mcacore
        self.dict = {}
        self.confname = confname
        self.jsonPath = self.mcacore.getConfFilePath(confname)
        self.qgiscanvas = qgiscanvas

        # treeWidget
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

        self.menuitem = None
        self.itemnameediting = None
        # self.lineEdit_sqlfinal.textChanged.connect(self.setMainRequestModified)
        self.textBrowser_sqlfinal.textChanged.connect(self.setMainRequestModified)

        if qgis.utils.iface is None:
            self.menuitem = self.maintreewdgitem
            # self.lineEdit_sqlfinal.setText("FROM #lamia.noeud INNER JOIN #lamia.descriptionsystem ON descriptionsystem.pk_descriptionsystem = noeud.lpk_descriptionsystem")
            self.textBrowser_sqlfinal.setPlainText(
                "FROM #lamia.noeud INNER JOIN #lamia.descriptionsystem ON descriptionsystem.pk_descriptionsystem = noeud.lpk_descriptionsystem"
            )

        # Load json file
        # self.jsonPath = jsonpath
        if self.jsonPath is not None and os.stat(self.jsonPath).st_size > 0:
            self.jsonToTreeWidget()

        # Results
        self.df = None  # the mainsql request result
        self.route = []
        self.result = pd.DataFrame()  # the mainsql request processed with bareme
        self.starttime = None

        # if False:
        #     # Click on save
        #     self.buttonSave.clicked.connect(self.saveClicked)
        #     self.toolButton_updatedb.clicked.connect(self.createDataFrame2)
        #     self.toolButton_testdb.clicked.connect(self.testDB2)

        #     # virtual layer process
        #     self.createdataframe2 = CreateDataframe2()
        #     self.thread2 = QtCore.QThread()
        #     self.createdataframe2.moveToThread(self.thread2)
        #     self.createdataframe2.finished.connect(self.postVLayerProcessed2)
        #     self.createdataframe2.finished.connect(self.thread2.quit)
        #     self.createdataframe2.dbasestatus.connect(self.showStatus)
        #     self.thread2.started.connect(self.createdataframe2.processVLayer)

        #     jsonname = os.path.basename(os.path.splitext(self.jsonPath)[0])
        #     self.filevirtuallayer = os.path.join(
        #         self.dbase.dbaseressourcesdirectory,
        #         "config",
        #         "amctools",
        #         jsonname + ".sqlite",
        #     )

        #     # inform about status
        #     self.createdataframe2.filename = self.filevirtuallayer
        #     self.toolButton_updatedb.setEnabled(False)
        #     self.getDBStatus2()

        if True:
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
            self.mcacore.mcavirtualayerFactory.setConfName(self.confname)
            self.toolButton_updatedb.setEnabled(False)
            self.getDBStatus()

        self.treeWidget.expandAll()

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
        if False:
            lineEditSelect.textChanged.connect(self.setMainRequestModified2)
        else:
            lineEditSelect.textChanged.connect(self.setMainRequestModified)
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

        print(
            "|____ Exit {fct}".format(fct=inspect.stack()[0][3])
        ) if self.isDebug else None

    def visualisationPressed(self):
        debug = False

        if debug:
            print("> Visualisation button pressed")

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

    def getNodeId(self, node):
        nodeid = ""
        while node.parent() is not None:
            parent = node.parent()
            childidx = parent.indexOfChild(node) + 1
            nodeid = str(childidx) + nodeid
            node = node.parent()

        print("okok", nodeid)
        return nodeid

    def evaluate_old(self, node=None):
        print(
            "| Enter {fct}".format(fct=inspect.stack()[0][3])
        ) if self.isDebug else None

        # Fetch current node if requested
        if node is None:
            node = self.treeWidget.currentItem()
        nodeid = self.getNodeId(node)

        self.mcacore.computeNodeScore(self.confname, self.getJsonDict(), nodeid)

        return

        if node is None:  # called from main amc gui
            node = self.maintreewdgitem

        # Get number of child
        childNr = node.childCount()

        # Visit all child nodes
        if childNr:

            # Create temp dataframe
            stockChildValue = pd.DataFrame()

            sumWeightings = 0

            for childItem in range(childNr):

                # Define current node
                child = node.child(childItem)

                # Get child weighting
                # Check fourth column type
                fourthColumnChild = self.treeWidget.itemWidget(child, 4)
                # Weighting
                if isinstance(fourthColumnChild, QDoubleSpinBox):
                    weighting = fourthColumnChild.value()
                # Class
                else:
                    weighting = 1
                sumWeightings += weighting
                if child.text(0) in stockChildValue.columns:  # for no duplicate
                    columnname = child.text(0) + "-" + str(childItem)
                else:
                    columnname = child.text(0)
                # Calculate baremized ans ponderated results
                stockChildValue[columnname] = self.evaluate(child)

                # TODO: if ponderation / if class
                stockChildValue[columnname] = stockChildValue[columnname] * weighting

            # Sum columns
            # stockChildValue["total"] = stockChildValue.sum(axis=1) / sumWeightings
            stockChildValue["total"] = stockChildValue.sum(axis=1)
            # pprint(stockChildValue)

            print(
                "| Exit {fct}".format(fct=inspect.stack()[0][3])
            ) if self.isDebug else None

            return stockChildValue["total"]

        # Evaluate if leaf
        else:
            print(
                "| Exit {fct}".format(fct=inspect.stack()[0][3])
            ) if self.isDebug else None
            return self.calculus(node)

    # +-------------------------------+
    # |---------- SAVE JSON ----------|
    # +-------------------------------+

    # def getName(self):
    #     """
    #     Ask user for a file name
    #     :return: str, name if correct, None otherwise
    #     """
    #     text, ok = QInputDialog.getText(
    #         self, "Create a new IKDIJFIDJFIDJFLFJLDKJFLD", "File name"
    #     )
    #     if ok:
    #         return str(text + ".json")
    #     return None

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

        print(
            "| Exit {fct}".format(fct=inspect.stack()[0][3])
        ) if self.isDebug else None

    def getJsonDict(self):
        jsondict = {}
        jsondict["mainsql"] = self.textBrowser_sqlfinal.toPlainText()
        self.visitTree(self.maintreewdgitem, jsondict)
        return jsondict

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

            print("|____", node.text(0), "has no child") if self.isDebug else None

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
            print("|____", node.text(0), "has children") if self.isDebug else None
            # Loop through children and add them to dct
            for childItem in range(childNr):

                # Define currentKey
                currentKey = str(parentKey) + str(childItem + 1)

                # Define current node
                child = node.child(childItem)
                dct.setdefault(currentKey, {})

                # Loop through children recursively
                self.visitTree(child, dct[currentKey], currentKey)

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

    def legitChildren2_old(self, dct):
        """
        Return dct's child that are dict
        :param dct: dict, current node values and children
        :return: dict, only item from dct that are dict
        """
        legitChildren = {}
        # Loop through dct and append legitChildren if (element is dict and != "bareme")
        for element in dct.keys():
            if isinstance(dct[element], dict) and element != "bareme":
                legitChildren[element] = dct[element]
        return legitChildren

    def loadWidgetProperties(self, qtreewidgetitm, select, bareme, typeValue, value):
        """
        Load widget properties for each row
        :param qtreewidgetitm: qTreeWidgetItem, current "row"
        :param select: str, database query
        :param bareme: dict, bareme as json file
        :param typeValue: str, qComboBox value
        :param value: str, qDoubleSpinBox value, qComboBox value otherwise
        """
        print(
            "|____ Enter {fct}".format(fct=inspect.stack()[0][3])
        ) if self.isDebug else None

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

        print(
            "|____ Exit {fct}".format(fct=inspect.stack()[0][3])
        ) if self.isDebug else None

    # |---------- GET DATAFRAME ----------|

    def showStatus(self, txtstatus):
        self.label_rawdbasestate.setText(txtstatus)

    def testDB(self):
        jsondict = self.getJsonDict()
        success, message = self.mcacore.testDB(self.confname, jsondict)
        if not success:
            self.toolButton_updatedb.setEnabled(False)
        else:
            self.toolButton_updatedb.setEnabled(True)
        self.appendMessage(message)

    #     if False:
    #         # Get selects
    #         selects = self.mcacore.getSelects(self.getJsonDict())
    #         # print("::", selects)
    #         print("::", self.getSelects())
    #         # selects = self.getSelects()
    #         # print("::", selects)
    #         if not selects:
    #             self.appendMessage("sql not ok - do not find main table")
    #             self.toolButton_updatedb.setEnabled(False)
    #             return

    #         sql = {
    #             # "final": self.lineEdit_sqlfinal.text(),
    #             # "final": sqlfinal,
    #             "final": self.textBrowser_sqlfinal.toPlainText() + " LIMIT 1",
    #             "critere": selects,
    #         }

    #         try:
    #             qgsvectorlay, sqltxt = self.prepareVLayerScript(sql)
    #         except Exception as e:
    #             self.appendMessage("sql not ok")
    #             self.toolButton_updatedb.setEnabled(False)
    #             return

    #         # restrict query to fist row of main table
    #         # construct where clause
    #         maintable, pkmaintable = self.getMainTable()
    #         sql = "SELECT Min(" + pkmaintable + ") FROM " + maintable
    #         sql = self.dbase.updateQueryTableNow(sql)
    #         res = self.dbase.query(sql)
    #         sentence = maintable + "." + pkmaintable + " = " + str(res[0][0])
    #         # insert it in sql
    #         sqlsplitted = self.dbase.utils.splitSQLSelectFromWhereOrderby(sqltxt)
    #         if "WHERE" in sqlsplitted.keys():
    #             sqlsplitted["WHERE"] += " AND " + sentence
    #         else:
    #             sqlsplitted["WHERE"] = sentence
    #         sqlfinal = self.dbase.utils.rebuildSplittedQuery(sqlsplitted)

    #         # print("***", sqlfinal)

    #         self.starttime = time.time()
    #         self.createdataframe.testsql = True  # before prepareVLayerScript
    #         self.createdataframe.scriptvl = sqlfinal
    #         self.createdataframe.qgsvectorlay = qgsvectorlay
    #         # self.createdataframe.filename = self.filevirtuallayer
    #         self.thread.start()

    # def testDB2(self):
    #     # Get selects
    #     selects = self.mcacore.getSelects(self.getJsonDict())
    #     if selects is None:
    #         self.appendMessage("sql not ok - do not find main table")
    #         self.toolButton_updatedb.setEnabled(False)
    #         return

    #     # Fetch raw data from DB
    #     sql = {
    #         # "final": self.lineEdit_sqlfinal.text(),
    #         "final": self.textBrowser_sqlfinal.toPlainText() + " LIMIT 1",
    #         "critere": selects,
    #     }
    #     try:
    #         scriptvl, sqltxt = self.prepareVLayerScript2(sql)
    #     except Exception as e:
    #         self.appendMessage("sql not ok")
    #         self.toolButton_updatedb.setEnabled(False)
    #         return

    #     self.createdataframe2.testsql = True
    #     self.createdataframe2.scriptvl = scriptvl
    #     # self.createdataframe2.filename = self.filevirtuallayer
    #     self.thread2.start()

    def createDataFrame(self):
        res, lay = self.mcacore.createMcaDB(self.confname, self.getJsonDict())
        self.df = res
        # print(self.df)

    #     # if self.thread.isRunning():
    #     #     # self.label_errormessage.setText('thread runs !!')
    #     #     self.appendMessage("thread runs !!")
    #     #     return

    #     # if self.sender() == self.toolButton_updatedb:
    #     #     self.createdataframe.setStatus("False")  # force to update

    #     # # Clear dataFrame
    #     # self.df = None
    #     # # Get selects
    #     # selects = self.mcacore.getSelects(self.getJsonDict())

    #     # # Fetch raw data from DB
    #     # sql = {
    #     #     # "final": self.lineEdit_sqlfinal.text(),
    #     #     "final": self.textBrowser_sqlfinal.toPlainText(),
    #     #     "critere": selects,
    #     # }

    #     # layersql, sqltxt = self.prepareVLayerScript(sql)
    #     # self.createdataframe.testsql = False
    #     # self.createdataframe.scriptvl = sqltxt
    #     # self.createdataframe.qgsvectorlay = layersql
    #     # # self.createdataframe.filename = self.filevirtuallayer
    #     # self.starttime = time.time()
    #     # self.appendMessage("begin update  ")
    #     # self.appendMessage(" SQL request :  ")
    #     # self.appendMessage(sqltxt)

    #     # self.thread.start()

    # def createDataFrame2(self):
    #     """
    #     Fetch data from DB
    #     :return:
    #     """
    #     if self.thread2.isRunning():
    #         # self.label_errormessage.setText('thread runs !!')
    #         self.appendMessage("thread runs !!")
    #         return

    #     # Clear dataFrame
    #     self.df = None
    #     # Get selects
    #     selects = self.mcacore.getSelects(self.getJsonDict())

    #     # Fetch raw data from DB
    #     sql = {
    #         # "final": self.lineEdit_sqlfinal.text(),
    #         "final": self.textBrowser_sqlfinal.toPlainText(),
    #         "critere": selects,
    #     }
    #     scriptvl, sqltxt = self.prepareVLayerScript2(sql)
    #     self.createdataframe2.testsql = False
    #     self.createdataframe2.scriptvl = scriptvl
    #     # self.createdataframe2.filename = self.filevirtuallayer
    #     self.starttime = time.time()
    #     self.appendMessage("begin update  ")

    #     self.thread2.start()

    # def postVLayerProcessed(self, rawdata):
    #     """
    #      Called when the creation of virtual layer is done
    #      :param rawdata: list of results of sql request
    #      """

    #     selects = self.mcacore.getSelects(self.getJsonDict())

    #     if self.createdataframe.testsql:
    #         self.createdataframe.testsql = False
    #         self.appendMessage(" : " + "results : ")
    #         if len(rawdata) > 0:
    #             tempdf = pd.DataFrame(rawdata)
    #             tempdf.columns = selects
    #             txttoshow = str(tempdf)
    #             self.appendMessage(txttoshow)
    #             self.toolButton_updatedb.setEnabled(True)
    #         else:
    #             txttoshow = "Requete mal construite"
    #             self.toolButton_updatedb.setEnabled(False)
    #             self.appendMessage(txttoshow)
    #             sql = {
    #                 # "final": self.lineEdit_sqlfinal.text(),
    #                 "final": self.textBrowser_sqlfinal.toPlainText(),
    #                 "critere": selects,
    #             }
    #             scriptvl, sqltxt = self.prepareVLayerScript(sql)
    #             # self.appendMessage(scriptvl)
    #             self.appendMessage(sqltxt)

    #     else:
    #         self.cleanData(rawdata, selects)
    #         # pprint(self.df)
    #         self.createdataframe.setStatus("True")

    #     if self.starttime is not None:
    #         self.appendMessage(
    #             "end update  "
    #             + str(round(time.time() - self.starttime, 2))
    #             + " seconds"
    #         )
    #         self.starttime = None

    # def postVLayerProcessed2(self, rawdata):
    #     """
    #     Called when the creation of virtual layer is done
    #     :param rawdata: list of results of sql request
    #     """
    #     selects = self.mcacore.getSelects(self.getJsonDict())

    #     if self.createdataframe2.testsql:
    #         self.createdataframe2.testsql = False
    #         self.appendMessage(" : " + "results : ")
    #         if len(rawdata) > 0:
    #             tempdf = pd.DataFrame(rawdata)
    #             tempdf.columns = selects
    #             txttoshow = str(tempdf)
    #             self.appendMessage(txttoshow)
    #             self.toolButton_updatedb.setEnabled(True)
    #         else:
    #             txttoshow = "Requete mal construite"
    #             self.toolButton_updatedb.setEnabled(False)
    #             self.appendMessage(txttoshow)
    #             sql = {
    #                 # "final": self.lineEdit_sqlfinal.text(),
    #                 "final": self.textBrowser_sqlfinal.toPlainText(),
    #                 "critere": selects,
    #             }
    #             scriptvl, sqltxt = self.prepareVLayerScript2(sql)
    #             self.appendMessage(scriptvl)
    #             self.appendMessage(sqltxt)

    #     else:
    #         self.cleanData(rawdata, selects)
    #         # pprint(self.df)
    #         self.createdataframe2.setStatus("True")
    #         self.appendMessage(
    #             "end update  "
    #             + str(round(time.time() - self.starttime, 2))
    #             + " seconds"
    #         )

    # def getSelects(self):
    #     """
    #     Loop through all criterias and get selects
    #     :return: list, unique selects
    #     """

    #     maintable, pkmaintable = self.getMainTable()
    #     if maintable is None:
    #         return None

    #     selects = [maintable + "." + pkmaintable]

    #     # Create iteraotr
    #     iterator = QTreeWidgetItemIterator(self.treeWidget, QTreeWidgetItemIterator.All)
    #     # Iterate through QTreeWidget
    #     while iterator.value():
    #         item = iterator.value()
    #         lineeditselect = self.treeWidget.itemWidget(item, 1)

    #         # Append selects if is QLineEdit and not empty
    #         if isinstance(lineeditselect, QLineEdit) and lineeditselect.text() != "":
    #             selects.extend(lineeditselect.text().split(", "))
    #         iterator += 1
    #     # Return unique values from selects
    #     finalselects = []
    #     for sel in selects:
    #         if sel not in finalselects:
    #             finalselects.append(sel)

    #     return finalselects

    # def queryDB(self, selects):
    #     """
    #     Fetch data from DB
    #     :param selects: list, unique selects
    #     :return: 2D array,
    #     """
    #     if selects is False or selects is None or len(selects) == 0:
    #         selects = self.mcacore.getSelects(self.getJsonDict())
    #     sql = {
    #         # "final": self.lineEdit_sqlfinal.text(),
    #         "final": self.textBrowser_sqlfinal.toPlainText(),
    #         "critere": selects,
    #     }

    #     sqlvlayer, sqltxt = self.prepareVLayerScript2(sql)
    #     rawdata = self.processVLayer(sqlvlayer)
    #     return rawdata

    # def cleanData(self, rawdata, selects):
    #     """
    #     Clean data, dataFrame and rename headers
    #     :param rawdata: 2D array,
    #     :param selects: list, selects (columns name)
    #     """
    #     self.df = pd.DataFrame(rawdata)
    #     nbrecolumn1 = len(self.df.columns)
    #     nbrecolumn2 = len(selects)
    #     # Rename self.df headers
    #     if nbrecolumn1 == nbrecolumn2:
    #         self.df.columns = selects
    #     else:
    #         print("Error cleaing datas")
    #         pprint(self.df)
    #         print(selects)
    #     # pprint(self.df)

    # def prepareVLayerScript(self, sqlsict):
    #     """

    #     :param sqlsict:
    #     :return: sqlrequest, qgsvectorlayerslist
    #     """
    #     debug = False

    #     if debug:
    #         logging.getLogger("Lamia").debug("sqlsict %s", str(sqlsict))

    #     layers = {}
    #     # build SELECT part
    #     sqlfinal = " SELECT "
    #     for sql in sqlsict["critere"]:
    #         layersql, sentencesql = self.analyseRawSQL(sql)
    #         for vlayername, vlayersql in layersql:
    #             if vlayername not in layers.keys():
    #                 layers[vlayername] = vlayersql
    #         sqlfinal += sentencesql + ", "
    #     sqlfinal = sqlfinal[:-2]
    #     # print("analyseRawSQL", sqlfinal, sqlsict)
    #     # build FROM part and get qgsvectorlayers needed
    #     layersql, sentencesql = self.analyseRawSQL(sqlsict["final"])
    #     # print(layersql, sentencesql)

    #     sqlfinal += sentencesql
    #     sqlfinal = self.dbase.updateQueryTableNow(sqlfinal)

    #     return layersql, sqlfinal

    # def prepareVLayerScript2(self, sqlsict):
    #     """
    #     Construct virtual layer of raw sql script
    #     :param sqlsict:
    #     :return: the script used in virtual layer creation
    #     """
    #     debug = False

    #     if debug:
    #         logging.getLogger("Lamia").debug("sqlsict %s", str(sqlsict))

    #     layers = {}
    #     # build sql
    #     sqlfinal = " SELECT "
    #     for sql in sqlsict["critere"]:
    #         layersql, sentencesql = self.analyseRawSQL2(sql)
    #         for vlayername, vlayersql in layersql:
    #             if vlayername not in layers.keys():
    #                 layers[vlayername] = vlayersql
    #         sqlfinal += sentencesql + ", "
    #     sqlfinal = sqlfinal[:-2]
    #     layersql, sentencesql = self.analyseRawSQL2(sqlsict["final"])

    #     for vlayername, vlayersql in layersql:
    #         if vlayername not in layers.keys():
    #             layers[vlayername] = vlayersql

    #     sqlfinal += sentencesql

    #     sqlfinal = self.dbase.updateQueryTableNow(sqlfinal)

    #     if debug:
    #         logging.getLogger("Lamia").debug("********************* ")
    #         logging.getLogger("Lamia").debug("layers %s", str(layers))
    #         logging.getLogger("Lamia").debug("sqlfinal %s", str(sqlfinal))

    #     # Build final script for virtual layer
    #     scriptvl = "?" + "&".join([layers[key] for key in layers.keys()])

    #     if sys.version_info.major == 2:
    #         scriptvl += "&query=" + str(QtCore.QUrl.toPercentEncoding(sqlfinal))
    #     elif sys.version_info.major == 3:
    #         scriptvl += "&query=" + QtCore.QUrl.toPercentEncoding(
    #             sqlfinal
    #         ).data().decode("utf-8")

    #     if debug:
    #         logging.getLogger("Lamia").debug("scriptvl %s", str(scriptvl))

    #     return scriptvl, sqlfinal

    # def analyseRawSQL(self, sql):
    #     """
    #     Preparing data to be inserted in a virtual layer - process the FROM part of sql sentence

    #     :param sql: sql sentence startig from FROM
    #     :return: layersql, sentencesql :
    #     * layer sql : list of [tablenamevlayer, vlayerlayer] : name of layer in virtual table , and associated qggsvectorlayer
    #     * sentencesql : text to be inserted in virtual layer creation
    #     """

    #     debug = False

    #     layersql, sentencesql = [], ""

    #     if "#" in sql:
    #         sqlssplitspace = sql.split(" ")
    #         for sqlsplitspace in sqlssplitspace:
    #             if "#" in sqlsplitspace:
    #                 # print("*", sqlsplitspace)
    #                 # tabletype, tablename = sqlsplitspace.split(".")
    #                 tabletype, tablename = sqlsplitspace.split(".")[0:2]
    #                 # print(tabletype, tablename)
    #                 # print(self.qgiscanvas.layers)
    #                 vlayerlayer = ""
    #                 if tabletype == "#lamia":
    #                     if "_now" in tablename:
    #                         rawtablename = "_".join(tablename.split("_")[:-1])
    #                         tablenamevlayer = (
    #                             "_".join(tablename.split("_")[:-1]) + "_qgis"
    #                         )
    #                     elif "_qgis" in tablename:
    #                         rawtablename = "_".join(tablename.split("_")[:-1])
    #                         tablenamevlayer = (
    #                             "_".join(tablename.split("_")[:-1]) + "_qgis"
    #                         )
    #                     else:
    #                         rawtablename = tablename
    #                         tablenamevlayer = tablename
    #                     # print(
    #                     #     self.qgiscanvas.layers[rawtablename]["layerqgis"]
    #                     #     .dataProvider()
    #                     #     .uri()
    #                     #     .uri()
    #                     # )
    #                     vectorlayer = qgis.core.QgsVectorLayer(
    #                         self.qgiscanvas.layers[rawtablename]["layerqgis"]
    #                         .dataProvider()
    #                         .uri()
    #                         .uri(),
    #                         tablenamevlayer,
    #                         "spatialite",
    #                     )
    #                     # print(vectorlayer, vectorlayer.isValid())
    #                     vectorlayer.setSubsetString("")

    #                 elif tabletype == "#lamiashp":
    #                     # searchfilepath of tablename
    #                     sql = (
    #                         "SELECT file FROM Rasters_now WHERE libelle = '"
    #                         + str(tablename)
    #                         + "'"
    #                     )
    #                     sql = self.dbase.updateQueryTableNow(sql)
    #                     res = self.dbase.query(sql)
    #                     if res and len(res) > 0:
    #                         shppath = res[0][0]
    #                         shpcompletepath = str(
    #                             self.dbase.completePathOfFile(shppath)
    #                         )
    #                         if sys.version_info.major == 3:
    #                             tablenamevlayer = tablename
    #                             vectorlayer = qgis.core.QgsVectorLayer(
    #                                 shpcompletepath, tablenamevlayer, "ogr"
    #                             )
    #                             vectorlayer.setProviderEncoding("UTF-8")

    #                 layersql.append([tablenamevlayer, vectorlayer])
    #                 sentencesql += " " + tablename

    #             else:
    #                 sentencesql += " " + sqlsplitspace
    #                 continue
    #     else:
    #         sentencesql = sql

    #     return layersql, sentencesql

    def analyseRawSQL2_old(self, sql):
        """
        Preparing data to be inserted in a virtual layer - process the FROM part of sql sentence

        :param sql: sql sentence startig from FROM
        :return: layersql, sentencesql :
        * layer sql : list of [tablenamevlayer, vlayerlayer] : name of layer in virtual table , text to be inserted in virtual layer creation
        * sentencesql : text to be inserted in virtual layer creation
        """

        debug = False

        layersql, sentencesql = [], ""

        if "#" in sql:
            sqlssplitspace = sql.split(" ")
            for sqlsplitspace in sqlssplitspace:
                if "#" in sqlsplitspace:
                    tabletype, tablename = sqlsplitspace.split(".")
                    vlayerlayer = ""
                    if tabletype == "#lamia":
                        if "_now" in tablename:
                            rawtablename = "_".join(tablename.split("_")[:-1])
                            tablenamevlayer = (
                                "_".join(tablename.split("_")[:-1]) + "_qgis"
                            )
                        elif "_qgis" in tablename:
                            rawtablename = "_".join(tablename.split("_")[:-1])
                            tablenamevlayer = (
                                "_".join(tablename.split("_")[:-1]) + "_qgis"
                            )
                        else:
                            rawtablename = tablename
                            tablenamevlayer = tablename

                        vlayerlayer = "layer=spatialite:"

                        if sys.version_info.major == 2:
                            if self.dbase.isTableSpatial(rawtablename):
                                vlayerlayer += str(
                                    QtCore.QUrl.toPercentEncoding(
                                        "dbname='"
                                        + self.dbase.spatialitefile
                                        + "' key ='pk_"
                                        + rawtablename.lower()
                                        + "' "
                                        + 'table="'
                                        + tablenamevlayer.lower()
                                        + '"'
                                        + " (geom) sql="
                                    )
                                )
                            else:
                                vlayerlayer += str(
                                    QtCore.QUrl.toPercentEncoding(
                                        "dbname='"
                                        + self.dbase.spatialitefile
                                        + "' key ='pk_"
                                        + rawtablename.lower()
                                        + "' "
                                        + 'table="'
                                        + tablenamevlayer.lower()
                                        + '"'
                                        + " () sql="
                                    )
                                )
                        elif sys.version_info.major == 3:
                            if self.dbase.isTableSpatial(rawtablename):
                                vlayerlayer += (
                                    QtCore.QUrl.toPercentEncoding(
                                        "dbname='"
                                        + self.dbase.spatialitefile
                                        + "' key ='pk_"
                                        + rawtablename.lower()
                                        + "' "
                                        + 'table="'
                                        + tablenamevlayer.lower()
                                        + '"'
                                        + " (geom) sql="
                                    )
                                    .data()
                                    .decode("utf-8")
                                )
                            else:
                                vlayerlayer += (
                                    QtCore.QUrl.toPercentEncoding(
                                        "dbname='"
                                        + self.dbase.spatialitefile
                                        + "' key ='pk_"
                                        + rawtablename.lower()
                                        + "' "
                                        + 'table="'
                                        + tablenamevlayer.lower()
                                        + '"'
                                        + " () sql="
                                    )
                                    .data()
                                    .decode("utf-8")
                                )

                    elif tabletype == "#lamiashp":
                        # searchfilepath of tablename
                        sql = (
                            "SELECT file FROM Rasters_now WHERE libelle = '"
                            + str(tablename)
                            + "'"
                        )
                        sql = self.dbase.updateQueryTableNow(sql)
                        res = self.dbase.query(sql)
                        if res and len(res) > 0:
                            shppath = res[0][0]
                            shpcompletepath = str(
                                self.dbase.completePathOfFile(shppath)
                            )
                            if sys.version_info.major == 3:
                                vlayerlayer = "layer=ogr:"
                                vlayerlayer += (
                                    QtCore.QUrl.toPercentEncoding(shpcompletepath)
                                    .data()
                                    .decode("utf-8")
                                )
                                tablenamevlayer = tablename

                    vlayerlayer += ":" + str(tablenamevlayer) + ":UTF8"
                    layersql.append([tablenamevlayer, vlayerlayer])
                    sentencesql += " " + tablename

                else:
                    sentencesql += " " + sqlsplitspace
                    continue
        else:
            sentencesql = sql

        return layersql, sentencesql

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

    def reverseListToBareme(self, node):
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

    def routeToBareme(self):
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

    def fetchBareme(self, route):
        """
        Fetch bareme
        :param route: dict keys from root to selected bareme
        :return: dict, bareme
        """

        data = self.dict

        for key in route:
            data = data[key]

        return data["bareme"]

    # |---------- CALCULUS ----------|

    def calculus_old(self, node):
        # Get data
        # if hasattr(self, "createdataframe"):
        fromup, selectup = self.mcacore.checkVLayerUpdate(
            self.confname, self.getJsonDict()
        )
        if not fromup or not selectup or self.df is None:
            print("update DB first")
            return

        # if not self.createdataframe.getVirtualLayerUpdateStatus:
        #     self.createDataFrame()
        #     return None
        # else:
        #     if not self.createdataframe2.getVirtualLayerUpdateStatus:
        #         self.createDataFrame2()
        #         return None

        dummyDF = pd.DataFrame()

        # Get current selects
        selectsAsStr = self.treeWidget.itemWidget(node, 1)
        selects = selectsAsStr.text().split(", ")

        # Get bareme as dict
        bareme = self.getBareme(node)

        try:
            defaultValue = bareme["default"]
        except KeyError:
            defaultValue = 0
        except TypeError:
            defaultValue = 0

        # Create df with only selects from current line
        print("*", selects, self.df.columns)
        for select in selects:
            dummyDF[select] = self.df[select]

        dftonumpy = dummyDF.values

        # Get type of columns of dftonumpy
        typelist = self.getTypeList(dftonumpy)
        res = []
        for (
            line
        ) in (
            dftonumpy
        ):  # on s'en tirera à coup de boucle for .... il y a peut etre mieux mais ca marche
            result = self.someFct(line, bareme, typelist, defaultValue)
            res.append(result)

        return res

    def someFct_old(self, value, dct, typelist, defaultValue=0):
        """
        :param value: int, str, value to test
        :param dct: dict, bareme
        :return: int, evaluation of value in regards of dict
        """

        if len(typelist) > 0 and typelist[0] in [
            int,
            float,
            np.int8,
            np.int16,
            np.int32,
            np.int64,
            np.float32,
            np.float64,
        ]:
            for key in dct.keys():
                if (
                    isinstance(dct[key], dict) and value[0] <= dct[key]["value"]
                ):  # "value" in dct.keys() and
                    if self.legitChildren(dct[key]):
                        return self.someFct(
                            value[1:],
                            self.legitChildren2(dct[key]),
                            typelist[1:],
                            defaultValue,
                        )
                    else:
                        return dct[key]["weighting"]

        elif len(typelist) > 0 and typelist[0] == str:
            for key in dct.keys():
                if self.dbase.isAttributeNull(value[0]):
                    value[0] = "None"
                if isinstance(dct[key], dict) and value[0] in dct[key]["value"]:
                    if self.legitChildren(dct[key]):
                        return self.someFct(
                            value[1:],
                            self.legitChildren2(dct[key]),
                            typelist[1:],
                            defaultValue,
                        )
                    else:
                        return dct[key]["weighting"]

        try:
            return int(defaultValue)
        except ValueError:
            return 0
        except KeyError:
            return 0

    def getTypeList_old(self, df):
        typevalues = []
        dfT = df.transpose()
        for col in dfT:
            for elem in col:
                if not self.mcacore.dbase.utils.isAttributeNull(elem):
                    typevalues.append(type(elem))
                    break
        return typevalues

    def getMainTable_old(self):
        # sqlfrom = self.lineEdit_sqlfinal.text()
        sqlfrom = self.textBrowser_sqlfinal.toPlainText()

        maintable, pkmaintable = None, None
        for elem in re.split("([ ._])", sqlfrom):
            if elem in self.dbase.dbasetables.keys():
                maintable, pkmaintable = elem, "pk_" + str(elem).lower()
                break
        for elem in re.split("([ .])", sqlfrom):
            if maintable in elem:
                maintable = elem
                break

        return maintable, pkmaintable

    def setMainRequestModified(self, newtext=None):
        # self.mainrequestmodified = True
        if hasattr(self, "createdataframe"):
            self.createdataframe.setStatus("False")

        # print('setMainRequestModified',newtext )

    def setMainRequestModified2(self, newtext=None):
        # self.mainrequestmodified = True
        if hasattr(self, "createdataframe2"):
            self.createdataframe2.setStatus("False")

        # print('setMainRequestModified',newtext )

    def getDBStatus(self):
        if hasattr(self, "createdataframe"):
            status = self.createdataframe.getVirtualLayerUpdateStatus()
            if status:
                self.label_rawdbasestate.setText("DBase updated")
                self.toolButton_updatedb.setEnabled(True)
                self.createDataFrame()
            else:
                self.label_rawdbasestate.setText("DBase not updated")
        else:
            self.label_rawdbasestate.setText("DBase not updated")

    def getDBStatus2(self):
        if hasattr(self, "createdataframe"):
            status = self.createdataframe2.getVirtualLayerUpdateStatus()
            if status:
                self.label_rawdbasestate.setText("DBase updated")
                self.toolButton_updatedb.setEnabled(True)
                self.createDataFrame2()
            else:
                self.label_rawdbasestate.setText("DBase not updated")
        else:
            self.label_rawdbasestate.setText("DBase not updated")

    def appendMessage(self, messagetxt):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.textBrowser_errors.append(now + " : " + messagetxt)

    def stopThread(self):
        if self.thread.isRunning():
            # self.label_errormessage.setText('thread runs !!')
            self.thread.terminate()
            self.thread.wait()

