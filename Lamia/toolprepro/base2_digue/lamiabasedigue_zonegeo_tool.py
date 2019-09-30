# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QTableWidgetItem)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QTableWidgetItem)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_zonegeo_tool import BaseZonegeoTool
import os
import datetime



class BaseDigueZonegeoTool(BaseZonegeoTool):

    LOADFIRST = False
    dbasetablename = 'Zonegeo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseDigueZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initFieldUI(self):
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Zonegeo' : {'linkfield' : 'id_zonegeo',
                                             'widgets' : {'typezonegeo':self.userwdgfield.comboBox_type,

                                                          'BV_superficie':self.userwdgfield.doubleSpinBox_superf,
                                                          'BV_cheminhydrau': self.userwdgfield.doubleSpinBox_chem,
                                                           'BV_pente': self.userwdgfield.doubleSpinBox_pente,
                                                 'BV_coefruissellement': self.userwdgfield.doubleSpinBox_coef,

                                                 'BV_capacite': self.userwdgfield.doubleSpinBox_perret,


                                                        }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {
                                                        'libelle' : self.userwdgfield.lineEdit_nom,
                                              'commentaire': self.userwdgfield.textBrowser_com,
                                                        }}}

            # rem : il sera affiné le select avec le champ datetimecreation trouvé dans la requete
            # il faut que zone geo soit présent dans la requete
            self.stats = [['Infralineaire lineaire',
                           ''' SELECT SUM(ST_Length(ST_MakeValid(Infralineaire_now.geom))) 
                                FROM Infralineaire_now, Zonegeo 
                                WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom), ST_MakeValid(Zonegeo.geom)) ''']
                           ]

            self.userwdgfield.tableWidget_stats.setRowCount(0)
            self.userwdgfield.tableWidget_stats.setColumnCount(2)
            self.userwdgfield.tableWidget_stats.horizontalHeader().setStretchLastSection(True)
            for i, stat in enumerate(self.stats):
                rowPosition = self.userwdgfield.tableWidget_stats.rowCount()
                self.userwdgfield.tableWidget_stats.insertRow(rowPosition)
                itemfield = QTableWidgetItem(stat[0])
                itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.userwdgfield.tableWidget_stats.setItem(rowPosition, 0, itemfield)



            self.userwdgfield.toolButton_superf.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_superf))
            self.userwdgfield.toolButton_chem.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_chem))
            self.userwdgfield.toolButton_pente.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_pente))
            self.userwdgfield.toolButton_coef.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_coef))
            self.userwdgfield.toolButton_perret.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_perret))

            self.userwdgfield.comboBox_type.currentIndexChanged.connect(self.combotypeChanged)
            self.userwdgfield.comboBox_type.currentIndexChanged.emit(0)



    def combotypeChanged(self, currentindex):
        if self.userwdgfield.comboBox_type.currentText() == 'Bassin versant':
            self.userwdgfield.stackedWidget.setCurrentIndex(1)
        else:
            self.userwdgfield.stackedWidget.setCurrentIndex(0)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_zonegeo_tool_ui.ui')
        uic.loadUi(uipath, self)