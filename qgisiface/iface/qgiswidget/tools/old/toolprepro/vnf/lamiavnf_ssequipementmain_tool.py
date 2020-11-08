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
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import sys
"""
from ..toolprepro.InspectionDigue_photos_tool import PhotosTool
from ..toolprepro.InspectionDigue_observation_tool import ObservationTool
from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
"""

from .lamiavnf_sousequipement_tool import SousEquipementTool
import io

class EquipementMainTool(AbstractInspectionDigueTool):

    LOADFIRST = False
    # dbasetablename = 'Equipement'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(EquipementMainTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Description'
        self.NAME = 'Proprietes'
        # self.visualmode = [1]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None


        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()

            self.dbasechildwdgfield = []
            self.propertieswdgPropriete = SousEquipementTool(dbase=self.dbase,
                                                              linkedtreewidget=self.userwdgfield.treeWidget_proprietes,
                                                              # dialog = self.windowdialog,
                                                              parentwidget=self)


            self.userwdgfield.frame.layout().addWidget(self.propertieswdgPropriete)


            #self.userwdgfield.treeWidget_proprietes.itemSelectionChanged.connect(self.treewidgetchanged)
            #self.userwdgfield.treeWidget_proprietes.activated.connect(self.treewidgetactivated)



    def treewidgetchanged(self):
        print('changed')





        if False:
            self.propertieswdgPropriete.disconnectIdsGui()
            self.propertieswdgPropriete.saveFeature()
            self.propertieswdgPropriete.connectIdsGui()
            #self.userwdgfield.treeWidget_proprietes.itemSelectionChanged.disconnect(self.treewidgetchanged)
            #self.propertieswdgPropriete.saveFeature()
            #self.userwdgfield.treeWidget_proprietes.itemSelectionChanged.connect(self.treewidgetchanged)
        #self.propertieswdgPropriete.saveFeature()


    def treewidgetactivated(self):
        print('activated')


    def postOnActivation(self):
        pass
        # self.propertieswdgPropriete.connectIdsGui()
        # self.propertieswdgPropriete.onActivationRaw()

    def postOnDesactivation(self):
        pass

    def postInitFeatureProperties(self, feat):
        if self.userwdgfield.treeWidget_proprietes.invisibleRootItem().childCount()>0:
            wdgchildzero = self.userwdgfield.treeWidget_proprietes.invisibleRootItem().child(0)
            self.userwdgfield.treeWidget_proprietes.setCurrentItem(wdgchildzero)


    def loadIds(self):
        # objetid = int(self.parentWidget.linkedtreewidget.currentItem().text(0))
        # self.disconnectIdsGui()
        self.propertieswdgPropriete.disconnectIdsGui()

        if False:

            try:
                self.propertieswdgPropriete.linkedtreewidget.currentItemChanged.disconnect(self.propertieswdgPropriete.doSaveJob)
            except:
                pass

        ids = []
        if self.parentWidget.currentFeature is not None:

            self.userwdgfield.treeWidget_proprietes.clear()
            sql = "SELECT id_propriete_option, propriete FROM Propriete_option "
            sql += " WHERE lk_equipement = " + str(self.parentWidget.currentFeature['id_equipement'])
            query = self.dbase.query(sql)
            ids = [list(row) for row in query]
            # print(ids)
            for id in ids:
                id[1] = self.dbase.getConstraintTextFromRawValue('Propriete_option','propriete',id[1])
            # print(ids)

            headerlist = ['ID', 'Nom']
            #headerlist.insert(0,'ID')
            self.userwdgfield.treeWidget_proprietes.setColumnCount(len(headerlist))
            self.userwdgfield.treeWidget_proprietes.header().setVisible(True)
            self.userwdgfield.treeWidget_proprietes.header().setSectionHidden(0,True)

            self.userwdgfield.treeWidget_proprietes.setHeaderItem(QTreeWidgetItem(headerlist))
            header = self.userwdgfield.treeWidget_proprietes.header()
            lenheaderlist = len(headerlist)
            for i in range(lenheaderlist):
                header.setResizeMode(i, QHeaderView.ResizeToContents)
            header.setResizeMode(lenheaderlist-1, QHeaderView.Stretch)

            rootiitem = self.userwdgfield.treeWidget_proprietes.invisibleRootItem()
            treefeatlist = [[id[0], QTreeWidgetItem([str(id[i]) for i in range(1)])] for id in ids]
            rootiitem.addChildren([elem[1] for elem in treefeatlist])

            for i, wdgitem in enumerate([elem[1] for elem in treefeatlist]):
                label = QLabel(ids[i][1])
                label.setWordWrap(True)
                self.userwdgfield.treeWidget_proprietes.setItemWidget(wdgitem, 1, label)
                if i%2 == 0:
                    if sys.version_info.major == 2:
                        wdgitem.setBackgroundColor(1,QtGui.QColor('lightGray'))


            # self.onActivationRaw(elem[1][0])

        if False:
            #
            self.propertieswdgPropriete.linkedtreewidget.currentItemChanged.connect(self.propertieswdgPropriete.doSaveJob)
            self.propertieswdgPropriete.connectIdsGui()
        self.propertieswdgPropriete.connectIdsGui()
        return ids




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiavnf_ssequipementmain_tool_ui.ui')
        uic.loadUi(uipath, self)