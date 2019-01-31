import os
import sys
import qgis
import qgis.gui
import qgis.utils
import shutil

from Lamia.Lamia.main.DBaseParser import DBaseParser
import datetime



#pathfrom = "C://000_testdigue//convertBM//FROM//BD_SIJALAG_ind10.sqlite"
pathfrom = "C://000_testdigue//convertBM2//FROM//BD_Begles_ind16.sqlite"
pathfrom = "I://FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//62_Dessins//620_Qgis//Base_Valeyrac.sqlite"
pathfrom = "M://FR//BOR//VT//FLUVIAL//4352409_33_ASA_Baurech_EDD//6_Reglementaire//61_Calculs//lamia//baurech.sqlite"


#pathfrom = "C://000_testdigue//convertBM2//FROM//BD_SIJALAG_ind14.sqlite"
#pathfrom = "C://000_testdigue//convertBM2//FROM//BD_Rivedroite_ind5.sqlite"

dbaseparserfrom = DBaseParser(None)
dbaseparserfrom.loadQgisVectorLayers(pathfrom)

#pathto = "C://000_testdigue//convertBM//TO//BD_SIJALAG_ind10.sqlite"
pathto = "C://000_testdigue//convertBM2//TO//BD_Begles_ind17.sqlite"
pathto = "I://FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//62_Dessins//620_Qgis//temp//ancien//val3.sqlite"
pathto = "M://FR//BOR//VT//FLUVIAL//4352409_33_ASA_Baurech_EDD//6_Reglementaire//61_Calculs//lamia2//baurech2.sqlite"
#pathto = "C://000_testdigue//convertBM2//TO//BD_SIJALAG_ind15.sqlite"
# pathto = "C://000_testdigue//convertBM2//TO//BD_Rivedroite_ind6.sqlite"


if True:
    #originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'DBase_ind0.sqlite')
    #shutil.copyfile(originalfile, pathto)
    dbaseparserto = DBaseParser(None)
    # dbaseparserto.printsql = True
    dbaseparserto.createDbase(slfile=pathto, crs=2154, worktype='Base2_digue', dbasetype='spatialite',
                           dbaseressourcesdirectory=None)


if False:
    dbaseparserto = DBaseParser(None)
    dbaseparserto.createDbase(file=None, crs=3945, type='Base_digue', dbasetype='postgis',
                    dbname='PVR_test', schema='lamia_BM', user='postgres', host='localhost', port=5432, password='PVR',    # postgis
                    dbaseressourcesdirectory='C://000_testdigue//temp_postgis//digue')



# ************************************ MAIN **************************************************************************
if True:
    if False:
        sql = "SELECT metier, repertoireressources, crs FROM Basedonnees"
        results = list(dbaseparserfrom.query(sql))
        for result in results :
            print(result)
            sql = "INSERT INTO Basedonnees (metier, repertoireressources, crs) VALUES (?,?,?) "
            args = ['digue2',result[1],  result[2]]
            dbaseparserto.query(sql,args)



    if True:
        sql = "SELECT id_objet, datecreation, datemodification, datedestruction, commentaire, libelle FROM Objet"
        result = list(dbaseparserfrom.query(sql))
        results = list(dbaseparserfrom.query(sql))




        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            datetimecreation, datetimemodification,datetimedestruction  = None, None, None

            if result[1] is not None:
                datevalue = datetime.datetime.strptime(result[1], "%Y-%m-%d").date()
                datetime.datetime.combine(datevalue, datetime.datetime.min.time())
                datetimecreation = datevalue.strftime("%Y-%m-%d %H:%M:%S")
            if result[2] is not None:
                datevalue = datetime.datetime.strptime(result[2], "%Y-%m-%d").date()
                datetime.datetime.combine(datevalue, datetime.datetime.min.time())
                datetimemodification = datevalue.strftime("%Y-%m-%d %H:%M:%S")
            if result[3] is not None:
                datevalue = datetime.datetime.strptime(result[3], "%Y-%m-%d").date()
                datetime.datetime.combine(datevalue, datetime.datetime.min.time())
                datetimedestruction = datevalue.strftime("%Y-%m-%d %H:%M:%S")


            sql = "INSERT INTO Objet (id_objet,lpk_revision_begin, lpk_revision_end, datetimecreation,datetimemodification,datetimedestruction, commentaire, libelle  ) VALUES (?,?,?,?,?,?,?,?) "
            args = [                  result[0], 1,                 None,            datetimecreation,   datetimemodification,        datetimedestruction,       result[4],  result[5] ]
            dbaseparserto.query(sql,args)



    if True:

        # UPDATE Descriptionsystem SET id_objet = (SELECT id_objet FROM Equipement WHERE Equipement.id_descriptionsystem = Descriptionsystem.id_descriptionsystem) WHERE id_objet IS NULL

        print('*************** Descriptionsystem *************************  ')
        sql = "SELECT id_descriptionsystem, id_objet FROM Descriptionsystem"
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            if result[1] is not None:

                sqltemp = "SELECT pk_objet FROM Objet WHERE id_objet = " + str(result[1])
                resulttemp = dbaseparserto.query(sqltemp)
                if resulttemp is not None:
                    pkobjet = resulttemp[0][0]
                    sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet  ) VALUES (?,?) "
                    args = [                             result[0],             pkobjet ]
                    dbaseparserto.query(sql,args)



    if True:
        print('*************** Ressource *************************  ')
        sql = "SELECT id_ressource, source, dateressource, file, description, id_objet,lk_marche  FROM Ressource"
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sql = "SELECT pk_objet FROM Objet WHERE id_objet = " + str(result[5])
            pkobjet = dbaseparserto.query(sql)[0][0]

            sql = '''INSERT INTO Ressource (id_ressource, lpk_objet,  file,  description, lid_marche ) 
                    VALUES (?,?,?,?,?) '''
            args = [                        result[0],     pkobjet,  result[3], result[4], result[6]  ]
            dbaseparserto.query(sql,args)



# ************************************ Autre **************************************************************************

if True:
    if True:
        print('*************** Zonegeo *************************  ')
        sql = "SELECT id_zonegeo, id_objet,typezonegeo , geom  FROM Zonegeo"
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sqltemp = "SELECT pk_objet FROM Objet WHERE id_objet = " + str(result[1])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkobjet = resulttemp[0][0]

                sql = '''INSERT INTO Zonegeo (id_zonegeo, lpk_objet, typezonegeo, geom ) 
                        VALUES (?,?,?,?) '''
                args = [                        result[0],      pkobjet,  result[2], result[3]  ]
                dbaseparserto.query(sql,args)


    if True:
        print('*************** Intervenant *************************  ')
        sql = "SELECT id_intervenant, id_objet,nom, societe,adresse  FROM Intervenant"
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)


            sqltemp = "SELECT pk_objet FROM Objet WHERE id_objet = " + str(result[1])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkobjet = resulttemp[0][0]


            sql = '''INSERT INTO Intervenant (id_intervenant, lpk_objet, nom, societe, adresse ) 
                    VALUES (?,?,?,?,?) '''
            args = [                        result[0],        pkobjet,result[2], result[3],result[4]  ]
            dbaseparserto.query(sql,args)

    if True:
        print('*************** Desordre *************************  ')
        sql = '''SELECT id_desordre, id_objet,lk_descriptionsystem,  
                groupedesordre, cote, position, catdes, typedes, geom
                 FROM Desordre '''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results):
            if i % 50 == 0:
                print(result)

            if result[3] == 'OH':
                groupedes = 'EQP'
            else:
                groupedes = result[3]


            sqltemp = "SELECT pk_objet FROM Objet WHERE id_objet = " + str(result[1])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkobjet = resulttemp[0][0]


                sql = '''INSERT INTO Desordre (id_desordre, lpk_objet, 
                                groupedesordre, cote, position,catdes, typedes, lid_descriptionsystem,
                                geom   ) 
                         VALUES (?,?,?,?,?,?,?,?,?) '''
                args = [                        result[0],               pkobjet,
                                groupedes, result[4],result[5],result[6],result[7], result[2],
                            result[8]               ]
                dbaseparserto.query(sql, args)





    if True:
        print('*************** Observation *************************  ')
        sql = '''SELECT id_observation, id_objet,lk_desordre,  dateobservation,source,
                nombre, gravite, evolution, commentairesuite,   typesuite
                FROM Observation '''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sqltemp = "SELECT pk_objet FROM Objet WHERE id_objet = " + str(result[1])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkobjet = resulttemp[0][0]

                sql = '''INSERT INTO Observation (id_observation, lpk_objet, 
                          datetimeobservation,  source,  nombre,     gravite,   evolution,
                           typesuite, commentairesuite, lid_desordre  ) 
                        VALUES (?,?,?,?,?,?,?,?,?,?) '''
                args = [                        result[0],        pkobjet,
                            result[3] + ' 00:00:00', result[4],  result[5],   result[6],   result[7],
                            result[9],result[8],    result[2]               ]
                dbaseparserto.query(sql,args)

                if False:
                    if result[8]:
                        comm = result[8]
                    else:
                        comm = ''

                    sql = 'UPDATE Objet SET commentaire = ' + "'" + comm + "'" + ' WHERE id_objet = ' + str(result[1])
                    dbaseparserto.query(sql)




# ************************************ descriptionsystem **************************************************************************

if True:
    if True:
        print('*************** Infralineaire *************************  ')
        sql = '''SELECT id_infralineaire, id_objet, id_descriptionsystem, description1 ,description2,classement,aubaredelargeur ,
                aubaredevegherbacee,aubaredevegarbustive, aubaredevegarboree,aubaredecommentaire ,lk_ressource2 ,lk_ressource4  ,geom
                FROM Infralineaire'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            if False:
                #photocrete
                if result[11] is not None:
                    sql = '''SELECT id_ressource FROM Photo WHERE id_objet = ''' + str(result[11])
                    resulttemp = list(dbaseparserfrom.query(sql))
                    lk_ressource2 = resulttemp[0][0]
                    if i%50 == 0:
                        print('lk_ressource2',lk_ressource2)
                else:
                    lk_ressource2 = None

            #lien profil
            #idem lk_profil
            sqltemp = "SELECT pk_descriptionsystem FROM Descriptionsystem WHERE id_descriptionsystem = " + str(result[2])
            resulttemp = dbaseparserto.query(sqltemp)
            print(resulttemp)
            if resulttemp is not None and resulttemp[0] is not None:
                pkdessys = resulttemp[0][0]


                sql = '''INSERT INTO Infralineaire 
                        (id_infralineaire,  lpk_descriptionsystem, description1, description2,
                        classement, aubaredelargeur,aubaredevegherbacee, aubaredevegarbustive, aubaredevegarboree, aubaredecommentaire,
                         lid_ressource_2,lid_ressource_4, geom )
                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) '''
                args = [ result[0],        pkdessys,      result[3],      result[4],
                         result[5], result[6],      result[7],              result[8],          result[9],          result[10],
                         result[11],result[12],  result[13] ]

                if i%50 == 0:
                    print(sql)
                    print(args)

                dbaseparserto.query(sql,args)

    if True:
        print('*************** Equipement *************************  ')
        sql = '''SELECT id_equipement, id_objet, id_descriptionsystem, lk_descriptionsystem,
                cote, position, categorie, typeequipement, implantation, ecoulement, utilisation,
                dimverti, dimhori, securite, geom
                FROM Equipement'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results):
            if i % 50 == 0:
                print(result)
            if False:
                # lienequip
                if result[3] is not None:
                    sql = '''SELECT id_descriptionsystem FROM Equipement WHERE id_equipement = ''' + str(result[3])
                    resulttemp = list(dbaseparserfrom.query(sql))
                    lk_dessys = resulttemp[0][0]
                    if i % 50 == 0:
                        print('lk_ressource2', lk_ressource2)
                else:
                    lk_dessys = None

            # lien profil
            # idem lk_profil

            sqltemp = "SELECT pk_descriptionsystem FROM Descriptionsystem WHERE id_descriptionsystem = " + str(result[2])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkdessys = resulttemp[0][0]

                sql = '''INSERT INTO Equipement 
                        (id_equipement,   lpk_descriptionsystem, 
                        categorie, typeequipement, implantation, ecoulement, utilisation, 
                        dimverti, dimhori, securite,  cote, position, geom , lid_descriptionsystem )
                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
                args = [result[0],               pkdessys,
                        result[6],result[7],       result[8],   result[9], result[10],
                        result[11],result[12], result[13], result[4], result[5], result[14], result[3] ]

                if i % 50 == 0:
                    print(sql)
                    print(args)
                dbaseparserto.query(sql, args)

                if False:
                    if result[14]:
                        comm = result[14]
                    else:
                        comm = ''
                    sql = 'UPDATE Objet SET commentaire = ' + "'" + comm + "'" + ' WHERE id_objet = ' + str(result[1])
                    dbaseparserto.query(sql)


    if True:
        print('*************** Profil *************************  ')
        sql = '''SELECT id_profil, id_objet, id_descriptionsystem, type ,lk_descriptionsystem,  geom
                FROM Profil'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)
            if False:
                #ressource
                if result[4] is not None:
                    sql = '''SELECT id_descriptionsystem FROM Infralineaire WHERE id_objet = ''' + str(result[4])
                    resulttemp = list(dbaseparserfrom.query(sql))
                    lk_dessys = resulttemp[0][0]
                    if i%50 == 0:
                        print('lk_ressource2',lk_dessys)
                else:
                    lk_dessys = None


            sqltemp = "SELECT pk_descriptionsystem FROM Descriptionsystem WHERE id_descriptionsystem = " + str(result[2])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkdessys = resulttemp[0][0]

                sql = '''INSERT INTO Profil  
                        (id_profil,   lpk_descriptionsystem, 
                        type, lid_descriptionsystem,  geom )
                         VALUES (?,?,?,?,?) '''

                args = [ result[0],       pkdessys,
                         result[3],  result[4] ,  result[5]]

                if i%50 == 0:
                    print(sql)
                    print(args)

                dbaseparserto.query(sql,args)









# ************************************ ressoruces **************************************************************************

if True:

    if True:
        sql = '''SELECT id_photo, id_objet, id_ressource, typephoto  ,geom
                FROM Photo'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)


            sqltemp = "SELECT pk_ressource FROM Ressource WHERE id_ressource = " + str(result[2])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkress = resulttemp[0][0]

                sql = '''INSERT INTO Photo 
                        (id_photo,   lpk_ressource, typephoto, geom  )
                         VALUES (?,?,?,?) '''
                args = [ result[0],  pkress,      result[3],      result[4] ]

                if i%50 == 0:
                    print(sql)
                    print(args)

                dbaseparserto.query(sql,args)




    if True:
        sql = '''SELECT id_rasters, id_objet, id_ressource, typeraster 
                FROM Rasters'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)


            sqltemp = "SELECT pk_ressource FROM Ressource WHERE id_ressource = " + str(result[2])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkress = resulttemp[0][0]

                sql = '''INSERT INTO Rasters 
                        (id_rasters, lpk_ressource, typeraster  )
                         VALUES (?,?,?) '''
                args = [ result[0],   pkress,      result[3] ]

                if i%50 == 0:
                    print(sql)
                    print(args)

                dbaseparserto.query(sql,args)


    if True:
        sql = '''SELECT id_topographie, id_objet, id_ressource
                FROM Topographie'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sqltemp = "SELECT pk_ressource FROM Ressource WHERE id_ressource = " + str(result[2])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkress = resulttemp[0][0]

                sql = '''INSERT INTO Topographie 
                        (id_topographie, lpk_ressource  )
                         VALUES (?,?) '''
                args = [ result[0],     pkress ]

                if i%50 == 0:
                    print(sql)
                    print(args)

                dbaseparserto.query(sql,args)

    if True:
        sql = '''SELECT id_pointtopo,id_topographie, typepointtopo, zmngf, geom
                FROM Pointtopo'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sqltemp = "SELECT pk_topographie FROM Topographie WHERE id_topographie = " + str(result[1])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pktopo = resulttemp[0][0]

                sql = '''INSERT INTO Pointtopo 
                        (id_pointtopo,  lpk_topographie, typepointtopo,  zmngf, geom  )
                         VALUES (?,?,?,?,?) '''
                args = [ result[0],       pktopo,     result[2], result[3], result[4] ]

                if i%50 == 0:
                    print(sql)
                    print(args)

                dbaseparserto.query(sql,args)

    if True:
        sql = '''SELECT id_graphique, id_objet, id_ressource, typegraphique
                FROM Graphique'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sqltemp = "SELECT pk_ressource FROM Ressource WHERE id_ressource = " + str(result[2])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkress = resulttemp[0][0]

                sql = '''INSERT INTO Graphique 
                        (id_graphique,  lpk_ressource, typegraphique  )
                         VALUES (?,?,?) '''
                args = [ result[0],        pkress,result[3] ]

                if i%50 == 0:
                    print(sql)
                    print(args)

                dbaseparserto.query(sql,args)


    if True:
        sql = '''SELECT id_graphiquedata ,id_graphique, typedata, x, y, z, 
                index1, index2, index3
                FROM Graphiquedata'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sqltemp = "SELECT pk_graphique FROM Graphique WHERE id_graphique = " + str(result[1])
            resulttemp = dbaseparserto.query(sqltemp)
            if resulttemp is not None:
                pkgraph = resulttemp[0][0]

                sql = '''INSERT INTO Graphiquedata 
                        (id_graphiquedata, lpk_graphique, typedata, x, y, z,
                          index1, index2, index3  )
                         VALUES (?,?,?,?,?,?,?,?,?) '''
                args = [ result[0],    pkgraph,  result[2], result[3], result[4],result[5],
                         result[6],result[7],result[8]]

                if i%50 == 0:
                    print(sql)
                    print(args)

                dbaseparserto.query(sql,args)



# ************************************ Tc **************************************************************************

if True:

    if True:
        sql = '''SELECT  id_tcintervenant, id_tcobjet, fonction 
                FROM Tcobjetintervenant'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sql = '''INSERT INTO Tcobjetintervenant 
                    (lpk_revision_begin, lid_intervenant,  lid_objet, fonction  )
                     VALUES (?,?,?,?) '''
            args = [  1,                  result[0],  result[1],      result[2] ]

            if i%50 == 0:
                print(sql)
                print(args)

            dbaseparserto.query(sql,args)

    if True:
        sql = '''SELECT  id_tcressource, id_tcobjet
                FROM Tcobjetressource'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sql = '''INSERT INTO Tcobjetressource 
                    (lpk_revision_begin, lid_ressource,  lid_objet  )
                     VALUES (?,?,?) '''
            args = [  1,                  result[0],  result[1] ]

            if i%50 == 0:
                print(sql)
                print(args)

            dbaseparserto.query(sql,args)