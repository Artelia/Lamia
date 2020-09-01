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

from .postgisdbaseparser import *


class DjangoDBaseParser(PostGisDBaseParser):

    TYPE = "django"

    def __init__(self, parserfactory, messageinstance):
        super(PostGisDBaseParser, self).__init__(parserfactory, messageinstance)


    def query(self, sql, arguments=[], docommit=True):
        with self.connPGis.cursor() as cursor:
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
    
