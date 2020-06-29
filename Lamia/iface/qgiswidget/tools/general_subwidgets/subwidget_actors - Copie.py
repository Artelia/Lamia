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
import os, logging

from qgis.PyQt.QtWidgets import (QWidget, QVBoxLayout,QTableWidgetItem, QHeaderView, QInputDialog,
                                    QComboBox, QAbstractItemView)
from qgis.PyQt import uic, QtCore

from .subwidget_abstract import AbstractSubWidget

class ActorChooserWidget(AbstractSubWidget):



    def __init__(self, parentwdg=None ,
                        tcmanytomanyname,
                        childtablename,
                        parentmanytomanyconf,
                        childmanytomanyconf,

                        actorfields=[]):
        super(ActorChooserWidget, self).__init__(parent=parentwdg)
        uipath = os.path.join(os.path.dirname(__file__), 'subwidget_actors_ui.ui')
        uic.loadUi(uipath, self)

        self.parentwdg = parentwdg
        if actorfields:
            self.actorfields = actorfields
        else:
            self.actorfields = ['actorname', 'society']
        self.actorfields.insert(0,'pk_actor')
        # self.actorfields.insert(len(self.actorfields),'role')

        self.toolButton_add.clicked.connect(lambda: self.addActor())
        self.toolButton_remove.clicked.connect(self.removeActor)

        self.tableWidget_actors.setRowCount(0)
        self.tableWidget_actors.setColumnCount(len(self.actorfields) + 1)
        self.tableWidget_actors.setHorizontalHeaderLabels([field.title() for field in (self.actorfields + ['role'])])
        self.tableWidget_actors.setColumnHidden(0, True)
        self.tableWidget_actors.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.parenttablename = self.parentwdg.DBASETABLENAME
        self.sqlwholetable = f" FROM actor_now INNER JOIN tcobjectactor ON tcobjectactor.lid_actor = actor_now.id_actor \
                INNER JOIN {self.parenttablename}_now ON tcobjectactor.lid_object = {self.parenttablename}_now.id_object "
        self.rolesraw = [elem[1] for elem in self.parentwdg.dbase.dbasetables['tcobjectactor']['fields']['role']['Cst']]
        self.roleslong = [elem[0] for elem in self.parentwdg.dbase.dbasetables['tcobjectactor']['fields']['role']['Cst']]


    def postSelectFeature(self):
        #init table
        self.tableWidget_actors.setRowCount(0)
        pkparent = self.parentwdg.currentFeaturePK
        if pkparent is None:
            return

        #get linked actors
        sql = "SELECT pk_actor, role " + self.sqlwholetable 
        sql += f" WHERE {self.parenttablename}_now.pk_{self.parenttablename} = {pkparent}"
        sql = self.parentwdg.dbase.sqlNow(sql)
        res = self.parentwdg.dbase.query(sql)
        if res:
            for (pkactor, role) in res:
                self.addActor(pkactor,role)
        self._resizeLastSection()


    def postSaveFeature(self, parentfeaturepk=None):
        idobjectparent = self.parentwdg.dbase.getValuesFromPk(self.parenttablename + '_qgis',
                                                             'id_object',
                                                             parentfeaturepk)

        for rowindex in range(self.tableWidget_actors.rowCount()):
            pkactor = int(self.tableWidget_actors.item(rowindex, 0).text())
            idactor = self.parentwdg.dbase.getValuesFromPk('actor',
                                                             'id_actor',
                                                             pkactor)
            combo = self.tableWidget_actors.cellWidget(rowindex, self.tableWidget_actors.columnCount() - 1)
            roleindex = combo.currentIndex()
            rolerawvalue = self.rolesraw[roleindex]
            sql = f"SELECT pk_tcobjectactor FROM tcobjectactor \
                    WHERE lid_object = {idobjectparent} AND lid_actor = {idactor} \
                    AND role = '{rolerawvalue}'"
            res = self.parentwdg.dbase.query(sql)
            if not res:
                dbasemaxrevision= self.parentwdg.dbase.maxrevision


                sql = f"INSERT INTO tcobjectactor(lpk_revision_begin,lid_actor,lid_object,role) \
                    VALUES({dbasemaxrevision}, {idactor}, {idobjectparent}, '{rolerawvalue}')"
                res = self.parentwdg.dbase.query(sql)
        self._resizeLastSection()


    def addActor(self, pkactor=None, role=None):

        if pkactor is None: #come from click
            sql = f"SELECT {',' .join(self.actorfields)} FROM actor_now"
            sql = self.parentwdg.dbase.sqlNow(sql)
            res = self.parentwdg.dbase.query(sql)
            itemsforinputdialog = []
            for row in res:
                itemsforinputdialog.append(', '.join([str(elem) for elem in row]))
            item, ok = QInputDialog.getItem(self, "select actor", 
                "list of actors", itemsforinputdialog, 0, False)
            if ok and item:
                pkactor = int(item.split(', ')[0])
                self.parentwdg.updateFormTitleBackground(subwidgethaschanged=True)
            else:
                return

        pkparent = self.parentwdg.currentFeaturePK
        headerfields = self.actorfields + ['role']
        values = self.parentwdg.dbase.getValuesFromPk('actor_qgis',
                                                    self.actorfields,
                                                    pkactor)
        #put values
        introw = self.tableWidget_actors.rowCount()
        self.tableWidget_actors.insertRow(introw)
        for i, val in enumerate(values):
            field = headerfields[i]
            item = QTableWidgetItem(str(val))
            self.tableWidget_actors.setItem(introw, i, item)

        #role cell
        combobox = QComboBox()
        combobox.addItems(self.roleslong)
        self.tableWidget_actors.setCellWidget(introw , self.tableWidget_actors.columnCount() -1, combobox)
        if role:
            comboindex = self.rolesraw.index(role)
            combobox.setCurrentIndex(comboindex)
        #display
        self._resizeLastSection()

        

    def removeActor(self):
        indexrowtodelete=[]
        for qtrow in self.tableWidget_actors.selectionModel().selectedRows():
            self.parentwdg.updateFormTitleBackground(subwidgethaschanged=True)
            rowindex = qtrow.row()
            pkactor = int(self.tableWidget_actors.item(rowindex, 0).text())
            idactor = self.parentwdg.dbase.getValuesFromPk('actor_qgis',
                                                            'id_actor',
                                                            pkactor)
            parentidobjet = self.parentwdg.dbase.getValuesFromPk(self.parenttablename + '_qgis',
                                                            'id_object',
                                                            self.parentwdg.currentFeaturePK)
            combo = self.tableWidget_actors.cellWidget(rowindex, self.tableWidget_actors.columnCount() - 1)
            roleindex = combo.currentIndex()
            rolerawvalue = self.rolesraw[roleindex]
            sql = f"DELETE FROM tcobjectactor WHERE lid_object = {parentidobjet} \
                  AND lid_actor = {idactor} AND role='{rolerawvalue}'"
            self.parentwdg.dbase.query(sql)
            indexrowtodelete.append(rowindex)

        if indexrowtodelete:
            for indexrow in sorted(indexrowtodelete, reverse=True):
                self.tableWidget_actors.removeRow(indexrow)
        self._resizeLastSection()

    def _resizeLastSection(self):
        header = self.tableWidget_actors.horizontalHeader()
        header.resizeSections(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)