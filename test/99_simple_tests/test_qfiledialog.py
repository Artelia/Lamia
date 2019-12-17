try:
    from qgis.PyQt.QtGui import ( QFileDialog , QWidget, QApplication)
except ImportError:
    from qgis.PyQt.QtWidgets import ( QFileDialog, QWidget,QApplication )
import sys


class testQFileDialog():

    def __init__(self):

        self.qfiledlg = QFileDialog()
        self.qfiledlg.currentChanged.connect(self.dirchanged)
        self.qfiledlg.currentUrlChanged.connect(self.dirchanged)


    def start(self):
        self.qfiledlg.getOpenFileName(None, "ouverture", "c://","","",QFileDialog.DontUseNativeDialog )

    def dirchanged(dir):
        print('dir', dir)
        self.qfiledlg.setDirectory("c://")



app = QApplication(sys.argv)
t = testQFileDialog()
t.start()











print('end')