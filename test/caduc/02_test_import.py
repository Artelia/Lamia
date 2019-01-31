# -*- coding: utf-8 -*-

import os
import qgis
import qgis.gui
import shutil
from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget



def testVirtualLayer():

    if False:
        layers = qgis.core.QgsMapLayerRegistry.instance().mapLayers()

        for lay, mapl in layers.iteritems():
            print(mapl.name())



    if True:
        if True:
            sql = "SELECT Infralineaire.*,"
            sql += " Objet.datecreation, Objet.datedestruction, Objet.commentaire, Objet.libelle, "
            sql += "Descriptionsystem.importancestrat, Descriptionsystem.etatfonct, Descriptionsystem.datederniereobs, Descriptionsystem.qualitegeoloc, Descriptionsystem.parametres, Descriptionsystem.listeparametres"
            sql += " FROM Infralineaire INNER JOIN Descriptionsystem ON Infralineaire.id_descriptionsystem = Descriptionsystem.id_descriptionsystem "
            sql += "INNER JOIN Objet ON Objet.id_objet = Infralineaire.id_objet"
            print(sql)
        if False:
            sql = "SELECT * FROM Infralineaire"
        if False:
            sql = "SELECT * FROM Infralineaire INNER JOIN Objet ON Objet.id_objet = Infralineaire.id_objet"
        l1 = qgis.core.QgsVectorLayer("?query=" + sql +"&uid=id_infralineaire", "myvlayer", "virtual")
        #l1 = qgis.core.QgsVectorLayer("?query=" + sql + '?key="id_infralineaire"', "myvlayer", "virtual")

    if True:
        for fet in l1.getFeatures():
            print(fet.attributes())
            print(fet.id())
            #print(fet.geometry())

    if True:
        print([field.name() for field in l1.fields()])


def testRapport(canvas, loadfile=True, typedb="spatialite",reporttype=None, pdffile=None ):

    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    wind.setParent(None)

    if loadfile:
        if typedb == "spatialite":
            # path = os.path.normpath('C://Users//patrice.verchere//Documents//GitHub//InspectionDigue//DBASE//test1.sqlite')
            # path = os.path.normpath('c://000_testdigue//testdbase.sqlite')
            # path = os.path.normpath('C://000_testimportBM//BD_BM_ind1.sqlite')
            # path = os.path.normpath('C://000_testimportBM//BD_BM_ind3.sqlite')
            #path = os.path.normpath('C://001_travail_BM//BD_SIJALAG_ind0_travail2.sqlite')
            #path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201710_Begles//BD_Begles_ind0.sqlite')
            # path = os.path.normpath('C://000_testdigue//testBM//BD_Begles_ind0.sqlite')
            #path = os.path.normpath('C://000_testdigue//BM//BD_SIJALAG_ind4.sqlite')
            # path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201708_SIJALAG//BD_SIJALAG_ind5.sqlite')
            # path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201710_Begles//BD_Begles_ind8.sqlite')
            #path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201709_RD//BD_Rivedroite_ind2.sqlite')
            # path = os.path.normpath('C://000_testdigue//BM_SIJALAG//BD_SIJALAG_ind6.sqlite')
            # path = os.path.normpath('C://00_Affaires//BM_digues//Base_donnees//Begles//BD_Begles_ind9.sqlite')
            # path = os.path.normpath('C://000_testdigue//BD_Begles_ind8.sqlite')
            # path = os.path.normpath('I://CD17-2016//03-BDC//4352286-BDC182131-00790-DIGUE DE GUYENNE BOYARDVILLE//5_Etude//Basedonnees//BD_Cayenne_ind1.sqlite')

            #path = os.path.normpath("C://000_testdigue//convertBM//TO//BD_SIJALAG_ind10.sqlite")

            #path = os.path.normpath("C://000_testdigue//201710_Begles//BD_Begles_ind13.sqlite")

            #path = os.path.normpath("C://000_testdigue//voncent//Plaisance_ind0.sqlite")
            path = "C://000_testdigue//URBAIN//Nieul_ind1.sqlite"
            path = "C://000_testdigue//temp_base2_assainissement//test02.sqlite"

            wind.dbase.loadQgisVectorLayers(path)
            wind.loadUiDesktop()

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)




    if True:
        indexrapport = None
        for i, menutool in enumerate(wind.menutools):
            #print('ook', menutool.__class__.__name__)
            if 'importShapefile' in menutool.__class__.__name__ :
                #print('oooo',i)
                indexrapport = i
                break
        """
        self.pdffile = pdffile
        self.reporttype = reporttype
        """
        # Desordres Infralineaire Equipement_hydraulique

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
                [u'Infralineaire.anPoseSup', u''], [u'Infralineaire.maitreOuvrage', u''], [u'Infralineaire.exploitant', u''], [u'Infralineaire.enService', u''],
                [u'Infralineaire.branchement', u''], [u'Infralineaire.modeCirculation', u''], [u'Infralineaire.anPoseInf', u''], [u'Infralineaire.longueur', u''],

                [u'Infralineaire.typeReseau', u'type2'],

                 [u'Infralineaire.contCanAss', u''], [u'Infralineaire.fonctionCannAss', u''], [u'Infralineaire.altAmont', u''],
                [u'Infralineaire.altAval', u''], [u'Infralineaire.profamont', u''], [u'Infralineaire.profaval', u''], [u'Objet.pk_objet', u''], [u'Objet.id_objet', u''],
                [u'Objet.id_revisionbegin', u''], [u'Objet.id_revisionend', u''], [u'Objet.datecreation', u''], [u'Objet.datemodification', u''], [u'Objet.datedestruction', u''],
                [u'Objet.commentaire', u''], [u'Objet.libelle', u''], [u'Objet.importid', u''], [u'Objet.importtable', u''], [u'Descriptionsystem.pk_descriptionsystem', u''],
                [u'Descriptionsystem.id_descriptionsystem', u''], [u'Descriptionsystem.id_revisionbegin', u''], [u'Descriptionsystem.id_revisionend', u''],
                [u'Descriptionsystem.id_objet', u''], [u'Descriptionsystem.importancestrat', u''], [u'Descriptionsystem.etatfonct', u''],
                [u'Descriptionsystem.qualitegeolocXY', u''], [u'Descriptionsystem.qualiteGeolocZ', u''], [u'Descriptionsystem.dateGeoloc', u''],
                [u'Descriptionsystem.sourceGeoloc', u''], [u'Descriptionsystem.parametres', u''], [u'Descriptionsystem.listeparametres', u'']]

        linknoeud =  [[u'Noeud.pk_noeud', u''], [u'Noeud.id_noeud', u''], [u'Noeud.id_revisionbegin', u''],
                 [u'Noeud.id_revisionend', u''], [u'Noeud.id_objet', u''], [u'Noeud.id_descriptionsystem', u''],
                 [u'Noeud.altradierouvrage', u''], [u'Noeud.alttamponouvrage', u''], [u'Noeud.profradierouvrage', u''],

                 [u'Noeud.typeReseau', u''],

                 [u'Noeud.typeOuvrageAss', u''], [u'Noeud.accessibilite', u''],
                 [u'Noeud.cloisonsiphoide', u''], [u'Noeud.couvercle', u''], [u'Noeud.X', u''], [u'Noeud.dX', u''], [u'Noeud.Y', u''],
                 [u'Noeud.dY', u''], [u'Noeud.Z', u''], [u'Noeud.dZ', u''], [u'Objet.pk_objet', u''], [u'Objet.id_objet', u''],
                 [u'Objet.id_revisionbegin', u''], [u'Objet.id_revisionend', u''], [u'Objet.datecreation', u''], [u'Objet.datemodification', u''],
                 [u'Objet.datedestruction', u''], [u'Objet.commentaire', u''], [u'Objet.libelle', u''], [u'Objet.importid', u''],
                 [u'Objet.importtable', u''], [u'Descriptionsystem.pk_descriptionsystem', u''], [u'Descriptionsystem.id_descriptionsystem', u''],
                 [u'Descriptionsystem.id_revisionbegin', u''], [u'Descriptionsystem.id_revisionend', u''], [u'Descriptionsystem.id_objet', u''],
                 [u'Descriptionsystem.importancestrat', u''], [u'Descriptionsystem.etatfonct', u''],
                 [u'Descriptionsystem.qualitegeolocXY', u''],  [u'Descriptionsystem.qualiteGeolocZ', u''],  [u'Descriptionsystem.dateGeoloc', u''],
                 [u'Descriptionsystem.sourceGeoloc', u''],[u'Descriptionsystem.parametres', u''], [u'Descriptionsystem.listeparametres', u'']]





        wind.dbase.printsql = True

        if True:
            #layer = qgis.core.QgsVectorLayer('C://000_testdigue//voncent//31424_RESEAU31-EU_a_regard.shp', 'test', "ogr")
            # layer = qgis.core.QgsVectorLayer("C://000_testdigue//URBAIN//reseau_noeudsV1.shp", 'test', "ogr")
            layer = qgis.core.QgsVectorLayer("C://000_testdigue//URBAIN//reseau_tronconsV2.shp", 'test', "ogr")
            layer = qgis.core.QgsVectorLayer("C://000_testdigue//testnoeud.shp", 'test', "ogr")


            wind.menutools[indexrapport].importtable = 'Noeud'
            wind.menutools[indexrapport].work(linknoeud,layer)




# *********************************************************************************************************************
# ******************************************   MAIN      *************************************************************
# *********************************************************************************************************************


try:
    qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
except AttributeError:  #qgis 3
    qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT

print(qgisversion_int)

if int(str(qgisversion_int)[0:3]) < 220:
    qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
else:
    qgis_path = "C://OSGeo4W64//apps//qgis"

app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()
canvas = qgis.gui.QgsMapCanvas()
canvas.enableAntiAliasing(True)


# spatialite   postgis
# Infrastructure lineaire   #  Equipements hydrauliques #Desordres
# c://testrapport.pdf
testRapport(canvas,True,typedb="spatialite",reporttype="Desordres", pdffile="c://testrapport.pdf")


app.exec_()
qgis.core.QgsApplication.exitQgis()
print('ok')
