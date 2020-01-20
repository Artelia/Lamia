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


try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from qgis.PyQt import uic, QtCore
import os, logging

class LidChooser(QWidget):


    def __init__(self, parentwdg=None, parentlidfield=None, parentlabel=None, searchdbase='', searchfieldtoshow=[] ):
        super(LidChooser, self).__init__(parent=parentwdg)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantiertram_lidchooser_ui.ui')
        uic.loadUi(uipath, self)
        self.parentwdg=parentwdg
        self.parentlidfield=parentlidfield
        # self.parentfieldtoshow=parentfieldtoshow
        self.searchdbase = searchdbase
        self.searchfieldtoshow = searchfieldtoshow
        self.parentlabel = parentlabel
        #seelf.dbasetosearch=None


        self.lineEdit.textChanged.connect(self.loadDatas)
        self.pushButton_interv.clicked.connect(self.saveDatas)

    def postInitFeatureProperties(self,feat):
        """
        if self.parentwdg.currentFeaturePK is None:
            self.frame_sigedit.setEnabled(False)
        else:
            self.frame_sigedit.setEnabled(True)
        """
        # load intervenant

        debug = False

        if debug: timestart = self.parentwdg.dbase.getTimeNow()

        self.loadDatas()

        if debug: logging.getLogger('Lamia').debug('end  %.3f', self.parentwdg.dbase.getTimeNow() - timestart)



    def loadDatas(self, txtstr=None):

        self.comboBox_interv.clear()
        fields = ['id_' + self.searchdbase.lower() ] + self.searchfieldtoshow
        #sql = "SELECT id_intervenant,  nom, societe FROM Intervenant_now"
        sql = "SELECT " + ','.join(fields) + " FROM " + self.searchdbase + "_now"
        sql = self.parentwdg.dbase.updateQueryTableNow(sql)
        res = self.parentwdg.dbase.query(sql)

        #self.comboBox_interv.addItem('/')
        for elem in res:
            elemstr = [str(t) for t in elem]
            nomstring = ' / '.join(elemstr)
            if txtstr is not None:
                for sselem in elem:
                    if txtstr.lower() in str(sselem).lower():
                        #if txtstr.lower() in str(nom).lower() or txtstr.lower() in str(societe).lower():
                        self.comboBox_interv.addItem(nomstring)
                        break
            else:
                self.comboBox_interv.addItem(nomstring)


        if self.parentwdg.currentFeaturePK is not None:
            #         self.intervenantid = intervenantid
            #         self.signatureid = signatureid

            #sql = "SELECT " + self.intervenantid  + " FROM Observation WHERE pk_observation = " + str(self.parentwdg.currentFeaturePK)
            sql = "SELECT " + str(self.parentlidfield) + " FROM " + self.parentwdg.dbasetablename
            sql += " WHERE pk_" + self.parentwdg.dbasetablename.lower() + " = " + str(self.parentwdg.currentFeaturePK)
            res = self.parentwdg.dbase.query(sql)
            if res is not None and len(res) > 0 and res[0][0] is not None:
                for itemindex in range(self.comboBox_interv.count()):
                    if int(self.comboBox_interv.itemText(itemindex).split(' / ')[0]) == int(res[0][0] ):
                        self.comboBox_interv.setCurrentIndex(itemindex)
                        self.parentlabel.setText(self.comboBox_interv.currentText())
                        break
            else:
                self.parentlabel.setText('/')
        else:
            self.parentlabel.setText('/')



    def saveDatas(self):
        idtxt = self.comboBox_interv.currentText().split(' / ')[0]

        if self.parentwdg.currentFeaturePK is None:
            self.parentwdg.windowdialog.errorMessage("Enregistrer l'observation d'abord")
            return

        try:
            id = int(idtxt)
            sql = "UPDATE " + self.parentwdg.dbasetablename + " SET " + self.parentlidfield
            sql += " = " + str(id) + " WHERE pk_" + self.parentwdg.dbasetablename.lower() + " = " + str(self.parentwdg.currentFeaturePK)
            print(sql)
            self.parentwdg.dbase.query(sql)

            self.parentlabel.setText(self.comboBox_interv.currentText())
            # self.parentwdg.loadChildFeatureinWidget()
            self.parentwdg.dbase.dbasetables[self.searchdbase]['layerqgis'].reload()

        except ValueError as e:
            self.parentwdg.windowdialog.errorMessage("Pas de signataire selectionné" + str(e))
            # print('error', e)
