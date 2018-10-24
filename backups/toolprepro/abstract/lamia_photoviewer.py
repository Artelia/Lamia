
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget, QMainWindow, QSpinBox, QAction, QDialog, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QMainWindow, QSpinBox, QAction, QDialog, QLabel, QFrame)

class PhotoViewer(QLabel):
    def __init__(self, img = None):
        super(PhotoViewer, self).__init__()
        self.setFrameStyle(QFrame.StyledPanel)
        self.pixmap = QtGui.QPixmap(img)

    def paintEvent(self, event):
        size = self.size()
        painter = QtGui.QPainter(self)
        point = QtCore.QPoint(0,0)
        if not self.pixmap.isNull() :
            scaledPix = self.pixmap.scaled(size, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
            # start painting the label from left upper corner
            if True:
                point.setX((size.width() - scaledPix.width())/2)
                point.setY((size.height() - scaledPix.height())/2)
                #print point.x(), ' ', point.y()
                painter.drawPixmap(point, scaledPix)
            if False:
                painter.drawPixmap(point, scaledPix)

    def setPixmap(self, img):
        if isinstance(img, QtGui.QImage):
            self.pixmap = QtGui.QPixmap.fromImage(img)

        else:   # file
            self.pixmap = QtGui.QPixmap(img)
            self.repaint()

    def clear(self):
        self.pixmap = QtGui.QPixmap()
        self.repaint()