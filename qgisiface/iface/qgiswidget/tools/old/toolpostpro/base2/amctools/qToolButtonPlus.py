# -*- coding: utf-8 -*-


try:
    from qgis.PyQt.QtGui import (QPushButton, QTreeWidgetItem)
except ImportError:
    from qgis.PyQt.QtWidgets import (QPushButton, QTreeWidgetItem)

# Import Bareme class
from .widgetBareme import WidgetBareme


class QPushButtonPlus(QPushButton):

    def __init__(self, simulationWidget, qtreewidgetitm):
        super(QPushButtonPlus, self).__init__()

        # Init attributes
        self.simulationWidget = simulationWidget
        self.qtreewidgetitm = qtreewidgetitm

        # Create WidgetBareme
        self.baremeWidget = WidgetBareme(self)
        self.tmpTreeWidget = None

        self.clicked.connect(self.buttonPressed)

    def buttonPressed(self):
        """
        Create/Load and open widgetBareme
        """

        # Fill treeWidget if dataframe is None
        if False and self.baremeWidget.df is None:
            self.baremeWidget.initBareme()

        success = self.baremeWidget.initBareme()
        if not success:
            self.simulationWidget.appendMessage('Dbase not updated - values not available')
            return

        # Save current treeWidget
        # TODO: NE FONCTIONNE PAS ######################################################################################

        # Créer copie #############################
        # self.tmpTreeWidget = QTreeWidgetItem(self.baremeWidget.maintreewdgitem)
        self.tmpTreeWidget = self.baremeWidget.maintreewdgitem.clone()
        # root = self.baremeWidget.maintreewdgitem.topLevelItem(0)
        # self.tmpTreeWidget = root.clone()

        # Hide self.simulationWidget and open self.baremeWidget
        if self.simulationWidget.dbase.qgsiface is None:
            self.baremeWidget.exec_()
        else:
            self.simulationWidget.hide()
            self.baremeWidget.show()

    def getDataframe(self):
        return self.baremeWidget.df

    def setDataframe(self):
        self.baremeWidget.df = None

    # def setEnable(self):

