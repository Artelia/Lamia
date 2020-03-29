# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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

import os, sys, shutil
if sys.version_info.major == 2:
    import pyspatialite
elif sys.version_info.major == 3:
    import sqlite3

from .dbaseparserabstract import *


class SpatialiteDBaseParser(AbstractDBaseParser):

    def __init__(self, parserfactory):
         super(SpatialiteDBaseParser, self).__init__(parserfactory)

    def connectToDBase(self, slfile=None):
        self.spatialitefile = slfile
        self.connSLITE = sqlite3.dbapi2.connect(slfile)
        self.connSLITE.enable_load_extension(True)
        self.connSLITE.execute("SELECT load_extension('mod_spatialite')")
        self.SLITEcursor = self.connSLITE.cursor()

    def disconnect(self):
        self.connSLITE.close()

    def generateSQLTableCreationFromDBConfig(self, name, dbasetable, crs):

        sql = {}
        listFK = []
        sql['main'] = 'CREATE TABLE '
        sql['main'] += name + '('

        for key in dbasetable['fields']:
            sltype = None
            if dbasetable['fields'][key]['PGtype'] in PGTYPE_TO_SLTYPE.keys():
                sltype = PGTYPE_TO_SLTYPE[dbasetable['fields'][key]['PGtype']]
            elif 'VARCHAR' in dbasetable['fields'][key]['PGtype']:
                sltype = 'TEXT'
            sql['main'] += key + ' ' + sltype + ','

            if 'FK' in dbasetable['fields'][key].keys():
                listFK.append('FOREIGN KEY(' + key + ') REFERENCES ' + dbasetable['fields'][key]['FK'])

        sql['main'] += ','.join(listFK)
        if sql['main'][-1] == ',':
            sql['main'] = sql['main'][:-1]
        sql['main'] = sql['main'] + ');'

        if 'geom' in dbasetable.keys():
            sql['other'] = []
            sql['other'].append("SELECT AddGeometryColumn('" + name + "','geom'," + str(crs)
                                                          + ", '" + dbasetable['geom'] + "', 'XY');")
        return sql


    def generateSQLViewCreationFromDBConfig(self, dbname, dbasetable,worktype, crs ):
        """
        return sql list to be queried
        """
        finalsqllist=[]
        viewnames={}
        if 'djangoviewsql' in dbasetable.keys():
            viewnames['djangoviewsql'] = str(dbname) + '_django'

        if  'qgisPGviewsql' in dbasetable.keys():
            viewnames['qgisPGviewsql'] = str(dbname) + '_qgis'
        elif 'qgisviewsql' in dbasetable.keys():
            viewnames['qgisviewsql'] = str(dbname) + '_qgis'

        if 'exportviewsql' in dbasetable.keys():
            viewnames['exportviewsql'] = str(dbname) + '_export'

        for viewname in viewnames.keys():
            sql = 'CREATE VIEW ' + str(viewnames[viewname]) + ' AS '
            if dbasetable[viewname].strip() != '':
                sql += dbasetable[viewname]
            else:
                sql = 'SELECT * FROM ' + str(dbname)
            finalsqllist.append(sql)

            if self.isTableSpatial(viewnames[viewname]):
                dbnamelower = dbname.lower()
                idcolumnname = self.getFirstIdColumn(viewnames[viewname])
                viewlower = viewnames[viewname].lower()
                sql = "INSERT INTO views_geometry_columns (view_name, view_geometry, view_rowid, "
                sql += "f_table_name, f_geometry_column,read_only)"
                sql += " VALUES ('" + str(viewlower) + "','geom','" + idcolumnname + "','" + str(dbnamelower)
                sql += "','geom',0)"
                finalsqllist.append(sql)

        return finalsqllist

    def initDBase(self, **kwargs):
        slfile=kwargs.get('slfile', None)
        if slfile is None:
            raise ValueError('Init DBase : No file path given')

        originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'sqlite_base', 'DBase_ind0.sqlite')
        shutil.copyfile(originalfile, slfile)


    def query(self, sql,arguments=[], docommit=True):
        # cursor = self.connSLITE.cursor()
        if self.SLITEcursor is None:
            self.SLITEcursor = self.connSLITE.cursor()
        try:
            if self.printsql :
                logging.getLogger('Lamia').debug('%s - %s %.3f', docommit, sql,  self.getTimeNow() - timestart)

            query = self.SLITEcursor.execute(sql,arguments)
            returnquery = list(query)
            if docommit and self.forcenocommit == False:
                self.commit()

            return returnquery
        except (sqlite3.dbapi2.OperationalError ,sqlite3.dbapi2.IntegrityError) as e:
            # self.errorquerymessage.emit(str(e))
            #if self.qgsiface is None:
            print(sql)
            print('error query', e)

            return None

    def vacuum(self):
        raise NotImplementedError 

    def commit(self):
        self.connSLITE.commit()

    def reInitDBase(self):
        raise NotImplementedError 

    def isTableSpatial(self, tablename):
        sql = "PRAGMA table_info(" + str(tablename) + ")"
        query = self.query(sql)
        result = [row[1] for row in query]
        #print(result)
        if 'geom' in result:
            return True
        else:
            return False

    def getColumns(self, tablename):
        sql = "PRAGMA table_info(" + str(tablename) + ")"
        query = self.query(sql)
        result = [row[1] for row in query]
        return result

    def getFirstIdColumn(self,tablename):
        sql = "PRAGMA table_info(" + str(tablename) + ")"
        query = self.query(sql)
        result = [row[1] for row in query]
        #print(result)
        for fieldname in result:
            if self.revisionwork:
                if 'pk_' in fieldname:
                    return fieldname
            else:
                if 'id_' in fieldname:
                    return fieldname

    def getLastPK(self, tablename):
        sql = "SELECT * FROM sqlite_sequence "
        results = self.query(sql)
        for res in results:
            if res[0] == tablename:
                return res[1]
        return 0