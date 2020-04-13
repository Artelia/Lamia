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


    def test_a_testSaveFeature(self):
        self._initQGis()
        self._createWin()
        self._createMainWin()
        self.mainwin.resize(QtCore.QSize(1000,800))
        slfile = os.path.join(os.path.dirname(__file__), 'lamia_test2','test01.sqlite')
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
        self.mainwin.exec_()
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
        logging.getLogger("Lamia_unittest").debug('******* Testing %s ******', name)
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
                if 'POINT' in typegeom:
                    tt.setTempGeometry([qgis.core.QgsPointXY(i,0)])
                elif 'LINESTRING'  in typegeom:
                    tt.setTempGeometry([qgis.core.QgsPointXY(i,0),qgis.core.QgsPointXY(i,1)])
                else:
                    tt.setTempGeometry([qgis.core.QgsPointXY(i,0),qgis.core.QgsPointXY(i,1),
                                        qgis.core.QgsPointXY(i-0.5,1),qgis.core.QgsPointXY(i-0.5,0)])
            self.wind.toolbarSave()
            logging.getLogger("Lamia_unittest").debug('%s - pk created : %s', tt.DBASETABLENAME,
                                                                                tt.currentFeaturePK)
        else:
            tt.selectFeature(pk=tt.choosertreewidget.ids['pk'].values[0])

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
        self.canvas = qgis.gui.QgsMapCanvas()
        self.canvas.enableAntiAliasing(True)
        canvascrs = qgis.core.QgsCoordinateReferenceSystem()
        canvascrs.createFromString('EPSG:2154')
        self.canvas.setDestinationCrs(canvascrs)

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

    def _createWin(self):
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
        



