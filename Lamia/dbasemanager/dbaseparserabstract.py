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

import  datetime 
import os, sys, re, logging, shutil
try:
    import PIL
    import PIL.Image
    PILexists = True
except ImportError:
    PILexists = False

from ..libslamia.lamiareg.updatereg import updateWinReg
from .dbconfigreader import DBconfigReader
from .dbaseofflinemanager import DBaseOfflineManager
from ..iface.ifaceabstractconnector import LamiaIFaceAbstractConnectors
from . import dbaseutils



PGTYPE_TO_SLTYPE = {'VARCHAR' : 'TEXT',
                    'INT' : 'INTEGER',
                    'SERIAL PRIMARY KEY' : 'INTEGER PRIMARY KEY AUTOINCREMENT',
                    'TIMESTAMP' : 'TEXT',
                    'TEXT' : 'TEXT',
                    'TIMESTAMP WITH TIME ZONE' : 'TEXT',
                    'REAL': 'REAL',
                    'NUMERIC': 'REAL',
                    'BOOLEAN' : 'INTEGER'}

PROJECTCONFIGDIRS = ['dbase', 'rapporttools', 'styles', 'importtools']


class AbstractDBaseParser():


    def __init__(self, parserfactory=None,messageinstance=None):
        """Read the dbase

        :param parserfactory: the parent class
        :type parserfactory: [type], optional
        :param messageinstance: [description], defaults to None
        :type messageinstance: [type], optional
        :raises ImportError: [description]
        """

        #:the dictionnary of dbase (cf DBconfigReader)
        self.dbasetables = None

        if messageinstance is None:
            self.messageinstance = LamiaIFaceAbstractConnectors()
        else:
            self.messageinstance = messageinstance

        #utils
        self.utils = dbaseutils

        #:dbase type : Base2_digue, Base2_assainissement ....
        self.worktype = None
        #:dbase variante
        self.variante = None
        #: crs of dbase int
        self.crsnumber = None

        #:ressources dir
        self.dbaseressourcesdirectory = None

        #:the parser class (used to create another dbaseparser if needed)
        self.parserfactory = parserfactory

        #:the config reader instance
        self.dbconfigreader = DBconfigReader(self)
        #:the offline manager instance
        self.dbaseofflinemanager = DBaseOfflineManager(self)

        #:for debug purpose
        self.printsql = False

        self.base3version = False   #for transition beetween base2 and base3 model

        # ?? temp variable for export
        self.featureaddedid = None

        self.imagedirectory = None
        #:visual mode used in ui
        self.visualmode = 0

        #  not used yet
        self.searchbuffer = 20
        # used to define the working date in db
        #self.workingdate = QtCore.QDate.currentDate().toString('yyyy-MM-dd')
        #self.workingdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.workingdate = (datetime.datetime.now()+ datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        # self.workingdate = (datetime.datetime.now()).strftime("%Y-%m-%d")

        # the current prestation id
        self.currentprestationid = None

        self.baseversion = None  # dbase version
        self.workversion = None  # dbase version

        self.revisionwork = False
        self.currentrevision = None
        self.maxrevision = 0

        self.forcenocommit=False        #force query to no commit

        self.connectconf = None    #dict of connection data

        #:language setting
        self.locale = None
        try:
            from qgis.PyQt.QtCore import QSettings
            if QSettings().value('locale/userLocale') is None:
                raise ImportError()
            self.locale = QSettings().value('locale/userLocale')[0:2]
        except ImportError:
            import locale
            localelang, encod = locale.getdefaultlocale()
            self.locale = localelang.split('_')[0]





    def __________________________DBase_handing(self):
        pass

    def connectToDBase(self):
        raise NotImplementedError

    def getDBName(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def createDBase(self, 
                    crs=None, 
                    worktype=None, 
                    dbaseressourcesdirectory=None, 
                    variante=None,
                    **kwargs):
        """
        kwargs for postgis :
          host='localhost', 
          port=None, 
          dbname=None, 
          schema=None, 
          user=None,  
          password=None
        kwargs for spatialite :
          slfile = slfile
        """

        self.initDBase(**kwargs)

        self.crsnumber = crs
        self.variante = variante
        self.worktype = worktype

        baseversion = kwargs.get('baseversion', None)
        workversion = kwargs.get('workversion', None)

        self.dbconfigreader.createDBDictionary(worktype=worktype,
                                               baseversiontoread=baseversion,
                                                workversiontoread=workversion)
        finaldbaseressourcesdirectory = self.createRessourcesDir(dbaseressourcesdirectory,**kwargs)

        # sqlfile contains output of dbase creation script
        sqlfile = os.path.join(finaldbaseressourcesdirectory, 'sqlcreation.txt')
        openedsqlfile = open(sqlfile, u'w')

        self.connectToDBase(**kwargs)

        # Tables creation
        for order in range(20):
            for dbname in self.dbconfigreader.dbasetables:
                if self.dbconfigreader.dbasetables[dbname]['order'] == order:
                    sql = self.generateSQLTableCreationFromDBConfig(dbname, self.dbconfigreader.dbasetables[dbname], crs)
                    openedsqlfile.write(sql['main'] + '\n')
                    self.query(sql['main'])
                    self.commit()
                    if 'other' in sql.keys():
                        for sqlother in sql['other']:
                            openedsqlfile.write(sqlother + '\n')
                            # print(sqlother)
                            self.query(sqlother)
                            self.commit()

        # init table configZ
        if dbaseressourcesdirectory is None and 'slfile' in kwargs.keys():
            dbaseressourcesdirectoryrelative = './/DBspatialite'
        else:
            dbaseressourcesdirectoryrelative = finaldbaseressourcesdirectory

        ## Basedonnees table
        versionsql = "'" + str(self.dbconfigreader.baseversion) + "'"
        workversionsql = "'" + str(self.dbconfigreader.workversion) + "'"
        if variante is None:
            variantesql = 'NULL'
        else:
            variantesql = "'" + variante + "'"
        
        if 'Basedonnees' in self.dbconfigreader.dbasetables.keys():
            sql = "INSERT INTO Basedonnees (metier,repertoireressources,crs, version, workversion, variante) "
        else:
            sql = "INSERT INTO database (businessline,resourcesdirectory,crs, baseversion, workversion, variant) "
        sql += "VALUES('" + worktype + "','" + dbaseressourcesdirectoryrelative + "'," + str(crs) + "," + versionsql
        sql += "," + workversionsql +  ',' + variantesql + ")"
        self.query(sql)
        #Revision table
        datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if 'Basedonnees' in self.dbconfigreader.dbasetables.keys():
            sql = "INSERT INTO Revision (datetimerevision, commentaire) "
        else:
            sql = "INSERT INTO revision (datetimerevision, comment) "
        sql += "VALUES('" + datecreation + "','Premiere version ');"
        self.query(sql)
        
    
        # Views creation
        for dbname in self.dbconfigreader.dbasetables.keys():
            dbasetable = self.dbconfigreader.dbasetables[dbname]

            sqls = self.generateSQLViewCreationFromDBConfig(dbname, dbasetable, worktype, crs)
            for sql in sqls:
                openedsqlfile.write(sql + '\n')
                self.query(sql)
 

        openedsqlfile.close()

    def generateSQLTableCreationFromDBConfig(self):
        raise NotImplementedError

    def generateSQLViewCreationFromDBConfig(self):
        raise NotImplementedError

    def loadDBase(self, **kwargs):
        """
        kwargs for postgis :
            host, 
            port, 
            dbname, 
            schema, 
            user, 
            password
        kwargs for spatialite : 
            slfile
        """
        self.connectconf = kwargs
        self.connectToDBase(**kwargs)


        #init variables
        # sql = "SELECT metier, repertoireressources,crs, version, workversion, variante   FROM Basedonnees;"
        if 'database' in self.getTables():
            sql = "SELECT businessline, resourcesdirectory,crs, baseversion, workversion, variant   FROM database"
        else:
            sql = "SELECT metier, repertoireressources,crs, version, workversion, variante   FROM Basedonnees"
        query = self.query(sql)
        worktype, resdir, crs , version, workversion, variante  = [row[0:6] for row in query][0]


        if resdir[0] == '.' and hasattr(self,'spatialitefile'):
            self.dbaseressourcesdirectory = os.path.join(os.path.dirname(self.spatialitefile ), resdir)
        else:
            self.dbaseressourcesdirectory = os.path.normpath(resdir)
        self.crsnumber = crs
        self.baseversion = version
        self.workversion = workversion
        self.variante = variante
        self.worktype = worktype

        self.maxrevision = self.getLastPK('Revision')


        self.dbconfigreader.createDBDictionary(self.worktype)
        self.dbasetables = self.dbconfigreader.dbasetables

        if (self.baseversion < self.dbconfigreader.maxbaseversion 
                or self.workversion < self.dbconfigreader.maxworkversion):
            self.updateDBaseVersion()

        sql = "SELECT MAX(pk_revision) FROM Revision;"
        query = self.query(sql)
        self.currentrevision = query[0][0]

        self.base3version = not ('Basedonnees' in self.dbasetables.keys())
        updateWinReg(worktype=worktype)

    def initDBase(self):
        raise NotImplementedError

    def updateDBaseVersion(self):
        debug = True
        # if (self.baseversion < self.dbconfigreader.maxbaseversion 
        #         or self.workversion < self.dbconfigreader.maxworkversion):

        # indexbaseversion = [ver[0] for ver in baseversions].index(self.version)
        # indexworkversion = [ver[0] for ver in workversions].index(self.workversion)
        if debug: logging.getLogger("Lamia_unittest").debug('currentbaseversion %s - verions : %s', self.baseversion, self.dbconfigreader.baseversionnumbers)
        if debug: logging.getLogger("Lamia_unittest").debug('currentworkversion %s - verions : %s', self.workversion,self.dbconfigreader.workversionnumbers)
        indexbaseversion = self.dbconfigreader.baseversionnumbers.index(self.baseversion)
        indexworkversion = self.dbconfigreader.workversionnumbers.index(self.workversion)

        for indexversion in range(indexbaseversion, len(self.dbconfigreader.baseversionnumbers) -1 ):
            self._updateTables('base',
                              self.dbconfigreader.baseversionnumbers[indexversion],
                              self.dbconfigreader.baseversionnumbers[indexversion +1] )


        for indexversion in range(indexworkversion, len(self.dbconfigreader.workversionnumbers) -1 ):
            self._updateTables('work',
                              self.dbconfigreader.workversionnumbers[indexversion],
                              self.dbconfigreader.workversionnumbers[indexversion + 1])

        if debug: logging.getLogger("Lamia_unittest").debug('currentbaseversion %s - verions : %s', self.baseversion, self.dbconfigreader.baseversionnumbers)
        if debug: logging.getLogger("Lamia_unittest").debug('currentworkversion %s - verions : %s', self.workversion,self.dbconfigreader.workversionnumbers)

    def _updateTables(self, typebase, oldversion, newversion ):

        debug = True
        if debug: logging.getLogger("Lamia_unittest").debug(' %s - old : %s, new : %s', str(typebase), str(oldversion), str(newversion))
        
        baseversions = self.dbconfigreader.baseversionnumbers
        workversions = self.dbconfigreader.workversionnumbers
        
        #get old and new dict
        if typebase == 'base':
            self.dbconfigreader.createDBDictionary(worktype=self.worktype,
                                                    baseversiontoread=oldversion,
                                                    workversiontoread=self.workversion)
            dictold = self.dbconfigreader.basedict
            self.dbconfigreader.createDBDictionary(worktype=self.worktype,
                                                    baseversiontoread=newversion,
                                                    workversiontoread=self.workversion)
            dictnew = self.dbconfigreader.basedict
            indexbaseversionspathlist = self.dbconfigreader.baseversionnumbers.index(newversion)
            pythonupdatefile = self.dbconfigreader.baseversionspathlist[indexbaseversionspathlist][1]
        if typebase == 'work':
            self.dbconfigreader.createDBDictionary(worktype=self.worktype,
                                                    baseversiontoread=self.baseversion,
                                                    workversiontoread=oldversion)
            dictold = self.dbconfigreader.workdict
            self.dbconfigreader.createDBDictionary(worktype=self.worktype,
                                                    baseversiontoread=self.baseversion,
                                                    workversiontoread=newversion)
            dictnew = self.dbconfigreader.workdict
            indexworkversionspathlist = self.dbconfigreader.workversionnumbers.index(newversion)
            pythonupdatefile = self.dbconfigreader.workversionspathlist[indexworkversionspathlist][1]
        #* get diffs saved in results
        results = []
        for table in dictnew.keys():
            if table not in dictold.keys():
                results.append([table, None])
            else:
                for field in dictnew[table]['fields']:
                    if field not in dictold[table]['fields'].keys():
                        results.append([table, field])

        if debug: logging.getLogger("Lamia_unittest").debug('diffs : %s', results)

        #* update dbase
        for table, field in results:
            if table is not None and field is None:
                #table creation
                sql = self.generateSQLTableCreationFromDBConfig(table, dictnew[table], self.crsnumber)
                #openedsqlfile.write(sql['main'] + '\n')
                self.query(sql['main'])
                self.commit()
                if 'other' in sql.keys():
                    for sqlother in sql['other']:
                        #openedsqlfile.write(sqlother + '\n')
                        # print(sqlother)
                        self.query(sqlother)
                        self.commit()
                #view creation
                sqls = self.generateSQLViewCreationFromDBConfig(table, dictnew[table], self.worktype, self.crsnumber)
                
                for sql in sqls:
                    #openedsqlfile.write(sql + '\n')
                    self.query(sql)


            else:
                sql = 'ALTER TABLE ' + table + ' ADD COLUMN ' + field + ' '

                if self.__class__.__name__ == 'SpatialiteDBaseParser':
                    if 'VARCHAR' in dictnew[table]['fields'][field]['PGtype']:
                        sql += ' TEXT '
                    else:
                        sql += PGTYPE_TO_SLTYPE[dictnew[table]['fields'][field]['PGtype']]
                elif self.__class__.__name__ == 'PostGisDBaseParser':
                    sql += dictnew[table]['fields'][field]['PGtype']
                self.query(sql)

        #* read potential python file
        pythonfile, ext = os.path.splitext(pythonupdatefile)
        pythonfile = pythonfile + '.txt'

        if os.path.isfile(pythonfile):
            pyfile = open(pythonfile,'r')
            text = pyfile.read()
            pyfile.close()
            exec (text)


        #* update version
        self.dbasetables = dictnew
        if typebase == 'base':
            self.baseversion = newversion
            self.workversion = self.workversion
        elif typebase == 'work':
            self.baseversion = self.baseversion
            self.workversion = newversion

        # sql = "UPDATE Basedonnees SET version = '" + str(self.version) + "'"
        if 'database' in self.getTables():
            sql = "UPDATE database SET baseversion = '" + str(self.baseversion) + "'"
        else:
            sql = "UPDATE Basedonnees SET version = '" + str(self.baseversion) + "'"
        if self.workversion is not None:
            sql += ",workversion = '" + str(self.workversion) + "'"

        self.query(sql)


    def createRessourcesDir(self, dbaseressourcesdirectory, **kwargs):

      slfile=kwargs.get('slfile', None)

      if dbaseressourcesdirectory is None and slfile:
          dbaseressourcesdirectorytemp = os.path.join(os.path.dirname(slfile), u'DBspatialite')
      else:
          dbaseressourcesdirectorytemp = dbaseressourcesdirectory

      if not os.path.isdir(dbaseressourcesdirectorytemp):
          os.makedirs(dbaseressourcesdirectorytemp)
      configdir = os.path.join(dbaseressourcesdirectorytemp, 'config')
      if not os.path.isdir(configdir):
          os.makedirs(configdir)

      for tooldir in PROJECTCONFIGDIRS:
          dbasedir = os.path.join(configdir, tooldir)
          if not os.path.isdir(dbasedir):
              os.makedirs(dbasedir)

      return dbaseressourcesdirectorytemp

    def __________________________DBase_querying(self):
        pass

    def query(self):
        raise NotImplementedError 

    def vacuum(self):
        raise NotImplementedError 

    def commit(self):
        raise NotImplementedError 

    def beginTransaction(self):
        sql = "BEGIN"
        self.query(sql)
        self.forcenocommit = True

    def commitTransaction(self):
        sql = "COMMIT"
        self.query(sql)
        self.forcenocommit = False


    def reInitDBase(self):
        raise NotImplementedError 

    def isTableSpatial(self):
        raise NotImplementedError 

    def getColumns(self, tablename):
        raise NotImplementedError 

    def getFirstIdColumn(self,tablename):
        raise NotImplementedError 

    def getLastPK(self, tablename):
        """
        Renvoi la version max de la table Revision
        :return: la version max de la table Revision
        """
        raise NotImplementedError 

    def getmaxColumnValue(self, tablename, field):
        sql = "SELECT MAX(" + field + ") FROM " + str(tablename)
        query = self.query(sql, docommit=False)
        result = [row[0] for row in query]
        if len(result)>0 and result[0] is not  None:
            return result[0]
        else:       
            return 0

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
        except ValueError  as e:
            if False and self.qgsiface is None:
                logging.getLogger("Lamia").debug('error %s %s %s %s',e, table,field , str([value[0] for value in dbasetable['fields'][field]['Cst']] ))
            return None
        except KeyError as e:
            if False and self.qgsiface is None:
                logging.getLogger("Lamia").debug('error %s %s %s %s',e, table,field , 'No contraint')
            return txt

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
            if not dbaseutils.isAttributeNull(rawvalue):
                if isinstance(rawvalue, int) or isinstance(rawvalue, long):
                    rawvalue = str(rawvalue)
                try:
                    index = [value[1] for value in dbasetable['fields'][field]['Cst']].index(rawvalue)
                    return dbasetable['fields'][field]['Cst'][index][0]
                except ValueError as e:
                    logging.getLogger("Lamia_unittest").debug('error : %s %s %s %s', table, field, e, str([value[1] for value in dbasetable['fields'][field]['Cst']]))
                    return str(rawvalue)

            else:
                return ''
        else:
            if not dbaseutils.isAttributeNull(rawvalue):
                # print(table, field, rawvalue, type(rawvalue))
                return rawvalue
            else:
                return ''

    def getValuesFromPk(self, dbasename, fields, pk):
        # if isinstance(fields, str) or isinstance(fields, unicode):
        if isinstance(fields, str):
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
    
    def getWktGeomFromPk(self, dbasename, pk):
        return self.getValuesFromPk(dbasename, 'ST_AsText(geom)', pk)

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
                if ((isinstance(res, str)  or isinstance(res, bytes))  and listoffields[l] != 'geom' 
                        and 'datetime' not in listoffields[l]) :
                    restemp.append("'" + str(res).replace("'", "''") + "'")
                elif 'datetime' in listoffields[l] and  res is not None and res != 'None':
                        restemp.append("'" + str(res) + "'")
                elif listoffields[l] == 'geom' and res is not None:
                    restemp.append("ST_GeomFromText('" + res + "', " + str(self.crsnumber) + ")")
                elif res is None or res == ''  :
                    restemp.append('NULL')
                elif (isinstance(res, str)  or isinstance(res, bytes)) and 'None' in res:
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

    def sqlNow(self, sqlin, date=None):
        sqlout = self.updateQueryTableNow(sqlin, date)
        return sqlout

    def updateQueryTableNow(self, sqlin, date=None):
        
        sqllist = re.split(' |,|\(|\)|\.|=', sqlin)
        withsql = ''
        alreadytables=[]
        for sqlword in sqllist:
            if '_now' in sqlword:
                tablename=sqlword.split('_now')[0]
                if 'lpk_revision_begin' in self.getColumns(tablename + '_qgis'):
                    if tablename.lower() not in  alreadytables:
                        alreadytables.append(tablename.lower())
                        withsql +=  sqlword + " AS "
                        withsql += " (SELECT * FROM " + tablename + "_qgis WHERE "
                        withsql += self._dateVersionConstraintSQL(date)
                        withsql += "), "
                else:
                    if tablename.lower() not in  alreadytables:
                        alreadytables.append(tablename.lower())
                        withsql +=  sqlword + " AS "
                        withsql += " (SELECT * FROM " + tablename + "), "

        withsql = withsql[0:-2]
        sqltemp1 = self.utils.splitSQLSelectFromWhereOrderby(sqlin)
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

    def _dateVersionConstraintSQL(self, specialdate=None):
        raise NotImplementedError

    def __________________________Feature_creation_saving(self):
        pass

    def createNewObjet(self, docommit=True):
        datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #lastobjetid = self.getLastId('Objet') + 1
        if self.base3version:
            lastobjetid = self.getmaxColumnValue('object', 'id_object')
            sql = "INSERT INTO object (id_object, lpk_revision_begin, datetimecreation, datetimemodification ) "
            sql += "VALUES(" + str(lastobjetid + 1) + "," + str(self.maxrevision) + ",'" + datecreation + "','" + datecreation + "' )"
            self.query(sql, docommit=docommit)
            pkobjet = self.getLastPK('object') 
        else:
            lastobjetid = self.getmaxColumnValue('Objet', 'id_objet')
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation, datetimemodification ) "
            sql += "VALUES(" + str(lastobjetid + 1) + "," + str(self.maxrevision) + ",'" + datecreation + "','" + datecreation + "' )"
            self.query(sql, docommit=docommit)
            pkobjet = self.getLastPK('Objet') 
        return pkobjet
        
    def createNewFeature(self, tablename):
        parenttables = [tablename] + self.getParentTable(tablename)
        parenttablename = None
        for itertablename in parenttables[::-1]:
            if itertablename in ['Objet','object']:
                parenttablepk = self.createNewObjet()
                parenttablename = itertablename
            else:
                tablepk = self.getLastPK(itertablename) + 1

                if parenttablename is not None :
                    #if not 'onlyoneparenttable' in self.dbasetables[itertablename].keys():
                    if  not itertablename[-4:] == 'data':
                        maxid = self.getmaxColumnValue(itertablename, 'id_' + itertablename.lower()) + 1
                        listofields = ['id_' + itertablename.lower(), 'lpk_' + parenttablename.lower()]
                        listofrawvalues = [maxid, parenttablepk]
                    else:
                        listofields = ['lpk_' + parenttablename.lower()]
                        listofrawvalues = [parenttablepk]
                    sql = self.createSetValueSentence(type='INSERT',
                                                tablename=itertablename,
                                                listoffields=listofields,
                                                listofrawvalues=listofrawvalues)
                    self.query(sql)
                parenttablename = itertablename
                parenttablepk = self.getLastPK(itertablename)
            
        return self.getLastPK(tablename)

    def manageFeatureCreationOrUpdate(self, tablename, featurepk=None):
        """
        Called by saveFeature - Manage versioning
        return pk of object
        """

        if featurepk is not None :  #existing feature saved
            if 'lpk_revision_begin' in self.getColumns(tablename + '_qgis'):
                featlastrevision = self.getValuesFromPk(tablename + '_qgis',
                                                        'lpk_revision_begin',
                                                            featurepk)

                if featlastrevision != self.maxrevision:   #new version feature
                    print('*********** new feat vers')
                    self.createNewFeatureVersion(tablename,
                                                featurepk)
                    pktoreturn= self.getLastPK(tablename)
                else:       #simple feature update
                    pktoreturn = featurepk
            else:
                pktoreturn = featurepk

        else:           # feature creation
            pktoreturn = self.createNewFeature(tablename)

        return pktoreturn

    def createNewFeatureVersion(self,dbname, rawpk):

        #first be sure
        if self.base3version:
            pkobjet, revbegin = self.getValuesFromPk(dbname + "_qgis", ['pk_object','lpk_revision_begin'], rawpk)
        else:
            pkobjet, revbegin = self.getValuesFromPk(dbname + "_qgis", ['pk_objet','lpk_revision_begin'], rawpk)
        if revbegin < self.maxrevision:
            #first close object
            if self.base3version:
                sql = self.createSetValueSentence('UPDATE',
                                                'object',
                                                ['lpk_revision_end'],
                                                [self.maxrevision])
                sql += " WHERE pk_objet = " + str(pkobjet)
                self.query(sql)
            else:
                sql = self.createSetValueSentence('UPDATE',
                                                'Objet',
                                                ['lpk_revision_end'],
                                                [self.maxrevision])
                sql += " WHERE pk_object = " + str(pkobjet)
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
                lastpk.append(self.getLastPK(tablename))
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

    def saveRessourceFile(self,dbname, 
                                featurepk=None, 
                                previousfeaturepk=None   #case new version - its the old pk
                                ):
        """
        Called by saveFeature
        If ressource file is not in the dbase directory, save it in the dbase directory

        """
        # get date
        """
        sql = "SELECT datetimecreation FROM " + self.dbasetablename.lower() + "_qgis"
        sql += " WHERE pk_"+ self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
        query = self.dbase.query(sql)
        result = [row[0] for row in query]
        """
        if self.base3version:
            if not 'resource' in self.getParentTable(dbname):
                return
        else:
            if not 'Ressource' in self.getParentTable(dbname):
                return
            
        DBASETABLENAMElower = dbname.lower()
        result = self.getValuesFromPk(DBASETABLENAMElower + "_qgis",
                                                            'datetimecreation',
                                                            featurepk)

        if result is not None:
            datevalue = datetime.datetime.strptime(str(result), "%Y-%m-%d %H:%M:%S").date()
            if isinstance(datevalue, datetime.date):
                datevalue = datevalue.strftime('%Y-%m-%d')
        else:
            return

        date = ''.join(datevalue.split('-'))
        if self.base3version:
            fieldrequested = ['pk_resource', 'id_resource', 'file']
        else:
            fieldrequested = ['pk_ressource', 'id_ressource', 'file']

        result = self.getValuesFromPk(DBASETABLENAMElower + "_qgis",
                                                            fieldrequested,
                                                            featurepk)
        if len(result) > 0:
            pkressource, idressource, file = result
        else:
            return

        dbaseressourcesdirectory = self.dbaseressourcesdirectory
        if file is not None and len(file) > 0:
            if file[0] == '.':
                file = os.path.join(dbaseressourcesdirectory,file)
            else:
                if os.path.isfile(file):
                    filename = os.path.basename(file)
                    filename = str(idressource) + '_' + filename
                    destinationdir = os.path.join(dbaseressourcesdirectory,dbname,date)
                    destinationfile = os.path.join(destinationdir, filename)

                    self.copyRessourceFile(fromfile= file,
                                            tofile=destinationfile,
                                            withthumbnail=0,
                                            copywholedirforraster=False)


                    finalname = os.path.join('.',os.path.relpath(destinationfile, dbaseressourcesdirectory ))
                    if self.base3version:
                        sql = "UPDATE resource SET file = '" + finalname + "' WHERE pk_resource = " +  str(pkressource) + ";"
                        query = self.query(sql)

                        if previousfeaturepk is not None:   #case updating existing feature
                            sql = "SELECT file FROM resource  WHERE pk_resource = " + str(pkressource) + ";"
                            query = self.query(sql)
                            result = [row[0] for row in query]
                            oldfile = result[0]
                        else:
                            oldfile = ''
                    else:
                        sql = "UPDATE Ressource SET file = '" + finalname + "' WHERE pk_ressource = " +  str(pkressource) + ";"
                        query = self.query(sql)

                        if previousfeaturepk is not None:   #case updating existing feature
                            sql = "SELECT file FROM Ressource  WHERE pk_ressource = " + str(pkressource) + ";"
                            query = self.query(sql)
                            result = [row[0] for row in query]
                            oldfile = result[0]
                        else:
                            oldfile = ''

                    newfile = finalname

                    if os.path.isfile(self.completePathOfFile(oldfile)) and oldfile != newfile:
                        os.remove(self.completePathOfFile(oldfile))
                    else:
                        pass

    def completePathOfFile(self,filetoprocess):
        """
        Génère le path complet du filetoprocess demandé. Utile quand on a un chemin relatif
        :param filetoprocess: le chemin rentré (relatif ou absolu)
        :return: le chemin absolu
        """
        completefile = ''
        #if int(str(self.qgisversion_int)[0:3]) < 220 and isinstance(filetoprocess, QtCore.QPyNullVariant):
        #    filetoprocess = None
        if filetoprocess is None:
            return completefile
        if len(filetoprocess)>0:
            if filetoprocess[0] == '.':
                completefile = os.path.join(self.dbaseressourcesdirectory, filetoprocess)
            else:
                completefile = filetoprocess
            completefile = os.path.normpath(completefile)
        return completefile

    def getParentTable(self, tablename):
        """
        Get Parents table name
        :param tablename:
        :return:
        """
        parenttablenamelist = []
        dbasetable = self.dbasetables[tablename]
        continuesearchparent = True

        #if 'onlyoneparenttable' in dbasetable.keys() and dbasetable['onlyoneparenttable'] :
        #    onlyoneiteration = True

        while continuesearchparent:
            for field in dbasetable['fields'].keys():
                continuesearchparent = False
                if 'lpk_' == field[:4]:
                    if 'Basedonnees' in self.dbasetables.keys():
                        parenttablename = field.split('_')[1].title()
                    else:
                        parenttablename = field.split('_')[1]
                    parenttablenamelist.append(parenttablename)
                    if tablename[-4:] == 'data':
                        continuesearchparent = False
                    elif field[4:] in ['objet','object'] :
                        continuesearchparent = False
                    else:
                        continuesearchparent = True
                    dbasetable = self.dbasetables[parenttablename]
                    break
                    

        return parenttablenamelist

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


