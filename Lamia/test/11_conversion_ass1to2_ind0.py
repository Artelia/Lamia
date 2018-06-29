import os
import sys
import qgis
import qgis.gui
import qgis.utils
import shutil

from Lamia.Lamia.main.DBaseParser import DBaseParser




pathfrom = "C://000_testdigue//URBAIN//FROM//SLT.sqlite"
pathfrom = "M://FR//BOR//EE//URBAIN//4352240_87_NOBLAT_EtudeAEP_EU_EP//5_Etude//01_SIG//sqlite//Saint_Paul.sqlite"
pathfrom = "I://URBAIN//4352260_87_ELAN_EtudeAEP_EU//5_Etude//01_SIG//Qgs//SQLITE//Nantiat.sqlite"
pathfrom = "C://000_testdigue//URBAIN//autre//SLT.sqlite"
#pathfrom = "C://000_testdigue//URBAIN//autre//St_Jouvent.sqlite"

dbaseparserfrom = DBaseParser(None)
dbaseparserfrom.loadQgisVectorLayers(pathfrom)

pathto = "C://000_testdigue//URBAIN//TO//SLT.sqlite"
pathto = "M://FR//BOR//EE//URBAIN//4352240_87_NOBLAT_EtudeAEP_EU_EP//5_Etude//01_SIG//sqlite//Saint_Paul1.sqlite"
pathto = "I://URBAIN//4352260_87_ELAN_EtudeAEP_EU//5_Etude//01_SIG//Qgs//SQLITE//Nantiat3.sqlite"
pathto = "C://000_testdigue//URBAIN//autre//SLT1.sqlite"
#pathto = "C://000_testdigue//URBAIN//autre//St_Jouvent1.sqlite"


originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'DBase_ind0.sqlite')
shutil.copyfile(originalfile, pathto)

dbaseparserto= DBaseParser(None)
dbaseparserto.createDbase(file=pathto, crs=2154, type='Base_assainissement', dbasetype='spatialite',
                       dbaseressourcesdirectory=None)




# ************************************ MAIN **************************************************************************
if True:
    if False:
        sql = "SELECT metier, repertoireressources, crs FROM Basedonnees"
        results = list(dbaseparserfrom.query(sql))
        for result in results :
            print(result)
            sql = "INSERT INTO Basedonnees ( repertoireressources, crs) VALUES (?,?) "
            args = [result[1],  result[2]]
            dbaseparserto.query(sql,args)



    if True:
        sql = "SELECT id_objet, datecreation, datemodification, datedestruction, commentaire, libelle FROM Objet"
        result = list(dbaseparserfrom.query(sql))
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)
            sql = "INSERT INTO Objet (id_objet,id_revisionbegin, id_revisionend, datecreation,datemodification,datedestruction, commentaire, libelle  ) VALUES (?,?,?,?,?,?,?,?) "
            args = [                  result[0], 1,             None,            result[1],   result[2],        result[3],       result[4],  result[5] ]
            dbaseparserto.query(sql,args)



    if True:
        print('*************** Descriptionsystem *************************  ')
        sql = "SELECT id_descriptionsystem, id_objet FROM Descriptionsystem"
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)
            sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, id_objet,id_revisionbegin  ) VALUES (?,?,?) "
            args = [                             result[0],             result[1],  1 ]
            dbaseparserto.query(sql,args)



    if True:
        print('*************** Ressource *************************  ')
        sql = "SELECT id_ressource, source, dateressource, file, description, id_objet,lk_marche  FROM Ressource"
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)
            sql = '''INSERT INTO Ressource (id_ressource, id_revisionbegin, id_objet,  file,  description, lk_marche ) 
                    VALUES (?,?,?,?,?,?) '''
            args = [                        result[0],      1,             result[5],  result[3], result[4], result[6]  ]
            dbaseparserto.query(sql,args)



# ************************************ Autre **************************************************************************

if True:
    if False:
        print('*************** Zonegeo *************************  ')
        sql = "SELECT id_zonegeo, id_objet,type_zonegeo, nom , geom  FROM Zonegeo"
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)
            sql = '''INSERT INTO Zonegeo (id_zonegeo,id_revisionbegin, id_objet, typezonegeo, geom ) 
                    VALUES (?,?,?,?,?) '''
            args = [                        result[0],      1,         result[1],  result[2], result[4]  ]
            dbaseparserto.query(sql,args)


    if False:
        print('*************** Intervenant *************************  ')
        sql = "SELECT id_intervenant, id_objet,nom, societe,adresse  FROM Intervenant"
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)
            sql = '''INSERT INTO Intervenant (id_intervenant,id_revisionbegin, id_objet, nom, societe, adresse ) 
                    VALUES (?,?,?,?,?,?) '''
            args = [                        result[0],      1,                result[1],result[2], result[3],result[4]  ]
            dbaseparserto.query(sql,args)

    if True:
        print('*************** Desordre *************************  ')
        sql = '''SELECT id_desordre, id_objet,lk_descriptionsystem,  
                groupedesordre, geom
                 FROM Desordre '''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results):
            if i % 50 == 0:
                print(result)

            if result[3] == 'NOE':
                groupedes = 'NOD'
            else:
                groupedes = result[3]

            sql = '''INSERT INTO Desordre (id_desordre,id_revisionbegin, id_objet, 
                            groupedesordre, lk_descriptionsystem,
                            geom   ) 
                     VALUES (?,?,?,?,?,?) '''
            args = [                        result[0], 1,                result[1],
                            groupedes, result[2],
                        result[4]               ]
            dbaseparserto.query(sql, args)





    if True:
        print('*************** Observation *************************  ')
        sql = '''SELECT id_observation, id_objet,lk_desordre, 
                 dateobservation, source, nombre, gravite, evolution, commentaires,
                 depots,  typesuite, precisionsuite, suite,
                 ECPPdepuisbranchement, gcdegrade, infiltration, intrusionracine, miseencharge, tamponendommage
                FROM Observation '''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sql = '''INSERT INTO Observation (id_observation,id_revisionbegin, id_objet, lk_desordre ,
                      dateobservation,  source,  nombre,     gravite,   evolution,
                       depots, typesuite, precisionsuite, commentairesuite, 
                        ECPPdepuisbranchement, gcdegrade, infiltration, intrusionracine, miseencharge, tamponendommage ) 
                    VALUES (?,?,?,?,?,?,?,?,?,?, ?,?,?,?,?,?,?,?,?) '''
            args = [                        result[0],      1,                result[1], result[2],
                        result[3], result[4],  result[5],   result[6],   result[7],
                        result[9],result[10],result[11],    result[12],
                        result[13],         result[14],    result[15]  ,  result[16]      ,result[17], result[18]  ]
            dbaseparserto.query(sql,args)





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

        sql = '''SELECT id_infralineaire, id_objet, id_descriptionsystem, 
                materiau, diametreNominal, formecanalisation, hauteur, branchement, modeCirculation,
                typeReseau, profamont, profaval, lk_noeud1, lk_noeud2,
                geom
                FROM Infralineaire'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sql = '''INSERT INTO Infralineaire 
                    (id_infralineaire, id_revisionbegin,  id_objet, id_descriptionsystem, 
                    materiau, diametreNominal, formecanalisation, hauteur,branchement, modeCirculation,
                    typeReseau, profamont, profaval,lk_descriptionsystem1,lk_descriptionsystem2,
                     geom )
                     VALUES (?,?,?,?,?,?,?,?,?,? ,?,?,?,?,?,?) '''
            args = [ result[0],         1,                  result[1],  result[2],
                     result[3],      result[4], result[5],   result[6],      result[7],   result[8],
                     result[9], result[10],result[11],result[12],result[13],
                     result[14] ]

            if i%50 == 0:
                print(sql)
                print(args)

            dbaseparserto.query(sql,args)



    if True:
        print('*************** Noeud  *************************  ')


        sql = '''SELECT id_noeud, id_objet, id_descriptionsystem, 
                profradierouvrage, typeReseau, typeOuvrageAss, accessibilite,cloisonsiphoide,
                X,dX,Y,dY,Z,dZ,
                geom
                FROM Noeud'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sql = '''INSERT INTO Noeud 
                    (id_noeud, id_revisionbegin,  id_objet, id_descriptionsystem, 
                    profradierouvrage, typeReseau, typeOuvrageAss, accessibilite,cloisonsiphoide,
                    X,dX,Y,dY,Z,dZ,
                    geom )
                     VALUES (?,?,?,?,?,?,?,?,?,? ,?,?,?,?,?,?) '''

            #typeouvrage
            if result[5] is not None:
                if len(str(result[5]))==1:
                    typeOuvrageAss = str(result[5]) + '0'
                else:
                    typeOuvrageAss = str(result[5])
            else:
                typeOuvrageAss = None

            args = [ result[0],         1,                  result[1],  result[2],
                     result[3],      result[4],      typeOuvrageAss,      result[6],      result[7],
                     result[8], result[9], result[10],result[11],result[12],result[13],
                     result[14] ]

            if i%50 == 0:
                print(sql)
                print(args)

            dbaseparserto.query(sql,args)



    if True:
        print('*************** Equipement *************************  ')
        sql = '''SELECT id_equipement, id_objet, id_descriptionsystem, lk_descriptionsystem,
                typeReseau, typeAppAss, commentaireequipement, ST_AsText(geom)
                FROM Equipement'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results):
            if i % 50 == 0:
                print(result)



            """
            # lienequip
            if result[3] is not None:
                sql = '''SELECT id_descriptionsystem FROM Equipement WHERE id_equipement = ''' + str(result[3])
                resulttemp = list(dbaseparserfrom.query(sql))
                lk_dessys = resulttemp[0][0]
                if i % 50 == 0:
                    print('lk_ressource2', lk_dessys)
            else:
                lk_dessys = None
            """
            # lien profil
            # idem lk_profil

            #geom
            # print(result[7])
            geom1 = qgis.core.QgsGeometry.fromWkt(result[7]).asPoint()
            # print(geom1)
            geomline = qgis.core.QgsGeometry.fromPolyline([geom1, geom1])

            geomlinewkt = geomline.exportToWkt()

            geomlinewfb = geomline.asWkb()

            # print('tt',geomlinewkt)

            #print('tot', qgis.core.QgsGeometry.fromWkb(geomlinewfb).exportToWkt() )

            sql = '''INSERT INTO Equipement 
                    (id_equipement, id_revisionbegin,  id_objet, id_descriptionsystem, lk_descriptionsystem,
                    categorie, typeReseau,typeAppAss )
                     VALUES (?,?,?,?,?,?,?,?) '''
            args = [result[0],   1,                 result[1],      result[2],          result[3],
                    'NOD', result[4] , result[5] ]
            dbaseparserto.query(sql,args)


            sql = "UPDATE  Equipement SET geom = ST_GeomFromText('" + str(geomlinewkt) + "',2154) "
            sql += " WHERE id_equipement = " + str(result[0])
            dbaseparserto.query(sql)

            if result[6]:
                sql = 'UPDATE Objet SET commentaire = ' + "'" + str(result[6]) + "'" + ' WHERE id_objet = ' + str(result[1])
                dbaseparserto.query(sql)

            if i % 50 == 0:
                print(sql)
                print(args)
            #dbaseparserto.query(sql, args)


    if False:
        print('*************** Profil *************************  ')
        sql = '''SELECT id_profil, id_objet, id_descriptionsystem, type ,lk_objet,  geom
                FROM Profil'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            #ressource
            if result[4] is not None:
                sql = '''SELECT id_descriptionsystem FROM Infralineaire WHERE id_objet = ''' + str(result[4])
                resulttemp = list(dbaseparserfrom.query(sql))
                lk_dessys = resulttemp[0][0]
                if i%50 == 0:
                    print('lk_ressource2',lk_dessys)
            else:
                lk_dessys = None


            sql = '''INSERT INTO Profil  
                    (id_profil, id_revisionbegin,  id_objet, id_descriptionsystem, 
                    type, lk_descriptionsystem,  geom )
                     VALUES (?,?,?,?,?,?,?) '''

            args = [ result[0],         1,                  result[1],  result[2],
                     result[3],  lk_dessys ,  result[5]]

            if i%50 == 0:
                print(sql)
                print(args)

            dbaseparserto.query(sql,args)









# ************************************ ressoruces **************************************************************************

if True:

    if True:
        sql = '''SELECT id_photo, id_objet, id_ressource, typephoto  ,numphoto, geom 
                FROM Photo'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sql = '''INSERT INTO Photo 
                    (id_photo, id_revisionbegin,  id_objet, id_ressource, typephoto, geom  )
                     VALUES (?,?,?,?,?,?) '''
            args = [ result[0],         1,        result[1],  result[2],    result[3],result[5] ]
            dbaseparserto.query(sql, args)

            if result[4]:
                sql = 'UPDATE Ressource SET numphoto = ' + str(result[4])  + ' WHERE id_ressource = ' + str(result[2])
                dbaseparserto.query(sql)




            if i%50 == 0:
                print(sql)
                print(args)







    if True:
        sql = '''SELECT id_rasters, id_objet, id_ressource, typeraster 
                FROM Rasters'''
        results = list(dbaseparserfrom.query(sql))
        for i, result in enumerate(results) :
            if i%50 == 0:
                print(result)

            sql = '''INSERT INTO Rasters 
                    (id_rasters, id_revisionbegin,  id_objet, id_ressource, typeraster  )
                     VALUES (?,?,?,?,?) '''
            args = [ result[0],         1,                  result[1],  result[2],      result[3] ]

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

            sql = '''INSERT INTO Topographie 
                    (id_topographie, id_revisionbegin,  id_objet, id_ressource  )
                     VALUES (?,?,?,?) '''
            args = [ result[0],         1,                  result[1],  result[2] ]

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

            sql = '''INSERT INTO Pointtopo 
                    (id_pointtopo, id_revisionbegin, id_topographie, typepointtopo,  zmngf, geom  )
                     VALUES (?,?,?,?,?,?) '''
            args = [ result[0],         1,                  result[1],  result[2], result[3], result[4] ]

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

            sql = '''INSERT INTO Graphique 
                    (id_graphique, id_revisionbegin,  id_objet, id_ressource, typegraphique  )
                     VALUES (?,?,?,?,?) '''
            args = [ result[0],         1,                  result[1],  result[2] ,result[3] ]

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

            sql = '''INSERT INTO Graphiquedata 
                    (id_graphiquedata, id_revisionbegin, id_graphique, typedata, x, y, z,
                      index1, index2, index3  )
                     VALUES (?,?,?,?,?,?,?,?,?,?) '''
            args = [ result[0],         1,                  result[1],  result[2], result[3], result[4],result[5],
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
                    (id_revisionbegin, id_tcintervenant,  id_tcobjet, fonction  )
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
                    (id_revisionbegin, id_tcressource,  id_tcobjet  )
                     VALUES (?,?,?) '''
            args = [  1,                  result[0],  result[1] ]

            if i%50 == 0:
                print(sql)
                print(args)

            dbaseparserto.query(sql,args)