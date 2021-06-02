import unittest, os, logging, sys, shutil, logging, time, glob

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..")))
import warnings
import pandas as pd
import numpy as np
# TODO JB ICI
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

import Lamia
import qgis, qgis.core
from qgis.PyQt.QtWidgets import QApplication

from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
# from Lamia.api.libslamia.lamiaITVimport.lamiaITVimport.ITVImportCore import computeOneIndicator
from Lamia.api.libslamia.lamiaITVimport.lamiaITVimport import computeOneIndicator
from Lamia.api.libslamia.lamiaITVimport.exfiltration_indicators import all_exfiltration_indicators
from Lamia.qgisiface.iface.qgsconnector.ifaceqgisconnector import QgisConnector
from test_utils import *
from settings import *

# tester computeOneIndicator
class TestRereau(unittest.TestCase):

    # un test pour vérifier ce qui s passe quand length = 0
    def test_no_length_for_edge(self):
        df = pd.DataFrame({'length': [0, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BCCA': [2, 5], 'BACA': [0, 0]})
        indicator = 'EXF4'
        alpha = 2
        P = 5
        result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
        self.assertEqual(result_df['result_' + indicator][1], 0)
        self.assertTrue(np.isnan(result_df['result_' + indicator][0]))
        self.assertEqual(result_df['score_' + indicator][1], 1)
        self.assertTrue(np.isnan(result_df['score_' + indicator][0]))
        # tester si sans défaut, la note est bien 0 et le score 1

    def test_no_defaut_in_EXF4(self):
        df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BCCA': [2, 5], 'BACA': [0, 0]})
        indicator = 'EXF4'
        alpha = 2
        P = 5
        result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
        self.assertEqual(np.min(result_df['result_' + indicator]), np.max(result_df['result_' + indicator]))
        self.assertEqual(np.max(result_df['result_' + indicator]), 0)
        self.assertEqual(np.min(result_df['score_' + indicator]), np.max(result_df['score_' + indicator]))
        self.assertEqual(np.max(result_df['score_' + indicator]), 1)
        # tester si sans défaut, la note est bien 0 et le score 1

    def test_light_defaut_in_EXF4(self):
        df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BACA': [1, 0]})
        indicator = 'EXF4'
        alpha = 2
        P = 5
        result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
        self.assertNotEqual(result_df['result_' + indicator][0], 0)
        self.assertEqual(result_df['score_' + indicator][0], 1)
        # tester si peu de défaut, la note n'est pas 0 et le score 1

    def test_medium_defaut_in_EXF4(self):
        df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BACA': [3, 0]})
        indicator = 'EXF4'
        alpha = 2
        P = 5
        result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
        self.assertEqual(result_df['result_' + indicator][0], 0.6)
        self.assertEqual(result_df['score_' + indicator][0], 2)
        # tester si quelques défaut, la note n'est pas 0 et le score 2

    def test_heavy_defaut_in_EXF4(self):
        df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BACA': [11, 0]})
        indicator = 'EXF4'
        alpha = 2
        P = 5
        result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
        self.assertEqual(result_df['result_' + indicator][0], 2.2)
        self.assertEqual(result_df['score_' + indicator][0], 3)
        # tester si beaucoup de défaut, la note n'est pas 0 et le score 3

    def test_max_defaut_in_EXF4(self):
        df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BACA': [100, 0]})
        indicator = 'EXF4'
        alpha = 2
        P = 5
        result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
        self.assertEqual(result_df['result_' + indicator][0], 20)
        self.assertEqual(result_df['score_' + indicator][0], 4)
        # tester si enormement de défaut, la note n'est pas 0 et le score 4

if __name__ == "__main__":
    unittest.main()
