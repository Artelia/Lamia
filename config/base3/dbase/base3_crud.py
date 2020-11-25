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
import qgis.core


class LamiaORM(object):
    def __init__(self, dbase):
        super()
        self.dbase = dbase

    def __getitem__(self, key):
        return getattr(self, key)

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

        def __getitem__(self, key):
            "Enable SELECT action on class dict"
            if not isinstance(key, str):
                return AttributeError
            formertable = ""
            sql = f"WITH {self.linkedtables[0]}_temp AS (SELECT * FROM "
            columns = []
            for table in self.linkedtables:
                columns += self.dbase.getColumns(table)

                if formertable:
                    sql += f" INNER JOIN {table} ON {formertable}.lpk_{table} = {table}.pk_{table} "
                else:
                    sql += f" {table} "
                formertable = table
            sql += ")"

            readvalues = list(columns)
            if "geom" in readvalues:
                idx = readvalues.index("geom")
                readvalues[idx] = "ST_AsText(geom)"

            sql += f" SELECT {', '.join(readvalues)} FROM {self.linkedtables[0]}_temp"
            sql += f" WHERE {key}"
            allres = self.dbase.query(sql)
            finalres = []
            if allres:
                for res in allres:
                    finalres += [dict(zip(columns, res))]
            return finalres

        def create(self, featurepk=None):
            if self.dbase.printorm:
                print(f"ORM create {self.__class__.__name__}")
            savedfeaturepk = self.orm._manageFeatureCreationOrUpdate(
                self.__class__.__name__.lower(), featurepk
            )
            return savedfeaturepk

        def update(self, pk, valuesdict):
            if self.dbase.printorm:
                print(
                    f"ORM update {self.__class__.__name__} pk : {pk} -  : {valuesdict}"
                )

            pk = self.orm._manageFeatureCreationOrUpdate(
                self.__class__.__name__.lower(), pk
            )

            if "datetimemodification" in list(self.read(pk).keys()):
                valuesdict[
                    "datetimemodification"
                ] = self.dbase.utils.getCurrentDateTime()

            for k in set(valuesdict.keys()):
                if k.startswith(("pk_", "lpk_")) and not k.startswith("lpk_revision_"):
                    valuesdict.pop(k)
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

                # setstring = ", ".join([k + " = " + v for k, v in filtereddict.items()])
                # if setstring:
                #     sql = f"UPDATE {table} SET {setstring} WHERE pk_{table} = {curpk}"
                #     # print("***", sql)
                #     self.dbase.query(sql)
                if filtereddict:
                    setstring = ", ".join(
                        [
                            k + " = ?" if k != "geom" else k + " =" + v
                            for k, v in filtereddict.items()
                        ]
                    )
                    sql = f"UPDATE {table} SET {setstring} WHERE pk_{table} = {curpk}"
                    argus = [v for k, v in filtereddict.items() if k != "geom"]
                    self.dbase.query(sql, arguments=argus)

                curpk = None
            return pk

        def delete(self, pk):
            if self.dbase.printorm:
                print(f"ORM delete {self.__class__.__name__} pk : {pk}")
            curpk = pk
            valuesdict = {}
            prevval = self.read(curpk)
            for table in self.linkedtables:
                if not curpk:
                    curpk = prevval[f"lpk_{table}"]
                sql = f"DELETE FROM {table} WHERE pk_{table} = {curpk}"
                self.dbase.query(sql)
                curpk = None

        def read(self, pk):
            curpk = pk
            valuesdict = {}
            for table in self.linkedtables:
                if not curpk:
                    curpk = valuesdict[f"lpk_{table}"]
                columns = self.dbase.getColumns(table)
                readvalues = list(columns)
                if "geom" in readvalues:
                    idx = readvalues.index("geom")
                    readvalues[idx] = "ST_AsText(geom)"
                sql = f"SELECT {', '.join(readvalues)} FROM {table} WHERE pk_{table} = {curpk}"
                res = self.dbase.query(sql)
                if res:
                    valuesdict = {**valuesdict, **dict(zip(columns, res[0]))}
                else:
                    return None
                curpk = None
            return valuesdict

        def _cleanValues(self, valdict):
            for k, val in valdict.items():
                # resulttemp = None
                # if isinstance(val, str) or isinstance(val, unicode):
                # if isinstance(val, str) and k != "geom":
                #     if val != "":
                #         if val == "NULL":
                #             resulttemp = val
                #         else:
                #             resultstring = val
                #             if "'" in resultstring:
                #                 resultstring = "''".join(resultstring.split("'"))
                #             resulttemp = "'" + resultstring + "'"
                #     else:
                #         resulttemp = "NULL"
                if k == "geom":
                    resulttemp = f"ST_GeomFromText('{val}',{self.dbase.crsnumber})"
                    valdict[k] = resulttemp

                if self.dbase.utils.isAttributeNull(val):
                    valdict[k] = None
                # elif val is None:
                #     resulttemp = "NULL"
                # else:
                #     resulttemp = str(val)

                # valdict[k] = resulttemp

    # *********** ASSETS ********************

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

    class Observation(AbstractTableOrm):
        def create(self, featurepk=None):
            pkobs = super().create(featurepk)
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.update(pkobs, {"datetimeobservation": datecreation})
            return pkobs

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

                if featlastrevision != self.dbase.maxrevision:  # new version feature
                    # print("*********** new feat vers")
                    pktoreturn = self._createNewFeatureVersion(tablename, featurepk)
                    # pktoreturn = self.dbase.getLastPK(tablename)
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
                if itertablename.startswith("tc"):
                    parenttablename = itertablename

                if parenttablename is not None:

                    if not (itertablename[-4:] == "data" or itertablename[0:2] == "tc"):
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
                    elif itertablename[-4:] == "data":
                        listofields = ["lpk_" + parenttablename.lower()]
                        listofrawvalues = [parenttablepk]
                    else:
                        listofields = ["lpk_revision_begin"]
                        listofrawvalues = [self.dbase.maxrevision]

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
        formerval = None
        # first be sure

        formerval = self[dbname].read(rawpk)
        pkobjet = None
        revbegin = None
        if "pk_object" in list(formerval.keys()):
            pkobjet = formerval["pk_object"]
        if "lpk_revision_begin" in list(formerval.keys()):
            revbegin = formerval["lpk_revision_begin"]

        # pkobjet, revbegin = formerval["pk_object"], formerval["lpk_revision_begin"]
        # pkobjet, revbegin = self.dbase.getValuesFromPk(
        #     dbname + "_qgis", ["pk_object", "lpk_revision_begin"], rawpk
        # )

        if revbegin == self.dbase.maxrevision:
            return

        # if revbegin < self.dbase.maxrevision:
        # first close object
        # if self.dbase.base3version:
        # sql = self.dbase.createSetValueSentence(
        #     "UPDATE", "object", ["lpk_revision_end"], [self.dbase.maxrevision]
        # )
        # sql += " WHERE pk_object = " + str(pkobjet)
        # self.dbase.query(sql)
        # self["object"].update(pkobjet, {"lpk_revision_end": self.dbase.maxrevision})
        if pkobjet:
            sql = f"UPDATE object SET lpk_revision_end = {self.dbase.maxrevision} WHERE pk_object = {pkobjet}"
            self.dbase.query(sql)
        else:  # tc table
            sql = f"UPDATE {dbname} SET lpk_revision_end = {self.dbase.maxrevision} WHERE pk_{dbname} = {rawpk}"
            self.dbase.query(sql)
        # then clone parents

        newpk = self[dbname].create()
        newval = dict(formerval)
        newval["lpk_revision_begin"], newval["lpk_revision_end"] = (
            self.dbase.maxrevision,
            None,
        )
        self[dbname].update(newpk, newval)

        return newpk

        # ***
        # parenttables = self.dbase.getParentTable(dbname)[::-1] + [dbname]
        # # get pkparents
        # pknames = ["pk_" + parenttablename.lower() for parenttablename in parenttables]
        # parentspk = self.dbase.getValuesFromPk(dbname.lower() + "_qgis", pknames, rawpk)

        # lastpk = []
        # for i, tablename in enumerate(parenttables):
        #     pkfields = []
        #     nonpkfields = []
        #     for fields in self.dbase.getColumns(tablename):
        #         if fields[0:3] == "pk_" or fields[0:4] == "lpk_":
        #             pkfields.append(fields)
        #         elif fields == "geom":
        #             nonpkfields.append("ST_AsText(geom)")
        #         else:
        #             nonpkfields.append(fields)
        #     values = self.dbase.getValuesFromPk(tablename, nonpkfields, parentspk[i])

        #     nonpkfields = ["geom" if x == "ST_AsText(geom)" else x for x in nonpkfields]
        #     sql = self.dbase.createSetValueSentence(
        #         "INSERT", tablename, nonpkfields, list(values)
        #     )
        #     self.dbase.query(sql)
        #     lastpk.append(self.dbase.getLastPK(tablename))
        #     fieldstoupdate = []
        #     valuestoupdate = []
        #     if "lpk_revision_begin" in pkfields:
        #         fieldstoupdate += ["lpk_revision_begin", "lpk_revision_end"]
        #         valuestoupdate += [self.dbase.maxrevision, None]
        #     if "datetimemodification" in nonpkfields:
        #         datemodif = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #         fieldstoupdate += ["datetimemodification"]
        #         valuestoupdate += [datemodif]
        #     if i > 0 and "lpk_" + parenttables[i - 1].lower() in pkfields:
        #         fieldstoupdate += ["lpk_" + parenttables[i - 1].lower()]
        #         valuestoupdate += [lastpk[i - 1]]

        #     sql = self.dbase.createSetValueSentence(
        #         "UPDATE", tablename, fieldstoupdate, valuestoupdate
        #     )
        #     sql += " WHERE pk_" + tablename.lower() + " = " + str(lastpk[i])
        #     self.dbase.query(sql)

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
                + str(self.dbase.maxrevision)
                + ",'"
                + datecreation
                + "','"
                + datecreation
                + "' )"
            )
            self.dbase.query(sql, docommit=docommit)
            pkobjet = self.getLastPK("Objet")
        return pkobjet
