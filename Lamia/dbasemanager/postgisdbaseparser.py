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

import os, sys, shutil, datetime
import psycopg2

from .dbaseparserabstract import *



class PostGisDBaseParser(AbstractDBaseParser):

    def __init__(self, parserfactory):
         super(PostGisDBaseParser, self).__init__(parserfactory)

    
    def connectToDBase(self,
                        host='localhost', port=None, dbname=None, schema=None, user=None, password=None):
        self.dbasetype = 'postgis'
        self.pgport = port
        self.pghost = host
        self.pgdb = dbname
        self.pgschema = schema
        self.pguser = user
        self.pgpassword = password

        # connexion
        # connect to postgres for checking database existence
        connectstr = "dbname='postgres' user='" + user + "' host='" + host + "' password='" + password + "'"
        connpgis = psycopg2.connect(connectstr)
        pgiscursor = connpgis.cursor()
        connpgis.autocommit = True
        pgiscursor.close()
        connpgis.close()

        # connexion to database
        connectstr = "dbname='" + self.pgdb.lower() + "' user='" + user + "' host='" + host
        connectstr += "' password='" + password + "'"
        self.connPGis = psycopg2.connect(connectstr)
        self.PGiscursor = self.connPGis.cursor()

        #searchpath
        sql = 'SET search_path TO ' + self.pgschema + ',public'
        self.query(sql)
        self.commit()

    def disconnect(self):
        self.PGiscursor.close()
        self.connPGis.close()

    def getDBName(self):
        return self.pgschema

    def generateSQLTableCreationFromDBConfig(self, name, dbasetable, crs):

        sql = {}
        listFK = []
        sql['main'] = 'CREATE TABLE '
        sql['main'] += self.pgschema + '.' + name + '('

        for key in dbasetable['fields']:
            sql['main'] += key + ' ' + dbasetable['fields'][key]['PGtype']
            if 'FK' in dbasetable['fields'][key].keys():
                sql['main'] += ' REFERENCES ' + self.pgschema.lower() + '.' + dbasetable['fields'][key]['FK']
            sql['main'] += ','

        if sql['main'][-1] == ',':
            sql['main'] = sql['main'][:-1]
        sql['main'] = sql['main'] + ');'

        if 'geom' in dbasetable.keys():
            sql['other'] = []
            sql['other'].append('ALTER TABLE ' + self.pgschema + '.' + name
                                + " ADD  COLUMN   geom geometry('" + dbasetable['geom'] + "'," + str(crs) + ");")

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
                sql = 'INSERT INTO geometry_columns(f_table_catalog, f_table_schema, f_table_name, '
                sql += 'f_geometry_column, coord_dimension, srid, "type") VALUES ('
                sql += "'" + worktype.lower() + "', '" + self.pgschema.lower() + "', '" + str( viewlower) + "','geom',2,"
                sql += str(crs) + ",'" + dbasetable['geom'] + "' );"
                finalsqllist.append(sql)

        return finalsqllist

    def initDBase(self, **kwargs):
        host=kwargs.get('host', 'localhost')
        port=kwargs.get('port', 5432)
        dbname=kwargs.get('dbname', None)
        schema=kwargs.get('schema', None)
        user=kwargs.get('user', None)
        password=kwargs.get('password', None)
        
        if None in [dbname, schema, user,password ]:
            raise ValueError('Init DBase : postgis conf not complete')

        # connexion
        # connect to postgres for checking database existence
        connectstr = "dbname='postgres' user='" + user + "' host='" + host + "' password='" + password + "'"
        try:
            connpgis = psycopg2.connect(connectstr)
        except psycopg2.OperationalError as e:
            print('Error connecting : ' , connectstr, '\n', e)
            return
        pgiscursor = connpgis.cursor()
        connpgis.autocommit = True

        # check if database exists
        sql = "SELECT  datname FROM pg_database WHERE datistemplate = false;"
        pgiscursor.execute(sql)
        rows = pgiscursor.fetchall()
        rows = [elem[0] for elem in rows]
        if dbname.lower() not in rows:
            pgiscursor.execute('CREATE DATABASE ' + dbname)
        connpgis.autocommit = True
        pgiscursor.close()
        connpgis.close()

        # connexion to database
        connectstr = "dbname='" + dbname.lower() + "' user='" + user + "' host='" + host
        connectstr += "' password='" + password + "'"
        self.connPGis = psycopg2.connect(connectstr)
        self.PGiscursor = self.connPGis.cursor()
        self.connPGis.autocommit = True

        #check if postgis extension exists
        sql = "Select * FROM pg_extension"
        self.PGiscursor.execute(sql)
        rows = self.PGiscursor.fetchall()
        result = [elem[0] for elem in rows]
        if 'postgis' not in result:
            sql = 'CREATE EXTENSION postgis'
            try:
                self.PGiscursor.execute(sql)
                self.commit()
            except psycopg2.ProgrammingError as e:
                pass
            self.connPGis.autocommit = False

        # schema
        sql = "SELECT * FROM pg_namespace"
        # sql = "select schema_name from information_schema.schemata"
        # query = self.query(sql)
        self.PGiscursor.execute(sql)
        rows = self.PGiscursor.fetchall()
        result = [row[1] for row in rows]

        if schema.lower() in result:
            try:
                sql = 'DROP SCHEMA ' + schema + ' CASCADE'
                self.query(sql)
                self.commit()
            except Exception as e:
                print(e)
        sql = 'CREATE SCHEMA ' + schema
        self.query(sql)
        self.commit()

        # configure search_path
        sql = 'SET search_path TO ' + schema + ',public'
        self.query(sql)
        self.commit()
        self.disconnect()




    def query(self, sql,arguments=[], docommit=True):
        if self.PGiscursor is None:
            self.PGiscursor = self.connPGis.cursor()
        try:
            if self.printsql :
                logging.getLogger('Lamia').debug('%s %.3f', sql,  self.getTimeNow() - timestart)
            self.PGiscursor.execute(sql)
        except psycopg2.ProgrammingError as e:
            print('error query : ', sql, '\n', e)
            return None
        except (psycopg2.DataError, psycopg2.InternalError) as e:
            print('error query : ', sql, '\n', e)
            return None


        if sql.strip()[0:6] == 'SELECT':
            try:
                rows = self.PGiscursor.fetchall()
                returnrows = list(rows)
                if docommit:
                    self.commit()
                if self.printsql:
                    logging.getLogger('Lamia').debug('%s %.3f', sql, self.getTimeNow() - timestart)
                return returnrows
            except psycopg2.ProgrammingError as e:
                print('error query', e)
                return None

    def vacuum(self):
        raise NotImplementedError 

    def commit(self):
        self.connPGis.commit()

    def reInitDBase(self):
        raise NotImplementedError 

    def isTableSpatial(self,tablename ):
        sql = "SELECT column_name FROM information_schema.columns WHERE table_name  = '" +  str(tablename).lower() + "'"
        query = self.query(sql)
        result = [row[0] for row in query]
        if 'geom' in result:
            return True
        else:
            return False

    def getColumns(self, tablename):
        sql = "SELECT column_name FROM information_schema.columns WHERE table_name  = '" +  str(tablename).lower() + "'"
        query = self.query(sql)
        result = [row[0] for row in query]
        return result

    def getFirstIdColumn(self,tablename):
        sql = "SELECT column_name FROM information_schema.columns WHERE table_name  = '" +  str(tablename).lower() + "'"
        query = self.query(sql)
        result = [row[0] for row in query]
        for fieldname in result:
            if self.revisionwork:
                if 'pk_' in fieldname:
                    return fieldname
            else:
                if 'id_' in fieldname:
                    return fieldname


    def getLastPK(self, tablename):
        sql = "SELECT last_value FROM "  
        sql +=  tablename.lower() + '_pk_' + tablename.lower() + '_seq'
        
        try:
            result = self.query(sql)[0][0]
            return result
        except TypeError as e:
            print('no seq for ' + tablename)
            return 0
        except Exception as e:
            print(e, ' - no seq for ' + tablename)
            return 0

    def _dateVersionConstraintSQL(self, specialdate=None):
        if specialdate is None or specialdate == 'now':
            #workingdatemodif = QtCore.QDate.fromString(self.workingdate, 'yyyy-MM-dd').addDays(1).toString('yyyy-MM-dd')
            workingdatemodif = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            workingdatemodif = QtCore.QDate.fromString(specialdate, 'dd/MM/yyyy').addDays(1).toString('yyyy-MM-dd')


        sqlin = ' datetimecreation <= ' + "'" + workingdatemodif + "'"
        sqlin += ' AND CASE WHEN datetimedestruction IS NOT NULL  '
        sqlin += 'THEN datetimedestruction > ' + "'" + workingdatemodif + "'" + ' ELSE TRUE END'
        sqlin += " AND lpk_revision_begin <= " + str(self.currentrevision)
        sqlin += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
        sqlin += " lpk_revision_end > " + str(self.currentrevision)
        sqlin += " ELSE TRUE END "

        return sqlin