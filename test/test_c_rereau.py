# import unittest, os, logging, sys, shutil, logging, time, glob

# sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..")))
# import warnings
# import pandas as pd
# import numpy as np
# # TODO JB ICI
# with warnings.catch_warnings():
#     warnings.filterwarnings("ignore", category=DeprecationWarning)


# import qgis, qgis.core
# from qgis.PyQt.QtWidgets import QApplication

# from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
# # from Lamia.api.libslamia.lamiaITVimport.lamiaITVimport.ITVImportCore import computeOneIndicator
# from Lamia.api.libslamia.lamiaITVimport.lamiaITVimport import ITVImportCore
# from Lamia.api.libslamia.lamiaITVimport.exfiltration_indicators import all_exfiltration_indicators
# from Lamia.qgisiface.iface.qgsconnector.ifaceqgisconnector import QgisConnector
# from test_utils import *
# from settings import *

# # tester computeOneIndicator
# class TestStringMethods(unittest.TestCase):

#     def setUp(self):
#         """Initialisation des tests."""
#         # TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
#         self.connector = QgisConnector()
#         self.testcdir = os.path.join(TESTDIR, "c_rereau")
#         ITVImportCore
#         # self.itvtdir = os.path.join(TESTDIR, "itvimport")
#         # if not os.path.isdir(self.itvtdir):
#         #     os.mkdir(self.itvtdir)

#     def computeOneIndicator(self, result_df, indicator, alpha, P, dict_of_indictors):
#         pass

#     # un test pour vérifier ce qui s passe quand length = 0
#     def no_length_for_edge(self):
#         df = pd.DataFrame({'length': [0, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BCCA': [2, 5], 'BACA': [0, 0]})
#         indicator = 'EXF4'
#         alpha = 2
#         P = 5
#         result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
#         self.assertEqual(np.min(result_df['result_' + indicator]), np.max(result_df['result_' + indicator]))
#         self.assertEqual(np.max(result_df['result_' + indicator]), float(np.nan))
#         self.assertEqual(np.min(result_df['score_' + indicator]), np.max(result_df['score_' + indicator]))
#         self.assertEqual(np.max(result_df['score_' + indicator]), float(np.nan))
#         # tester si sans défaut, la note est bien 0 et le score 1

#     def no_defaut_in_EXF4(self):
#         df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BCCA': [2, 5], 'BACA': [0, 0]})
#         indicator = 'EXF4'
#         alpha = 2
#         P = 5
#         result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
#         self.assertEqual(np.min(result_df['result_' + indicator]), np.max(result_df['result_' + indicator]))
#         self.assertEqual(np.max(result_df['result_' + indicator]), 0)
#         self.assertEqual(np.min(result_df['score_' + indicator]), np.max(result_df['score_' + indicator]))
#         self.assertEqual(np.max(result_df['score_' + indicator]), 1)
#         # tester si sans défaut, la note est bien 0 et le score 1

#     def light_defaut_in_EXF4(self):
#         df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BACA': [1, 0]})
#         indicator = 'EXF4'
#         alpha = 2
#         P = 5
#         result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
#         self.assertNotEqual(result_df['result_' + indicator][0], 0)
#         self.assertEqual(result_df['score_' + indicator][0], 1)
#         # tester si peu de défaut, la note n'est pas 0 et le score 1

#     def medium_defaut_in_EXF4(self):
#         df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BACA': [3, 0]})
#         indicator = 'EXF4'
#         alpha = 2
#         P = 5
#         result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
#         self.assertEqual(result_df['result_' + indicator][0], 0.6)
#         self.assertEqual(result_df['score_' + indicator][0], 2)
#         # tester si quelques défaut, la note n'est pas 0 et le score 2

#     def heavy_defaut_in_EXF4(self):
#         df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BACA': [11, 0]})
#         indicator = 'EXF4'
#         alpha = 2
#         P = 5
#         result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
#         self.assertEqual(result_df['result_' + indicator][0], 2.2)
#         self.assertEqual(result_df['score_' + indicator][0], 3)
#         # tester si beaucoup de défaut, la note n'est pas 0 et le score 3

#     def max_defaut_in_EXF4(self):
#         df = pd.DataFrame({'length': [100, 200], 'k_reg_1': ['1', '2'], 'k_reg_2': ['2', '3'], 'BACA': [100, 0]})
#         indicator = 'EXF4'
#         alpha = 2
#         P = 5
#         result_df = computeOneIndicator(df, indicator, alpha, P, all_exfiltration_indicators)
#         self.assertEqual(result_df['result_' + indicator][0], 20)
#         self.assertEqual(result_df['score_' + indicator][0], 4)
#         # tester si enormement de défaut, la note n'est pas 0 et le score 4

# # class DBaseTest(unittest.TestCase):

# #     """Test case utilisé pour tester les fonctions du module 'random'."""

# #     def setUp(self):
# #         """Initialisation des tests."""
# #         # TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
# #         self.connector = QgisConnector()
# #         self.testcdir = os.path.join(TESTDIR, "c_creation")
# #         # self.itvtdir = os.path.join(TESTDIR, "itvimport")
# #         # if not os.path.isdir(self.itvtdir):
# #         #     os.mkdir(self.itvtdir)

# #     def test_a_generateITV(self):
# #         sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
# #         # slfile = os.path.join(
# #         #     self.testcdir, "sl_base3_urbandrainage_Lamia", "test01.sqlite"
# #         # )
# #         slfile = r"C:\01_WORKINGDIR\aaaa\test.sqlite"
# #         sqlitedbase.loadDBase(slfile=slfile)

# #         itvcore = ITVImportCore(sqlitedbase, messageinstance=self.connector)

# #         datafiles = os.path.join(
# #             os.path.dirname(__file__), "datas", "itvimport", "VU-5024-0418.txt"
# #         )

# #         logging.getLogger("Lamia_itvcore").debug("STARTING")

# #         # resdataframe = itvcore.readITVs(datafiles)

# #         # logging.getLogger("Lamia_itvcore").debug(
# #         #     "res %s", str(resdataframe.values.tolist())
# #         # )

# #         # noidinlamia = itvcore.checkNodesExistInLamia(datafiles)
# #         # logging.getLogger("Lamia_itvcore").debug(
# #         #     "res %s", str(noidinlamia)
# #         # )

# #         # itvcore.getUniquesValuesbyEdge(datafiles)

# #         itvcore.computeNotation("rereau_base", [1])


# def main():
#     app = initQGis()
#     logging.basicConfig(
#         format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
#         datefmt="%H:%M:%S",
#     )
#     logging.getLogger("Lamia_itvcore").setLevel(logging.DEBUG)
#     unittest.main()
#     exitQGis()


# if __name__ == "__main__":
#     main()

