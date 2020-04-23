# -*- coding: utf-8 -*-




from Lamia.test.AbstractTest import Test
import os
import datetime
import shutil


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()
        # spatialite postgis
        typedb = 'spatialite'


        # export  importnouvelle
        testcherche = 'importterrain'

        if typedb == "spatialite":
            pathexport = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test01', '01_original',
                                      'test01.sqlite')
            pathexport = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//BD_totale_ind6.sqlite"


            #pathimportterrain = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test01','03_fusion_modif_terrain', 'test01.sqlite')

            pathimportterrain = "C://BM//pourimport//BD_totale_ind8.sqlite"




            if testcherche == 'export':
                self.wind.dbase.loadQgisVectorLayers(pathexport)

            elif testcherche == 'importterrain':
                pass
                if False:
                    # pathmodif = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test01', '02_modif','test01.sqlite')
                    pathmodif = "C://BM//original//BD_totale_ind8.sqlite"
                    pathimportterrain = "C://BM//pourimport//BD_totale_ind8.sqlite"

                    dirtodelete = os.path.dirname(pathimportterrain)
                    shutil.rmtree(dirtodelete, ignore_errors=True)
                    shutil.copytree(os.path.dirname(pathmodif), dirtodelete)

                self.wind.dbase.loadQgisVectorLayers(pathimportterrain)

            elif testcherche == 'importnouvelle':
                spatialitefile = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test02', 'to',
                                              'BD_totale.sqlite')
                spatialitefile = "M://FR//BOR//VT//URBAIN//4352329-33-GPMB-diag complet EU et EP-Bacalan, Le Verdon, Pauillac et Blaye//05-ETUDES//05-1-Dessins-plans//6-lamia//temp//temp2//gpmb_ind0.sqlite"

                # self.dbase.printsql = True

                self.wind.dbase.createDbase(slfile=spatialitefile, crs=3945, worktype='Base2_assainissement')

            elif testcherche == 'exporttotal':
                pathimportterrain = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test03', 'from',
                                                 'BD_totale.sqlite')

                self.wind.dbase.loadQgisVectorLayers(pathimportterrain)

        elif typedb == "postgis":
            self.wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm',
                                            user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)


        self.wind.dbase.printsql = False


        if testcherche == 'export':
            pathtoexport = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test01', '02_terrain','test01_terrain.sqlite')
            pathtoexport = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//20190321_exportterrain//export01.sqlite"
            self.wind.dbase.exportDbase(pathtoexport)
            if False:
                pathmodif = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test01', '02_modif','test01_modif.sqlite')
                dirtodelete = os.path.dirname(pathmodif)
                shutil.rmtree(dirtodelete, ignore_errors=True)
                shutil.copytree(os.path.dirname(pathexport), dirtodelete)
            print('finisehd')

        elif testcherche == 'exporttotal':
            pathtoexport = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test03', 'to',
                                        'test01_terrain.sqlite')
            self.wind.dbase.exportDbase(pathtoexport)
            print('finisehd')

        elif testcherche == 'importterrain':

            # pathterrain = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test01', '02_terrain', 'test01_terrain.sqlite')

            # pathterrain = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees_terrains//201903252627_Terrain_JRS//export_BD_BM_mars2019.sqlite"
            #pathterrain = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees_terrains//201903252627_Terrain_SPS//export_BD_BM_mars2019.sqlite"
            #pathterrain = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees_terrains//20190325_Terrain_HDA//export_BD_BM_mars2019.sqlite"

            pathterrain = "C://BM//Terrain _SPS//20191120//Test_FJE.sqlite"
            # ##pathterrain = "C://BM//Terrain_JRS//20191120//Test_FJE.sqlite"
            pathterrain = "C://BM//Terrain _SPS//20191107//Terrain_VTA_11_2019_FJE.sqlite"
            pathterrain = "C://BM//Terrain_JRS//20191107//Terrain_VTA_11_2019_JDE.sqlite"
            pathterrain = "C://BM//Rive_Droite//Test_JDE.sqlite"



            # UPDATE OBJET SET lpk_revision_begin = 2 WHERE datetimecreation > '2019-11-05 00:00:00' AND datetimecreation != 'None'
            # UPDATE TcObjetRessource SET lpk_revision_begin = 2


            self.wind.importDBase(slfile=pathterrain, typeimport='import_terrain')

        elif testcherche == 'importnouvelle':
            if True:

                path1 = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test02', 'from',
                                     'BD_SIJALAG_ind15.sqlite')
                path1 = "M://FR//BOR//VT//FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//61_Calculs//Lamia//vvvvv.sqlite"
                path1 = "M://FR//BOR//VT//URBAIN//4352329-33-GPMB-diag complet EU et EP-Bacalan, Le Verdon, Pauillac et Blaye//05-ETUDES//05-1-Dessins-plans//6-lamia//temp//gpmb_ind0.sqlite"

                self.wind.importDBase(slfile=path1)


            if False:
                if True:
                    path1 = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test02', 'from','BD_Begles_ind17.sqlite')
                    self.wind.importDBase(slfile=path1)
                if True:
                    path1 = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test02', 'from', 'BD_Rivedroite_ind6.sqlite')
                    self.wind.importDBase(slfile=path1)

        print("Finished")



test = TestMain()
test.launchTest()

