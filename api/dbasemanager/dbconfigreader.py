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


* Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
* 
* SPDX-License-Identifier: GPL-3.0-or-later
* License-Filename: LICENSING.md
"""


import os, sys, locale, shutil
import xlrd
import Lamia.config
import Lamia.api.libs.odf
from Lamia.api.libs.odsreader.ODSReader import ODSReader


class DBconfigReader:
    def __init__(self, dbaseparser):
        self.dbase = dbaseparser
        self.dbasetables = {}
        self.variantespossibles = []
        # self.variante = None
        self.baseversion = None
        self.workversion = None

        self.maxbaseversion = None
        self.maxworkversion = None

        self.basedict = None  # dict with only base reading
        self.workdict = None  # dict with work reading

    def createDBDictionary(
        self,
        worktype,
        # useprojectdir=False,
        baseversiontoread=None,
        workversiontoread=None,
        # chekupdate=True
    ):
        """
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
                          'qgisviewsql' : sql statement for initial qgis    view creation
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
        self.dbase.messageinstance.showNormalMessage("Creating DBase dictionnary ...")
        if debug:
            logging.getLogger("Lamia").debug("started")
        if worktype is None:
            raise ValueError("createDBDictionary : worktype not defined")

        # first readfiles in ./DBASE\create directory and create self.dbasetables
        createfilepath = None
        createbasefilepath = None
        self.variantespossibles = []
        self.dbasetables = {}
        self.worktype = worktype
        isbase3 = worktype.split("_")[0] == "base3"

        self.baseversionspathlist = self.getWorktypeVersionsList(
            self.worktype.split("_")[0]
        )
        self.baseversionnumbers = [elem[0] for elem in self.baseversionspathlist]
        self.maxbaseversion = self.baseversionnumbers[-1]
        if len(self.worktype.split("_")) > 0:
            self.workversionspathlist = self.getWorktypeVersionsList(self.worktype)
            self.workversionnumbers = [elem[0] for elem in self.workversionspathlist]
            self.maxworkversion = self.workversionnumbers[-1]
        else:
            self.workversionspathlist = None
            self.workversionnumbers = None

        # first read base version
        if baseversiontoread is None:
            baseversiontoread, createbasefilepathtoread = self.baseversionspathlist[-1]
        else:
            createbasefilepathtoread = self.baseversionspathlist[
                self.baseversionnumbers.index(baseversiontoread)
            ][1]

        # self.basedict = self.readXlsDbDictionnary(createbasefilepathtoread)
        if isbase3:
            self.basedict = self.readOdsDictionnaryBase3(createbasefilepathtoread)
        else:
            self.basedict = self.readOdsDictionnary(createbasefilepathtoread)
        self.baseversion = baseversiontoread
        # then read work version:
        if self.workversionspathlist is None:
            return
        if workversiontoread is None:
            workversiontoread, createworkfilepathtoread = self.workversionspathlist[-1]
        else:
            createworkfilepathtoread = self.workversionspathlist[
                self.workversionnumbers.index(workversiontoread)
            ][1]

        # self.workdict = self.readXlsDbDictionnary(createworkfilepathtoread)
        if isbase3:
            self.workdict = self.readOdsDictionnaryBase3(createworkfilepathtoread)
        else:
            self.workdict = self.readOdsDictionnary(createworkfilepathtoread)

        self.workversion = workversiontoread

        # finally read project's dbase if exists
        if self.dbase.dbaseressourcesdirectory is not None:
            createfilepath = os.path.join(
                self.dbase.dbaseressourcesdirectory,
                "config",
                "dbase",
                self.worktype + ".ods",
            )
            # self.readXlsDbDictionnary(createworkfilepathtoread)
            if isbase3:
                self.readOdsDictionnaryBase3(createfilepath)
            else:
                self.readOdsDictionnary(createfilepath)

    def readOdsDictionnary(self, dictfile=None, vartoread=None):
        debug = False

        if dictfile is None or not os.path.isfile(dictfile):
            return

        if self.dbasetables is None:
            self.dbasetables = {}
        odsdoc = ODSReader(dictfile, clonespannedcolumns=False)

        for sheetname in odsdoc.SHEETS.keys():
            tablename = sheetname.split("_")
            fieldname = None
            cstcolumntoread = None
            order = None

            if len(tablename) == 1:  # non table file
                continue
            else:
                order = tablename[0]
                tablename = "_".join(tablename[1:])

            if tablename not in self.dbasetables.keys():
                self.dbasetables[tablename] = {}
                self.dbasetables[tablename]["order"] = int(order)
                self.dbasetables[tablename]["fields"] = {}
                self.dbasetables[tablename]["showinqgis"] = False
                self.dbasetables[tablename]["widget"] = []
                self.dbasetables[tablename]["row_variantes"] = -1

            firstqgsviewoccurrence = True
            sheetdatas = odsdoc.SHEETS[sheetname]
            # uniforming row lengh
            maxlen = 0
            for row in sheetdatas:
                if len(row) > maxlen:
                    maxlen = len(row)
            for i, row in enumerate(sheetdatas):
                sheetdatas[i] = row + [""] * (maxlen - len(row))

            for row, rowcontent in enumerate(sheetdatas):
                firstcol = sheetdatas[row][0]
                if (
                    firstcol is not None and len(firstcol) > 0 and firstcol[0] == "#"
                ):  # comment - pass
                    if firstcol.strip() == "#DJAN":
                        self.dbasetables[tablename]["djangoviewsql"] = sheetdatas[row][
                            1
                        ].strip()
                    elif firstcol.strip() == "#QGISSL":
                        if "qgisSLviewsql" in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]["qgisSLviewsql"] += (
                                " " + sheetdatas[row][1].strip() + " "
                            )
                        else:
                            self.dbasetables[tablename]["qgisSLviewsql"] = sheetdatas[
                                row
                            ][1].strip()
                    elif firstcol.strip() == "#QGISPG":
                        if "qgisPGviewsql" in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]["qgisPGviewsql"] += (
                                " " + sheetdatas[row][1].strip() + " "
                            )
                        else:
                            self.dbasetables[tablename]["qgisPGviewsql"] = sheetdatas[
                                row
                            ][1].strip()
                    elif firstcol.strip() == "#QGIS":
                        if firstqgsviewoccurrence:
                            firstqgsviewoccurrence = False
                            self.dbasetables[tablename]["qgisviewsql"] = ""

                        if "qgisviewsql" in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]["qgisviewsql"] += (
                                " " + sheetdatas[row][1].strip() + " "
                            )
                        else:
                            self.dbasetables[tablename]["qgisviewsql"] = sheetdatas[
                                row
                            ][1].strip()
                    elif firstcol.strip() == "#EXPO":
                        self.dbasetables[tablename]["exportviewsql"] = sheetdatas[row][
                            1
                        ].strip()
                    elif firstcol.strip() == "#SCAL":
                        self.dbasetables[tablename]["scale"] = float(
                            sheetdatas[row][1].strip()
                        )
                    elif firstcol.strip() == "#SHOW":
                        value = sheetdatas[row][1].strip().strip()
                        if value == "YES":
                            self.dbasetables[tablename]["showinqgis"] = True
                    elif firstcol.strip() == "#SPATIALINDEX":
                        value = sheetdatas[row][1].strip()
                        if value == "YES":
                            self.dbasetables[tablename]["spatialindex"] = True
                    # elif firstcol.strip() == '#ONLYONEPARENTTABLE':
                    #     value = sheetdatas[row][ 1].strip()
                    #     if value == 'YES':
                    #         self.dbasetables[tablename]['onlyoneparenttable'] = True
                    elif firstcol.strip() == "#VARIANTES":
                        # for colnbr in range(1,sheet.ncols):
                        for colnbr in range(1, len(rowcontent)):
                            value = sheetdatas[row][colnbr]
                            if value is None:
                                continue
                            if value.strip() != "":
                                self.dbasetables[tablename]["row_variantes"] = row
                                if value not in self.variantespossibles:
                                    self.variantespossibles.append(
                                        sheetdatas[row][colnbr].strip()
                                    )
                    else:
                        continue

                else:  # column declaration
                    # if firstcol != '':
                    if firstcol not in [None, ""]:
                        fieldname = sheetdatas[row][0].strip()
                        cstcolumntoread = None
                        if fieldname == "geom":
                            self.dbasetables[tablename]["geom"] = sheetdatas[row][
                                1
                            ].strip()
                            continue

                        self.dbasetables[tablename]["fields"][fieldname] = {}
                        self.dbasetables[tablename]["fields"][fieldname][
                            "PGtype"
                        ] = sheetdatas[row][
                            1
                        ].strip()  # the pg type

                        # the foreign key
                        if sheetdatas[row][2] not in [None, ""]:
                            self.dbasetables[tablename]["fields"][fieldname][
                                "FK"
                            ] = sheetdatas[row][2].strip()

                        if sheetdatas[row][4] not in [None, ""]:
                            self.dbasetables[tablename]["fields"][fieldname][
                                "ParFldCst"
                            ] = sheetdatas[row][4].strip()

                        cstcolumntoread = self.readOdsConstraints(
                            tablename, fieldname, sheetdatas, row, cstcolumntoread
                        )

                    else:
                        if fieldname is not None and fieldname != "geom":
                            self.readOdsConstraints(
                                tablename, fieldname, sheetdatas, row, cstcolumntoread
                            )

            if debug and self.dbasetables[tablename]["order"] <= 4:
                print("**************************")
                print(self.dbasetables[tablename])

        if "Revision" in self.dbasetables.keys():
            self.revisionwork = True

        return dict(self.dbasetables)

    def readOdsDictionnaryBase3(self, dictfile=None, vartoread=None):
        """[summary]

        :param dictfile: [description], defaults to None
        :type dictfile: [type], optional
        :param vartoread: [description], defaults to None
        :type vartoread: [type], optional
        :return: [description]
        :rtype: [type]


        cstcolumntoread : column of the proper variante to read, where raw data are written
        colindexlocalvalue: column of the proper variante to read, where displayed data are written - locale dependant
        colindexdescription : col of description of field -  - locale dependant

        """
        debug = False

        if dictfile is None or not os.path.isfile(dictfile):
            return

        if self.dbasetables is None:
            self.dbasetables = {}
        odsdoc = ODSReader(dictfile, clonespannedcolumns=False)

        for sheetname in odsdoc.SHEETS.keys():
            tablename = sheetname.split("_")
            fieldname = None
            cstcolumntoread = None
            colindexlocalvalue = None
            order = None
            colidxdescription, colidxvariante, colidxdisplayedvalue = None, None, None

            if len(tablename) == 1:  # non table file
                continue
            else:
                order = tablename[0]
                tablename = "_".join(tablename[1:])

            if not order.isdigit():
                continue

            if tablename not in self.dbasetables.keys():
                self.dbasetables[tablename] = {}
                self.dbasetables[tablename]["order"] = int(order)
                self.dbasetables[tablename]["fields"] = {}
                self.dbasetables[tablename]["showinqgis"] = False
                self.dbasetables[tablename]["widget"] = []
                self.dbasetables[tablename]["row_variantes"] = -1
                self.dbasetables[tablename]["row_locale"] = -1

            firstqgsviewoccurrence = True
            sheetdatas = odsdoc.SHEETS[sheetname]
            # uniforming row lengh
            maxlen = 0
            for row in sheetdatas:
                if len(row) > maxlen:
                    maxlen = len(row)
            for i, row in enumerate(sheetdatas):
                sheetdatas[i] = row + [""] * (maxlen - len(row))

            for row, rowcontent in enumerate(sheetdatas):
                firstcol = sheetdatas[row][0]
                if (
                    firstcol is not None and len(firstcol) > 0 and firstcol[0] == "#"
                ):  # comment - pass
                    if firstcol.strip() == "#DJAN":
                        self.dbasetables[tablename]["djangoviewsql"] = sheetdatas[row][
                            1
                        ].strip()
                    elif firstcol.strip() == "#QGISSL":
                        if "qgisSLviewsql" in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]["qgisSLviewsql"] += (
                                " " + sheetdatas[row][1].strip() + " "
                            )
                        else:
                            self.dbasetables[tablename]["qgisSLviewsql"] = sheetdatas[
                                row
                            ][1].strip()
                    elif firstcol.strip() == "#QGISPG":
                        if "qgisPGviewsql" in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]["qgisPGviewsql"] += (
                                " " + sheetdatas[row][1].strip() + " "
                            )
                        else:
                            self.dbasetables[tablename]["qgisPGviewsql"] = sheetdatas[
                                row
                            ][1].strip()
                    elif firstcol.strip() == "#QGIS":
                        if firstqgsviewoccurrence:
                            firstqgsviewoccurrence = False
                            self.dbasetables[tablename]["qgisviewsql"] = ""

                        if "qgisviewsql" in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]["qgisviewsql"] += (
                                " " + sheetdatas[row][1].strip() + " "
                            )
                        else:
                            self.dbasetables[tablename]["qgisviewsql"] = sheetdatas[
                                row
                            ][1].strip()
                    elif firstcol.strip() == "#EXPO":
                        self.dbasetables[tablename]["exportviewsql"] = sheetdatas[row][
                            1
                        ].strip()
                    elif firstcol.strip() == "#SCAL":
                        self.dbasetables[tablename]["scale"] = float(
                            sheetdatas[row][1].strip()
                        )
                    elif firstcol.strip() == "#SHOW":
                        value = sheetdatas[row][1].strip().strip()
                        if value == "YES":
                            self.dbasetables[tablename]["showinqgis"] = True
                    elif firstcol.strip() == "#SPATIALINDEX":
                        value = sheetdatas[row][1].strip()
                        if value == "YES":
                            self.dbasetables[tablename]["spatialindex"] = True
                    # elif firstcol.strip() == '#ONLYONEPARENTTABLE':
                    #     value = sheetdatas[row][ 1].strip()
                    #     if value == 'YES':
                    #         self.dbasetables[tablename]['onlyoneparenttable'] = True
                    elif firstcol.strip() == "#VARIANTES":
                        # for colnbr in range(1,sheet.ncols):
                        for colnbr in range(1, len(rowcontent)):
                            value = sheetdatas[row][colnbr]
                            if value is None:
                                continue
                            if value.strip() != "":
                                self.dbasetables[tablename]["row_variantes"] = row
                                if value not in self.variantespossibles:
                                    self.variantespossibles.append(
                                        sheetdatas[row][colnbr].strip()
                                    )
                    elif firstcol.strip() == "#field_name":
                        self.dbasetables[tablename]["row_locale"] = row
                        # coldescr, colcst = self._getLocaleColumn(sheetdatas[row])
                        #localize variante, descrption and displayvaklue


                    else:
                        continue

                else:  # column declaration
                    # if firstcol != '':
                    if firstcol not in [None, ""]:
                        fieldname = sheetdatas[row][0].strip()
                        cstcolumntoread = None
                        colindexlocalvalue = None
                        if fieldname == "geom":
                            self.dbasetables[tablename]["geom"] = sheetdatas[row][
                                1
                            ].strip()
                            continue

                        self.dbasetables[tablename]["fields"][fieldname] = {}
                        self.dbasetables[tablename]["fields"][fieldname][
                            "PGtype"
                        ] = sheetdatas[row][
                            1
                        ].strip()  # the pg type

                        # the foreign key
                        if sheetdatas[row][2] not in [None, ""]:
                            self.dbasetables[tablename]["fields"][fieldname][
                                "FK"
                            ] = sheetdatas[row][2].strip()

                        if sheetdatas[row][3] not in [None, ""]:
                            self.dbasetables[tablename]["fields"][fieldname][
                                "ParFldCst"
                            ] = sheetdatas[row][3].strip()
                            
                        # print('***', tablename,fieldname,row)
                        colidxdescription, colidxvariante, colidxdisplayedvalue = self._getLocaleColIndex(tablename,fieldname, sheetdatas, row)
                        # print('**',tablename,fieldname,colidxdescription, colidxvariante, colidxdisplayedvalue  )
                        
                        self.dbasetables[tablename]["fields"][fieldname][
                                    "description"
                                ] = sheetdatas[row][colidxdescription].strip() if (colidxdescription and sheetdatas[row][colidxdescription])  else ''


                        # (
                        #     cstcolumntoread,
                        #     colindexlocalvalue,
                        # ) = self.readOdsConstraintsBase3(
                        #     tablename, fieldname, sheetdatas, row
                        # )
                        self.readOdsConstraintsBase3(
                            tablename,
                            fieldname,
                            sheetdatas,
                            row,
                            colidxvariante,
                            colidxdisplayedvalue,
                        )

                    else:
                        if fieldname is not None and fieldname != "geom":
                            self.readOdsConstraintsBase3(
                                tablename,
                                fieldname,
                                sheetdatas,
                                row,
                                colidxvariante,
                                colidxdisplayedvalue,
                            )

            if debug and self.dbasetables[tablename]["order"] <= 4:
                print("**************************")
                print(self.dbasetables[tablename])

        if "Revision" in self.dbasetables.keys():
            self.revisionwork = True

        return dict(self.dbasetables)

    def _getLocaleColIndex(self,tablename, fieldname, sheetdatas, xlrow ):
        # colidxdescription, colidxvariante, colidxdisplayedvalue
        colidxvariante = self._getColVariante(tablename, sheetdatas, xlrow)
        colidxdisplayedvalue = self._getLocaleColumn(sheetdatas,xlrow, colidxvariante, fieldname,tablename )
        colidxdescription = self._getDescriptionColumn(sheetdatas,xlrow,tablename)

        return colidxdescription, colidxvariante, colidxdisplayedvalue


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
            tablename = sheet.name.split("_")
            fieldname = None
            cstcolumntoread = None
            order = None

            if len(tablename) == 1:  # non table file
                continue
            else:
                order = tablename[0]
                tablename = "_".join(tablename[1:])

            if tablename not in self.dbasetables.keys():
                self.dbasetables[tablename] = {}
                self.dbasetables[tablename]["order"] = int(order)
                self.dbasetables[tablename]["fields"] = {}
                self.dbasetables[tablename]["showinqgis"] = False
                self.dbasetables[tablename]["widget"] = []
                self.dbasetables[tablename]["row_variantes"] = -1

            firstqgsviewoccurrence = True

            for row in range(sheet.nrows):
                firstcol = sheet.cell_value(row, 0)
                if len(firstcol) > 0 and firstcol[0] == "#":  # comment - pass
                    if firstcol.strip() == "#DJAN":
                        self.dbasetables[tablename]["djangoviewsql"] = sheet.cell_value(
                            row, 1
                        ).strip()
                    elif firstcol.strip() == "#QGISSL":
                        if "qgisSLviewsql" in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]["qgisSLviewsql"] += (
                                " " + sheet.cell_value(row, 1).strip() + " "
                            )
                        else:
                            self.dbasetables[tablename][
                                "qgisSLviewsql"
                            ] = sheet.cell_value(row, 1).strip()
                    elif firstcol.strip() == "#QGISPG":
                        if "qgisPGviewsql" in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]["qgisPGviewsql"] += (
                                " " + sheet.cell_value(row, 1).strip() + " "
                            )
                        else:
                            self.dbasetables[tablename][
                                "qgisPGviewsql"
                            ] = sheet.cell_value(row, 1).strip()
                    elif firstcol.strip() == "#QGIS":
                        if firstqgsviewoccurrence:
                            firstqgsviewoccurrence = False
                            self.dbasetables[tablename]["qgisviewsql"] = ""

                        if "qgisviewsql" in self.dbasetables[tablename].keys():
                            self.dbasetables[tablename]["qgisviewsql"] += (
                                " " + sheet.cell_value(row, 1).strip() + " "
                            )
                        else:
                            self.dbasetables[tablename][
                                "qgisviewsql"
                            ] = sheet.cell_value(row, 1).strip()
                    elif firstcol.strip() == "#EXPO":
                        self.dbasetables[tablename]["exportviewsql"] = sheet.cell_value(
                            row, 1
                        ).strip()
                    elif firstcol.strip() == "#SCAL":
                        self.dbasetables[tablename]["scale"] = float(
                            sheet.cell_value(row, 1).strip()
                        )
                    elif firstcol.strip() == "#SHOW":
                        value = sheet.cell_value(row, 1).strip().strip()
                        if value == "YES":
                            self.dbasetables[tablename]["showinqgis"] = True
                    elif firstcol.strip() == "#SPATIALINDEX":
                        value = sheet.cell_value(row, 1).strip()
                        if value == "YES":
                            self.dbasetables[tablename]["spatialindex"] = True
                    # elif firstcol.strip() == '#ONLYONEPARENTTABLE':
                    #     value = sheet.cell_value(row, 1).strip()
                    #     if value == 'YES':
                    #         self.dbasetables[tablename]['onlyoneparenttable'] = True
                    elif firstcol.strip() == "#VARIANTES":
                        for colnbr in range(1, sheet.ncols):
                            value = sheet.cell_value(row, colnbr)
                            if value.strip() != "":
                                self.dbasetables[tablename]["row_variantes"] = row
                                if value not in self.variantespossibles:
                                    self.variantespossibles.append(
                                        sheet.cell_value(row, colnbr).strip()
                                    )
                    else:
                        continue

                else:  # column declaration
                    if firstcol != "":
                        fieldname = sheet.cell_value(row, 0).strip()
                        cstcolumntoread = None
                        if fieldname == "geom":
                            self.dbasetables[tablename]["geom"] = sheet.cell_value(
                                row, 1
                            ).strip()
                            continue

                        self.dbasetables[tablename]["fields"][fieldname] = {}
                        self.dbasetables[tablename]["fields"][fieldname][
                            "PGtype"
                        ] = sheet.cell_value(
                            row, 1
                        ).strip()  # the pg type

                        # the foreign key
                        if sheet.cell_value(row, 2).strip() != "":
                            self.dbasetables[tablename]["fields"][fieldname][
                                "FK"
                            ] = sheet.cell_value(row, 2).strip()

                        if sheet.cell_value(row, 4).strip() != "":
                            self.dbasetables[tablename]["fields"][fieldname][
                                "ParFldCst"
                            ] = sheet.cell_value(row, 4).strip()

                        cstcolumntoread = self.readXlsConstraints(
                            tablename, fieldname, sheet, row, cstcolumntoread
                        )

                    else:
                        if fieldname is not None and fieldname != "geom":
                            self.readXlsConstraints(
                                tablename, fieldname, sheet, row, cstcolumntoread
                            )

            if debug and self.dbasetables[tablename]["order"] <= 4:
                print("**************************")
                print(self.dbasetables[tablename])

        if "Revision" in self.dbasetables.keys():
            self.revisionwork = True

        return dict(self.dbasetables)

    # def readConstraints(self, tablename,fieldname  ,sheet, xlrow,cstcolumntoread=None):
    def readOdsConstraints(
        self, tablename, fieldname, sheetdatas, xlrow, cstcolumntoread=None
    ):

        # dbasefield self.dbasetables[tablename]['fields'][fieldname]
        # print('readConstraints',tablename,fieldname  ,sheet, xlrow)
        colindexvariante = cstcolumntoread
        dbasefield = self.dbasetables[tablename]["fields"][fieldname]

        if colindexvariante is None:
            colindexvariante = None
            if self.dbase.variante is None:
                colindexvariante = 5
            else:
                if self.dbasetables[tablename]["row_variantes"] >= 0:
                    rowvariantes = self.dbasetables[tablename]["row_variantes"]
                    if self.dbase.variante == "Lamia":
                        colindexvariante = 5
                    else:
                        for col in range(len(sheetdatas[rowvariantes])):
                            try:
                                if (
                                    sheetdatas[rowvariantes][col] == self.dbase.variante
                                    and sheetdatas[xlrow][col] != ""
                                ):
                                    colindexvariante = col
                                    # print('colindexvariante', tablename, fieldname, colindexvariante)
                                    break
                            except:
                                print(
                                    "error", tablename, fieldname, self.dbase.variante
                                )
                        # if colindexvariante is None:
                        #    colindexvariante = 5
        if colindexvariante is None:
            colindexvariante = 5

        # if unicode(sheet.cell_value(xlrow, colindexvariante)).strip() != '':
        if (
            sheetdatas[xlrow][colindexvariante] is not None
            and sheetdatas[xlrow][colindexvariante].strip() != ""
        ):
            if "Cst" in dbasefield.keys():
                dbasefield["Cst"].append([])
            else:
                dbasefield["Cst"] = [[]]

            showvalue = self.convertxlsdataToString(sheetdatas[xlrow][colindexvariante])
            datavalue = self.convertxlsdataToString(
                sheetdatas[xlrow][colindexvariante + 1]
            )
            dbasefield["Cst"][-1].append(showvalue.strip())
            dbasefield["Cst"][-1].append(datavalue.strip())

            if (
                sheetdatas[xlrow][colindexvariante + 2] is not None
                and sheetdatas[xlrow][colindexvariante + 2].strip() != ""
            ):
                dbasefield["Cst"][-1].append(
                    eval(sheetdatas[xlrow][colindexvariante + 2].strip())
                )
            else:
                dbasefield["Cst"][-1].append(None)

        return colindexvariante

    def readOdsConstraintsBase3(
        self,
        tablename,
        fieldname,
        sheetdatas,
        xlrow,
        colidxvariante=None,
        colidxdisplayedvalue=None,
    ):
        # dbasefield self.dbasetables[tablename]['fields'][fieldname]
        # print('readConstraints',tablename,fieldname  ,sheet, xlrow)
        # rowvariantes = self.dbasetables[tablename]["row_variantes"]
        # rowlocale = self.dbasetables[tablename]["row_locale"]
        # colindexvariante = cstcolumntoread
        # colindexlocalvalue = cstlocalvaluecolumntoread
        dbasefield = self.dbasetables[tablename]["fields"][fieldname]
        # loclanguage = self.dbase.locale

        # if colindexvariante is None:
        #     colindexvariante = None
        #     if self.dbase.variante is None:
        #         colindexvariante = 6
        #     else:
        #         if rowvariantes >= 0:
        #             if self.dbase.variante == "Lamia":
        #                 colindexvariante = 6
        #             else:
        #                 for col in range(len(sheetdatas[rowvariantes])):
        #                     try:
        #                         if (
        #                             sheetdatas[rowvariantes][col] == self.dbase.variante
        #                             and sheetdatas[xlrow][col] != ""
        #                         ):
        #                             colindexvariante = col
        #                             # print('colindexvariante', tablename, fieldname, colindexvariante)
        #                             break
        #                     except:
        #                         print(
        #                             "error", tablename, fieldname, self.dbase.variante
        #                         )
        #                 # if colindexvariante is None:
        #                 #    colindexvariante = 5
        # if colindexvariante is None:
        #     colindexvariante = 6
        
        # colindexvariante = self._getColVariante(tablename, sheetdatas, xlrow, colindexvariante)
        
        if (
            sheetdatas[xlrow][colidxvariante] is not None
            and sheetdatas[xlrow][colidxvariante].strip() != ""
        ):
            if "Cst" in dbasefield.keys():
                dbasefield["Cst"].append([])
            else:
                dbasefield["Cst"] = [[]]

        #     if colindexlocalvalue is None:
        #         # if unicode(sheet.cell_value(xlrow, colindexvariante)).strip() != '':
        #         # get showvalue column according to language
        #         initcolumn = colindexvariante + 2
        #         dictlang = {}
        #         while (
        #             initcolumn < len(sheetdatas[rowlocale])
        #             and "Displayvalue" in sheetdatas[rowlocale][initcolumn].strip()
        #         ):
        #             valuesplited = sheetdatas[rowlocale][initcolumn].split("_")
        #             if len(valuesplited):
        #                 dictlang[valuesplited[1]] = initcolumn
        #             else:
        #                 dictlang["None"] = initcolumn
        #             initcolumn += 1
        #         if (
        #             loclanguage in dictlang.keys()
        #             and sheetdatas[xlrow][dictlang[loclanguage]] != ""
        #         ):
        #             colindexlocalvalue = dictlang[loclanguage]
        #         elif (
        #             "fr" in dictlang.keys() and sheetdatas[xlrow][dictlang["fr"]] != ""
        #         ):
        #             colindexlocalvalue = dictlang["fr"]
        #         elif (
        #             "None" in dictlang.keys()
        #             and sheetdatas[xlrow][dictlang["None"]] != ""
        #         ):
        #             colindexlocalvalue = dictlang["None"]

            print('**', 
                    tablename,
                    fieldname,
                    # sheetdatas,
                    xlrow,
                    colidxvariante,
                    colidxdisplayedvalue)

            datavalue = self.convertxlsdataToString(sheetdatas[xlrow][colidxvariante])
            showvalue = self.convertxlsdataToString(
                sheetdatas[xlrow][colidxdisplayedvalue]
            )

            if datavalue == "NULL":
                datavalue = ""

            dbasefield["Cst"][-1].append(showvalue.strip())
            dbasefield["Cst"][-1].append(datavalue.strip())

            if (
                sheetdatas[xlrow][colidxvariante + 1] is not None
                and sheetdatas[xlrow][colidxvariante + 1].strip() != ""
            ):
                dbasefield["Cst"][-1].append(
                    eval(sheetdatas[xlrow][colidxvariante + 1].strip())
                )
            else:
                dbasefield["Cst"][-1].append(None)

        # return colindexvariante, colindexlocalvalue

    # def readConstraints(self, tablename,fieldname  ,sheet, xlrow,cstcolumntoread=None):
    def readXlsConstraints(
        self, tablename, fieldname, sheet, xlrow, cstcolumntoread=None
    ):

        # dbasefield self.dbasetables[tablename]['fields'][fieldname]
        # print('readConstraints',tablename,fieldname  ,sheet, xlrow)
        colindexvariante = cstcolumntoread
        dbasefield = self.dbasetables[tablename]["fields"][fieldname]

        if colindexvariante is None:
            colindexvariante = None
            if self.dbase.variante is None:
                colindexvariante = 5
            else:
                if self.dbasetables[tablename]["row_variantes"] >= 0:
                    rowvariantes = self.dbasetables[tablename]["row_variantes"]
                    if self.dbase.variante == "Lamia":
                        colindexvariante = 5
                    else:
                        for col in range(sheet.ncols):
                            try:
                                if (
                                    sheet.cell_value(rowvariantes, col)
                                    == self.dbase.variante
                                    and sheet.cell_value(xlrow, col) != ""
                                ):
                                    colindexvariante = col
                                    # print('colindexvariante', tablename, fieldname, colindexvariante)
                                    break
                            except:
                                print(
                                    "error", tablename, fieldname, self.dbase.variante
                                )
                        # if colindexvariante is None:
                        #    colindexvariante = 5
        if colindexvariante is None:
            colindexvariante = 5

        # if unicode(sheet.cell_value(xlrow, colindexvariante)).strip() != '':
        if sheet.cell_value(xlrow, colindexvariante).strip() != "":
            if "Cst" in dbasefield.keys():
                dbasefield["Cst"].append([])
            else:
                dbasefield["Cst"] = [[]]

            showvalue = self.convertxlsdataToString(
                sheet.cell_value(xlrow, colindexvariante)
            )
            datavalue = self.convertxlsdataToString(
                sheet.cell_value(xlrow, colindexvariante + 1)
            )
            dbasefield["Cst"][-1].append(showvalue.strip())
            dbasefield["Cst"][-1].append(datavalue.strip())

            if sheet.cell_value(xlrow, colindexvariante + 2).strip() != "":
                dbasefield["Cst"][-1].append(
                    eval(sheet.cell_value(xlrow, colindexvariante + 2).strip())
                )
            else:
                dbasefield["Cst"][-1].append(None)

        return colindexvariante

    def _getColVariante(self,tablename, sheetdatas,xlrow, colindexvariante=None):
        """Get, for a field the index of col with the variante. 
        If variante description is null for the field, take he default (Lamia) variante
        """
        # get lamia col
        rowvariantes = self.dbasetables[tablename]["row_variantes"]
        variantedefaultlamiacol = None
        variantecol = None
        for col in range(len(sheetdatas[rowvariantes])):
            if sheetdatas[rowvariantes][col] and sheetdatas[rowvariantes][col].lower() == 'lamia':
                variantedefaultlamiacol = col
            elif sheetdatas[rowvariantes][col] and  sheetdatas[rowvariantes][col] == self.dbase.variante:
                variantecol = col
        
        if colindexvariante is None:
            if self.dbase.variante is None or self.dbase.variante == "Lamia":
                colindexvariante = variantedefaultlamiacol
            elif sheetdatas[xlrow][variantecol] != "" : #something is filled in the variante col
                colindexvariante = variantecol
            else:   #nothing is filled in the variant col
                colindexvariante = variantedefaultlamiacol

        # if colindexvariante is None:
        #     # colindexvariante = None
        #     if self.dbase.variante is None:
        #         # colindexvariante = 6
        #         colindexvariante = variantedefaultlamiacol
        #     else:
        #         if rowvariantes >= 0:
        #             if self.dbase.variante == "Lamia":
        #                 # colindexvariante = 6
        #                 colindexvariante = variantedefaultlamiacol
        #             else:
        #                 for col in range(len(sheetdatas[rowvariantes])):
        #                     try:
        #                         if (
        #                             sheetdatas[rowvariantes][col] == self.dbase.variante
        #                             and sheetdatas[xlrow][col] != ""
        #                         ):
        #                             colindexvariante = col
        #                             # print('colindexvariante', tablename, fieldname, colindexvariante)
        #                             break
        #                     except:
        #                         pass
        #                         # print(
        #                         #     "error", tablename, fieldname, self.dbase.variante
        #                         # )
        #                 # if colindexvariante is None:
        #                 #    colindexvariante = 5
        # if colindexvariante is None:
        #     colindexvariante = 6

        return colindexvariante

    def _getLocaleColumn(self,sheetdatas,xlrow, colindexvariante,fieldname,tablename ):
        """get the column of displayed value for the choosen variante.
        Take fr value if nooting is filled 
        """
        rowlocale = self.dbasetables[tablename]["row_locale"]
        # dbasefield = self.dbasetables[tablename]["fields"][fieldname]
        loclanguage = self.dbase.locale
        colindexlocalvalue = None

        if fieldname == 'presencesiphoidpartition':
            print('ok')

        if (
            sheetdatas[xlrow][colindexvariante] is not None
            and sheetdatas[xlrow][colindexvariante].strip() != ""
        ):
            # if "Cst" in dbasefield.keys():
            #     dbasefield["Cst"].append([])
            # else:
            #     dbasefield["Cst"] = [[]]

            if colindexlocalvalue is None:
                # if unicode(sheet.cell_value(xlrow, colindexvariante)).strip() != '':
                # get showvalue column according to language
                initcolumn = colindexvariante + 2
                # get dict : {..., locale:colidx,...}
                dictlang = {}
                while (
                    initcolumn < len(sheetdatas[rowlocale])
                    and "Displayvalue" in sheetdatas[rowlocale][initcolumn].strip()
                ):
                    valuesplited = sheetdatas[rowlocale][initcolumn].split("_")
                    if len(valuesplited):
                        dictlang[valuesplited[1]] = initcolumn
                    else:
                        dictlang["None"] = initcolumn
                    initcolumn += 1
                
                if (
                    loclanguage in dictlang.keys()
                    and sheetdatas[xlrow][dictlang[loclanguage]] != ""
                ):
                    colindexlocalvalue = dictlang[loclanguage]
                elif (
                    "fr" in dictlang.keys() and sheetdatas[xlrow][dictlang["fr"]] != ""
                ):
                    colindexlocalvalue = dictlang["fr"]
                elif (
                    "None" in dictlang.keys()
                    and sheetdatas[xlrow][dictlang["None"]] != ""
                ):
                    colindexlocalvalue = dictlang["None"]

        return colindexlocalvalue

    def _getDescriptionColumn(self,sheetdatas,xlrow,tablename ):
        rowlocale = self.dbasetables[tablename]["row_locale"]
        loclanguage = self.dbase.locale
        colidxdescription = None

        initcolumn = 1
        # get dict : {..., locale:colidx,...}
        dictlang = {}
        while (
            initcolumn < len(sheetdatas[rowlocale])
            # and "Displayvalue" in sheetdatas[rowlocale][initcolumn].strip()
        ):
            valuesplited = sheetdatas[rowlocale][initcolumn].split("_")
            if len(valuesplited) and valuesplited[0].lower() == 'description':
                dictlang[valuesplited[1]] = initcolumn
            # else:
            #     dictlang["None"] = initcolumn
            initcolumn += 1

            if (
                loclanguage in dictlang.keys()
                and sheetdatas[xlrow][dictlang[loclanguage]] != ""
            ):
                colidxdescription = dictlang[loclanguage]
            elif (
                "fr" in dictlang.keys() and sheetdatas[xlrow][dictlang["fr"]] != ""
            ):
                colidxdescription = dictlang["fr"]
            elif (
                "None" in dictlang.keys()
                and sheetdatas[xlrow][dictlang["None"]] != ""
            ):
                colidxdescription = dictlang["None"]
        
        return colidxdescription
        

    def convertxlsdataToString(self, data):
        if data is None:
            data = ""
        elif isinstance(data, str):
            data = data
        elif isinstance(data, float):
            data = str(data).rstrip("0").rstrip(".")
        else:
            data = str(data)

        # print('data1', data, data.__class__)
        return data

    def getMaxVersionRepository(self, typemetier):
        """
        REcherche dans Lamia/DBASE/create le repertoire qui correspond au typemetier, avec la plus grande version
        s'il n'y a pas de version (lamia avant sept.2018) , renvoi le repertoire avec version = None

        :param typemetier:
        :return:
        """
        version = ""
        repository = None

        createfilesdir = os.path.join(
            os.path.dirname(__file__), "..", "DBASE", "create"
        )
        listrep = os.listdir(createfilesdir)
        for rep in listrep:
            if len(rep.split("_")) > 2:
                if typemetier == "_".join(rep.split("_")[:-2]):
                    versiontemp = "_".join(rep.split("_")[-2:])
                    if versiontemp > version:
                        repository = os.path.join(createfilesdir, rep)
                        version = versiontemp
            else:
                if typemetier == rep:
                    repository = os.path.join(createfilesdir, rep)

        return repository, version

    def getWorktypeVersionsList(self, worktype):
        """
        return list of versions for worktype
        """
        debug = False
        results = []

        if worktype.split("_")[0] == "base3":
            createfilesdir = os.path.join(
                os.path.dirname(Lamia.config.__file__), worktype, "dbase"
            )
        else:
            # createfilesdir = os.path.join(
            #     os.path.dirname(__file__), "..", "DBASE_old", "create"
            # )
            createfilesdir = os.path.join(
                os.path.dirname(Lamia.qgisiface.__file__), "DBASE_old", "create"
            )

        if debug:
            logging.getLogger("Lamia").debug("dbase dir : %s", str(createfilesdir))

        listfiles = os.listdir(createfilesdir)
        for filename in listfiles:
            filepath = os.path.join(createfilesdir, filename)
            filebasename, ext = os.path.splitext(filename)

            # if os.path.isfile(filepath) and ext in ['.xls', '.xlsx']:
            if os.path.isfile(filepath) and ext in [".ods"]:
                filebasenamesplitted = filebasename.split("_")
                if (
                    len(filebasenamesplitted) > 2
                    and filebasenamesplitted[-2].isdigit()
                    and filebasenamesplitted[-1].isdigit()
                    and worktype == "_".join(filebasenamesplitted[:-2])
                ):  # case child of dabse2
                    versiontemp = "_".join(filebasename.split("_")[-2:])
                    repository = os.path.join(createfilesdir, filename)
                    results.append([versiontemp, repository])
        if debug:
            logging.getLogger("Lamia").debug("results: %s", str(results))

        results.sort()

        if debug:
            logging.getLogger("Lamia").debug("results: %s", str(results))

        return results

    def createProjectOds(self, projectresourcedir, wortype):
        toodspath = os.path.join(
            projectresourcedir, "config", "dbase", wortype + ".ods",
        )
        fromodspath = os.path.join(
            os.path.dirname(Lamia.__file__), "api", "assets", "emptyform.ods"
        )
        shutil.copy(fromodspath, toodspath)

