# -*- coding: utf-8 -*-

from pyspatialite import dbapi2 as db
import qgis
import os
import psycopg2

def convertstring(str):
    temp = str.split("'")
    return ' '.join(temp)



uri = qgis.core.QgsDataSourceURI()

# file = 'C:\\000_testimportBM\\source\\VTA_final_ind0.sqlite'
# file = 'C:\\000_testimportBM\\source\\vta_begles.sqlite'
file = 'C:\\000_testimportBM\\source\\VTA_RD_ind0.sqlite'

# fileto = 'C:\\Users\\patrice.verchere\\Documents\\GitHub\\InspectionDigueV2\\import\\Vta_imported.sqlite'
fileto = 'C:\\000_testimportBM\\BD_BM_ind1.sqlite'


spatialitefilefrom = file
connSLITEfrom = db.connect(file)
SLITEcursorfrom = connSLITEfrom.cursor()


connectstr = "dbname='PVR_test'  user='postgres' host='localhost' password='PVR'"
connPGis = psycopg2.connect(connectstr)
PGiscursor = connPGis.cursor()
sql = 'SET search_path TO exportBM ,public'



if False:
    sql = 'DELETE FROM Objet'
    SLITEcursorto.execute(sql)
    connSLITEto.commit()
    sql = "DELETE FROM sqlite_sequence WHERE name = 'Objet'"
    SLITEcursorto.execute(sql)
    connSLITEto.commit()


    sql = 'DELETE FROM Descriptionsystem'
    SLITEcursorto.execute(sql)
    connSLITEto.commit()
    sql = "DELETE FROM sqlite_sequence WHERE name = 'Descriptionsystem'"
    SLITEcursorto.execute(sql)
    connSLITEto.commit()

    sql = 'DELETE FROM Infralineaire'
    SLITEcursorto.execute(sql)
    connSLITEto.commit()
    sql = "DELETE FROM sqlite_sequence WHERE name = 'Infralineaire'"
    SLITEcursorto.execute(sql)
    connSLITEto.commit()

    sql = 'DELETE FROM Equipement'
    SLITEcursorto.execute(sql)
    connSLITEto.commit()
    sql = "DELETE FROM sqlite_sequence WHERE name = 'Equipement'"
    SLITEcursorto.execute(sql)
    connSLITEto.commit()

    sql = 'DELETE FROM Desordre'
    SLITEcursorto.execute(sql)
    connSLITEto.commit()
    sql = "DELETE FROM sqlite_sequence WHERE name = 'Desordre'"
    SLITEcursorto.execute(sql)
    connSLITEto.commit()

    sql = 'DELETE FROM Tcdesordredescriptionsystem'
    SLITEcursorto.execute(sql)
    connSLITEto.commit()
    sql = "DELETE FROM sqlite_sequence WHERE name = 'Tcdesordredescriptionsystem'"
    SLITEcursorto.execute(sql)
    connSLITEto.commit()

    sql = 'DELETE FROM Observation'
    SLITEcursorto.execute(sql)
    connSLITEto.commit()
    sql = "DELETE FROM sqlite_sequence WHERE name = 'Observation'"
    SLITEcursorto.execute(sql)
    connSLITEto.commit()

    sql = 'DELETE FROM Photo'
    SLITEcursorto.execute(sql)
    connSLITEto.commit()
    sql = "DELETE FROM sqlite_sequence WHERE name = 'Photo'"
    SLITEcursorto.execute(sql)
    connSLITEto.commit()

    sql = 'DELETE FROM Tcobjetressource'
    SLITEcursorto.execute(sql)
    connSLITEto.commit()
    sql = "DELETE FROM sqlite_sequence WHERE name = 'Tcobjetressource'"
    SLITEcursorto.execute(sql)
    connSLITEto.commit()


sql = 'PRAGMA encoding="UTF-8";'
SLITEcursorto.execute(sql)
connSLITEto.commit()


print('# ******************************************************************************************')
print('# structure')

if False:


    tcstructureinfralin = []

    sql = 'SELECT id, dig_id, NOM, COMMENTAIR, AsText(geoml) FROM structures'
    query = list(SLITEcursorfrom.execute(sql))
    resultstructures = [list(row) for row in query]
    # print(resultstructures)

    for i, result in enumerate(resultstructures) :
        # print result

        if i%50 ==0:
            print(result)

        if result[3] is not None and  "'"  in result[3]:
            result[3] = convertstring(result[3])

        sql = "INSERT INTO Objet(datecreation, commentaire,libelle) VALUES('2017-11-15','" + unicode(result[2]) + "','" + unicode(result[3]) + "');"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        idobj = [row[0] for row in query][0]

        tcstructureinfralin.append([result[0], idobj])

        sql = "INSERT INTO Descriptionsystem DEFAULT VALUES;"
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        iddessys = [row[0] for row in query][0]

        sql = "INSERT INTO Infralineaire(id_objet,id_descriptionsystem,geom) VALUES(" + str(idobj) + "," + str(iddessys) + ",ST_LineMerge(GeomFromText('" + str(result[4]) + "',3945)) );"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()


print('# ******************************************************************************************')
print('# equipement ')

if False:
    sql = 'SELECT id, interv, date, source, cote, categorie, type, diametre, ecoulement, utilisatio, hauteur, LK_TR,  AsText(geoml), AsText(geomp) FROM reseaux'
    print(sql)
    query = list(SLITEcursorfrom.execute(sql))
    resultreseaux = [list(row) for row in query]
    # print(resultreseaux)
    tcreseauxequipement = []

    for i, result in enumerate(resultreseaux):
        # print result
        if i % 50 == 0:
            print(result)

        sql = "INSERT INTO Objet(datecreation)  VALUES('2017-11-15') ;"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        idobj = [row[0] for row in query][0]

        tcreseauxequipement.append([result[0], idobj])

        sql = "INSERT INTO Descriptionsystem DEFAULT VALUES;"
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        iddessys = [row[0] for row in query][0]



        sql = "INSERT INTO Equipement(cote, categorie, type, utilisation, dimverti, dimhori,id_objet, id_descriptionsystem, geom )"
        sql += "VALUES('" + str(result[4]) + "','" + str(result[5]) + "','" + str(result[6]) + "','" + str(result[9])
        sql += "'," + str(result[7]) + "," + str(result[10]) + "," + str(idobj) + "," + str(iddessys)
        if result[12] is None:
            point = result[13].split('(')[1][:-1]
            geomtoset = ",GeomFromText('LINESTRING(" + point + "," + point + ")', 3945 ));"
        else:
            geomtoset = ", ST_LineMerge(GeomFromText('" + str(result[12])  + "',3945)));"


        sql +=  geomtoset
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()

print('# ******************************************************************************************')
print('# equipement spe')


if False:
    sql = 'SELECT id, interventi, date, source, cote, categorie, type, res_id, secu, commentair, TR_ID,  AsText(geomP) FROM reseaux_spe'
    print(sql)
    query = list(SLITEcursorfrom.execute(sql))
    resultreseaux = [list(row) for row in query]
    # print(resultreseaux)
    tcreseauxspeequipement = []

    for i, result in enumerate(resultreseaux):
        # print result
        if i % 50 == 0:
            print(result)

        sql = "INSERT INTO Objet(datecreation)  VALUES('2017-11-15') ;"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        idobj = [row[0] for row in query][0]

        tcreseauxspeequipement.append([result[0], idobj])

        sql = "INSERT INTO Descriptionsystem DEFAULT VALUES;"
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        iddessys = [row[0] for row in query][0]

        if result[9] is not None and  "'"  in result[9]:
            result[9] = convertstring(result[9])

        if result[6] == 'CAR':
            result[6] = 'PON'
        elif result[6] == 'PAF':
            result[6] = 'CLA'
        elif result[6] == 'STP':
            result[6] = 'POS'

        if result[8] == -1:
            result[8] = 'NULL'

        sql = "INSERT INTO Equipement(cote, categorie, type, securite,comment ,id_objet, id_descriptionsystem, geom )"
        sql += " VALUES('" + str(result[4]) + "','" + str(result[5]) + "','" + str(result[6]) + "','" + str(result[8]) + "','" + unicode(result[9])
        sql += "'," + str(idobj) + "," + str(iddessys)


        point = result[11].split('(')[1][:-1]
        geomtoset = ",GeomFromText('LINESTRING(" + point + "," + point + ")', 3945 ));"


        sql += geomtoset
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()



print(' ******************************************************************************************')
print('# deosrdre')


if False:
    sql = 'SELECT id, cote, position, type_des, lk_type, lk_id, AsText(geoml), AsText(geomp) FROM desordres'
    print(sql)
    query = list(SLITEcursorfrom.execute(sql))
    resultreseaux = [list(row) for row in query]
    # print(resultreseaux)
    tcdesordre = []

    for i, result in enumerate(resultreseaux):
        # print result
        if i % 50 == 0:
            print(result)

        sql = "INSERT INTO Objet(datecreation)  VALUES('2017-11-15') ;"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        idobj = [row[0] for row in query][0]

        tcdesordre.append([result[0], idobj])

        sql = "INSERT INTO Descriptionsystem DEFAULT VALUES;"
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        iddessys = [row[0] for row in query][0]

        #catdes
        typedes = result[3]
        if typedes == 'TRR':
            typedes = 'TER'
        elif typedes == 'ORN':
            typedes = 'PAS'
        elif typedes == 'PEF':
            typedes = 'MVT'


        if typedes in ['TER','CHS','DEP']:
            catdes = 'ERI'
        elif typedes in ['VEG','DSA']:
            catdes = 'ENT'
        elif typedes in ['COR','DES','MVT','FIS','PTB','PRV','DEJ']:
            catdes = 'DAF'
        elif typedes in ['ARR','PIE','ERF']:
            catdes = 'ERX'


        sql = "INSERT INTO Desordre(cote, position, catdes, typedes, id_objet, geom )"
        sql += " VALUES('" + str(result[1]) + "','" + str(result[2]) + "','" + str(catdes) + "','" + str(typedes)
        sql += "'," + str(idobj)

        if result[6] is None:
            point = result[7].split('(')[1][:-1]
            geomtoset = ",GeomFromText('LINESTRING(" + point + "," + point + ")', 3945 ));"
        else:
            geomtoset = ", ST_LineMerge(GeomFromText('" + str(result[6])  + "',3945)));"

        sql += geomtoset
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()

        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        iddesordre = [row[0] for row in query][0]

        # Tcdesordredescriptionsystem
        # print('lk',result[4], result[5])
        if result[4] == 'STR':
            listidfrom = [elem[0] for elem in tcstructureinfralin]
            index = listidfrom.index(int(result[5]))
            idobjet = tcstructureinfralin[index][1]
            sql = "SELECT id_descriptionsystem FROM Infralineaire_view WHERE id_objet = " + str(idobjet)
            # print(sql)

        elif result[4] == 'RSP':
            listidfrom = [elem[0] for elem in tcreseauxspeequipement]
            index = listidfrom.index(int(result[5]))
            idobjet = tcreseauxspeequipement[index][1]
            sql = "SELECT id_descriptionsystem FROM Equipement_view WHERE id_objet = " + str(idobjet)
            # print(sql)

        #iddessy

        query = list(SLITEcursorto.execute(sql))
        # print('res',[row[0] for row in query])
        iddessys = [row[0] for row in query][0]

        sql = "INSERT INTO Tcdesordredescriptionsystem(id_tcdesordre, id_tcdescriptionsystem) "
        sql += "VALUES("+str(iddesordre) + "," + str(iddessys) + ");"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()

print(' ******************************************************************************************')
print('# desordres_obs')

if False:
    #              0                     4                  6
    sql = 'SELECT id,des_id,date,source, urgence,nombre_des,commentair, evolution, SUITE FROM desordres_obs'
    print(sql)
    query = list(SLITEcursorfrom.execute(sql))
    resultreseaux = [list(row) for row in query]
    # print(resultreseaux)
    tcobservation = []

    for i, result in enumerate(resultreseaux):
        # print result
        if i % 50 == 0:
            print(result)

        # cherche lk_desordre
        listidfrom = [elem[0] for elem in tcdesordre]
        try:
            index = listidfrom.index(int(result[1]))
        except ValueError:
            continue
        idlkobjet = tcdesordre[index][1]


        sql = "INSERT INTO Objet(datecreation)  VALUES('2017-11-15') ;"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        idobj = [row[0] for row in query][0]

        tcobservation.append([result[0], idobj])


        sql = "SELECT id_desordre FROM Desordre_view WHERE id_objet = " + str(idlkobjet)
        query = list(SLITEcursorto.execute(sql))
        idlkdesordre = [row[0] for row in query][0]

        if result[8] is not None and  "'"  in result[8]:
            result[8] = convertstring(result[8])

        if result[6] is not None and  "'"  in result[6]:
            result[6] = convertstring(result[6])

        if result[4] is not None :
            if int(result[4]) -1 >= 0:
                result[4] = str(int(result[4])-1)
            else:
                result[4] = ''

        sql = "INSERT INTO Observation(date, nombre,urgence,evolution,commentaires,suite,id_objet, lk_desordre )"
        sql += " VALUES('" + str(result[2]) + "'," + str(result[5]) + ",'" + str(result[4]) + "','" + str(result[7])
        sql += "','" + unicode(result[6]) + "','" + unicode(result[8]) + "'," + str(idobj) + "," + str(idlkdesordre)
        sql += ");"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()

print(' ******************************************************************************************')
print('# photos')

if False:
    #              0                   4                     6
    sql = 'SELECT id,date,source,cote, orientatio,observatio,chemin_fic,lk_type,lk_id ,AsText(geomp) FROM photographies'
    print(sql)
    query = list(SLITEcursorfrom.execute(sql))
    resultphoto = [list(row) for row in query]
    # print(resultreseaux)
    tcphoto = []

    for i, result in enumerate(resultphoto):
        # print result
        if i % 50 == 0:
            print(result)

        sql = "INSERT INTO Objet(datecreation)  VALUES('2017-11-15') ;"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        idobj = [row[0] for row in query][0]

        tcphoto.append([result[0], idobj])

        if result[5] is not None and  "'"  in result[5]:
            result[5] = convertstring(result[5])

        #file
        # file = 'C:\\000_testimportBM\\source\\VTA_final_ind0.sqlite'
        # file = 'C:\\000_testimportBM\\source\\vta_begles.sqlite'
        if file == 'C:\\000_testimportBM\\source\\vta_begles.sqlite':
            newlocationfile = os.path.join('.','Photo','20171116', os.path.basename(result[6]))
        elif file == 'C:\\000_testimportBM\\source\\VTA_final_ind0.sqlite':
            newlocationfile = os.path.join('.','Photo','20171115', os.path.basename(result[6]))
        elif file =='C:\\000_testimportBM\\source\\VTA_RD_ind0.sqlite':
            newlocationfile = os.path.join('.', 'Photo', '20171117', os.path.basename(result[6]))

        sql = "INSERT INTO Ressource(file,description, date, id_objet) "
        sql += "VALUES('" + str(newlocationfile) + "','" + unicode(result[5])+ "','" + str(result[1])+ "'," + str(idobj) + ");"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()
        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        idressource = [row[0] for row in query][0]

        sql = "INSERT INTO Photo (id_objet, id_ressource,data_type,  geom )"
        sql += " VALUES(" + str(idobj) + "," + str(idressource) + ",'PHO',"
        sql += "GeomFromText('" +str(result[9]) + "',3945));"
        # print(sql)
        SLITEcursorto.execute(sql)
        connSLITEto.commit()

        sql = 'SELECT last_insert_rowid()'
        query = SLITEcursorto.execute(sql)
        idphoto = [row[0] for row in query][0]

        if True:

            # Tcdesordredescriptionsystem
            # print('lk',result[4], result[5])
            if result[7] == 'STR':
                listidfrom = [elem[0] for elem in tcstructureinfralin]
                if int(result[8]) >= 0:
                    index = listidfrom.index(int(result[8]))
                    if index >= 0 :
                        idobjet = tcstructureinfralin[index][1]
                    else:
                        continue
                    # sql = "SELECT id_descriptionsystem FROM Infralineaire_view WHERE id_objet = " + str(idobjet)
                    # print(sql) Tcobjetressource
                else:
                    continue


            elif result[7] == 'OBS':
                listidfrom = [elem[0] for elem in tcobservation]
                if int(result[8]) >= 0:
                    try:
                        index = listidfrom.index(int(result[8]))
                    except ValueError:
                        print('valuerror')
                        continue
                    if index >= 0 :
                        idobjet = tcobservation[index][1]
                    else:
                        continue
                else:
                    continue
                # sql = "SELECT id_descriptionsystem FROM Equipement_view WHERE id_objet = " + str(idobjet)
                # print(sql)

            elif result[7] == 'RSP':
                listidfrom = [elem[0] for elem in tcreseauxspeequipement]
                if int(result[8]) >= 0:
                    try:
                        index = listidfrom.index(int(result[8]))
                    except ValueError:
                        print('valuerror')
                        continue
                    if index >= 0:
                        idobjet = tcreseauxspeequipement[index][1]
                    else:
                        continue
                else:
                    continue

            elif result[7] == '':
                continue

            # iddessy
            """
            query = list(SLITEcursorto.execute(sql))
            # print('res',[row[0] for row in query])
            iddessys = [row[0] for row in query][0]
            """

            sql = "INSERT INTO Tcobjetressource(id_tcoobjet, id_tcressource) "
            sql += "VALUES(" + str(idobjet) + "," + str(idressource) + ");"
            # print(sql)
            SLITEcursorto.execute(sql)
            connSLITEto.commit()




# ******************************************************************************************
# fin



SLITEcursorfrom.close()
SLITEcursorto.close()
connSLITEto.close()
connSLITEfrom.close()


print('end')