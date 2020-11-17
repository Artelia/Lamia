import unittest, os, logging, sys, platform

sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), ".."))
"""
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
"""
import networkx
import Lamia.api.libs.pyqtgraph


from pprint import pprint
import qgis, qgis.core, qgis.gui
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import QWidget, QDialog, QMainWindow

import warnings, os

# warnings.simplefilter("ignore")
# os.environ["PYTHONWARNINGS"] = "ignore" # Also affect subprocesses
warnings.filterwarnings("default", category=DeprecationWarning, module="networkx")

from Lamia.qgisiface.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
from test_utils import *
from settings import *


X_BEGIN = 400000.0
Y_BEGIN = 6000000.0
TEST_WITH_FEATURE_CREATION = True
SHOWIFACE = False


class DBaseTest(unittest.TestCase):
    def setUp(self):
        """Initialisation des tests."""
        # TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')

    def test_a_testSaveFeature(self):
        testcdir = os.path.join(TESTDIR, "c_creation")

        self.mainwin, self.canvas, self.lamiawidget = getDisplayWidget()

        if "SLFILE" in globals().keys():
            self.lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)
            self.launchTest()
        elif "PGschema" in globals().keys():
            self.lamiawidget.loadDBase(
                dbtype="Postgis",
                host=PGhost,
                port=PGport,
                dbname=PGbase,
                schema=PGschema,
                user=PGuser,
                password=PGpassword,
            )
            self.launchTest()
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
                    # self._createWin()
                    # self._createMainWin()

                    if SPATIALITE:
                        mainwin, canvas, lamiawidget = getDisplayWidget()
                        slfile = os.path.join(
                            testcdir, "sl_" + work + "_" + variante, "test01.sqlite"
                        )
                        lamiawidget.loadDBase(dbtype="Spatialite", slfile=slfile)
                        self.launchTest(lamiawidget, mainwin)
                    if POSTGIS:
                        self.mainwin, self.canvas, self.lamiawidget = getDisplayWidget()
                        # self._createWin()
                        # self._createMainWin()
                        PGschema = work + "_" + variante
                        self.lamiawidget.loadDBase(
                            dbtype="Postgis",
                            host=PGhost,
                            port=PGport,
                            dbname=PGbase,
                            schema=PGschema,
                            user=PGuser,
                            password=PGpassword,
                        )
                        self.launchTest()

    def launchTest(self, lamiawidget, mainwin):
        if TEST_WITH_FEATURE_CREATION:
            self.featurecreation(lamiawidget)
        if SHOWIFACE:
            self.showIFace(lamiawidget, mainwin)

    def showIFace(self, lamiawidget, mainwin):
        lamiawidget.setVisualMode(visualmode=1)
        if lamiawidget.qgiscanvas.layers["edge"]["layer"].featureCount() > 0:
            extent = (
                lamiawidget.qgiscanvas.layers["edge"]["layer"].extent().buffered(10.0)
            )
        else:
            extent = qgis.core.QgsRectangle(
                X_BEGIN, Y_BEGIN, X_BEGIN + 10, Y_BEGIN + 10
            )

        lamiawidget.qgiscanvas.canvas.setExtent(extent)
        mainwin.exec_()

    def featurecreation(self, lamiawidget):
        global i
        i = 0
        for toolname, toolinstance in lamiawidget.toolwidgets.items():
            if hasattr(toolinstance, "PREPROTOOLNAME"):
                self.recursive_creation(toolinstance, lamiawidget)

    def recursive_creation(self, tt, lamiawidget):
        global i
        i += 1
        name = [tt.tooltreewidgetSUBCAT]

        lamiawidget.dbase.printsql = False
        lamiawidget.dbase.raiseexceptions = True

        parentwdg = tt
        while parentwdg.parentWidget is not None:
            name.append(parentwdg.parentWidget.tooltreewidgetSUBCAT)
            parentwdg = parentwdg.parentWidget
        try:
            name = "/".join(name[::-1])
        except TypeError as e:
            print(e, name)
            assert TypeError

        tt.widgetClicked()
        if len(tt.choosertreewidget.ids) == 0:

            dbasetable = lamiawidget.dbase.dbasetables[tt.DBASETABLENAME]
            if "geom" in dbasetable.keys():
                typegeom = dbasetable["geom"]
            else:
                typegeom = None

            logging.getLogger("Lamia_unittest").debug(
                str(name) + " - typegeom : " + str(typegeom)
            )

            lamiawidget.toolbarNew()

            if typegeom and tt.tempgeometry is None:
                """
                X_BEGIN = 100000.0
                Y_BEGIN = 6000000.0
                """
                if tt.DBASETABLENAME != "geoarea":
                    if "POINT" in typegeom:
                        tt.setTempGeometry(
                            [qgis.core.QgsPointXY(X_BEGIN + i, Y_BEGIN + 0)]
                        )
                    elif "LINESTRING" in typegeom:
                        tt.setTempGeometry(
                            [
                                qgis.core.QgsPointXY(X_BEGIN + i, Y_BEGIN + 0),
                                qgis.core.QgsPointXY(X_BEGIN + i, Y_BEGIN + 1),
                            ]
                        )
                    else:
                        tt.setTempGeometry(
                            [
                                qgis.core.QgsPointXY(X_BEGIN + i, Y_BEGIN + 0),
                                qgis.core.QgsPointXY(X_BEGIN + i, Y_BEGIN + 1),
                                qgis.core.QgsPointXY(X_BEGIN + i - 0.5, Y_BEGIN + 1),
                                qgis.core.QgsPointXY(X_BEGIN + i - 0.5, Y_BEGIN + 0),
                            ]
                        )
                else:
                    tt.setTempGeometry(
                        [
                            qgis.core.QgsPointXY(X_BEGIN - 1, Y_BEGIN - 1),
                            qgis.core.QgsPointXY(X_BEGIN + 50, Y_BEGIN - 1),
                            qgis.core.QgsPointXY(X_BEGIN + 50, Y_BEGIN + 50),
                            qgis.core.QgsPointXY(X_BEGIN - 1, Y_BEGIN + 50),
                        ]
                    )

            lamiawidget.toolbarSave()
            # logging.getLogger("Lamia_unittest").debug('%s - pk created : %s', tt.DBASETABLENAME,tt.currentFeaturePK)
            self.assertIsNotNone(tt.currentFeaturePK)
        else:
            pk = tt.choosertreewidget.ids["pk"].values[0]
            tt.selectFeature(pk=pk)
            self.assertIsNotNone(pk)
            # logging.getLogger("Lamia_unittest").debug('%s - pk selected : %s', tt.DBASETABLENAME, pk)
        for childwdg in tt.dbasechildwdgfield:
            if childwdg.tooltreewidgetSUBCAT is None:
                logging.getLogger("Lamia_unittest").debug(
                    "not testing %s child of %s because tooltreewidgetSUBCAT is None",
                    childwdg.__class__.__name__,
                    tt.tooltreewidgetSUBCAT,
                )
                raise Exception("This is broken")
            else:
                self.recursive_creation(childwdg, lamiawidget)


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
