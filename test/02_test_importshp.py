# -*- coding: utf-8 -*-





from Lamia.test.AbstractTest import Test
import os
import sys
import datetime
import qgis


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        path = "C://000_testdigue//temp_base2_ass2//test01.sqlite"

        self.wind.dbase.loadQgisVectorLayers(path)
        self.loadLayersInCanvas()
        self.createMainWin()

        if True:       # test of desktop version
            self.wind.loadUiDesktop()
            self.dbase.visualmode = 4

        self.dbase.printsql = False

        wdg = None
        for i, tool in enumerate(self.wind.tools):
            print(tool.__class__.__name__)
            if 'ImportTool' in tool.__class__.__name__:
                print('ok')
                wdg = self.wind.tools[i]
                break

        wdg.changePropertiesWidget()
        self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)



        if False:
            indexrapport = None
            for i, menutool in enumerate(self.wind.menutools):
                if 'importShapefile' in menutool.__class__.__name__ :
                    indexrapport = i
                    break


        # Infralineaire_BM Equipement_point_BM Photo_BM Graphdata_BM Desordres_ligne_BM
        layerpath = "M://FR//BOR//VT//URBAIN//4352329-33-GPMB-diag complet EU et EP-Bacalan, Le Verdon, Pauillac et Blaye//05-ETUDES//05-1-Dessins-plans//3-Autocad//Travail PLA//ART_TRAITEMENT_backup.shp"
        layer = qgis.core.QgsVectorLayer(layerpath, 'test', "ogr")
        wdg.currentlayer = layer


        if True:
            linkinfra = [[u'Infralineaire.pk_infralineaire', u''],
                         [u'Infralineaire.id_infralineaire', u''],
                         [u'Infralineaire.id_revisionbegin', u''],
                         [u'Infralineaire.id_revisionend', u''],
                         [u'Infralineaire.id_objet', u''],
                         [u'Infralineaire.id_descriptionsystem', u''],
                         [u'Infralineaire.lk_ressource1', u''],
                         [u'Infralineaire.lk_descriptionsystem1', u''],
                         [u'Infralineaire.lk_descriptionsystem2', u''],
                         [u'Infralineaire.materiau', u''],
                         [u'Infralineaire.diametreNominal', u''],
                         [u'Infralineaire.formecanalisation', u''],
                         [u'Infralineaire.hauteur', u''],
                         [u'Infralineaire.anPoseSup', u''], [u'Infralineaire.maitreOuvrage', u''],
                         [u'Infralineaire.exploitant', u''], [u'Infralineaire.enService', u''],
                         [u'Infralineaire.branchement', u''], [u'Infralineaire.modeCirculation', u''],
                         [u'Infralineaire.anPoseInf', u''], [u'Infralineaire.longueur', u''],

                         [u'Infralineaire.typeReseau', u'type2'],

                         [u'Infralineaire.contCanAss', u''], [u'Infralineaire.fonctionCannAss', u''],
                         [u'Infralineaire.altAmont', u''],
                         [u'Infralineaire.altAval', u''], [u'Infralineaire.profamont', u''],
                         [u'Infralineaire.profaval', u''], [u'Objet.pk_objet', u''], [u'Objet.id_objet', u''],
                         [u'Objet.id_revisionbegin', u''], [u'Objet.id_revisionend', u''], [u'Objet.datecreation', u''],
                         [u'Objet.datemodification', u''], [u'Objet.datedestruction', u''],
                         [u'Objet.commentaire', u''], [u'Objet.libelle', u''], [u'Objet.importid', u''],
                         [u'Objet.importtable', u''], [u'Descriptionsystem.pk_descriptionsystem', u''],
                         [u'Descriptionsystem.id_descriptionsystem', u''], [u'Descriptionsystem.id_revisionbegin', u''],
                         [u'Descriptionsystem.id_revisionend', u''],
                         [u'Descriptionsystem.id_objet', u''], [u'Descriptionsystem.importancestrat', u''],
                         [u'Descriptionsystem.etatfonct', u''],
                         [u'Descriptionsystem.qualitegeolocXY', u''], [u'Descriptionsystem.qualiteGeolocZ', u''],
                         [u'Descriptionsystem.dateGeoloc', u''],
                         [u'Descriptionsystem.sourceGeoloc', u''], [u'Descriptionsystem.parametres', u''],
                         [u'Descriptionsystem.listeparametres', u'']]

            linknoeud = [[u'Noeud.pk_noeud', u''], [u'Noeud.id_noeud', u''], [u'Noeud.id_revisionbegin', u''],
                         [u'Noeud.id_revisionend', u''], [u'Noeud.id_objet', u''], [u'Noeud.id_descriptionsystem', u''],
                         [u'Noeud.altradierouvrage', u''], [u'Noeud.alttamponouvrage', u''],
                         [u'Noeud.profradierouvrage', u''],

                         [u'Noeud.typeReseau', u''],

                         [u'Noeud.typeOuvrageAss', u''], [u'Noeud.accessibilite', u''],
                         [u'Noeud.cloisonsiphoide', u''], [u'Noeud.couvercle', u''], [u'Noeud.X', u''],
                         [u'Noeud.dX', u''], [u'Noeud.Y', u''],
                         [u'Noeud.dY', u''], [u'Noeud.Z', u''], [u'Noeud.dZ', u''], [u'Objet.pk_objet', u''],
                         [u'Objet.id_objet', u''],
                         [u'Objet.id_revisionbegin', u''], [u'Objet.id_revisionend', u''], [u'Objet.datecreation', u''],
                         [u'Objet.datemodification', u''],
                         [u'Objet.datedestruction', u''], [u'Objet.commentaire', u''], [u'Objet.libelle', u''],
                         [u'Objet.importid', u''],
                         [u'Objet.importtable', u''], [u'Descriptionsystem.pk_descriptionsystem', u''],
                         [u'Descriptionsystem.id_descriptionsystem', u''],
                         [u'Descriptionsystem.id_revisionbegin', u''], [u'Descriptionsystem.id_revisionend', u''],
                         [u'Descriptionsystem.id_objet', u''],
                         [u'Descriptionsystem.importancestrat', u''], [u'Descriptionsystem.etatfonct', u''],
                         [u'Descriptionsystem.qualitegeolocXY', u''], [u'Descriptionsystem.qualiteGeolocZ', u''],
                         [u'Descriptionsystem.dateGeoloc', u''],
                         [u'Descriptionsystem.sourceGeoloc', u''], [u'Descriptionsystem.parametres', u''],
                         [u'Descriptionsystem.listeparametres', u'']]

        # self.wind.dbase.dbasetables['Zonegeo']['layerqgis'].selectByIds([5])
        #wdg.importtable = 'Infralineaire'
        indextxt = wdg.userwdgfield.comboBox_typeimport.findText('Infralineaire')
        wdg.userwdgfield.comboBox_typeimport.setCurrentIndex(indextxt)
        wdg.showTable()

        #wdg.work(layer=layer, linktable=linkinfra)

        self.mainwin.exec_()





test = TestMain()
test.launchTest()
sys.exit()

