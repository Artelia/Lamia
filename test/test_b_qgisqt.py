import unittest, os, logging, sys, platform
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), '..'))
"""
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
"""
import networkx
import Lamia.libs.pyqtgraph


from pprint import pprint
import qgis, qgis.core, qgis.gui
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow)

import warnings, os
#warnings.simplefilter("ignore")
#os.environ["PYTHONWARNINGS"] = "ignore" # Also affect subprocesses
warnings.filterwarnings("default", category=DeprecationWarning,
                                   module='networkx')

from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from settings import *

X_BEGIN = 400000.0
Y_BEGIN = 6000000.0
TEST_WITH_FEATURE_CREATION = True
SHOWIFACE = False


class DBaseTest(unittest.TestCase):

    def setUp(self):
        """Initialisation des tests."""
        #TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')


    def test_a_testSaveFeature(self):

        testcdir = os.path.join(TESTDIR, 'c_creation')
        

        if 'SLFILE' in globals().keys() :
            self._createWin()
            self._createMainWin()
            self.wind.loadDBase(dbtype='Spatialite', slfile=SLFILE)
            self.launchTest()
        elif 'PGschema' in globals().keys():
            self._createWin()
            self._createMainWin()
            self.wind.loadDBase(dbtype='Postgis', host=PGhost, port=PGport, dbname=PGbase, schema= PGschema, user=PGuser,  password=PGpassword)
            self.launchTest()
        else:
            for work in DBTYPE:
                sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
                sqlitedbase.dbconfigreader.createDBDictionary(work)

                if not 'VARIANTES' in globals().keys():
                    variantes = list(sqlitedbase.dbconfigreader.variantespossibles)
                else:
                    variantes = globals()['VARIANTES']

                for variante in variantes:
                    logging.getLogger("Lamia_unittest").debug('*************** Opening %s %s', work, variante)
                    self._createWin()
                    self._createMainWin()

                    if SPATIALITE:
                        self._createWin()
                        self._createMainWin()
                        slfile = os.path.join(testcdir, 'sl_' + work + '_' + variante, 'test01.sqlite')
                        self.wind.loadDBase(dbtype='Spatialite', slfile=slfile)
                        self.launchTest()
                    if POSTGIS:
                        self._createWin()
                        self._createMainWin()
                        PGschema = work + '_' + variante
                        self.wind.loadDBase(dbtype='Postgis', host=PGhost, port=PGport, dbname=PGbase, schema= PGschema, user=PGuser,  password=PGpassword)
                        self.launchTest()
        
        

    def launchTest(self):
        if TEST_WITH_FEATURE_CREATION:
            self.featurecreation()
        if SHOWIFACE:
            self.showIFace()

    def showIFace(self):
        self.wind.setVisualMode(visualmode=4)
        if self.wind.qgiscanvas.layers['Infralineaire']['layer'].featureCount() > 0:
            extent = self.wind.qgiscanvas.layers['Infralineaire']['layer'].extent().buffered(10.0)
        else:
            extent = qgis.core.QgsRectangle(X_BEGIN, Y_BEGIN, X_BEGIN + 10, Y_BEGIN + 10)
        # logging.getLogger("Lamia_unittest").debug('Extent : %s', extent)
        self.wind.qgiscanvas.canvas.setExtent(extent)
        # display good widget
        # wdg = self.wind.toolwidgets['toolprepro']['Graphique_csv'][0]
        # wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)
        # wdg = self.wind.toolwidgets['toolpostpro']['Import'][0]
        # wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)
        # self.wind.dbase.printsql = True
        wdg = self.wind.toolwidgets['toolprepro']['Troncon'][0]
        wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)

        # res = self.wind.connector.inputMessage(['nom','mdp'])
        # print(res)


        self.mainwin.exec_()

    def featurecreation(self):
        toolpreprolist = self.wind.toolwidgets['toolprepro']
        global i
        i = 0
        for toolpreproname, toolpreprovalue in self.wind.toolwidgets['toolprepro'].items():
            if isinstance(toolpreprovalue, list):
                for tt in toolpreprovalue:
                    self.recursive_creation(tt)

    def recursive_creation(self, tt):
        global i
        i += 1
        name=[tt.tooltreewidgetSUBCAT]

        parentwdg=tt
        while parentwdg.parentWidget is not None:
            name.append(parentwdg.parentWidget.tooltreewidgetSUBCAT)
            parentwdg = parentwdg.parentWidget
        try:
            name = '/'.join(name[::-1])
        except TypeError as e:
            print(e, name)
            assert TypeError
        # logging.getLogger("Lamia_unittest").debug('******* Testing %s', name)
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
                if tt.DBASETABLENAME != 'Zonegeo':
                    if 'POINT' in typegeom:
                        tt.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 0)])
                    elif 'LINESTRING'  in typegeom:
                        tt.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 0),qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 1)])
                    else:
                        tt.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 0),qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 1),
                                            qgis.core.QgsPointXY(X_BEGIN + i-0.5,Y_BEGIN + 1),qgis.core.QgsPointXY(X_BEGIN + i-0.5,Y_BEGIN + 0)])
                else:
                        tt.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN - 1,Y_BEGIN - 1),qgis.core.QgsPointXY(X_BEGIN + 50 ,Y_BEGIN - 1),
                                            qgis.core.QgsPointXY(X_BEGIN + 50,Y_BEGIN + 50),qgis.core.QgsPointXY(X_BEGIN - 1,Y_BEGIN + 50)])
            self.wind.toolbarSave()
            #logging.getLogger("Lamia_unittest").debug('%s - pk created : %s', tt.DBASETABLENAME,tt.currentFeaturePK)
            self.assertIsNotNone(tt.currentFeaturePK)
        else:
            pk = tt.choosertreewidget.ids['pk'].values[0]
            tt.selectFeature(pk=pk)
            self.assertIsNotNone(pk)
            #logging.getLogger("Lamia_unittest").debug('%s - pk selected : %s', tt.DBASETABLENAME, pk)
        for childwdg in tt.dbasechildwdgfield:
            if childwdg.tooltreewidgetSUBCAT is None:
                logging.getLogger("Lamia_unittest").debug('not testing %s child of %s because tooltreewidgetSUBCAT is None',  childwdg.__class__.__name__,tt.tooltreewidgetSUBCAT)
                raise Exception('This is broken')
            else:
                self.recursive_creation(childwdg)




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

def main():
    app = initQGis()
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s',
                        datefmt="%H:%M:%S")
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
    exitQGis()

if __name__ == "__main__":
    main()

        



