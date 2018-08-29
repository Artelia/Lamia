# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from qgis.PyQt import QtCore
import os
import sys
import qgis
import qgis.utils
qgis.utils.uninstallErrorHook()     #for standart output
import math

try:
    from pyspatialite import dbapi2 as db
    from pyspatialite.dbapi2 import *
except ImportError:
    import sqlite3
    from sqlite3 import *
    print('spatialite not enabled')
import psycopg2
import glob
from collections import OrderedDict

import logging
#logger = logging.getLogger("Lamia")


class DBaseParser(QtCore.QObject):
    """!
    the database parser
    """

    recentDBaseChanged = QtCore.pyqtSignal()
    dBaseLoaded = QtCore.pyqtSignal()
    errorMessage = QtCore.pyqtSignal(str)



    def __init__(self,canvas):
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
        #  not used yet
        self.searchbuffer = 20
        # used to define the working date in db
        self.workingdate = QtCore.QDate.currentDate().toString('yyyy-MM-dd')
        # crs of dbase
        self.crsnumber = None
        self.qgiscrs = None
        #gps things
        self.hauteurperche = 2.0
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
        self.horsligne=False
        self.date_deconnexion=None
        self.offLineConn=None
        self.offLineCursor = None
        self.pghost = None
        self.pgdb = None
        self.pguser = None
        self.pgpassword = None
        self.pgport = None
        self.pgschema = None
        #the qgis canvas
        self.canvas = canvas
        # self.canvas.renderStarting.connect(self.renderStarts)
        # the QgsCoordinateTransform var
        self.xform = None
        self.xformreverse = None
        #debug
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

        self.revisionwork = False
        self.currentrevision = None
        self.maxrevision = 0



        self._readRecentDBase()

        #getqgisversion : ex : 21820
        try:
            self.qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
        except AttributeError:  #qgis 3
            self.qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT

        self.qgsiface = qgis.utils.iface



        #logger.info('qgisversion : %s', str(self.qgisversion_int))
        #logging.getLogger("Lamia").info('qgisversion : %s', str(self.qgisversion_int))

    """

    def renderStarts(self):
        # print('digue render')
        if self.dbasetype == 'spatialite':
            if False and self.connSLITE is not None:
                self.SLITEcursor.close()
                self.connSLITE.close()
                self.connSLITE = None
            if self.SLITEcursor is not None:
                self.SLITEcursor.close()
                self.SLITEcursor = None

        elif self.dbasetype == 'postgis':
            if False and self.connPGis is not None:
                self.PGiscursor.close()
                self.connPGis.close()
                self.connPGis = None
            if self.PGiscursor is not None:
                self.PGiscursor.close()
                self.PGiscursor = None
    """


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

    def createDbase(self, file=None, crs=None, type=None, dbasetype='spatialite',
                    dbname=None, schema=None, user=None, host='localhost', port=None, password=None,    # postgis
                    dbaseressourcesdirectory=None):
        """
        pass
        :param file:
        :param crs:
        :param type:
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

        # create dbasedict
        self.createDBDictionary(type)
        # manage ressource directory
        if False:
            if not os.path.isdir(dbaseressourcesdirectory):
                os.makedirs(dbaseressourcesdirectory)
        if True:
            if dbaseressourcesdirectory is None and dbasetype == 'spatialite':
                dbaseressourcesdirectorytemp = os.path.join(os.path.dirname(file),'DBspatialite')
            else:
                dbaseressourcesdirectorytemp = dbaseressourcesdirectory

            if not os.path.isdir(dbaseressourcesdirectorytemp):
                os.makedirs(dbaseressourcesdirectorytemp)

        # sql file contains output of dbase creation script
        sqlfile = os.path.join(dbaseressourcesdirectorytemp, 'sqlcreation.txt')
        openedsqlfile = open(sqlfile, u'w')
        # dbasetype
        self.dbasetype = dbasetype

        # ***************************************************************************************
        # Manage connection - creation and config
        if self.dbasetype == 'spatialite':
            self.spatialitefile = file
            if sys.version_info.major == 2:
                self.connSLITE = db.connect(file)
            elif sys.version_info.major == 3:   #python 3
                self.connSLITE = qgis.utils.spatialite_connect(file)
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
            connectstr = "dbname='" + self.pgdb + "' user='" + user + "' host='" + host + "' password='" + password + "'"
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
            # print(sql)
            # res = self.PGiscursor.execute(sql)
            self.query(sql)
            self.commit()
            sql = 'SET search_path TO ' + self.pgschema + ',public'
            self.query(sql)
            self.commit()
            # print(sql)
            # res = self.PGiscursor.execute(sql)
            if False:

                sql = 'GRANT ALL ON SCHEMA '+self.pgschema+' TO vadjango'
                self.query(sql)
                self.commit()



        # ***************************************************************************************
        # Tables creation
        for order in range(10):
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

                    if debug: logging.getLogger("Lamia").debug('sql : %s', sql['main'] )

                    self.query(sql['main'])
                    self.commit()
                    if 'other' in sql.keys():
                        for sqlother in sql['other']:
                            openedsqlfile.write(sqlother + '\n')
                            # print(sqlother)
                            self.query(sqlother)
                            self.commit()


        if dbaseressourcesdirectory is None and dbasetype == 'spatialite':
            dbaseressourcesdirectorytemp2 = '.\DBspatialite'
        else:
            dbaseressourcesdirectorytemp2 = dbaseressourcesdirectorytemp

        sql = "INSERT INTO Basedonnees (metier,repertoireressources,crs) "
        sql += "VALUES('" + type + "','" + dbaseressourcesdirectorytemp2 + "'," + str(crs) + ");"
        self.query(sql)
        self.commit()

        if self.revisionwork:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            sql = "INSERT INTO Revision (daterevision, commentaire) "
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
                        sql += "f_table_name, f_geometry_column,read_only) VALUES ("
                        # sql += "'" + str(viewlower) + "','geom','id_" + str(dbnamelower) + "','" + str(dbnamelower) + "','geom',0);"
                        sql += "'" + str(viewlower) + "','geom','" + idcolumnname + "','" + str(dbnamelower) + "','geom',0);"
                        openedsqlfile.write(sql + '\n')
                        self.query(sql)
                        self.commit()
                    elif dbasetype == 'postgis':
                        dbnamelower = dbname.lower()
                        idcolumnname = self.getFirstIdColumn(viewnames[viewname])
                        viewlower = viewnames[viewname].lower()
                        sql = 'INSERT INTO geometry_columns(f_table_catalog, f_table_schema, f_table_name, '
                        sql += 'f_geometry_column, coord_dimension, srid, "type") VALUES ('
                        sql += "'" + type.lower() + "', '" + self.pgschema.lower() + "', '" + str( viewlower) + "','geom',2,"
                        sql += str(crs) + ",'" + self.dbasetables[dbname]['geom'] + "' );"
                        # print(sql)
                        openedsqlfile.write(sql + '\n')
                        self.query(sql)
                        self.commit()




                if False:
                    #sql = 'CREATE VIEW ' + str(dbname) + '_view AS '
                    sql = 'CREATE VIEW ' + str(viewnames[viewname]) + ' AS '
                    if self.dbasetables[dbname]['sqlview'] != '':
                        sql += self.dbasetables[dbname]['sqlview']
                    else:
                        sql += 'SELECT * FROM ' + str(dbname)
                    openedsqlfile.write(sql + '\n')
                    self.query(sql)
                    self.commit()
                    # add view in geom register
                    if 'geom' in self.dbasetables[dbname].keys():
                        if self.dbasetype == 'spatialite':
                            dbnamelower = dbname.lower()
                            sql = "INSERT INTO views_geometry_columns (view_name, view_geometry, view_rowid, "
                            sql += "f_table_name, f_geometry_column,read_only) VALUES ("
                            sql += "'" + str(dbnamelower) + "_view','geom','id_" + str(dbnamelower) + "','" + str(dbnamelower) + "','geom',0);"
                            # print(sql)
                            self.query(sql)
                            self.commit()
                        elif dbasetype == 'postgis':
                            dbnamelower = dbname.lower()
                            sql = 'INSERT INTO geometry_columns(f_table_catalog, f_table_schema, f_table_name, '
                            sql += 'f_geometry_column, coord_dimension, srid, "type") VALUES ('
                            sql += "'" + type.lower() + "', '" + self.pgschema.lower()  +"', '" + str(dbnamelower) + "_view','geom',2,"
                            sql += str(crs) + ",'" + self.dbasetables[dbname]['geom'] + "' );"
                            # print(sql)
                            openedsqlfile.write(sql + '\n')
                            self.query(sql)
                            self.commit()

        #delete non used srid
        if False:
            if self.dbasetype == 'spatialite':
                sql = "DELETE FROM spatial_ref_sys_aux WHERE srid != " + str(crs)
                print(sql)
                self.query(sql)
                self.commit()

                sql = "DELETE FROM spatial_ref_sys WHERE srid != " + str(crs)
                print(sql)
                self.query(sql)
                self.commit()


        openedsqlfile.close()

        self.loadQgisVectorLayers(file=self.spatialitefile, dbasetype=self.dbasetype,
                                  host=self.pghost, port=self.pgport, dbname=self.pgdb, schema=self.pgschema,
                                  user=self.pguser, password=self.pgpassword)


    def createDBDictionary(self, type):
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
        self.type = type
        self.dbasetables = {}
        createfilesdir = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'create', self.type)

        if len(self.type.split('_')) == 2 and self.type.split('_')[0] == 'Base':
            parsertemp = DBaseParser(None)
            parsertemp.createDBDictionary('Base')
            self.dbasetables = parsertemp.dbasetables
            del parsertemp






        for filename in glob.glob(os.path.join(createfilesdir, '*.txt')):

            # print(filename)
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
                        self.dbasetables[tablename]['qgisviewsql'] = line[5:].strip()
                    elif line[0:5] == '#EXPO':
                        self.dbasetables[tablename]['exportviewsql'] = line[5:].strip()
                    elif line[0:5] == '#SCAL':
                        self.dbasetables[tablename]['scale'] = float(line[5:].strip())
                    elif line[0:5] == '#SHOW':
                        value = line[5:].strip()
                        if value == 'YES':
                            self.dbasetables[tablename]['showinqgis'] = True
                    else:
                        continue


                else:                           # field constraint
                    if 'Cst' in self.dbasetables[tablename]['fields'][fieldname].keys():
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'].append([])
                    else:
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'] = [[]]

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


        # print(self.dbasetables)

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


    def loadQgisVectorLayers(self, file=None, dbasetype='spatialite',
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

        self._AddDbaseInRecentsDBase(spatialitefile=file, host=host, port=port, dbname=dbname, schema=schema, user=user,
                                     password=password)
        self.reInitDBase()

        sql = "SELECT metier, repertoireressources,crs FROM Basedonnees;"
        query = self.query(sql)
        type, resdir, crs = [row[0:3] for row in query][0]
        if resdir[0] == '.' and self.dbasetype == 'spatialite':
            self.dbaseressourcesdirectory = os.path.join(os.path.dirname(self.spatialitefile ), resdir)
        else:
            self.dbaseressourcesdirectory = os.path.normpath(resdir)
        self.crsnumber = crs
        self.qgiscrs = qgis.core.QgsCoordinateReferenceSystem(self.crsnumber)



        if debug: logging.getLogger('Lamia').debug('step2')

        if type is not None:
            self.createDBDictionary(type)

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
                    #if geom is not None:
                    if self.isTableSpatial(tablename):
                        uri.setDataSource('', str(tablename), 'geom')
                    else:
                        uri.setDataSource('', str(tablename), '')
                    self.dbasetables[tablename]['layer'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'spatialite')

                    # view layer qgis
                    #if geom is not None:

                    #get id column
                    idcolumnname = self.getFirstIdColumn(tablename + '_qgis')
                    # print('***', tablename + '_qgis' , idcolumnname)

                    if self.isTableSpatial(str(tablename)+'_qgis'):
                        #uri.setDataSource('', str(tablename)+'_qgis', 'geom', '', "id_" + str(tablename).lower())
                        uri.setDataSource('', str(tablename) + '_qgis', 'geom', '', idcolumnname)

                    else:
                        #uri.setDataSource('', str(tablename) + '_qgis', '', '', "id_" + str(tablename).lower())
                        uri.setDataSource('', str(tablename) + '_qgis', '', '', idcolumnname)
                    self.dbasetables[tablename]['layerqgis'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'spatialite')

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
            timestart = time.clock()

        if self.dbasetype == 'spatialite':
            # cursor = self.connSLITE.cursor()
            if self.SLITEcursor is None:
                # self.connSLITE = db.connect(self.spatialitefile)
                self.SLITEcursor = self.connSLITE.cursor()
            try:
                if self.printsql :
                    logging.getLogger('Lamia').debug('%s %.3f', sql,  time.clock() - timestart)
                query = self.SLITEcursor.execute(sql,arguments)
                returnquery = list(query)
                if docommit:
                    self.commit()

                return returnquery
            except OperationalError as e:
                if self.qgsiface is None:
                    print('error query', e)
                return None
        elif self.dbasetype == 'postgis':
            if self.PGiscursor is None:
                # connectstr = "dbname='" + self.pgdb + "' user='" + self.pguser + "' host='"
                # connectstr += self.pghost + "' password='" + self.pgpassword + "'"
                # self.connPGis = psycopg2.connect(connectstr)
                self.PGiscursor = self.connPGis.cursor()
            try:
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
                        logging.getLogger('Lamia').debug('%s %.3f', sql, time.clock() - timestart)
                    return returnrows
                except psycopg2.ProgrammingError as e:
                    print('error query', e)
                    return None

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


    def _readRecentDBase(self):
        """
        Lit le fichier des bases de données recentes et rempli le  menu\Fichier\base de données recentes
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
        Ajoute le chemin dans le fichier chargé dans Menu\Fichier\base de données recentes
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
        menu\Fichier\base de données recentes
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
        if self.dbasetype == 'spatialite':
            subsetstring = '"datecreation" <= ' + "'" + self.workingdate + "'"
            subsetstring += ' AND CASE WHEN "datedestruction" IS NOT NULL  THEN "datedestruction" > ' + "'" + self.workingdate + "'" + ' ELSE 1 END'
            if self.revisionwork:
                subsetstring += ' AND "revisionbegin" <= ' + str(self.currentrevision)
                subsetstring += ' AND CASE WHEN "revisionend" IS NOT NULL  THEN "revisionend" > '  + str(self.currentrevision)  + ' ELSE 1 END'

        elif self.dbasetype == 'postgis':
            subsetstring = '"datecreation" <= ' + "'" + self.workingdate + "'"
            subsetstring += ' AND CASE WHEN "datedestruction" IS NOT NULL  THEN "datedestruction" > ' + "'" + self.workingdate + "'" + ' ELSE TRUE END'
            if self.revisionwork:
                subsetstring += ' AND "revisionbegin" <= ' + str(self.currentrevision)
                subsetstring += ' AND CASE WHEN "revisionend" IS NOT NULL  THEN "revisionend" > '  + str(self.currentrevision)  + ' ELSE TRUE END'

        for tablename in self.dbasetables:
            fieldnames = [field.name().lower() for field in self.dbasetables[tablename]['layerqgis'].fields()]
            if 'datecreation' in fieldnames:
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
                logging.getLogger("Lamia").debug('error %s %s %s',e, table,field )
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
        if (table in self.dbasetables.keys()
            and field in self.dbasetables[table]['fields'].keys()
            and 'Cst' in self.dbasetables[table]['fields'][field].keys()):

            dbasetable = self.dbasetables[table]
            #if field in dbasetable['fields'].keys() and 'Cst' in dbasetable['fields'][field].keys():
            if not self.isAttributeNull(rawvalue):
                if isinstance(rawvalue, int) or isinstance(rawvalue, long):
                    rawvalue = str(rawvalue)

                index = [value[1] for value in dbasetable['fields'][field]['Cst']].index(rawvalue)
                return dbasetable['fields'][field]['Cst'][index][0]
            else:
                return ''
        else:
            if not self.isAttributeNull(rawvalue):
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
            timestart = time.clock()

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
            if not nearestfetgeom.isGeosValid() and nearestfetgeom.type() == 1:
                nearestfetgeom = qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(nearestfetgeom.asPolyline()[0]))

            disfrompoint = nearestfetgeom.distance(point2geom)
            bboxtofilter = point2geom.buffer(disfrompoint * 1.2, 12).boundingBox()
            idsintersectingbbox = spindex.intersects(bboxtofilter)

            if debug: logging.getLogger("Lamia").debug('idsintersectingbbox %s', str(idsintersectingbbox))

            # search nearest geom in bbox
            distance = None
            nearestindex = None
            finalgeomispoint = False

            for intersectingid in idsintersectingbbox:
                ispoint = False
                if not self.revisionwork:
                    feat = self.getLayerFeatureById(dbasetablename, intersectingid)
                else:
                    feat = self.getLayerFeatureByPk(dbasetablename, intersectingid)
                featgeom = feat.geometry()

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

                # algo for keeping point in linestring layer as nearest
                # if point is nearest than 1.2 x dist from nearest line
                if distance is None:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = ispoint
                elif not finalgeomispoint and ispoint and dist < distance*1.2:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = True
                elif dist < distance:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = ispoint

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


            if True:
                txtrequest = ' "id_' + layername.lower() + '" =  ' + str(fid)
                request = qgis.core.QgsFeatureRequest().setFilterExpression(txtrequest)
                # request.setFlags(qgis.core.QgsFeatureRequest.NoGeometry)
                if int(str(self.qgisversion_int)[0:3]) < 220:
                    qgisfeat = self.dbasetables[layername]['layer'].getFeatures(request).next()
                else:
                    qgisfeat = self.dbasetables[layername]['layer'].getFeatures(request).__next__()

                # print(txtrequest, qgisfeat.id(), qgisfeat.attributes())

                return qgisfeat

    def getLayerFeatureByPk(self, layername, fid):
        """
        Renvoie le QgsFeature de la table lamia nommée layername dont le pk est fid
        :param layername: le nom de la table dans la BD lamia
        :param fid: le pk dont on veut le feature
        :return: le QgsFeature associé au pk demandé
        """
        if int(str(self.qgisversion_int)[0:3]) < 220:
            return self.dbasetables[layername]['layer'].getFeatures(qgis.core.QgsFeatureRequest(fid)).next()
        else:
            return self.dbasetables[layername]['layer'].getFeature(fid)

    def dateVersionConstraintSQL(self):
        """
        Crée une chaine à rajouter à la fin d'autre requetes pour spécifier la date et la version voulue
        :return: requete sql comprenant les éléments nécessaires pour filtrer les dates et les versions
        """
        sqlin = ' datecreation <= ' + "'" + self.workingdate + "'"
        if self.dbasetype == 'postgis':
            sqlin += ' AND CASE WHEN datedestruction IS NOT NULL  '
            sqlin += 'THEN DateDestruction > ' + "'" + self.workingdate + "'" + ' ELSE TRUE END'
            if self.revisionwork:
                sqlin += " AND revisionbegin <= " + str(self.currentrevision)
                sqlin += " AND CASE WHEN revisionend IS NOT NULL THEN "
                sqlin += " revisionend > " + str(self.currentrevision)
                sqlin += " ELSE TRUE END "
        elif self.dbasetype == 'spatialite':
            sqlin += ' AND CASE WHEN datedestruction IS NOT NULL  '
            sqlin += 'THEN datedestruction > ' + "'" + self.workingdate + "'" + ' ELSE 1 END'
            if self.revisionwork:
                sqlin += " AND revisionbegin <= " + str(self.currentrevision)
                sqlin += " AND CASE WHEN revisionend IS NOT NULL THEN "
                sqlin += " revisionend > " + str(self.currentrevision)
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
            sql = "SELECT currval('" + tablelower + "_id_" + tablelower + "_seq');"
            query = self.query(sql)
            id = [row[0] for row in query][0]
        return id

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

    def exportBase(self, exportdbase):

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

