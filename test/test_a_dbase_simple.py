import unittest, os, logging, sys, shutil, logging, time
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), ".."))
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

from settings import *

KEEP_DB_CREATION = True


class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        # TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        if os.path.isdir(TESTDIR):
            shutil.rmtree(TESTDIR, ignore_errors=False, onerror=None)
            time.sleep(1)
        os.mkdir(TESTDIR)

    def test_a_DbaseInit(self):
        if SPATIALITE:
            sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
            slfile = os.path.join(TESTDIR, "a_testslinit", "test_a.sqlite")
            os.mkdir(os.path.dirname(slfile))
            sqlitedbase.initDBase(slfile=slfile)
        if POSTGIS:
            pgdbase = DBaseParserFactory("postgis").getDbaseParser()
            pgdbase.initDBase(
                host=PGhost,
                port=PGport,
                dbname=PGbase,
                schema="testa",
                user=PGuser,
                password=PGpassword,
            )

        logging.getLogger("Lamia_unittest").debug("test_a_DbaseInit OK")

    def test_b_DbaseReader(self):
        for work in DBTYPE:
            sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
            sqlitedbase.dbconfigreader.createDBDictionary(work)
            # logging.getLogger("Lamia_unittest").debug('%s', str(sqlitedbase.dbconfigreader.dbasetables.keys()))
            self.assertTrue(True)

        logging.getLogger("Lamia_unittest").debug("test_b_DbaseReader OK")

    def test_c_DbaseCreate(self):
        testcdir = os.path.join(TESTDIR, "c_creation")
        os.mkdir(testcdir)
        for work in DBTYPE:
            sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
            # slfile = os.path.join(testcdir, work ,'test01.sqlite')
            # os.mkdir(os.path.dirname(slfile))
            sqlitedbase.dbconfigreader.createDBDictionary(work)
            if not "VARIANTES" in globals().keys():
                variantes = list(sqlitedbase.dbconfigreader.variantespossibles)
            else:
                variantes = globals()["VARIANTES"]
            for variante in variantes:
                # spatialite
                if SPATIALITE:
                    logging.getLogger("Lamia_unittest").debug(
                        "Creating spatialite %s %s ...", work, variante
                    )
                    slfile = os.path.join(
                        testcdir, "sl_" + work + "_" + variante, "test01.sqlite"
                    )
                    os.mkdir(os.path.dirname(slfile))
                    sqlitedbase.createDBase(
                        crs=CRS,
                        worktype=work,
                        dbaseressourcesdirectory=None,
                        variante=variante,
                        slfile=slfile,
                    )
                    dbasetables = sqlitedbase.dbconfigreader.dbasetables
                    for tablename in dbasetables.keys():
                        dbasecolums = sqlitedbase.getColumns(tablename)
                        for field in dbasetables[tablename]["fields"].keys():
                            if not field in dbasecolums:
                                logging.getLogger("Lamia_unittest").debug(
                                    "%s %s", tablename, field
                                )
                                logging.getLogger("Lamia_unittest").debug(
                                    "%s", str(dbasecolums)
                                )
                                assert False

                    sqlitedbase.disconnect()

                if POSTGIS:
                    logging.getLogger("Lamia_unittest").debug(
                        "Creating postgis %s %s ...", work, variante
                    )
                    pgdir = os.path.join(testcdir, "pg_" + work + "_" + variante)
                    os.mkdir(pgdir)
                    pgdbase = DBaseParserFactory("postgis").getDbaseParser()
                    pgdbase.createDBase(
                        crs=CRS,
                        worktype=work,
                        dbaseressourcesdirectory=pgdir,
                        variante=variante,
                        host=PGhost,
                        port=PGport,
                        dbname=PGbase,
                        schema=work + "_" + variante,
                        user=PGuser,
                        password=PGpassword,
                    )
                    dbasetables = pgdbase.dbconfigreader.dbasetables
                    for tablename in dbasetables.keys():
                        dbasecolums = pgdbase.getColumns(tablename)
                        for field in dbasetables[tablename]["fields"].keys():
                            if not field.lower() in dbasecolums:
                                logging.getLogger("Lamia_unittest").debug(
                                    "%s %s", tablename, field
                                )
                                logging.getLogger("Lamia_unittest").debug(
                                    "%s", str(dbasecolums)
                                )
                                assert False
                    pgdbase.disconnect()

        logging.getLogger("Lamia_unittest").debug("test_c_DbaseCreate OK")


def main():
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)
    unittest.main()


if __name__ == "__main__":
    main()

