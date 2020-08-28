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

import pandas as pd
import logging, threading


class IDChooser:
    def __init__(self, **kwargs):
        self.toolwidget = kwargs.get("toolwidget", None)
        self.dbase = kwargs.get("dbase", None)
        self.ids = pd.DataFrame()

    def loadIds(self):
        """

        toolwidget : {DBASETABLENAME:str ,CHOOSERTREEWDGSPEC:...,PARENTJOIN:dict, TABLEFILTERFIELD:...
        parentWidget:{DBASETABLENAME:str, currentFeaturePK:int  }

        """

        debug = False
        # CHOOSERTREEWDG_COLSHOW = ['datetimeobservation']
        dbnamelower = self.toolwidget.DBASETABLENAME.lower()
        fields_to_request = ["pk_" + dbnamelower]
        pandascolumns = ["pk"]
        # if not 'onlyoneparenttable' in self.toolwidget.dbase.dbasetables[self.toolwidget.DBASETABLENAME].keys():
        if not dbnamelower[-4:] == "data":
            fields_to_request += ["id_" + dbnamelower]
            pandascolumns += ["id"]
        else:
            fields_to_request += ["pk_" + dbnamelower]
            pandascolumns += ["pk2"]
        """
        if (hasattr(self.toolwidget, 'CHOOSERTREEWDG_COLSHOW') 
                and len(self.toolwidget.CHOOSERTREEWDG_COLSHOW) > 0 ):
            fields_to_request += self.toolwidget.CHOOSERTREEWDG_COLSHOW
            pandascolumns += self.toolwidget.CHOOSERTREEWDG_COLSHOW
        """
        if (
            hasattr(self.toolwidget, "CHOOSERTREEWDGSPEC")
            and "colshow" in self.toolwidget.CHOOSERTREEWDGSPEC.keys()
        ):
            # fields_to_request += (
            #     self.toolwidget.DBASETABLENAME
            #     + "_now."
            #     + self.toolwidget.CHOOSERTREEWDGSPEC["colshow"]
            # )
            fields_to_request += [
                self.toolwidget.DBASETABLENAME + "_now." + fldname
                for fldname in self.toolwidget.CHOOSERTREEWDGSPEC["colshow"]
            ]

            pandascolumns += self.toolwidget.CHOOSERTREEWDGSPEC["colshow"]

        sql = "SELECT {} FROM {}_now ".format(
            ", ".join(fields_to_request), self.toolwidget.DBASETABLENAME
        )

        if (
            self.toolwidget.parentWidget is not None
            and self.toolwidget.parentWidget.currentFeaturePK is not None
        ):
            parenttablename = self.toolwidget.parentWidget.DBASETABLENAME
            if (
                self.toolwidget.PARENTJOIN
                and parenttablename in self.toolwidget.PARENTJOIN.keys()
            ):
                joindict = self.toolwidget.PARENTJOIN[parenttablename]
                thistablename = self.toolwidget.DBASETABLENAME
                if joindict["tctable"] is None:
                    if parenttablename != thistablename:
                        sql += "JOIN {}_now ON {} = {}" " WHERE pk_{} = {}".format(
                            parenttablename,
                            parenttablename + "_now." + joindict["colparent"],
                            thistablename + "_now." + joindict["colthistable"],
                            parenttablename.lower(),
                            self.toolwidget.parentWidget.currentFeaturePK,
                        )
                    else:
                        valsearched = self.dbase.getValuesFromPk(
                            thistablename + "_qgis",
                            joindict["colparent"],
                            self.toolwidget.parentWidget.currentFeaturePK,
                        )
                        if valsearched is not None:
                            sql += " WHERE {} = {}".format(
                                joindict["colthistable"], valsearched
                            )
                            # print('***', sql)
                        else:
                            sql = None
                else:

                    sql += (
                        "INNER JOIN {} ON {} = {} "
                        "INNER JOIN {}_now ON {} = {} "
                        "WHERE pk_{} = {} ".format(
                            joindict["tctable"],
                            thistablename + "_now." + joindict["colthistable"],
                            joindict["tctable"] + "." + joindict["tctablecolthistable"],
                            parenttablename,
                            joindict["tctable"] + "." + joindict["tctablecolparent"],
                            parenttablename + "_now." + joindict["colparent"],
                            parenttablename.lower(),
                            self.toolwidget.parentWidget.currentFeaturePK,
                        )
                    )

            if sql is not None:
                sql = self.dbase.sqlNow(sql)
            # query = self.dbase.query(sql)
            # self.ids = pd.DataFrame(query, columns = ['pk', 'id'])
            # print(self.ids)
            # return query
        elif self.toolwidget.parentWidget is not None:
            sql = None
        else:
            sql = self.dbase.sqlNow(sql)

        if sql:
            if (
                hasattr(self.toolwidget, "TABLEFILTERFIELD")
                and self.toolwidget.TABLEFILTERFIELD is not None
            ):
                for fieldname, fieldvalue in self.toolwidget.TABLEFILTERFIELD.items():
                    if isinstance(fieldvalue, str):
                        fieldvalue = "'" + fieldvalue + "'"
                    sqlsplitted = self.dbase.utils.splitSQLSelectFromWhereOrderby(sql)
                    if "WHERE" in sqlsplitted.keys():
                        sql += " AND {} = {}".format(fieldname, fieldvalue)
                    else:
                        sql += " WHERE  {} = {}".format(fieldname, fieldvalue)
            if debug:
                logging.getLogger("Lamia_unittest").debug("sql : %s", sql)
            if debug:
                logging.getLogger("Lamia_unittest").debug(
                    "search : %s", self.dbase.query("show search_path")
                )

            query = self.dbase.query(sql)
            print(query)
            self.ids = pd.DataFrame(query, columns=pandascolumns)
        else:
            self.ids = pd.DataFrame(columns=pandascolumns)

        # * sorting ids
        if (
            hasattr(self.toolwidget, "CHOOSERTREEWDGSPEC")
            and "sort" in self.toolwidget.CHOOSERTREEWDGSPEC.keys()
        ):
            sortcolumn = self.toolwidget.CHOOSERTREEWDGSPEC["sort"][0]
            if self.toolwidget.CHOOSERTREEWDGSPEC["sort"][1] == "ASC":
                ascending = True
            else:
                ascending = False
        elif "id" in pandascolumns:
            sortcolumn = "id"
            ascending = True
        else:
            sortcolumn = "pk"
            ascending = True
        self.ids.sort_values(sortcolumn, ascending=ascending, inplace=True)
        self.ids.reset_index(drop=True, inplace=True)

        if debug:
            logging.getLogger("Lamia_unittest").debug("ids : %s", self.ids)

        return self.ids

