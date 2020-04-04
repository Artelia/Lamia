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
import os, sys
import xlrd

class DBconfigReader():

    def __init__(self, dbaseparser):
        self.dbase = dbaseparser
        self.dbasetables = {}
        self.variantespossibles=[]
        # self.variante = None
        self.baseversion = None
        self.workversion = None



    def createDBDictionary(self, 
                            worktype, 
                            #useprojectdir=False, 
                            baseversiontoread=None, 
                            workversiontoread=None,
                            #chekupdate=True
                            ):
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
        if worktype is None:
            raise ValueError('createDBDictionary : worktype not defined')


        # first readfiles in ./DBASE\create directory and create self.dbasetables
        createfilepath = None
        createbasefilepath = None
        self.dbasetables = {}
        self.worktype = worktype

        baseversionspathlist = self.getWorktypeVersionsList(self.worktype.split('_')[0])
        baseversionnumbers = [elem[0] for elem in baseversionspathlist]
        if len(self.worktype.split('_')) > 0:
            workversionspathlist = self.getWorktypeVersionsList(self.worktype)
            workversionnumbers = [elem[0] for elem in workversionspathlist]
        else:
            workversionspathlist = None
            workversionnumbers = None
        
        #first read base version
        if baseversiontoread is None:
            baseversiontoread, createbasefilepathtoread = baseversionspathlist[-1]
        else:
            createbasefilepathtoread = baseversionspathlist[baseversionnumbers.index(baseversiontoread)][1]

        self.readXlsDbDictionnary(createbasefilepathtoread)
        self.baseversion = baseversiontoread


        #then read work version:
        if workversionspathlist is None:
            return
        if workversiontoread is None:
            workversiontoread, createworkfilepathtoread = workversionspathlist[-1]
        else:
            createworkfilepathtoread = workversions[workversionnumbers.index(workversiontoread)][1]

        self.readXlsDbDictionnary(createworkfilepathtoread)
        self.workversion = workversiontoread

        # finally read project's dbase if exists
        if self.dbase.dbaseressourcesdirectory is not None:
            createfilepath = os.path.join(self.dbase.dbaseressourcesdirectory,'config','dbase',self.worktype + '.xlsx')
            self.readXlsDbDictionnary(createworkfilepathtoread)



    def createDBDictionary_old(self, 
                            worktype, 
                            useprojectdir=False, 
                            baseversiontoread=None, 
                            workversiontoread=None,
                            chekupdate=True
                            ):
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
        if not useprojectdir:
            if baseversiontoread is None:
                self.worktype = worktype
                self.dbasetables = {}

                workversionmax, createfilesdir = self.getWorktypeVersionsList(self.worktype)[-1]
                baseversionmax, createfilesdirbase = self.getWorktypeVersionsList(self.worktype.split('_')[0])[-1]

                if (chekupdate and self.version is not None
                        and (self.version < baseversionmax or self.workversion < workversionmax)) :
                    self.updateDBaseVersion2()



                self.version = baseversionmax
                self.workversion = workversionmax

                if debug: logging.getLogger("Lamia").debug('baseversion : %s, workversion : %s', str(self.version ), str(self.workversion ))

                if createfilesdirbase and createfilesdirbase != createfilesdir :    #cas de la lecture du bd enfant
                    parsertemp = DBaseParser(None)
                    parsertemp.createDBDictionary2(self.worktype.split('_')[0])
                    self.dbasetables = parsertemp.dbasetables
                    del parsertemp
            else:
                self.worktype = worktype
                self.dbasetables = {}

                baseversions = self.getWorktypeVersionsList(self.worktype.split('_')[0])
                workversions = self.getWorktypeVersionsList(self.worktype)
                baseversionnumbers = [elem[0] for elem in baseversions]
                workversionnumbers = [elem[0] for elem in workversions]


                createfilesdirbase = baseversions[baseversionnumbers.index(baseversiontoread)][1]
                createfilesdir = workversions[workversionnumbers.index(workversiontoread)][1]

                if createfilesdirbase != createfilesdir:
                    #createfilesdir = workversions[workversionnumbers.index(workversiontoread)][1]
                    parsertemp = DBaseParser(None)
                    parsertemp.createDBDictionary2(self.worktype.split('_')[0], baseversiontoread=baseversiontoread,workversiontoread=baseversiontoread)
                    self.dbasetables = parsertemp.dbasetables
                    del parsertemp


        else:
            createfilesdir = os.path.join(self.dbaseressourcesdirectory,'config','dbase',self.worktype + '.xlsx')
            if not os.path.exists(createfilesdir):
                return

        if debug: logging.getLogger("Lamia").debug('createfilesdir : %s', str(createfilesdir))

        self.readDbDictionnary(createfilesdir)



    def readXlsDbDictionnary(self, dictfile=None, vartoread=None):
        """

        :param dictfile:
        :param vartoread:
        :return:
        """

        debug = False
        if dictfile is None or not os.path.isfile(dictfile):
            return

        if self.dbasetables is None:
            self.dbasetables = {}

        xlsbook = xlrd.open_workbook(dictfile)

        for sheet in xlsbook.sheets():
            tablename = sheet.name.split('_')
            fieldname = None
            cstcolumntoread = None
            order = None

            if len(tablename) == 1:  # non table file
                continue
            else:
                order = tablename[0]
                tablename = '_'.join(tablename[1:])


            if tablename not in self.dbasetables.keys():
                self.dbasetables[tablename] = {}
                self.dbasetables[tablename]['order'] = int(order)
                self.dbasetables[tablename]['fields'] = {}
                self.dbasetables[tablename]['showinqgis'] = False
                self.dbasetables[tablename]['widget'] = []
                self.dbasetables[tablename]['row_variantes'] = -1

            firstqgsviewoccurrence = True

            for row in range(sheet.nrows):
                firstcol =  sheet.cell_value(row, 0)
                if len(firstcol) > 0 and firstcol[0] == '#':  # comment - pass
                    if firstcol.strip() == '#DJAN':
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
                        if firstqgsviewoccurrence:
                            firstqgsviewoccurrence = False
                            self.dbasetables[tablename]['qgisviewsql'] = ''

                        if 'qgisviewsql' in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]['qgisviewsql'] += ' ' + sheet.cell_value(row, 1).strip() + ' '
                        else:
                            self.dbasetables[tablename]['qgisviewsql'] = sheet.cell_value(row, 1).strip()
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

                else:   #column declaration
                    if firstcol != '':
                        fieldname = sheet.cell_value(row, 0).strip()
                        cstcolumntoread = None
                        if fieldname == 'geom':
                            self.dbasetables[tablename]['geom'] = sheet.cell_value(row, 1).strip()
                            continue

                        self.dbasetables[tablename]['fields'][fieldname] = {}
                        self.dbasetables[tablename]['fields'][fieldname]['PGtype'] = sheet.cell_value(row, 1).strip() # the pg type

                        # the foreign key
                        if sheet.cell_value(row, 2).strip() != '':
                            self.dbasetables[tablename]['fields'][fieldname]['FK'] = sheet.cell_value(row, 2).strip()

                        if sheet.cell_value(row, 4).strip() != '':
                            self.dbasetables[tablename]['fields'][fieldname]['ParFldCst'] = sheet.cell_value(row, 4).strip()

                        cstcolumntoread = self.readConstraints(tablename,fieldname, sheet, row, cstcolumntoread)

                    else:
                        if fieldname is not None and fieldname != 'geom':
                            self.readConstraints(tablename,fieldname,sheet, row,cstcolumntoread)


            if debug and self.dbasetables[tablename]['order'] <= 4:
                print('**************************')
                print(self.dbasetables[tablename])

        if "Revision" in self.dbasetables.keys():
            self.revisionwork = True





    def readConstraints(self, tablename,fieldname  ,sheet, xlrow,cstcolumntoread=None):

        # dbasefield self.dbasetables[tablename]['fields'][fieldname]
        # print('readConstraints',tablename,fieldname  ,sheet, xlrow)
        colindexvariante = cstcolumntoread
        dbasefield = self.dbasetables[tablename]['fields'][fieldname]

        if colindexvariante is None:
            colindexvariante = None
            if self.dbase.variante is None:
                colindexvariante = 5
            else:
                if self.dbasetables[tablename]['row_variantes'] >= 0 :
                    rowvariantes = self.dbasetables[tablename]['row_variantes']
                    if self.dbase.variante =='Lamia':
                        colindexvariante = 5
                    else:
                        for col in range(sheet.ncols):
                            try:
                                if (sheet.cell_value(rowvariantes,col ) == self.dbase.variante
                                        and sheet.cell_value(xlrow,col ) != '' ):
                                    colindexvariante = col
                                    # print('colindexvariante', tablename, fieldname, colindexvariante)
                                    break
                            except:
                                print('error',tablename,fieldname ,self.dbase.variante )
                        #if colindexvariante is None:
                        #    colindexvariante = 5
        if colindexvariante is None:
            colindexvariante = 5

        #if unicode(sheet.cell_value(xlrow, colindexvariante)).strip() != '':
        if sheet.cell_value(xlrow, colindexvariante).strip() != '':
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



    def getWorktypeVersionsList(self, worktype):
        """
        return list of versions for worktype
        """
        debug = False
        results = []

        createfilesdir = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'create')
        if debug: logging.getLogger("Lamia").debug('dbase dir : %s', str(createfilesdir))

        listfiles = os.listdir(createfilesdir)
        for filename in listfiles:
            filepath = os.path.join(createfilesdir,filename )
            filebasename, ext = os.path.splitext(filename)

            if os.path.isfile(filepath) and ext in ['.xls', '.xlsx']:
                filebasenamesplitted = filebasename.split('_')
                if (len(filebasenamesplitted) > 2 and filebasenamesplitted[-2].isdigit() and filebasenamesplitted[-1].isdigit()
                        and worktype == '_'.join(filebasenamesplitted[:-2]) ):     #case child of dabse2
                    versiontemp = '_'.join(filebasename.split('_')[-2:])
                    repository = os.path.join(createfilesdir, filename)
                    results.append([versiontemp, repository])


        if debug: logging.getLogger("Lamia").debug('results: %s', str(results))

        results.sort()

        if debug: logging.getLogger("Lamia").debug('results: %s', str(results))

        return results

