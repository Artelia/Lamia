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


from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (
        QWidget,
        QMainWindow,
        QSpinBox,
        QAction,
        QDialog,
        QLabel,
        QFrame,
    )
except ImportError:
    from qgis.PyQt.QtWidgets import (
        QWidget,
        QMainWindow,
        QSpinBox,
        QAction,
        QDialog,
        QLabel,
        QFrame,
    )


class PictureViewer(QLabel):
    def __init__(self, img=None):
        super(PictureViewer, self).__init__()
        self.setFrameStyle(QFrame.StyledPanel)
        self.pixmap = QtGui.QPixmap(img)

    def paintEvent(self, event):
        size = self.size()
        painter = QtGui.QPainter(self)
        point = QtCore.QPoint(0, 0)
        if not self.pixmap.isNull():
            scaledPix = self.pixmap.scaled(
                size,
                QtCore.Qt.KeepAspectRatio,
                transformMode=QtCore.Qt.SmoothTransformation,
            )
            # start painting the label from left upper corner
            if True:
                point.setX((size.width() - scaledPix.width()) / 2)
                point.setY((size.height() - scaledPix.height()) / 2)
                # print point.x(), ' ', point.y()
                painter.drawPixmap(point, scaledPix)
            if False:
                painter.drawPixmap(point, scaledPix)

    def setPixmap(self, img):
        if isinstance(img, QtGui.QImage):
            self.pixmap = QtGui.QPixmap.fromImage(img)

        elif isinstance(img, str):  # file
            self.pixmap = QtGui.QPixmap(img)
            self.repaint()

        elif isinstance(img, bytes):  # db thumbnail
            self.pixmap = QtGui.QPixmap()
            self.pixmap.loadFromData(img, "PNG")
            self.repaint()

    def clear(self):
        self.pixmap = QtGui.QPixmap()
        self.repaint()
