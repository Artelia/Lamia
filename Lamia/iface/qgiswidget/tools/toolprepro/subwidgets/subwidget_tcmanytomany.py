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
                                    QComboBox, QAbstractItemView,QMessageBox,QDialog)
from qgis.PyQt import uic, QtCore

from .subwidget_abstract import AbstractSubWidget

class TcmanytomanyChooserWidget(AbstractSubWidget):



    def __init__(self, 
                parentwdg ,
                tcmanytomanyname,
                childtablename,
                parentmanytomanyfield,
                childmanytomanyfield,
                childdisplayfields=[],
                tcmanytomanydisplayfields=[]):
        super(TcmanytomanyChooserWidget, self).__init__(parent=parentwdg)
        uipath = os.path.join(os.path.dirname(__file__), 'subwidget_tcmanytomany_ui.ui')
        uic.loadUi(uipath, self)

        self.parentwdg = parentwdg
        self.parenttablename = self.parentwdg.DBASETABLENAME
        
        self.childtablename = childtablename
        self.childdisplayfields = childdisplayfields
        if not f'pk_{childtablename}' in childdisplayfields:
            self.childdisplayfields.insert(0,f'pk_{childtablename}')

        self.tcmanytomanydisplayfields = tcmanytomanydisplayfields
        self.tcmanytomanyname = tcmanytomanyname
        self.parentmanytomanyfield = parentmanytomanyfield
        self.childmanytomanyfield = childmanytomanyfield

        #tabconf
        self.toolButton_add.clicked.connect(lambda: self.addChild())
        self.toolButton_remove.clicked.connect(self.removeChild)

        self.headerfields = self.childdisplayfields + self.tcmanytomanydisplayfields
        self.tableWidget_actors.setRowCount(0)
        self.tableWidget_actors.setColumnCount(len(self.headerfields))
        self.tableWidget_actors.setHorizontalHeaderLabels([field.title() for field in self.headerfields])
        self.tableWidget_actors.setColumnHidden(0, True)
        self.tableWidget_actors.setSelectionBehavior(QAbstractItemView.SelectRows)


        #cheat
        self.sqlwholetable = f" FROM {childtablename}_now \
                            INNER JOIN {self.tcmanytomanyname} ON {self.tcmanytomanyname}.l{self.childmanytomanyfield} = {childtablename}_now.{self.childmanytomanyfield} \
                            INNER JOIN {self.parenttablename}_now ON {self.tcmanytomanyname}.l{self.parentmanytomanyfield} = {self.parenttablename}_now.{self.parentmanytomanyfield} "
        
        self.rubberBand = None
        self.isspatial = False
        if self.parentwdg.dbase.isTableSpatial(self.childtablename):
            self.isspatial = True
            self.parentwdg.mainifacewidget.qgiscanvas.createorresetRubberband(type=0, instance=self)
            self.tableWidget_actors.itemSelectionChanged.connect(self._cellChanged)
            self.toolButton_add.setText('Pick')


    def postSelectFeature(self):
        #init table
        qgiscanvas = self.parentwdg.mainifacewidget.qgiscanvas
        qgiscanvas.createorresetRubberband(instance=self)
        self.tableWidget_actors.setRowCount(0)
        pkparent = self.parentwdg.currentFeaturePK
        if pkparent is None:
            self.setEnabled(False)
            # self.parentwdg.mainifacewidget.connector.showErrorMessage(QtCore.QCoreApplication.translate('base3','Save first'))
            return
        self.setEnabled(True)
        fieldlist = [self.childdisplayfields[0]] +  self.tcmanytomanydisplayfields

        #get linked child
        sql = f"SELECT  {', '.join(fieldlist)} "
        sql += self.sqlwholetable 
        sql += f" WHERE {self.parenttablename}_now.pk_{self.parenttablename} = {pkparent}"
        sql = self.parentwdg.dbase.sqlNow(sql)
        res = self.parentwdg.dbase.query(sql)
        if res:
            for reslist in res:
                if len(reslist)>1:
                    self.addChild(reslist[0],reslist[1:])
                else:   #no manytomanyfield
                    self.addChild(reslist[0])

        self._resizeLastSection()


    def postSaveFeature(self, parentfeaturepk=None):
        
        # self.parentmanytomanyfield

        idparentmanytomanyfield = self.parentwdg.dbase.getValuesFromPk(self.parenttablename + '_qgis',
                                                             self.parentmanytomanyfield,
                                                             parentfeaturepk)

        for rowindex in range(self.tableWidget_actors.rowCount()):
            pkchild = int(self.tableWidget_actors.item(rowindex, 0).text())
            idchildmanytomanyfield = self.parentwdg.dbase.getValuesFromPk(self.childtablename + '_qgis',
                                                                        self.childmanytomanyfield,
                                                                        pkchild)
            childdisplayres = []
            for i, tcmanytomanyfield in enumerate(self.tcmanytomanydisplayfields):
                columnindex = len(self.childdisplayfields) + i
                combo = self.tableWidget_actors.cellWidget(rowindex, columnindex)
                tcraw, tclong = self._getfieldrawlong(self.tcmanytomanyname,tcmanytomanyfield)
                roleindex = combo.currentIndex()
                rolerawvalue = tcraw[roleindex]
                if rolerawvalue == '':
                    rolerawvalue = 'NULL'
                else:
                    rolerawvalue = "'" + rolerawvalue + "'"
                childdisplayres.append(rolerawvalue)

            sql = f"SELECT pk_{self.tcmanytomanyname} FROM  {self.tcmanytomanyname} \
                    WHERE l{self.parentmanytomanyfield} = {idparentmanytomanyfield} \
                    AND l{self.childmanytomanyfield } = {idchildmanytomanyfield}"
            if self.tcmanytomanydisplayfields:
                for i, field in enumerate(self.tcmanytomanydisplayfields):
                    res =  childdisplayres[i] 
                    if res == 'NULL':
                        sql += f" AND {field} IS NULL"
                    else:
                        sql += f" AND {field} = {res}"
            res = self.parentwdg.dbase.query(sql)

            if not res:
                dbasemaxrevision= self.parentwdg.dbase.maxrevision
                fieldtoinsert = ['lpk_revision_begin','l' + self.parentmanytomanyfield,'l' + self.childmanytomanyfield] + self.tcmanytomanydisplayfields
                valuetoinsert = [str(dbasemaxrevision), str(idparentmanytomanyfield), str(idchildmanytomanyfield)] + childdisplayres
                sql = f"INSERT INTO {self.tcmanytomanyname}({','.join(fieldtoinsert)}) VALUES({','.join(valuetoinsert)})"
                res = self.parentwdg.dbase.query(sql)
        self._resizeLastSection()


    def addChild(self, pkchild=None, tcmanytomanyres=None):

        if pkchild is None: #come from click
            pkchild = self._childChooser()
        
        if pkchild is None:
            return

        pkparent = self.parentwdg.currentFeaturePK
        values = self.parentwdg.dbase.getValuesFromPk(f'{self.childtablename}_qgis',
                                                    self.childdisplayfields,
                                                    pkchild)
        longvalues=[self.parentwdg.dbase.getConstraintTextFromRawValue(self.childtablename, self.childdisplayfields[i], values[i])
                    for i in range(len(self.childdisplayfields))]

        #put values
        introw = self.tableWidget_actors.rowCount()
        self.tableWidget_actors.insertRow(introw)
        for i, val in enumerate(longvalues):
            field = self.headerfields[i]
            item = QTableWidgetItem(str(val))
            self.tableWidget_actors.setItem(introw, i, item)

        #tc cell
        for i, tcmanytomanyfield in enumerate(self.tcmanytomanydisplayfields):

            if 'Cst' in self.parentwdg.dbase.dbasetables['tcobjectactor']['fields']['role'].keys():
                tcraw, tclong = self._getfieldrawlong(self.tcmanytomanyname,tcmanytomanyfield)
                combobox = QComboBox()
                combobox.addItems(tclong)
                self.tableWidget_actors.setCellWidget(introw , self.tableWidget_actors.columnCount() -1, combobox)
                if tcmanytomanyres and tcmanytomanyres[i] is not None:
                    tcmanytomanyre = tcmanytomanyres[i]
                    comboindex = tcraw.index(tcmanytomanyre)
                    combobox.setCurrentIndex(comboindex)

        #display
        self._resizeLastSection()

    def _childChooser(self):
        if not self.isspatial:
            sql = f"SELECT {',' .join(self.childdisplayfields)} FROM {self.childtablename}_now"
            sql = self.parentwdg.dbase.sqlNow(sql)
            res = self.parentwdg.dbase.query(sql)
            itemsforinputdialog = []
            for row in res:
                itemsforinputdialog.append(', '.join([str(elem) for elem in row]))
            item, ok = QInputDialog.getItem(self, "select actor", 
                "list of actors", itemsforinputdialog, 0, False)
            if ok and item:
                pkchild = int(item.split(', ')[0])
                self.parentwdg.updateFormTitleBackground(subwidgethaschanged=True)
                return pkchild
            else:
                return None
        else:
            self.parentwdg.mainifacewidget.qgiscanvas.captureGeometry(fctonstopcapture=self.stopCapture,
                                                                       listpointinitialgeometry=[])
            return None

    def stopCapture(self,points):
        qgiscanvas = self.parentwdg.mainifacewidget.qgiscanvas
        pkchild, dist = qgiscanvas.getNearestPk(self.childtablename, points[0])
        self.addChild(pkchild)
        self.tableWidget_actors.selectRow(self.tableWidget_actors.rowCount() - 1)
        qgiscanvas.stopCapture()


    def removeChild(self):
        indexrowtodelete=[]
        for qtrow in self.tableWidget_actors.selectionModel().selectedRows():
            self.parentwdg.updateFormTitleBackground(subwidgethaschanged=True)
            rowindex = qtrow.row()
            pkchild = int(self.tableWidget_actors.item(rowindex, 0).text())
            idchild = self.parentwdg.dbase.getValuesFromPk(self.childtablename + '_qgis',
                                                            self.childmanytomanyfield,
                                                            pkchild)
            parentidobjet = self.parentwdg.dbase.getValuesFromPk(self.parenttablename + '_qgis',
                                                            self.parentmanytomanyfield,
                                                            self.parentwdg.currentFeaturePK)
            tcmanytomanyfieldvalues=[]
            for i, tcmanytomanyfield in enumerate(self.tcmanytomanydisplayfields):
                columnindex = len(self.childdisplayfields) + i
                tcraw, tclong = self._getfieldrawlong(self.tcmanytomanyname,tcmanytomanyfield)
                combo = self.tableWidget_actors.cellWidget(rowindex, columnindex)
                roleindex = combo.currentIndex()
                rolerawvalue = tcraw[roleindex]
                if rolerawvalue == '':
                    rolerawvalue = 'NULL'
                else:
                    rolerawvalue = "'" + rolerawvalue + "'"
                tcmanytomanyfieldvalues.append(rolerawvalue)

            # sql = f"DELETE FROM tcobjectactor WHERE lid_object = {parentidobjet}  AND lid_actor = {idactor}"
            sql = f"DELETE FROM {self.tcmanytomanyname} \
                     WHERE l{self.parentmanytomanyfield} = {parentidobjet}  \
                    AND l{self.childmanytomanyfield} = {idchild}"

            for i, tcmanytomanyfield in enumerate(self.tcmanytomanydisplayfields):
                res = tcmanytomanyfieldvalues[i]
                if res == 'NULL':
                    sql += f" AND {tcmanytomanyfield} IS NULL"
                else:
                    sql += f" AND {tcmanytomanyfield} = {res}"
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
        self.tableWidget_actors.update()

    def _getfieldrawlong(self,tablename,fieldname):
        fieldraw = [elem[1] for elem in self.parentwdg.dbase.dbasetables[tablename]['fields'][fieldname]['Cst']]
        fieldlong = [elem[0] for elem in self.parentwdg.dbase.dbasetables[tablename]['fields'][fieldname]['Cst']]
        return fieldraw, fieldlong

    def _cellChanged(self):
        qgiscanvas = self.parentwdg.mainifacewidget.qgiscanvas
        geoms=[]
        for qtrow in self.tableWidget_actors.selectionModel().selectedRows():
            currentRow = qtrow.row()
            pkchild = int(self.tableWidget_actors.item(currentRow, 0).text())
            geoms.append(qgiscanvas.getQgsGeomFromPk(self.parentwdg.dbase, self.childtablename, pkchild))
        qgiscanvas.createRubberBandForSelection(geoms,instance=self)


class pickerDialog(QDialog):
    def __init__(self, qgiscanvas):
        super().__init__(None)
        self.qgiscanvas = qgiscanvas
        self.setWindowTitle("Dialog")
        """
            def captureGeometry(self, 
                        capturetype=0,
                        fctonstopcapture=None,
                        listpointinitialgeometry=[]):
        """
        self.qgiscanvas.captureGeometry(fctonstopcapture=self.stopCapture)

    def stopCapture(self,points):
        print(points)

