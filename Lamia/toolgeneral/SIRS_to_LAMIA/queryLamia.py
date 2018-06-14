import sqlite3
import json
import re

from pyspatialite import dbapi2 as db
from pyspatialite.dbapi2 import *
import sys
import os

class queryLamia():

    def __init__(self, path):
        if sys.version_info.major == 2:
            self.connSLITE = db.connect(path)
        elif sys.version_info.major == 3:   #python 3
            self.connSLITE = qgis.utils.spatialite_connect(path)
        self.SLITEcursor = self.connSLITE.cursor()
        self.configPATH = os.path.join(os.path.dirname(__file__), 'jsonConfig/config.json')
        self.swapPATH = os.path.join(os.path.dirname(__file__), 'jsonConfig/swapping.json')

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

        self.SLITEcursor.execute(config[key]['query_sql'], values)

        try:
            fetch = self.SLITEcursor.lastrowid
        except TypeError:
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
        self.SLITEcursor.execute(query)

    def selectId(self, table01, field01, field02, id_search):
        config = json.load(open(self.configPATH,'r'))
        query = config['Misc']['Select_using_id'].format(table_name01 = table01, field_name01 = field01, field_name02 = field02, id_search = id_search)
        open('output.txt','a').write(query+'\n')
        return self.SLITEcursor.execute(query).fetchone()[0]

def main():
    print("Class name : QueryLamia\npurpose: make SQL query to the Lamia database")

if __name__ == '__main__':
    main()
