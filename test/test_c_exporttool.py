import unittest, os, logging, sys, shutil, logging, time, glob
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

import qgis


sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), ".."))
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.api.libslamia.lamiaexportshp.lamiaexportshp import ExportShapefileCore
from Lamia.qgisiface.iface.qgsconnector.ifaceqgisconnector import QgisConnector

# from . import settings
# import settings
from settings import *


class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        # TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        self.connector = QgisConnector()
        self.testcdir = os.path.join(TESTDIR, "c_creation")
        self.exportshpdir = os.path.join(TESTDIR, "exportshp")
        if not os.path.isdir(self.exportshpdir):
            os.mkdir(self.exportshpdir)
        """
        if os.path.isdir(TESTDIR):
            shutil.rmtree(TESTDIR, ignore_errors=False, onerror=None)
            time.sleep(1)
        os.mkdir(TESTDIR)
        """

    def test_a_generateShapefile(self):

        testcdir = os.path.join(TESTDIR, "c_creation")

        if "SLFILE" in globals().keys():
            sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
            sqlitedbase.loadDBase(slfile=SLFILE)
            basename = os.path.basename(SLFILE).split(".")[0]
            self.makeTests(
                basename, sqlitedbase.worktype, sqlitedbase.variante, sqlitedbase
            )
            sqlitedbase.disconnect()
        elif "PGschema" in globals().keys():
            pgdbase = DBaseParserFactory("postgis").getDbaseParser()
            pgdbase.loadDBase(
                host=PGhost,
                port=PGport,
                dbname=PGbase,
                schema=PGschema,
                user=PGuser,
                password=PGpassword,
            )
            basename = PGschema
            self.makeTests(basename, pgdbase.worktype, pgdbase.variante, sqlitedbase)
            pgdbase.disconnect()
        else:
            for work in DBTYPE:
                sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
                sqlitedbase.dbconfigreader.createDBDictionary(work)

                if not "VARIANTES" in globals().keys():
                    variantes = list(sqlitedbase.dbconfigreader.variantespossibles)
                else:
                    variantes = globals()["VARIANTES"]

                for variante in variantes:
                    logging.getLogger("Lamia_unittest").debug(
                        "*************** Opening %s %s", work, variante
                    )

                    if SPATIALITE:
                        slfile = os.path.join(
                            testcdir, "sl_" + work + "_" + variante, "test01.sqlite"
                        )
                        sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
                        sqlitedbase.loadDBase(slfile=slfile)
                        self.makeTests("spatialite", work, variante, sqlitedbase)
                        sqlitedbase.disconnect()
                    if POSTGIS:
                        pgdbase = DBaseParserFactory("postgis").getDbaseParser()
                        pgdbase.loadDBase(
                            host=PGhost,
                            port=PGport,
                            dbname=PGbase,
                            schema=work + "_" + variante,
                            user=PGuser,
                            password=PGpassword,
                        )
                        self.makeTests("postgis", work, variante, pgdbase)
                        pgdbase.disconnect()

        # exitQGis()

    """
    def test_c_DbaseCreate(self):

        for work in DBTYPE:
            sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
            # slfile = os.path.join(testcdir, work ,'test01.sqlite')
            # os.mkdir(os.path.dirname(slfile))
            sqlitedbase.dbconfigreader.createDBDictionary(work)

            if not 'variantes' in globals().keys():
                variantes = list(sqlitedbase.dbconfigreader.variantespossibles)
            else:
                variantes = globals()['variantes']

            for variante in variantes:
                # spatialite
                if SPATIALITE:
                    logging.getLogger("Lamia_unittest").debug('Creating spatialite %s %s ...', work, variante)
                    slfile = os.path.join(self.testcdir, 'sl_' + work + '_' + variante, 'test01.sqlite')
                    
                    #os.mkdir(os.path.dirname(slfile))
                    sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
                    sqlitedbase.loadDBase(slfile=slfile)
                    exportershp = ExportShapefileCore(sqlitedbase,
                                                        messageinstance=self.connector)
                    self.makeTests('spatialite',work, variante, exportershp)
                    sqlitedbase.disconnect()

                if POSTGIS:
                    logging.getLogger("Lamia_unittest").debug('Creating postgis %s %s ...', work, variante)
                    pgdir = os.path.join(self.testcdir, 'pg_' + work + '_' + variante)
                    #os.mkdir(pgdir)
                    pgdbase = DBaseParserFactory('postgis').getDbaseParser()
                    pgdbase.loadDBase(host=PGhost, port=PGport, dbname=PGbase, schema= work + '_' + variante, user=PGuser,  password=PGpassword)
                    exportershp = ExportShapefileCore(pgdbase,
                                                        messageinstance=self.connector)
                    self.makeTests('postgis', work, variante, exportershp)
                    sqlitedbase.disconnect()
                    pgdbase.disconnect()

    
        logging.getLogger("Lamia_unittest").debug('test_c_DbaseCreate OK')
    """

    def makeTests(self, dbtype, work, variante, dbase):

        exportershp = ExportShapefileCore(dbase, messageinstance=self.connector)

        conftotest = []
        for filename in glob.glob(os.path.join(exportershp.confdatadirplugin, "*.txt")):
            basename = os.path.basename(filename).split(".")[0]
            if basename == "README":
                continue
            conftotest.append(basename)

        # conftotest = ['Infralineaire']        #uncomment to test only one conf
        for confname in conftotest:
            logging.getLogger("Lamia_unittest").debug(
                "********************** %s %s, %s - exporting conf : %s ...",
                dbtype,
                work,
                variante,
                basename,
            )
            destfile = os.path.join(
                self.exportshpdir,
                dbtype + "_" + work + "_" + variante + "_" + confname + ".shp",
            )
            exportershp.runExport(
                destinationshapefile=destfile,
                exportconffilepath=confname,
                pkzonegeos=[],
            )


def main():
    app = initQGis()
    logging.basicConfig(
        format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)
    unittest.main()
    exitQGis()


if __name__ == "__main__":
    main()

