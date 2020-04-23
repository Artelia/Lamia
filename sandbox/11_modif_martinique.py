# -*- coding: utf-8 -*-

import os
import sys
import qgis
import qgis.gui
import qgis.utils
import shutil
import pprint
from shutil import copyfile

from Lamia.Lamia.main.DBaseParser import DBaseParser

try:
    qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
except AttributeError:  # qgis 3
    qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT
# print(qgisversion_int)

if int(str(qgisversion_int)[0:3]) < 220:
    qgis_path = "C://OSGeo4W64//apps//qgis218"
    qgis_path = "C://Program Files//OSGeo4W64//apps//qgis-ltr"
else:
    qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
    # os.environ["QT_QPA_PLATFORM"] = "offscreen"

app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()


def scriptMartinique(filelamia):
    """


    :param filelamia:
    :return:
    """


    dbaseparserfrom = DBaseParser(None)
    dbaseparserfrom.loadQgisVectorLayers(filelamia)




    sql = """SELECT pk_noeud, pk_desordre FROM Noeud_qgis 
             LEFT JOIN Desordre_qgis ON Desordre_qgis.lid_descriptionsystem = Noeud_qgis.id_descriptionsystem"""
    ressql = dbaseparserfrom.query(sql)

    pprint.pprint(ressql)

    for pk_noeud, pk_desordre in ressql:
        print(pk_noeud, pk_desordre)

        if  pk_desordre is None:



            # save a disorder on first creation
            pkobjet = dbaseparserfrom.createNewObjet()
            lastiddesordre = dbaseparserfrom.getLastId('Desordre') + 1
            geomtext, iddessys = dbaseparserfrom.getValuesFromPk('Noeud_qgis',
                                                            ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                            #self.currentFeaturePK)
                                                            pk_noeud)


            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext)

            if int(str(dbaseparserfrom.qgisversion_int)[0:3]) < 220:
                newgeom = qgis.core.QgsGeometry.fromPolyline([qgsgeom.asPoint(), qgsgeom.asPoint()])
                newgeomwkt = newgeom.exportToWkt()
            else:
                # newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPointXY(), qgsgeom.asPointXY()])
                newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
                newgeomwkt = newgeom.asWkt()

            sql = dbaseparserfrom.createSetValueSentence(type='INSERT',
                                                    tablename='Desordre',
                                                    listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                  'lid_descriptionsystem', 'geom'],
                                                    listofrawvalues=[lastiddesordre, pkobjet, 'NOD',
                                                                     iddessys, newgeomwkt])
            dbaseparserfrom.query(sql, docommit=False)

    dbaseparserfrom.commit()






print('start')

pathfile = "C://000_testdigue//00_martinique//Martinique_import.sqlite"
scriptMartinique(pathfile)

print('ok')