import unittest, os, logging, sys, shutil, logging, time
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
import psycopg2
from settings import *

logger = logging.getLogger("LamiaTest")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)




class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""
        self.dbase = None
        self.tempdir = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        if os.path.isdir(self.tempdir):
            shutil.rmtree(self.tempdir, ignore_errors=False, onerror=None)
            time.sleep(1)
        os.mkdir(self.tempdir)
    
    def test_a_import_from_sl_to_postgis(self):

        sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
        sqlitedbase.loadDBase(slfile = os.path.join(os.path.dirname(__file__),'lamia_test','BD_totale_ind11.sqlite' ))

        pgdbase = DBaseParserFactory('postgis').getDbaseParser()
        work = 'Base2_digue'
        variante='lamia'
        vardir = os.path.join(self.tempdir,'Import_DB' )
        pgdbase.createDbase(crs=CRS, 
                    worktype=work, 
                    dbaseressourcesdirectory=vardir, 
                    variante=variante,
                    host=PGhost, port=PGport, dbname=PGbase, schema= 'test_import', user=PGuser,  password=PGpassword)
        pgdbase.loadDBase(host=PGhost, port=PGport, dbname=PGbase, schema= 'test_import', user=PGuser,  password=PGpassword)
        pgdbase.dbaseofflinemanager.importDbase(sqlitedbase)

    """
    def test_b_export_from_postgis_to_sl_field_investigation(self):

        work = 'Base2_digue'
        variante='lamia'

        pgdbase = DBaseParserFactory('postgis').getDbaseParser()
        pgdbase.loadDBase(host=PGhost, port=PGport, dbname=PGbase, schema= 'test_import', user=PGuser,  password=PGpassword)
        exportfile = os.path.join(os.path.dirname(__file__),'temp','export_DB','exporttest.sqlite' )
        pgdbase.dbaseofflinemanager.exportDbase(exportfile)
        pgdbase.disconnect()
    """

    """
    def test_c_modify_sl_field_investigation(self):
        exportfile = os.path.join(os.path.dirname(__file__),'temp','export_DB','exporttest.sqlite' )
        self.dbase = DBaseParser()
        self.dbase.loadQgisVectorLayers(file=exportfile)

        #creating new entries
    """



    def test_d_reimport_sl_field_investigation(self):
        pass





if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
        



