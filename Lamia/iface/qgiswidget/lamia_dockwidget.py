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


# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GPS2PointDockWidget
                                 A QGIS plugin
 gps to point
                             -------------------
        begin                : 2017-06-16
        git sha              : $Format:%H$
        copyright            : (C) 2017 by ARTELIA
        email                : aa
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import qgis
import time

from qgis.PyQt import QtGui, uic, QtCore
from qgis.PyQt.QtCore import pyqtSignal
from .InspectionDigue_windowwidget import InspectiondigueWindowWidget
try:
    from qgis.PyQt.QtGui import QDockWidget, QMainWindow
except:
    from qgis.PyQt.QtWidgets import QDockWidget, QMainWindow
"""
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'InspectionDigue_dockwidget_base2.ui'))
"""

class InspectiondigueDockWidget(QDockWidget):
    """!
    The dock widget used in QGis
    """

    closingPlugin = pyqtSignal()

    def __init__(self, canvas, parent=None):
        """!
        Constructor
        @param canvas : current qgsmapcanvas
        @param parent : pyqt widget parent
        """
        super(InspectiondigueDockWidget, self).__init__(parent)
        ## The windowwidget put inside te dockwidget
        self.windowwidget = InspectiondigueWindowWidget(canvas,self)

        if True:
            stylesheet = """
                        QMainWindow{
                                    background-color: rgba(0, 55, 90,80);
                                    }
                        """
            stylesheet=''
            self.windowwidget.setStyleSheet(stylesheet)


        self.setWidget(self.windowwidget)
        self.setWindowTitle('Lamia')

        if False:
            p = self.windowwidget.palette()
            p.setColor(self.windowwidget.Window(), QtCore.Qt.black)
            self.windowwidget.setPalette(p)





    def closeEvent(self, event):
        if True:
            for tool in self.windowwidget.tools:
                if tool.rubberBand is not None:
                    tool.rubberBand.reset(0)


            # self.windowwidget.dbase.reInitDBase()
            self.windowwidget.cleanLayerTree()

        self.windowwidget.gpsutil.closeConnection()
        self.closingPlugin.emit()
        event.accept()
