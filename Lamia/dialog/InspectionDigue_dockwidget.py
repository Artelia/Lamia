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
        self.setWidget(self.windowwidget)
        self.setWindowTitle('Lamia')
        


    def closeEvent(self, event):
        for tool in self.windowwidget.tools:
            if tool.rubberBand is not None:
                tool.rubberBand.reset(0)
                
        self.windowwidget.dbase.reInitDBase()

        self.windowwidget.gpsutil.closeConnection()
        self.closingPlugin.emit()
        event.accept()
