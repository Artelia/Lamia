from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.image = ImageView(QImage())
        self.resize(500, 300)
        self.setWindowTitle("Image loader")
        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)

        """
        Adding of actions for the tool bar
        """
        iconToolBar = self.addToolBar("iconBar")

        # About
        _actionAbout = QAction(self)
        _actionAbout.triggered.connect(self._actionAbout)

        _actionAbout.setIcon(QIcon("Pics\info-icon.jpg"))
        _actionAbout.setStatusTip("Pop up the About dialog.")
        iconToolBar.addAction(_actionAbout)
        # Rubber
        _actionRubber = QAction(self)

        _actionRubber.setIcon(QIcon("Pics\eraser2.png"))
        _actionRubber.setStatusTip("Enable or Disable eraser tool")
        iconToolBar.addAction(_actionRubber)
        """
        Add of scroll bars to see properly the images
        """
        self.area = QScrollArea(self)
        self.area.setWidget(self.image)
        self.area.setWidgetResizable(True)
        self.setCentralWidget(self.area)
        """
            Add of the Menu which contains all the features like of Open/Save/..
            and the edit options
        """
        menu = QMenuBar()
        self.setMenuBar(menu)
        _file = menu.addMenu('File')
        _edit = menu.addMenu("Edit")
        # Menu Open
        _action = QAction('Open', _file, shortcut=QKeySequence.Open)
        _action.triggered.connect(self.__actionOpen)
        _file.addAction(_action)
        # Menu Save
        _action = QAction('Save', _file, shortcut=QKeySequence.Save)
        _action.triggered.connect(self.__actionSave)
        _file.addAction(_action)
        # Menu Close
        _action = QAction('Close', _file, shortcut=QKeySequence.Close)
        _action.triggered.connect(self.__actionClose)
        _file.addAction(_action)
        # Menu Edit
        # Check Box rub
        self._ckbox = QCheckBox("Rubber On")
        statusbar.addWidget(self._ckbox)
        if self._ckbox.isChecked():
            self._mode = "rub"
        else:
            self._mode = "select"
        # Init of the boolean to know whether we select or rub
        self.image.mode = self._mode
        self._ckbox.stateChanged.connect(self.__rubberBoxChanged)

    def __rubberBoxChanged(self, state):
        if self._ckbox.isChecked():
            self._mode = 'rub'
        else:
            self._mode = 'select'
        self.image.mode = self._mode

    def __actionOpen(self):
        _file = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if _file:
            self.image.setWorkingImage(QImage(_file[0]))
        else:
            print "Invalid Image"

    def __actionSave(self):
        _file = QFileDialog.getSaveFileName(parent=None, caption="Save image as")
        _result = self.image.workingImage().save(_file[0], "BMP", -1)
        # Test to know if it's working
        if _result:
            print "Saved successfully"
        else:
            print "Saving failed"

    def __actionClose(self):
        self.close()

    def _actionAbout(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PySide, Platform and the like",
                          """<b> About this program </b> 
                                  <p>Copyright  2012 Maugin Guillaume. 
                                  All rights reserved in accordance with
                                  GPL v2 or later 
                                  <p>This application can be used for
                                  displaying OS and platform details.
                                  <p>Python %s - PySide version %s - Qt version %s on %s""")


class ImageView(QWidget):
    def __init__(self, image, parent=None):
        super(ImageView, self).__init__(parent=parent)
        self.__image = image

        self._mode = "rub"
        # self._getMode()

        # Get of the mode        self._mode = image.mode
        # Init of selection
        self.__band = QRubberBand(QRubberBand.Rectangle, self)
        self.__origin = None
        # Init of rubber
        # the rub is a rectangle that should be the size of one pixel and the color and full
        # of the one selected

    def getMode(self):
        return self._mode

    def setMode(self, _newMode):
        self._mode = _newMode
        self.update()

    def setWorkingImage(self, img):
        self.__image = img
        self.setMinimumSize(img.size())
        self.update()

    def workingImage(self):
        return self.__image

    def mousePressEvent(self, e):
        self.__origin = e.pos()
        if self._mode == "select":
            # __ private variable
            self.__band.setGeometry(QRect(self.__origin, QSize()))
            self.__band.show()
        if self._mode == "rub":
            if e.button() == Qt.LeftButton:
                self.x1 = e.x()
                self.y1 = e.y()

    def mouseReleaseEvent(self, e):
        self.__band.hide()
        if self._mode == "select":
            print "La selection est :", QRect.intersect(self.__band.geometry(), self.rect())
        if self._mode == "rub":
            if e.button() == Qt.LeftButton:
                self.x2 = e.x()
                self.y2 = e.y()
                painter = QPainter(self.__image)
                painter.drawLine(self.x1, self.y1, self.x2, self.y2)
                self.update()

    def mouseMoveEvent(self, e):
        self.__band.setGeometry(QRect(self.__origin, e.pos()).normalized())
        if self._mode == "rub":
            self.x2 = e.x()
            self.y2 = e.y()
            self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.__image)

        # Important ou non ?
        try:
            painter.drawLine(self.x1, self.y1, self.x2, self.y2)
        except:
            pass

    # Init of the property for mode
    mode = property(getMode, setMode)


if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()