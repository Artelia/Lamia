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
from Lamia.iface.qgscanvas.ifaceqgiscanvas import QgisCanvas
# from settings import *



class DBaseViewer():

    def __init__(self):
        pass


    def run(self):
        pgdbase = DBaseParserFactory('postgis').getDbaseParser()
            
        if False:
            dbaseressourcesdirectory = os.path.join(os.path.dirname(__file__),'importBM_pg')
            pgdbase.createDBase(crs='2154', 
                                worktype='Base2_digue', 
                                dbaseressourcesdirectory=dbaseressourcesdirectory, 
                                variante='Lamia',
                                host='localhost', 
                                port='5432', 
                                dbname='lamiaunittest', 
                                schema='importBM', 
                                user='pvr',  
                                password='pvr')
            pgdbase.loadDBase(host='localhost', 
                                port='5432', 
                                dbname='lamiaunittest', 
                                schema='importBM', 
                                user='pvr',  
                                password='pvr')

            bmtoimport = os.path.join(os.path.dirname(__file__),'..','test','datas', 'lamia_digue','test01.sqlite')

            pgdbase.dbaseofflinemanager.addDBase(**{'slfile': bmtoimport})

        pgdbase.loadDBase(host='localhost', 
                            port='5432', 
                            dbname='lamiaunittest', 
                            schema='importBM', 
                            user='pvr',  
                            password='pvr')
        canvas = qgis.gui.QgsMapCanvas()
        canvas.enableAntiAliasing(True)
        canvascrs = qgis.core.QgsCoordinateReferenceSystem()
        canvascrs.createFromString('EPSG:2154')
        canvas.setDestinationCrs(canvascrs)
        
        qgscanvas = QgisCanvas(canvas)

        qgscanvas.createLayersForQgisServer(pgdbase)

        if False:

            if True :
                SLFILE = os.path.join(os.path.dirname(__file__), '..','test','datas','lamia_digue','test01.sqlite')
                #SLFILE = r"C:\Users\Public\Documents\lamia\test01\test01.sqlite"
                self._createWin()
                self._createMainWin()
                self.wind.loadDBase(dbtype='Spatialite', slfile=SLFILE)
                
            if False:
                self._createWin()
                self._createMainWin()
                self.wind.loadDBase(dbtype='Postgis', host=PGhost, port=PGport, dbname=PGbase, schema= PGschema, user=PGuser,  password=PGpassword)
                self.launchTest()

            self.wind.setVisualMode(visualmode=1)
            self.showIFace()
        

    def showIFace(self):
        
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

def initQGis():
    if platform.system() == 'Windows':
        qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
    elif platform.system() == 'Linux':
        qgis_path = '/usr'

    app = qgis.core.QgsApplication([], True)
    qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
    qgis.core.QgsApplication.initQgis()
    return app

def exitQGis():
    qgis.core.QgsApplication.exitQgis()

def main():
    app = initQGis()
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s',
                        datefmt="%H:%M:%S")
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )

    #unittest.main()
    dbaseviewer = DBaseViewer()
    dbaseviewer.run()


    exitQGis()

if __name__ == "__main__":
    main()

        



