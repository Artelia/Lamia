# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from qgis.PyQt import QtCore
import os
import qgis
import qgis.utils
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



        self._readRecentDBase()

        #getqgisversion : ex : 21820
        try:
            self.qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
        except AttributeError:  #qgis 3
            self.qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT

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
        # create dbasedict
        self._createDBDictionary(type)
        # manage ressource directory
        if False:
            if not os.path.isdir(dbaseressourcesdirectory):
                os.makedirs(dbaseressourcesdirectory)
        if True:
            if dbaseressourcesdirectory is None and dbasetype == 'spatialite':
                dbaseressourcesdirectory = os.path.join(os.path.dirname(file),'DBspatialite')

            if not os.path.isdir(dbaseressourcesdirectory):
                os.makedirs(dbaseressourcesdirectory)

        # sql file contains output of dbase creation script
        sqlfile = os.path.join(dbaseressourcesdirectory, 'sqlcreation.txt')
        openedsqlfile = open(sqlfile, u'w')
        # dbasetype
        self.dbasetype = dbasetype

        # ***************************************************************************************
        # Manage connection - creation and config
        if self.dbasetype == 'spatialite':
            self.spatialitefile = file
            try:    #python 2
                self.connSLITE = db.connect(file)
            except NameError:   #python 3
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
            # print(sql)
            # res = self.PGiscursor.execute(sql)
            self.query(sql)
            self.commit()
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
                    print(sql['main'])
                    self.query(sql['main'])
                    self.commit()
                    if 'other' in sql.keys():
                        for sqlother in sql['other']:
                            openedsqlfile.write(sqlother + '\n')
                            # print(sqlother)
                            self.query(sqlother)
                            self.commit()

        sql = "INSERT INTO Basedonnees (metier,repertoireressources,crs) "
        sql += "VALUES('" + type + "','" + dbaseressourcesdirectory + "'," + str(crs) + ");"
        self.query(sql)
        self.commit()

        # ***************************************************************************************
        # view creation
        for dbname in self.dbasetables:
            print(dbname)
            viewnames={}
            if 'djangoviewsql' in self.dbasetables[dbname].keys():
                viewnames['djangoviewsql'] = str(dbname) + '_django'
            if 'qgisviewsql' in self.dbasetables[dbname].keys():
                viewnames['qgisviewsql'] = str(dbname) + '_qgis'

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
                if 'geom' in self.dbasetables[dbname].keys():
                    if self.dbasetype == 'spatialite':
                        dbnamelower = dbname.lower()
                        viewlower = viewnames[viewname].lower()
                        sql = "INSERT INTO views_geometry_columns (view_name, view_geometry, view_rowid, "
                        sql += "f_table_name, f_geometry_column,read_only) VALUES ("
                        sql += "'" + str(viewlower) + "','geom','id_" + str(dbnamelower) + "','" + str(
                            dbnamelower) + "','geom',0);"
                        # print(sql)
                        self.query(sql)
                        self.commit()
                    elif dbasetype == 'postgis':
                        dbnamelower = dbname.lower()
                        viewlower = viewnames[viewname].lower()
                        sql = 'INSERT INTO geometry_columns(f_table_catalog, f_table_schema, f_table_name, '
                        sql += 'f_geometry_column, coord_dimension, srid, "type") VALUES ('
                        sql += "'" + type.lower() + "', '" + self.pgschema.lower() + "', '" + str(
                            viewlower) + "','geom',2,"
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

        self.loadQgisVectorLayers(file=self.spatialitefile, dbasetype=self.dbasetype,
                                  host=self.pghost, port=self.pgport, dbname=self.pgdb, schema=self.pgschema,
                                  user=self.pguser, password=self.pgpassword)


    def _createDBDictionary(self, type):
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
                          'layer' : real layer
                          'layerqgis' : view layer with parent fields
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
        # first readfiles in ./DBASE\create directory and create self.dbasetables
        self.type = type
        self.dbasetables = {}
        createfilesdir = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'create', self.type)

        for filename in glob.glob(os.path.join(createfilesdir, '*.txt')):
            print(filename)
            basename = os.path.basename(filename).split('.')[0]
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
            self.dbasetables[tablename] = {}
            self.dbasetables[tablename]['order'] = int(temp[0])
            self.dbasetables[tablename]['fields'] = OrderedDict()
            self.dbasetables[tablename]['showinqgis'] = False
            self.dbasetables[tablename]['widget'] = []

            file = open(filename, 'r')
            compt = 0
            for line in file:
                if line[0:3] == '###':          # new field
                    line = line[3:].strip()
                    linesplit = line.split(';')
                    fieldname = linesplit[0].strip()
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
                    elif line[0:5] == '#QGIS':
                        self.dbasetables[tablename]['qgisviewsql'] = line[5:].strip()
                    elif line[0:5] == '#SCAL':
                        self.dbasetables[tablename]['scale'] = float(line[5:].strip())
                    elif line[0:5] == '#SHOW':
                        value = line[5:].strip()
                        if value == 'YES':
                            self.dbasetables[tablename]['showinqgis'] = True


                else:                           # field constraint
                    if 'Cst' in self.dbasetables[tablename]['fields'][fieldname].keys():
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'].append([])
                    else:
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'] = [[]]
                    linesplit = line.split(';')
                    self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(linesplit[0].strip())
                    self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(linesplit[1].strip())
                    if len(linesplit) > 2:
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(eval(linesplit[2].strip()))
                    else:
                        self.dbasetables[tablename]['fields'][fieldname]['Cst'][-1].append(None)
                compt += 1


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
        self.dbasetype = dbasetype

        if self.dbasetype == 'spatialite' and file is not None:
            self.spatialitefile = file
            try:    #python 2
                self.connSLITE = db.connect(file)
            except NameError:   #python 3
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

        if type is not None:
            self._createDBDictionary(type)
            # create a list of tables to load
            listoftabletoload = []
            for tablename in self.dbasetables:
                if 'geom' in self.dbasetables[tablename]:
                    listoftabletoload.append((tablename, self.dbasetables[tablename]['geom']))
                else:
                    listoftabletoload.append((tablename, None))

            # load the table as qgsvectorlayer
            for tablename, geom in listoftabletoload:
                if int(str(self.qgisversion_int)[0:3]) < 220:
                    uri = qgis.core.QgsDataSourceURI()
                else:
                    uri = qgis.core.QgsDataSourceUri()
                if self.dbasetype == 'spatialite':
                    uri.setDatabase(file)
                    # raw layer
                    if geom is not None:
                        uri.setDataSource('', str(tablename), 'geom')
                    else:
                        uri.setDataSource('', str(tablename), '')
                    self.dbasetables[tablename]['layer'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'spatialite')
                    # view layer
                    if geom is not None:
                        uri.setDataSource('', str(tablename)+'_qgis', 'geom', '', "id_" + str(tablename).lower())
                    else:
                        uri.setDataSource('', str(tablename) + '_qgis', '', '', "id_" + str(tablename).lower())
                    self.dbasetables[tablename]['layerqgis'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'spatialite')

                elif self.dbasetype == 'postgis':
                    uri.setConnection(self.pghost, str(self.pgport), self.pgdb, self.pguser, self.pgpassword)
                    tablenamelayer = tablename.lower()
                    # raw layer
                    if geom is not None:
                        uri.setDataSource(self.pgschema, str(tablenamelayer), 'geom', '', "id_" + str(tablenamelayer))
                    else:
                        uri.setDataSource(self.pgschema, str(tablenamelayer), None, '', "'id_" + str(tablenamelayer))
                    self.dbasetables[tablename]['layer'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'postgres')
                    # view layer
                    if geom is not None:
                        uri.setDataSource(self.pgschema, str(tablenamelayer) + '_qgis', 'geom', '', "id_" + str(tablenamelayer))
                    else:
                        uri.setDataSource(self.pgschema, str(tablenamelayer) + '_qgis', None, '', "id_" + str(tablenamelayer))
                    self.dbasetables[tablename]['layerqgis'] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'postgres')

                # style and loading
                stylepath = os.path.join(os.path.dirname(__file__), '..',
                                         'DBASE', 'style', self.type, self.dbasetables[tablename]['layer'].name() + '.qml')

                if True:
                    if os.path.isfile(stylepath):
                        self.dbasetables[tablename]['layerqgis'].loadNamedStyle(stylepath)

                    if self.dbasetables[tablename]['showinqgis']:
                        if int(str(self.qgisversion_int)[0:3]) < 220:
                            qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbasetables[tablename]['layerqgis'],
                                                                                 True)
                        else:
                            qgis.core.QgsProject.instance().addMapLayer(self.dbasetables[tablename]['layerqgis'],
                                                                                 True)
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

            self.updateQgsCoordinateTransformFromLayerToCanvas()
            self.dBaseLoaded.emit()


    def query(self, sql):
        if self.dbasetype == 'spatialite':
            # cursor = self.connSLITE.cursor()
            if self.SLITEcursor is None:
                # self.connSLITE = db.connect(self.spatialitefile)
                self.SLITEcursor = self.connSLITE.cursor()
            try:
                query = self.SLITEcursor.execute(sql)
                returnquery = list(query)
                self.commit()
                return returnquery
            except OperationalError as e:
                print('error query', e)
                return None
        elif self.dbasetype == 'postgis':
            if self.PGiscursor is None:
                # connectstr = "dbname='" + self.pgdb + "' user='" + self.pguser + "' host='"
                # connectstr += self.pghost + "' password='" + self.pgpassword + "'"
                # self.connPGis = psycopg2.connect(connectstr)
                self.PGiscursor = self.connPGis.cursor()

            self.PGiscursor.execute(sql)
            if sql.strip()[0:6] == 'SELECT':
                try:
                    rows = self.PGiscursor.fetchall()
                    returnrows = list(rows)
                    self.commit()
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
        print('vacuum')
        if self.dbasetype == 'spatialite':
            sql = "VACUUM " + str(table)
            print(sql)
            self.query(sql)
        elif self.dbasetype == 'postgis':
            old_isolation_level = self.connPGis.isolation_level
            self.connPGis.set_isolation_level(0)
            sql = "VACUUM " + str(table)
            self.query(sql)
            self.connPGis.set_isolation_level(old_isolation_level)


    def commit(self):
        if self.dbasetype == 'spatialite':
            self.connSLITE.commit()
        elif self.dbasetype == 'postgis':
            self.connPGis.commit()

    def getLastRowId(self, table=None):
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

    def _readRecentDBase(self):
        """!
        Read the file where the recents projects are stored and display it in recents files menu
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
        pass
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
        Save recents project in a file
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

    def updateWorkingDate(self):
        if self.dbasetype == 'spatialite':
            subsetstring = '"datecreation" <= ' + "'" + self.workingdate + "'"
            subsetstring += ' AND CASE WHEN "datedestruction" IS NOT NULL  THEN "datedestruction" > ' + "'" + self.workingdate + "'" + ' ELSE 1 END'
        elif self.dbasetype == 'postgis':
            subsetstring = '"datecreation" <= ' + "'" + self.workingdate + "'"
            subsetstring += ' AND CASE WHEN "datedestruction" IS NOT NULL  THEN "datedestruction" > ' + "'" + self.workingdate + "'" + ' ELSE TRUE END'

        for tablename in self.dbasetables:
            fieldnames = [field.name().lower() for field in self.dbasetables[tablename]['layerqgis'].fields()]
            if 'datecreation' in fieldnames:
                self.dbasetables[tablename]['layerqgis'].setSubsetString(subsetstring)
                self.dbasetables[tablename]['layerqgis'].triggerRepaint()

    def reInitDBase(self):
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



    def updateQgsCoordinateTransformFromLayerToCanvas(self):
        if self.qgiscrs is not None:
            if int(str(self.qgisversion_int)[0:3]) < 220:
                self.xform = qgis.core.QgsCoordinateTransform(self.qgiscrs,
                                                              self.canvas.mapSettings().destinationCrs())
            else:
                self.xform = qgis.core.QgsCoordinateTransform(self.qgiscrs,
                                                              self.canvas.mapSettings().destinationCrs(),
                                                              qgis.core.QgsProject.instance() )


    def getConstraintRawValueFromText(self, table, field, txt):
        # print('_getConstraintRawValueFromText',[value[0] for value in self.dbasetable['fields'][field]['Cst']], txt )
        dbasetable = self.dbasetables[table]
        index = [value[0] for value in dbasetable['fields'][field]['Cst']].index(txt)
        return dbasetable['fields'][field]['Cst'][index][1]


    def getConstraintTextFromRawValue(self, table, field, rawvalue):
        # print('_getConstraintTextFromRawValue',self.dbasetablename, self.dbasetable['fields'][field], rawvalue,field)
        dbasetable = self.dbasetables[table]
        try:
            index = [value[1] for value in dbasetable['fields'][field]['Cst']].index(rawvalue)
            return dbasetable['fields'][field]['Cst'][index][0]
        except ValueError:
            self.errorMessage.emit('Probleme de valeur de champ : table : "' + str(table)
                                                                  + '" champ : "' + str(field)
                                                                  + '" valeur :"' + str(rawvalue) + '"')
            return ''


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
        self.featureaddedid = id
