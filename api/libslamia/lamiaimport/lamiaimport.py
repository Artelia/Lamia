# -*- coding: utf-8 -*-

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


import logging, sys, re, os
import numpy as np
from pprint import pprint
from ..abstractlibslamia import AbstractLibsLamia


class ImportCore(AbstractLibsLamia):

    POSTPROTOOLNAME = "lamiaimport"
    fileext = ".json"

    def __init__(self, dbaseparser, messageinstance=None):
        super(ImportCore, self).__init__(dbaseparser, messageinstance)
        # super(ExportShapefileTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
        # self.dbase = dbaseparser
        # self.messageinstance = messageinstance
        # self.tooldir = os.path.join(
        #     os.path.dirname(__file__), self.dbase.worktype.lower()
        # )

        # self.confdataplugin = os.path.join(
        #     os.path.dirname(__file__), self.dbase.worktype.lower()
        # )
        # self.confdataproject = os.path.join(
        #     self.dbase.dbaseressourcesdirectory, "config", self.POSTPROTOOLNAME
        # )

    def importCleanedDatas(
        self,
        rawtablename=None,
        table_field_list=None,
        values=None,
        geoms=None,
        returnfield=None,
    ):

        """

        :param tablename: table name
        :param table_field_list: list of values tablename.fieldname
        :param values: array of values : each line is e new element, and each row correspond to table_field row
        :params geoms: list of geoms in wkt form
        :param returnfield:  fieldname corresponding to the data returned by this method
        :return: array of data of returnfield
        """

        debug = False

        print(table_field_list)
        print(values)
        # print(geoms)

        tablesnames = np.array([result.split(".")[0] for result in table_field_list])
        fieldsnames = np.array([result.split(".")[1] for result in table_field_list])

        parenttables = [rawtablename] + self.dbase.getParentTable(rawtablename)
        self.messageinstance.createProgressBar(
            inittext="import ...", maxvalue=len(values)
        )

        self.dbase.beginTransaction()

        # cas des couches enfant de descriptionsystem
        for i, valueline in enumerate(values):

            valueline = np.array(self.cleanvalue(rawtablename, fieldsnames, valueline))
            # print("**", valueline)
            zipdict = dict(zip(fieldsnames.tolist(), valueline.tolist()))
            if "geom" in self.dbase.dbasetables[rawtablename].keys():
                zipdict["geom"] = self._getCleanedWktGeom(geoms[i])
            # print(zipdict)
            # self.setLoadingProgressBar(progress, i)
            if i % 50 == 0:
                # return
                self.messageinstance.updateProgressBar(i)

            # pktablename = self.dbase.createNewFeature(rawtablename)
            pktablename = self.dbase.lamiaorm[rawtablename].create()
            self.dbase.lamiaorm[rawtablename].update(pktablename, zipdict)

            # for tablename in parenttables:
            #     pktable = self.dbase.getValuesFromPk(
            #         rawtablename + "_qgis", "pk_" + tablename.lower(), pktablename
            #     )
            #     indexobjectvalues = np.where(np.array(tablesnames) == tablename)
            #     lisfield = fieldsnames[indexobjectvalues]
            #     listvalues = valueline[indexobjectvalues]
            #     self.updateTable(tablename, lisfield, listvalues, pktable)

            #     if "geom" in self.dbase.dbasetables[tablename].keys():
            #         if self.dbase.__class__.TYPE == "spatialite":
            #             geomsql = "CastToSingle(CastToXY(ST_GeomFromText('"
            #             geomsql += geoms[i]
            #             geomsql += "', " + str(self.dbase.crsnumber) + ")))"
            #         elif self.dbase.__class__.TYPE == "postgis":
            #             geomsql = "ST_GeometryN(ST_Force2D(ST_GeomFromText('"
            #             geomsql += geoms[i]
            #             geomsql += "', " + str(self.dbase.crsnumber) + ")),0)"

            #         self.updateTable(tablename, ["geom"], [geomsql], pktable)

        self.dbase.commitTransaction()

        self.messageinstance.closeProgressBar()

    def _getCleanedWktGeom(self, wktgeom):

        if self.dbase.__class__.TYPE == "spatialite":
            geomsql = "SELECT ST_AsText(CastToSingle(CastToXY(ST_GeomFromText('"
            geomsql += wktgeom
            geomsql += "', " + str(self.dbase.crsnumber) + "))))"
        elif self.dbase.__class__.TYPE == "postgis":
            geomsql = "SELECT ST_AsText(ST_GeometryN(ST_Force2D(ST_GeomFromText('"
            geomsql += wktgeom
            geomsql += "', " + str(self.dbase.crsnumber) + ")),0))"
        geomwkt = self.dbase.query(geomsql)
        # print("*", geomwkt)
        return geomwkt[0][0]

    def cleanvalue(self, tablename, listfield, listvalues):
        finallistvalues = []
        for i, fieldname in enumerate(listfield):
            if listvalues[i] != "":
                # sql += fieldname + " = "
                finallistvalues.append(
                    self.convertDataType(tablename, fieldname, listvalues[i])
                )
        return finallistvalues

    def updateTable(self, tablename, listfield, listvalues, pkvalue):

        sql = "UPDATE " + tablename + " SET "
        for i, fieldname in enumerate(listfield):
            if listvalues[i] != "":
                sql += fieldname + " = "
                sql += self.convertDataType(tablename, fieldname, listvalues[i]) + ", "

        if sql[-2:] == ", ":
            sql = sql[:-2]
        sql += " WHERE pk_" + tablename.lower() + " = " + str(pkvalue)
        query = self.dbase.query(sql, docommit=False)

    def convertDataType(self, rawtable, field, value):
        if field == "geom":
            return str(value)

        if self.dbase.utils.isAttributeNull(value):
            return "NULL"

        for temptable in [rawtable] + self.dbase.getParentTable(rawtable):
            if field in self.dbase.dbasetables[temptable]["fields"].keys():
                # typevalue = self.dbase.dbasetables[temptable]["fields"][field]["PGtype"]
                # getConstraintRawValueFromText(self, table, field, txt):
                rawvalue = self.dbase.getConstraintRawValueFromText(
                    temptable, field, value
                )
                break

        # if "VARCHAR" in typevalue:
        #     returnvalue = "'" + str(rawvalue) + "'"
        # elif "TIMESTAMP" in typevalue:
        #     returnvalue = "'" + str(rawvalue) + "'"
        # elif "TEXT" in typevalue:
        #     returnvalue = "'" + str(rawvalue) + "'"
        # else:
        #     returnvalue = str(rawvalue)

        return str(rawvalue)

    def postImport(self, layerfeat, pkobjet=None, pkdessys=None, pksubdessys=None):
        pass
