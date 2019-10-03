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


from qgis.PyQt import QtCore
import os
import sys
import qgis
import qgis.utils
if qgis.utils.iface is None:
    qgis.utils.uninstallErrorHook()     #for standart output
import math
import shutil
import re
try:
    from pyspatialite import dbapi2 as db
    from pyspatialite.dbapi2 import *
except ImportError:
    import sqlite3
    from sqlite3 import *
    print('spatialite not enabled')

try:
    from qgis.PyQt.QtGui import (QMessageBox, QProgressBar, QApplication)
except ImportError:
    from qgis.PyQt.QtWidgets import (QMessageBox, QProgressBar, QApplication )

try:
    import PIL
    import PIL.Image
    PILexists = True
except:
    PILexists = False

if sys.version_info.major == 2:
    from ..libs import xlrd
else:
    import xlrd


import psycopg2
import glob
from collections import OrderedDict

import logging
#logger = logging.getLogger("Lamia")



class DBaseParser(QtCore.QObject):
    """
    the database parser
    """

    # recentDBaseChanged = QtCore.pyqtSignal()
    dBaseLoaded = QtCore.pyqtSignal()
    errorMessage = QtCore.pyqtSignal(str)
    normalMessage = QtCore.pyqtSignal(str)

    pgtypetosltype = {'VARCHAR' : 'TEXT',
                      'INT' : 'INTEGER',
                      'SERIAL PRIMARY KEY' : 'INTEGER PRIMARY KEY AUTOINCREMENT',
                      'TIMESTAMP' : 'TEXT',
                      'TEXT' : 'TEXT',
                      'TIMESTAMP WITH TIME ZONE' : 'TEXT',
                      'REAL': 'REAL',
                      'NUMERIC': 'REAL',
                      'BOOLEAN' : 'INTEGER'}



    def __init__(self,canvas=None):
        """
        Init func
        """
        super(QtCore.QObject, self).__init__()
        # ?? temp variable for export
        self.featureaddedid = None
        # the dictionnary of dbase
        self.dbasetables = None
        self.imagedirectory = None
        # visual mode used in ui
        self.visualmode = 0
        # dabse type Digue Assainissement
        self.type = None
        # spatialite or postgis
        self.dbasetype = None
        self.pghost = None
        self.pgdb = None
        self.pguser = None
        self.pgpassword = None
        #  working dir
        self.dbaseressourcesdirectory = None
        self.variante = None
        self.variantespossibles=[]
        #  not used yet
        self.searchbuffer = 20
        # used to define the working date in db
        self.workingdate = QtCore.QDate.currentDate().toString('yyyy-MM-dd')

        # crs of dbase
        self.crsnumber = None
        self.qgiscrs = None
        # gps things
        # self.hauteurperche = 2.0
        # the current prestation id
        self.currentprestationid = None
        # connextion var
        self.connSLITE = None      # spatialite connection
        self.SLITEcursor = None     # spatialite cursor
        self.connPGis = None        # postgis connection
        self.PGiscursor = None      # postgis cursor
        # spatialite spec
        self.spatialitefile = None
        # postgis spec
        self.horsligne = False
        self.date_deconnexion = None
        self.offLineConn = None
        self.offLineCursor = None
        self.pghost = None
        self.pgdb = None
        self.pguser = None
        self.pgpassword = None
        self.pgport = None
        self.pgschema = None
        # the qgis canvas
        self.canvas = canvas
        # self.canvas.renderStarting.connect(self.renderStarts)
        # the QgsCoordinateTransform var
        self.xform = None
        self.xformreverse = None
        # debug
        if False:
            formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(funcName)s -- %(message)s")
            self.logger = logging.getLogger("Lamia")
            self.logger.setLevel(logging.DEBUG)             # DEBUG INFO WARNING
            self.stream_handler = logging.StreamHandler()
            self.stream_handler.setFormatter(formatter)
            self.stream_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(self.stream_handler)
        if False:
            logging.basicConfig(level=logging.DEBUG)
            logging.info('popo')

        self.printsql = False
        self.version = None  # dbase version
        self.workversion = None  # dbase version

        self.revisionwork = False
        self.currentrevision = None
        self.maxrevision = 0

        self.xlsreader = True
        #self._readRecentDBase()

        # getqgisversion : ex : 21820
        try:
            self.qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
        except AttributeError:  # qgis 3
            self.qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT

        self.qgsiface = qgis.utils.iface


    def checkIfPGShcemaExists(self, dbname=None, schema=None, user=None,
                              host='localhost', password=None):
        """
        :param dbname:
        :param schema:
        :param user:
        :param host:
        :param password:
        :return: tuple (database exists, schema exists)
        """
        # connexion
        connectstr = "dbname='postgres' user='" + user + "' host='" + host + "' password='" + password + "'"
        connpgis = psycopg2.connect(connectstr)
        pgiscursor = connpgis.cursor()
        # database
        sql = "SELECT  datname FROM pg_database WHERE datistemplate = false;"
        pgiscursor.execute(sql)
        rows = pgiscursor.fetchall()
        rows = [elem[0] for elem in rows]
        if dbname not in rows:
            return False, False
        pgiscursor.close()
        connpgis.close()

        # connexion to database
        connectstr = "dbname='" + dbname + "' user='" + user + "' host='" + host + "' password='" + password + "'"
        connpgis = psycopg2.connect(connectstr)
        pgiscursor = connpgis.cursor()

        # schema
        sql = "select * from pg_namespace"
        pgiscursor.execute(sql)
        rows = pgiscursor.fetchall()
        # query = self.query(sql)
        result = [row[0] for row in rows]
        pgiscursor.close()
        connpgis.close()
        if schema in result:
            return True, True
        else:
            return True, False

    def createDbase(self, slfile=None, crs=None, worktype=None, dbasetype='spatialite',
                    dbname=None, schema=None, user=None, host='localhost', port=None, password=None,    # postgis
                    dbaseressourcesdirectory=None, variante=None):
        """
        pass
        :param slfile:
        :param crs:
        :param worktype:
        :param dbasetype:
        :param dbname:
        :param schema:
        :param user:
        :param host:
        :param port:
        :param password:
        :param dbaseressourcesdirectory:
        :return:
        """
        debug = False
        if debug: logging.getLogger("Lamia").debug('started')

        self.variante = variante
        # create dbasedict
        if not self.xlsreader:
            self.createDBDictionary(worktype)
        else:
            self.createDBDictionary2(worktype)

        if False:
            # manage ressource directory
            dbaseressourcesdirectorytemp = None
            if dbaseressourcesdirectory is None and dbasetype == 'spatialite':
                dbaseressourcesdirectorytemp = os.path.join(os.path.dirname(slfile), u'DBspatialite')
            else:
                dbaseressourcesdirectorytemp = dbaseressourcesdirectory

            if not os.path.isdir(dbaseressourcesdirectorytemp):
                os.makedirs(dbaseressourcesdirectorytemp)
                configdir = os.path.join(dbaseressourcesdirectorytemp,'config')
                os.makedirs(configdir)
                #tool dir
                dbasedir = os.path.join(configdir,'dbase')
                os.makedirs(dbasedir)
                rapportdir = os.path.join(configdir,'rappporttools')
                os.makedirs(rapportdir)
                styledir = os.path.join(configdir,'styles')
                os.makedirs(styledir)
                importdir = os.path.join(configdir,'importtools')
                os.makedirs(importdir)

        # dbaseressourcesdirectorytemp = dbaseressourcesdirectory
        dbaseressourcesdirectorytemp = self.createRessourcesDir(dbasetype, dbaseressourcesdirectory, slfile=slfile)


        # sql file contains output of dbase creation script
        sqlfile = os.path.join(dbaseressourcesdirectorytemp, 'sqlcreation.txt')
        openedsqlfile = open(sqlfile, u'w')
        # dbasetype
        self.dbasetype = dbasetype

        # ***************************************************************************************
        # Manage connection - creation and config
        if self.dbasetype == 'spatialite':

            originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'sqlite_base', 'DBase_ind0.sqlite')
            shutil.copyfile(originalfile, slfile)

            self.spatialitefile = slfile
            if sys.version_info.major == 2:
                self.connSLITE = db.connect(slfile)
            elif sys.version_info.major == 3:   # python 3
                self.connSLITE = qgis.utils.spatialite_connect(slfile)
            self.SLITEcursor = self.connSLITE.cursor()
            sql = "PRAGMA foreign_keys = ON"
            openedsqlfile.write(sql + '\n')
            self.query(sql)

        elif dbasetype == 'postgis':
            self.dbasetype = 'postgis'
            self.pghost = host
            self.pgdb = dbname
            self.pguser = user
            self.pgpassword = password
            self.pgport = port
            self.pgschema = schema
            # connexion
            # connect to postgres for checking database existence
            connectstr = "dbname='postgres' user='" + user + "' host='" + host + "' password='" + password + "'"
            connpgis = psycopg2.connect(connectstr)
            pgiscursor = connpgis.cursor()
            connpgis.autocommit = True

            # database
            sql = "SELECT  datname FROM pg_database WHERE datistemplate = false;"
            pgiscursor.execute(sql)
            rows = pgiscursor.fetchall()
            rows = [elem[0] for elem in rows]
            if self.pgdb not in rows:
                # self.errorMessage.emit('Base de donnees deja existante')
                pgiscursor.execute('CREATE DATABASE DIGUE')

            sql = "Select * FROM pg_extension"
            pgiscursor.execute(sql)
            rows = pgiscursor.fetchall()
            result = [elem[0] for elem in rows]
            if 'postgis' not in result:
                sql = 'CREATE EXTENSION postgis'
                openedsqlfile.write(sql + '\n')
                pgiscursor.execute(sql)
                self.commit()
                connpgis.autocommit = False
            pgiscursor.close()
            connpgis.close()

            # connexion to database
            connectstr = "dbname='" + self.pgdb + "' user='" + user + "' host='" + host
            connectstr += "' password='" + password + "'"
            self.connPGis = psycopg2.connect(connectstr)
            self.PGiscursor = self.connPGis.cursor()

            # schema
            sql = "SELECT * FROM pg_namespace"
            query = self.query(sql)
            result = [row[0] for row in query]
            if self.pgschema in result:
                try:
                    sql = 'DROP SCHEMA ' + self.pgschema + ' CASCADE'
                    self.query(sql)
                    self.commit()
                except Exception as e:
                    print(e)
            sql = 'CREATE SCHEMA ' + self.pgschema
            # res = self.PGiscursor.execute(sql)
            self.query(sql)
            self.commit()
            sql = 'SET search_path TO ' + self.pgschema + ',public'
            self.query(sql)
            self.commit()
            # res = self.PGiscursor.execute(sql)
            if False:
                sql = 'GRANT ALL ON SCHEMA '+self.pgschema+' TO vadjango'
                self.query(sql)
                self.commit()

        # ***************************************************************************************
        # Tables creation
        for order in range(20):
            for dbname in self.dbasetables:
                if self.dbasetables[dbname]['order'] == order:
                    if self.dbasetype == 'spatialite':
                        sql = self._generateSpatialiteCreationSQL(dbname, self.dbasetables[dbname], crs)
                        # print(sql['main'])
                        openedsqlfile.write(sql['main'] + '\n')
                    elif dbasetype == 'postgis':
                        sql = self._generatePostGisCreationSQL(dbname, self.dbasetables[dbname], crs)
                        # print(sql['main'])
                        openedsqlfile.write(sql['main'] + '\n')

                    if debug: logging.getLogger("Lamia").debug('sql : %s', sql['main'])

                    self.query(sql['main'])
                    self.commit()
                    if 'other' in sql.keys():
                        for sqlother in sql['other']:
                            openedsqlfile.write(sqlother + '\n')
                            # print(sqlother)
                            self.query(sqlother)
                            self.commit()

        if dbaseressourcesdirectory is None and dbasetype == 'spatialite':
            dbaseressourcesdirectorytemp2 = './/DBspatialite'
        else:
            dbaseressourcesdirectorytemp2 = dbaseressourcesdirectorytemp



        if self.version is None or self.version == '':
            versionsql = 'NULL'
            sql = "INSERT INTO Basedonnees (metier,repertoireressources,crs, version) "
            sql += "VALUES('" + worktype + "','" + dbaseressourcesdirectorytemp2 + "'," + str(crs) + "," + versionsql + ");"
            self.query(sql)
            self.commit()
        else:
            versionsql = "'" + str(self.version) + "'"
            workversionsql = "'" + str(self.workversion) + "'"
            if self.variante is None:
                variantesql = 'NULL'
            else:
                variantesql = "'" + self.variante + "'"
            sql = "INSERT INTO Basedonnees (metier,repertoireressources,crs, version, workversion, variante) "
            sql += "VALUES('" + worktype + "','" + dbaseressourcesdirectorytemp2 + "'," + str(crs) + "," + versionsql
            sql += "," + workversionsql +  ',' + variantesql + ")"
            self.query(sql)
            self.commit()

        if self.revisionwork:
            # datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "INSERT INTO Revision (datetimerevision, commentaire) "
            sql += "VALUES('" + datecreation + "','Premiere version ');"
            self.query(sql)
            self.commit()

        # ***************************************************************************************
        # view creation
        for dbname in self.dbasetables:
            if debug: logging.getLogger("Lamia").debug('view creation : %s', dbname)
            viewnames={}
            if 'djangoviewsql' in self.dbasetables[dbname].keys():
                viewnames['djangoviewsql'] = str(dbname) + '_django'
            if self.dbasetype == 'spatialite' and 'qgisSLviewsql' in self.dbasetables[dbname].keys():
                viewnames['qgisSLviewsql'] = str(dbname) + '_qgis'
            elif self.dbasetype == 'postgis' and 'qgisPGviewsql' in self.dbasetables[dbname].keys():
                viewnames['qgisPGviewsql'] = str(dbname) + '_qgis'
            elif 'qgisviewsql' in self.dbasetables[dbname].keys():
                viewnames['qgisviewsql'] = str(dbname) + '_qgis'
            if 'exportviewsql' in self.dbasetables[dbname].keys():
                if True:
                    viewnames['exportviewsql'] = str(dbname) + '_export'
                if False:
                    for i, idexpo in enumerate(self.dbasetables[dbname]['exportviewsql']):
                        viewnames['exportviewsql' + str(i)] = str(dbname) + '_export' + str(i)

            for viewname in viewnames.keys():

                # sql = 'CREATE VIEW ' + str(dbname) + '_view AS '
                sql = 'CREATE VIEW ' + str(viewnames[viewname]) + ' AS '
                if self.dbasetables[dbname][viewname] != '':
                    sql += self.dbasetables[dbname][viewname]
                else:
                    sql += 'SELECT * FROM ' + str(dbname)
                openedsqlfile.write(sql + '\n')
                self.query(sql)
                self.commit()
                # add view in geom register
                #if 'geom' in self.dbasetables[dbname].keys():
                if self.isTableSpatial(viewnames[viewname]):
                    if self.dbasetype == 'spatialite':
                        dbnamelower = dbname.lower()
                        idcolumnname = self.getFirstIdColumn(viewnames[viewname])
                        viewlower = viewnames[viewname].lower()
                        sql = "INSERT INTO views_geometry_columns (view_name, view_geometry, view_rowid, "
                        sql += "f_table_name, f_geometry_column,read_only)"
                        sql += " VALUES ('" + str(viewlower) + "','geom','" + idcolumnname + "','" + str(dbnamelower)
                        sql += "','geom',0)"
                        openedsqlfile.write(sql + '\n')
                        self.query(sql)
                        self.commit()
                    elif dbasetype == 'postgis':
                        dbnamelower = dbname.lower()
                        idcolumnname = self.getFirstIdColumn(viewnames[viewname])
                        viewlower = viewnames[viewname].lower()
                        sql = 'INSERT INTO geometry_columns(f_table_catalog, f_table_schema, f_table_name, '
                        sql += 'f_geometry_column, coord_dimension, srid, "type") VALUES ('
                        sql += "'" + worktype.lower() + "', '" + self.pgschema.lower() + "', '" + str( viewlower) + "','geom',2,"
                        sql += str(crs) + ",'" + self.dbasetables[dbname]['geom'] + "' );"
                        openedsqlfile.write(sql + '\n')
                        self.query(sql)
                        self.commit()

            #spatialindex
            if 'spatialindex' in self.dbasetables[dbname].keys():
                if self.dbasetype == 'spatialite':
                    sql = "SELECT CreateSpatialIndex('" + dbname + "','geom')"
                    openedsqlfile.write(sql + '\n')
                    self.query(sql)
                elif self.dbasetype == 'postgis':
                    pass



        openedsqlfile.close()



        if True:

            self.loadQgisVectorLayers(file=self.spatialitefile, dbasetype=self.dbasetype,
                                      host=self.pghost, port=self.pgport, dbname=self.pgdb, schema=self.pgschema,
                                      user=self.pguser, password=self.pgpassword)



    def createRessourcesDir(self, dbasetype, dbaseressourcesdirectory, slfile=None):
        dbaseressourcesdirectorytemp = None

        if dbaseressourcesdirectory is None and dbasetype == 'spatialite':
            dbaseressourcesdirectorytemp = os.path.join(os.path.dirname(slfile), u'DBspatialite')
        else:
            dbaseressourcesdirectorytemp = dbaseressourcesdirectory

        if not os.path.isdir(dbaseressourcesdirectorytemp):
            os.makedirs(dbaseressourcesdirectorytemp)
        configdir = os.path.join(dbaseressourcesdirectorytemp, 'config')
        if not os.path.isdir(configdir):
            os.makedirs(configdir)
        # tool dir
        dbasedir = os.path.join(configdir, 'dbase')
        if not os.path.isdir(dbasedir):
            os.makedirs(dbasedir)

        rapportdir = os.path.join(configdir, 'rappporttools')
        if not os.path.isdir(rapportdir):
            os.makedirs(rapportdir)

        styledir = os.path.join(configdir, 'styles')
        if not os.path.isdir(styledir):
            os.makedirs(styledir)

        importdir = os.path.join(configdir, 'importtools')
        if not os.path.isdir(importdir):
            os.makedirs(importdir)


        return dbaseressourcesdirectorytemp



    def createDBDictionary2(self, type, configdir=False, baseversiontoread=None, workversiontoread=None,chekupdate=True):
        """!
        Read the files in ./DBASE/create
        A file describes the fields  like that:
        #comment
        ###Field_name;PG_type;SL_type;Foreignkey_type
        ## parent field - used for ui - enable to sort the child fields depending the parent field    (optional)
        constraint value description;constraint value value;[depending parent field value]

        And fill the var self.dbasetables which is a dictionnary like that :
        {...{tablename : {'order' : order,
                          'geom' : geometry type ,
                          'widget' : the table widget,
                          'djangoviewsql' : sql statement for initial django view creation
                          'qgisviewsql' : sql statement for initial qgis view creation
                          'qgisSLviewsql' : sql statement for initial qgis view creation - spatialite compatible
                          'qgisPGviewsql' : sql statement for initial qgis view creation - postgis compatible
                          'exportviewsql' : sql statement for initial special view creation
                          'layer' : real layer
                          'layerqgis' : view layer with parent fields
                          'layerdjango' : view layer with parent fields
                          'showinqgis' : display layer in canvas
                          'scale' : visibility scale
                          'spatialindex' : create a spatialite spatial index
                          'fields' : OrderedDict{...{fieldname : {'PGtype' : PostGis type (integer not null...)
                                                                  'SLtype' : spatialite type (integer not null...)
                                                                  'FK' (optional) : foreign key definition
                                                                  'ParFldCst (optional) : name of the parent field for contraint
                                                                  'Cst' (optional) : list of constraint : [description,value,[parent field consraint value]}
                                                 ...}

                          }
         ...}

        """
        debug = False
        if debug: logging.getLogger("Lamia").debug('started')



        # first readfiles in ./DBASE\create directory and create self.dbasetables
        createfilesdir = None

        if not configdir:
            if baseversiontoread is None:
                self.type = type
                self.dbasetables = {}

                workversionmax, createfilesdir = self.getVersionRepositories2(self.type)[-1]
                baseversionmax, createfilesdirbase = self.getVersionRepositories2(self.type.split('_')[0])[-1]

                if (chekupdate and self.version is not None
                        and (self.version < baseversionmax or self.workversion < workversionmax)) :
                    self.updateDBaseVersion2()



                self.version = baseversionmax
                self.workversion = workversionmax

                if debug: logging.getLogger("Lamia").debug('baseversion : %s, workversion : %s', str(self.version ), str(self.workversion ))

                if createfilesdirbase and createfilesdirbase != createfilesdir :    #cas de la lecture du bd enfant
                    parsertemp = DBaseParser(None)
                    parsertemp.createDBDictionary2(self.type.split('_')[0])
                    self.dbasetables = parsertemp.dbasetables
                    del parsertemp
            else:
                self.type = type
                self.dbasetables = {}

                baseversions = self.getVersionRepositories2(self.type.split('_')[0])
                workversions = self.getVersionRepositories2(self.type)
                baseversionnumbers = [elem[0] for elem in baseversions]
                workversionnumbers = [elem[0] for elem in workversions]


                createfilesdirbase = baseversions[baseversionnumbers.index(baseversiontoread)][1]
                createfilesdir = workversions[workversionnumbers.index(workversiontoread)][1]

                if createfilesdirbase != createfilesdir:
                    #createfilesdir = workversions[workversionnumbers.index(workversiontoread)][1]
                    parsertemp = DBaseParser(None)
                    parsertemp.createDBDictionary2(self.type.split('_')[0], baseversiontoread=baseversiontoread,workversiontoread=baseversiontoread)
                    self.dbasetables = parsertemp.dbasetables
                    del parsertemp


        else:
            createfilesdir = os.path.join(self.dbaseressourcesdirectory,'config','dbase')
            if not os.path.exists(createfilesdir):
                return



        if debug: logging.getLogger("Lamia").debug('createfilesdir : %s', str(createfilesdir))

        self.readDbDictionnary(createfilesdir)



    def readDbDictionnary(self, dictfile=None, vartoread=None):
        """

        :param dictfile:
        :param vartoread:
        :return:
        """

        debug = False
        if dictfile is None or not os.path.isfile(dictfile):
            return

        xlsbook = xlrd.open_workbook(dictfile)

        for sheet in xlsbook.sheets():
            tablename = sheet.name.split('_')
            fieldname = None
            cstcolumntoread = None
            order = None
            # print(tablename)
            if len(tablename) == 1:  # non table file
                continue
            else:
                order = tablename[0]
                tablename = '_'.join(tablename[1:])


            #print(tablename)
            # print(self.dbasetables)

            if tablename not in self.dbasetables.keys():
                self.dbasetables[tablename] = {}
                self.dbasetables[tablename]['order'] = int(order)
                self.dbasetables[tablename]['fields'] = OrderedDict()
                self.dbasetables[tablename]['showinqgis'] = False
                self.dbasetables[tablename]['widget'] = []
                self.dbasetables[tablename]['row_variantes'] = -1

            for row in range(sheet.nrows):


                firstcol =  sheet.cell_value(row, 0)
                if len(firstcol) > 0 and firstcol[0] == '#':  # comment - pass
                    if firstcol.strip() == '#DJAN':
                        #self.dbasetables[tablename]['djangoviewsql'] = line[5:].strip()
                        self.dbasetables[tablename]['djangoviewsql'] = sheet.cell_value(row, 1).strip()
                    elif firstcol.strip() == '#QGISSL':
                        if 'qgisSLviewsql' in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]['qgisSLviewsql'] += ' ' + sheet.cell_value(row, 1).strip() + ' '
                        else:
                            self.dbasetables[tablename]['qgisSLviewsql'] = sheet.cell_value(row, 1).strip()
                    elif firstcol.strip() == '#QGISPG':
                        if 'qgisPGviewsql' in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]['qgisPGviewsql'] += ' ' + sheet.cell_value(row, 1).strip() + ' '
                        else:
                            self.dbasetables[tablename]['qgisPGviewsql'] = sheet.cell_value(row, 1).strip()
                    elif firstcol.strip() == '#QGIS':
                        if 'qgisviewsql' in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]['qgisviewsql'] += ' ' + sheet.cell_value(row, 1).strip() + ' '
                        else:
                            self.dbasetables[tablename]['qgisviewsql'] = sheet.cell_value(row, 1).strip()
                        # self.dbasetables[tablename]['qgisviewsql'] = line[5:].strip()
                    elif firstcol.strip() == '#EXPO':
                        self.dbasetables[tablename]['exportviewsql'] = sheet.cell_value(row, 1).strip()
                    elif firstcol.strip() == '#SCAL':
                        self.dbasetables[tablename]['scale'] = float(sheet.cell_value(row, 1).strip())
                    elif firstcol.strip() == '#SHOW':
                        value = sheet.cell_value(row, 1).strip().strip()
                        if value == 'YES':
                            self.dbasetables[tablename]['showinqgis'] = True
                    elif firstcol.strip() == '#SPATIALINDEX':
                        value = sheet.cell_value(row, 1).strip()
                        if value == 'YES':
                            self.dbasetables[tablename]['spatialindex'] = True
                    elif firstcol.strip() == '#VARIANTES':
                        for colnbr in range(1,sheet.ncols):
                            value = sheet.cell_value(row, colnbr)
                            if value.strip() != '' :
                                self.dbasetables[tablename]['row_variantes'] = row
                                if value not in self.variantespossibles:
                                    self.variantespossibles.append(sheet.cell_value(row, colnbr).strip())




                    else:
                        continue

                else:
                    if firstcol != '':
                        fieldname = sheet.cell_value(row, 0).strip()
                        cstcolumntoread = None
                        if fieldname == 'geom':
                            self.dbasetables[tablename]['geom'] = sheet.cell_value(row, 1).strip()
                            continue

                        self.dbasetables[tablename]['fields'][fieldname] = {}
                        self.dbasetables[tablename]['fields'][fieldname]['PGtype'] = sheet.cell_value(row, 1).strip() # the pg type

                        #self.dbasetables[tablename]['fields'][fieldname]['SLtype'] = linesplit[2].strip()  # the spatialite type
                        # the foreign key
                        if sheet.cell_value(row, 2).strip() != '':
                            self.dbasetables[tablename]['fields'][fieldname]['FK'] = sheet.cell_value(row, 2).strip()

                        if sheet.cell_value(row, 4).strip() != '':
                            self.dbasetables[tablename]['fields'][fieldname]['ParFldCst'] = sheet.cell_value(row, 4).strip()

                        """
                        try:
                            sheet.cell_value(row, 5).strip()
                        except :
                            valetmp = sheet.cell_value(row, 5)
                            print(valetmp, valetmp.__class__,tablename, fieldname )
                        """

                        if False and sheet.cell_value(row, 5).strip() != '':


                            if 'Cst' in self.dbasetables[tablename]['fields'][fieldname].keys():
                                self.dbasetables[tablename]['fields'][fieldname]['Cst'].append([])
                            else:
                                self.dbasetables[tablename]['fields'][fieldname]['Cst'] = [[]]

                            showvalue = self.convertxlsdataToString(sheet.cell_value(row, 5))
                            datavalue = self.convertxlsdataToString(sheet.cell_value(row, 6))
                            self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(showvalue.strip())
                            self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(datavalue.strip())

                            if sheet.cell_value(row, 7).strip() != '':
                                self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(eval(sheet.cell_value(row, 7).strip()))
                            else:
                                self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(None)

                        cstcolumntoread = self.readConstraints(tablename,fieldname, sheet, row, cstcolumntoread)





                    else:
                        # if fieldname in self.dbasetables[tablename]['fields'].keys():
                        if fieldname is not None and fieldname != 'geom':
                            self.readConstraints(tablename,fieldname,sheet, row,cstcolumntoread)

                        if False:
                            if sheet.cell_value(row, 5).strip() != '':
                                self.dbasetables[tablename]['fields'][fieldname]['Cst'].append([])
                                # value = sheet.cell_value(row, 6)
                                showvalue = self.convertxlsdataToString(sheet.cell_value(row, 5))
                                datavalue = self.convertxlsdataToString(sheet.cell_value(row, 6))
                                self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(showvalue.strip())
                                self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(datavalue.strip())
                                if sheet.cell_value(row, 7).strip() != '':
                                    self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(eval(sheet.cell_value(row, 7).strip() ))
                                else:
                                    self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(None)






        if False:
            for filename in glob.glob(os.path.join(createfilesdir, '*.txt')):
                if True:
                    basename = os.path.basename(filename).split('.')[0]
                    if debug: logging.getLogger("Lamia").debug('filename %s',basename )
                    temp = basename.split('_')
                    if len(temp) == 1:  # non table file
                        continue
                    elif len(temp) == 3:  # underscore in the name
                        temp[1]+='_'
                        temp[1]+=temp[2]
                    elif len(temp) == 4:  # underscore in the name
                        temp[1]+='_'
                        temp[1]+=temp[2]
                        temp[1]+='_'
                        temp[1]+=temp[3]
                    elif len(temp) == 5:  # underscore in the name
                        temp[1]+='_'
                        temp[1]+=temp[2]
                        temp[1]+='_'
                        temp[1]+=temp[3]
                        temp[1]+='_'
                        temp[1]+=temp[4]
                    tablename = temp[1]
                    if tablename not in self.dbasetables.keys():
                        self.dbasetables[tablename] = {}
                        self.dbasetables[tablename]['order'] = int(temp[0])
                        self.dbasetables[tablename]['fields'] = OrderedDict()
                        self.dbasetables[tablename]['showinqgis'] = False
                        self.dbasetables[tablename]['widget'] = []
                    # self.dbasetables[tablename]['exportviewsql'] = []
                if sys.version_info.major == 2:
                    file = open(filename, 'r')
                elif sys.version_info.major == 3:
                    file = open(filename, 'r',encoding="utf-8")
                    #file = open(filename, 'rb')
                compt = 0
                for line in file:
                    if sys.version_info.major == 2:
                        line = line.decode('utf-8-sig')

                    if len(line.strip()) == 0:
                        continue

                    if line[0:3] == '###':          # new field
                        line = line[3:].strip()
                        linesplit = line.split(';')
                        fieldname = linesplit[0].strip()
                        if debug: logging.getLogger("Lamia").debug('fieldname %s', fieldname)
                        if fieldname == 'geom':
                            self.dbasetables[tablename]['geom'] = linesplit[1].strip()
                            continue
                        self.dbasetables[tablename]['fields'][fieldname] = {}
                        self.dbasetables[tablename]['fields'][fieldname]['PGtype'] = linesplit[1].strip()  # the pg type
                        self.dbasetables[tablename]['fields'][fieldname]['SLtype'] = linesplit[2].strip()  # the spatialite type
                        # the foreign key
                        if len(linesplit) > 3:
                            self.dbasetables[tablename]['fields'][fieldname]['FK'] = linesplit[3].strip()

                    elif line[0:2] == '##':         # parent field constraint name
                        self.dbasetables[tablename]['fields'][fieldname]['ParFldCst'] = line[2:].strip()

                    elif line[0] == '#':            # comment - pass
                        if line[0:5] == '#DJAN':
                            self.dbasetables[tablename]['djangoviewsql'] = line[5:].strip()
                        elif line[0:7] == '#QGISSL':
                            if 'qgisSLviewsql' in self.dbasetables[tablename].keys():
                                self.dbasetables[tablename]['qgisSLviewsql'] += ' ' + line[7:].strip() + ' '
                            else:
                                self.dbasetables[tablename]['qgisSLviewsql'] = line[7:].strip()
                        elif line[0:7] == '#QGISPG':
                            if 'qgisPGviewsql' in self.dbasetables[tablename].keys():
                                self.dbasetables[tablename]['qgisPGviewsql'] += ' ' + line[7:].strip() + ' '
                            else:
                                self.dbasetables[tablename]['qgisPGviewsql'] = line[7:].strip()
                        elif line[0:5] == '#QGIS':
                            if 'qgisviewsql' in self.dbasetables[tablename].keys():
                                self.dbasetables[tablename]['qgisviewsql'] += ' ' + line[5:].strip() + ' '
                            else:
                                self.dbasetables[tablename]['qgisviewsql'] = line[5:].strip()
                            # self.dbasetables[tablename]['qgisviewsql'] = line[5:].strip()
                        elif line[0:5] == '#EXPO':
                            self.dbasetables[tablename]['exportviewsql'] = line[5:].strip()
                        elif line[0:5] == '#SCAL':
                            self.dbasetables[tablename]['scale'] = float(line[5:].strip())
                        elif line[0:5] == '#SHOW':
                            value = line[5:].strip()
                            if value == 'YES':
                                self.dbasetables[tablename]['showinqgis'] = True
                        elif line[0:13] == '#SPATIALINDEX':
                            value = line[13:].strip()
                            if value == 'YES':
                                self.dbasetables[tablename]['spatialindex'] = True
                        else:
                            continue


                    else:                           # field constraint
                        if 'Cst' in self.dbasetables[tablename]['fields'][fieldname].keys():
                            self.dbasetables[tablename]['fields'][fieldname]['Cst'].append([])
                        else:
                            self.dbasetables[tablename]['fields'][fieldname]['Cst'] = [[]]

                        if True:
                            linesplit = line.split(';')

                        if False:
                            if sys.version_info.major == 2:
                                linesplit = line.decode('utf-8').split(';')
                            elif sys.version_info.major == 3:
                                # print(line.__class__)
                                linesplit = line.split(';')
                                #print(type(linesplit[0]))
                                #linesplit = line.decode('utf-8').split(';')
                        if debug: logging.getLogger("Lamia").debug('cst line split %s %s',fieldname, str(linesplit))

                        self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(linesplit[0].strip())
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(linesplit[1].strip())
                        if len(linesplit) > 2:
                            self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(eval(linesplit[2].strip()))
                        else:
                            self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(None)
                    compt += 1

                file.close()

        if "Revision" in self.dbasetables.keys():
            self.revisionwork = True


        if debug:
            for key in self.dbasetables.keys():
                logging.getLogger("Lamia").debug('dbasetables %s : %s', str(key), str(self.dbasetables[key]))


    def readConstraints(self, tablename,fieldname  ,sheet, xlrow,cstcolumntoread=None):

        # dbasefield self.dbasetables[tablename]['fields'][fieldname]
        # print('readConstraints',tablename,fieldname  ,sheet, xlrow)
        colindexvariante = cstcolumntoread
        dbasefield = self.dbasetables[tablename]['fields'][fieldname]

        if colindexvariante is None:
            colindexvariante = None
            if self.variante is None:
                colindexvariante = 5
            else:
                if self.dbasetables[tablename]['row_variantes'] >= 0 :
                    rowvariantes = self.dbasetables[tablename]['row_variantes']
                    if self.variante =='Lamia':
                        colindexvariante = 5
                    else:
                        for col in range(sheet.ncols):
                            try:
                                if (sheet.cell_value(rowvariantes,col ) == self.variante
                                        and sheet.cell_value(xlrow,col ) != '' ):
                                    colindexvariante = col
                                    # print('colindexvariante', tablename, fieldname, colindexvariante)
                                    break
                            except:
                                print('error',tablename,fieldname ,self.variante )
                        if colindexvariante is None:
                            colindexvariante = 5



        if unicode(sheet.cell_value(xlrow, colindexvariante)).strip() != '':
            if 'Cst' in dbasefield.keys():
                dbasefield['Cst'].append([])
            else:
                dbasefield['Cst'] = [[]]


            showvalue = self.convertxlsdataToString(sheet.cell_value(xlrow, colindexvariante))
            datavalue = self.convertxlsdataToString(sheet.cell_value(xlrow, colindexvariante +1 ))
            dbasefield['Cst'][-1].append(showvalue.strip())
            dbasefield['Cst'][-1].append(datavalue.strip())

            if sheet.cell_value(xlrow, colindexvariante + 2).strip() != '':
                dbasefield['Cst'][-1].append(eval(sheet.cell_value(xlrow, colindexvariante + 2).strip()))
            else:
                dbasefield['Cst'][-1].append(None)

        return colindexvariante


    def convertxlsdataToString(self, data):
        #print('data0', data, data.__class__)
        if sys.version_info.major == 2:
            if data is None:
                data = ''
            elif isinstance(data, unicode):
                data = data
            elif isinstance(data, float):
                data = str(data).rstrip('0').rstrip('.')
            else:
                data = str(data)
        else:
            if data is None:
                data = ''
            elif isinstance(data, str):
                data = data
            elif isinstance(data, float):
                data = str(data).rstrip('0').rstrip('.')
            else:
                data = str(data)

        #print('data1', data, data.__class__)
        return data





    def createDBDictionary(self, type, configdir=False, baseversiontoread=None, workversiontoread=None):
        """!
        Read the files in ./DBASE/create
        A file describes the fields  like that:
        #comment
        ###Field_name;PG_type;SL_type;Foreignkey_type
        ## parent field - used for ui - enable to sort the child fields depending the parent field    (optional)
        constraint value description;constraint value value;[depending parent field value]

        And fill the var self.dbasetables which is a dictionnary like that :
        {...{tablename : {'order' : order,
                          'geom' : geometry type ,
                          'widget' : the table widget,
                          'djangoviewsql' : sql statement for initial django view creation
                          'qgisviewsql' : sql statement for initial qgis view creation
                          'qgisSLviewsql' : sql statement for initial qgis view creation - spatialite compatible
                          'qgisPGviewsql' : sql statement for initial qgis view creation - postgis compatible
                          'exportviewsql' : sql statement for initial special view creation
                          'layer' : real layer
                          'layerqgis' : view layer with parent fields
                          'layerdjango' : view layer with parent fields
                          'showinqgis' : display layer in canvas
                          'scale' : visibility scale
                          'spatialindex' : create a spatialite spatial index
                          'fields' : OrderedDict{...{fieldname : {'PGtype' : PostGis type (integer not null...)
                                                                  'SLtype' : spatialite type (integer not null...)
                                                                  'FK' (optional) : foreign key definition
                                                                  'ParFldCst (optional) : name of the parent field for contraint
                                                                  'Cst' (optional) : list of constraint : [description,value,[parent field consraint value]}
                                                 ...}

                          }
         ...}

        """
        debug = False
        if debug: logging.getLogger("Lamia").debug('started')



        # first readfiles in ./DBASE\create directory and create self.dbasetables
        createfilesdir = None

        if not configdir:
            if baseversiontoread is None:
                self.type = type
                self.dbasetables = {}

                createfilesdir, workversionmax = self.getMaxVersionRepository(self.type)
                createfilesdirbase, baseversionmax = self.getMaxVersionRepository(self.type.split('_')[0])



                if (self.version is not None
                        and (self.version < baseversionmax or self.workversion < workversionmax)) :
                    self.updateDBaseVersion()

                self.version = baseversionmax
                self.workversion = workversionmax

                if createfilesdirbase and createfilesdirbase != createfilesdir :    #cas de la lecture du bd enfant
                    parsertemp = DBaseParser(None)
                    parsertemp.createDBDictionary(self.type.split('_')[0])
                    self.dbasetables = parsertemp.dbasetables
                    del parsertemp
            else:
                self.type = type
                self.dbasetables = {}
                createfilesdir, workversionmax = self.getMaxVersionRepository(self.type)
                createfilesdirbase, baseversionmax = self.getMaxVersionRepository(self.type.split('_')[0])


                createfilesdirbase = os.path.join(os.path.dirname(createfilesdir),  self.type.split('_')[0] +'_' + baseversiontoread)
                createfilesdir = None
                if workversiontoread is not None:
                    createfilesdir = os.path.join(os.path.dirname(createfilesdirbase),self.type + '_' + workversiontoread)

                if createfilesdirbase and createfilesdirbase != createfilesdir :    #cas de la lecture du bd enfant
                    parsertemp = DBaseParser(None)
                    parsertemp.createDBDictionary(self.type.split('_')[0], baseversiontoread=baseversiontoread,workversiontoread=baseversiontoread)
                    self.dbasetables = parsertemp.dbasetables
                    del parsertemp




        else:
            createfilesdir = os.path.join(self.dbaseressourcesdirectory,'config','dbase')
            if not os.path.exists(createfilesdir):
                return


        for filename in glob.glob(os.path.join(createfilesdir, '*.txt')):

            basename = os.path.basename(filename).split('.')[0]
            if debug: logging.getLogger("Lamia").debug('filename %s',basename )
            temp = basename.split('_')
            if len(temp) == 1:  # non table file
                continue
            elif len(temp) == 3:  # underscore in the name
                temp[1]+='_'
                temp[1]+=temp[2]
            elif len(temp) == 4:  # underscore in the name
                temp[1]+='_'
                temp[1]+=temp[2]
                temp[1]+='_'
                temp[1]+=temp[3]
            elif len(temp) == 5:  # underscore in the name
                temp[1]+='_'
                temp[1]+=temp[2]
                temp[1]+='_'
                temp[1]+=temp[3]
                temp[1]+='_'
                temp[1]+=temp[4]
            tablename = temp[1]
            if tablename not in self.dbasetables.keys():
                self.dbasetables[tablename] = {}
                self.dbasetables[tablename]['order'] = int(temp[0])
                self.dbasetables[tablename]['fields'] = OrderedDict()
                self.dbasetables[tablename]['showinqgis'] = False
                self.dbasetables[tablename]['widget'] = []
            # self.dbasetables[tablename]['exportviewsql'] = []
            if sys.version_info.major == 2:
                file = open(filename, 'r')
            elif sys.version_info.major == 3:
                file = open(filename, 'r',encoding="utf-8")
                #file = open(filename, 'rb')
            compt = 0
            for line in file:
                if sys.version_info.major == 2:
                    line = line.decode('utf-8-sig')

                if len(line.strip()) == 0:
                    continue

                if line[0:3] == '###':          # new field
                    line = line[3:].strip()
                    linesplit = line.split(';')
                    fieldname = linesplit[0].strip()
                    if debug: logging.getLogger("Lamia").debug('fieldname %s', fieldname)
                    if fieldname == 'geom':
                        self.dbasetables[tablename]['geom'] = linesplit[1].strip()
                        continue
                    self.dbasetables[tablename]['fields'][fieldname] = {}
                    self.dbasetables[tablename]['fields'][fieldname]['PGtype'] = linesplit[1].strip()  # the pg type
                    self.dbasetables[tablename]['fields'][fieldname]['SLtype'] = linesplit[2].strip()  # the spatialite type
                    # the foreign key
                    if len(linesplit) > 3:
                        self.dbasetables[tablename]['fields'][fieldname]['FK'] = linesplit[3].strip()

                elif line[0:2] == '##':         # parent field constraint name
                    self.dbasetables[tablename]['fields'][fieldname]['ParFldCst'] = line[2:].strip()

                elif line[0] == '#':            # comment - pass
                    if line[0:5] == '#DJAN':
                        self.dbasetables[tablename]['djangoviewsql'] = line[5:].strip()
                    elif line[0:7] == '#QGISSL':
                        if 'qgisSLviewsql' in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]['qgisSLviewsql'] += ' ' + line[7:].strip() + ' '
                        else:
                            self.dbasetables[tablename]['qgisSLviewsql'] = line[7:].strip()
                    elif line[0:7] == '#QGISPG':
                        if 'qgisPGviewsql' in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]['qgisPGviewsql'] += ' ' + line[7:].strip() + ' '
                        else:
                            self.dbasetables[tablename]['qgisPGviewsql'] = line[7:].strip()
                    elif line[0:5] == '#QGIS':
                        if 'qgisviewsql' in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]['qgisviewsql'] += ' ' + line[5:].strip() + ' '
                        else:
                            self.dbasetables[tablename]['qgisviewsql'] = line[5:].strip()
                        # self.dbasetables[tablename]['qgisviewsql'] = line[5:].strip()
                    elif line[0:5] == '#EXPO':
                        self.dbasetables[tablename]['exportviewsql'] = line[5:].strip()
                    elif line[0:5] == '#SCAL':
                        self.dbasetables[tablename]['scale'] = float(line[5:].strip())
                    elif line[0:5] == '#SHOW':
                        value = line[5:].strip()
                        if value == 'YES':
                            self.dbasetables[tablename]['showinqgis'] = True
                    elif line[0:13] == '#SPATIALINDEX':
                        value = line[13:].strip()
                        if value == 'YES':
                            self.dbasetables[tablename]['spatialindex'] = True
                    else:
                        continue


                else:                           # field constraint
                    if 'Cst' in self.dbasetables[tablename]['fields'][fieldname].keys():
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'].append([])
                    else:
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'] = [[]]

                    if True:
                        linesplit = line.split(';')

                    if False:
                        if sys.version_info.major == 2:
                            linesplit = line.decode('utf-8').split(';')
                        elif sys.version_info.major == 3:
                            # print(line.__class__)
                            linesplit = line.split(';')
                            #print(type(linesplit[0]))
                            #linesplit = line.decode('utf-8').split(';')
                    if debug: logging.getLogger("Lamia").debug('cst line split %s %s',fieldname, str(linesplit))

                    self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(linesplit[0].strip())
                    self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(linesplit[1].strip())
                    if len(linesplit) > 2:
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(eval(linesplit[2].strip()))
                    else:
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(None)
                compt += 1

            file.close()

        if "Revision" in self.dbasetables.keys():
            self.revisionwork = True






    def _generateSpatialiteCreationSQL(self, name, dbasetable, crs):
        """!
        generate sql for creating Spatialite table

        @param name : name of the table to be created
        @param dbasetable : value linked with created table in self.dbasetables
        @param crs : crs used (int)

        @return sql{'main' : the create table sentence, 'other' : [list of sql sentences to e done after table creation] }

        main exemple :
        CREATE TABLE DESCRIPTIONSYSTEME (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,"
            name TEXT NOT NULL,
            ObjID INTEGER,
            FOREIGN KEY(ObjID) REFERENCES OBJECT(id)
         )
         other exemple:
         SELECT AddGeometryColumn('DESCRIPTIONSYSTEME','geom',2154, 'LINESTRING', 'XY')

        """

        sql = {}
        listFK = []
        sql['main'] = 'CREATE TABLE '
        sql['main'] += name + '('

        for key in dbasetable['fields']:
            if self.xlsreader:
                sltype = None
                if dbasetable['fields'][key]['PGtype'] in self.pgtypetosltype.keys():
                    sltype = self.pgtypetosltype[dbasetable['fields'][key]['PGtype']]
                elif 'VARCHAR' in dbasetable['fields'][key]['PGtype']:
                    sltype = 'TEXT'
                # print(name,key, dbasetable['fields'][key]['PGtype'], sltype )
                sql['main'] += key + ' ' + sltype + ','
            else:
                sql['main'] += key + ' ' + dbasetable['fields'][key]['SLtype'] + ','
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

    def _generatePostGisCreationSQL(self, name, dbasetable, crs):
        """!
        generate sql for creating Spatialite table

        @param name : name of the table to be created
        @param dbasetable : value linked with created table in self.dbasetables
        @param crs : crs used (int)

        @return sql{'main' : the create table sentence, 'other' : [list of sql sentences to e done after table creation] }

        main exemple :
        CREATE TABLE DESCRIPTIONSYSTEME (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,"
            name TEXT NOT NULL,
            ObjID INTEGER,
            FOREIGN KEY(ObjID) REFERENCES OBJECT(id)
         )
         other exemple:
         SELECT AddGeometryColumn('DESCRIPTIONSYSTEME','geom',2154, 'LINESTRING', 'XY')

        """

        sql = {}
        listFK = []
        sql['main'] = 'CREATE TABLE '
        sql['main'] += self.pgschema + '.' + name + '('

        for key in dbasetable['fields']:
            sql['main'] += key + ' ' + dbasetable['fields'][key]['PGtype']
            if 'FK' in dbasetable['fields'][key].keys():
                sql['main'] += ' REFERENCES ' + dbasetable['fields'][key]['FK']
            sql['main'] += ','

        if sql['main'][-1] == ',':
            sql['main'] = sql['main'][:-1]
        sql['main'] = sql['main'] + ');'

        if 'geom' in dbasetable.keys():
            sql['other'] = []
            sql['other'].append('ALTER TABLE ' + self.pgschema + '.' + name
                                + " ADD  COLUMN   geom geometry('" + dbasetable['geom'] + "'," + str(crs) + ");")

        return sql


    def loadQgisVectorLayers(self, file=None, dbasetype='spatialite', variante=None,
                             host='localhost', port=None, dbname=None, schema=None, user=None, password=None):
        """!
        Load dbase as Qgis layers
        put the layer in self.dbasetables['layer']
        """
        debug = False
        if debug: logging.getLogger('Lamia').debug('start')
        self.dbasetype = dbasetype

        if self.dbasetype == 'spatialite' and file is not None:
            self.spatialitefile = file
            if sys.version_info.major == 2:
                self.connSLITE = db.connect(file)
            elif sys.version_info.major == 3:
                self.connSLITE = qgis.utils.spatialite_connect(file)

            self.SLITEcursor = self.connSLITE.cursor()


        elif (self.dbasetype == 'postgis'
              and host is not None and port is not None and dbname is not None and schema is not None
              and user is not None and password is not None):
            self.pghost = host
            self.pgdb = dbname
            self.pguser = user
            self.pgpassword = password
            self.pgport = port
            self.pgschema = schema
            connectstr = "dbname='" + self.pgdb + "' user='" + self.pguser + "' host='"
            connectstr += self.pghost + "' password='" + self.pgpassword + "'"
            self.connPGis = psycopg2.connect(connectstr)
            #self.connPGis.autocommit = True
            self.PGiscursor = self.connPGis.cursor()
            sql = 'SET search_path TO ' + self.pgschema + ',public'
            self.query(sql)
            self.commit()

        if debug: logging.getLogger('Lamia').debug('step1')

        # self._AddDbaseInRecentsDBase(spatialitefile=file, host=host, port=port, dbname=dbname, schema=schema, user=user,password=password)
        # self.reInitDBase()

        version = None
        workversion = None
        variante = None


        sql = "SELECT metier, repertoireressources,crs, version   FROM Basedonnees;"
        query = self.query(sql)
        type, resdir, crs , version  = [row[0:4] for row in query][0]

        try:
            sql = "SELECT  workversion  FROM Basedonnees;"
            query = self.query(sql)
            workversion  = [row[0] for row in query][0]
        except TypeError:
            return


        try:
            sql = "SELECT  variante  FROM Basedonnees;"
            query = self.query(sql)
            variante  = [row[0] for row in query][0]
        except:
            pass

        """
        except:
            sql = "SELECT metier, repertoireressources,crs, version FROM Basedonnees;"
            query = self.query(sql)
            type, resdir, crs , version= [row[0:4] for row in query][0]
        """


        if resdir[0] == '.' and self.dbasetype == 'spatialite':
            self.dbaseressourcesdirectory = os.path.join(os.path.dirname(self.spatialitefile ), resdir)
        else:
            self.dbaseressourcesdirectory = os.path.normpath(resdir)
        self.crsnumber = crs
        self.qgiscrs = qgis.core.QgsCoordinateReferenceSystem(self.crsnumber)
        self.version = version
        self.workversion = workversion
        self.variante = variante

        if self.qgsiface is None:
            print(type, resdir, crs , version, workversion, variante)

        self.createRessourcesDir(self.dbasetype,self.dbaseressourcesdirectory )

        if debug: logging.getLogger('Lamia').debug('step2')

        if type is not None:
            if not self.xlsreader:
                self.createDBDictionary(type)
                self.createDBDictionary(type, configdir=True)
            else:
                self.createDBDictionary2(type)
                self.createDBDictionary2(type, configdir=True)





            if self.revisionwork:
                sql = "SELECT MAX(pk_revision) FROM Revision;"
                query = self.query(sql)
                self.currentrevision = query[0][0]
                if debug: logging.getLogger('Lamia').debug('rev : %s', str(self.currentrevision) )


            # create a list of tables to load
            if False:
                listoftabletoload = []
                for tablename in self.dbasetables:
                    if 'geom' in self.dbasetables[tablename] :
                        listoftabletoload.append((tablename, self.dbasetables[tablename]['geom']))
                    else:
                        listoftabletoload.append((tablename, None))

            # load the table as qgsvectorlayer
            #for tablename, geom in listoftabletoload:
            for tablename in self.dbasetables:
                if int(str(self.qgisversion_int)[0:3]) < 220:
                    uri = qgis.core.QgsDataSourceURI()
                else:
                    uri = qgis.core.QgsDataSourceUri()
                if self.dbasetype == 'spatialite':
                    uri.setDatabase(file)

                    # raw layer

                    if self.isTableSpatial(tablename):
                        uri.setDataSource('', str(tablename), 'geom')
                    else:
                        uri.setDataSource('', str(tablename), '')

                    self.dbasetables[tablename]['layer'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'spatialite')

                    # view layer qgis

                    #get id column
                    idcolumnname = self.getFirstIdColumn(tablename + '_qgis')
                    # print('***', tablename + '_qgis' , idcolumnname)
                    #if sys.version_info.major == 2:       #bug on qgis 3
                    if True:
                        if self.isTableSpatial(str(tablename)+'_qgis'):
                            if 'spatialindex' in self.dbasetables[tablename].keys() and sys.version_info.major == 3:    #qis 3 bug
                                uri.setDataSource('', '(SELECT * FROM ' + str(tablename) + '_qgis)', 'geom', '',idcolumnname)
                            else:
                                uri.setDataSource('', str(tablename) + '_qgis', 'geom', '', idcolumnname)

                            if False:
                                if 'spatialindex' in self.dbasetables[tablename].keys() and sys.version_info.major == 3:
                                    uri.setDataSource('', str(tablename) + '_qgis', 'geometry', '', idcolumnname)
                                else:
                                    #uri.setDataSource('', str(tablename)+'_qgis', 'geom', '', "id_" + str(tablename).lower())
                                    uri.setDataSource('', str(tablename) + '_qgis', 'geom', '', idcolumnname)

                        else:
                            #uri.setDataSource('', str(tablename) + '_qgis', '', '', "id_" + str(tablename).lower())
                            uri.setDataSource('', str(tablename) + '_qgis', '', '', idcolumnname)

                        self.dbasetables[tablename]['layerqgis'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'spatialite')


                    if False:
                        if sys.version_info.major == 3:
                            if self.isTableSpatial(str(tablename) + '_qgis'):
                                # uri.setDataSource('', str(tablename)+'_qgis', 'geom', '', "id_" + str(tablename).lower())
                                uri.setDataSource('', '(SELECT * FROM ' + str(tablename) + '_qgis)', 'geom', '', idcolumnname)

                            else:
                                # uri.setDataSource('', str(tablename) + '_qgis', '', '', "id_" + str(tablename).lower())
                                uri.setDataSource('', '(SELECT * FROM ' + str(tablename) + '_qgis)', '', '', idcolumnname)
                            self.dbasetables[tablename]['layerqgis'] = qgis.core.QgsVectorLayer(uri.uri(), tablename,
                                                                                                'spatialite')

                    # view layer django
                    idcolumnname = self.getFirstIdColumn(tablename + '_django')
                    # print('***', tablename+ '_django' , idcolumnname)

                    #if geom is not None:
                    if self.isTableSpatial(str(tablename) + '_django'):
                        #uri.setDataSource('', str(tablename)+'_django', 'geom', '', "id_" + str(tablename).lower())
                        uri.setDataSource('', str(tablename) + '_django', 'geom', '', idcolumnname)
                    else:
                        # uri.setDataSource('', str(tablename) + '_django', '', '', "id_" + str(tablename).lower())
                        uri.setDataSource('', str(tablename) + '_django', '', '', idcolumnname)
                    self.dbasetables[tablename]['layerdjango'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'spatialite')




                elif self.dbasetype == 'postgis':
                    uri.setConnection(self.pghost, str(self.pgport), self.pgdb, self.pguser, self.pgpassword)
                    tablenamelayer = tablename.lower()
                    # raw layer
                    # if geom is not None:
                    if self.isTableSpatial(tablenamelayer):
                        uri.setDataSource(self.pgschema, str(tablenamelayer), 'geom', '', "id_" + str(tablenamelayer))
                    else:
                        uri.setDataSource(self.pgschema, str(tablenamelayer), None, '', "'id_" + str(tablenamelayer))
                    self.dbasetables[tablename]['layer'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'postgres')
                    # view layer qgis
                    #if geom is not None:
                    if self.isTableSpatial(str(tablenamelayer) + '_qgis'):
                        uri.setDataSource(self.pgschema, str(tablenamelayer) + '_qgis', 'geom', '', "id_" + str(tablenamelayer))
                    else:
                        uri.setDataSource(self.pgschema, str(tablenamelayer) + '_qgis', None, '', "id_" + str(tablenamelayer))
                    self.dbasetables[tablename]['layerqgis'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'postgres')
                    # view layer django
                    #if geom is not None:
                    if self.isTableSpatial(str(tablenamelayer) + '_django'):
                        uri.setDataSource(self.pgschema, str(tablenamelayer) + '_django', 'geom', '', "id_" + str(tablenamelayer))
                    else:
                        uri.setDataSource(self.pgschema, str(tablenamelayer) + '_django', None, '', "id_" + str(tablenamelayer))
                    self.dbasetables[tablename]['layerdjango'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'postgres')

                if False:
                    # style and loading
                    stylepath = os.path.join(os.path.dirname(__file__), '..',
                                             'DBASE', 'style', self.type, self.dbasetables[tablename]['layer'].name() + '.qml')


                    if os.path.isfile(stylepath):
                        self.dbasetables[tablename]['layerqgis'].loadNamedStyle(stylepath)

                if False:
                    #load qgsvectorlayers and add to canvas if #showinqgis

                    if self.dbasetables[tablename]['showinqgis']:
                        if int(str(self.qgisversion_int)[0:3]) < 220:
                            qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbasetables[tablename]['layerqgis'],
                                                                                 True)
                        else:
                            qgis.core.QgsProject.instance().addMapLayer(self.dbasetables[tablename]['layerqgis'],
                                                                                 True)
                    else:
                        if int(str(self.qgisversion_int)[0:3]) < 220:
                            qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbasetables[tablename]['layer'],
                                                                                 False)
                        else:
                            qgis.core.QgsProject.instance().addMapLayer(self.dbasetables[tablename]['layer'],
                                                                                 False)

                    if 'scale' in self.dbasetables[tablename].keys():
                        self.dbasetables[tablename]['layerqgis'].setScaleBasedVisibility(True)
                        if int(str(self.qgisversion_int)[0:3]) < 220:
                            self.dbasetables[tablename]['layerqgis'].setMaximumScale(self.dbasetables[tablename]['scale'])
                        else:
                            self.dbasetables[tablename]['layerqgis'].setMinimumScale(self.dbasetables[tablename]['scale'])

                if False:
                    if os.path.isfile(stylepath):
                        self.dbasetables[tablename]['layer'].loadNamedStyle(stylepath)

                    if self.dbasetables[tablename]['showinqgis']:
                        if int(str(self.qgisversion_int)[0:3]) < 220:
                            qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbasetables[tablename]['layer'],
                                                                                 True)
                        else:
                            qgis.core.QgsProject.instance().addMapLayer(self.dbasetables[tablename]['layer'],
                                                                                 True)

            if debug: logging.getLogger('Lamia').debug('step3')


            self.updateQgsCoordinateTransformFromLayerToCanvas()

            if self.revisionwork:
                self.maxrevision = self.getMaxRevision()


            self.dBaseLoaded.emit()


        if debug: logging.getLogger('Lamia').debug('end')


    def createQgsVectorLayer(self,tablename='tempvectorlayer',isspatial = True,  sql='', tableid=None):
        layer = None

        if tableid is not None:
            finaltableid = tableid
        else:
            finaltableid = "id_" + str(tablename.lower())

        if int(str(self.qgisversion_int)[0:3]) < 220:
            uri = qgis.core.QgsDataSourceURI()
        else:
            uri = qgis.core.QgsDataSourceUri()

        if 'SELECT' in sql :
            sql = '(' + sql + ')'

        if self.dbasetype == 'spatialite':
            # uri.setDataSource("public","japan_ver52","the_geom","","gid")
            # uri.setDataSource("",sql,"the_geom","","gid")
            uri.setDatabase(self.spatialitefile)
            if isspatial:
                uri.setDataSource('', sql , 'geom' ,'',finaltableid)
            else:
                uri.setDataSource('', sql, '', '', finaltableid)

            layer = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'spatialite')



        elif self.dbasetype == 'postgis':
            uri.setConnection(self.pghost, str(self.pgport), self.pgdb, self.pguser, self.pgpassword)
            if isspatial:
                uri.setDataSource(self.pgschema, sql, 'geom', sql, finaltableid)
            else:
                uri.setDataSource(self.pgschema, sql, None, sql , finaltableid )

            layer = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'postgres')

        return layer


    def query(self, sql,arguments=[], docommit=True):

        if self.printsql :
            timestart = self.getTimeNow()

        if self.dbasetype == 'spatialite':
            # cursor = self.connSLITE.cursor()
            if self.SLITEcursor is None:
                # self.connSLITE = db.connect(self.spatialitefile)
                self.SLITEcursor = self.connSLITE.cursor()
            try:
                if self.printsql :
                    logging.getLogger('Lamia').debug('%s %.3f', sql,  self.getTimeNow() - timestart)
                query = self.SLITEcursor.execute(sql,arguments)
                returnquery = list(query)
                if docommit:
                    self.commit()

                return returnquery
            except (OperationalError ,IntegrityError) as e:
                if self.qgsiface is None:
                    print(sql)
                    print('error query', e)
                return None




        elif self.dbasetype == 'postgis':
            if self.PGiscursor is None:
                # connectstr = "dbname='" + self.pgdb + "' user='" + self.pguser + "' host='"
                # connectstr += self.pghost + "' password='" + self.pgpassword + "'"
                # self.connPGis = psycopg2.connect(connectstr)
                self.PGiscursor = self.connPGis.cursor()

            try:
                if self.printsql :
                    logging.getLogger('Lamia').debug('%s %.3f', sql,  self.getTimeNow() - timestart)
                self.PGiscursor.execute(sql)

            except psycopg2.ProgrammingError as e:
                print('error', sql)
                print('error query', e)
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



    def updateQueryTableNow(self, sqlin, date=None):
        #sqllist = sqlin.split(' ')
        sqllist = re.split(' |,|\(|\)|\.|=', sqlin)
        withsql = ''
        alreadytables=[]
        for sqlword in sqllist:
            if '_now' in sqlword:
                tablename=sqlword.split('_now')[0]
                if tablename.lower() not in  alreadytables:
                    alreadytables.append(tablename.lower())
                    withsql +=  sqlword + " AS "
                    withsql += " (SELECT * FROM " + tablename.lower() + "_qgis WHERE "
                    withsql += self.dateVersionConstraintSQL(date)
                    withsql += "), "

        withsql = withsql[0:-2]
        if False and withsql == '':
            withsql = ''

        sqltemp1 = self.splitSQLSelectFromWhereOrderby(sqlin)

        sqlout = ''
        if 'WITH' in sqltemp1.keys():
            sqlout += 'WITH ' + sqltemp1['WITH']
            sqlout += ', ' + withsql
            sqlout += ' SELECT ' + sqltemp1['SELECT'] + ' FROM ' + sqltemp1['FROM']+ ' WHERE ' + sqltemp1['WHERE']
            if 'ORDER' in sqltemp1.keys():
                sqlout += ' ORDER BY ' + sqltemp1['ORDER']
            if 'GROUP' in sqltemp1.keys():
                sqlout += ' GROUP BY ' + sqltemp1['GROUP']

        elif withsql != '':
            sqlout += 'WITH ' + withsql + sqlin

        else:
            sqlout += sqlin



        return sqlout



    def splitSQLSelectFromWhereOrderby(self,sqlin):
        sqltemp = sqlin.split(' ')
        indexparenthesis=0

        specwords = ['WITH', 'SELECT', 'FROM', 'WHERE', 'GROUP','ORDER']
        listres={}
        actualsqlword = None
        for sqlword in sqltemp:
            if '(' in sqlword or ')' in sqlword:
                indexparenthesis += sqlword.count('(')
                indexparenthesis += - sqlword.count(')')
                listres[actualsqlword] += ' ' + sqlword
            elif  sqlword in specwords and indexparenthesis == 0 :
                actualsqlword = sqlword
                listres[actualsqlword] = ''
            else:
                if actualsqlword:
                    listres[actualsqlword] += ' ' + sqlword

        if 'GROUP' in listres.keys():
            listres['GROUP'] = ' '.join(listres['GROUP'].strip().split(' ')[1:])

        return listres

    def rebuildSplittedQuery(self, sqlin):
        sqlout = ''
        if 'WITH' in sqlin.keys():
            sqlout += ' WITH ' + sqlin['WITH']
        if 'SELECT' in sqlin.keys():
            sqlout += ' SELECT ' + sqlin['SELECT']
        if 'FROM' in sqlin.keys():
            sqlout += ' FROM ' + sqlin['FROM']
        if 'WHERE' in sqlin.keys():
            sqlout += ' WHERE ' + sqlin['WHERE']
        if 'GROUP' in sqlin.keys():
            sqlout += ' GROUP BY ' + sqlin['GROUP']
        if 'ORDER' in sqlin.keys():
            sqlout += ' ORDER BY ' + sqlin['ORDER']
        return sqlout



    def query2(self, sql):
        if self.dbasetype == 'spatialite':
            # cursor = self.connSLITE.cursor()
            query = self.SLITEcursor.execute(sql)
            return query
        elif self.dbasetype == 'postgis':
            self.PGiscursor.execute(sql)
            try:
                rows = self.PGiscursor.fetchall()
                return rows
            except psycopg2.ProgrammingError:
                return None

    def vacuum(self,table):
        """
        Methode invoquée pour faire des vacuum dans la BD lamia en cours d'utilisation
        """
        self.commit()   #nedd to be done before vacuum
        if self.dbasetype == 'spatialite':
            sql = "VACUUM " + str(table)
            self.query(sql)
        elif self.dbasetype == 'postgis':
            old_isolation_level = self.connPGis.isolation_level
            self.connPGis.set_isolation_level(0)
            sql = "VACUUM " + str(table)
            self.query(sql)
            self.connPGis.set_isolation_level(old_isolation_level)


    def commit(self):
        """
        Methode invoquée pour faire des commits dans la BD lamia en cours d'utilisation
        """
        if self.dbasetype == 'spatialite':
            self.connSLITE.commit()
        elif self.dbasetype == 'postgis':
            self.connPGis.commit()

    if False:
        def _readRecentDBase(self):
            """
            Lit le fichier des bases de données recentes et rempli le  menu//Fichier//base de données recentes
            """
            pathrecentproject = os.path.join(os.path.dirname(__file__), '..', 'config', 'recentprojects.txt')
            try:
                file = open(pathrecentproject, "r")
                lines = file.readlines()
                file.close()
                self.recentsdbase = []
                for line in lines:
                    if os.path.isfile(line.strip()):
                        self.recentsdbase.append(line.strip())
                    elif len(line.split(';')) == 3:
                        self.recentsdbase.append(line.strip())
            except :
                pass
            self.recentDBaseChanged.emit()

        def _AddDbaseInRecentsDBase(self, spatialitefile=None, host='localhost',
                                    port=None, dbname=None, schema=None, user=None, password=None):
            """
            Methode appelée lors du chargement d'une BD lamia
            Ajoute le chemin dans le fichier chargé dans Menu//Fichier//base de données recentes
            """
            if self.dbasetype == 'spatialite':
                if spatialitefile in self.recentsdbase:
                    index = self.recentsdbase.index(spatialitefile)
                    del self.recentsdbase[index]
                self.recentsdbase.insert(0, spatialitefile)
                self._saveRecentDBase()
                self.recentDBaseChanged.emit()
            elif self.dbasetype == 'postgis':
                name = dbname + '.' +schema  + '@' + host + ':' + str(port) + ';' + user + ';' + password
                if name in self.recentsdbase:
                    index = self.recentsdbase.index(name)
                    del self.recentsdbase[index]
                self.recentsdbase.insert(0, name)
                self._saveRecentDBase()
                self.recentDBaseChanged.emit()


        def _saveRecentDBase(self):
            """
            Sauve le path de la BD lamia en cours d'utilisation dans le ficier employé dans
            menu//Fichier//base de données recentes
            """
            pathrecentproject = os.path.join(os.path.dirname(__file__), '..', 'config', 'recentprojects.txt')
            file = open(pathrecentproject, "w")
            for i, path in enumerate(self.recentsdbase):
                if i > 10:
                    break
                if not path == '':
                    file.write(path + '\n')
            file.close()
            self.recentDBaseChanged.emit()


    def reInitDBase(self):

        self.dbasetables = None



    def reInitDBase2(self):
        """
        Methode appelée lors d'un changement de base de données
        Reinitialise toutes les variables
        """
        if self.dbasetables is not None:
            for layername in self.dbasetables.keys():
                if 'layer' in self.dbasetables[layername]:
                    if int(str(self.qgisversion_int)[0:3]) < 220:
                        try:
                            qgis.core.QgsMapLayerRegistry.instance().removeMapLayer(self.dbasetables[layername]['layer'])
                        except:
                            pass
                    else:
                        try:
                            qgis.core.QgsProject.instance().removeMapLayer(self.dbasetables[layername]['layer'])
                        except:
                            pass

                if 'layerqgis' in self.dbasetables[layername]:
                    if int(str(self.qgisversion_int)[0:3]) < 220:
                        try:
                            qgis.core.QgsMapLayerRegistry.instance().removeMapLayer(self.dbasetables[layername]['layerqgis'])
                        except:
                            pass
                    else:
                        try:
                            qgis.core.QgsProject.instance().removeMapLayer(self.dbasetables[layername]['layerqgis'])
                        except:
                            pass

                if 'widget' in self.dbasetables[layername]:
                    self.dbasetables[layername]['widget'] = []

                    if False:
                        if not isinstance(self.dbasetables[layername]['widget'],list):
                            tablewdgs = [self.dbasetables[layername]['widget']]
                        else:
                            tablewdgs = self.dbasetables[layername]['widget']

                        for tablewdg in tablewdgs:
                            tablewdg.onActivationRaw(None)

                            try:
                                tablewdg.unloadWidgetinMainTree()
                            except Exception as e:
                                print('unload', e)


                            if tablewdg.linkedtreewidget is not None:
                                try:
                                    tablewdg.linkedtreewidget.disconnect()
                                except:
                                    pass
                            tablewdg.dbasetable = None

        self.dbasetables = None

    def updateWorkingDate(self):
        """
        Methode appelée lorsque la date de travail (self.workingdate) ou la version de travail (self.currentrevision)
        est modifiée
        Change les filtres de toutes les tables qgis en fonction
        """


        workingdatemodif = QtCore.QDate.fromString(self.workingdate, 'yyyy-MM-dd').addDays(1).toString('yyyy-MM-dd')


        if self.version is None or self.version == '':
            if self.dbasetype == 'spatialite':
                subsetstring = '"datecreation" <= ' + "'" + workingdatemodif + "'"
                subsetstring += ' AND CASE WHEN "datedestruction" IS NOT NULL  THEN "datedestruction" > ' + "'" + workingdatemodif + "'" + ' ELSE 1 END'
                if self.revisionwork:
                    subsetstring += ' AND "revisionbegin" <= ' + str(self.currentrevision)
                    subsetstring += ' AND CASE WHEN "revisionend" IS NOT NULL  THEN "revisionend" > '  + str(self.currentrevision)  + ' ELSE 1 END'

            elif self.dbasetype == 'postgis':
                subsetstring = '"datecreation" <= ' + "'" + workingdatemodif + "'"
                subsetstring += ' AND CASE WHEN "datedestruction" IS NOT NULL  THEN "datedestruction" > ' + "'" + workingdatemodif + "'" + ' ELSE TRUE END'
                if self.revisionwork:
                    subsetstring += ' AND "revisionbegin" <= ' + str(self.currentrevision)
                    subsetstring += ' AND CASE WHEN "revisionend" IS NOT NULL  THEN "revisionend" > '  + str(self.currentrevision)  + ' ELSE TRUE END'
        else:
            if self.dbasetype == 'spatialite':
                subsetstring = '"datetimecreation" <= ' + "'" + workingdatemodif + "'"
                subsetstring += ' AND CASE WHEN "datetimedestruction" IS NOT NULL  THEN "datetimedestruction" > ' + "'" + workingdatemodif + "'" + ' ELSE 1 END'
                if self.revisionwork:
                    subsetstring += ' AND "lpk_revision_begin" <= ' + str(self.currentrevision)
                    subsetstring += ' AND CASE WHEN "lpk_revision_end" IS NOT NULL  THEN "lpk_revision_end" > ' + str(
                        self.currentrevision) + ' ELSE 1 END'

            elif self.dbasetype == 'postgis':
                subsetstring = '"datetimecreation" <= ' + "'" + workingdatemodif + "'"
                subsetstring += ' AND CASE WHEN "datetimedestruction" IS NOT NULL  THEN "datetimedestruction" > ' + "'" + workingdatemodif + "'" + ' ELSE TRUE END'
                if self.revisionwork:
                    subsetstring += ' AND "lpk_revision_begin" <= ' + str(self.currentrevision)
                    subsetstring += ' AND CASE WHEN "lpk_revision_end" IS NOT NULL  THEN "lpk_revision_end" > ' + str(
                        self.currentrevision) + ' ELSE TRUE END'


        for tablename in self.dbasetables:
            fieldnames = [field.name().lower() for field in self.dbasetables[tablename]['layerqgis'].fields()]
            if 'datecreation' in fieldnames or 'datetimecreation' in fieldnames :
                self.dbasetables[tablename]['layerqgis'].setSubsetString(subsetstring)
                self.dbasetables[tablename]['layerqgis'].triggerRepaint()


    def updateQgsCoordinateTransformFromLayerToCanvas(self):
        """
        Methode appellée lorsque le crs du canvas qgis change
        met à jour self.xform et self.xformreverse pour effectuer les transformations crs canvas <-> crs lamia
        """
        if self.qgiscrs is not None and self.canvas is not None:
            if int(str(self.qgisversion_int)[0:3]) < 220:
                self.xform = qgis.core.QgsCoordinateTransform(self.qgiscrs,
                                                              self.canvas.mapSettings().destinationCrs())
                self.xformreverse = qgis.core.QgsCoordinateTransform(self.canvas.mapSettings().destinationCrs(),
                                                                     self.qgiscrs)
            else:
                self.xform = qgis.core.QgsCoordinateTransform(self.qgiscrs,
                                                              self.canvas.mapSettings().destinationCrs(),
                                                              qgis.core.QgsProject.instance() )
                self.xformreverse = qgis.core.QgsCoordinateTransform(self.canvas.mapSettings().destinationCrs(),
                                                                     self.qgiscrs,
                                                                    qgis.core.QgsProject.instance() )


    def getConstraintRawValueFromText(self, table, field, txt):
        """
        Convertie la valeur textuelle  txt de la table lamia "table" vers sa valeur trigramme
        :param table: la table lamia considérée
        :param field: la colonne considérée
        :param txt: la valeur textuelle
        :return: le trigramme
        """
        # print('_getConstraintRawValueFromText',[value[0] for value in self.dbasetables[table]['fields'][field]['Cst']], txt )
        dbasetable = self.dbasetables[table]
        try:
            index = [value[0] for value in dbasetable['fields'][field]['Cst']].index(txt)
            return dbasetable['fields'][field]['Cst'][index][1]
        except ValueError as e:
            if self.qgsiface is None :
                logging.getLogger("Lamia").debug('error %s %s %s %s',e, table,field , str([value[0] for value in dbasetable['fields'][field]['Cst']] ))
            return None

    def getConstraintTextFromRawValue(self, table, field, rawvalue):
        """
        Convertie le trigramme rawvalue de la table lamia "table" vers sa valeur textuelle
        :param table: la table lamia considérée
        :param field: la colonne considérée
        :param rawvalue: le trigramme ou valeur stockée considérée
        :return: la valeur textuelle
        """
        # print('_getConstraintTextFromRawValue',table, self.dbasetables[table]['fields'][field], rawvalue,field)
        # print('_getConstraintTextFromRawValue',table, field, rawvalue )

        if (table in self.dbasetables.keys()
            and field in self.dbasetables[table]['fields'].keys()
            and 'Cst' in self.dbasetables[table]['fields'][field].keys()):

            dbasetable = self.dbasetables[table]
            #if field in dbasetable['fields'].keys() and 'Cst' in dbasetable['fields'][field].keys():
            if not self.isAttributeNull(rawvalue):
                if isinstance(rawvalue, int) or isinstance(rawvalue, long):
                    rawvalue = str(rawvalue)

                try:
                    index = [value[1] for value in dbasetable['fields'][field]['Cst']].index(rawvalue)
                    return dbasetable['fields'][field]['Cst'][index][0]
                except ValueError as e:
                    if qgis.utils.iface is None:
                        print('getConstraintTextFromRawValue error', table, field, e, [value[1] for value in dbasetable['fields'][field]['Cst']])
                    return str(rawvalue)

            else:
                return ''
        else:
            if not self.isAttributeNull(rawvalue):
                # print(table, field, rawvalue, type(rawvalue))
                return rawvalue
                if False:
                    if sys.version_info.major == 2:
                        if isinstance(rawvalue, unicode):
                            return rawvalue.encode('utf-8')
                        else:
                            return rawvalue
                else:
                    return rawvalue
            else:
                return ''

    def isAttributeNull(self ,attr):
        """
        Vérifie si un qgisfeature attribute est NULL - piégeux car le NULL peu prendre plusieurs formes
        :param attr: get an qgisfeature attribute
        :return: True if NULL, else False
        """
        if int(str(self.qgisversion_int)[0:3]) < 220 and isinstance(attr, QtCore.QPyNullVariant):
            return True
        elif int(str(self.qgisversion_int)[0:3]) > 220 and isinstance(attr, QtCore.QVariant) and attr.isNull():
            return True
        elif (isinstance(attr,unicode) or isinstance(attr,str)) and (attr == 'NULL' or attr == '' or attr == 'None') :
            return True
        elif attr is None:
            return True
        else:
            return False

    def isTableSpatial(self, tablename):
        """
        Permet de savoir si une table lamia est spatiale en cherchant le mot clé 'geom' dans la liste des colonnes
        :param tablename: la table à analyser
        :return: True si 'geom' est trouvé, False sinon
        """

        if self.dbasetype == 'spatialite':
            sql = "PRAGMA table_info(" + str(tablename) + ")"
            query = self.query(sql)
            result = [row[1] for row in query]
            #print(result)
            if 'geom' in result:
                return True

        elif self.dbasetype == 'postgis':
            sql = "SELECT column_name FROM information_schema.columns WHERE table_name  = '" +  str(tablename).lower() + "'"
            query = self.query(sql)
            result = [row[0] for row in query]
            if 'geom' in result:
                return True

        return False

    def getNearestPk(self, dbasetable, dbasetablename, point, comefromcanvas=True):
        """
        Permet d'avoir le pk du feature le plus proche du qgsvectorlayer correspondant à dbasetablename
        pas besoin de filtre sur les dates et versions on travaille avec le qgsectorlyaer de la table
        qui dispose déjà d'un filtre en fonction de la date et de la version
        :param dbasetable: la dbasetable considérée
        :param dbasetablename:  le nom de la dbasetable
        :param point: le point dont on veut connaitre le plus proche élément
        :param comefromcanvas: spécifie sir le point provient du canvas qgis (nécessité de trasformation) ou non
        :return: le pk de la table dbasetablenamele plus proche du point
        """

        debug = False
        if debug:
            timestart = self.getTimeNow()

        # vérifie que la table est spatiale
        if int(str(self.qgisversion_int)[0:3]) < 218:
            isspatial = dbasetable['layerqgis'].geometryType() < 3
        else:
            isspatial = dbasetable['layerqgis'].isSpatial()
        if not isspatial:
            return None, None

        # Effectue la transformation geographique si necessaire
        if debug: logging.getLogger("Lamia").debug('pointbefore %s', str(point))
        if comefromcanvas:
            if self.qgsiface is not None:
                point2 = self.xformreverse.transform(point)
            else:
                point2 = point
        else:
            point2 = point
        if debug: logging.getLogger("Lamia").debug('pointafter %s', str(point2))

        # créé l'index spatial
        spindex = qgis.core.QgsSpatialIndex(dbasetable['layerqgis'].getFeatures())

        layernearestid = spindex.nearestNeighbor(point2, 1)

        #on cherche la geometry du nearestid
        if int(str(self.qgisversion_int)[0:3]) < 220:
            point2geom = qgis.core.QgsGeometry.fromPoint(point2)
        else:
            point2geom = qgis.core.QgsGeometry.fromPointXY(point2)

        if not self.revisionwork:
            nearestfet = self.getLayerFeatureById(dbasetablename, layernearestid[0])
        else:
            nearestfet = self.getLayerFeatureByPk(dbasetablename, layernearestid[0])

        nearestfetgeom = nearestfet.geometry()



        # cas d'un point : le nearestNeighbor renvoi la bonne valeur
        if dbasetable['layerqgis'].geometryType() == 0:
            disfrompoint = nearestfetgeom.distance(point2geom)
            return layernearestid[0], disfrompoint




        # cas d'une ligne ou polygone : comme la recherce se fait su une boundingbox, il faut filtrer les
        # elements dans cette box
        else:
            # clean nearestfet geometry if not valid
            if int(str(self.qgisversion_int)[0:3]) < 220:
                if not nearestfetgeom.isGeosValid() and nearestfetgeom.type() == 1:
                    nearestfetgeom = qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(nearestfetgeom.asPolyline()[0]))
            else:
                if not nearestfetgeom.isGeosValid() and nearestfetgeom.type() == 1:
                    nearestfetgeom = qgis.core.QgsGeometry.fromPointXY(qgis.core.QgsPointXY(nearestfetgeom.asPolyline()[0]))

            disfrompoint = nearestfetgeom.distance(point2geom)

            if debug: logging.getLogger("Lamia").debug('nearestfetgeom - dist %s %s', str(nearestfetgeom.exportToWkt()), str(disfrompoint))
            if disfrompoint < 0.1:
                disfrompoint = 0.1

            bboxtofilter = point2geom.buffer(disfrompoint * 1.2, 12).boundingBox()
            idsintersectingbbox = spindex.intersects(bboxtofilter)

            if debug: logging.getLogger("Lamia").debug('idsintersectingbbox %s', str(idsintersectingbbox))

            # search nearest geom in bbox
            distance = None
            nearestindex = None
            finalgeomispoint = False
            distanceratio = 1.2

            for intersectingid in idsintersectingbbox:
                ispoint = False
                if not self.revisionwork:
                    feat = self.getLayerFeatureById(dbasetablename, intersectingid)
                else:
                    feat = self.getLayerFeatureByPk(dbasetablename, intersectingid)
                featgeom = feat.geometry()

                if debug: logging.getLogger("Lamia").debug('intersectingid %s  - is valid : %s - type : %s - multi : %s',
                                                           str(intersectingid), str(featgeom.isGeosValid()),
                                                           str(featgeom.type()), str(featgeom.isMultipart()))

                if featgeom.isGeosValid():  # if not valid, return dist = -1...
                    dist = featgeom.distance(point2geom)
                else:  # point
                    if featgeom.type() == 1 and not featgeom.isMultipart():

                        ispoint = True
                        if int(str(self.qgisversion_int)[0:3]) < 220:
                            if len(featgeom.asPolyline()) == 1:  # polyline of 1 point
                                dist = qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(featgeom.asPolyline()[0])).distance(point2geom)
                            elif len(featgeom.asPolyline()) == 2 and featgeom.asPolyline()[0] == featgeom.asPolyline()[1]:
                                dist = qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(featgeom.asPolyline()[0])).distance(point2geom)
                        else:
                            if len(featgeom.asPolyline()) == 1:  # polyline of 1 point
                                dist = qgis.core.QgsGeometry.fromPointXY(qgis.core.QgsPointXY(featgeom.asPolyline()[0])).distance(point2geom)
                            elif len(featgeom.asPolyline()) == 2 and featgeom.asPolyline()[0] == featgeom.asPolyline()[1]:
                                dist = qgis.core.QgsGeometry.fromPointXY(qgis.core.QgsPointXY(featgeom.asPolyline()[0])).distance(point2geom)
                    else:
                        continue
                if debug: logging.getLogger("Lamia").debug('distance : %s - ispoint : %s', str(dist), str(ispoint))
                # algo for keeping point in linestring layer as nearest
                # if point is nearest than 1.2 x dist from nearest line
                if debug: logging.getLogger("Lamia").debug('distance : %s - ispoint : %s - geomfinalispoint : %s - finaldist : %s' ,
                                                           str(dist), str(ispoint), str(finalgeomispoint), str(distance))
                if distance is None:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = ispoint
                elif not finalgeomispoint and ispoint and dist < distance*distanceratio:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = True
                elif finalgeomispoint and not ispoint and dist < distance/distanceratio:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = False
                elif finalgeomispoint == ispoint and dist < distance:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = ispoint


        if debug: logging.getLogger("Lamia").debug('nearestpk, dist %s %s', str(nearestindex), str(distance))
        return nearestindex, distance

    def areNodesEquals(self, node1, node2):
        """
        Fonction pour examiner l'égalité géographique de deux points.
        Nécessaire car parfois les arrondis des coordonnées géographiques font que deux points égaux ont une
        différence de qques micromètres
        :param node1: point1 (list 2x1)
        :param node2: point2 (list 2x1)
        :return: Boolean, en fonction de l'égalité geographique des points
        """
        dist = math.sqrt( (node2[0] - node1[0])**2 + (node2[1]-node1[1])**2 )
        if dist < 0.01:
            return True
        else:
            return False

    def getLayerFeatureById(self, layername, fid):
        """
        Renvoie le QgsFeature de la table lamia nommée layername dont le id est fid
        Remarque : on demande ici l'id et non la cle primaire de la table
        Remarquebis : on fait la requete sur le qgsvectorlayer de la table (dans self.dbasetables[layername]['layerqgis'])
                      du coup, comme ce qgsvectorlayer dispose déjà d'un filtre en fonction de la date et de la version,
                      pas besoin de requeter en plus sur ce sujet
        :param layername: le nom de la table dans la BD lamia
        :param fid: le id dont on veut le feature
        :return: le QgsFeature associé au id demandé
        """
        if not self.revisionwork:
            if int(str(self.qgisversion_int)[0:3]) < 220:
                return self.dbasetables[layername]['layer'].getFeatures(qgis.core.QgsFeatureRequest(fid)).next()
            else:
                return self.dbasetables[layername]['layer'].getFeature(fid)
        else:
            # requete pour avoir le feature avec l'id demandé, puis on ndemande le pk_XXX de ce feature
            # ex : request =  qgis.core.QgsFeatureRequest().setFilterExpression(' "some_field_name" = \'some_value\' ')
            if False:
                sql = "SELECT pk_" + str(layername).lower() + " FROM " + layername + '_qgis  '
                sql += 'WHERE id_' + str(layername).lower() + ' = ' + str(fid) + ' AND '
                sql += self.dateVersionConstraintSQL()
                pk = self.query(sql)[0][0]
                if int(str(self.qgisversion_int)[0:3]) < 220:
                    return self.dbasetables[layername]['layer'].getFeatures(qgis.core.QgsFeatureRequest(pk)).next()
                else:
                    return self.dbasetables[layername]['layer'].getFeature(pk)

            if self.version is None or self.version == '' :
                txtrequest = ' "id_' + layername.lower() + '" =  ' + str(fid)
                request = qgis.core.QgsFeatureRequest().setFilterExpression(txtrequest)
                # request.setFlags(qgis.core.QgsFeatureRequest.NoGeometry)
                if int(str(self.qgisversion_int)[0:3]) < 220:
                    qgisfeat = self.dbasetables[layername]['layer'].getFeatures(request).next()
                else:
                    qgisfeat = self.dbasetables[layername]['layer'].getFeatures(request).__next__()

            else:
                sql = "SELECT pk_" + str(layername).lower() + " FROM " + str(layername).lower() +"_qgis "
                sql += "WHERE id_" + str(layername).lower() + " = " + str(fid)
                sql += " AND "
                sql += self.dateVersionConstraintSQL()
                pk = self.query(sql)[0][0]
                if int(str(self.qgisversion_int)[0:3]) < 220:
                    qgisfeat = self.dbasetables[layername]['layer'].getFeatures(qgis.core.QgsFeatureRequest(pk)).next()
                else:
                    qgisfeat = self.dbasetables[layername]['layer'].getFeature(pk)

                # print(txtrequest, qgisfeat.id(), qgisfeat.attributes())

            return qgisfeat

    def getLayerFeatureByPk(self, layername, fid):
        """
        Renvoie le QgsFeature de la table lamia nommée layername dont le pk est fid
        :param layername: le nom de la table dans la BD lamia
        :param fid: le pk dont on veut le feature
        :return: le QgsFeature associé au pk demandé
        """
        #print('featpk')
        debug = False

        if fid is None:
            return None

        if debug : logging.getLogger("Lamia").debug('Start %s %s', str(layername), str(fid))

        if int(str(self.qgisversion_int)[0:3]) < 220:
            return self.dbasetables[layername]['layer'].getFeatures(qgis.core.QgsFeatureRequest(fid)).next()

        else:
            return self.dbasetables[layername]['layer'].getFeature(fid)


    def getValuesFromPk(self, dbasename, fields, pk):
        # print('getValuesFromPk',type(fields) )
        if isinstance(fields, str) or isinstance(fields, unicode):
            fields = [fields]
        sql = " SELECT " + ','.join(fields) + " FROM " + dbasename
        sql += " WHERE pk_" + dbasename.split('_')[0].lower()
        sql += " = " + str(pk)
        res = self.query(sql)
        if res  :
            if len(res[0]) == 1:
                return res[0][0]
            else:
                return res[0]
        else:
            if len(fields) == 1:
                return None
            else:
                return tuple([None]*len(fields))

    def createNewObjet(self):
        datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        lastobjetid = self.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation, datetimemodification ) "
        sql += "VALUES(" + str(lastobjetid) + "," + str(self.maxrevision) + ",'" + datecreation + "','" + datecreation + "' )"
        self.query(sql)
        #self.dbase.commit()
        pkobjet = self.getLastRowId('Objet')
        return pkobjet

    def createNewLineVersion(self,dbname, rawpk):

        #first be sure
        pkobjet, revbegin = self.getValuesFromPk(dbname + "_qgis", ['pk_objet','lpk_revision_begin'], rawpk)
        if revbegin < self.maxrevision:

            #first close object
            sql = self.createSetValueSentence('UPDATE',
                                              'Objet',
                                              ['lpk_revision_end'],
                                              [self.maxrevision])
            sql += " WHERE pk_objet = " + str(pkobjet)
            self.query(sql)

            # then clone parents
            parenttables = self.getParentTable(dbname)[::-1] + [dbname]
            # get pkparents
            pknames = ['pk_' + parenttablename.lower() for parenttablename in parenttables]
            parentspk = self.getValuesFromPk(dbname.lower() + "_qgis", pknames, rawpk)

            lastpk = []
            for i, tablename in enumerate(parenttables):
                pkfields = []
                nonpkfields = []
                for fields in self.getColumns(tablename):
                    if fields[0:3] == 'pk_' or fields[0:4] == 'lpk_':
                        pkfields.append(fields)
                    elif fields == 'geom':
                        nonpkfields.append('ST_AsText(geom)')
                    else:
                        nonpkfields.append(fields)
                values = self.getValuesFromPk(tablename, nonpkfields,parentspk[i] )

                nonpkfields = ['geom' if x == 'ST_AsText(geom)' else x for x in nonpkfields]
                sql = self.createSetValueSentence('INSERT',
                                                  tablename,
                                                  nonpkfields,
                                                  list(values))
                self.query(sql)
                lastpk.append(self.getLastRowId(tablename))
                fieldstoupdate = []
                valuestoupdate=[]
                if 'lpk_revision_begin' in pkfields:
                    fieldstoupdate +=['lpk_revision_begin', 'lpk_revision_end']
                    valuestoupdate += [self.maxrevision,None]
                if 'datetimemodification' in nonpkfields:
                    datemodif = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    fieldstoupdate +=['datetimemodification']
                    valuestoupdate += [datemodif]
                if i > 0 and 'lpk_' + parenttables[i-1].lower() in pkfields:
                    fieldstoupdate += ["lpk_" + parenttables[i-1].lower()]
                    valuestoupdate += [lastpk[i-1]]

                sql = self.createSetValueSentence('UPDATE',
                                                  tablename,
                                                  fieldstoupdate,
                                                  valuestoupdate)
                sql += " WHERE pk_" + tablename.lower() + " = " + str(lastpk[i])
                self.query(sql)





    def dateVersionConstraintSQL(self, specialdate=None):
        """
        Crée une chaine à rajouter à la fin d'autre requetes pour spécifier la date et la version voulue
        :return: requete sql comprenant les éléments nécessaires pour filtrer les dates et les versions
        """

        if specialdate is None or specialdate == 'now':
            workingdatemodif = QtCore.QDate.fromString(self.workingdate, 'yyyy-MM-dd').addDays(1).toString('yyyy-MM-dd')
        else:
            workingdatemodif = QtCore.QDate.fromString(specialdate, 'dd/MM/yyyy').addDays(1).toString('yyyy-MM-dd')



        if self.version == '':
            sqlin = ' datecreation <= ' + "'" + workingdatemodif + "'"
            if self.dbasetype == 'postgis':
                sqlin += ' AND CASE WHEN datedestruction IS NOT NULL  '
                sqlin += 'THEN DateDestruction > ' + "'" + workingdatemodif + "'" + ' ELSE TRUE END'
                if self.revisionwork:
                    sqlin += " AND revisionbegin <= " + str(self.currentrevision)
                    sqlin += " AND CASE WHEN revisionend IS NOT NULL THEN "
                    sqlin += " revisionend > " + str(self.currentrevision)
                    sqlin += " ELSE TRUE END "
            elif self.dbasetype == 'spatialite':
                sqlin += ' AND CASE WHEN datedestruction IS NOT NULL  '
                sqlin += 'THEN datedestruction > ' + "'" + workingdatemodif + "'" + ' ELSE 1 END'
                if self.revisionwork:
                    sqlin += " AND revisionbegin <= " + str(self.currentrevision)
                    sqlin += " AND CASE WHEN revisionend IS NOT NULL THEN "
                    sqlin += " revisionend > " + str(self.currentrevision)
                    sqlin += " ELSE 1 END"
        else:

            sqlin = ' datetimecreation <= ' + "'" + workingdatemodif + "'"
            if self.dbasetype == 'postgis':
                sqlin += ' AND CASE WHEN datetimedestruction IS NOT NULL  '
                sqlin += 'THEN datetimedestruction > ' + "'" + workingdatemodif + "'" + ' ELSE TRUE END'
                if self.revisionwork:
                    sqlin += " AND lpk_revision_begin <= " + str(self.currentrevision)
                    sqlin += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
                    sqlin += " lpk_revision_end > " + str(self.currentrevision)
                    sqlin += " ELSE TRUE END "
            elif self.dbasetype == 'spatialite':
                sqlin += ' AND CASE WHEN datetimedestruction IS NOT NULL  '
                sqlin += 'THEN datetimedestruction > ' + "'" + workingdatemodif + "'" + ' ELSE 1 END'
                if self.revisionwork:
                    sqlin += " AND lpk_revision_begin <= " + str(self.currentrevision)
                    sqlin += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
                    sqlin += " lpk_revision_end > " + str(self.currentrevision)
                    sqlin += " ELSE 1 END"

        return sqlin


    def completePathOfFile(self,filetoprocess):
        """
        Génère le path complet du filetoprocess demandé. Utile quand on a un chemin relatif
        :param filetoprocess: le chemin rentré (relatif ou absolu)
        :return: le chemin absolu
        """
        completefile = ''
        if int(str(self.qgisversion_int)[0:3]) < 220 and isinstance(filetoprocess, QtCore.QPyNullVariant):
            filetoprocess = None
        if filetoprocess is None:
            return completefile
        if len(filetoprocess)>0:
            if filetoprocess[0] == '.':
                completefile = os.path.join(self.dbaseressourcesdirectory, filetoprocess)
            else:
                completefile = filetoprocess
            completefile = os.path.normpath(completefile)
        return completefile


    def getLastId(self, table):
        """
        renvoi l'id maximum de la table lamia demandée
        :param table: la table lamia dont on veut l'id max
        :return: l'id max
        """
        sql = "SELECT MAX(id_" + table.lower() + ") FROM " + str(table)
        query = self.query(sql)
        result = [row[0] for row in query]
        if len(result)>0 and result[0] is not  None:
            return result[0]
        else:       #initialization
            return 0

    def getLastPk(self, table):
        """
        renvoi le pk maximum de la table lamia demandée
        :param table: la table lamia dont on veut le pk max
        :return: le pk max
        """
        sql = "SELECT MAX(pk_" + table.lower() + ") FROM " + str(table)
        query = self.query(sql)
        result = [row[0] for row in query]
        if len(result) > 0 and result[0] is not None:
            return result[0]
        else:       # initialization
            return None

    def getLastRowId(self, table=None):
        """
        Renvoi le dernier pk ajouté dans la table lamia 'table'
        :param table: la table dont on veut le dernier pk ajouté
        :return: le dernier pk ajouté
        """
        id = None
        if self.dbasetype == 'spatialite':
            sql = 'SELECT last_insert_rowid()'
            query = self.query(sql)
            id = [row[0] for row in query][0]
        elif self.dbasetype == 'postgis':
            tablelower = table.lower()
            if self.version is None or self.version == '':
                sql = "SELECT currval('" + tablelower + "_id_" + tablelower + "_seq');"
            else:
                sql = "SELECT currval('" + tablelower + "_pk_" + tablelower + "_seq');"
            query = self.query(sql)
            id = [row[0] for row in query][0]
        return id


    def getColumns(self, tablename):

        result = None

        if self.dbasetype == 'spatialite':
            sql = "PRAGMA table_info(" + str(tablename) + ")"
            query = self.query(sql)
            result = [row[1] for row in query]

        elif self.dbasetype == 'postgis':
            sql = "SELECT column_name FROM information_schema.columns WHERE table_name  = '" +  str(tablename).lower() + "'"
            query = self.query(sql)
            result = [row[0] for row in query]

        return result


    def getFirstIdColumn(self,tablename):
        """
        Permet d'avoir la premiere colonne de la table lamia tablename avec pk_ en prefixe
        :param tablename: la table lamia
        :return: le nom du premier champ trouvé avec pk_ en sufixe
        """

        if self.dbasetype == 'spatialite':
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

        elif self.dbasetype == 'postgis':
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



        return None

    def getLatestVersion(self):
        """
        Renvoi la version max de la table Revision
        :return: la version max de la table Revision
        """
        sql = "SELECT MAX(pk_revision) FROM Revision;"
        query = self.query(sql)
        return query[0][0]

    def getMaxRevision(self):
        """
        Renvoi la version max de la table Revision
        :return: la version max de la table Revision
        """
        return self.getLastPk('Revision')

    def exportBase2(self, exportdbase):

        # load all features
        self.linkedids = {}

        # copy features
        for layer in self.layers:
            # dbasename = '_'.join(layer.name().split('_')[0:-1])
            if '_point' in layer.name():
                dbasename = layer.name()[0:-6]
            elif '_line' in layer.name():
                dbasename = layer.name()[0:-5]
            else:
                dbasename = layer.name()
            exec ("dbase = self.dbase_" + dbasename)

            if dbasename not in self.linkedids.keys():
                self.linkedids[dbasename] = {}

            for layerexport in exportdbase.layers:
                if layer.name() == layerexport.name():
                    layerexport.featureAdded.connect(self.featureAdded)

                    if layer.fields() == layerexport.fields():
                        for feat in layer.getFeatures():
                            with qgis.core.edit(layerexport):
                                if len(dbase['type'])>0:
                                    if feat.geometry() is None:
                                        continue
                                fet = qgis.core.QgsFeature(feat)
                                idparent = fet['ID']
                                fet['ID'] = None
                                bool = layerexport.addFeature(fet)
                                if bool:
                                    layerexport.updateFeature(fet)
                                else:
                                    print(layer.name(), 'feature', idparent, 'non exporte')
                            self.linkedids[dbasename][int(idparent)] = int(self.featureaddedid)
                    else:
                        for feat in layer.getFeatures():
                            with qgis.core.edit(layerexport):
                                fet = qgis.core.QgsFeature(layerexport.fields())
                                if len(dbase['type'])>0:
                                    if feat.geometry() is None:
                                        continue
                                    else:
                                        fet.setGeometry(feat.geometry())
                                idparent = feat['ID']
                                fieldnames = [field.name() for field in layerexport.fields()]
                                for field in layer.fields():
                                    if field.name() in fieldnames:
                                        fet[field.name()] = feat[field.name()]
                                fet['ID'] = None
                                bool = layerexport.addFeature(fet)
                                if bool:
                                    layerexport.updateFeature(fet)
                                else:
                                    print(layer.name(), 'feature', idparent, 'non exporte')
                            self.linkedids[dbasename][int(idparent)] = int(self.featureaddedid)
                    layerexport.featureAdded.disconnect(self.featureAdded)

        # print(self.linkedids)

        # reassign linked ids

        for layer in exportdbase.layers:

            if '_point' in layer.name():
                dbasename = layer.name()[0:-6]
            elif '_line' in layer.name():
                dbasename = layer.name()[0:-5]
            else:
                dbasename = layer.name()
            exec ("dbase = self.dbase_" + dbasename)

            # if dbasename in self.linkedids.keys():

            if dbase['linkfield'] is not None:
                for link in dbase['linkfield']:
                    # print(dbasename,link)
                    if link[0] is None:
                        if link[1] in self.linkedids.keys() and dbasename in self.linkedids.keys():

                            linkparenttouse = self.linkedids[link[1]]
                            linkchildtouse = self.linkedids[dbasename]

                            if False:
                                print(dbasename, '***************')
                                print(linkparenttouse)
                                print(linkchildtouse)

                            request = qgis.core.QgsFeatureRequest().setFilterFids(linkchildtouse.values())
                            with qgis.core.edit(layer):
                                for feat in layer.getFeatures(request):
                                    if not isinstance(feat[link[2]], QtCore.QPyNullVariant):
                                        if int(feat[link[2]]) in linkparenttouse.keys():
                                            feat[link[2]] = linkparenttouse[feat[link[2]]]
                                            layer.updateFeature(feat)
                                        else:
                                            feat[link[2]] = None
                                            layer.updateFeature(feat)
                                    else:
                                        feat[link[2]] = None
                                        layer.updateFeature(feat)
                    else:
                        if dbasename in self.linkedids.keys() :
                            linkchildtouse = self.linkedids[dbasename]
                            request = qgis.core.QgsFeatureRequest().setFilterFids(linkchildtouse.values())
                            with qgis.core.edit(layer):
                                for feat in layer.getFeatures(request):
                                    parentlayertrigram = feat[link[0]]
                                    if parentlayertrigram in [elem[0] for elem in self.dbase_tables]:
                                        parentlayername = self.dbase_tables[[elem[0] for elem in self.dbase_tables].index(parentlayertrigram)][1]
                                        if parentlayername in  self.linkedids.keys():
                                            linkparenttouse = self.linkedids[parentlayername]

                                            if False:
                                                print(dbasename, '***************')
                                                print(linkparenttouse)
                                                print(linkchildtouse)

                                            if feat[link[2]] in linkparenttouse.keys():
                                                feat[link[2]] = linkparenttouse[feat[link[2]]]
                                                layer.updateFeature(feat)
                                            else:
                                                feat[link[2]] = None
                                                layer.updateFeature(feat)

    def featureAdded(self, id):
        """
        Méthode connectée au signal featureAdded d'un qgsvectorlayer pour connaitre le pk du feature ajouté
        assigne cette valeur à self.featureaddedid
        :param id: le pk fourni par le signal
        """
        self.featureaddedid = id

    def getMaxVersionRepository(self, typemetier):
        """
        REcherche dans Lamia/DBASE/create le repertoire qui correspond au typemetier, avec la plus grande version
        s'il n'y a pas de version (lamia avant sept.2018) , renvoi le repertoire avec version = None

        :param typemetier:
        :return:
        """
        version = ''
        repository = None

        createfilesdir = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'create')
        listrep = os.listdir(createfilesdir)
        for rep in listrep:
            if len(rep.split('_')) > 2 :
                if typemetier == '_'.join(rep.split('_')[:-2]) :
                    versiontemp = '_'.join(rep.split('_')[-2:])
                    if versiontemp > version:
                        repository = os.path.join(createfilesdir,rep)
                        version = versiontemp
            else:
                if typemetier == rep :
                    repository = os.path.join(createfilesdir,rep)


        return repository, version



    def getVersionRepositories2(self, typemetier):
        """
        REcherche dans Lamia/DBASE/create le repertoire qui correspond au typemetier, avec la plus grande version
        s'il n'y a pas de version (lamia avant sept.2018) , renvoi le repertoire avec version = None

        :param typemetier:
        :return:
        """
        debug = False
        results = []

        createfilesdir = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'create')
        if debug: logging.getLogger("Lamia").debug('dbase dir : %s', str(createfilesdir))

        if False:
            listrep = os.listdir(createfilesdir)
            for rep in listrep:
                if len(rep.split('_')) > 2 :
                    if typemetier == '_'.join(rep.split('_')[:-2]) :
                        versiontemp = '_'.join(rep.split('_')[-2:])
                        if versiontemp > version:
                            repository = os.path.join(createfilesdir,rep)
                            version = versiontemp
                else:
                    if typemetier == rep :
                        repository = os.path.join(createfilesdir,rep)

        listfiles = os.listdir(createfilesdir)
        for filename in listfiles:
            filepath = os.path.join(createfilesdir,filename )
            filebasename, ext = os.path.splitext(filename)

            if os.path.isfile(filepath) and ext in ['.xls', '.xlsx']:
                filebasenamesplitted = filebasename.split('_')
                if (len(filebasenamesplitted) > 2 and filebasenamesplitted[-2].isdigit() and filebasenamesplitted[-1].isdigit()
                        and typemetier == '_'.join(filebasenamesplitted[:-2]) ):     #case child of dabse2
                    versiontemp = '_'.join(filebasename.split('_')[-2:])
                    repository = os.path.join(createfilesdir, filename)
                    results.append([versiontemp, repository])

                if False:
                    if len(filebasename.split('_')) > 2 :
                        if typemetier == '_'.join(filebasename.split('_')[:-2]) :

                            versiontemp = '_'.join(filebasename.split('_')[-2:])
                            repository = os.path.join(createfilesdir, filename)
                            results.append([versiontemp,repository ])

                            if False and versiontemp > version:
                                repository = os.path.join(createfilesdir,filename)
                                version = versiontemp
                    else:
                        if typemetier == filebasename :
                            repository = os.path.join(createfilesdir,filename)

        if debug: logging.getLogger("Lamia").debug('results: %s', str(results))

        results.sort()

        if debug: logging.getLogger("Lamia").debug('results: %s', str(results))

        return results



    def updateDBaseVersion2(self):

        self.normalMessage.emit("Mise à jour de la base de données...")

        debug = True

        if debug: logging.getLogger("Lamia").debug('DBASE need an update')

        workversions = self.getVersionRepositories2(self.type)
        baseversions = self.getVersionRepositories2(self.type.split('_')[0])

        workversionmax,  createfilesdir, = workversions[-1]
        baseversionmax, createfilesdirbase = baseversions[-1]

        if debug: logging.getLogger("Lamia").debug('main version projet : %s, new : %s', str(self.version),
                                                   str(baseversionmax))
        if debug: logging.getLogger("Lamia").debug('work version projet : %s, new : %s', str(self.workversion),
                                                   str(workversionmax))

        indexbaseversion = [ver[0] for ver in baseversions].index(self.version)
        indexworkversion = [ver[0] for ver in workversions].index(self.workversion)

        for indexversion in range(indexbaseversion, len(baseversions) -1 ):
            self.updateTables('base',
                              baseversions[indexversion][0],
                              baseversions[indexversion +1][0] )


        for indexversion in range(indexworkversion, len(workversions) -1 ):
            self.updateTables('metier',
                              workversions[indexworkversion][0],
                              workversions[indexworkversion + 1][0])


        self.normalMessage.emit("Mise à jour de la base de données terminée")



    def updateTables(self, typebase, oldversion, newversion ):

        debug = False
        if debug: logging.getLogger("Lamia").debug(' %s - old : %s, new : %s', str(typebase), str(oldversion), str(newversion))
        if self.qgsiface is None:
            print('type base :',str(typebase), ' - oldversion : ', str(oldversion), ' - newversion ', str(newversion))


        baseversions = self.getVersionRepositories2(self.type.split('_')[0])
        workversions = self.getVersionRepositories2(self.type)


        if typebase == 'base':
            indexnewversion = [ver[0] for ver in baseversions].index(newversion)
            filenewversion = baseversions[indexnewversion][1]
            #updates new columsns
            self.createDBDictionary2(self.type, baseversiontoread=oldversion, workversiontoread=self.workversion)
            dictold = dict(self.dbasetables)
            self.createDBDictionary2(self.type, baseversiontoread=newversion, workversiontoread=self.workversion)
            dictnew = dict(self.dbasetables)
        elif typebase == 'metier':
            indexnewversion = [ver[0] for ver in workversions].index(newversion)
            filenewversion = workversions[indexnewversion][1]
            #updates new columsns
            self.createDBDictionary2(self.type, baseversiontoread=self.version, workversiontoread=oldversion)
            dictold = dict(self.dbasetables)
            self.createDBDictionary2(self.type, baseversiontoread=self.version, workversiontoread=newversion)
            dictnew = dict(self.dbasetables)



        results = []

        for table in dictnew.keys():
            for field in dictnew[table]['fields']:
                if field not in dictold[table]['fields'].keys():
                    results.append([table, field])

        if debug: logging.getLogger("Lamia").debug('diff : %s', str(results))
        if self.qgsiface is None:
            print('diff :',str(results))

        for table, field in results:
            sql = 'ALTER TABLE ' + table + ' ADD COLUMN ' + field + ' '
            if self.dbasetype == 'spatialite':
                if 'VARCHAR' in dictnew[table]['fields'][field]['PGtype']:
                    sql += ' TEXT '
                else:
                    sql += self.pgtypetosltype[dictnew[table]['fields'][field]['PGtype']]
            elif self.dbasetype == 'postgis':
                sql += dictnew[table]['fields'][field]['PGtype']
            self.query(sql)

        # read potential python file
        pythonfile, ext = os.path.splitext(filenewversion)
        pythonfile = pythonfile + '.txt'

        if os.path.isfile(pythonfile):
            pyfile = open(pythonfile,'r')
            text = pyfile.read()
            pyfile.close()
            exec (text)


        #update version
        if typebase == 'base':
            self.version = newversion
            self.workversion = self.workversion
        elif typebase == 'metier':
            self.version = self.version
            self.workversion = newversion

        sql = "UPDATE Basedonnees SET version = '" + str(self.version) + "'"
        if self.workversion is not None:
            sql += ",workversion = '" + str(self.workversion) + "'"

        self.query(sql)



    def updateDBaseVersion(self):

        self.normalMessage.emit("Mise à jour de la base de données...")


        debug = False
        if debug: logging.getLogger("Lamia").debug('DBASE need an update')

        createfilesdir, workversionmax = self.getMaxVersionRepository(self.type)
        createfilesdirbase, baseversionmax = self.getMaxVersionRepository(self.type.split('_')[0])

        if debug: logging.getLogger("Lamia").debug('main version projet : %s, new : %s', str(self.version), str(baseversionmax))
        if debug: logging.getLogger("Lamia").debug('work version projet : %s, new : %s', str(self.workversion), str(workversionmax))


        if not self.xlsreader:
            self.createDBDictionary(self.type, baseversiontoread=self.version, workversiontoread=self.workversion)
            dictold = dict(self.dbasetables)
            self.createDBDictionary(self.type, baseversiontoread=baseversionmax, workversiontoread=workversionmax)
            dictnew = dict(self.dbasetables)
        else:
            self.createDBDictionary2(self.type, baseversiontoread=self.version, workversiontoread=self.workversion)
            dictold = dict(self.dbasetables)
            self.createDBDictionary2(self.type, baseversiontoread=baseversionmax, workversiontoread=workversionmax)
            dictnew = dict(self.dbasetables)





        results=[]

        for table in dictnew.keys():
            for field in dictnew[table]['fields']:
                if field not in dictold[table]['fields'].keys():
                    results.append([table, field])

        if debug: logging.getLogger("Lamia").debug('diff : %s',str(results))


        for table, field in results:
            sql = 'ALTER TABLE ' + table + ' ADD COLUMN ' + field + ' '
            if self.dbasetype == 'spatialite':
                if self.xlsreader:
                    sql += self.pgtypetosltype[dictnew[table]['fields'][field]['PGtype']]
                else:
                    sql += dictnew[table]['fields'][field]['SLtype']
            elif self.dbasetype == 'postgis':
                sql += dictnew[table]['fields'][field]['PGtype']
            self.query(sql)



        sql = "UPDATE Basedonnees SET version = '" + str(baseversionmax) + "'"
        if workversionmax is not None:
            sql += ",workversion = '" + str(workversionmax) + "'"

        self.query(sql)

        self.normalMessage.emit("Mise à jour de la base de données terminée")






    def getParentTable(self, tablename):
        """
        Get Parents table name
        :param tablename:
        :return:
        """
        parenttablenamelist = []
        dbasetable = self.dbasetables[tablename]
        continuesearchparent = True

        while continuesearchparent:
            for field in dbasetable['fields'].keys():
                continuesearchparent = False
                if 'lpk_' == field[:4]:
                    tablename = field.split('_')[1].title()
                    parenttablenamelist.append(tablename)
                    dbasetable = self.dbasetables[tablename]
                    if field[4:] == 'objet':
                        continuesearchparent = False
                    else:
                        continuesearchparent = True
                    break

        return parenttablenamelist




    def importDbase(self, dbaseparserfrom, typeimport='nouvelle'):
        """

        :param dbaseparserfrom:
        :param typeimport:  nouvelle import_terrain
        :return:
        """

        debug = False
        if debug:
            logging.getLogger("Lamia").debug('Start ')
            dbaseparserfrom.printsql = True

        self.backupBase()

        if self.qgsiface is not None:
            #if not self.dbase.standalone:
            progressMessageBar = self.qgsiface.messageBar().createMessage("Import des donnees...")
            progress = QProgressBar()
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.qgisversion_int)[0:3]) < 220:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, self.qgsiface.messageBar().INFO)
            else:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
            #len
            maxprogress = len(self.dbasetables.keys())
            progress.setMaximum(maxprogress)
        else:
            progress = None

        # ********** Variables générales ***********************************
        # import dict : {tablename : {...{idfrom : idto} ...} }
        # utilise pour la correspondance entre les id de la table d'import et les id de la table main
        importdictid = {}
        # import dict : {tablename : {...{pkfrom : pkto} ...} }
        # utilise pour la correspondance entre les pk de la table d'import et les pk de la table main
        importdictpk = {}
        # import dict : {tablename : [pk1, pk2,..] }
        # utilise pour se souvenir des pk qui ont un revsionend
        importdictdeletedpk = {}
        #conflictobjetids dict : {..., idobjet:{fields : [], importvalue:[], mainvalue:[]},... }
        conflictobjetids = OrderedDict()

        # ************** add version
        datedebutimport = str((datetime.datetime.now() - datetime.timedelta(seconds=2)).strftime("%Y-%m-%d %H:%M:%S"))
        if typeimport == 'nouvelle':
            comment = 'import'
        elif typeimport == 'import_terrain':
            comment = 'import_terrain'
        sql = "INSERT INTO Revision(datetimerevision, commentaire) "
        sql += " VALUES('" + str(datedebutimport) + "', '" + comment + "')"
        self.query(sql)
        self.maxrevision = self.getMaxRevision()
        self.currentrevision = int(self.maxrevision)
        self.updateWorkingDate()

        # **************** date de la version d'import
        datetravailhorsligne = None
        if typeimport == 'import_terrain':
            # datetravailhorsligne
            sql = "SELECT datetimerevision FROM Revision WHERE pk_revision = 2"
            datetravailhorsligne = dbaseparserfrom.query(sql)[0][0]

        # **************** debut de l'iteration sur les tables à importer
        counter = 0
        for order in range(1, 10):
            for dbname in self.dbasetables:
                if self.dbasetables[dbname]['order'] == order:

                    counter += 1

                    if progress: progressMessageBar.setText("Import des donnees... : " + dbname)
                    self.setLoadingProgressBar(progress, counter)



                    if debug: logging.getLogger("Lamia").debug(' ******************* %s *********  ', dbname)
                    # self.normalMessage.emit("Chargement de " + str(dbname))

                    # initialisation des variables génerales
                    importdictid[dbname.lower()] = {}
                    importdictpk[dbname.lower()] = {}
                    importdictdeletedpk[dbname.lower()] = []

                    # get non critical fields (not pk and non id)
                    noncriticalfield = []           # the "non-critical" fields
                    pkidfields = []                 # the "critical" fields (pk; id, lpk, lid)
                    for field in self.dbasetables[dbname]['fields'].keys():
                        if field[0:3] in ['id_', 'pk_'] or field[0:4] in ['lpk_', 'lid_']:
                            pkidfields.append(field)
                        else:
                            noncriticalfield.append(field)
                    #add geom at rank-1
                    if 'geom' in self.dbasetables[dbname].keys():
                        noncriticalfield.insert(-1, 'ST_AsText(ST_Transform(geom,' + str(self.crsnumber) + '))')
                    if not noncriticalfield:
                        noncriticalfield = ['*']
                    if debug: logging.getLogger("Lamia").debug(' fields, critical : %s %s ',
                                                               str(noncriticalfield),str(pkidfields))

                    # request results from dbaseparserfrom
                    if typeimport == 'nouvelle':
                        sqlconstraint = " WHERE lpk_revision_end IS NULL"
                    elif typeimport == 'import_terrain':
                        sqlconstraint = " WHERE lpk_revision_begin = 2 OR lpk_revision_end = 2"

                    sql, sqlpk = '', ''
                    if 'Objet' in self.getParentTable(dbname):
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower() + "_qgis"
                        sql += sqlconstraint
                        sqlpk = "SELECT " + ','.join(pkidfields) + " FROM " + dbname.lower() + "_qgis"
                        sqlpk += sqlconstraint
                    elif 'lpk_revision_end' in self.dbasetables[dbname]['fields'].keys():
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()
                        sql += sqlconstraint
                        sqlpk = "SELECT " + ','.join(pkidfields) + " FROM " + dbname.lower()
                        sqlpk += sqlconstraint
                    else:
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()
                        sqlpk = "SELECT " + ','.join(pkidfields) + " FROM " + dbname.lower()
                    results = dbaseparserfrom.query(sql)
                    resultpk = dbaseparserfrom.query(sqlpk)


                    strtofind = 'ST_AsText(ST_Transform(geom,' + str(self.crsnumber) + '))'
                    if strtofind in noncriticalfield:
                        noncriticalfield[noncriticalfield.index(strtofind)] = 'geom'

                    # get previoux existing id and other things for import terrain
                    resultsid = None            # the existing id in main table
                    indexidfield = None         # the index of id_ column
                    indexrevisionend = None     # the index of lpk_revision_end
                    indexpkdbase = None         # the index of pk_ column
                    importid = None             # the id in the table lines iteration
                    parenttable = None          # the parent table of actual table - defined as lpk_(parenttable)
                    indexlkparenttable = None   # the index of parent table in pkidfields
                    if typeimport == 'import_terrain':
                        # get resultsid and indexidfield
                        if "id_" + dbname.lower() in pkidfields:
                            if True:
                                sqlid = "SELECT id_" + dbname.lower() + " FROM " + dbname.lower() + "_qgis"
                                sqlid += " WHERE lpk_revision_begin = 1 "
                                resultsid = [elem[0] for elem in dbaseparserfrom.query(sqlid)]

                            if False:
                                sqlid = "SELECT id_" + dbname.lower() + " FROM " + dbname.lower() + "_qgis"
                                sqlid += " WHERE datetimecreation < '" + str(datetravailhorsligne) + "'"
                                resultsid = [elem[0] for elem in self.query(sqlid)]
                            indexidfield = pkidfields.index("id_" + dbname.lower())
                        # get indexrevisionend
                        if "lpk_revision_end" in pkidfields:
                            indexrevisionend = pkidfields.index('lpk_revision_end')
                        indexpkdbase = pkidfields.index("pk_" + dbname.lower())
                        # get eventual parenttable
                        for j, fieldname in enumerate(pkidfields):
                            if fieldname[0:4] == 'lpk_':
                                parenttable = fieldname.split('_')[1]
                                indexlkparenttable = j
                        if debug: logging.getLogger("Lamia").debug(' parenttable, index : %s %s ',
                                                                   str(parenttable),
                                                                   str(indexlkparenttable))

                    # start the iteration in table lines
                    # if results is not None:
                    for i, result in enumerate(results):

                        if i % 50 == 0 and debug: logging.getLogger("Lamia").debug(' result : %s  ', str(result))

                        if resultsid is not None:
                            importid = resultpk[i][indexidfield]

                        # id already exists before - search if it was modified
                        if resultsid is not None and importid in resultsid:
                            # get its  datemodif
                            if False:
                                sqldate = " SELECT datetimemodification FROM " + dbname.lower() + "_qgis"
                                sqldate += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                sqldate += " AND lpk_revision_end IS NULL"
                            if True:
                                sqldate = " SELECT MAX(datetimemodification) FROM " + dbname.lower() + "_qgis"
                                sqldate += " WHERE id_" + dbname.lower() + " = " + str(importid)
                            resultdatesql = self.query(sqldate)
                            resultdate = None
                            if resultdatesql : # cases 3, 5, 6, 8, 9
                                resultdate = self.query(sqldate)[0][0]
                            else:       # case 4 or 7 : line deleted in main
                                pass

                            if debug:  logging.getLogger("Lamia").debug('**** existing id : %s / date main : %s / date2 : %s', str(importid), str(resultdate), str(datetravailhorsligne))

                            # Search if possible conflict
                            # isinconflict = False
                            if resultdate is None :  # case 4 or 7
                                # not modified while field investigation- create new version - done
                                if dbname.lower() == 'objet':
                                    if debug: self.printsql = False
                                    isinconflict, listfields, listvaluemain, listvalueimport = self.isInConflict(dbaseparserfrom, importid)
                                    if debug: self.printsql = True
                                    if debug: logging.getLogger("Lamia").debug('in conflict : %s', str(isinconflict))
                                    if debug: logging.getLogger("Lamia").debug('date : %s %s', str(resultdate), str(datetravailhorsligne))
                                    if isinconflict:
                                        conflictobjetids[importid]={}
                                        conflictobjetids[importid]['fields'] =  listfields
                                        conflictobjetids[importid]['mainvalue'] = listvaluemain
                                        conflictobjetids[importid]['importvalue'] = listvalueimport

                            elif resultdate < datetravailhorsligne or resultdate > datedebutimport:     #case 1, 3 - no conflict
                                pass






                            else:     # cases  5, 6, 8, 9
                                if dbname.lower() == 'objet':
                                    if debug: self.printsql = False
                                    isinconflict, listfields, listvaluemain, listvalueimport = self.isInConflict(dbaseparserfrom, importid)
                                    if debug: self.printsql = True
                                    if debug: logging.getLogger("Lamia").debug('in conflict : %s', str(isinconflict))
                                    if debug: logging.getLogger("Lamia").debug('date : %s %s', str(resultdate), str(datetravailhorsligne))
                                    if isinconflict:
                                        conflictobjetids[importid]={}
                                        conflictobjetids[importid]['fields'] =  listfields
                                        conflictobjetids[importid]['mainvalue'] = listvaluemain
                                        conflictobjetids[importid]['importvalue'] = listvalueimport

                            # **** in all cases, create a new line or set revisionend  with import table value *****
                            #   eventualy rewrite it when conflict process

                            # deleted id case
                            # its sure its an existing pk
                            # case 3a, 4a, 5a, 6a, 7a, 8a, 9a
                            if (typeimport == 'import_terrain' and indexrevisionend is not None
                                    and resultpk[i][indexrevisionend] == 2):

                                if debug: logging.getLogger("Lamia").debug(' set revisionend id, date: %s %s', str(importid), str(resultdate))

                                # case 4a or 7a
                                if not resultdate:
                                    sql = " SELECT pk_" + dbname.lower() + "FROM " + dbname.lower() + "_qgis"
                                    sql += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                    sql += " AND lpk_revision_end IS NULL"
                                    resultcase = dbaseparserfrom.query(sql)
                                    if resultcase:  # case 4a : do nothing - wait for active rev line
                                        pass
                                    else:    # case 7a : do nothing
                                        pass

                                # cases 3a, 5a, 6a, 8a, 9a, 10a, 11a
                                else:
                                    # simply set lpk_revision_end to main table
                                    if 'lpk_revision_end' in self.dbasetables[dbname]['fields'].keys():
                                        # search latest pk in main with same id
                                        sql = "SELECT pk_" + dbname.lower() + " FROM  " + dbname.lower()
                                        sql += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                        sql += " AND lpk_revision_end IS NULL"
                                        sqlpkmain = self.query(sql)
                                        # sqlpkimport = dbaseparserfrom.query(sql)

                                        # add pk to importdictdeletedpk
                                        importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])

                                        if sqlpkmain:
                                            self.printsql = True
                                            pkmain = sqlpkmain[0][0]
                                            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                            sql = "UPDATE " + dbname.lower() + " SET lpk_revision_end = " + str(self.maxrevision)
                                            sql += " , datetimemodification = '" + datesuppr + "'"
                                            sql += " WHERE pk_" + dbname.lower() + " = " + str(pkmain)
                                            self.query(sql, docommit=False)


                                    if False:

                                        sql = " SELECT pk_" + dbname.lower() + "FROM " + dbname.lower() + "_qgis"
                                        sql += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                        sql += " AND lpk_revision_end IS NULL "
                                        sql += "AND datetimemodification > '"  + str(datetravailhorsligne) + "'"
                                        resultcase = self.query(sql)

                                        if resultcase:  #case 3a, 6a, 9a : revend to main line without possible conflict
                                            pass
                                        else:
                                            pass


                                        if 'lpk_revision_end' in self.dbasetables[dbname]['fields'].keys():
                                            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                            sql = "UPDATE " + dbname.lower() + " SET lpk_revision_end = " + str(self.maxrevision)
                                            sql += " , datetimemodification = '" + datesuppr + "'"
                                            sql += " WHERE pk_" + dbname.lower() + " = " + str(resultpk[i][indexpkdbase])
                                            self.query(sql, docommit=False)

                                            # add pk to importdictdeletedpk
                                            importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])

                                            if True:
                                                # search if another id is in main and not in import
                                                sql = "SELECT pk_" + dbname.lower() + " FROM  " + dbname.lower()
                                                sql += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                                sql += " AND lpk_revision_end IS NULL"
                                                idmain = self.query(sql)
                                                idimport = dbaseparserfrom.query(sql)

                                                if not idimport and idmain:        # simple delete from import and remain in main
                                                    pkmain = idmain[0][0]
                                                    sql = "UPDATE " + dbname.lower() + " SET lpk_revision_end = " + str(self.maxrevision)
                                                    sql += " , datetimemodification = '" + datesuppr + "'"
                                                    sql += " WHERE pk_" + dbname.lower() + " = " + str(pkmain)
                                                    self.query(sql, docommit=False)





                            # if parent table pk is in  importdictdeletedpk
                            elif (parenttable is not None
                                  and parenttable in importdictdeletedpk.keys()
                                  and resultpk[i][indexlkparenttable] in importdictdeletedpk[parenttable]):
                                if debug: logging.getLogger("Lamia").debug(' parent revisionend : %s', str(importid))
                                importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])


                            # new version case
                            # case 3b, 4b, 5b, 6b, 11b
                            else:
                                if debug: logging.getLogger("Lamia").debug(' new elem : %s', str(importid))
                                # insert new line in main table
                                sql = self.createSetValueSentence(type='INSERT',
                                                                  tablename=dbname,
                                                                  listoffields=noncriticalfield,
                                                                  listofrawvalues=result)
                                self.query(sql, docommit=True)
                                # udpate id/pk fields without changing id_table value
                                sqlup = self.updateIdPkSqL(tablename=dbname,
                                                           listoffields=pkidfields,
                                                           listofrawvalues=resultpk[i],
                                                           dictpk=importdictpk,
                                                           dictid=importdictid,
                                                           changeID=False)
                                self.query(sqlup, docommit=False)



                        # id does not exists before - create new line or for tc
                        else:
                            if debug: logging.getLogger("Lamia").debug('****  new elem id : %s',str(importid))

                            if (typeimport == 'import_terrain' and indexrevisionend is not None
                                    and resultpk[i][indexrevisionend] == 2):
                                # case of line deleted in main and deleted in import - dont t process it
                                importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])



                            elif (parenttable is not None
                                  and parenttable in importdictdeletedpk.keys()
                                  and resultpk[i][indexlkparenttable] in importdictdeletedpk[parenttable]):
                                if debug: logging.getLogger("Lamia").debug(' parent revisionend : %s', str(importid))
                                importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])

                            else:
                                # traite la mise en forme du result
                                if noncriticalfield != ['*']:
                                    sql = self.createSetValueSentence(type='INSERT',
                                                                      tablename=dbname,
                                                                      listoffields=noncriticalfield,
                                                                      listofrawvalues=result)
                                else:
                                    sql = "INSERT INTO " + dbname + " DEFAULT VALUES"
                                self.query(sql, docommit=False)

                                # traite les id, pk et lid et lpk
                                if True:
                                    sqlup = self.updateIdPkSqL(tablename=dbname,
                                                               listoffields=pkidfields,
                                                               listofrawvalues=resultpk[i],
                                                               dictpk=importdictpk,
                                                               dictid=importdictid,
                                                               changeID=True)


                                    self.query(sqlup, docommit=False)

                                # Ressource case : copy file
                                if dbname == 'Ressource':
                                    indexfile = noncriticalfield.index('file')
                                    filepath = result[indexfile]
                                    if not self.isAttributeNull(filepath):
                                        filefrom = dbaseparserfrom.completePathOfFile(filepath)
                                        fileto = os.path.join(self.dbaseressourcesdirectory, filepath)
                                        self.copyRessourceFile(fromfile=filefrom,
                                                               tofile=fileto,
                                                               withthumbnail=0,
                                                               copywholedirforraster=False)
                    # Finaly commit all
                    self.commit()

                    if debug: logging.getLogger("Lamia").debug(' importdictid %s  ', str(importdictid[dbname.lower()]))
                    if debug: logging.getLogger("Lamia").debug(' importdictpk %s  ', str(importdictpk[dbname.lower()]))
                    if debug: logging.getLogger("Lamia").debug(' importdictdeletedpk %s  ', str(importdictdeletedpk[dbname.lower()]))
                    if debug: logging.getLogger("Lamia").debug(' conflictobjetids %s  ', str(conflictobjetids))

        self.resolveConflict(dbaseparserfrom,conflictobjetids )


        if int(str(self.qgisversion_int)[0:3]) < 220:
            self.canvas.refresh()
        else:
            self.canvas.refreshAllLayers()

        if progress is not None: self.qgsiface.messageBar().clearWidgets()
        self.normalMessage.emit("Import termine")




    def isInConflict(self, dbaseparserfrom, conflictobjetid):
        """
        cases: (datet : datetravail)
        MAin                                             Import
        case n° datem       revbegin    revend          datem       revbegin    revend      Action                              Action on import                    Action if main retained
        1       <datet      11                          <datet      1                       nothing modified                    /                                   /
        2       >datet      11                          <datet      1                       only main modified - ok             /                                   /
        3       <datet      11                          >datet      1           2           only import modified ok             close lastrev and create new rev    /
                                                        >datet      2
        4       suppr                                   >datet      1           2           conflict                            add new rev with same id            close new rev
                                                        >datet      2
        5       >datet      11          12              >datet      1           2           conflict                            rewrite main new rev                rewrite new rev with main
                >datet      12                          >datet      2
        6       >datet      11          12              >datet      1           2           conflict                            add new rev                         close new rev
                                                        >datet      2
        7       suppr                                   >datet      1           2           ok : deleted on main and import     /                                   /
        8       >datet      11          12              >datet      1           2           conflict                            close lastrev                      write new rev with main
                >datet      12
        9       >datet      11                          >datet      1           2           conflit                             close lastrev                       unclose lastrev
        10      >datet      11          12              >datet      1           2           ok : deleted on main and import     /                                   /
        11      >datet      11          12              >datet      1           2           conlit                              add new rev                         /  close las rev
                                                        >datet      2

        :param dbaseparserfrom:
        :param conflictobjetid:
        :return:
        """

        debug = False
        if debug: logging.getLogger("Lamia").debug(' isInConflict - idobjet : %s  ', str(conflictobjetid))

        # get mainpkobjet and importpkobjet
        sql = " SELECT MAX(pk_objet) FROM Objet WHERE id_objet = " + str(conflictobjetid)
        mainpkobjetsql = self.query(sql)
        importpkobjetsql = dbaseparserfrom.query(sql)


        if False:
            sql = " SELECT pk_objet FROM Objet WHERE id_objet = " + str(conflictobjetid)
            sql += " AND lpk_revision_end IS NULL"
            mainpkobjet = None
            resmain = self.query(sql)
            if resmain:
                mainpkobjet = resmain[0][0]
            importpkobjet = None
            resimport = dbaseparserfrom.query(sql)
            if resimport:
                importpkobjet = resimport[0][0]

            if mainpkobjet is None:
                sql = " SELECT pk_objet FROM Objet WHERE id_objet = " + str(conflictobjetid)
                sql += " AND lpk_revision_end = MAX(lpk_revision_end)"


        # print('mainpkobjetsql',mainpkobjetsql,conflictobjetid)
        if mainpkobjetsql[0][0] is not None: #cases 3, 5, 6, 8, 9

            mainpkobjet = mainpkobjetsql[0][0]
            importpkobjet = importpkobjetsql[0][0]

            # get child table name and pk
            mainconflictdbname, mainconflictpk = self.searchChildfeatureFromPkObjet(self, mainpkobjet)
            importconflictdbname, importconflictpk = self.searchChildfeatureFromPkObjet(dbaseparserfrom, importpkobjet)

            #get revend of pk
            sql = "SELECT lpk_revision_end FROM " + mainconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
            revendmain = self.query(sql)[0][0]
            sql = "SELECT lpk_revision_end FROM " + importconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
            revendimport = dbaseparserfrom.query(sql)[0][0]


            if revendimport is not None and revendmain is not None:     # main and import has been deleted - non conflict
                return False, None, None, None


            # values from child table
            sql = "SELECT * FROM " + mainconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
            resmain = self.query(sql)[0]
            sql = "SELECT * FROM " + importconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
            resimport = dbaseparserfrom.query(sql)[0]

            fields = self.getColumns(mainconflictdbname.lower() + "_qgis")

            # get geom
            resgeom1, resgeom2 = None, None
            if 'geom' in fields:
                sql = " SELECT ST_AsText(geom) FROM " + mainconflictdbname.lower() + "_qgis"
                sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
                resgeommain = self.query(sql)[0][0]
                sql = " SELECT ST_AsText(geom) FROM " + importconflictdbname.lower() + "_qgis"
                sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
                resgeomimport = dbaseparserfrom.query(sql)[0][0]

            if False:
                print('resmain',resmain)
                print('resimport',resimport)
                print('resgeommain',resgeommain)
                print('resgeomimport', resgeomimport)


        else:

            sql = " SELECT pk_objet FROM Objet WHERE id_objet = " + str(conflictobjetid)
            sql += " AND lpk_revision_end = 2"
            mainpkobjetsql = dbaseparserfrom.query(sql)

            mainpkobjet = mainpkobjetsql[0][0]
            importpkobjet = importpkobjetsql[0][0]

            if mainpkobjet == importpkobjet:   #main was deleted and import also - no conflict
                return False, None, None, None



            mainconflictdbname, mainconflictpk = self.searchChildfeatureFromPkObjet(dbaseparserfrom, mainpkobjet)
            importconflictdbname, importconflictpk = self.searchChildfeatureFromPkObjet(dbaseparserfrom, importpkobjet)

            # values from child table
            sql = "SELECT * FROM " + mainconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
            resmain = dbaseparserfrom.query(sql)[0]
            sql = "SELECT * FROM " + importconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
            resimport = dbaseparserfrom.query(sql)[0]

            fields = self.getColumns(mainconflictdbname.lower() + "_qgis")

            # get geom
            resgeom1, resgeom2 = None, None
            if 'geom' in fields:
                sql = " SELECT ST_AsText(geom) FROM " + mainconflictdbname.lower() + "_qgis"
                sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
                resgeommain = dbaseparserfrom.query(sql)[0][0]
                sql = " SELECT ST_AsText(geom) FROM " + importconflictdbname.lower() + "_qgis"
                sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
                resgeomimport = dbaseparserfrom.query(sql)[0][0]




        # manage fields in conflict
        conflict1values = []  # conflict value in main table
        conflict2values = []  # conflict value in import table
        conflictfields = []  # conflict fields in import table
        for i, restemp in enumerate(resmain):
            if (fields[i] not in ['geom', 'datetimecreation', 'datetimemodification']
                    and fields[i][0:3] != "pk_" and fields[i][0:4] != "lpk_"
                    and restemp != resimport[i]):
                conflict1values.append(restemp)
                conflict2values.append(resimport[i])
                conflictfields.append(fields[i])
            elif fields[i] == 'geom' and resgeommain != resgeomimport:
                conflict1values.append(resgeommain)
                conflict2values.append(resgeomimport)
                conflictfields.append(fields[i])

        if debug:
            logging.getLogger("Lamia").debug(' isInConflict - conflictfields : %s  ', str(conflictfields))
            logging.getLogger("Lamia").debug(' isInConflict - conflict1values : %s  ', str(conflict1values))
            logging.getLogger("Lamia").debug(' isInConflict - conflict2values : %s  ', str(conflict2values))


        if len(conflict1values)>0:
            return True, conflictfields, conflict1values, conflict2values
        else:
            return False, None, None, None


    def resolveConflict(self,dbaseparserfrom,conflictobjetids ):
        """
                conflictobjetpks[importid]['fields'] =  listfields
        conflictobjetpks[importid]['mainvalue'] = listvaluemain
        conflictobjetpks[importid]['importvalue'] = listvalueimport
        :param dbaseparserfrom:
        :param conflictobjetpks:
        :return:
        """

        debug = False

        for conflictobjetid in conflictobjetids.keys():

            # cas ou la ligne main a ete supprimee
            sql = "SELECT lpk_revision_end FROM Objet WHERE id_objet = " + str(conflictobjetid)
            resendpks = self.query(sql)
            listrevendpks = [res[0] for res in resendpks]
            # id was suppressed before import - re delet it
            # print('listrevendpks', listrevendpks)
            if not self.maxrevision in listrevendpks:
                conflictobjetids[conflictobjetid]['mainvalue'] = 'Supprime'

            # cas ou la ligne import a ete supprimee
            sql = " SELECT MAX(pk_objet) FROM Objet WHERE id_objet = " + str(conflictobjetid)
            pkobjet = self.query(sql)[0][0]
            if pkobjet is not None:
                sql = " SELECT  lpk_revision_end FROM Objet WHERE pk_objet = " + str(pkobjet)
                mainrevend  = self.query(sql)[0][0]
                if mainrevend is not None:
                    conflictobjetids[conflictobjetid]['importvalue'] = 'Supprime'

            # ui demande
            message =  "ID objet       : " + str(conflictobjetid) + '\n'
            message += "champs         : " + str(conflictobjetids[conflictobjetid]['fields']) + '\n'
            message += "valeurs import : " + str(conflictobjetids[conflictobjetid]['importvalue']) + '\n'
            message += "valeurs main   : " + str(conflictobjetids[conflictobjetid]['mainvalue']) + '\n'

            reply = QMessageBox.question(None, 'Keep import values ?',
                                         message, QMessageBox.Yes, QMessageBox.No)

            # retour a la valeur du main
            if reply == QMessageBox.No:
                if debug : self.printsql = True

                if conflictobjetids[conflictobjetid]['mainvalue'] == 'Supprime':
                    datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    sql = " UPDATE Objet SET "
                    sql += "lpk_revision_begin = " + str(self.maxrevision - 1)
                    sql += ", lpk_revision_end = " + str(self.maxrevision)
                    sql += ", datetimedestruction = '" + str(datesuppr) + "'"
                    sql += " WHERE pk_objet = " + str(pkobjet)
                    self.query(sql, docommit=True)
                    continue

                if conflictobjetids[conflictobjetid]['importvalue'] == 'Supprime':
                    # to know if deleted object - case of deleted objet in import and not in main
                    # sql = " SELECT  lpk_revision_end FROM Objet WHERE pk_objet = " + str(pkobjet)
                    # mainrevend  = self.query(sql)[0][0]
                    # if mainrevend is not None:
                    sql = " UPDATE Objet SET lpk_revision_end = NULL, datetimedestruction = NULL WHERE pk_objet = " + str(pkobjet)
                    self.query(sql, docommit=False)


                childdbname, childpk = self.searchChildfeatureFromPkObjet(self, pkobjet)
                parenttables = [childdbname] + self.getParentTable(childdbname)

                for tablename in parenttables:
                    sql = " SELECT pk_" + tablename.lower() + " FROM " +  childdbname.lower() + "_qgis"
                    sql += " WHERE pk_" + childdbname.lower() + " = " + str(childpk)
                    pktable = self.query(sql)[0][0]
                    fieldstomodif = []
                    valuetoinsert=[]
                    for i, field in enumerate(conflictobjetids[conflictobjetid]['fields']):
                        #for i, field in enumerate(self.dbasetables[tablename]['fields']):
                        #if field in conflictobjetids[conflictobjetid]['fields']:
                        if field in self.dbasetables[tablename]['fields'].keys():
                            # print(i, field, conflictobjetids[conflictobjetid]['mainvalue'])
                            fieldstomodif.append(field)
                            valuetoinsert.append(conflictobjetids[conflictobjetid]['mainvalue'][i])
                        elif field == 'geom' and 'geom' in self.dbasetables[tablename].keys():
                            fieldstomodif.append(field)
                            valuetoinsert.append(conflictobjetids[conflictobjetid]['mainvalue'][i])

                    if fieldstomodif:
                        sql = self.createSetValueSentence(type='UPDATE',
                                                          tablename=tablename,
                                                          listoffields=fieldstomodif,
                                                          listofrawvalues=valuetoinsert)
                        sql += " WHERE pk_" + tablename.lower() + " = " + str(pktable)
                        self.query(sql, docommit=False)
                self.commit()
                if debug: self.printsql = False


            else:
                continue



    def searchChildfeatureFromPkObjet(self,dbaseparser, pkobjet):

        currentdbname = "Objet"
        currentpk = pkobjet

        for order in range(1,10):
            for dbname in self.dbasetables:
                if self.dbasetables[dbname]['order'] == order :
                    if "lpk_" + currentdbname.lower() in self.dbasetables[dbname]['fields'].keys():
                        sql = "SELECT pk_" + dbname.lower() + " FROM " + dbname.lower()
                        sql += " WHERE lpk_" + currentdbname.lower() + " = " + str(currentpk)
                        result = dbaseparser.query(sql)
                        if len(result)== 1 :
                            currentdbname = dbname
                            currentpk = result[0][0]
                            break

        return currentdbname, currentpk




    def exportDbase(self,  exportfile=None ):

        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')

        if self.qgsiface is not None:
            # if not self.dbase.standalone:
            progressMessageBar = self.qgsiface.messageBar().createMessage("Backup...")
            progress = QProgressBar()
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.qgisversion_int)[0:3]) < 220:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, self.qgsiface.messageBar().INFO)
            else:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
            # len
            maxprogress = len(self.dbasetables.keys())
            progress.setMaximum(maxprogress)
        else:
            progress = None

        exportparser = DBaseParser(self.canvas)
        exportparser.createDbase(slfile=exportfile,
                                 crs = self.crsnumber,
                                 worktype = self.type)

        counter = 0
        for order in range(1,10):

            for dbname in self.dbasetables:

                if self.dbasetables[dbname]['order'] == order:
                    counter += 1
                    if progress: progressMessageBar.setText("Import des donnees... : " + dbname)
                    self.setLoadingProgressBar(progress, counter)

                    noncriticalfield = []

                    for field in self.dbasetables[dbname]['fields'].keys():
                            noncriticalfield.append(field)


                    #add geom at rank-1
                    if 'geom' in self.dbasetables[dbname].keys():
                        noncriticalfield.insert(-1, 'ST_AsText(ST_Transform(geom,' + str(self.crsnumber) + '))')


                    sql = ''
                    if 'Objet' in self.getParentTable(dbname):
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower() + "_qgis"
                        sql += " WHERE lpk_revision_end IS NULL"


                    elif 'lpk_revision_end' in self.dbasetables[dbname]['fields'].keys():
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()
                        sql += " WHERE lpk_revision_end IS NULL"


                    else:
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()


                    results = self.query(sql)

                    if 'ST_AsText(ST_Transform(geom,' + str(self.crsnumber) + '))' in noncriticalfield :
                        noncriticalfield[noncriticalfield.index('ST_AsText(ST_Transform(geom,' + str(self.crsnumber) + '))')] = 'geom'


                    # noncriticalfield.insert(0, "id_" + dbname)

                    for i, result in enumerate(results):

                        #traite la mise en forme du result
                        restemp = []
                        if noncriticalfield != ['*']:
                            for l, res in enumerate(result):
                                if noncriticalfield[l] == 'lpk_revision_begin':
                                    restemp.append(str(1))
                                elif isinstance(res, str) or  ( isinstance(res, unicode) and noncriticalfield[l] != 'geom') :
                                    if sys.version_info.major == 2:
                                        if isinstance(res, unicode):
                                            restemp.append("'" + res.replace("'","''") + "'")
                                        else:
                                            restemp.append("'" + str(res).replace("'", "''") + "'")
                                    else:
                                        restemp.append("'" + str(res).replace("'", "''") + "'")

                                elif noncriticalfield[l] == 'geom' and res is not None:
                                    # print('geom', "ST_GeomFromText('" + res + "', " + str(self.crsnumber)  + ")")
                                    restemp.append("ST_GeomFromText('" + res + "', " + str(self.crsnumber)  + ")")

                                elif res is None or res == '':
                                    restemp.append('NULL')
                                else:
                                    restemp.append(str(res))

                            # copy les valeurs
                            if True:
                                sql = "INSERT INTO " + dbname + '(' + ','.join(noncriticalfield) + ')'
                                sql += " VALUES(" + ','.join(restemp) + ")"
                                exportparser.query(sql,docommit=False)



                            #ressource
                            if dbname == 'Ressource':
                                fileindex = noncriticalfield.index('file')
                                filepath = result[fileindex]

                                pkobjetindex = noncriticalfield.index('lpk_objet')
                                pkobjet = result[pkobjetindex]

                                childdbname, childpk = self.searchChildfeatureFromPkObjet(self, pkobjet)

                                # only export reference rasters
                                if childdbname.lower() == 'rasters':
                                    sql = " SELECT typeraster FROM Rasters_qgis WHERE pk_rasters = " + str(childpk)
                                    typeraster = self.query(sql,docommit=False)[0][0]
                                    if typeraster not in ['ORF', 'IRF']:
                                        continue


                                if not self.isAttributeNull(filepath):

                                    # print(self.dbaseressourcesdirectory,filepath,  exportparser.dbaseressourcesdirectory)

                                    fromfile = os.path.join(self.dbaseressourcesdirectory, filepath)
                                    tofile = os.path.join(exportparser.dbaseressourcesdirectory, filepath)

                                    self.copyRessourceFile(fromfile=fromfile,
                                                           tofile=tofile,
                                                           withthumbnail=1,
                                                           copywholedirforraster = True)


                        else:
                            sql = "INSERT INTO " + dbname + " DEFAULT VALUES"
                            exportparser.query(sql,docommit=False)


                    exportparser.commit()


        #update seq file to remember last pk of each table
        sql = "SELECT * FROM sqlite_sequence "
        results = self.query(sql)
        for res in results:
            if res[0] == 'Revision':
                continue
            sql = "UPDATE sqlite_sequence SET seq = " + str(res[1])
            sql += " WHERE name = '" + str(res[0]) + "'"
            exportparser.query(sql)

        datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sql = "INSERT INTO Revision(datetimerevision, commentaire)  "
        sql += " VALUES('" + datecreation + "','travail horsligne')"
        exportparser.query(sql)

        if progress is not None: self.qgsiface.messageBar().clearWidgets()



    def backupBase(self):

        if self.qgsiface is not None:
            #if not self.dbase.standalone:
            progressMessageBar = self.qgsiface.messageBar().createMessage("Backup...")
            progress = QProgressBar()
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.qgisversion_int)[0:3]) < 220:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, self.qgsiface.messageBar().INFO)
            else:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
            #len
            maxprogress = len(self.dbasetables.keys())
            progress.setMaximum(maxprogress)
        else:
            progress = None

        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')


        datesuppr = str(datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S"))
        # fileexport = os.path.join(exportdir, 'backup_' + datesuppr + '.sqlite')
        exportdir = os.path.join(self.dbaseressourcesdirectory , 'backup')
        if not os.path.exists(exportdir):
            os.makedirs(exportdir)

        fileexport = os.path.join(exportdir, 'backup_' + datesuppr + '.sqlite')

        exportparser = DBaseParser(self.canvas)
        exportparser.createDbase(slfile=fileexport,
                                 crs=self.crsnumber,
                                 worktype=self.type)


        counter = 0
        for order in range(0, 10):
            for dbname in self.dbasetables:
                if self.dbasetables[dbname]['order'] == order:
                    counter += 1
                    self.setLoadingProgressBar(progress, counter)

                    if dbname.lower() == 'basedonnees':
                        continue

                    # self.normalMessage.emit("Export de " + str(dbname))

                    noncriticalfield = []

                    for field in self.dbasetables[dbname]['fields'].keys():
                            noncriticalfield.append(field)

                    #add geom at rank-1
                    if 'geom' in self.dbasetables[dbname].keys():
                        noncriticalfield.insert(-1, 'ST_AsText(ST_Transform(geom,' + str(self.crsnumber) + '))')

                    sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()

                    results = self.query(sql)

                    if 'ST_AsText(ST_Transform(geom,' + str(self.crsnumber) + '))' in noncriticalfield :
                        noncriticalfield[noncriticalfield.index('ST_AsText(ST_Transform(geom,' + str(self.crsnumber) + '))')] = 'geom'

                    for i, result in enumerate(results):
                        if dbname.lower() == 'revision' and i == 0:
                            continue

                        #traite la mise en forme du result
                        sql = self.createSetValueSentence(type='INSERT',
                                                          tablename=dbname,
                                                          listoffields=noncriticalfield,
                                                          listofrawvalues=result)
                        exportparser.query(sql, docommit=False)

                    exportparser.commit()

        if False:
            #update seq file to remember last pk of each table
            sql = "SELECT * FROM sqlite_sequence "
            results = self.query(sql)
            for res in results:
                if res[0] == 'Revision':
                    continue
                sql = "UPDATE sqlite_sequence SET seq = " + str(res[1])
                sql += " WHERE name = '" + str(res[0]) + "'"
                exportparser.query(sql)

            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "INSERT INTO Revision(datetimerevision, commentaire)  "
            sql += " VALUES('" + datecreation + "','travail horsligne')"
            exportparser.query(sql)
        if progress is not None: self.qgsiface.messageBar().clearWidgets()
        # print(self.dbasetables)







    def updateIdPkSqL(self,tablename=None, listoffields=[], listofrawvalues=[], dictpk = {}, dictid = {}, changeID = True):
        pktable = None
        fields = []
        values = []

        for k, field in enumerate(listoffields):

            if "pk_" == field[0:3]:
                pktable = self.getLastRowId(tablename)
                # print(pktable)
                pkoldtable = listofrawvalues[k]
                dictpk[tablename.lower()][pkoldtable] = pktable


            elif "id_" == field[0:3]:

                fields.append(field)
                if changeID :
                    idtable = self.getLastId(tablename) + 1
                else:
                    idtable = listofrawvalues[k]
                values.append(str(idtable))

                oldid = listofrawvalues[k]
                dictid[tablename.lower()][oldid] = idtable

            elif "lid_" == field[0:4]:
                if field.split('_')[1] in dictid.keys():
                    if listofrawvalues[k] is not None:
                        if listofrawvalues[k] in dictid[field.split('_')[1]].keys():
                            fields.append(field)
                            values.append(str(dictid[field.split('_')[1]][listofrawvalues[k]]))
                        else:
                            fields.append(field)
                            values.append(str(  listofrawvalues[k]    ))
                            print('error lid_' )
                            print('base : ' ,tablename, ' - column : ', field, ' - lid value : ',listofrawvalues[k]  )

                else:
                    if listofrawvalues[k] is not None:
                        fields.append(field)
                        values.append(str(listofrawvalues[k]))

            elif "lpk_" == field[0:4]:

                #if "lpk_revision_begin" in self.dbasetables[tablename]['fields'].keys():
                if field == "lpk_revision_begin":
                    fields.append('lpk_revision_begin')
                    values.append(str(self.maxrevision))



                elif field.split('_')[1] in dictpk.keys():
                    if listofrawvalues[k] is not None:
                        if listofrawvalues[k] in dictpk[field.split('_')[1]].keys():
                            fields.append(field)
                            values.append(str(dictpk[field.split('_')[1]][listofrawvalues[k]]))
                        else:
                            print('error lpk_', listofrawvalues)


        if "lpk_revision_begin" in listoffields and not changeID:
            #pkcurrentable
            sql = " SELECT pk_" + tablename.lower() + " FROM " + tablename.lower()
            sql += " WHERE id_" + tablename.lower() + " = " + str(idtable)
            sql += " AND lpk_revision_end IS NULL"

            tempres = self.query(sql)

            if len(tempres)>0:
                pkcurrenttable = self.query(sql)[0][0]


                sql = "UPDATE " + tablename.lower() + " SET lpk_revision_end = " + str(self.maxrevision)
                sql += " WHERE pk_" + tablename.lower() + " = " + str(pkcurrenttable)
                self.query(sql, docommit=False)

        # if i % 50 == 0:
            # if debug: logging.getLogger("Lamia").debug(' field, value : %s %s  ', str(fields), str(values))

        if pktable is not None:
            # update line
            sqlup = "UPDATE " + tablename.lower() + " SET "
            for j, field in enumerate(fields):
                sqlup += field + " = " + str(values[j]) + ","
            sqlup = sqlup[:-1]
            sqlup += " WHERE pk_" + tablename.lower() + ' = ' + str(pktable)

            #self.query(sqlup, docommit=False)



        return sqlup





    def createSetValueSentence(self,type='INSERT',tablename=None, listoffields=[], listofrawvalues=[]):

        debug = False
        if debug : logging.getLogger("Lamia").debug(' fields / rawvalues %s %s  ', str(listoffields), str(listofrawvalues))

        restemp = []

        for l, res in enumerate(listofrawvalues):
            if sys.version_info.major == 2:
                if isinstance(res, str) or (isinstance(res, unicode) and listoffields[l] != 'geom'):
                    if isinstance(res, unicode):
                        restemp.append("'" + res.replace("'", "''") + "'")
                    else:
                        restemp.append("'" + str(res).replace("'", "''") + "'")

                elif listoffields[l] == 'geom' and res is not None:
                    # print('geom', "ST_GeomFromText('" + res + "', " + str(self.crsnumber)  + ")")
                    restemp.append("ST_GeomFromText('" + res + "', " + str(self.crsnumber) + ")")
                elif res is None or res == '':
                    restemp.append('NULL')
                else:
                    restemp.append(str(res))

            elif sys.version_info.major == 3:
                #print(res, str(type(res)))
                if isinstance(res, str)  and listoffields[l] != 'geom':
                    restemp.append("'" + str(res).replace("'", "''") + "'")
                elif listoffields[l] == 'geom' and res is not None:
                    # print('geom', "ST_GeomFromText('" + res + "', " + str(self.crsnumber)  + ")")
                    restemp.append("ST_GeomFromText('" + res + "', " + str(self.crsnumber) + ")")
                elif res is None or res == '':
                    restemp.append('NULL')
                else:
                    restemp.append(str(res))

        if type == 'INSERT':
            sql = "INSERT INTO " + tablename + '(' + ','.join(listoffields) + ')'
            sql += " VALUES(" + ','.join(restemp) + ")"

        elif type == 'UPDATE':
            sql = " UPDATE " + tablename.lower() + " SET "
            for i, field in enumerate(listoffields):
                sql += field + " = " + str(restemp[i]) + ', '
            sql = sql[:-2]

        return sql



    def copyRessourceFile(self,fromfile, tofile, withthumbnail=0, copywholedirforraster = False):
        """

        :param fromrep:
        :param fromfile:
        :param torep:
        :param withthumbnail: 0 : copy  file + create thumbnail ; 1 : copy only thumnail; 2 : copyonly file
        :param copywholedirforraster:
        :return:
        """

        debug = False

        if debug: logging.getLogger("Lamia").debug('Copy %s %s', str(fromfile), str(tofile))

        fromfile = fromfile
        fromdir =  os.path.dirname(fromfile)
        fromfilename, fromfileext = os.path.splitext(os.path.basename(fromfile))
        destinationfile = tofile
        destinationdir = os.path.dirname(destinationfile)
        destinationfilename, destinationfileext = os.path.splitext(os.path.basename(destinationfile))

        if os.path.isfile(fromfile):

            if copywholedirforraster and 'Rasters' in fromfile:
                if not os.path.exists(destinationdir):
                    shutil.copytree(fromdir, destinationdir)
            else:
                if not os.path.exists(destinationdir):
                    os.makedirs(destinationdir)

                fromfilebase, fromext = os.path.splitext(fromfile)
                tofilebase, toext = os.path.splitext(destinationfile)


                if len(fromfilebase.split('_')) > 1 and fromfilebase.split('_')[1] == 'croquis':
                    shutil.copy(fromfile, destinationfile)

                elif fromext in ['.shp']:
                    dirfiles = [f for f in os.listdir(fromdir) if os.path.isfile(os.path.join(fromdir,f))]
                    for dirfile in dirfiles:
                        dirfilebase, dirfileext = os.path.splitext(dirfile)
                        if dirfilebase == fromfilename:
                            fromshpfile = os.path.join(fromdir,dirfilebase + dirfileext )
                            toshpfile = os.path.join(destinationdir,destinationfilename + dirfileext)
                            shutil.copy(fromshpfile, toshpfile)

                else:
                    if withthumbnail in [0,1] and PILexists and fromext.lower() in ['.jpg', '.jpeg', '.png']:

                        possibletbnailfile = fromfilebase + "_thumbnail.png"
                        if os.path.isfile(possibletbnailfile):
                            if possibletbnailfile != tofilebase + "_thumbnail.png":
                                shutil.copy(possibletbnailfile, tofilebase + "_thumbnail.png")
                        else:
                            size = 256, 256
                            im = PIL.Image.open(fromfile)
                            im.thumbnail(size)
                            im.save(tofilebase + "_thumbnail.png", "PNG")

                    if withthumbnail in [0,2]:
                        shutil.copy(fromfile, destinationfile)




    def setLoadingProgressBar(self, progressbar, val):
        if progressbar is not None:
            progressbar.setValue(val)
        else:
            logging.getLogger("Lamia").info('Chargement %d', val )
        QApplication.processEvents()




    def getTimeNow(self):
        if  sys.version_info.major == 2:
            return time.clock()
        elif sys.version_info.major == 3:
            return time.process_time()
