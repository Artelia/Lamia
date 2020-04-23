# -*- coding: utf-8 -*-

from test.AbstractTest import Test
import os
import datetime


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()
        crs = 3945
        # Digue VNF  Assainissement  Default Assainissement2 Base Base_default Base_assainissement Base2_digue Base2_parking
        # Base2_tramway Base2_eaupotable Base2_assainissement Base2_eclairagepublic Base2_chantier
        typebase = 'Base2_assainissement'
        # CD41 Lamia Reseau_chaleur Orange
        variante = 'Lamia'
        # spatialite   postgis

        typedb = 'spatialite'

        if typedb == "spatialite":
            if typebase == 'VNF':
                spatialitefile = 'C://000_testdigue//temp_VNF//test01.sqlite'
            elif typebase == 'Digue':
                spatialitefile = 'C://000_testdigue//temp_digue//test01.sqlite'
            elif typebase == 'Assainissement':
                spatialitefile = 'C://000_testdigue//temp_ass//test01.sqlite'
            elif typebase == 'Assainissement2':
                spatialitefile = 'C://000_testdigue//temp_ass2//test01.sqlite'
            elif typebase == 'Default':
                spatialitefile = 'C://000_testdigue//temp_default//test01.sqlite'
            elif typebase == 'Base':
                spatialitefile = 'C://000_testdigue//temp_base//test01.sqlite'
            elif typebase == 'Base_default':
                spatialitefile = 'C://000_testdigue//temp_basedefault//test01.sqlite'
            elif typebase == 'Base_assainissement':
                spatialitefile = 'C://000_testdigue//temp_baseassainissement//test01.sqlite'
            elif typebase == 'Base2':
                spatialitefile = 'C://000_testdigue//temp_base2//test01.sqlite'
            elif typebase == 'Base2_digue':
                spatialitefile = 'C://000_testdigue//temp_base2_digue//test01.sqlite'
            elif typebase == 'Base2_parking':
                spatialitefile = 'C://000_testdigue//temp_base2_parking//test01.sqlite'
            elif typebase == 'Base2_assainissement':
                spatialitefile = "C://000_testdigue//temp_base2_ass2//test01.sqlite"
            elif typebase == 'Base2_tramway':
                spatialitefile = "C://000_testdigue//temp_base2_tram2//test01.sqlite"
            elif typebase == 'Base2_eaupotable':
                spatialitefile = "C://000_testdigue//temp_base2_aep//test01.sqlite"
            elif typebase == 'Base2_eclairagepublic':
                spatialitefile = "C://000_testdigue//temp_base2_eclairagepublic//test01.sqlite"
            elif typebase == 'Base2_chantier':
                spatialitefile = "C://000_testdigue//temp_base2_chantiertram//test01.sqlite"


            self.dbase.printsql = True
            #self.dbase.xlsreader = True

            dbaseressourcesdirectory = os.path.join(os.path.dirname(spatialitefile),'DBspatialite')

            self.dbase.createDbase(slfile=spatialitefile, crs=crs, worktype=typebase, variante=variante)




        elif typedb == "postgis":
            if typebase == 'Default':
                self.dbase.printsql = True
                self.dbase.createDbase(crs=crs, type=typebase, dbasetype='postgis', dbname='PVR_test',
                                       schema='lamia_default',
                                       user='pvr', host='localhost',
                                       password='pvr',
                                       dbaseressourcesdirectory='C://000_Docker_rep//bdpostgres')
            if typebase == 'Digue':
                self.dbase.printsql = True
                self.dbase.createDbase(crs=crs, type=typebase, dbasetype='postgis', dbname='PVR_test',
                                       schema='lamia_digue',
                                       user='postgres', host='localhost',
                                       password='PVR',
                                       dbaseressourcesdirectory='c://000_testdigue//temp_postgis//digue')

            if typebase == 'Base2_digue':
                self.dbase.printsql = True
                self.dbase.createDbase(crs=crs, worktype=typebase, dbasetype='postgis', dbname='PVR_test',
                                       schema='digue3',
                                       user='postgres', host='localhost',
                                       password='PVR',
                                       dbaseressourcesdirectory='c://000_testdigue//temp_postgis//digue')


            if typebase == 'Base2_assainissement':
                print('***********************okok')
                self.dbase.printsql = True
                self.dbase.createDbase(crs=crs, worktype=typebase, dbasetype='postgis', dbname='gis',
                                       schema='assainissement',
                                       user='pvr', host='localhost', port=5432,
                                       password='pvr',
                                       dbaseressourcesdirectory='C://000_Docker_rep//bdpostgres//assainissement')

        print('fin')


test = TestMain()
test.launchTest()
