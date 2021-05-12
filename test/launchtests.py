import sys
import unittest, logging
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

# comment for desactivating tests
from settings import *
from test_utils import *

import test_a_dbase_simple

# import test_a_autoupdatedbase
import test_b_qgisqt

# import test_b_qtimporttool
import test_b_qtofflinemode
import test_c_exporttool

import test_c_reporttool

import test_c_costtool

# import test_c_rereau


def suite():
    suite = unittest.TestSuite()

    # * test_a_dbase_simple
    if "test_a_dbase_simple" in globals().keys():
        suite.addTest(test_a_dbase_simple.DBaseTest("test_a_DbaseInit"))
        suite.addTest(test_a_dbase_simple.DBaseTest("test_b_DbaseReader"))
        suite.addTest(test_a_dbase_simple.DBaseTest("test_c_DbaseCreate"))

        # * test_a_autoupdatedbase
    if "test_a_autoupdatedbase" in globals().keys():
        suite.addTest(test_a_autoupdatedbase.DBaseTest("test_a_updatedbase"))

    # * test_b_qgisqt
    if "test_b_qgisqt" in globals().keys():
        suite.addTest(test_b_qgisqt.DBaseTest("test_a_testSaveFeature"))

    # * test_b_qtimporttool
    if "test_b_qtimporttool" in globals().keys():
        suite.addTest(test_b_qtimporttool.DBaseTest("test_a_generateImport"))

    # * test_b_qtofflinemode
    if "test_b_qtofflinemode" in globals().keys():
        suite.addTest(test_b_qtofflinemode.DBaseTest("test_a_testoffline"))

    # * test_c_exporttool
    if "test_c_exporttool" in globals().keys():
        suite.addTest(test_c_exporttool.DBaseTest("test_a_generateShapefile"))

    # * test_c_reporttool
    if "test_c_reporttool" in globals().keys():
        suite.addTest(test_c_reporttool.DBaseTest("test_a_generateReport"))

    # * test_c_costtool
    if "test_c_costtool" in globals().keys():
        suite.addTest(test_c_costtool.DBaseTest("test_a_generateCost"))

    return suite


if __name__ == "__main__":
    app = initQGis()
    logging.basicConfig(
        format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)
    # unittest.TextTestRunner().run(suite)
    runner = unittest.TextTestRunner()
    runner.run(suite())
    exitQGis()
