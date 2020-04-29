import unittest, os, logging, sys, shutil, logging, time, glob
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), '..'))
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)


import qgis, qgis.core
from qgis.PyQt.QtWidgets import  (QApplication)

from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.libslamia.lamiacost.lamiacost import CostCore
from Lamia.iface.qgsconnector.ifaceqgisconnector import QgisConnector

from settings import *

class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""
        #TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        self.connector = QgisConnector()
        self.testcdir = os.path.join(TESTDIR, 'c_creation')
        self.costtdir = os.path.join(TESTDIR, 'cost')
        if not os.path.isdir(self.costtdir):
            os.mkdir(self.costtdir)


    def test_a_generateCost(self):

        testcdir = os.path.join(TESTDIR, 'c_creation')
        
        slfile = SLFILE = os.path.join(os.path.dirname(__file__), 'datas','lamia_digue','test01.sqlite')
        sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
        sqlitedbase.loadDBase(slfile=SLFILE)
        basename = os.path.basename(SLFILE).split('.')[0]
        sqlitedbase.variante = 'test' if sqlitedbase.variante is None else sqlitedbase.variante
        self.makeTests(basename,sqlitedbase.worktype, sqlitedbase.variante, sqlitedbase)
        sqlitedbase.disconnect()
        


    def makeTests(self,dbtype,  work, variante, dbase):

        costtool = CostCore(dbase,
                            messageinstance=self.connector)

        conftotest = []

        for filename in glob.glob(os.path.join(costtool.confdataplugin, '*.csv' )):
            basename = os.path.basename(filename).split('.')[0]
            if basename == 'README':
                continue
            conftotest.append(basename)
        
        # conftotest = ['Infralineaire']        #uncomment to test only one conf 
        for confname in conftotest:
            logging.getLogger("Lamia_unittest").debug('********************** %s %s, %s - exporting conf : %s ...',dbtype, work, variante, confname)
            #destfile = os.path.join(self.reportdir, dbtype + '_' + work + '_' + variante + '_' + confname  + '.pdf')
            costtool.runCost(costfilepath=confname,
                            pkzonegeos=[2])


 


def main():
    app = initQGis()
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s',
                        datefmt="%H:%M:%S")
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
    exitQGis()

if __name__ == "__main__":
    main()
    """
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
    """



