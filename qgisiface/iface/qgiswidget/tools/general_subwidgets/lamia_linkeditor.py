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

from qgis.PyQt.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidgetItem,
    QHeaderView,
    QInputDialog,
    QComboBox,
    QAbstractItemView,
    QMessageBox,
    QDialog,
    QVBoxLayout,
)
from qgis.PyQt import uic, QtCore
from Lamia.api.libslamia.dbaseutils.chooserid import IDChooser


class LamiaLinkEditor(QDialog):

    UIPATH = os.path.join(os.path.dirname(__file__), "lamia_linkeditor_ui.ui")

    def __init__(self, wdg, currentfeaturepk):
        super(LamiaLinkEditor, self).__init__()
        uic.loadUi(self.UIPATH, self)
        self.wdg = wdg
        self.tablename = self.wdg.DBASETABLENAME
        self.dbase = self.wdg.dbase
        self.currentfeaturepk = currentfeaturepk

        self.linkchild = self._getLinkSpec()

        self.comboBox_parenttype.addItems(list(self.linkchild.keys()))
        self.comboBox_parenttype.currentIndexChanged.connect(self.JointableChanged)

        self.toolButton_add.clicked.connect(lambda: self.addChild())
        self.toolButton_remove.clicked.connect(self.removeChild)

        if list(self.linkchild.keys()):
            self.comboBox_parenttype.currentIndexChanged.emit(0)

    def _getLinkSpec(self):
        spec = {}
        for childwdg in self.wdg.dbasechildwdgfield:
            name = childwdg.tooltreewidgetSUBCAT
            spec[name] = childwdg

        return spec

    def JointableChanged(self, idx):
        childjointable = self.comboBox_parenttype.currentText()

        self.childtablename = self.linkchild[childjointable].DBASETABLENAME

        self.parentmanytomanyfield = self.linkchild[childjointable].PARENTJOIN[
            self.tablename
        ]["colparent"]
        self.childmanytomanyfield = self.linkchild[childjointable].PARENTJOIN[
            self.tablename
        ]["colthistable"]

        self.tcmanytomanyname = self.linkchild[childjointable].PARENTJOIN[
            self.tablename
        ]["tctable"]

        self.childdisplayfields = [
            f"pk_{self.childtablename}",
            f"id_{self.childtablename}",
        ]

        if hasattr(self.linkchild[childjointable], "CHOOSERTREEWDGSPEC"):
            self.childdisplayfields += self.linkchild[
                childjointable
            ].CHOOSERTREEWDGSPEC["colshow"]
        qgiscanvas = self.wdg.mainifacewidget.qgiscanvas
        qgiscanvas.createorresetRubberband(instance=self)

        self.headerfields = self.childdisplayfields
        # self.headerfields = self.childdisplayfields + self.tcmanytomanydisplayfields
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(self.headerfields))
        self.tableWidget.setHorizontalHeaderLabels(
            [field.title() for field in self.headerfields]
        )
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.rubberBand = None
        self.isspatial = False
        if self.dbase.isTableSpatial(self.childtablename):
            self.isspatial = True
            self.wdg.mainifacewidget.qgiscanvas.createorresetRubberband(
                type=0, instance=self
            )
            self.tableWidget.itemSelectionChanged.connect(self._cellChanged)
            self.toolButton_add.setText("Pick")
        else:
            self.toolButton_add.setText("Add")

        # * different cases : tc table or simplefield

        if self.tcmanytomanyname:
            self.joincase = "tc"
            idchooser = IDChooser(
                toolwidget=self.linkchild[childjointable], dbase=self.dbase
            )
            for pk in idchooser.loadIds()["pk"].tolist():
                self.addChild(pk)
            pass

        else:
            self.joincase = "lid"
            idchooser = IDChooser(
                toolwidget=self.linkchild[childjointable], dbase=self.dbase
            )
            for pk in idchooser.loadIds()["pk"].tolist():
                self.addChild(pk)

    def _postSelectFeature_old(self):
        # init table
        qgiscanvas = self.parentwdg.mainifacewidget.qgiscanvas
        qgiscanvas.createorresetRubberband(instance=self)
        self.tableWidget_actors.setRowCount(0)
        pkparent = self.parentwdg.currentFeaturePK
        if pkparent is None:
            self.setEnabled(False)
            # self.parentwdg.mainifacewidget.connector.showErrorMessage(QtCore.QCoreApplication.translate('base3','Save first'))
            return
        self.setEnabled(True)
        fieldlist = [self.childdisplayfields[0]] + self.tcmanytomanydisplayfields

        # get linked child
        sql = f"SELECT  {', '.join(fieldlist)} "
        sql += self.sqlwholetable
        sql += (
            f" WHERE {self.parenttablename}_now.pk_{self.parenttablename} = {pkparent}"
        )
        sql = self.parentwdg.dbase.sqlNow(sql)
        res = self.parentwdg.dbase.query(sql)
        if res:
            for reslist in res:
                if len(reslist) > 1:
                    self.addChild(reslist[0], reslist[1:])
                else:  # no manytomanyfield
                    self.addChild(reslist[0])

        self._resizeLastSection()

    def _postSaveFeature_old(self, parentfeaturepk=None):

        # self.parentmanytomanyfield

        idparentmanytomanyfield = self.parentwdg.dbase.getValuesFromPk(
            self.parenttablename + "_qgis", self.parentmanytomanyfield, parentfeaturepk
        )

        for rowindex in range(self.tableWidget_actors.rowCount()):
            pkchild = int(self.tableWidget_actors.item(rowindex, 0).text())
            idchildmanytomanyfield = self.parentwdg.dbase.getValuesFromPk(
                self.childtablename + "_qgis", self.childmanytomanyfield, pkchild
            )
            childdisplayres = []
            for i, tcmanytomanyfield in enumerate(self.tcmanytomanydisplayfields):
                columnindex = len(self.childdisplayfields) + i
                combo = self.tableWidget_actors.cellWidget(rowindex, columnindex)
                tcraw, tclong = self._getfieldrawlong(
                    self.tcmanytomanyname, tcmanytomanyfield
                )
                roleindex = combo.currentIndex()
                rolerawvalue = tcraw[roleindex]
                if rolerawvalue == "":
                    rolerawvalue = "NULL"
                else:
                    rolerawvalue = "'" + rolerawvalue + "'"
                childdisplayres.append(rolerawvalue)

            sql = f"SELECT pk_{self.tcmanytomanyname} FROM  {self.tcmanytomanyname} \
                    WHERE l{self.parentmanytomanyfield} = {idparentmanytomanyfield} \
                    AND l{self.childmanytomanyfield } = {idchildmanytomanyfield}"
            if self.tcmanytomanydisplayfields:
                for i, field in enumerate(self.tcmanytomanydisplayfields):
                    res = childdisplayres[i]
                    if res == "NULL":
                        sql += f" AND {field} IS NULL"
                    else:
                        sql += f" AND {field} = {res}"
            res = self.parentwdg.dbase.query(sql)

            if not res:
                dbasemaxrevision = self.parentwdg.dbase.maxrevision
                fieldtoinsert = [
                    "lpk_revision_begin",
                    "l" + self.parentmanytomanyfield,
                    "l" + self.childmanytomanyfield,
                ] + self.tcmanytomanydisplayfields
                valuetoinsert = [
                    str(dbasemaxrevision),
                    str(idparentmanytomanyfield),
                    str(idchildmanytomanyfield),
                ] + childdisplayres
                sql = f"INSERT INTO {self.tcmanytomanyname}({','.join(fieldtoinsert)}) VALUES({','.join(valuetoinsert)})"
                res = self.parentwdg.dbase.query(sql)
        self._resizeLastSection()

    def addChild(self, pkchild=None, tcmanytomanyres=None):

        if pkchild is None:  # come from click
            pkchild = self._childChooser()
            return

        if pkchild is None:
            return

        pkparent = self.wdg.currentFeaturePK
        values = self.dbase.getValuesFromPk(
            f"{self.childtablename}_qgis", self.childdisplayfields, pkchild
        )
        longvalues = [
            self.dbase.getConstraintTextFromRawValue(
                self.childtablename, self.childdisplayfields[i], values[i]
            )
            for i in range(len(self.childdisplayfields))
        ]

        if self.joincase == "lid":
            # update child
            relationnalchildval = self.dbase.lamiaorm[self.childtablename].read(
                pkchild
            )[self.childmanytomanyfield]
            relationnalparentval = self.dbase.lamiaorm[self.tablename].read(
                self.wdg.currentFeaturePK
            )[self.parentmanytomanyfield]
            if relationnalchildval != relationnalparentval:
                self.dbase.lamiaorm[self.childtablename].update(
                    pkchild, {self.childmanytomanyfield: relationnalparentval}
                )
            # put values
            introw = self.tableWidget.rowCount()
            self.tableWidget.insertRow(introw)
            for i, val in enumerate(longvalues):
                field = self.headerfields[i]
                item = QTableWidgetItem(str(val))
                self.tableWidget.setItem(introw, i, item)

        elif self.joincase == "tc":
            # update child
            relationnalchildval = self.dbase.lamiaorm[self.childtablename].read(
                pkchild
            )[self.childmanytomanyfield]
            relationnalparentval = self.dbase.lamiaorm[self.tablename].read(
                self.wdg.currentFeaturePK
            )[self.parentmanytomanyfield]

            # sql = f"SELECT pk_{self.tcmanytomanyname} FROM {self.tcmanytomanyname} \
            #      WHERE lid_{self.tablename} = {relationnalparentval} AND lid_{self.childtablename} = {relationnalchildval}"
            # res = self.dbase.query(sql)
            sqlclause = f"lid_{self.parentmanytomanyfield.split('_')[1]} = {relationnalparentval}   \
                AND lid_{self.childmanytomanyfield.split('_')[1]} = {relationnalchildval}"
            res = self.dbase.lamiaorm[self.tcmanytomanyname][sqlclause]
            if not res:
                newpk = self.dbase.lamiaorm[self.tcmanytomanyname].create()
                self.dbase.lamiaorm[self.tcmanytomanyname].update(
                    newpk,
                    {
                        f"lid_{self.parentmanytomanyfield.split('_')[1]}": relationnalparentval,
                        f"lid_{self.childmanytomanyfield.split('_')[1]}": relationnalchildval,
                    },
                )

            # put values
            introw = self.tableWidget.rowCount()
            self.tableWidget.insertRow(introw)
            for i, val in enumerate(longvalues):
                field = self.headerfields[i]
                item = QTableWidgetItem(str(val))
                self.tableWidget.setItem(introw, i, item)

            # tc cell
            if hasattr(self, "tcmanytomanydisplayfields"):
                for i, tcmanytomanyfield in enumerate(self.tcmanytomanydisplayfields):

                    if (
                        "Cst"
                        in self.dbase.dbasetables["tcobjectactor"]["fields"][
                            "role"
                        ].keys()
                    ):
                        tcraw, tclong = self._getfieldrawlong(
                            self.tcmanytomanyname, tcmanytomanyfield
                        )
                        combobox = QComboBox()
                        combobox.addItems(tclong)
                        self.tableWidget.setCellWidget(
                            introw, self.tableWidget.columnCount() - 1, combobox
                        )
                        if tcmanytomanyres and tcmanytomanyres[i] is not None:
                            tcmanytomanyre = tcmanytomanyres[i]
                            comboindex = tcraw.index(tcmanytomanyre)
                            combobox.setCurrentIndex(comboindex)

        # display
        self._resizeLastSection()

    def _childChooser(self):
        if not self.isspatial:
            sql = f"SELECT {',' .join(self.childdisplayfields)} FROM {self.childtablename}_now"
            sql = self.wdg.dbase.sqlNow(sql)
            res = self.wdg.dbase.query(sql)
            itemsforinputdialog = []
            for row in res:
                itemsforinputdialog.append(", ".join([str(elem) for elem in row]))
            item, ok = QInputDialog.getItem(
                self, "select actor", "list of actors", itemsforinputdialog, 0, False
            )
            if ok and item:
                pkchild = int(item.split(", ")[0])
                self.wdg.updateFormTitleBackground(subwidgethaschanged=True)
                # return pkchild
                self.addChild(pkchild)

            else:
                return None
        else:
            self.wdg.mainifacewidget.qgiscanvas.captureGeometry(
                fctonstopcapture=self.stopCapture, listpointinitialgeometry=[]
            )
            return None

    def stopCapture(self, points):
        qgiscanvas = self.wdg.mainifacewidget.qgiscanvas
        pkchild, dist = qgiscanvas.getNearestPk(self.childtablename, points[0])
        self.addChild(pkchild)
        self.tableWidget.selectRow(self.tableWidget.rowCount() - 1)
        qgiscanvas.stopCapture()

    def removeChild(self):
        indexrowtodelete = []
        for qtrow in self.tableWidget.selectionModel().selectedRows():
            # self.parentwdg.updateFormTitleBackground(subwidgethaschanged=True)
            rowindex = qtrow.row()
            pkchild = int(self.tableWidget.item(rowindex, 0).text())

            if self.joincase == "lid":
                indexrowtodelete.append(rowindex)
                self.dbase.lamiaorm[self.childtablename].update(
                    pkchild, {self.childmanytomanyfield: "NULL"}
                )

            elif self.joincase == "tc":
                idchild = self.dbase.getValuesFromPk(
                    self.childtablename + "_qgis", self.childmanytomanyfield, pkchild
                )
                parentidobjet = self.dbase.getValuesFromPk(
                    self.tablename + "_qgis",
                    self.parentmanytomanyfield,
                    self.wdg.currentFeaturePK,
                )
                tcmanytomanyfieldvalues = []
                if hasattr(self, "tcmanytomanydisplayfields"):
                    for i, tcmanytomanyfield in enumerate(
                        self.tcmanytomanydisplayfields
                    ):
                        columnindex = len(self.childdisplayfields) + i
                        tcraw, tclong = self._getfieldrawlong(
                            self.tcmanytomanyname, tcmanytomanyfield
                        )
                        combo = self.tableWidget.cellWidget(rowindex, columnindex)
                        roleindex = combo.currentIndex()
                        rolerawvalue = tcraw[roleindex]
                        if rolerawvalue == "":
                            rolerawvalue = "NULL"
                        else:
                            rolerawvalue = "'" + rolerawvalue + "'"
                        tcmanytomanyfieldvalues.append(rolerawvalue)

                # sql = f"DELETE FROM tcobjectactor WHERE lid_object = {parentidobjet}  AND lid_actor = {idactor}"
                sql = f"DELETE FROM {self.tcmanytomanyname} \
                        WHERE l{self.parentmanytomanyfield} = {parentidobjet}  \
                        AND l{self.childmanytomanyfield} = {idchild}"

                if hasattr(self, "tcmanytomanydisplayfields"):
                    for i, tcmanytomanyfield in enumerate(
                        self.tcmanytomanydisplayfields
                    ):
                        res = tcmanytomanyfieldvalues[i]
                        if res == "NULL":
                            sql += f" AND {tcmanytomanyfield} IS NULL"
                        else:
                            sql += f" AND {tcmanytomanyfield} = {res}"
                self.dbase.query(sql)
                indexrowtodelete.append(rowindex)

        if indexrowtodelete:
            for indexrow in sorted(indexrowtodelete, reverse=True):
                self.tableWidget.removeRow(indexrow)
        self._resizeLastSection()

    def _resizeLastSection(self):
        header = self.tableWidget.horizontalHeader()
        header.resizeSections(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        self.tableWidget.update()

    def _getfieldrawlong(self, tablename, fieldname):
        fieldraw = [
            elem[1]
            for elem in self.parentwdg.dbase.dbasetables[tablename]["fields"][
                fieldname
            ]["Cst"]
        ]
        fieldlong = [
            elem[0]
            for elem in self.parentwdg.dbase.dbasetables[tablename]["fields"][
                fieldname
            ]["Cst"]
        ]
        return fieldraw, fieldlong

    def _cellChanged(self):
        qgiscanvas = self.wdg.mainifacewidget.qgiscanvas
        geoms = []
        for qtrow in self.tableWidget.selectionModel().selectedRows():
            currentRow = qtrow.row()
            pkchild = int(self.tableWidget.item(currentRow, 0).text())
            geoms.append(
                qgiscanvas.getQgsGeomFromPk(
                    self.wdg.dbase, self.childtablename, pkchild
                )
            )
        qgiscanvas.createRubberBandForSelection(geoms, instance=self)

    def closeEvent(self, evt):
        qgiscanvas = self.wdg.mainifacewidget.qgiscanvas
        qgiscanvas.createorresetRubberband(instance=self)

