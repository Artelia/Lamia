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

        self.configPATH = os.path.join(os.path.dirname(__file__), 'jsonConfig/config.json')
        self.swapPATH = os.path.join(os.path.dirname(__file__), 'jsonConfig/swapping.json')
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



    def commit(self):
        self.connSLITE.commit()

    def disconnect(self):
        self.connSLITE.close()

    """
    Insert a new object with all his dependencies into the database
    """
    def insertion(self, type, obj):
        listDict = self.getListDict(obj)
        listAttr = self.getListAttributs(obj)
        if len(listDict) > 0:
            for it in listDict:
                listAttr[it] = self.insertion(it, listDict[it])
        if len(listAttr) == 1 and type in listAttr:
            return listAttr[type]
        return self.execSql(type, listAttr)

    """
    Get all the elements of type Dict  present in obj
    :param obj: dict
    :rtype: list of string
    """
    def getListDict(self, obj):
        ret = {}
        for it in obj:
            if isinstance(obj[it], dict):
                ret[it] = obj[it]
        else:
            return ret

    """
    Get all the elements of type String or int present in obj
    :param obj: dict
    :rtype: list of string or int
    """
    def getListAttributs(self, obj):
        ret = {}
        for it in obj:
            if isinstance(it, unicode) or isinstance(it, int):
                ret[it] = obj[it]
        else:
            return ret

    """
    Execute an sql query using an external json file
    :param key: string
    :param values: Dict
    :rtype: the id of the last inserted row
    """
    def execSql(self, key, values):
        config = json.load(open(self.configPATH,'r'))
        swap = json.load(open(self.swapPATH, 'r'))

        for val in values:
            if val in swap:
                values[val] = swap[val]['back']+''+re.search(swap[val]['regex'], str(values[val])).group()+''+swap[val]['front']


        tmp = []
        for id in sorted(values):
            tmp.append(values[id])
        values = tmp
        del tmp

        print(values)

        if ' ' in key:
            key = self.formatKey(key.split(' '))


        query_to_run = config[key]['query_sql']

        query_to_run=query_to_run.replace('2154',self.srid)



        #self.SLITEcursor.execute(config[key]['query_sql'], values)

        for value in values :
            query_to_run=query_to_run.replace('?',"'"+str(value)+"'",1)

        print('1 :', query_to_run)

        if self.typedb:
            self.SLITEcursor.execute(query_to_run)

            try:
                fetch = self.SLITEcursor.lastrowid
            except TypeError:
                fetch = 0
            return fetch

        else:
            try :
                query_to_run = query_to_run+ "RETURNING id_"+query_to_run[query_to_run.find("O")+2:query_to_run[query_to_run.find("O")+2:].find("(")+2+query_to_run.find("O")]
                print(query_to_run)
                self.SLITEcursor.execute(query_to_run)
                fetch = self.SLITEcursor.fetchone()[0]
            except :
                print("erreur !", query_to_run)
                self.SLITEcursor.execute(query_to_run)
                fetch = 0
            return fetch

    """
    format the key to a more standard string
    :param key: string
    :rtype: string
    """
    def formatKey(self, key):
        for word in key:
            if re.match('[A-Z][a-z]+',word):
                return word
        return key

    """
    Update the dependencies using the different arguments given in entry
    :param table: string - the table to inject on
    :param field: string - the field to inject on
    :param id_lm_field: int - the id of the row to inject on
    :param id_lm_src: int - the id to put inject
    :rtype: None
    """
    def updateDependencies(self, table01, field01, field02, value, id_search):
        config = json.load(open(self.configPATH,'r'))
        query = config['Misc']['Update_using_id'].format(table_name01=table01, field_name01=field01, field_name02=field02, value=value, id_search=id_search)
        open('output.txt','a').write(query+'\n')
        print('2 :', query)
        self.SLITEcursor.execute(query)

    def selectId(self, table01, field01, field02, id_search):
        config = json.load(open(self.configPATH,'r'))
        query = config['Misc']['Select_using_id'].format(table_name01 = table01, field_name01 = field01, field_name02 = field02, id_search = id_search)
        open('output.txt','a').write(query+'\n')
        print('3 :',query )

        if self.typedb:
            return self.SLITEcursor.execute(query).fetchone()[0]

        else:
            self.SLITEcursor.execute(query)
            fetch = self.SLITEcursor.fetchone()[0]
            return fetch


def main():
    print("Class name : QueryLamia\npurpose: make SQL query to the Lamia database")

if __name__ == '__main__':
    main()
