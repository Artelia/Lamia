import unittest, os, logging, sys, shutil, logging, time
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), '..'))
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory


from settings import *


class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""

    
    def test_a_updatedbase(self):
        # first create old dbase
        
        if SPATIALITE:
            slfile = os.path.join(TESTDIR, 'b_testupdate','test_a.sqlite')
            sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
            if not os.path.isdir(os.path.dirname(slfile)):
                os.mkdir(os.path.dirname(slfile))
            sqlitedbase.createDBase(crs=CRS, 
                                    worktype='Base2_digue', 
                                    dbaseressourcesdirectory=None, 
                                    variante='Lamia',
                                    slfile=slfile,
                                    baseversion = '0_3',
                                    workversion = '0_1')
            sqlitedbase.disconnect()
            #then reload it - autoupdate will be done
            sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
            sqlitedbase.loadDBase(slfile=slfile)


def main():
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()

if __name__ == "__main__":
    main()
    """
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
    """



