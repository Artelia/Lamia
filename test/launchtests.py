import sys
import unittest, logging
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)

# uncomment for activating tests
from settings import *
import test_a_dbase_simple
import test_b_qgisqt
import test_c_exporttool
import test_c_reporttool
import test_c_costtool

def suite():
    suite = unittest.TestSuite()

    #* test_a_dbase_simple
    if 'test_a_dbase_simple' in globals().keys():
        suite.addTest(test_a_dbase_simple.DBaseTest('test_a_DbaseInit'))
        suite.addTest(test_a_dbase_simple.DBaseTest('test_b_DbaseReader'))
        suite.addTest(test_a_dbase_simple.DBaseTest('test_c_DbaseCreate'))

    #* test_b_qgisqt
    if 'test_b_qgisqt' in globals().keys():
        suite.addTest(test_b_qgisqt.DBaseTest('test_a_testSaveFeature'))

    #* test_c_exporttool
    if 'test_c_exporttool' in globals().keys():
        suite.addTest(test_c_exporttool.DBaseTest('test_a_generateShapefile'))

    #* test_c_reporttool
    if 'test_c_reporttool' in globals().keys():
        suite.addTest(test_c_reporttool.DBaseTest('test_a_generateReport'))

    #* test_c_costtool
    if 'test_c_costtool' in globals().keys():
        suite.addTest(test_c_costtool.DBaseTest('test_a_generateCost'))

    return suite

if __name__ == '__main__':
    app = initQGis()
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s',
                        datefmt="%H:%M:%S")
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    #unittest.TextTestRunner().run(suite)
    runner = unittest.TextTestRunner()
    runner.run(suite())
    exitQGis()

