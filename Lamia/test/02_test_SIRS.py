# -*- coding: utf-8 -*-





from Lamia.Lamia.test.AbstractTest import Test
import os
import datetime

from Lamia.Lamia.toolgeneral.SIRS_to_LAMIA.FDtL import *
from Lamia.Lamia.toolgeneral.LAMIA_to_SIRS.LtFD import *

class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        self.dbase.createDbase(slfile=spatialitefile, crs=2154, worktype='Base2_digue')

        FDtL = FranceDiguetoLamia(user, pwd, ip, port, nom_sirs, path_LAMIA, user_LAMIA, password_LAMIA, adresse_LAMIA,port_LAMIA, nom_LAMIA, srid, type_spatialite, type_postgis)
        FDtL.insertInLamia()


test = TestMain()
test.launchTest()

