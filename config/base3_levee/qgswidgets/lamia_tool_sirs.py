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
import os, sys
from qgis.PyQt import QtGui, uic, QtCore
from qgis.PyQt.QtWidgets import QWidget

from lamiaqgisiface.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool
from lamiaapi.libslamia.sirsconverter.sirsconverter import SirsConverter


class LeveeSIRSTool(AbstractLamiaTool):

    POSTPROTOOLNAME = "SIRSconverter"

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Import/export")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "SIRS database")

    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_tool_sirs_icon.png"
    )

    def __init__(self, **kwargs):
        super(LeveeSIRSTool, self).__init__(**kwargs)
        self.sirsconverter = SirsConverter(self.dbase)

        if self.dbase.variante in [None, "Lamia"]:
            self.POSTPROTOOLNAME = None

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.toolwidgetmain.lineEdit_user.textChanged.connect(
            self.reinitLabelConnection
        )
        self.toolwidgetmain.lineEdit_password.textChanged.connect(
            self.reinitLabelConnection
        )
        self.toolwidgetmain.lineEdit_ip.textChanged.connect(self.reinitLabelConnection)
        self.toolwidgetmain.lineEdit_port.textChanged.connect(
            self.reinitLabelConnection
        )
        self.toolwidgetmain.lineEdit_dbname.textChanged.connect(
            self.reinitLabelConnection
        )

        self.toolwidgetmain.pushButton_test.clicked.connect(self.testConnection)
        self.toolwidgetmain.pushButton_import.clicked.connect(self.importSIRS)
        self.toolwidgetmain.pushButton_export.clicked.connect(self.exportSIRS)

        self.toolwidgetmain.pushButton_import.setEnabled(False)
        self.toolwidgetmain.pushButton_export.setEnabled(False)

    def testConnection(self):

        sirsconnectiondict = self._getConnectiondata()

        print(sirsconnectiondict)

        self.sirsconverter.sirsconnectiondict = sirsconnectiondict

        client, my_db = self.sirsconverter.getSirsConnection()

        if client:
            self.setConnectionLabelOK()
        else:
            self.setConnectionLabelError(my_db)

    def setConnectionLabelOK(self):
        self.toolwidgetmain.label_test.setStyleSheet(
            "QLabel { background-color : green}"
        )
        self.toolwidgetmain.label_test.setText("OK")

        self.toolwidgetmain.pushButton_import.setEnabled(True)
        self.toolwidgetmain.pushButton_export.setEnabled(True)

    def setConnectionLabelError(self, errortxt):
        self.toolwidgetmain.label_test.setStyleSheet("QLabel { background-color : red}")
        self.toolwidgetmain.label_test.setText(errortxt)

        self.toolwidgetmain.pushButton_import.setEnabled(False)
        self.toolwidgetmain.pushButton_export.setEnabled(False)

    def reinitLabelConnection(self):
        self.toolwidgetmain.label_test.setStyleSheet("")
        self.toolwidgetmain.label_test.setText("...")

        self.toolwidgetmain.pushButton_import.setEnabled(False)
        self.toolwidgetmain.pushButton_export.setEnabled(False)

    def importSIRS(self):

        sql = "SELECT id_object FROM object"
        res = self.dbase.query(sql)
        if len(res) > 0:
            self.dbase.messageinstance.showErrorMessage(
                QtCore.QCoreApplication.translate(
                    "base3", "DBASE not Empty - create a new Levee - SIRS DBase"
                )
            )
            return

        sirsconnectiondict = self._getConnectiondata()
        self.sirsconverter.sirsconnectiondict = sirsconnectiondict
        self.sirsconverter.import_sirs()

    def exportSIRS(self):

        sirsconnectiondict = self._getConnectiondata()
        self.sirsconverter.sirsconnectiondict = sirsconnectiondict
        self.sirsconverter.export_lamia()

    def _getConnectiondata(self):
        user = self.toolwidgetmain.lineEdit_user.text()
        password = self.toolwidgetmain.lineEdit_password.text()
        ip = self.toolwidgetmain.lineEdit_ip.text()
        port = self.toolwidgetmain.lineEdit_port.text()
        dbname = self.toolwidgetmain.lineEdit_dbname.text()

        sirsconnectiondict = {
            "user": user,
            "password": password,
            "ip": ip,
            "port": port,
            "dbname": dbname,
        }

        return sirsconnectiondict


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_sirs_ui.ui")
        uic.loadUi(uipath, self)
