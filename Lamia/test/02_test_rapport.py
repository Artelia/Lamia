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
            print mapl.name()



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
            # path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201708_SIJALAG//BD_SIJALAG_ind4.sqlite')
            path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201710_Begles//BD_Begles_ind8.sqlite')
            #path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201709_RD//BD_Rivedroite_ind2.sqlite')
            wind.dbase.loadQgisVectorLayers(path)

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)


    if True:
        # testVirtualLayer()
        wind.printRapport(reporttype=reporttype, pdffile=pdffile)
        print('fin')

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
