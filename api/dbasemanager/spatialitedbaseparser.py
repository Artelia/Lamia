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

if sys.version_info.major == 2:
    import pyspatialite
elif sys.version_info.major == 3:
    import sqlite3

from .dbaseparserabstract import *


class SpatialiteDBaseParser(AbstractDBaseParser):

    TYPE = "spatialite"

    def __init__(self, parserfactory, messageinstance):
        super(SpatialiteDBaseParser, self).__init__(parserfactory, messageinstance)

    def connectToDBase(self, slfile=None, **kwargs):
        self.spatialitefile = slfile
        self.connSLITE = sqlite3.dbapi2.connect(slfile)
        self.connSLITE.enable_load_extension(True)
        cur = self.connSLITE.cursor()
        cur.execute("SELECT load_extension('mod_spatialite')")  # mod_spatialite.so
        self.SLITEcursor = self.connSLITE.cursor()

    def disconnect(self):
        try:
            self.connSLITE.close()
        except Exception as e:
            pass
            # print("error on closing connection : ", e)

    def getDBName(self):
        name, ext = os.path.splitext(os.path.basename(self.spatialitefile))
        return name

    def generateSQLTableCreationFromDBConfig(self, name, dbasetable, crs):

        sql = {}
        listFK = []
        sql["main"] = "CREATE TABLE "
        sql["main"] += name + "("

        for key in dbasetable["fields"]:
            sltype = None
            if dbasetable["fields"][key]["PGtype"] in PGTYPE_TO_SLTYPE.keys():
                sltype = PGTYPE_TO_SLTYPE[dbasetable["fields"][key]["PGtype"]]
            elif "VARCHAR" in dbasetable["fields"][key]["PGtype"]:
                sltype = "TEXT"
            if key is None or sltype is None:
                raise TypeError(key, sltype, name)
            sql["main"] += key + " " + sltype + ","

            if "FK" in dbasetable["fields"][key].keys():
                listFK.append(
                    "FOREIGN KEY("
                    + key
                    + ") REFERENCES "
                    + dbasetable["fields"][key]["FK"]
                )

        sql["main"] += ",".join(listFK)
        if sql["main"][-1] == ",":
            sql["main"] = sql["main"][:-1]
        sql["main"] = sql["main"] + ");"

        if "geom" in dbasetable.keys():
            sql["other"] = []
            sql["other"].append(
                "SELECT AddGeometryColumn('"
                + name
                + "','geom',"
                + str(crs)
                + ", '"
                + dbasetable["geom"]
                + "', 'XY');"
            )
        return sql

    def generateSQLViewCreationFromDBConfig(self, dbname, dbasetable, worktype, crs):
        """
        return sql list to be queried
        """
        finalsqllist = []
        viewnames = {}
        if "djangoviewsql" in dbasetable.keys():
            viewnames["djangoviewsql"] = str(dbname) + "_django"

        if "qgisPGviewsql" in dbasetable.keys():
            viewnames["qgisPGviewsql"] = str(dbname) + "_qgis"
        elif "qgisviewsql" in dbasetable.keys():
            viewnames["qgisviewsql"] = str(dbname) + "_qgis"

        if "exportviewsql" in dbasetable.keys():
            viewnames["exportviewsql"] = str(dbname) + "_export"

        for viewname in viewnames.keys():
            sql = "CREATE VIEW " + str(viewnames[viewname]) + " AS "
            if dbasetable[viewname].strip() != "":
                sql += dbasetable[viewname]
            else:
                sql += "SELECT * FROM " + str(dbname)
            finalsqllist.append(sql)

            # if self.isTableSpatial(viewnames[viewname]):
            if self.isTableSpatial(dbname):
                dbnamelower = dbname.lower()
                # idcolumnname = self.getFirstIdColumn(viewnames[viewname])
                idcolumnname = self.getFirstIdColumn(dbname)
                viewlower = viewnames[viewname].lower()
                try:
                    sql = "INSERT INTO views_geometry_columns (view_name, view_geometry, view_rowid, "
                    sql += "f_table_name, f_geometry_column,read_only)"
                    sql += (
                        " VALUES ('"
                        + str(viewlower)
                        + "','geom','"
                        + idcolumnname
                        + "','"
                        + str(dbnamelower)
                    )
                    sql += "','geom',0)"
                    finalsqllist.append(sql)
                except TypeError as e:
                    print(dbname, e)
                    print(viewlower, idcolumnname, dbnamelower)
                    raise TypeError

        return finalsqllist

    def initDBase(self, **kwargs):
        slfile = kwargs.get("slfile", None)
        if slfile is None:
            raise ValueError("Init DBase : No file path given")

        originalfile = os.path.join(
            os.path.dirname(__file__), "..", "assets", "DBase_ind0.sqlite"
        )
        shutil.copyfile(originalfile, slfile)

    def query(self, sql, arguments=[], docommit=True):
        # cursor = self.connSLITE.cursor()
        if self.SLITEcursor is None:
            self.SLITEcursor = self.connSLITE.cursor()
        try:
            if self.printsql and sql.split(' ')[0].lower() == 'update':
                logging.getLogger("Lamia_unittest").debug("%s - %s ", docommit, sql)
                # if sql.split(' ')[0].lower() in ['update', 'delete','insert']:
                #     #logging.getLogger('Lamia').debug('%s - %s %.3f', docommit, sql,  self.getTimeNow() - timestart)
                #     logging.getLogger('Lamia_unittest').debug('%s - %s ', docommit, sql)

            query = self.SLITEcursor.execute(sql, arguments)
            returnquery = list(query)
            if docommit and self.forcenocommit == False:
                self.commit()

            return returnquery
        except (sqlite3.dbapi2.OperationalError, sqlite3.dbapi2.IntegrityError) as e:
            # self.errorquerymessage.emit(str(e))
            # if self.qgsiface is None:

            if self.raiseexceptions:
                print(sql, arguments)
                raise TypeError("error query", e)
            else:
                print(sql)
                print("error query", e)

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
        # print(result)
        if "geom" in result:
            return True
        else:
            return False

    def getTables(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table'"
        result = self.query(sql)
        return [elem[0] for elem in result]

    def getColumns(self, tablename):
        if tablename in self.columnsnames.keys():
            return self.columnsnames[tablename]

        sql = "PRAGMA table_info(" + str(tablename) + ")"
        query = self.query(sql)
        result = [row[1] for row in query]
        self.columnsnames[tablename] = result
        return result

    def getFirstIdColumn(self, tablename):
        sql = "PRAGMA table_info(" + str(tablename) + ")"
        query = self.query(sql)
        result = [row[1] for row in query]
        for fieldname in result:
            if "pk_" in fieldname:
                return fieldname

    def getLastPK(self, tablename):
        sql = "SELECT * FROM sqlite_sequence "
        results = self.query(sql)
        for res in results:
            if res[0] == tablename:
                return res[1]
        return 0

    def _dateVersionConstraintSQL(self, specialdate=None):
        if specialdate is None or specialdate == "now":
            # workingdatemodif = QtCore.QDate.fromString(self.workingdate, 'yyyy-MM-dd').addDays(1).toString('yyyy-MM-dd')
            workingdatemodif = (
                datetime.datetime.now() + datetime.timedelta(days=1)
            ).strftime("%Y-%m-%d")
        else:
            # workingdatemodif = QtCore.QDate.fromString(specialdate, 'dd/MM/yyyy').addDays(1).toString('yyyy-MM-dd')
            workingdatemodif = (
                datetime.datetime.strptime(specialdate, "%d/%m/%Y")
                + datetime.timedelta(days=1)
            ).strftime("%Y-%m-%d")

        sqlin = " datetimecreation <= " + "'" + workingdatemodif + "'"
        sqlin += " AND CASE WHEN datetimedestruction IS NOT NULL  "
        sqlin += (
            "THEN datetimedestruction > " + "'" + workingdatemodif + "'" + " ELSE 1 END"
        )
        sqlin += " AND lpk_revision_begin <= " + str(self.currentrevision)
        sqlin += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
        sqlin += " lpk_revision_end > " + str(self.currentrevision)
        sqlin += " ELSE 1 END"

        return sqlin

    def createBlobThumbnail(self, pkresource, filepath):
        if not os.path.isfile(self.completePathOfFile(filepath)):
            return

        filebase, fileext = os.path.splitext(filepath)

        if PILexists and fileext.lower() in [".jpg", ".jpeg", ".png"]:
            try:
                size = THUMBNAIL_SIZE, THUMBNAIL_SIZE
                im = PIL.Image.open(filepath)
                im.thumbnail(size)
                imgByteArr = io.BytesIO()
                im.save(imgByteArr, format="PNG")
                im.close()
                biteval = imgByteArr.getvalue()
                self.connSLITE.cursor().execute(
                    "UPDATE resource SET thumbnail = (?) WHERE pk_resource = (?)",
                    [biteval, pkresource],
                )
            except OSError:
                pass

    def valToBinary(self, val):
        return sqlite3.Binary(val)
