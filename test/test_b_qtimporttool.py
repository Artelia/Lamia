import unittest, os, logging, sys, shutil, logging, time, glob
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), '..'))
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)


import qgis, qgis.core
from qgis.PyQt.QtWidgets import  (QApplication)

from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
#from Lamia.libslamia.lamiaimport.lamiaimport import ImportCore
from Lamia.iface.qgiswidget.tools.toolpostpro.base2.Lamia_import_tool_flowchart import FlowChartWidget
from Lamia.iface.qgsconnector.ifaceqgisconnector import QgisConnector


from settings import *

class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""
        self.tempdir = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        self.connector = QgisConnector()
        self.testcdir = os.path.join(self.tempdir, 'c_creation')
        self.costtdir = os.path.join(self.tempdir, 'cost')
        if not os.path.isdir(self.costtdir):
            os.mkdir(self.costtdir)


    def test_a_generateImport(self):

        testcdir = os.path.join(self.tempdir, 'c_creation')

        DBTYPE = ['base2_digue']
        VARIANTE = ['Lamia']
        work = DBTYPE[0]
        variante = VARIANTE[0]
        print(testcdir, work, variante)
        if SPATIALITE:
            slfile = os.path.join(testcdir, 'sl_' + work + '_' + variante, 'test01.sqlite')
            sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
            sqlitedbase.loadDBase(slfile=slfile)
            self.makeTests('spatialite',work, variante, sqlitedbase)
            sqlitedbase.disconnect()
        if POSTGIS:
            pgdbase = DBaseParserFactory('postgis').getDbaseParser()
            pgdbase.loadDBase(host=PGhost, port=PGport, dbname=PGbase, schema= PGschema, user=PGuser,  password=PGpassword)
            self.makeTests('postgis',work, variante, pgdbase)
            pgdbase.disconnect()
        


    def makeTests(self,dbtype,  work, variante, dbase):
        importwdg = FlowChartWidget(dbase=dbase,
                                    messageinstance=self.connector,
                                    mainifacewidget=None)
        configdir = os.path.join(os.path.dirname(__file__),'shpforimporttest')
        importlayerpath = os.path.join(configdir,'TRONCONS_TEST.shp')
        importlayer = qgis.core.QgsVectorLayer(importlayerpath,'testimport','ogr')
        importwdg.initFromandToLayers(fromqgslayer=importlayer,
                                     tolayername='Infralineaire')
        configfile = os.path.join(configdir,'configfortest.fc')
        importwdg.fcLoad(fileName=configfile)

        #importwdg.exec_()
        importwdg.runImport()



def main():
    app = initQGis()
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s',
                        datefmt="%H:%M:%S")
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
    exitQGis()

if __name__ == "__main__":
    main()




