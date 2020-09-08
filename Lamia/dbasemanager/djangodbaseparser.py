# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from psycopg2.pool import ThreadedConnectionPool

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

from .postgisdbaseparser import *


class DjangoDBaseParser(PostGisDBaseParser):

    TYPE = "django"

    def __init__(self, parserfactory, messageinstance):
        super(PostGisDBaseParser, self).__init__(parserfactory, messageinstance)


class DjangoDBaseParser(PostGisDBaseParser):

    TYPE = "django"

    def __init__(self, parserfactory, messageinstance):
        super(PostGisDBaseParser, self).__init__(parserfactory, messageinstance)

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
        self.dbasetype = "postgis"
        self.pgport = port
        self.pghost = host
        self.pgdb = dbname
        self.pgschema = schema
        self.pguser = user
        self.pgpassword = password

        # connexion
        # connect to postgres for checking database existence
        # connectstr = (
        #     "dbname='postgres' user='"
        #     + user
        #     + "' host='"
        #     + host
        #     + "' password='"
        #     + password
        #     + "'"
        # )

        self.threaded_postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(
            minconn=1,
            maxconn=5,
            user=user,
            password=password,
            host=host,
            port=port,
            database=dbname,
            options="-c search_path=" + schema + ",public",
            application_name='lamiawebservice'
        )

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

        # # searchpath
        # sql = "SET search_path TO " + self.pgschema.lower() + ", public;"
        # self.query(sql)
        # self.commit()

    def query(self, sql, arguments=[], docommit=True):
        ps_connection = self.threaded_postgreSQL_pool.getconn()
        # with self.connPGis.cursor() as cursor:
        with ps_connection.cursor() as cursor:
            try:
                if self.printsql:
                    logging.getLogger("Lamia_unittest").debug("%s", sql)
                cursor.execute(sql)
                # print(self.PGiscursor.statusmessage )
                if cursor.statusmessage.split(" ")[0] not in [
                    "INSERT",
                    "UPDATE",
                    "SET",
                    "CREATE",
                    "ALTER",
                    "DROP",
                    "BEGIN",
                    "COMMIT",
                ]:
                    rows = list(cursor.fetchall())
                else:
                    rows = None
                if docommit and self.forcenocommit == False:
                    self.commit()
                return rows

            except psycopg2.ProgrammingError as e:
                print("error query : ", sql, "\n", e, cursor.statusmessage)
                if self.raiseexceptions:
                    raise TypeError
                return None
            except (psycopg2.DataError, psycopg2.InternalError) as e:
                print("error query : ", sql, "\n", e)
                if self.raiseexceptions:
                    raise TypeError
                return None
            finally:
                self.threaded_postgreSQL_pool.putconn(ps_connection)

    def commit(self):
        pass
