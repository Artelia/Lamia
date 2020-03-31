import unittest, os, logging, sys, platform
import qgis, qgis.core, qgis.gui
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow)

from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget

from settings import *


class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""
        pass
        """
        self.tempdir = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        if os.path.isdir(self.tempdir):
            shutil.rmtree(self.tempdir, ignore_errors=False, onerror=None)
            time.sleep(1)
        os.mkdir(self.tempdir)

        self.filetoimport = os.path.join(os.path.dirname(__file__),'lamia_test1','test01.sqlite' )
        """


    def test_a_DbaseInit(self):
        logging.getLogger("Lamia_unittest").debug('ok01')
        self.initQGis()
        self.createWin()
        self.createMainWin()
        logging.getLogger("Lamia_unittest").debug('ok02')

        self.wind.loadDBase(dbtype='Spatialite', slfile='/home/docker/temp_base2_ass2/test01.sqlite')

        #self.mainwin.exec_()

        #sys.exit()
        self.exitQGis()


        """
        sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
        slfile = os.path.join(self.tempdir, 'a_testslinit','test_a.sqlite')
        os.mkdir(os.path.dirname(slfile))
        sqlitedbase.initDBase(slfile=slfile)

        pgdbase = DBaseParserFactory('postgis').getDbaseParser()
        pgdbase.initDBase(host=PGhost, 
                          port=PGport, 
                          dbname=PGbase, 
                          schema='testa', 
                          user=PGuser,  
                          password=PGpassword)

        logging.getLogger("Lamia_unittest").debug('test_a_DbaseInit OK')
        """

    def initQGis(self):


        if platform.system() == 'Windows':
            qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
        elif platform.system() == 'Linux':
            qgis_path = '/usr'


        self.app = qgis.core.QgsApplication([], True)
        qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
        qgis.core.QgsApplication.initQgis()
        self.canvas = qgis.gui.QgsMapCanvas()
        self.canvas.enableAntiAliasing(True)
        self.canvas.setDestinationCrs(qgis.core.QgsCoordinateReferenceSystem(2154))

        # self.createWin()

        # self.loadLocale() TODO


        # self.testMethod()
        #program.run(self.canvas, True, "spatialite")
        #self.app.exec_()



    def exitQGis(self):
        qgis.core.QgsApplication.exitQgis()
        print('Test fini')

    def createMainWin(self):
        self.mainwin = UserUI()
        self.mainwin.frame.layout().addWidget(self.canvas)
        self.mainwin.frame_2.layout().addWidget(self.wind)
        self.mainwin.setParent(None)

    def createWin(self):
        self.wind = LamiaWindowWidget()
        self.wind.qgiscanvas.setCanvas(self.canvas)
        # self.wind.createDBase()

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


    def loadLocale(self):
        # initialize locale
        # locale = QSettings().value('locale/userLocale')[0:2]
        locale = 'fr'
        plugin_dir = os.path.join(os.path.dirname(__file__),'..', 'Lamia')
        locale_path = os.path.join(
            plugin_dir,
            'i18n',
            'Lamia_{}.qm'.format(locale))

        print(locale_path,qVersion() )

        if os.path.exists(locale_path):
            print('ok')
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
                #self.app.installTranslator(self.translator)




class UserUI(QDialog):

    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'qtdialog', 'mainwindows.ui')
        uic.loadUi(uipath, self)



if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
        



