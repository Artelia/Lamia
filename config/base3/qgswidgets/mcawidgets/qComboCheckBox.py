from qgis.PyQt import QtGui, QtCore


try:
    from qgis.PyQt.QtGui import (QComboBox, QItemDelegate, QCheckBox)
except ImportError:
    from qgis.PyQt.QtWidgets import (QComboBox, QItemDelegate, QCheckBox)


import sys, os
import inspect







class CheckableComboBox(QComboBox):

    def __init__(self):
        super(CheckableComboBox, self).__init__()
        delegate = CheckBoxDelegate()
        self.setItemDelegate(delegate)

    def addItem(self, item):
        super(CheckableComboBox, self).addItem(item)
        item = self.model().item(self.count()-1, 0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)

    def getChecked(self):
        """
        Loop through CheckableComboBox and return checked items
        :return: list, items checked
        """
        print("|____ Enter {fct}".format(fct=inspect.stack()[0][3])) if False else None

        checkedItems = []
        for index in range(self.count()):
            if self.model().item(index).checkState():
                checkedItems.append(self.itemText(index))

        print("|____ Exit {fct}".format(fct=inspect.stack()[0][3])) if False else None
        return checkedItems

    def setChecked(self, lst):
        """
        Check item if in list
        :param lst: str, items to be checked
        """
        print("|____ Enter {fct}".format(fct=inspect.stack()[0][3])) if False else None

        for index in range(self.count()):
            if self.itemText(index) in lst:
                self.model().item(index).setCheckState(QtCore.Qt.Checked)

        print("|____ Exit {fct}".format(fct=inspect.stack()[0][3])) if False else None


class CheckBoxDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(CheckBoxDelegate, self).__init__(parent)

    def createEditor(parent, op, idx):
        self.editor = QCheckBox(parent)