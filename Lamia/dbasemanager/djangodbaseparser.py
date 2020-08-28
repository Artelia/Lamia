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
from django.db import connection
import django

from .dbaseparserabstract import *


class DjangoDBaseParser(AbstractDBaseParser):

    TYPE = "django"

    def __init__(self, parserfactory, messageinstance):
        super(DjangoDBaseParser, self).__init__(parserfactory, messageinstance)

    def connectToDBase(
        self,
        host="localhost",
        port=None,
        dbname=None,
        schema=None,
        user=None,
        password=None,
        **kwargs,
    ):
        # self.dbasetype = "postgis"
        # self.pgport = port
        # self.pghost = host
        # self.pgdb = dbname
        self.pgschema = schema
        # self.pguser = user
        # self.pgpassword = password

        # # connexion
        # # connect to postgres for checking database existence
        # connectstr = (
        #     "dbname='postgres' user='"
        #     + user
        #     + "' host='"
        #     + host
        #     + "' password='"
        #     + password
        #     + "'"
        # )
        # connpgis = psycopg2.connect(connectstr)
        # pgiscursor = connpgis.cursor()
        # connpgis.autocommit = True
        # pgiscursor.close()
        # connpgis.close()

        # # connexion to database
        # connectstr = (
        #     "dbname='" + self.pgdb.lower() + "' user='" + user + "' host='" + host
        # )
        # connectstr += "' password='" + password + "'"
        # self.connPGis = psycopg2.connect(connectstr)
        # self.PGiscursor = self.connPGis.cursor()

        self.djangocursor = connection.cursor()

        # searchpath
        sql = "SET search_path TO " + self.pgschema.lower() + ", public;"
        self.query(sql)
        self.commit()

    def disconnect(self):
        self.PGiscursor.close()
        self.connPGis.close()

    def getDBName(self):
        return self.pgschema

    def generateSQLTableCreationFromDBConfig_oldd(self, name, dbasetable, crs):

        sql = {}
        listFK = []
        sql["main"] = "CREATE TABLE "
        sql["main"] += name + "("

        for key in dbasetable["fields"]:
            sql["main"] += key + " " + dbasetable["fields"][key]["PGtype"]
            if "FK" in dbasetable["fields"][key].keys():
                sql["main"] += " REFERENCES " + dbasetable["fields"][key]["FK"]
            sql["main"] += ","

        if sql["main"][-1] == ",":
            sql["main"] = sql["main"][:-1]
        sql["main"] = sql["main"] + ");"

        if "geom" in dbasetable.keys():
            sql["other"] = []
            sql["other"].append(
                "ALTER TABLE "
                + name
                + " ADD  COLUMN   geom geometry('"
                + dbasetable["geom"]
                + "',"
                + str(crs)
                + ");"
            )

        return sql

    def generateSQLTableCreationFromDBConfig_Old(self, name, dbasetable, crs):

        sql = {}
        listFK = []
        sql["main"] = "CREATE TABLE "
        sql["main"] += self.pgschema + "." + name + "("

        for key in dbasetable["fields"]:
            sql["main"] += key + " " + dbasetable["fields"][key]["PGtype"]
            if "FK" in dbasetable["fields"][key].keys():
                sql["main"] += (
                    " REFERENCES "
                    + self.pgschema.lower()
                    + "."
                    + dbasetable["fields"][key]["FK"]
                )
            sql["main"] += ","

        if sql["main"][-1] == ",":
            sql["main"] = sql["main"][:-1]
        sql["main"] = sql["main"] + ");"

        if "geom" in dbasetable.keys():
            sql["other"] = []
            sql["other"].append(
                "ALTER TABLE "
                + self.pgschema
                + "."
                + name
                + " ADD  COLUMN   geom geometry('"
                + dbasetable["geom"]
                + "',"
                + str(crs)
                + ");"
            )

        return sql

    def generateSQLViewCreationFromDBConfig_old(
        self, dbname, dbasetable, worktype, crs
    ):
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

            if self.isTableSpatial(dbname):
                dbnamelower = dbname.lower()
                idcolumnname = self.getFirstIdColumn(dbname)
                viewlower = viewnames[viewname].lower()
                sql = "INSERT INTO geometry_columns(f_table_catalog, f_table_schema, f_table_name, "
                sql += 'f_geometry_column, coord_dimension, srid, "type") VALUES ('
                sql += (
                    "'"
                    + worktype.lower()
                    + "', '"
                    + self.pgschema.lower()
                    + "', '"
                    + str(viewlower)
                    + "','geom',2,"
                )
                sql += str(crs) + ",'" + dbasetable["geom"] + "' );"
                finalsqllist.append(sql)

        return finalsqllist

    def initDBase_old(self, **kwargs):
        host = kwargs.get("host", "localhost")
        port = kwargs.get("port", 5432)
        dbname = kwargs.get("dbname", None)
        schema = kwargs.get("schema", None)
        user = kwargs.get("user", None)
        password = kwargs.get("password", None)

        if None in [dbname, schema, user, password]:
            raise ValueError("Init DBase : postgis conf not complete")

        # connexion
        # connect to postgres for checking database existence
        connectstr = (
            "dbname='postgres' user='"
            + user
            + "' host='"
            + host
            + "' password='"
            + password
            + "'"
        )
        try:
            connpgis = psycopg2.connect(connectstr)
        except psycopg2.OperationalError as e:
            print("Error connecting : ", connectstr, "\n", e)
            return
        pgiscursor = connpgis.cursor()
        connpgis.autocommit = True

        # check if database exists
        sql = "SELECT  datname FROM pg_database WHERE datistemplate = false;"
        pgiscursor.execute(sql)
        rows = pgiscursor.fetchall()
        rows = [elem[0] for elem in rows]
        if dbname.lower() not in rows:
            pgiscursor.execute("CREATE DATABASE " + dbname)
        connpgis.autocommit = True
        pgiscursor.close()
        connpgis.close()

        # connexion to database
        connectstr = "dbname='" + dbname.lower() + "' user='" + user + "' host='" + host
        connectstr += "' password='" + password + "'"
        self.connPGis = psycopg2.connect(connectstr)
        self.PGiscursor = self.connPGis.cursor()
        self.connPGis.autocommit = True

        # check if postgis extension exists
        sql = "Select * FROM pg_extension"
        self.PGiscursor.execute(sql)
        rows = self.PGiscursor.fetchall()
        result = [elem[0] for elem in rows]
        if "postgis" not in result:
            sql = "CREATE EXTENSION postgis"
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
                sql = "DROP SCHEMA " + schema + " CASCADE"
                self.query(sql)
                self.commit()
            except Exception as e:
                print(e)
        sql = "CREATE SCHEMA " + schema
        self.query(sql)
        self.commit()

        # configure search_path
        sql = "SET search_path TO " + schema + ",public"
        self.query(sql)
        self.commit()
        self.disconnect()

    def checkIfPGShcemaExists_old(self, host, dbname, schema, user, password):
        dbexists = False
        schemaexists = False

        # connexion to database
        connectstr = "dbname='" + dbname.lower() + "' user='" + user + "' host='" + host
        connectstr += "' password='" + password + "'"
        try:
            self.connPGis = psycopg2.connect(connectstr)
        except psycopg2.OperationalError as e:
            print("Error connecting : ", connectstr, "\n", e)
            return dbexists, schemaexists

        dbexists = True
        pgiscursor = self.connPGis.cursor()

        sql = "SELECT * FROM pg_namespace"
        # sql = "select schema_name from information_schema.schemata"
        # query = self.query(sql)
        self.PGiscursor.execute(sql)
        rows = self.PGiscursor.fetchall()
        result = [row[1] for row in rows]

        if schema.lower() in result:
            schemaexists = True

        return dbexists, schemaexists

    def query(self, sql):
        with connection.cursor() as c:
            try:
                c.execute(sql)
                rows = c.fetchall()
                return rows
            except django.db.utils.ProgrammingError:
                print("error", sql)

    def query_(self, sql, arguments=[], docommit=True):
        if self.djangocursor is None:
            self.djangocursor = connection.cursor()
        try:
            if self.printsql:
                logging.getLogger("Lamia_unittest").debug("%s", sql)
            self.djangocursor.execute(sql)
            # print(self.PGiscursor.statusmessage )
            if self.djangocursor.statusmessage.split(" ")[0] not in [
                "INSERT",
                "UPDATE",
                "SET",
                "CREATE",
                "ALTER",
                "DROP",
                "BEGIN",
                "COMMIT",
            ]:
                rows = list(self.djangocursor.fetchall())
            else:
                rows = None
            if docommit and self.forcenocommit == False:
                self.commit()
            return rows

        except Exception as e:
            print("error query : ", sql, "\n", e)
            if self.raiseexceptions:
                raise TypeError
            return None

    def vacuum(self):
        raise NotImplementedError

    def commit(self):
        pass
        # self.connPGis.commit()

    def reInitDBase(self):
        raise NotImplementedError

    def isTableSpatial(self, tablename):
        # sql = "SELECT column_name FROM information_schema.columns WHERE table_name  = '" +  str(tablename).lower() + "'"
        # query = self.query(sql)
        # result = [row[0] for row in query]
        result = self.getColumns(tablename.lower())
        if "geom" in result:
            return True
        else:
            return False

    def getTables(self):
        # select * from information_schema.tables where table_schema = 'information_schema'
        # sql = "SELECT name FROM sqlite_master WHERE type='table'"
        sql = f"SELECT table_name  FROM information_schema.tables WHERE table_schema = '{self.pgschema.lower()}'"
        result = self.query(sql)
        return [elem[0] for elem in result]

    def getColumns(self, tablename):
        sql = (
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name  = '{}' AND table_schema = '{}'".format(
                tablename.lower(), self.pgschema.lower()
            )
        )
        query = self.query(sql)
        result = [row[0] for row in query]
        return result

    def getFirstIdColumn(self, tablename):
        # sql = "SELECT column_name FROM information_schema.columns WHERE table_name  = '" +  str(tablename).lower() + "'"
        # query = self.query(sql)
        # result = [row[0] for row in query]
        columns = self.getColumns(tablename.lower())
        for fieldname in columns:
            if "pk_" in fieldname:
                return fieldname

    def getLastPK(self, tablename):
        sql = "SELECT last_value FROM "
        sql += tablename.lower() + "_pk_" + tablename.lower() + "_seq"

        try:
            result = self.query(sql)[0][0]
            return result
        except TypeError as e:
            print("no seq for " + tablename)
            return 0
        except Exception as e:
            print(e, " - no seq for " + tablename)
            return 0

    def _dateVersionConstraintSQL(self, specialdate=None):
        if specialdate is None or specialdate == "now":
            # workingdatemodif = QtCore.QDate.fromString(self.workingdate, 'yyyy-MM-dd').addDays(1).toString('yyyy-MM-dd')
            workingdatemodif = (
                datetime.datetime.now() + datetime.timedelta(days=1)
            ).strftime("%Y-%m-%d")
        else:
            workingdatemodif = (
                QtCore.QDate.fromString(specialdate, "dd/MM/yyyy")
                .addDays(1)
                .toString("yyyy-MM-dd")
            )

        sqlin = " datetimecreation <= " + "'" + workingdatemodif + "'"
        sqlin += " AND CASE WHEN datetimedestruction IS NOT NULL  "
        sqlin += (
            "THEN datetimedestruction > "
            + "'"
            + workingdatemodif
            + "'"
            + " ELSE TRUE END"
        )
        sqlin += " AND lpk_revision_begin <= " + str(self.currentrevision)
        sqlin += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
        sqlin += " lpk_revision_end > " + str(self.currentrevision)
        sqlin += " ELSE TRUE END "

        return sqlin
