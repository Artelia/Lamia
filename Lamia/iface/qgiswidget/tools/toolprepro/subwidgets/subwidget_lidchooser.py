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

from qgis.PyQt.QtWidgets import (QWidget, QVBoxLayout)
from qgis.PyQt import uic, QtCore

from .subwidget_abstract import AbstractSubWidget

class LidChooserWidget(AbstractSubWidget):


    def __init__(self, parentwdg=None, parentlidfield=None, parentframe=None, searchdbase='', searchfieldtoshow=[] ):
        super(LidChooserWidget, self).__init__(parent=parentwdg)
        uipath = os.path.join(os.path.dirname(__file__), 'subwidget_lidchooser_ui.ui')
        uic.loadUi(uipath, self)
        self.parentwdg=parentwdg
        self.parentlidfield=parentlidfield
        self.searchdbase = searchdbase
        self.searchfieldtoshow = searchfieldtoshow
        self.parentframe = parentframe

        if self.parentframe.layout() is not None:
            self.parentframe.layout().addWidget(self)
        else:
            vlayout = QVBoxLayout()
            vlayout.addWidget(self)
            self.parentframe.setLayout(vlayout)

        self.lineEdit.textChanged.connect(self.loadDatas)



    def postSelectFeature(self):
        """
        if self.parentwdg.currentFeaturePK is None:
            self.frame_sigedit.setEnabled(False)
        else:
            self.frame_sigedit.setEnabled(True)
        """
        # load intervenant

        debug = False

        self._disconnectSignals()
        self.lineEdit.setText('')
        if debug: timestart = self.parentwdg.dbase.getTimeNow()

        self.loadDatas()

        #choose saved id in combobox
        if self.parentwdg.currentFeaturePK is not None:
            sql = f"SELECT {self.parentlidfield}  FROM {self.parentwdg.DBASETABLENAME}_qgis \
                   WHERE pk_{self.parentwdg.DBASETABLENAME.lower()} = {self.parentwdg.currentFeaturePK} "

            # sql = "SELECT " + str(self.parentlidfield) + " FROM " + self.parentwdg.DBASETABLENAME
            # sql += " WHERE pk_" + self.parentwdg.DBASETABLENAME.lower() + " = " + str(self.parentwdg.currentFeaturePK)
            res = self.parentwdg.dbase.query(sql)
            if res is not None and len(res) > 0 and res[0][0] is not None:
                for itemindex in range(self.comboBox_interv.count()):
                    idtxt = self.comboBox_interv.itemText(itemindex).split(' / ')[0]
                    if idtxt != '/' and int(idtxt) == int(res[0][0] ):
                        self.comboBox_interv.setCurrentIndex(itemindex)
                        break
            else:
                self.comboBox_interv.setCurrentIndex(0)
        else:
            self.comboBox_interv.setCurrentIndex(0)

        self._connectSignals()
        if debug: logging.getLogger('Lamia').debug('end  %.3f', self.parentwdg.dbase.getTimeNow() - timestart)




    def loadDatas(self, txtstr=None):
        print('loadDatas', self.parentwdg.DBASETABLENAME)
        self.comboBox_interv.clear()
        fields = ['id_' + self.searchdbase.lower() ] + self.searchfieldtoshow

        sql = "SELECT " + ','.join(fields) + " FROM " + self.searchdbase + "_now"
        sql = self.parentwdg.dbase.updateQueryTableNow(sql)
        res = self.parentwdg.dbase.query(sql)
        print(res)

        self.comboBox_interv.addItem('/')
        for elem in res:
            elemstr = [str(t) for t in elem]
            nomstring = ' / '.join(elemstr)
            if txtstr in [None, '']:
                self.comboBox_interv.addItem(nomstring)
            else:
                for sselem in elem:
                    if txtstr.lower() in str(sselem).lower():
                        self.comboBox_interv.addItem(nomstring)

    def postSaveFeature(self, parentfeaturepk=None):
        idtxt = self.comboBox_interv.currentText().split(' / ')[0]

        if parentfeaturepk is None:
            self.parentwdg.mainifacewidget.connector.showErrorMessage("Enregistrer l'observation d'abord")
            return

        if idtxt.isdigit():
            valuetoset = idtxt
        else:
            valuetoset = 'NULL'

        parenttables = [self.parentwdg.DBASETABLENAME] + self.parentwdg.dbase.getParentTable(self.parentwdg.DBASETABLENAME)
        parenttables = parenttables[::-1]
        for tablename in parenttables:
            if self.parentlidfield in self.parentwdg.dbase.dbasetables[tablename]['fields'].keys():
                tablepk = self.parentwdg.dbase.getValuesFromPk(self.parentwdg.DBASETABLENAME + '_qgis',
                                                              'pk_' + tablename.lower(),
                                                               parentfeaturepk)
                sql = f"UPDATE {tablename} SET {self.parentlidfield} = {valuetoset} \
                       WHERE pk_{tablename.lower()} = {tablepk}"

                # sql = "UPDATE " + self.parentwdg.DBASETABLENAME + " SET " + self.parentlidfield
                # sql += " = " + valuetoset + " WHERE pk_" + self.parentwdg.DBASETABLENAME.lower() + " = " + str(parentfeaturepk)
                self.parentwdg.dbase.query(sql)
                break

    def _connectSignals(self):
        self.comboBox_interv.currentIndexChanged.connect(self.comboChanged)
        self.lineEdit.textChanged.connect(self.loadDatas)

    def _disconnectSignals(self):
        try:
            self.comboBox_interv.currentIndexChanged.disconnect(self.comboChanged)
        except:
            pass
        try:
            self.lineEdit.textChanged.disconnect(self.loadDatas)
        except:
            pass

    def comboChanged(self):
        self.parentwdg.updateFormTitleBackground(subwidgethaschanged=True)