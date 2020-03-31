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

from datetime import datetime
import os, sys

from .dbconfigreader import DBconfigReader
from .dbaseofflinemanager import DBaseOfflineManager

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


    def __init__(self, parserfactory=None):

        """
        Init func
        """
        # the dictionnary of dbase (cf DBconfigReader)
        self.dbasetables = None

        # dbase type : Base2_digue, Base2_assainissement ....
        self.worktype = None
        self.variante = None
        # crs of dbase
        self.crsnumber = None
        self.qgiscrs = None

        #  ressources dir
        self.dbaseressourcesdirectory = None

        # the parser class (used to create another dbaseparser if needed)
        self.parserfactory = parserfactory

        # tools
        self.dbconfigreader = DBconfigReader(self)
        self.dbaseofflinemanager = DBaseOfflineManager(self)

        #for debug purpose
        self.printsql = False

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
        self.workingdate = datetime.now().strftime("%Y-%m-%d")


        # the current prestation id
        self.currentprestationid = None

        self.version = None  # dbase version
        self.workversion = None  # dbase version

        self.revisionwork = False
        self.currentrevision = None
        self.maxrevision = 0

        self.forcenocommit=False
        self.xlsreader = True

        if False:
          try:
              self.qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
          except AttributeError:  # qgis 3
              self.qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT

          self.qgsiface = qgis.utils.iface

    def connectToDBase(self):
        raise NotImplementedError

    def getBDName(self):
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

        self.dbconfigreader.createDBDictionary(worktype)
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
        sql = "INSERT INTO Basedonnees (metier,repertoireressources,crs, version, workversion, variante) "
        sql += "VALUES('" + worktype + "','" + dbaseressourcesdirectoryrelative + "'," + str(crs) + "," + versionsql
        sql += "," + workversionsql +  ',' + variantesql + ")"
        self.query(sql)
        #Revision table
        datecreation = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sql = "INSERT INTO Revision (datetimerevision, commentaire) "
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

        self.connectToDBase(**kwargs)

        #init variables
        sql = "SELECT metier, repertoireressources,crs, version, workversion, variante   FROM Basedonnees;"
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

        sql = "SELECT MAX(pk_revision) FROM Revision;"
        query = self.query(sql)
        self.currentrevision = query[0][0]

    def initDBase(self):
        raise NotImplementedError

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

    def query(self):
        raise NotImplementedError 

    def vacuum(self):
        raise NotImplementedError 

    def commit(self):
        raise NotImplementedError 

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

    def getValuesFromPk(self, dbasename, fields, pk):
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

    def createNewObjet(self, docommit=True):
        datecreation = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #lastobjetid = self.getLastId('Objet') + 1
        lastobjetid = self.getmaxColumnValue('Objet', 'id_objet')
        sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation, datetimemodification ) "
        sql += "VALUES(" + str(lastobjetid) + "," + str(self.maxrevision) + ",'" + datecreation + "','" + datecreation + "' )"
        self.query(sql, docommit=docommit)
        # pkobjet = self.getLastRowId('Objet')
        pkobjet = self.getLastPK('Objet') 
        return pkobjet
        
    def createNewFeature(self, tablename):
        parenttables = [tablename] + self.getParentTable(tablename)
        for itertablename in parenttables[::-1]:
            if itertablename == 'Objet':
                parenttablepk = self.createNewObjet()
                parenttablename = itertablename
            else:
                tablepk = self.getLastPK(itertablename) + 1
                """
                sql = "INSERT INTO Ressource (id_ressource, lpk_objet) "
                sql += "VALUES(" + str(lastressourceid) +   "," + str(pkobjet) + ");"

                createSetValueSentence(self,type='INSERT',tablename=None, listoffields=[], listofrawvalues=[]):
                """
                maxid = self.getmaxColumnValue(itertablename, 'id_' + itertablename.lower()) + 1
                listofields = ['id_' + itertablename.lower(), 'lpk_' + parenttablename.lower()]
                listofrawvalues = [maxid, parenttablepk]
                sql = self.createSetValueSentence(type='INSERT',
                                            tablename=itertablename,
                                             listoffields=listofields,
                                             listofrawvalues=listofrawvalues)
                self.query(sql)
                parenttablename = itertablename
                parenttablepk = self.getLastPK(itertablename)
            
        return self.getLastPK(tablename)


    def createNewFeatureVersion(self,dbname, rawpk):

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






    def setLoadingProgressBar(self, progressbar, val):
        pass
