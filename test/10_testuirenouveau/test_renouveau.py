from qgis.PyQt import uic, QtCore
import os, sys


try:
    from qgis.PyQt.QtGui import (QWidget,QDialog,QMainWindow,QApplication,QTreeWidgetItem,
                                 QMenu,QToolButton,QSpinBox,QDoubleSpinBox,QHeaderView,QLineEdit)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow,QApplication,QTreeWidgetItem,
                                     QMenu,QToolButton,QSpinBox,QDoubleSpinBox,QHeaderView,QLineEdit)



class UserUI(QMainWindow):

    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'main.ui')
        uic.loadUi(uipath, self)

        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.openMenu)

        self.maintreewdgitem = QTreeWidgetItem(self.treeWidget.invisibleRootItem(),['note'])

        headerlist = ['criteres', 'bareme', 'ponderation']
        self.treeWidget.setHeaderItem(QTreeWidgetItem(headerlist))

        self.treeWidget.header().setStretchLastSection(False)
        self.treeWidget.header().resizeSection(1,100)
        self.treeWidget.header().resizeSection(2, 100)
        self.treeWidget.header().setResizeMode(0, QHeaderView.Stretch)

        self.treeWidget.itemDoubleClicked.connect(self.itemdoubleclicked)
        self.treeWidget.itemChanged.connect(self.treeitemChanged)

        self.menuitem = None
        self.itemnameediting = None

    def treeitemChanged(self,itemchanged, column):
        self.treeWidget.closePersistentEditor(self.itemnameediting, 0)
        self.itemnameediting = None

    def itemdoubleclicked(self,itemclicked):
        print(itemclicked.text(0))
        if itemclicked == self.maintreewdgitem:
            return
        self.itemnameediting = itemclicked
        self.treeWidget.openPersistentEditor(itemclicked, 0)

    def openMenu(self,position):
        menu = QMenu()
        self.menuitem = self.treeWidget.currentItem()
        indexes = self.treeWidget.selectedIndexes()

        print(indexes, position)
        menu.addAction(self.tr("Add critere"))
        menu.addAction(self.tr("Rename critere"))
        menu.addAction(self.tr("Remove critere"))
        menu.triggered.connect(self.menuaction)

        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))

    def menuaction(self,actionname):
        print('ok',actionname)
        if actionname.text() == self.tr("Add critere"):
            lineedit = QLineEdit()
            #self.treeWidget.setItemWidget(qtreewidgetitm, 1, qbutton)
            qtreewidgetitm = QTreeWidgetItem(self.menuitem,['nouveau critere'])
            #qtreewidgetitm.setFlags(QtCore.Qt.ItemIsEditable)

            #lineedit = QLineEdit()
            #self.treeWidget.setItemWidget(qtreewidgetitm, 0, lineedit)

            qbutton = QToolButton()
            self.treeWidget.setItemWidget(qtreewidgetitm,1,qbutton)
            qbutton.clicked.connect(self.baremebuttonpressed)
            spinbox = QDoubleSpinBox()
            self.treeWidget.setItemWidget(qtreewidgetitm, 2, spinbox)
            self.menuitem.setExpanded(True)

            #self.treeWidget.resizeColumnToContents(0)

    def baremebuttonpressed(self,clickbool):
        barememenuitem = self.treeWidget.currentItem()
        print(self.sender().objectName())
        print(barememenuitem.text(0))
        print('ok')


app = QApplication(sys.argv)
mainwin = UserUI()
mainwin.show()
sys.exit(app.exec_())



