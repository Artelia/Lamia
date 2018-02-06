# -*- coding: utf-8 -*-

import qgis
import os
from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal
import numpy as np

class exportShapefileWorker(AbstractWorker):

    def __init__(self, dbase, windowdialog, reporttype, pdffile):
        AbstractWorker.__init__(self)
        self.dbase = dbase
        self.reporttype = reporttype
        self.windowdialog = windowdialog
        self.pdffile = pdffile

    def work(self):

        # export by zonegeo
        boundinggeom = None
        if len(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()) == 1:
            currentfeat = self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()[0]
            print(currentfeat['id_zonegeo'])
            sql = "SELECT ST_AsText(ST_MakeValid(Zonegeo.geom)) FROM Zonegeo WHERE Zonegeo.id_zonegeo = " + str(currentfeat['id_zonegeo'])
            query = self.dbase.query(sql)
            result = [row[0] for row in query][0]
            boundinggeom = result



        if self.reporttype == 'Infralineaire':

            champs = [['Objet', 'datecreation'],                    #0
                      ['Objet', 'datedestruction'],
                      ['Objet', 'commentaire'],
                      ['Objet', 'libelle'],
                      ['Descriptionsystem', 'importancestrat'],
                      ['Descriptionsystem', 'etatfonct'],                    #5
                      ['Descriptionsystem', 'datederniereobs'],
                      ['Descriptionsystem', 'qualitegeoloc'],
                      ['Descriptionsystem', 'parametres'],
                      ['Descriptionsystem', 'listeparametres'],
                      ['Infralineaire', 'id_infralineaire'],                    #10
                      ['Infralineaire', 'description1'],
                      ['Infralineaire', 'description2'],
                      ['Infralineaire', 'lk_noeud1'],
                      ['Infralineaire', 'lk_noeud2'],
                      ['Infralineaire', 'lk_photo'],                    #15
                      ['Infralineaire', 'lk_profil'],
                      ['Infralineaire', 'id_objet'],
                      ['Infralineaire', 'id_descriptionsystem']]

            fieldslinear = self.getFieldsfromList(champs)



            sql = "SELECT "
            sql += ', '.join([str(field[0])+'.'+str(field[1]) for field in champs])
            sql += ", ST_AsText(Infralineaire.geom) "
            sql += "FROM Infralineaire "
            sql += "INNER JOIN Descriptionsystem ON Infralineaire.id_descriptionsystem = Descriptionsystem.id_descriptionsystem "
            sql += "INNER JOIN Objet ON Objet.id_objet = Infralineaire.id_objet "
            sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
            sql += ";"
            # print(sql)
            query = self.dbase.query(sql)
            result = [row for row in query]

            #donnees profil
            if True:
                fieldslinear.append(qgis.core.QgsField('Hauteur', QtCore.QVariant.Double))
                fieldslinear.append(qgis.core.QgsField('Largeurcrete', QtCore.QVariant.Double))
                fieldslinear.append(qgis.core.QgsField('LargeurAubarede', QtCore.QVariant.Double))
                fieldslinear.append(qgis.core.QgsField('Des_prof', QtCore.QVariant.String))
                champs += [[],[],[],[]]
                # print('champs',champs)
                for i, row in enumerate(result):
                    largcrete = -1
                    largfrancbord = -1
                    hauteurdigue = -1
                    description = ''
                    lkprofil  = row[16]
                    if lkprofil is not None:
                        sql = "SELECT id_graphique, typegraphique FROM Graphique  WHERE id_ressource = " + str(lkprofil)
                        query = self.dbase.query(sql)
                        resultrow = [row1 for row1 in query]
                        if len(resultrow)>0 and resultrow[0][1] == 'PTR':
                            sql = "SELECT * FROM Graphiquedata WHERE id_graphique = " + str(resultrow[0][0])
                            sql += " ORDER BY id_graphiquedata"
                            query = self.dbase.query(sql)
                            resultrow2 = [list(row2) for row2 in query]
                            # row : [id, None, dx, dz, None, position, type1, type2, None, 1]
                            npresultrow = np.array(resultrow2)
                            #largeur crete
                            index = np.where(npresultrow[:,5] == 'CRE')
                            largcrete = np.sum(npresultrow[:,2][index])
                            #hauteur
                            minindex = int(np.amin(index))
                            hauteurdigue = np.sum(npresultrow[0:minindex, 3])
                            #francbord
                            index = np.where(npresultrow[:,5] == 'FRB')
                            largfrancbord = np.sum(npresultrow[:,2][index])
                            # print(hauteurdigue, largcrete, largfrancbord)
                            #description
                            listdescr = ['dX;dZ;Partie;Type1;Type2']
                            for elem in resultrow2:
                                listdescr += [';'.join([str(round(elem[2],1)),
                                                         str(round(elem[3],1)),
                                                         self.dbase.getConstraintTextFromRawValue('Graphiquedata', 'index1', elem[5]),
                                                        self.dbase.getConstraintTextFromRawValue('Graphiquedata','index2', elem[6]),
                                                         self.dbase.getConstraintTextFromRawValue('Graphiquedata', 'index3', elem[7])])]
                            description = '\n'.join(listdescr)
                            if False:
                                print(listdescr)

                                print(description)
                                return


                    result[i] = list(result[i])[:-1] + [hauteurdigue, largcrete, largfrancbord,description] + list(result[i])[-1:]


            #niveau protection surete
            if True:
                fieldslinear.append(qgis.core.QgsField('niv_pro_am', QtCore.QVariant.Double))
                fieldslinear.append(qgis.core.QgsField('niv_pro_av', QtCore.QVariant.Double))
                fieldslinear.append(qgis.core.QgsField('niv_sur_am', QtCore.QVariant.Double))
                fieldslinear.append(qgis.core.QgsField('niv_sur_av', QtCore.QVariant.Double))
                champs += [[], [], [],[]]

                profiletraverstool = self.windowdialog.pathtool
                profiletraverstool.computeNXGraph()

                for i, row in enumerate(result):
                    niv_pro_am = None
                    niv_pro_av = None
                    niv_sur_am = None
                    niv_sur_av = None

                    #currentgeom = self.currentFeature.geometry().asPolyline()
                    currentgeom = qgis.core.QgsGeometry.fromWkt(row[-1]).asPolyline()
                    profiletraverstool.computePath(list(currentgeom[0]), list(currentgeom[-1]))
                    datas = profiletraverstool.getGraphData()

                    for graphname in datas.keys():
                        if 'NIV' in graphname:
                            niv_pro_am = round(datas[graphname]['y'][0],2)
                            niv_pro_av = round(datas[graphname]['y'][-1],2)

                        if 'SUR' in graphname:
                            niv_sur_am = round(datas[graphname]['y'][0],2)
                            niv_sur_av = round(datas[graphname]['y'][-1],2)

                    result[i] = list(result[i])[:-1] + [niv_pro_am, niv_pro_av, niv_sur_am, niv_sur_av] + list(result[i])[-1:]

                profiletraverstool.rubberBand.reset(1)



            # gestionnaire
            if True:
                fieldslinear.append(qgis.core.QgsField('Gestionnaire', QtCore.QVariant.String))
                champs += [[]]

                for i, row in enumerate(result):
                    gestionnaire = ''
                    idobjet = row[17]
                    sql = "SELECT Tcobjetintervenant.fonction, Intervenant.nom,Intervenant.societe  FROM Tcobjetintervenant "
                    sql += " INNER JOIN Intervenant ON Tcobjetintervenant.id_tcintervenant = Intervenant.id_intervenant "
                    sql += "WHERE id_tcobjet = " + str(idobjet)
                    query = self.dbase.query(sql)
                    resultges = [row1 for row1 in query]
                    for interv in resultges:
                        if interv[0] == 'GES':
                            gestionnaire = interv[2] + ' - ' + interv[1]
                    result[i] = list(result[i])[:-1] + [gestionnaire] + list(result[i])[-1:]




            #process shapefile
            # print(len(result), result[0])
            self.fillShapefile(self.pdffile, qgis.core.QGis.WKBLineString, fieldslinear, champs, result)


        if self.reporttype == 'Equipement':

            champs = [['Objet', 'datecreation'],
                      ['Objet', 'datedestruction'],
                      ['Objet', 'commentaire'],
                      ['Objet', 'libelle'],
                      ['Descriptionsystem', 'importancestrat'],
                      ['Descriptionsystem', 'etatfonct'],
                      ['Descriptionsystem', 'datederniereobs'],
                      ['Descriptionsystem', 'qualitegeoloc'],
                      ['Descriptionsystem', 'parametres'],
                      ['Descriptionsystem', 'listeparametres'],
                      ['Equipement', 'id_equipement'],
                      ['Equipement', 'cote'],
                      ['Equipement', 'position'],
                      ['Equipement', 'categorie'],
                      ['Equipement', 'typeequipement'],
                      ['Equipement', 'implantation'],
                      ['Equipement', 'ecoulement'],
                      ['Equipement', 'utilisation'],
                      ['Equipement', 'dimverti'],
                      ['Equipement', 'dimhori'],
                      ['Equipement', 'securite'],
                      ['Equipement', 'commentaires'],
                      ['Equipement', 'id_objet'],
                      ['Equipement', 'lk_infralineaire'],
                      ['Equipement', 'lk_noeud'],
                      ['Equipement', 'lk_equipement']]

            fieldslinear = self.getFieldsfromList(champs)

            # **********************************************************
            # line elements
            pdfdir = os.path.dirname(self.pdffile)
            name = os.path.basename(self.pdffile).split('.')[0]
            linearname = os.path.join(pdfdir, name + '_lineaire.shp')

            sql = "SELECT "
            sql += ', '.join([str(field[0])+'.'+str(field[1]) for field in champs])
            sql += ", ST_AsText(Equipement.geom) "
            sql += "FROM Equipement "
            sql += "INNER JOIN Descriptionsystem ON Equipement.id_descriptionsystem = Descriptionsystem.id_descriptionsystem "
            sql += "INNER JOIN Objet ON Objet.id_objet = Equipement.id_objet "
            sql += " WHERE NOT ST_EQUALS(ST_StartPoint(Equipement.geom) , ST_EndPoint(Equipement.geom)) "

            if boundinggeom is not None :
                sql += " AND ST_WITHIN(ST_MakeValid(Equipement.geom), ST_GeomFromText('" + boundinggeom + "',"+ str(self.dbase.crsnumber) + ")) "

            sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
            sql += ";"
            print(sql)
            query = self.dbase.query(sql)
            result = [row for row in query]
            print(len(result), result[0])
            self.fillShapefile(linearname, qgis.core.QGis.WKBLineString, fieldslinear, champs, result)

            # **********************************************************
            # point elements
            pdfdir = os.path.dirname(self.pdffile)
            name = os.path.basename(self.pdffile).split('.')[0]
            linearname = os.path.join(pdfdir, name + '_ponctuel.shp')

            sql = "SELECT "
            sql += ', '.join([str(field[0]) + '.' + str(field[1]) for field in champs])
            sql += ", ST_AsText(ST_StartPoint(Equipement.geom)) "
            sql += "FROM Equipement "
            sql += "INNER JOIN Descriptionsystem ON Equipement.id_descriptionsystem = Descriptionsystem.id_descriptionsystem "
            sql += "INNER JOIN Objet ON Objet.id_objet = Equipement.id_objet "
            sql += " WHERE ST_EQUALS(ST_StartPoint(Equipement.geom) , ST_EndPoint(Equipement.geom))"
            if boundinggeom is not None :
                sql += " AND ST_WITHIN(ST_StartPoint(Equipement.geom), ST_GeomFromText('" + boundinggeom + "',"+ str(self.dbase.crsnumber) + ")) "


            sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
            sql += ";"
            query = self.dbase.query(sql)
            result = [row for row in query]
            self.fillShapefile(linearname, qgis.core.QGis.WKBPoint, fieldslinear, champs, result)




        elif self.reporttype == 'Observations':

            champs =[['Objet', 'datecreation'],
                     ['Objet', 'datedestruction'],
                     ['Objet', 'commentaire'],
                     ['Objet', 'libelle'],
                     ['Desordre', 'id_desordre'],
                     ['Desordre', 'cote'],
                     ['Desordre', 'position'],
                     ['Desordre', 'catdes'],
                     ['Desordre', 'typedes'],
                     ['Desordre', 'impact'],
                     # ['Desordre', 'gravite'],
                     ['Desordre', 'priorite'],
                     ['Desordre', 'risques'],
                     ['Observation', 'id_observation'],
                     ['Observation', 'dateobservation'],
                     ['Observation', 'source'],
                     ['Observation', 'nombre'],
                     ['Observation', 'gravite'],
                     ['Observation', 'evolution'],
                     ['Observation', 'commentaires'],
                     ['Observation', 'suite'],
                     ['Observation', 'lk_desordre'],
                     ['Observation', 'id_objet']]


            fieldslinear = self.getFieldsfromList(champs)

            # **********************************************************
            # line elements
            pdfdir = os.path.dirname(self.pdffile)
            name = os.path.basename(self.pdffile).split('.')[0]
            linearname = os.path.join(pdfdir, name + '_lineaire.shp')

            """
            spatialite
            SELECT Observation.*, MAX(Observation.dateobservation)
            FROM Observation
            INNER JOIN Desordre ON Observation.lk_desordre = Desordre.id_desordre
            INNER JOIN Objet ON Objet.id_objet = Observation.id_objet
            GROUP BY Observation.lk_desordre
            """

            """
            postgis
            # SET search_path TO digue ,public;
            SELECT DISTINCT ON (Observation.lk_desordre ) Observation.*
            FROM Observation
            INNER JOIN Desordre ON Observation.lk_desordre = Desordre.id_desordre
            INNER JOIN Objet ON Objet.id_objet = Observation.id_objet
            ORDER BY Observation.lk_desordre, Observation.dateobservation DESC;
            """

            sql = "SELECT "
            sql += ', '.join([str(field[0])+'.'+str(field[1]) for field in champs])
            sql += ", ST_AsText(Desordre.geom) "
            sql += "FROM Observation  "
            sql += " INNER JOIN Desordre ON Observation.lk_desordre = Desordre.id_desordre  "
            sql += "INNER JOIN Objet ON Objet.id_objet = Observation.id_objet "
            sql += " WHERE NOT ST_EQUALS(ST_StartPoint(Desordre.geom) , ST_EndPoint(Desordre.geom))"
            if boundinggeom is not None :
                sql += " AND ST_WITHIN(ST_MakeValid(Desordre.geom), ST_GeomFromText('" + boundinggeom + "',"+ str(self.dbase.crsnumber) + ")) "

            sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'

            sql += ";"

            print(sql)

            query = self.dbase.query(sql)
            result = [row for row in query]
            print(len(result), result[0])
            print(isinstance(result[0][0], datetime.date))
            self.fillShapefile(linearname, qgis.core.QGis.WKBLineString, fieldslinear, champs, result)

            # **********************************************************
            # point elements
            pdfdir = os.path.dirname(self.pdffile)
            name = os.path.basename(self.pdffile).split('.')[0]
            linearname = os.path.join(pdfdir, name + '_ponctuel.shp')

            sql = "SELECT "
            sql += ', '.join([str(field[0])+'.'+str(field[1]) for field in champs])
            sql += ", ST_AsText(ST_StartPoint(Desordre.geom)) "
            sql += "FROM Observation  "
            sql += " INNER JOIN Desordre ON Observation.lk_desordre = Desordre.id_desordre  "
            sql += "INNER JOIN Objet ON Objet.id_objet = Observation.id_objet "
            sql += " WHERE  ST_EQUALS(ST_StartPoint(Desordre.geom) , ST_EndPoint(Desordre.geom))"
            if boundinggeom is not None :
                sql += " AND ST_WITHIN(ST_StartPoint(Desordre.geom), ST_GeomFromText('" + boundinggeom + "',"+ str(self.dbase.crsnumber) + ")) "

            sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'

            sql += ";"

            print(sql)
            query = self.dbase.query(sql)
            result = [row for row in query]
            print(len(result), result[0])

            self.fillShapefile(linearname, qgis.core.QGis.WKBPoint, fieldslinear, champs, result)


        elif self.reporttype == 'Dernieres observations':

            champs =[
                    ['Desordre', 'id_desordre'],
                    ['Desordre', 'cote'],
                    ['Desordre', 'position'],
                    ['Desordre', 'catdes', 'Categorie'],
                    ['Desordre', 'typedes', 'Type'],
                    # ['Desordre', 'impact'],
                    # ['Desordre', 'gravite'],
                    # ['Desordre', 'priorite'],
                    # ['Desordre', 'risques'],
                    ['Observation', 'id_observation'],
                    ['Observation', 'dateobservation'],
                    ['Observation', 'source'],
                    ['Observation', 'nombre'],
                    ['Observation', 'gravite'],
                    ['Observation', 'evolution'],
                    ['Observation', 'commentaires'],
                    ['Observation', 'suite'],
                    #['Observation', 'lk_desordre'],
                    ['Observation', 'id_objet'],
                    #['Objet', 'datecreation'],
                    # ['Objet', 'datedestruction'],
                     #['Objet', 'commentaire'],
                     #['Objet', 'libelle']
                                                         ]



            fieldslinear = self.getFieldsfromList(champs)

            # **********************************************************
            # line elements
            pdfdir = os.path.dirname(self.pdffile)
            name = os.path.basename(self.pdffile).split('.')[0]
            linearname = os.path.join(pdfdir, name + '_lineaire.shp')

            """
            spatialite
            SELECT Observation.*, MAX(Observation.dateobservation)
            FROM Observation
            INNER JOIN Desordre ON Observation.lk_desordre = Desordre.id_desordre
            INNER JOIN Objet ON Objet.id_objet = Observation.id_objet
            GROUP BY Observation.lk_desordre
            """

            """
            postgis
            # SET search_path TO digue ,public;
            SELECT DISTINCT ON (Observation.lk_desordre ) Observation.*
            FROM Observation
            INNER JOIN Desordre ON Observation.lk_desordre = Desordre.id_desordre
            INNER JOIN Objet ON Objet.id_objet = Observation.id_objet
            ORDER BY Observation.lk_desordre, Observation.dateobservation DESC;
            """



            sql = "SELECT "
            if self.dbase.dbasetype == 'postgis':
                sql += "DISTINCT ON (Observation.lk_desordre) "
            sql += ', '.join([str(field[0])+'.'+str(field[1]) for field in champs])
            if self.dbase.dbasetype == 'spatialite':
                sql += ", MAX(Observation.dateobservation)"
            sql += ", ST_AsText(Desordre.geom) "
            sql += "FROM Observation  "
            sql += " INNER JOIN Desordre ON Observation.lk_desordre = Desordre.id_desordre  "
            sql += "INNER JOIN Objet ON Objet.id_objet = Observation.id_objet "
            sql += " WHERE NOT ST_EQUALS(ST_StartPoint(Desordre.geom) , ST_EndPoint(Desordre.geom))"
            if boundinggeom is not None :
                sql += " AND ST_WITHIN(ST_MakeValid(Desordre.geom), ST_GeomFromText('" + boundinggeom + "',"+ str(self.dbase.crsnumber) + ")) "

            sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'

            if self.dbase.dbasetype == 'postgis':
                sql += " ORDER BY Observation.lk_desordre, Observation.dateobservation DESC"
            elif self.dbase.dbasetype == 'spatialite':
                sql += " GROUP BY Observation.lk_desordre "
            sql += ";"

            query = self.dbase.query(sql)
            result = [row for row in query]
            self.fillShapefile(linearname, qgis.core.QGis.WKBLineString, fieldslinear, champs, result)

            # **********************************************************
            # point elements
            pdfdir = os.path.dirname(self.pdffile)
            name = os.path.basename(self.pdffile).split('.')[0]
            linearname = os.path.join(pdfdir, name + '_ponctuel.shp')

            sql = "SELECT "
            if self.dbase.dbasetype == 'postgis':
                sql += "DISTINCT ON (Observation.lk_desordre) "
            sql += ', '.join([str(field[0])+'.'+str(field[1]) for field in champs])
            if self.dbase.dbasetype == 'spatialite':
                sql += ", MAX(Observation.dateobservation)"
            sql += ", ST_AsText(ST_StartPoint(Desordre.geom)) "
            sql += "FROM Observation  "
            sql += " INNER JOIN Desordre ON Observation.lk_desordre = Desordre.id_desordre  "
            sql += "INNER JOIN Objet ON Objet.id_objet = Observation.id_objet "
            sql += " WHERE  ST_EQUALS(ST_StartPoint(Desordre.geom) , ST_EndPoint(Desordre.geom))"
            if boundinggeom is not None :
                sql += " AND ST_WITHIN(ST_StartPoint(Desordre.geom), ST_GeomFromText('" + boundinggeom + "',"+ str(self.dbase.crsnumber) + ")) "

            sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'

            if self.dbase.dbasetype == 'postgis':
                sql += " ORDER BY Observation.lk_desordre, Observation.dateobservation DESC"
            elif self.dbase.dbasetype == 'spatialite':
                sql += " GROUP BY Observation.lk_desordre "
            sql += ";"

            query = self.dbase.query(sql)
            result = [row for row in query]

            self.fillShapefile(linearname, qgis.core.QGis.WKBPoint, fieldslinear, champs, result)


        elif self.reporttype == 'Photo':

            champs =[['Photo', 'id_photo'],
                    #['Photo', 'typephoto'],
                    #['Photo', 'id_objet'],
                    #['Objet', 'datecreation' ],
                     #['Objet', 'datedestruction'],
                     #['Objet', 'commentaire'],
                     #['Objet', 'libelle'],
                     ['Ressource', 'source'],
                     ['Ressource', 'dateressource','datephoto'],
                     #['Ressource', 'contactadresse'],
                     #['Ressource', 'contactnom'],
                     #['Ressource', 'contactmail'],
                     #['Ressource', 'contacttel1'],
                     #['Ressource', 'contacttel2'],
                     ['Ressource', 'file','fichier'],
                     ['Ressource', 'description'],
                     # ['Ressource', 'lk_objet'],
                     ['Tcobjetressource', 'id_tcobjet','lk_objet']]


            fieldslinear = self.getFieldsfromList(champs)


            dir = os.path.dirname(self.pdffile)
            name = os.path.basename(self.pdffile).split('.')[0]
            linearname = os.path.join(dir, name + '.shp')

            """
            SELECT * FROM Photo
            INNER JOIN Ressource ON Ressource.id_ressource = Photo.id_ressource
            INNER JOIN Objet ON Objet.id_objet = Photo.id_objet
            LEFT JOIN Tcobjetressource ON Tcobjetressource.id_tcressource = Ressource.id_ressource
            """

            sql = "SELECT "
            sql += ', '.join([str(field[0])+'.'+str(field[1]) for field in champs])
            sql += ", ST_AsText(Photo.geom) "
            sql += "FROM Photo  "
            sql += " INNER JOIN Ressource ON Ressource.id_ressource = Photo.id_ressource "
            sql += "INNER JOIN Objet ON Objet.id_objet = Photo.id_objet "
            sql += " LEFT JOIN Tcobjetressource ON Tcobjetressource.id_tcressource = Ressource.id_ressource"

            sql += " WHERE "


            sql += '  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
            sql += " AND Photo.typephoto = 'PHO' "
            if boundinggeom is not None :
                sql += " AND ST_WITHIN(ST_MakeValid(Photo.geom), ST_GeomFromText('" + boundinggeom + "',"+ str(self.dbase.crsnumber) + ")) "
            sql += ";"

            query = self.dbase.query(sql)
            result = [row for row in query]
            # print(len(result),result[0])
            self.fillShapefile(linearname, qgis.core.QGis.WKBPoint, fieldslinear, champs, result)









    def fillShapefile(self, filename, typegeom, fields, champs, result):
        writer = qgis.core.QgsVectorFileWriter(filename,
                                               'UTF-8',
                                                fields,
                                                typegeom,
                                                # qgis.core.QGis.WKBPoint,
                                                # qgis.core.QGis.WKBLineString,
                                                self.dbase.qgiscrs)

        for row in result:
            feat = qgis.core.QgsFeature(fields)
            if row[-1] is not None:
                feat.setGeometry(qgis.core.QgsGeometry.fromWkt(row[-1]))
            else:
                continue
            # print(feat.geometry().exportToWkt())
            for i, field in enumerate(champs):
                if len(field)>0:       #come from simple db
                    if row[i] is not None and row[i] != 'NULL' and row[i] != 'None':
                        if 'Cst' in self.dbase.dbasetables[field[0]]['fields'][field[1]].keys():
                            feat[i] = self.dbase.getConstraintTextFromRawValue(field[0], field[1], row[i])
                        else:
                            if isinstance(row[i], datetime.date):
                                value = str(row[i])
                            elif isinstance(row[i], decimal.Decimal):
                                value = float(row[i])
                            else:
                                value = row[i]
                            feat[i] = value
                else:   #computed field
                    feat[i] = row[i]
            writer.addFeature(feat)

        del writer


    def getFieldsfromList(self,fieldlist):
        fieldslinear = qgis.core.QgsFields()

        for field in fieldlist:
            if len(field) == 3:
                fieldname = field[2]
            else:
                fieldname = field[1]

            if 'INTEGER' in self.dbase.dbasetables[field[0]]['fields'][field[1]]['SLtype']:
                fieldslinear.append(qgis.core.QgsField(fieldname, QtCore.QVariant.Int))
            elif 'REAL' in self.dbase.dbasetables[field[0]]['fields'][field[1]]['SLtype']:
                fieldslinear.append(qgis.core.QgsField(fieldname, QtCore.QVariant.Double))
            elif 'TEXT' in self.dbase.dbasetables[field[0]]['fields'][field[1]]['SLtype']:
                fieldslinear.append(qgis.core.QgsField(fieldname, QtCore.QVariant.String))

        return fieldslinear

