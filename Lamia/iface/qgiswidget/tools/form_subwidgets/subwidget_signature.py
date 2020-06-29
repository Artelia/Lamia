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

import os, datetime, logging

from qgis.PyQt.QtWidgets import QWidget
from qgis.PyQt import uic, QtCore


from .subwidget_abstract import AbstractSubWidget

# from .lamiabasechantier_croquis_tool import BaseChantierCroquisTool as BaseCroquisTool
from Lamia.worktypeconf.base3.qgswidgets.lamia_form_sketch import BaseSketchTool

# from ..base3.lamiabase_sketch_tool import BaseSketchTool
# from .lamiabasechantier_intervenant_tool import BaseChantierIntervenantTool as BaseIntervenantTool
from .subwidget_lidchooser import LidChooserWidget


class SignatureWidget(AbstractSubWidget):

    UIPATH = os.path.join(os.path.dirname(__file__), "subwidget_signature_ui.ui")

    def __init__(
        self,
        parentwdg=None,
        intervenantid=None,
        signatureid=None,
        datetimesig=None,
        parentframe=None,
    ):

        super(SignatureWidget, self).__init__(
            parentwdg=parentwdg, parentframe=parentframe
        )

        self.parentwdg = parentwdg
        self.intervenantid = intervenantid
        self.signatureid = signatureid
        self.datetimesigfield = datetimesig

        self.propertieswdgCROQUIS2 = BaseSketchTool(
            dbaseparser=self.parentwdg.dbase,
            mainifacewidget=self.parentwdg.mainifacewidget,
            parentwidget=self.parentwdg,
        )
        self.propertieswdgCROQUIS2.initMainToolWidget()
        # self.propertieswdgCROQUIS2.linkagespec = {'Observation': {'tabletc': None,
        #                                                          'idsource': 'id_ressource',
        #                                                          'idtcsource': None,
        #                                                          'iddest': self.signatureid,
        #                                                          'idtcdest': None,
        #                                                          'desttable': ['Observation']}}

        #  }
        self.propertieswdgCROQUIS2.PARENTJOIN = {
            "observation": {
                "colparent": self.signatureid,
                "colthistable": "id_resource",
                "tctable": None,
                "tctablecolparent": None,
                "tctablecolthistable": None,
            }
        }

        self.propertieswdgCROQUIS2.NAME = None
        self.propertieswdgCROQUIS2.SKIP_LOADING_UI = True
        # self.propertieswdgCROQUIS2.choosertreewidget = None
        self.frame_signature.layout().addWidget(self.propertieswdgCROQUIS2.photowdg)
        self.pushButton_editsig.clicked.connect(self.propertieswdgCROQUIS2.editPhoto)
        # self.propertieswdgCROQUIS2.groupBox_elements.setVisible(False)
        # self.propertieswdgCROQUIS2.userwdgfield.frame_editing.setVisible(False)
        self.parentwdg.CASCADEFEATURESELECTION = True
        self.parentwdg.dbasechildwdgfield.append(self.propertieswdgCROQUIS2)

        lidchooser = LidChooserWidget(
            parentwdg=self.parentwdg,
            parentlidfield=self.intervenantid,
            parentframe=self.frame_intervenant,
            searchdbase="Actor",
            searchfieldtoshow=["actorname", "society"],
        )
        self.parentwdg.lamiawidgets.append(lidchooser)

    def postSelectFeature(self):
        debug = False

        if debug:
            timestart = self.parentwdg.dbase.getTimeNow()

        # if self.parentwdg.currentFeaturePK is None:
        #     self.frame_sigedit.setEnabled(False)
        # else:
        #     self.frame_sigedit.setEnabled(True)

        # create new sketch if parentcurrentFeaturePK isnone...
        if self.parentwdg.currentFeaturePK is None:
            self.propertieswdgCROQUIS2.selectFeature()

        # date
        valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if self.parentwdg.currentFeaturePK is not None:
            sql = (
                "SELECT "
                + self.datetimesigfield
                + " FROM observation WHERE pk_observation = "
                + str(self.parentwdg.currentFeaturePK)
            )
            res = self.parentwdg.dbase.query(sql)
            if res is not None and len(res) > 0 and res[0][0] is not None:
                valuetoset = res[0][0]
            else:
                valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.dateTimeEdit_sig.setDateTime(
            QtCore.QDateTime.fromString(valuetoset, "yyyy-MM-dd hh:mm:ss")
        )
        if debug:
            logging.getLogger("Lamia").debug(
                "end  %.3f", self.parentwdg.dbase.getTimeNow() - timestart
            )

    def postSaveFeature(self, parentfeaturepk=None):
        # print(self.parentframe.objectName())
        # print(self.parentwdg.lamiawidgets)
        if parentfeaturepk is not None:
            signatureid = self.parentwdg.dbase.getValuesFromPk(
                self.parentwdg.DBASETABLENAME + "_qgis",
                self.signatureid,
                parentfeaturepk,
            )

            if signatureid is None:  # first creation
                # tricky : because lid_ is parent side....
                tempjoin = dict(self.propertieswdgCROQUIS2.PARENTJOIN)
                self.propertieswdgCROQUIS2.PARENTJOIN = {}
                # self.propertieswdgCROQUIS2.selectFeature()
                self.parentwdg.currentFeaturePK = (
                    parentfeaturepk  # needed for following saveFeature
                )
                self.propertieswdgCROQUIS2.toolbarSave()
                self.parentwdg.currentFeaturePK = None
                croquispk = self.propertieswdgCROQUIS2.currentFeaturePK
                resourceid = self.parentwdg.dbase.getValuesFromPk(
                    "media_qgis", "id_resource", croquispk
                )

                sql = f"UPDATE {self.parentwdg.DBASETABLENAME} SET {self.signatureid} = {resourceid} \
                        WHERE pk_{self.parentwdg.DBASETABLENAME.lower()} = {parentfeaturepk}"

                # sql = "UPDATE observation SET " + self.signatureid + " = " + str(resourceid)
                # sql += ' WHERE pk_observation = ' + str(parentfeaturepk)
                self.parentwdg.dbase.query(sql)
                self.propertieswdgCROQUIS2.PARENTJOIN = tempjoin
            else:
                self.propertieswdgCROQUIS2.toolbarSave()

            # date
            sql = f"UPDATE {self.parentwdg.DBASETABLENAME} \
                   SET {self.datetimesigfield } = '{self.dateTimeEdit_sig.dateTime().toString('yyyy-MM-dd hh:mm:ss')}' \
                   WHERE pk_{self.parentwdg.DBASETABLENAME.lower()} = {parentfeaturepk}"

            # sql = "UPDATE observation SET " + self.datetimesigfield + ' = '
            # sql += "'" + self.dateTimeEdit_sig.dateTime().toString('yyyy-MM-dd hh:mm:ss') + "'"
            # sql += " WHERE pk_observation = " + str(parentfeaturepk)
            self.parentwdg.dbase.query(sql)
