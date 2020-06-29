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
import Lamia.libs.pyqtgraph


from pprint import pprint
import qgis, qgis.core, qgis.gui
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import QWidget, QDialog, QMainWindow

import warnings, os

# warnings.simplefilter("ignore")
# os.environ["PYTHONWARNINGS"] = "ignore" # Also affect subprocesses
warnings.filterwarnings("default", category=DeprecationWarning, module="networkx")

from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
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
                        self.mainwin, self.canvas, self.lamiawidget = getDisplayWidget()
                        # self._createWin()
                        # self._createMainWin()
                        slfile = os.path.join(
                            testcdir, "sl_" + work + "_" + variante, "test01.sqlite"
                        )
                        self.lamiawidget.loadDBase(dbtype="Spatialite", slfile=slfile)
                        self.launchTest()
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

    def launchTest(self):
        if TEST_WITH_FEATURE_CREATION:
            self.featurecreation()
        if SHOWIFACE:
            self.showIFace()

    def showIFace(self):
        self.lamiawidget.setVisualMode(visualmode=4)
        if (
            self.lamiawidget.qgiscanvas.layers["Infralineaire"]["layer"].featureCount()
            > 0
        ):
            extent = (
                self.lamiawidget.qgiscanvas.layers["Infralineaire"]["layer"]
                .extent()
                .buffered(10.0)
            )
        else:
            extent = qgis.core.QgsRectangle(
                X_BEGIN, Y_BEGIN, X_BEGIN + 10, Y_BEGIN + 10
            )
        # logging.getLogger("Lamia_unittest").debug('Extent : %s', extent)
        self.lamiawidget.qgiscanvas.canvas.setExtent(extent)
        # display good widget
        # wdg = self.lamiawidget.toolwidgets['toolprepro']['Graphique_csv'][0]
        # wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)
        # wdg = self.lamiawidget.toolwidgets['toolpostpro']['Import'][0]
        # wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)
        # self.lamiawidget.dbase.printsql = True
        wdg = self.lamiawidget.toolwidgets["toolprepro"]["Troncon"][0]
        wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)

        # res = self.lamiawidget.connector.inputMessage(['nom','mdp'])
        # print(res)

        self.mainwin.exec_()

    def featurecreation(self):
        # toolpreprolist = self.lamiawidget.toolwidgets["toolprepro"]
        global i
        i = 0
        # for toolpreproname, toolpreprovalue in self.lamiawidget.toolwidgets['toolprepro'].items():
        for toolname, toolinstance in self.lamiawidget.toolwidgets.items():
            if hasattr(toolinstance, "PREPROTOOLNAME"):
                self.recursive_creation(toolinstance)

    def recursive_creation(self, tt):
        global i
        i += 1
        name = [tt.tooltreewidgetSUBCAT]

        parentwdg = tt
        while parentwdg.parentWidget is not None:
            name.append(parentwdg.parentWidget.tooltreewidgetSUBCAT)
            parentwdg = parentwdg.parentWidget
        try:
            name = "/".join(name[::-1])
        except TypeError as e:
            print(e, name)
            assert TypeError
        # logging.getLogger("Lamia_unittest").debug('******* Testing %s', name)
        # self.lamiawidget.MaintreeWidget.setCurrentItem(tt.qtreewidgetitem)
        tt.widgetClicked()
        if len(tt.choosertreewidget.ids) == 0:
            self.lamiawidget.toolbarNew()
            dbasetable = self.lamiawidget.dbase.dbasetables[tt.DBASETABLENAME]
            # logging.getLogger("Lamia_unittest").debug('fieldgeom : %s , tempgeom : %s',
            #                                            'geom' in dbasetable.keys(),
            #                                            tt.tempgeometry)
            if "geom" in dbasetable.keys() and tt.tempgeometry is None:
                typegeom = dbasetable["geom"]
                """
                X_BEGIN = 100000.0
                Y_BEGIN = 6000000.0
                """
                if tt.DBASETABLENAME != "Zonegeo":
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
            self.lamiawidget.toolbarSave()
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
                self.recursive_creation(childwdg)


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
