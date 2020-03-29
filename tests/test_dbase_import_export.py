import unittest, os, logging, sys, shutil, logging, time
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from settings import *

REMOVEDIRONSTARTUP = False




class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""
        self.dbase = None
        self.tempdir = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')

        self.filetoimport = os.path.join(os.path.dirname(__file__),'lamia_test','BD_totale_ind11.sqlite' )
        self.fieldfile = os.path.join(os.path.dirname(__file__),'temp','export_DB','exporttest.sqlite' )

        if REMOVEDIRONSTARTUP:
            if os.path.isdir(self.tempdir):
                shutil.rmtree(self.tempdir, ignore_errors=False, onerror=None)
                time.sleep(1)
            os.mkdir(self.tempdir)
    

    """
    def test_a_import_from_sl_to_postgis(self):

        sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
        sqlitedbase.loadDBase(slfile = self.filetoimport)

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

        logging.getLogger("Lamia_unittest").debug('test_a_import_from_sl_to_postgis OK')


    def test_b_export_from_postgis_to_sl_field_investigation(self):

        work = 'Base2_digue'
        variante='lamia'

        pgdbase = DBaseParserFactory('postgis').getDbaseParser()
        pgdbase.loadDBase(host=PGhost, port=PGport, dbname=PGbase, schema= 'test_import', user=PGuser,  password=PGpassword)
        os.mkdir(os.path.dirname(self.fieldfile ))

        pgdbase.dbaseofflinemanager.exportDbase(self.fieldfile )
        pgdbase.disconnect()

        logging.getLogger("Lamia_unittest").debug('test_b_export_from_postgis_to_sl_field_investigation OK')

    """
    def test_c_modify_sl_field_investigation(self):
        sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
        sqlitedbase.loadDBase(slfile = self.fieldfile  )

        pkinfra = sqlitedbase.createNewFeature('Infralineaire')

        logging.getLogger("Lamia_unittest").debug('pkinfra %s', str(pkinfra))




    """
    def test_d_reimport_sl_field_investigation(self):
        pass

    """


    def tearDown(self):
        if False and os.path.isdir(self.tempdir):
            shutil.rmtree(self.tempdir, ignore_errors=False, onerror=None)
            time.sleep(1)



if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
        

