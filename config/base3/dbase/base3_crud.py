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

import datetime
import inspect


class LamiaORM(object):
    def __init__(self, dbase):
        self.dbase = dbase

    def __getattr__(self, name):
        if name.title() in dir(self):
            newcls = getattr(self, name.title())(self.dbase, self)
            self.__setattr__(name, newcls)
            return newcls
        elif name in self.dbase.dbasetables.keys():
            newcls = type(name.title(), (self.AbstractTableOrm,), {})(self.dbase, self)
            self.__setattr__(name, newcls)
            return newcls
        else:
            return AttributeError

    class AbstractTableOrm(object):
        def __init__(self, dbaset=None, triggerd=None):
            # def __init__(self):
            self.orm = triggerd
            self.dbase = dbaset
            self.linkedtables = [
                self.__class__.__name__.lower()
            ] + self.dbase.getParentTable(self.__class__.__name__.lower())

        def create(self, featurepk=None):
            savedfeaturepk = self.orm._manageFeatureCreationOrUpdate(
                self.__class__.__name__.lower(), featurepk
            )
            return savedfeaturepk

        def update(self, pk, valuesdict):
            for key in set(valuesdict.keys()):
                if key.startswith(("pk_", "lpk_")):
                    valuesdict.pop(key)
            curpk = pk
            actualvalues = self.read(pk)  # get lpk values
            for table in self.linkedtables:
                if not curpk:
                    curpk = actualvalues[f"lpk_{table}"]
                columns = self.dbase.getColumns(table)
                matchingcol = set(columns).intersection(set(valuesdict.keys()))
                filtereddict = dict(
                    zip(matchingcol, [valuesdict[val] for val in matchingcol])
                )

                self._cleanValues(filtereddict)

                setstring = ", ".join([k + " = " + v for k, v in filtereddict.items()])
                if setstring:
                    sql = f"UPDATE {table} SET {setstring} WHERE pk_{table} = {curpk}"
                    self.dbase.query(sql)
                curpk = None

        def delete(self, pk):
            curpk = pk
            for table in self.linkedtables:
                if not curpk:
                    curpk = valuesdict[f"lpk_{table}"]
                sql = f"DELETE FROM {table} WHERE pk_{table} = {curpk}"
                self.dbase.query(sql)

        def read(self, pk):
            curpk = pk
            valuesdict = {}
            for table in self.linkedtables:
                if not curpk:
                    curpk = valuesdict[f"lpk_{table}"]
                columns = self.dbase.getColumns(table)
                sql = f"SELECT * FROM {table} WHERE pk_{table} = {curpk}"
                res = self.dbase.query(sql)
                valuesdict = {**valuesdict, **dict(zip(columns, res[0]))}
                curpk = None
            return valuesdict

        def _cleanValues(self, valdict):
            for k, val in valdict.items():
                # if isinstance(val, str) or isinstance(val, unicode):
                if isinstance(val, str):
                    if val != "":
                        if val == "NULL":
                            resulttemp = val
                        else:
                            resultstring = val
                            if "'" in resultstring:
                                resultstring = "''".join(resultstring.split("'"))
                            resulttemp = "'" + resultstring + "'"
                    else:
                        resulttemp = "NULL"
                elif val is None:
                    resulttemp = "NULL"
                else:
                    resulttemp = str(val)

                valdict[k] = resulttemp

    # *********** ASSETS ********************

    class Node(AbstractTableOrm):
        def create(self, pk=None):
            savedfeaturepk = super().create(pk)
            print("created")
            # deficiency creation
            pkdef = self.orm.deficiency.create()
            nodegeom = self.read(savedfeaturepk)["geom"]
            self.orm.deficiency.update(
                pkdef, {"lid_descriptionsystem": 2, "geom": nodegeom}
            )
            return savedfeaturepk

        def update(self, pk, valuesdict):
            super().update(pk, valuesdict)
            nodeval = self.orm.node.read(pk)
            nodedessys, nodegeom = nodeval["id_descriptionsystem"], nodeval["geom"]
            sql = f"SELECT pk_deficiency FROM deficiency_qgis WHERE lid_descriptionsystem = {nodedessys}\
                    AND lpk_revision_end IS NULL"
            defpks = self.dbase.query(sql)
            for defpk in defpks:
                self.orm.deficiency.update(defpk, {"geom": nodegeom})

    # class Surface(abstracttrigger):
    #     pass

    # class Facility(abstracttrigger):
    #     pass

    # class Equipment(abstracttrigger):
    #     pass

    # ********* RESOURCES***********

    # class Media(abstracttrigger):
    #     pass

    # class Rasters(abstracttrigger):
    #     pass

    # class Topography(abstracttrigger):
    #     pass

    # class Graph(abstracttrigger):
    #     pass

    # ********* MANAGEMENT***********

    # class Actor(abstracttrigger):
    #     pass

    # class Geoarea(abstracttrigger):
    #     pass

    # ************* STATE *************

    # class Deficiency(abstracttrigger):
    #     pass

    # class Observation(abstracttrigger):
    #     pass

    def _manageFeatureCreationOrUpdate(self, tablename, featurepk=None):
        """
        Called by saveFeature - Manage versioning
        return pk of object
        """

        if featurepk is not None:  # existing feature saved
            if "lpk_revision_begin" in self.dbase.getColumns(tablename + "_qgis"):
                # featlastrevision = self.dbase.getValuesFromPk(
                #     tablename + "_qgis", "lpk_revision_begin", featurepk
                # )
                featlastrevision = getattr(self, tablename).read(featurepk)[
                    "lpk_revision_begin"
                ]

                if featlastrevision != self.maxrevision:  # new version feature
                    # print("*********** new feat vers")
                    self._createNewFeatureVersion(tablename, featurepk)
                    pktoreturn = self.dbase.getLastPK(tablename)
                else:  # simple feature update
                    pktoreturn = featurepk
            else:
                pktoreturn = featurepk

        else:  # feature creation
            pktoreturn = self._createNewFeature(tablename)

        return pktoreturn

    def _createNewFeature(self, tablename):
        # parenttables = [tablename] + self.dbase.getParentTable(tablename)
        parenttables = getattr(self, tablename).linkedtables
        parenttablename = None
        for itertablename in parenttables[::-1]:
            if itertablename in ["Objet", "object"]:
                parenttablepk = self._createNewObjet()
                parenttablename = itertablename
            else:
                tablepk = self.dbase.getLastPK(itertablename) + 1

                if parenttablename is not None:
                    # if not 'onlyoneparenttable' in self.dbasetables[itertablename].keys():
                    if not itertablename[-4:] == "data":
                        maxid = (
                            self.dbase.getmaxColumnValue(
                                itertablename, "id_" + itertablename.lower()
                            )
                            + 1
                        )
                        listofields = [
                            "id_" + itertablename.lower(),
                            "lpk_" + parenttablename.lower(),
                        ]
                        listofrawvalues = [maxid, parenttablepk]
                    else:
                        listofields = ["lpk_" + parenttablename.lower()]
                        listofrawvalues = [parenttablepk]
                    sql = self.dbase.createSetValueSentence(
                        type="INSERT",
                        tablename=itertablename,
                        listoffields=listofields,
                        listofrawvalues=listofrawvalues,
                    )
                    self.dbase.query(sql)
                parenttablename = itertablename
                parenttablepk = self.dbase.getLastPK(itertablename)

        return self.dbase.getLastPK(tablename)

    def _createNewFeatureVersion(self, dbname, rawpk):

        # first be sure
        if self.dbase.base3version:
            pkobjet, revbegin = self.dbase.getValuesFromPk(
                dbname + "_qgis", ["pk_object", "lpk_revision_begin"], rawpk
            )
        else:
            pkobjet, revbegin = self.dbase.getValuesFromPk(
                dbname + "_qgis", ["pk_objet", "lpk_revision_begin"], rawpk
            )
        if revbegin < self.maxrevision:
            # first close object
            if self.dbase.base3version:
                sql = self.dbase.createSetValueSentence(
                    "UPDATE", "object", ["lpk_revision_end"], [self.maxrevision]
                )
                sql += " WHERE pk_object = " + str(pkobjet)
                self.dbase.query(sql)
            else:
                sql = self.dbase.createSetValueSentence(
                    "UPDATE", "Objet", ["lpk_revision_end"], [self.maxrevision]
                )
                sql += " WHERE pk_object = " + str(pkobjet)
                self.dbase.query(sql)

            # then clone parents
            parenttables = self.dbase.getParentTable(dbname)[::-1] + [dbname]
            # get pkparents
            pknames = [
                "pk_" + parenttablename.lower() for parenttablename in parenttables
            ]
            parentspk = self.dbase.getValuesFromPk(
                dbname.lower() + "_qgis", pknames, rawpk
            )

            lastpk = []
            for i, tablename in enumerate(parenttables):
                pkfields = []
                nonpkfields = []
                for fields in self.dbase.getColumns(tablename):
                    if fields[0:3] == "pk_" or fields[0:4] == "lpk_":
                        pkfields.append(fields)
                    elif fields == "geom":
                        nonpkfields.append("ST_AsText(geom)")
                    else:
                        nonpkfields.append(fields)
                values = self.dbase.getValuesFromPk(
                    tablename, nonpkfields, parentspk[i]
                )

                nonpkfields = [
                    "geom" if x == "ST_AsText(geom)" else x for x in nonpkfields
                ]
                sql = self.dbase.createSetValueSentence(
                    "INSERT", tablename, nonpkfields, list(values)
                )
                self.dbase.query(sql)
                lastpk.append(self.dbase.getLastPK(tablename))
                fieldstoupdate = []
                valuestoupdate = []
                if "lpk_revision_begin" in pkfields:
                    fieldstoupdate += ["lpk_revision_begin", "lpk_revision_end"]
                    valuestoupdate += [self.maxrevision, None]
                if "datetimemodification" in nonpkfields:
                    datemodif = str(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
                    fieldstoupdate += ["datetimemodification"]
                    valuestoupdate += [datemodif]
                if i > 0 and "lpk_" + parenttables[i - 1].lower() in pkfields:
                    fieldstoupdate += ["lpk_" + parenttables[i - 1].lower()]
                    valuestoupdate += [lastpk[i - 1]]

                sql = self.dbase.createSetValueSentence(
                    "UPDATE", tablename, fieldstoupdate, valuestoupdate
                )
                sql += " WHERE pk_" + tablename.lower() + " = " + str(lastpk[i])
                self.dbase.query(sql)

    def _createNewObjet(self, docommit=True):
        datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # lastobjetid = self.getLastId('Objet') + 1
        if self.dbase.base3version:
            lastobjetid = self.dbase.getmaxColumnValue("object", "id_object")
            sql = "INSERT INTO object (id_object, lpk_revision_begin, datetimecreation, datetimemodification ) "
            sql += (
                "VALUES("
                + str(lastobjetid + 1)
                + ","
                + str(self.dbase.maxrevision)
                + ",'"
                + datecreation
                + "','"
                + datecreation
                + "' )"
            )
            self.dbase.query(sql, docommit=docommit)
            pkobjet = self.dbase.getLastPK("object")
        else:
            lastobjetid = self.dbase.getmaxColumnValue("Objet", "id_objet")
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation, datetimemodification ) "
            sql += (
                "VALUES("
                + str(lastobjetid + 1)
                + ","
                + str(self.maxrevision)
                + ",'"
                + datecreation
                + "','"
                + datecreation
                + "' )"
            )
            self.dbase.query(sql, docommit=docommit)
            pkobjet = self.getLastPK("Objet")
        return pkobjet
