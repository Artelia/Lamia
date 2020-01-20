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
from .lamiabasechantier_croquis_tool import BaseChantierCroquisTool as BaseCroquisTool
from .lamiabasechantier_intervenant_tool import BaseChantierIntervenantTool as BaseIntervenantTool
from .lamiabasechantier_lidchooser import LidChooserWidget


import os, datetime, logging

class SignatureWidget(QWidget):


    def __init__(self, parentwdg=None, intervenantid=None, signatureid=None, datetimesig=None):
        super(SignatureWidget, self).__init__(parent=parentwdg)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantier_signature_tool_ui.ui')
        uic.loadUi(uipath, self)

        self.parentwdg = parentwdg
        self.intervenantid = intervenantid
        self.signatureid = signatureid
        self.datetimesigfield = datetimesig

        self.propertieswdgCROQUIS2 = BaseCroquisTool(dbase=self.parentwdg.dbase, parentwidget=self.parentwdg)
        self.propertieswdgCROQUIS2.linkagespec = {'Observation': {'tabletc': None,
                                                                  'idsource': 'id_ressource',
                                                                  'idtcsource': None,
                                                                  'iddest': self.signatureid,
                                                                  'idtcdest': None,
                                                                  'desttable': ['Observation']}}
        self.propertieswdgCROQUIS2.NAME = None
        self.frame_signature.layout().addWidget(self.propertieswdgCROQUIS2.photowdg)
        self.pushButton_editsig.clicked.connect(self.propertieswdgCROQUIS2.editPhoto)
        self.propertieswdgCROQUIS2.groupBox_elements.setVisible(False)
        self.propertieswdgCROQUIS2.userwdgfield.frame_editing.setVisible(False)
        self.parentwdg.dbasechildwdgfield.append(self.propertieswdgCROQUIS2)

        lidchooser = LidChooserWidget(parentwdg=self.parentwdg, parentlidfield=self.intervenantid,
                                parentframe=self.frame_intervenant,
                                searchdbase='Intervenant', searchfieldtoshow=['nom','societe'])
        self.parentwdg.lamiawidgets.append(lidchooser)



    def initProperties(self):
        debug = False

        if debug: timestart = self.parentwdg.dbase.getTimeNow()


        if self.parentwdg.currentFeaturePK is None:
            self.frame_sigedit.setEnabled(False)
        else:
            self.frame_sigedit.setEnabled(True)


        # date
        valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if self.parentwdg.currentFeaturePK is not None:
            sql = "SELECT " + self.datetimesigfield + " FROM Observation WHERE pk_observation = " + str(
                self.parentwdg.currentFeaturePK)
            res = self.parentwdg.dbase.query(sql)
            if res is not None and len(res) > 0 and res[0][0] is not None:
                valuetoset = res[0][0]
            else:
                valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.dateTimeEdit_sig.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd hh:mm:ss'))


        if debug: logging.getLogger('Lamia').debug('end  %.3f', self.parentwdg.dbase.getTimeNow() - timestart)






    def saveProperties(self):

        if self.parentwdg.currentFeaturePK is not None:
            #         self.intervenantid = intervenantid
            #         self.signatureid = signatureid
            #signaturecreation
            if hasattr(self.parentwdg, 'OBSTYPE') and self.parentwdg.OBSTYPE[0:2] in ['NC']:
                nclist = self.parentwdg.parentWidget.nclist
                nctype = [elem[1] for elem in nclist]
                ncindex = nctype.index(self.parentwdg.OBSTYPE)
                signaturebool = nclist[ncindex][2]
                if signaturebool == True:
                    sql = "SELECT " + self.signatureid  + "  FROM Observation "
                    sql += " WHERE pk_observation = " + str(self.parentwdg.currentFeaturePK)
                    res = self.parentwdg.dbase.query(sql)[0][0]
                    if res is None:
                        lastid = self.parentwdg.dbase.getLastId('Ressource') + 1
                        sql = "UPDATE Observation SET " + self.signatureid  + " = " + str(lastid)
                        sql += ' WHERE pk_observation = ' + str(self.parentwdg.currentFeaturePK)
                        self.parentwdg.dbase.query(sql)

                        self.propertieswdgCROQUIS2.featureSelected()
                    self.propertieswdgCROQUIS2.saveFeature(showsavemessage=False)

            elif hasattr(self.parentwdg, 'OBSTYPE') and self.parentwdg.OBSTYPE[0:2] in ['PV']:
                sql = "SELECT " + self.signatureid + "  FROM Observation "
                sql += " WHERE pk_observation = " + str(self.parentwdg.currentFeaturePK)
                res = self.parentwdg.dbase.query(sql)[0][0]
                if res is None:
                    lastid = self.parentwdg.dbase.getLastId('Ressource') + 1
                    sql = "UPDATE Observation SET " + self.signatureid + " = " + str(lastid)
                    sql += ' WHERE pk_observation = ' + str(self.parentwdg.currentFeaturePK)
                    self.parentwdg.dbase.query(sql)

                    self.propertieswdgCROQUIS2.featureSelected()
                self.propertieswdgCROQUIS2.saveFeature(showsavemessage=False)

            # date
            sql = "UPDATE Observation SET " + self.datetimesigfield + ' = '
            sql += "'" + self.dateTimeEdit_sig.dateTime().toString('yyyy-MM-dd hh:mm:ss') + "'"
            sql += " WHERE pk_observation = " + str(self.parentwdg.currentFeaturePK)
            self.parentwdg.dbase.query(sql)

