# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
"""
from qgis.PyQt.QtWidgets import (QWidget, QTreeWidgetItem, QMessageBox, QFileDialog, QTableWidget,
                                     QHeaderView, QComboBox, QSpinBox,QCheckBox, QPushButton, QDateEdit,QDateTimeEdit, QTextEdit,
                                     QDoubleSpinBox, QDialog, QVBoxLayout, QTreeWidget, QLineEdit, QCheckBox,
                                     QLabel, QMessageBox, QTextBrowser, QTableWidgetItem,QApplication,QToolButton, QAbstractItemView)
"""
from qgis.PyQt.QtWidgets import (QComboBox )
from qgis.PyQt import QtCore


class FormToolUtils(QtCore.QObject):

    def __init__(self, formtoolwidget):
         self.formtoolwidget = formtoolwidget

    def ___________________actionsOnWidgetCreation(self):
        pass

    def initWidgetBehaviour(self):

        templinkuserwgd = self.formtoolwidget.formtoolwidgetconfdict

        for tablename in templinkuserwgd:
            dbasetables = self.formtoolwidget.dbase.dbasetables

            if tablename in dbasetables.keys():
                dbasetable = dbasetables[tablename]
                for field in dbasetable['fields'].keys():
                    # for linkuserwdg in [self.linkuserwdg]:
                    for linkuserwdg in [templinkuserwgd]: 
                        if linkuserwdg is None or linkuserwdg.keys() is None:
                            continue

                        if (tablename in linkuserwdg.keys()
                                and field in linkuserwdg[tablename]['widgets'].keys()):
                            wdgs = linkuserwdg[tablename]['widgets'][field]
                            if 'Cst' in dbasetable['fields'][field].keys():
                                # combox filling with constraints
                                if isinstance(wdgs, QComboBox) or (
                                        isinstance(wdgs, list) and isinstance(wdgs[0], QComboBox)):

                                    templist = [description[0] for description in
                                                dbasetable['fields'][field]['Cst']]
                                    if isinstance(wdgs, QComboBox):
                                        wdgs = [wdgs]
                                    for wdg in wdgs:
                                        wdg.clear()
                                        wdg.addItems(templist)

                            if 'ParFldCst' in dbasetable['fields'][field].keys():
                                nameparentfield = dbasetable['fields'][field]['ParFldCst']
                                # userwidget
                                if (tablename in linkuserwdg.keys() and 'widgets' in linkuserwdg[tablename].keys()
                                        and nameparentfield in linkuserwdg[tablename]['widgets'].keys()
                                        and isinstance(linkuserwdg[tablename]['widgets'][nameparentfield], QComboBox)):
                                    linkuserwdg[tablename]['widgets'][nameparentfield].currentIndexChanged.connect(self.comboparentValueChanged)

                            # multiple wdg for field management
                            if isinstance(wdgs, list):
                                if isinstance(wdgs[0], QComboBox):
                                    for wdg in wdgs:
                                        wdg.currentIndexChanged.connect(self.manageMultipleWidgetField)
                                elif isinstance(wdgs[0], QSpinBox) or isinstance(wdgs[0], QDoubleSpinBox):
                                    for wdg in wdgs:
                                        wdg.valueChanged.connect(self.manageMultipleWidgetField)


    def initWidgetUI(self, basewidget):
        """
        Called by changePropertiesWidget

        - Init combobox with default values

        - Init Parent/child combobox behaviour
        """

        if self.linkuserwdg:
            templinkuserwgd = {self.dbasetablename: None}
        else:
            templinkuserwgd = self.linkuserwdg


        for tablename in templinkuserwgd:
            if tablename in self.dbase.dbasetables.keys():
                dbasetable = self.dbase.dbasetables[tablename]
                for field in dbasetable['fields'].keys():
                    for linkuserwdg in [self.linkuserwdg]:
                        if linkuserwdg is None or linkuserwdg.keys() is None:
                            continue

                        if (tablename in linkuserwdg.keys()
                                and field in linkuserwdg[tablename]['widgets'].keys()):
                            wdgs = linkuserwdg[tablename]['widgets'][field]
                            if 'Cst' in dbasetable['fields'][field].keys():
                                # combox filling with constraints
                                if isinstance(wdgs, QComboBox) or (
                                        isinstance(wdgs, list) and isinstance(wdgs[0], QComboBox)):

                                    templist = [description[0] for description in
                                                dbasetable['fields'][field]['Cst']]
                                    if isinstance(wdgs, QComboBox):
                                        wdgs = [wdgs]
                                    for wdg in wdgs:
                                        wdg.clear()
                                        wdg.addItems(templist)

                            if 'ParFldCst' in dbasetable['fields'][field].keys():
                                nameparentfield = dbasetable['fields'][field]['ParFldCst']
                                # userwidget
                                if (tablename in linkuserwdg.keys() and 'widgets' in linkuserwdg[tablename].keys()
                                        and nameparentfield in linkuserwdg[tablename]['widgets'].keys()
                                        and isinstance(linkuserwdg[tablename]['widgets'][nameparentfield], QComboBox)):
                                    linkuserwdg[tablename]['widgets'][nameparentfield].currentIndexChanged.connect(self.comboparentValueChanged)

                            # multiple wdg for field management
                            if isinstance(wdgs, list):
                                if isinstance(wdgs[0], QComboBox):
                                    for wdg in wdgs:
                                        wdg.currentIndexChanged.connect(self.manageMultipleWidgetField)
                                elif isinstance(wdgs[0], QSpinBox) or isinstance(wdgs[0], QDoubleSpinBox):
                                    for wdg in wdgs:
                                        wdg.valueChanged.connect(self.manageMultipleWidgetField)


    def manageMultipleWidgetField(self):
        """
        Activated by widget.valueChanged or widget.currentIndexChanged signal

        Manage multiple combobox or spinbox linked to one table field
        """
        senderwdg = self.sender()

        for tablename in self.linkuserwdg:
            for fieldname in self.linkuserwdg[tablename]['widgets'].keys():
                wdgs = self.linkuserwdg[tablename]['widgets'][fieldname]
                if isinstance(wdgs, list) and senderwdg in wdgs:
                    if isinstance(senderwdg, QComboBox):
                        for wdg in wdgs:
                            if wdg != senderwdg:
                                try:
                                    wdg.currentIndexChanged.disconnect(self.manageMultipleWidgetField)
                                except:
                                    pass
                                wdg.setCurrentIndex(senderwdg.currentIndex())
                                wdg.currentIndexChanged.connect(self.manageMultipleWidgetField)
                        break
                    elif isinstance(senderwdg, QSpinBox) or isinstance(senderwdg, QDoubleSpinBox):
                        for wdg in wdgs:
                            if wdg != senderwdg:
                                try:
                                    wdg.valueChanged.disconnect(self.manageMultipleWidgetField)
                                except:
                                    pass
                                wdg.setValue(senderwdg.value())
                                wdg.valueChanged.connect(self.manageMultipleWidgetField)
                        break


    def comboparentValueChanged(self, index):
        """
        Activated by currentIndexChanged

        Manage paret/child combobox
        """

        debug = False
        if debug:
            senderwdg = self.sender()
            print('**', senderwdg.objectName())

        senderwdg = self.sender()
        if isinstance(senderwdg, QComboBox) and senderwdg.count() == 0:  # case triple descendant and parent not filled
            return

        if self.groupBox_properties.layout().itemAt(0) is None:
            return

        parenttablename = None
        parentfieldname = None

        if self.groupBox_properties.layout().itemAt(0).widget() == self.userwdg:
            comefromrawtable = False
            if self.linkuserwdg is not None:
                for tablename in self.linkuserwdg.keys():
                    for fieldname in self.linkuserwdg[tablename]['widgets'].keys():
                        if senderwdg == self.linkuserwdg[tablename]['widgets'][fieldname]:
                            parenttablename = tablename
                            parentfieldname = fieldname
                            break

        elif self.groupBox_properties.layout().itemAt(0).widget() == self.tableWidget:
            ind = self.tableWidget.indexAt(senderwdg.pos()).row()
            parenttablename, parentfieldname = self.tableWidget.item(ind, 0).text().split('.')
            comefromrawtable = True

        if parenttablename is None:
            return

        try:
            parentcstvalue = self.dbase.getConstraintRawValueFromText(parenttablename, parentfieldname,
                                                                      senderwdg.currentText())
        except Exception as e:
            if self.dbase.qgsiface is None:
                logging.getLogger("Lamia").debug('error %s %s %s', e, parenttablename, parentfieldname)
            return

        dbasetable = self.dbase.dbasetables[parenttablename]
        # get child index and combochild
        listparentcst = [dbasetable['fields'][field]['ParFldCst']
                         if 'ParFldCst' in dbasetable['fields'][field].keys() else None
                         for field in dbasetable['fields'].keys()]

        childfieldnames = [list(dbasetable['fields'].keys())[i] for i in range(len(listparentcst))
                           if parentfieldname == listparentcst[i]]

        if debug: print('**', listparentcst)
        if debug: print('***', childfieldnames)

        if comefromrawtable:
            listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
            for childfieldname in childfieldnames:
                if dbasetable['fields'][parentfieldname][
                    'PGtype'] == 'INT' and parentcstvalue != '' and parentcstvalue is not None:
                    parentcstvalue = int(parentcstvalue)
                listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if
                             parentcstvalue in value[2]]
                indexchildintable = listfieldname.index(parenttablename + '.' + childfieldname)
                combochild = self.tableWidget.cellWidget(indexchildintable, 1)
                combochild.clear()
                if len(listtoadd) > 0:
                    combochild.addItems(listtoadd)
        else:
            for childfieldname in childfieldnames:
                if dbasetable['fields'][parentfieldname]['PGtype'] == 'INT' and parentcstvalue != '' and parentcstvalue is not None:
                    parentcstvalue = int(parentcstvalue)


                listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if (value[2] is None or parentcstvalue in value[2])]

                if debug: print('****', listtoadd)

                if childfieldname in self.linkuserwdg[parenttablename]['widgets']:
                    combochild = self.linkuserwdg[parenttablename]['widgets'][childfieldname]
                    combochild.clear()
                    if len(listtoadd) > 0:
                        combochild.addItems(listtoadd)


