import unittest, os, logging, sys, shutil, logging, time, glob, json
from pprint import pprint
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), '..'))
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)


import qgis, qgis.core
from qgis.PyQt.QtWidgets import  (QApplication)
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow)


from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.iface.qgsconnector.ifaceqgisconnector import QgisConnector


from settings import *

class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""
        self.tempdir = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        self.connector = QgisConnector()
        self.testcdir = os.path.join(self.tempdir, 'c_creation')
        self.offlinetdir = os.path.join(self.tempdir, 'offline')
        if not os.path.isdir(self.offlinetdir):
            os.mkdir(self.offlinetdir)


    def test_a_generateImport(self):
        self._createWin()
        self._createMainWin()

        SLFILE = os.path.join(os.path.dirname(__file__), 'lamia_test','test01.sqlite')

        #testcdir = os.path.join(self.tempdir, 'c_creation')
        #DBTYPE = ['base2_digue']
        #VARIANTE = ['Lamia']
        #work = DBTYPE[0]
        #variante = VARIANTE[0]
        #print(testcdir, work, variante)
        if SPATIALITE:
            offlinepath = os.path.join(self.offlinetdir,'testoffline.sqlite')

            self.wind.loadDBase(dbtype='Spatialite', slfile=SLFILE)
            logging.getLogger("Lamia_unittest").debug('ressourcedir %s', self.wind.dbase.dbaseressourcesdirectory)
            self.wind.pullDBase(exportfilepath=offlinepath)

            #self.wind.loadDBase(dbtype='Spatialite', slfile=offlinepath)
            logging.getLogger("Lamia_unittest").debug('ressourcedir %s', self.wind.dbase.dbaseressourcesdirectory)
            self.wind.pushDBase()



        """
        if POSTGIS:
            pgdbase = DBaseParserFactory('postgis').getDbaseParser()
            pgdbase.loadDBase(host=PGhost, port=PGport, dbname=PGbase, schema= PGschema, user=PGuser,  password=PGpassword)
            self.makeTests('postgis',work, variante, pgdbase)
            pgdbase.disconnect()
        """



    def _createMainWin(self):
        self.mainwin = UserUI()
        self.mainwin.frame.layout().addWidget(self.canvas)
        self.mainwin.frame_2.layout().addWidget(self.wind)
        self.mainwin.setParent(None)
        self.mainwin.resize(QtCore.QSize(1000,800))

    def _createWin(self):
        self.canvas = qgis.gui.QgsMapCanvas()
        self.canvas.enableAntiAliasing(True)
        canvascrs = qgis.core.QgsCoordinateReferenceSystem()
        canvascrs.createFromString('EPSG:2154')
        self.canvas.setDestinationCrs(canvascrs)

        self.wind = LamiaWindowWidget()
        self.wind.qgiscanvas.setCanvas(self.canvas)

        stylesheet = """
                    QMainWindow{
                                background-color: rgba(0, 55, 90,80);
                                }
                    """
        stylesheet = ''
        self.wind.setStyleSheet(stylesheet)
        self.wind.setParent(None)
        self.dbase = self.wind.dbase
        self.mainwin = None


class UserUI(QDialog):

    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'qtdialog', 'mainwindows.ui')
        uic.loadUi(uipath, self)

def main():
    app = initQGis()
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s',
                        datefmt="%H:%M:%S")
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
    exitQGis()

if __name__ == "__main__":
    main()




