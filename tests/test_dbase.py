import unittest, os, logging, sys
from Lamia.main.DBaseParser import DBaseParser

logger = logging.getLogger("LamiaTest")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""
        self.dbase = DBaseParser()
        createdir = os.path.join(os.path.dirname(__file__), '..', 'Lamia','DBASE', 'create')
        self.dictfiles = [os.path.join(createdir, 'Base2_0_6.xlsx'),
                         os.path.join(createdir, 'Base2_assanissement_0_6.xlsx'),
                         os.path.join(createdir,'Base2_chantier_0_1.xlsx'),
                         os.path.join(createdir, 'Base2_digue_0_4.xlsx'),
                         os.path.join(createdir, 'Base2_eaupotable_0_4.xlsx'),
                         os.path.join(createdir, 'Base2_tramway_0_3.xlsx'),
                         ]

    def test_DbaseInit(self):
        self.assertIsInstance(self.dbase, DBaseParser)
        logging.getLogger("LamiaTest").debug('ok')

    def test_readDbDictionnary(self):

        for dictfile in self.dictfiles:
            self.dbase.readDbDictionnary(dictfile)
            logging.getLogger("LamiaTest").debug('started %s', str(self.dbase.dbasetables))
            self.assertTrue(len(self.dbase.dbasetables.keys()) > 0)

            for tablename in self.dbase.dbasetables.keys():
                tabledict = self.dbase.dbasetables[tablename]
                self.assertTrue('order' in tabledict.keys())
                self.assertTrue('fields' in tabledict.keys())
                for fieldname in tabledict['fields'].keys():
                    fielddict = tabledict['fields'][fieldname]
                    self.assertTrue('PGtype' in fielddict.keys())
                    self.assertIsNotNone(fielddict['PGtype' ])

        logging.getLogger("LamiaTest").debug('ok')



