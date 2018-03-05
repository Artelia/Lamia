# -*- coding: utf-8 -*-

import qgis
import os
from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal

class ImportObjectWorker(AbstractWorker):

    def __init__(self, dbase, importtable,results):
        AbstractWorker.__init__(self)
        self.dbase = dbase
        self.importtable = importtable
        self.results = results


    def work(self):
        print(self.importtable)

        tablestemp = [result[0].split('.')[0] for result in self.results]
        tables = list(set(tablestemp))
        # print(tables)

        print(self.results)

        tablefield = [result[0] for result in self.results]
        values = [result[1] for result in self.results]

        if qgis.utils.iface is not None:
            layer = qgis.utils.iface.activeLayer()
        else:
            layer = qgis.core.QgsVectorLayer('C://001_travail_BM//testtopo//toposijalag1.shp', 'test', "ogr")

        layerfromfieldsname = [field.name() for field in layer.fields()]
        print('layerfromfieldsname',layerfromfieldsname)
        xform = qgis.core.QgsCoordinateTransform(layer.crs(), self.dbase.qgiscrs)
        if len(layer.selectedFeatures()) == 0:
            feats  = layer.getFeatures()
        else:
            feats = layer.selectedFeatures()



        if self.importtable == 'Points topo':
            table = 'Pointtopo'
            fielddestination=['typepointtopo', 'x', 'y', 'zgps', 'zwgs84', 'raf09', 'zmngf', 'precision', 'dx', 'dy', 'dz', 'hauteurperche',
                    'id_topographie','geom']


            linktable = {}
            for i, result in enumerate(self.results):
                for j, field in enumerate(fielddestination):
                    if table + '.' + field in result:
                        linktable[j] = i

            # print(linktable)




            for layerfeat in feats:
                sql = "INSERT INTO Pointtopo (" + ', '.join(fielddestination) + ") "
                sql += "VALUES("
                featvalues = []
                for i, field in enumerate(fielddestination):
                    # print('values',field,featvalues)
                    if field == 'geom':
                        featgeom = layerfeat.geometry()
                        success = featgeom.transform(xform)
                        featgeomwkt = featgeom.exportToWkt()

                        geomsql = "ST_GeomFromText('"
                        geomsql += featgeomwkt
                        geomsql += "', " + str(self.dbase.crsnumber) + ")"
                        featvalues.append(geomsql)
                    else:
                        valuefieldtemp = values[linktable[i]]
                        # print(valuefieldtemp, layerfromfieldsname)
                        if valuefieldtemp == '':
                            featvalues.append('NULL')
                        else:


                            if valuefieldtemp in layerfromfieldsname:
                                valuefieldtemp = layerfeat[valuefieldtemp]
                                # print(valuefieldtemp)
                                if valuefieldtemp is None:
                                    featvalues.append('NULL')
                                else:
                                    # print(type(valuefieldtemp))
                                    if isinstance(valuefieldtemp, unicode):
                                        featvalues.append("'" + str(valuefieldtemp) + "'")
                                    else:
                                        featvalues.append(str(valuefieldtemp))
                            else:
                                featvalues.append(str(valuefieldtemp))


                sql += ', '.join(featvalues)
                sql += ");"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()




        if self.importtable == 'Infralineaires':
            table = 'Infralineaire'
            fielddestination=['description1', 'description2', 'importancestrat', 'etatfonct', 'datederniereobs', 'qualitegeoloc', 'parametres', 'listeparametres', 'datecreation', 'datemodification', 'datedestruction', 'commentaire', 'libelle', 'geom']


            linktable = {}
            for i, result in enumerate(self.results):
                for j, field in enumerate(fielddestination):
                    if 'Infralineaire.' + field in result or 'Objet.'+ field in result or 'Descriptionsystem.' + field in result :
                        linktable[j] = i

            # print(linktable)




            for layerfeat in feats:
                sql = "INSERT INTO Objet (datecreation, datemodification, datedestruction, commentaire, libelle) VALUES ('"
                featvalues = []
                for i, field in enumerate(fielddestination):
                    if field in ['datecreation', 'datemodification', 'datedestruction', 'commentaire', 'libelle']:
                        valuefieldtemp = values[linktable[i]]
                        # print(valuefieldtemp, layerfromfieldsname)
                        if valuefieldtemp == '':
                            featvalues.append('NULL')
                        else:


                            if valuefieldtemp in layerfromfieldsname:
                                valuefieldtemp = layerfeat[valuefieldtemp]
                                # print(valuefieldtemp)
                                if valuefieldtemp is None:
                                    featvalues.append('NULL')
                                else:
                                    # print(type(valuefieldtemp))
                                    if isinstance(valuefieldtemp, unicode):
                                        featvalues.append("'" + str(valuefieldtemp) + "'")
                                    else:
                                        featvalues.append(str(valuefieldtemp))
                            else:
                                featvalues.append(str(valuefieldtemp))


                sql += ', '.join(featvalues)
                sql += ") RETURNING id_objet;"
                # print(sql)
                id_objet = self.dbase.query(sql)
                self.dbase.commit()



            for layerfeat in feats:
                sql = "INSERT INTO Descriptionsystem (id_objet, importancestrat, etatfonct, datederniereobs, qualitegeoloc, parametres, listeparametres) VALUES ('"
                sql += str(id_objet)+', '
                featvalues = []
                for i, field in enumerate(fielddestination):
                    if field in ['importancestrat', 'etatfonct', 'datederniereobs', 'qualitegeoloc', 'parametres', 'listeparametres']:
                        valuefieldtemp = values[linktable[i]]
                        # print(valuefieldtemp, layerfromfieldsname)
                        if valuefieldtemp == '':
                            featvalues.append('NULL')
                        else:


                            if valuefieldtemp in layerfromfieldsname:
                                valuefieldtemp = layerfeat[valuefieldtemp]
                                # print(valuefieldtemp)
                                if valuefieldtemp is None:
                                    featvalues.append('NULL')
                                else:
                                    # print(type(valuefieldtemp))
                                    if isinstance(valuefieldtemp, unicode):
                                        featvalues.append("'" + str(valuefieldtemp) + "'")
                                    else:
                                        featvalues.append(str(valuefieldtemp))
                            else:
                                featvalues.append(str(valuefieldtemp))


                sql += ', '.join(featvalues)
                sql += ") RETURNING id_descriptionsystem;"
                # print(sql)
                id_descriptionsystem = self.dbase.query(sql)
                self.dbase.commit()




                sql = "INSERT INTO Infralineaires (id_objet, id_descriptionsystem, description1, description2, geom) "
                sql += "VALUES("+str(id_objet)+', '+str(id_descriptionsystem)Z+', '
                featvalues = []
                for i, field in enumerate(fielddestination):
                    # print('values',field,featvalues)
                    if field == 'geom':
                        featgeom = layerfeat.geometry()
                        success = featgeom.transform(xform)
                        featgeomwkt = featgeom.exportToWkt()

                        geomsql = "ST_GeomFromText('"
                        geomsql += featgeomwkt
                        geomsql += "', " + str(self.dbase.crsnumber) + ")"
                        featvalues.append(geomsql)
                    else:
                        if field in ['description1', 'description2']:
                            valuefieldtemp = values[linktable[i]]
                            # print(valuefieldtemp, layerfromfieldsname)
                            if valuefieldtemp == '':
                                featvalues.append('NULL')
                            else:


                                if valuefieldtemp in layerfromfieldsname:
                                    valuefieldtemp = layerfeat[valuefieldtemp]
                                    # print(valuefieldtemp)
                                    if valuefieldtemp is None:
                                        featvalues.append('NULL')
                                    else:
                                        # print(type(valuefieldtemp))
                                        if isinstance(valuefieldtemp, unicode):
                                            featvalues.append("'" + str(valuefieldtemp) + "'")
                                        else:
                                            featvalues.append(str(valuefieldtemp))
                                else:
                                    featvalues.append(str(valuefieldtemp))


                sql += ', '.join(featvalues)
                sql += ");"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()








