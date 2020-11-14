# -*- coding: utf-8 -*-


from qgis.PyQt import uic, QtCore, QtGui
import os, re
import sys
import qgis.core
import logging

try:
    from qgis.PyQt.QtGui import (QApplication, QComboBox, QDialog, QDoubleSpinBox, QHeaderView, QInputDialog, QLabel,
                                 QLineEdit, QMainWindow, QMenu, QMessageBox, QSpinBox, QTextBrowser, QToolButton, QTreeWidgetItem,
                                 QTreeWidgetItemIterator, QWidget, UserRole, QComboBox)
except ImportError:
    from qgis.PyQt.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox, QHeaderView, QInputDialog,
                                     QLabel, QLineEdit, QMainWindow, QMenu, QMessageBox, QSpinBox, QTextBrowser, QToolButton,
                                     QTreeWidgetItem, QTreeWidgetItemIterator, QWidget, QComboBox)
# Import custom comboBox
from .qComboCheckBox import CheckableComboBox

from pprint import pprint
import json
import pandas as pd
import numpy as np
import inspect


class WidgetBareme(QDialog):

    def __init__(self, qPushButttonPlus, parent=None):
        super(WidgetBareme, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'widgetBareme.ui')
        uic.loadUi(uipath, self)

        # Debug
        self.isDebug = False

        # Init attributes
        self.qPushButttonPlus = qPushButttonPlus
        self.simulationWidget = self.qPushButttonPlus.simulationWidget
        self.qtreewidgetitm = self.qPushButttonPlus.qtreewidgetitm
        self.dbase = self.simulationWidget.dbase
        self.result = []
        self.types = []

        # Init data
        self.var1 = None
        self.var2 = None
        self.vars = []
        self.df = None
        self.numpyy = None
        self.tablesinsql = []
        self.uniqueListRaw=[]
        self.uniqueListCst = []

        # Init dict
        self.dict = {}

        # Init qTreeWidget
        self.menuitem = None
        self.maintreewdgitem = QTreeWidgetItem(self.twBareme.invisibleRootItem(), ["Bareme"])
        self.twBareme.customContextMenuRequested.connect(self.openMenu)

        # Right click on criteria
        self.menu = QMenu()
        self.menu.addAction(self.tr("Add line"))
        self.menu.addAction(self.tr("Remove line"))
        self.menu.triggered.connect(self.menuAction)

        # On click action
        self.pbOK.clicked.connect(self.pbOKClicked)
        self.pbCancel.clicked.connect(self.pbCancelClicked)

    def initBareme(self):
        """
        Create and fill baremeWidget at first opening
        """
        # Retrieve select from current node
        self.getSelects()

        # Display current selects
        self.updateSelectLabel()

        # Fetch data and transform to dataFrame
        success = self.getData()
        if not success:
            return False
        # self.df = pd.DataFrame(self.result)
        # self.getBoundaries()

        #self.numpyy = np.array(self.result)
        self.numpyy = self.df.values

        # Find all types
        self.findTypes()

        # Display boundaries
        self.getBoundaries()

        # TableWidget
        self.initTreeWidget()

        if self.dict and len(self.dict) > 0:
            self.loadFromJson(self.maintreewdgitem, self.dict)
            self.lValueOthers.setText(str(0))
            if "default" in self.dict.keys():
                self.lValueOthers.setText(self.dict["default"])

        self.twBareme.expandAll()


        return True



    def getBoundaries(self):
        bounds = ""
        self.uniqueListRaw = []
        self.uniqueListCst = []

        for i in range(len(self.types)):
            self.uniqueListRaw.append([])
            self.uniqueListCst.append([])

            if self.getVarType(self.types[i]) == 'float' :
                bounds += str(self.df.iloc[:, i].min()) + ", "
                bounds += str(self.df.iloc[:, i].max()) + ", "
            else:
                uniqueList = np.unique(self.numpyy[:, i]).tolist()
                for item in uniqueList:
                    if self.dbase.isAttributeNull(item) :
                        if (len(self.uniqueListRaw[i])>0 and self.uniqueListRaw[i][0] != None):
                            self.uniqueListRaw[i].insert(0, 'None')
                            self.uniqueListCst[i].insert(0, 'None')
                        continue

                    self.uniqueListRaw[i].append(item)
                    self.uniqueListCst[i].append(self.getConstraintTextFromRawValue(item))

                    if not self.dbase.isAttributeNull(item):
                        bounds += str(item) + ", "

        boundsList = set(bounds[:-2].split())

        self.lBornes.setText(", ".join(boundsList))


    def getVarType(self, typevar):
        if typevar in [np.int8, np.int16, np.int32, np.int64, np.float32, np.float64]:
            return 'float'
        else:
            return 'text'

    def getSelects(self):
        """
        Retrieve select from current node
        Retrieve table in request
        """
        print("|__ Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        #get vars
        lineEditSelect = self.simulationWidget.treeWidget.itemWidget(self.qtreewidgetitm, 1)
        self.vars = lineEditSelect.text().split(", ")
        lineedittextsplitted = re.split('[ ._()]', lineEditSelect.text())

        #get tables
        for table in lineedittextsplitted:
            if table in self.dbase.dbasetables.keys():
                for field in lineedittextsplitted:
                    if field in self.dbase.dbasetables[table]['fields'].keys():
                        self.tablesinsql.append(table + '.' + field)

        print("|__ Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None



    def updateSelectLabel(self):
        """
        Update self.lVariables label with current select value
        """
        print("| Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        variables = ", ".join(self.vars)
        self.lVariables.setText(variables)

        print("| Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def findTypes(self):
        """
        Find data type from dataFrame
        """
        columns = list(self.df)
        self.types=[]
        for col in columns:
            self.types.append(type(self.df[col][0]))

    def initDataFrame(self):
        self.df = None

    # +------------------------------+
    # |---------- GET DATA ----------|
    # +------------------------------+

    def getData(self):
        """
        Fetch data using select and database
        """
        if self.vars[0] is not None:
            try:
                self.df = self.simulationWidget.df[self.vars]
                return True
            except Exception as e :
                self.simulationWidget.appendMessage('Erreur : la variable ne se trouve pas dans la base de données')
                self.simulationWidget.appendMessage('Mettre à jour la base de données')
                print('error', e)
                return False

        return False


    # +--------------------------------+
    # |---------- TREEWIDGET ----------|
    # +--------------------------------+

    def initTreeWidget(self):
        """
        Clear self.twBareme, create correct number of columns
        """
        print("|__ Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        #clear all
        for i in reversed(range(self.maintreewdgitem.childCount())):
            self.maintreewdgitem.removeChild(self.maintreewdgitem.child(i))

        # Clear self.twBareme
        self.twBareme.setColumnCount(0)
        self.twBareme.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        # Create and name columns
        self.twBareme.setColumnCount(3)
        self.twBareme.setHeaderItem(QTreeWidgetItem(["Name", "Value", "Weighting"]))

        # Column's width
        self.twBareme.header().setResizeMode(0, QHeaderView.Stretch)
        self.twBareme.header().resizeSection(1, 100)
        self.twBareme.header().resizeSection(2, 100)

        print("|__ Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def openMenu(self, position):
        self.menuitem = self.twBareme.currentItem()
        self.menu.exec_(self.twBareme.viewport().mapToGlobal(position))

    def menuAction(self, actionname):
        """
        Modify qTreeWidget by adding or removing items
        :param actionname: ?????????????
        :return: qTreeWidgetItem, ?????????????
        """
        print("| Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Add new item
        if actionname.text() == self.tr("Add line"):
            levelitem = self.getItemLevel(self.menuitem)
            if levelitem >= len(self.vars) -1:
                return

            # Create empty item from parent item
            qtreewidgetitm = QTreeWidgetItem(self.menuitem, [""])


            # Add widgets to new item
            self.widgetsToNewItem(qtreewidgetitm)
            # move it if numeric
            if isinstance(self.twBareme.itemWidget(qtreewidgetitm, 1), QDoubleSpinBox):
                self.twBareme.itemWidget(qtreewidgetitm, 1).valueChanged.emit(0.0)


            return qtreewidgetitm

        # Delete current row
        elif actionname.text() == self.tr("Remove line"):
            self.menuitem.parent().removeChild(self.menuitem)

        print("| Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def widgetsToNewItem(self, qtreewidgetitm):
        """
        Add widgets to new item
        :param qtreewidgetitm: qTreeWidgetItem, row where to insert new widgets
        """
        print("|__ Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Get level
        levelitem = self.getItemLevel(qtreewidgetitm)

        # Text
        qtreewidgetitm.setText(0, self.vars[levelitem])

        # Create QDoubleSpinBox if numeric, QComboBox otherwise
        if self.types[levelitem] in [np.int8, np.int16, np.int32, np.int64, np.float32, np.float64]:
            valueWidget = QDoubleSpinBox()
            valueWidget.setMaximum(999999.0)
            valueWidget.setKeyboardTracking(False)
            valueWidget.valueChanged.connect(self.reorderSpin)
        else:
            valueWidget = CheckableComboBox()

            # valueWidget = QComboBox()
            # combomodel = QStandardItemModel(3, 1)

        # Fill CheckableComboBox if necessary
        if  isinstance(valueWidget, CheckableComboBox):
            #        self.uniqueListRaw=[]
            #self.uniqueListCst = []
            for item in self.uniqueListCst[levelitem]:
                valueWidget.addItem(item)

        self.twBareme.setItemWidget(qtreewidgetitm, 1, valueWidget)

        # Value
        weighting = QDoubleSpinBox()
        self.twBareme.setItemWidget(qtreewidgetitm, 2, weighting)

        # Open tree
        self.maintreewdgitem.setExpanded(True)

        print("|__ Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

    def getConstraintTextFromRawValue(self, value):
        valueprocessed = value

        for tablefield in self.tablesinsql:
            table, field = tablefield.split('.')
            if 'Cst' in self.dbase.dbasetables[table]['fields'][field]:
                valueprocessed = self.dbase.getConstraintTextFromRawValue(table, field, value)
                if value != valueprocessed:
                    return valueprocessed

        return valueprocessed



    def getItemLevel(self, qtreewdgitem):

        if qtreewdgitem is None:
            return None

        if qtreewdgitem == self.maintreewdgitem:
            return -1

        compt = 0
        while  qtreewdgitem.parent() != self.maintreewdgitem:
            compt += 1
            qtreewdgitem = qtreewdgitem.parent()

        return compt

    # +-------------------------------+
    # |---------- SAVE JSON ----------|
    # +-------------------------------+

    def pbOKClicked(self):
        """
        Close widgetBareme, modifications are  saved
        """
        print("| {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        if not self.checkQualitative(self.maintreewdgitem):
            return

        # Fill self.dict
        if not self.dict:
            self.dict = {}
        self.dict.clear()
        self.visitTree(self.maintreewdgitem, self.dict)
        self.dict.setdefault("default", self.lValueOthers.text())

        # pprint(self.dict)

        self.showSimulationWidget()

    def checkQualitative(self, node):
        # print("Enter checkQualitative with", node.text(0))

        selectedItems = []

        # Get number of child
        childNr = node.childCount()

        if childNr > 0:
            # Loop through children
            for childItem in range(childNr):

                # Define current node
                child = node.child(childItem)

                # Check qualitative if grandchildren exists
                if child.childCount() > 0:
                    if not self.checkQualitative(child):
                        return False

                # Append selectedItems
                secondColumn = self.twBareme.itemWidget(child, 1)
                if isinstance(secondColumn, CheckableComboBox):
                    selectedItems.extend(secondColumn.getChecked())

        if len(set(selectedItems)) != len(selectedItems):
            titleErr = "Error at {node}".format(node=node.text(0))
            msgErr = "Expected: [{expected}] \nGot: [{got}]".format(expected=", ".join(set(selectedItems)),
                                                                   got=", ".join(selectedItems))
            QMessageBox.warning(None, titleErr, msgErr)
            return False
        return True

    def pbCancelClicked(self):
        """
        Close widgetBareme, modifications are not saved
        """
        # TODO: NE FONCTIONNE PAS ######################################################################################
        print("| {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Replace current treeWidget with saved one
        self.maintreewdgitem = self.qPushButttonPlus.tmpTreeWidget
        self.showSimulationWidget()

    def showSimulationWidget(self):
        """
        Close current window and open/show AMC window
        """
        if self.dbase.qgsiface is None:
            pass
        else:
            self.close()
            self.simulationWidget.show()

    def visitTree(self, node, dct, parentKey=""):
        """
        Iterate over the tree and build dct
        :param node: QTreeWidgetItem, current node
        :param dct: dict, contain elements from current node
        :param parentKey: str, current looped key. Init at "" for root
        """
        print("|__ Enter {fct}, node: {node}".format(fct=inspect.stack()[0][3], node=node.text(0))) if self.isDebug \
            else None

        if node.parent():

            # Get name
            name = node.text(0)

            # Get value
            secondColumn = self.twBareme.itemWidget(node, 1)
            value = None
            # Fetch QDoubleSpinBox or QComboBox value/text
            if isinstance(secondColumn, QDoubleSpinBox):
                value = secondColumn.value()
            elif isinstance(secondColumn, CheckableComboBox):
                value = secondColumn.getChecked()
                level = self.getItemLevel(node)
                tosavevalues=[]
                for elem in value:
                    tosavevalues.append(self.uniqueListRaw[level][self.uniqueListCst[level].index(elem)])
                value = tosavevalues


            # Get weighting
            spinboxValueWeighting = self.twBareme.itemWidget(node, 2)
            weighting = spinboxValueWeighting.value()

            dct.setdefault("name", name)
            dct.setdefault("value", value)
            dct.setdefault("weighting", weighting)

        # Get number of child
        childNr = node.childCount()

        if childNr > 0: # TODO: <----- Confirm necessity
            print("|____", node.text(0), "has child") if self.isDebug else None

            # Loop through children and add them to dct
            for childItem in range(childNr):

                # Define currentKey
                currentKey = str(parentKey) + str(childItem + 1)

                # Define current node
                child = node.child(childItem)
                dct.setdefault(currentKey, {})

                # Loop through children recursively
                self.visitTree(child, dct[currentKey], currentKey)

        print("|__ Exit {fct}, node: {node}".format(fct=inspect.stack()[0][3], node=node.text(0))) if self.isDebug \
            else None

    # +-------------------------------+
    # |---------- LOAD JSON ----------|
    # +-------------------------------+

    def loadFromJson(self, node, dct):
        """
        Load json file into qTreeWidget
        :param node: qTreeWidgetItem, current "row"
        :param dct: dict, current "row" data containing values and children
        """
        print("|__ Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        pprint(dct) if self.isDebug else None

        # dct's legit children
        realChildren = self.legitChildren(dct)
        print("|____ realChildren {realChildren}".format(realChildren=realChildren)) if self.isDebug else None

        # Loop through legit children
        for child in realChildren:
            # Create new item
            qtreewidgetitm = QTreeWidgetItem(node, [dct[child]["name"]])

            print("|____ child {child}".format(child=child)) if self.isDebug else None
            print("|____ self.types {types}".format(types=self.types)) if self.isDebug else None

            # Add widgets to item
            self.widgetsToNewItem(qtreewidgetitm)

            # Load widgets' properties
            self.loadWidgetProperties(qtreewidgetitm, dct[child]["value"], dct[child]["weighting"])

            # Recursive call
            self.loadFromJson(qtreewidgetitm, dct[child])

        print("|__ Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

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
            if isinstance(dct[element], dict):
                legitChildren.append(element)
        return legitChildren

    def loadWidgetProperties(self, qtreewidgetitm, value, weighting):
        """
        Load widget properties for each row
        """
        print("|____ Enter {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None

        # Set value
        # Get second column type
        secondColumn = self.twBareme.itemWidget(qtreewidgetitm, 1)
        if isinstance(secondColumn, QDoubleSpinBox):
            secondColumn.valueChanged.disconnect(self.reorderSpin)
            secondColumn.setValue(value)
            secondColumn.valueChanged.connect(self.reorderSpin)
        elif isinstance(secondColumn, CheckableComboBox):
            level = self.getItemLevel(qtreewidgetitm)
            cstvalues = []
            for elem in value:
                try:
                    cstvalues.append(self.uniqueListCst[level][self.uniqueListRaw[level].index(elem)])
                except ValueError:
                    pass

            secondColumn.setChecked(cstvalues)
        else:
            print("NOPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPOPOPOPPOPOOOOOOOOOOOOOOOOOOOOOOOOOOP")
            return

        # Set weighting
        weightingSpinBox = self.twBareme.itemWidget(qtreewidgetitm, 2)
        if weightingSpinBox :
            weightingSpinBox.setValue(weighting)

        print("|____ Exit {fct}".format(fct=inspect.stack()[0][3])) if self.isDebug else None



    def reorderSpin(self, spinsignal):

        sender = self.sender()
        iterator = QTreeWidgetItemIterator(self.maintreewdgitem, QTreeWidgetItemIterator.All)
        while iterator.value():
            item = iterator.value()
            wdg = self.twBareme.itemWidget(item, 1)
            if True and wdg == sender:
                tempdict={}
                self.visitTree(item, tempdict, '1')
                currentitem = item
                currentitemparent = item.parent()
                currentitemindex = currentitemparent.indexOfChild(item)
                currentspinboxvalue = sender.value()

                if True:
                    currentitem = item
                    currentitemvalues = (self.twBareme.itemWidget(currentitem, 1).value(), self.twBareme.itemWidget(currentitem, 2).value())
                    currentitemparent = item.parent()
                    currentitemindex = currentitemparent.indexOfChild(item)
                    currentspinboxvalue = sender.value()

                break
            iterator += 1

        if True:
            if currentitemparent.childCount() > 1 :

                child = currentitemparent.takeChild(currentitemindex)
                child.takeChildren()

                for childindex in range(currentitemparent.childCount() ):

                    childspinboxvalue = self.twBareme.itemWidget(currentitemparent.child(childindex), 1).value()
                    if childspinboxvalue > currentspinboxvalue:
                        currentitemparent.insertChild(childindex, child)


                        if True:
                            self.widgetsToNewItem(child)
                            self.twBareme.itemWidget(child, 1).disconnect()
                            self.twBareme.itemWidget(child, 1).setValue(currentitemvalues[0])
                            self.twBareme.itemWidget(child, 2).setValue(currentitemvalues[1])
                            self.twBareme.itemWidget(child, 1).setFocus()
                            self.twBareme.itemWidget(child, 1).valueChanged.connect(self.reorderSpin)

                        self.loadFromJson(child, tempdict)

                        break


                    if childindex == currentitemparent.childCount() -1:
                        currentitemparent.insertChild(childindex +1, child)

                        if True:
                            self.widgetsToNewItem(child)
                            self.twBareme.itemWidget(child, 1).disconnect()
                            self.twBareme.itemWidget(child, 1).setValue(currentitemvalues[0])
                            self.twBareme.itemWidget(child, 2).setValue(currentitemvalues[1])
                            self.twBareme.itemWidget(child, 1).setFocus()
                            self.twBareme.itemWidget(child, 1).valueChanged.connect(self.reorderSpin)

                        self.loadFromJson(child, tempdict)

