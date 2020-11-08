import unittest, os, logging, sys, shutil, logging, time, glob

sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), ".."))
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)


import qgis, qgis.core
from qgis.PyQt.QtWidgets import QApplication

from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.api.libslamia.lamiareport.lamiareport import ReportCore
from Lamia.qgisiface.iface.qgsconnector.ifaceqgisconnector import QgisConnector

from settings import *


class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        # TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        self.connector = QgisConnector()
        self.testcdir = os.path.join(TESTDIR, "c_creation")
        self.reportdir = os.path.join(TESTDIR, "report")
        if not os.path.isdir(self.reportdir):
            os.mkdir(self.reportdir)

    def test_a_generateReport(self):

        testcdir = os.path.join(TESTDIR, "c_creation")

        if "SLFILE" in globals().keys():
            sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
            sqlitedbase.loadDBase(slfile=SLFILE)
            basename = os.path.basename(SLFILE).split(".")[0]
            sqlitedbase.variante = (
                "test" if sqlitedbase.variante is None else sqlitedbase.variante
            )
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

    """
    def test_c_DbaseCreate(self):

        self._initQGis()

        for work in DBTYPE:


            if not 'variantes' in globals().keys():
                sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
                sqlitedbase.dbconfigreader.createDBDictionary(work)
                variantes = list(sqlitedbase.dbconfigreader.variantespossibles)
            else:
                variantes = globals()['variantes']

            for variante in variantes:
                # spatialite
                if SPATIALITE:
                    logging.getLogger("Lamia_unittest").debug('Creating spatialite %s %s ...', work, variante)
                    slfile = os.path.join(self.testcdir, 'sl_' + work + '_' + variante, 'test01.sqlite')
                    #slfile = os.path.join(os.path.dirname(__file__), 'lamia_test','test01.sqlite')
                    #os.mkdir(os.path.dirname(slfile))
                    sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
                    sqlitedbase.loadDBase(slfile=slfile)
                    exporterreport = ReportCore(sqlitedbase,
                                                messageinstance=self.connector)
                    if True:
                        self.makeTests('spatialite',work, variante, exporterreport)
                    else:
                        basename = 'Infralineaire_PT_PL'
                        destfile = os.path.join(self.reportdir,'spatialite' + '_' + work + '_' + variante + '_' + basename  + '.pdf')
                        exporterreport.runReport(destinationfile=destfile,
                                                reportconffilename=basename,
                                                pkzonegeos=[2])
                    sqlitedbase.disconnect()

                if POSTGIS:
                    logging.getLogger("Lamia_unittest").debug('Creating postgis %s %s ...', work, variante)
                    pgdir = os.path.join(self.testcdir, 'pg_' + work + '_' + variante)
                    #os.mkdir(pgdir)
                    pgdbase = DBaseParserFactory('postgis').getDbaseParser()
                    pgdbase.loadDBase(host=PGhost, port=PGport, dbname=PGbase, schema= work + '_' + variante, user=PGuser,  password=PGpassword)
                    exporterreport = ReportCore(pgdbase,
                                            messageinstance=self.connector)
                    if True:
                        self.makeTests('postgis',work, variante, exporterreport)
                    else:
                        basename = 'Infralineaire'
                        destfile = os.path.join(self.reportdir,'postgis' + '_' + work + '_' + variante + '_' + basename  + '.pdf')
                        exporterreport.runReport(destinationfile=destfile,
                                                reportconffilename=basename,
                                                pkzonegeos=[])
                    pgdbase.disconnect()

    
        logging.getLogger("Lamia_unittest").debug('test_c_DbaseCreate OK')
        self._exitQGis()
    """

    def makeTests(self, dbtype, work, variante, dbase):

        exporterreport = ReportCore(dbase, messageinstance=self.connector)

        conftotest = []

        for filename in glob.glob(
            os.path.join(exporterreport.confdatadirplugin, "*.txt")
        ):
            basename = os.path.basename(filename).split(".")[0]
            if basename == "README":
                continue
            conftotest.append(basename)

        # conftotest = ['Infralineaire_PT_PL']        #uncomment to test only one conf
        for confname in conftotest:
            logging.getLogger("Lamia_unittest").debug(
                "********************** %s %s, %s - exporting conf : %s ...",
                dbtype,
                work,
                variante,
                confname,
            )
            destfile = os.path.join(
                self.reportdir,
                dbtype + "_" + work + "_" + variante + "_" + confname + ".pdf",
            )
            exporterreport.runReport(
                destinationfile=destfile, reportconffilename=confname, pkzonegeos=[]
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
    """
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    unittest.main()
    """

