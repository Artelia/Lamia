import unittest, os, logging, sys, platform
import qgis, qgis.core, qgis.gui
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow)

from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from settings import *

DBTYPE = ['Base2_assainissement']
X_BEGIN = 400000.0
Y_BEGIN = 6000000.0

class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""
        self.tempdir = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        """
        self.tempdir = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        if os.path.isdir(self.tempdir):
            shutil.rmtree(self.tempdir, ignore_errors=False, onerror=None)
            time.sleep(1)
        os.mkdir(self.tempdir)

        self.filetoimport = os.path.join(os.path.dirname(__file__),'lamia_test1','test01.sqlite' )
        """
    """
    def test_a_testSaveFeature(self):
        testcdir = os.path.join(self.tempdir, 'c_creation')
        work = 'Base2_assainissement'
        variante = '2018_SNCF'       # Lamia 2018_SNCF CD41
        self._initQGis()
        self._createWin()
        self._createMainWin()
        slfile = os.path.normpath(os.path.join(os.path.dirname(__file__), 'lamia_test2','test01.sqlite'))
        #slfile = os.path.join(testcdir, 'c_creation','sl_Base2_assainissement_CD41','test01.sqlite')
        slfile = os.path.normpath(os.path.join(testcdir, 'sl_' + work + '_' + variante, 'test01.sqlite'))
        self.wind.loadDBase(dbtype='Spatialite', slfile=slfile)
        self.wind.setVisualMode(visualmode=1)
        #selectfeaturetest
        if False:
            toolpreprolist = self.wind.toolwidgets['toolprepro']
            global i
            i = 0
            for toolpreproname, toolpreprovalue in self.wind.toolwidgets['toolprepro'].items():
                if isinstance(toolpreprovalue, list):
                    for tt in toolpreprovalue:
                        self.recursive_creation(tt)
        extent = self.wind.qgiscanvas.layers['Photo']['layerqgis'].extent().buffered(10.0)
        self.wind.qgiscanvas.canvas.setExtent(extent)

        # self.wind.qgiscanvas.canvas.xyCoordinates.connect(self.emitpoint)
        #self.wind.qgiscanvas.canvas.setCenter(qgis.core.QgsPointXY(X_BEGIN, Y_BEGIN))
        # self.wind.qgiscanvas.canvas.setScale(1000.0)
        self.mainwin.exec_()
        self._exitQGis()


    """
    def test_a_testSaveFeature(self):
        testcdir = os.path.join(self.tempdir, 'c_creation')
        self._initQGis()
        #self._createWin()
        #self._createMainWin()
        for work in DBTYPE:
            sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
            # slfile = os.path.join(testcdir, work ,'test01.sqlite')
            # os.mkdir(os.path.dirname(slfile))
            sqlitedbase.dbconfigreader.createDBDictionary(work)
            variantes = list(sqlitedbase.dbconfigreader.variantespossibles)
            logging.getLogger("Lamia_unittest").debug('************* Opening %s', variantes)
            for variante in variantes:
                logging.getLogger("Lamia_unittest").debug('************* Opening %s %s', work, variante)
                #self._initQGis()
                self._createWin()
                self._createMainWin()
                
                #slfile = os.path.join(os.path.dirname(__file__), 'lamia_test2','test01.sqlite')
                #slfile = os.path.join(testcdir, 'c_creation','sl_Base2_assainissement_CD41','test01.sqlite')
                slfile = os.path.join(testcdir, 'sl_' + work + '_' + variante, 'test01.sqlite')
                self.wind.loadDBase(dbtype='Spatialite', slfile=slfile)
                self.wind.setVisualMode(visualmode=1)
                #selectfeaturetest
                if True:
                    toolpreprolist = self.wind.toolwidgets['toolprepro']
                    global i
                    i = 0
                    for toolpreproname, toolpreprovalue in self.wind.toolwidgets['toolprepro'].items():
                        if isinstance(toolpreprovalue, list):
                            for tt in toolpreprovalue:
                                self.recursive_creation(tt)
                
                self.wind.qgiscanvas.layers['Photo']['layerqgis'].triggerRepaint()
                self.wind.qgiscanvas.canvas.refreshAllLayers()
                extent = self.wind.qgiscanvas.layers['Photo']['layerqgis'].extent().buffered(10.0)
                print(extent)
                extent = qgis.core.QgsRectangle(X_BEGIN, Y_BEGIN, X_BEGIN + 10, Y_BEGIN + 10)
                self.wind.qgiscanvas.canvas.setExtent(extent)
                self.mainwin.exec_()
                #self.wind.dbase.disconnect()
        self._exitQGis()


    def recursive_creation(self, tt):
        global i
        i += 1
        name=[tt.tooltreewidgetSUBCAT]
        parentwdg=tt
        while parentwdg.parentWidget is not None:
            name.append(parentwdg.parentWidget.tooltreewidgetSUBCAT)
            parentwdg = parentwdg.parentWidget
        name = '/'.join(name[::-1])
        logging.getLogger("Lamia_unittest").debug('******* Testing %s', name)
        #self.wind.MaintreeWidget.setCurrentItem(tt.qtreewidgetitem)
        tt.widgetClicked()
        if len(tt.choosertreewidget.ids) == 0:
            self.wind.toolbarNew()
            dbasetable = self.wind.dbase.dbasetables[tt.DBASETABLENAME]
            #logging.getLogger("Lamia_unittest").debug('fieldgeom : %s , tempgeom : %s',
            #                                            'geom' in dbasetable.keys(),
            #                                            tt.tempgeometry)
            if 'geom' in dbasetable.keys() and tt.tempgeometry is None:
                typegeom = dbasetable['geom']
                """
                X_BEGIN = 100000.0
                Y_BEGIN = 6000000.0
                """
                if 'POINT' in typegeom:
                    tt.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 0)])
                elif 'LINESTRING'  in typegeom:
                    tt.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 0),qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 1)])
                else:
                    tt.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 0),qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 1),
                                        qgis.core.QgsPointXY(X_BEGIN + i-0.5,Y_BEGIN + 1),qgis.core.QgsPointXY(X_BEGIN + i-0.5,Y_BEGIN + 0)])
            self.wind.toolbarSave()
            logging.getLogger("Lamia_unittest").debug('%s - pk created : %s', tt.DBASETABLENAME,
                                                                                tt.currentFeaturePK)
        else:
            pk = tt.choosertreewidget.ids['pk'].values[0]
            tt.selectFeature(pk=pk)
            logging.getLogger("Lamia_unittest").debug('%s - pk selected : %s', tt.DBASETABLENAME,
                                                                                pk)
        for childwdg in tt.dbasechildwdgfield:
            self.recursive_creation(childwdg)



    """
    def test_a_showLamia(self):
        self._initQGis()
        self._createWin()
        self._createMainWin()
        self.mainwin.resize(QtCore.QSize(1000,800))
        slfile = os.path.join(os.path.dirname(__file__), 'lamia_test2','test01.sqlite')
        self.wind.loadDBase(dbtype='Spatialite', slfile=slfile)
        # self.wind.setVisualMode(visualmode=1)
        #selectfeaturetest
        wdglist = self.wind.toolwidgets['toolprepro']['Troncon']
        if isinstance(wdglist, list):
            for tt in wdglist:
                self.wind.MaintreeWidget.setCurrentItem(tt.qtreewidgetitem)
                tt.selectFeature(pk=7158)

        self.mainwin.exec_()
        self._exitQGis()
    """


    """
    def test_b_OpeningToolWidget(self):
        logging.getLogger("Lamia_unittest").debug('ok01')
        self._initQGis()
        self._createWin()
        self._createMainWin()
        logging.getLogger("Lamia_unittest").debug('ok02')

        self.wind.loadDBase(dbtype='Spatialite', slfile='/usr/src/Lamia/tests/lamia_test2/test01.sqlite')
        
        #test opening tools (prepro and postpro)
        self.wind.setVisualMode(visualmode=1)
        for toolname in self.wind.toolwidgets['toolprepro'].keys():
            wdglist = self.wind.toolwidgets['toolprepro'][toolname]
            if isinstance(wdglist, list):
                for tt in wdglist:
                    self.wind.MaintreeWidget.setCurrentItem(tt.qtreewidgetitem)
        self.wind.setVisualMode(visualmode=4)
        for toolname in self.wind.toolwidgets['toolpostpro'].keys():
            wdglist = self.wind.toolwidgets['toolpostpro'][toolname]
            if isinstance(wdglist, list):
                for tt in wdglist:
                    self.wind.MaintreeWidget.setCurrentItem(tt.qtreewidgetitem)
            else:
                self.wind.MaintreeWidget.setCurrentItem(wdglist.qtreewidgetitem)

        self._exitQGis()
    """

    def _initQGis(self):
        if platform.system() == 'Windows':
            qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
        elif platform.system() == 'Linux':
            qgis_path = '/usr'

        self.app = qgis.core.QgsApplication([], True)
        qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
        qgis.core.QgsApplication.initQgis()


        # self.createWin()
        # self.loadLocale() TODO
        # self.testMethod()

    def _exitQGis(self):
        qgis.core.QgsApplication.exitQgis()

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


    def _loadLocale(self):
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
    #logging.basicConfig( stream=sys.stderr )
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s')
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )

    unittest.main()
        



