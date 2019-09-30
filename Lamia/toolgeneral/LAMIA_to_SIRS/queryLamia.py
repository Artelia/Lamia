"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """


# coding=utf-8
import sqlite3
import json
import re
import copy

"""
from pyspatialite import dbapi2 as db
from pyspatialite.dbapi2 import *
"""

try:
    from pyspatialite import dbapi2 as db
    from pyspatialite.dbapi2 import *
except ImportError:
    import sqlite3
    from sqlite3 import *
    #print('spatialite not enabled')



import psycopg2

import sys
import os

class queryLamia():

    def __init__(self, path, srid, user_LAMIA, password_LAMIA, adresse_LAMIA, port_LAMIA, nom_LAMIA, type_spatialite, type_postgis):

        path_config = os.path.dirname(__file__) + '/jsonConfig/config.json'
        path_config = path_config.replace('LAMIA_to_SIRS', 'SIRS_to_LAMIA')
        self.configPATH = path_config

        self.row = ()
        self.currObj = ""
        self.srid = srid
        self.typedb=type_spatialite #True si spatialite, false sinon


        if type_spatialite :
            if sys.version_info.major == 2:
                self.connSLITE = db.connect(path)
            elif sys.version_info.major == 3:   #python 3
                self.connSLITE = qgis.utils.spatialite_connect(path)
            self.SLITEcursor = self.connSLITE.cursor()

        else :
            # connexion
            # connect to postgres for checking database existence
            connectstr = "dbname='"+ nom_LAMIA + "' user='" + user_LAMIA + "' host='" + adresse_LAMIA + "' password='" + password_LAMIA + "'"
            print(connectstr)
            self.connSLITE = psycopg2.connect(connectstr)
            self.SLITEcursor = self.connSLITE.cursor()




    """Utilise Template donne en entre pour produire autant de metaObjet que de tuple recupere dans la base Sql"""
    def createMetaObjet(self, currObj, template, query):
        #On pré-charge la query
        print(query)
        self.SLITEcursor.execute(query)
        self.currObj = currObj
        i = 0
        #petite itération pour récupèrer les tuple du yeild
        for row in self.execSql(self.SLITEcursor, 1000):

            #copie profonde necessaire sinon Python edit le template
            tmp = copy.deepcopy(template)
            self.row = row
            #Remplacement des fld: par leur valeur
            print('template avant :', tmp)
            self.addValues(tmp)
            print('template apres :',tmp)
            #On ajoute un champ id pour le convertisseur
            tmp.update({'id':self.row[-1]})
            #On yield les résultats pour les traiter de manière fluide
            yield tmp

    """Permet d'ajouter des valeurs dans le clone du template"""
    def addValues(self, obj):
        #Sélection des dict présent dans l'obj
        listIndexDict = self.getListIndexDict(obj)
        #Sélection des list présent dans l'obj
        listIndexList = self.getListIndexList(obj)

        #traitement pour les dict
        if listIndexDict is not None and len(listIndexDict) > 0 :
            for idx in listIndexDict:
                obj[idx] = self.addValues(obj[idx])

        #traitement pour les list
        if listIndexList is not None and len(listIndexList) > 0 :
            for idx in listIndexList:
                obj[idx] = self.addValues(obj[idx])

        if isinstance(obj, list):
            for i in range(0, len(obj)):
                try :
                    if 'fld:' in obj[i]:
                        tmp = obj[i].split(' ')
                        print(self.row[tmp[1]])
                        obj[i] = str(self.row[tmp[1]])
                except:
                    pass

        if isinstance(obj, dict):
            for it in obj:
                try :
                    if 'fld:' in obj[it]:
                        tmp = obj[it].split(' ')
                        if int(tmp[1]) > len(self.row)-1:
                            raise LookupError('Error on '+self.currObj+'\nNumber of SQL values :'+str(len(self.row))+' Number of fld :'+tmp[1])
                        obj[it] = str(self.row[int(tmp[1])])
                except:
                    pass
        return obj

    """Retour la liste des cles menant vers un dict"""
    def getListIndexDict(self, obj):
        ret = []
        if isinstance(obj, list):
            for i in range(0, len(obj)):
                if isinstance(obj[i], dict):
                    ret.append(i)

        if isinstance(obj, dict):
            for it in obj:
                if isinstance(obj[it], dict):
                    ret.append(it)
        return ret

    """Retour la liste des cles menant vers une list"""
    def getListIndexList(self, obj):
        ret = []
        if isinstance(obj, list):
            for i in range(0, len(obj)):
                if isinstance(obj[i], list):
                    ret.append(i)

        if isinstance(obj, dict):
            for it in obj:
                if isinstance(obj[it], list):
                    ret.append(it)
        return ret

    """Execute une commande sql en utilsant yield"""
    def execSql(self, cursor, arraysize):
        while True:
            results = cursor.fetchmany(arraysize)
            if not results:
                break
            for result in results:
                yield result

    def selectId(self, table01, table02, field01, field02, id_search):
        config = json.load(open(self.configPATH,'r'))
        query = config['Misc']['Select_cross_field'].format(table_name01 = table01, table_name02 = table02, field_name01 = field01, field_name02 = field02, id_search = id_search)
        #Ecriture de la requête dans output pour le débug
        open('output.txt','a').write(query+'\n')
        #Try catch au cas où l'on reécupère par d'id


        if self.typedb:
            try:
                return self.SLITEcursor.execute(query).fetchone()[0]
            except TypeError:
                return None
        else:
            try:
                self.SLITEcursor.execute(query)
                fetch = self.SLITEcursor.fetchone()[0]
                return fetch
            except TypeError:
                return None



    def selectClosestGeom(self, table01, table02, field01, field02, id_search):
        config = json.load(open(self.configPATH,'r'))
        query = config['Misc']['Select_using_geom'].format(table_name01 = table01, table_name02 = table02, field_name01 = field01, field_name02 = field02, id_search = id_search)
        #Ecriture de la requête dans output pour le débug
        open('output.txt','a').write(query+'\n')
        #Try catch au cas où l'on reécupère par d'id
        if self.typedb:
            try:
                return self.SLITEcursor.execute(query).fetchone()[0]
            except TypeError:
                return None
        else:
            try:
                self.SLITEcursor.execute(query)
                fetch = self.SLITEcursor.fetchone()[0]
                return fetch
            except TypeError:
                return None

def main():
    print("Class name : QueryLamia\npurpose: make SQL query to the Lamia database")

if __name__ == '__main__':
    main()
