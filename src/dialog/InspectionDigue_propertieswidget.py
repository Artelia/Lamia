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
    from qgis.PyQt.QtGui import QWidget, QMainWindow
except:
    from qgis.PyQt.QtWidgets import QWidget, QMainWindow

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'InspectionDigue_propertieswidget.ui'))


class InspectiondiguePropertiesWidget(QWidget, FORM_CLASS):
    """!
    The dock widget used in QGis
    """

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """!
        Constructor
        @param canvas : current qgsmapcanvas
        @param parent : pyqt widget parent
        """
        super(InspectiondiguePropertiesWidget, self).__init__(parent)
        self.setupUi(self)

        """
        ## The windowwidget put inside te dockwidget
        self.windowwidget = InspectiondigueWindowWidget(canvas)
        self.setWidget(self.windowwidget)
        self.setWindowTitle('InspectionDigue')
        """


    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
