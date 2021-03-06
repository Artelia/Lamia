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

import logging, sys
import qgis.utils, qgis.core
from qgis.PyQt.QtWidgets import (
    QDialogButtonBox,
    QMessageBox,
    QDialog,
    QApplication,
    QProgressBar,
    QFormLayout,
    QLabel,
    QLineEdit,
)
from qgis.PyQt import QtCore

from ..ifaceabstractconnector import LamiaIFaceAbstractConnectors


class QgisConnector(LamiaIFaceAbstractConnectors):
    def __init__(self):
        LamiaIFaceAbstractConnectors.__init__(self)
        self.widget = None
        self.canvas = None

        self.progressbar = None

        self.stopdisplaymessage = False

    def showNormalMessage(self, text):
        if self.stopdisplaymessage:
            return
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().pushMessage(
                "Lamia ", text, qgis.core.Qgis.Info
            )
            QApplication.processEvents()

    def showErrorMessage(self, text):
        if self.stopdisplaymessage:
            return
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().pushMessage(
                "Lamia ", text, qgis.core.Qgis.Critical
            )
            QApplication.processEvents()

    def createProgressBar(self, inittext="", maxvalue=99):
        if self.stopdisplaymessage:
            return
        self.progressbarinittext = inittext
        if qgis.utils.iface is not None:
            progressMessageBar = qgis.utils.iface.messageBar().createMessage(inittext)
            self.progressbar = QProgressBar()
            self.progressbar.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(self.progressbar)
            qgis.utils.iface.messageBar().pushWidget(
                progressMessageBar, qgis.core.Qgis.Info
            )
            self.progressbar.setMaximum(maxvalue)

    def updateProgressBar(self, val):
        if self.stopdisplaymessage:
            return
        if qgis.utils.iface is not None and self.progressbar is not None:
            self.progressbar.setValue(val)
            QApplication.processEvents()

    def closeProgressBar(self):
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().clearWidgets()
            QApplication.processEvents()

        self.progressbar = None

    def inputMessage(self, listtext, title="Lamia input", withinput=True, parent=None):

        inputdlg = InputdialogLamia(listtext, title, withinput, parent)
        inputdlg.exec_()
        return inputdlg.dialogIsFinished()


class InputdialogLamia(QDialog):
    def __init__(self, listtext, title, withinput, parent):
        super(InputdialogLamia, self).__init__(parent)
        self.setWindowTitle(title)
        layout = QFormLayout()
        self.lineedits = []

        if not withinput:
            lbl = QLabel(title)
            lbl.setStyleSheet("font-weight: bold;")
            layout.addRow(lbl)

        for text in listtext:
            lbl = QLabel(text)
            if withinput:
                le = QLineEdit()
                self.lineedits.append(le)
                layout.addRow(lbl, le)
            else:
                layout.addRow(lbl)

        butdlg = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        butdlg.accepted.connect(self.accept)
        butdlg.rejected.connect(self.reject)
        if withinput:
            butdlg.button(QDialogButtonBox.Ok).setText("Ok")
            butdlg.button(QDialogButtonBox.Cancel).setText("Cancel")
        else:
            butdlg.button(QDialogButtonBox.Ok).setText("YES")
            butdlg.button(QDialogButtonBox.Cancel).setText("NO")

        layout.addRow(butdlg)
        self.setLayout(layout)
        self.setWindowTitle("Lamia input")

        self.finished.connect(self.dialogIsFinished)

    def dialogIsFinished(self):

        if self.result() == 1:
            if self.lineedits:
                return [lineedit.text() for lineedit in self.lineedits]
            else:
                return True
        else:
            if self.lineedits:
                return []
            else:
                return False
