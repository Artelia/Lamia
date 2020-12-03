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

import datetime, os, sys, platform
import logging, json

# from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

# from . import dbaseutils


class DBaseOfflineManager:

    # typeimport : append : "simply" append to self.dbase the datas of dbaseparserfrom
    # typeimport : update : dbaseparserfrom was created for offline use, now reimport modified data in self.dbase
    # typeimport : copy : copy dbase, keeping id values - used when pull of offline mode
    TYPEIMPORT = {"append": 0, "update": 1, "copy": -1}

    RESOLVECONFLICTTYPE = "manual"  # manual auto
    RESOLVECONFLICTCHOICE = "import"  # import main

    WINOFFLINEDIR = os.path.normpath("C://Users//Public//Documents//lamia")

    def __init__(self, dbase):
        self.dbase = dbase

    def addDBase(self, **kwargs):
        if "slfile" in kwargs.keys():
            dbaseparserfact = self.dbase.parserfactory.__class__
            importparser = dbaseparserfact(
                "spatialite", self.dbase.messageinstance
            ).getDbaseParser()
        elif "host" in kwargs.keys():
            dbaseparserfact = self.dbase.parserfactory.__class__
            importparser = dbaseparserfact(
                "postgis", self.dbase.messageinstance
            ).getDbaseParser()
        importparser.loadDBase(**kwargs)
        self.importDBase(
            importparser,
            typeimport="append",
            createnewversion=False,
            ressourcesimport="Full",
        )

    def pullDBase(self, pulledpath):

        # create pull dir
        if pulledpath is None:
            if platform.system() == "Linux":
                pass
            elif platform.system() == "Windows":
                lamiadir = self.WINOFFLINEDIR
            # lamiadir = os.path.join(importdir, "lamia")
            if not os.path.isdir(lamiadir):
                os.mkdir(lamiadir)
            dbname = self.dbase.getDBName()
            dbdir = os.path.join(lamiadir, dbname)
            if not os.path.isdir(dbdir):
                os.mkdir(dbdir)
            else:
                self.dbase.messageinstance.showErrorMessage(
                    f"Il y a déjà une copie locale de la base - Supprimez la : {dbdir}"
                )
                return

            lamiafilepath = os.path.join(dbdir, dbname + ".sqlite")
        else:
            lamiafilepath = pulledpath

        self.dbase.messageinstance.showNormalMessage(
            f"Creation de la copie locale : {os.path.normpath(lamiafilepath)}"
        )

        # create dbase
        dbaseparserfact = self.dbase.parserfactory.__class__
        exportparser = dbaseparserfact(
            "spatialite", self.dbase.messageinstance
        ).getDbaseParser()
        # exportparser = DBaseParserFactory(
        #     "spatialite", connector=self.dbase.messageinstance
        # ).getDbaseParser()

        exportparser.createDBase(
            crs=self.dbase.crsnumber,
            worktype=self.dbase.worktype,
            dbaseressourcesdirectory=None,
            variante=None,
            slfile=lamiafilepath,
        )
        exportparser.loadDBase(slfile=lamiafilepath)

        # make import in new dbase
        # but first verify thumbnailed images
        self._verifyColumnThumbnailedImage(self.dbase)

        exportparser.dbaseofflinemanager.importDBase(
            self.dbase,
            typeimport="copy",
            createnewversion=False,
            ressourcesimport="thumbnails",
        )

        # datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        datecreation = self.dbase.utils.getCurrentDateTime()
        if self.dbase.base3version:
            sql = "INSERT INTO revision(datetimerevision, comment)  "
            sql += " VALUES('" + datecreation + "','travail horsligne')"
            exportparser.query(sql)
        else:
            sql = "INSERT INTO Revision(datetimerevision, commentaire)  "
            sql += " VALUES('" + datecreation + "','travail horsligne')"
            exportparser.query(sql)

        # finaly create a file keeping in memory the parent dbase
        tempconffilepath = os.path.join(
            exportparser.dbaseressourcesdirectory, "config", ".offlinemode"
        )
        with open(tempconffilepath, "w", encoding="utf-8") as outfile:
            json.dump(self.dbase.connectconf, outfile, ensure_ascii=False, indent=4)

        self.dbase.messageinstance.showNormalMessage(
            f"Creation de la copie locale terminée: {os.path.normpath(lamiafilepath)}"
        )

        return lamiafilepath

    def pushDBase(self):
        tempconffilepath = os.path.join(
            self.dbase.dbaseressourcesdirectory, "config", ".offlinemode"
        )
        if not os.path.isfile(tempconffilepath):
            self.dbase.messageinstance.showErrorMessage(
                "La base ne provient pas d'une version locale \nou a déjà été reversée"
            )
            return

        with open(tempconffilepath) as outfile:
            connectconf = json.load(outfile)

        self.dbase.messageinstance.showNormalMessage(
            f"Synchronisation avec la base mère : {connectconf}"
        )

        dbaseparserfact = self.dbase.parserfactory.__class__
        if "slfile" in connectconf.keys():
            parentdbase = dbaseparserfact(
                "spatialite", self.dbase.messageinstance
            ).getDbaseParser()
        elif "pgschema" in connectconf.keys():
            parentdbase = dbaseparserfact(
                "postgis", self.dbase.messageinstance
            ).getDbaseParser()

        parentdbase.loadDBase(**connectconf)
        parentdbase.dbaseofflinemanager.importDBase(self.dbase, typeimport="update")

        os.remove(tempconffilepath)

        self.dbase.messageinstance.showErrorMessage(
            "Synchronisation terminée - Attention : il faut recréer une copie locale pour prendre en compte les changements à venir"
        )

    def importDBase(
        self,
        dbaseparserfrom,
        typeimport="append",
        createnewversion=True,
        ressourcesimport="Full",
        dobackup=True,
    ):
        """
        typeimport : append : "simply" append to self.dbase the datas of dbaseparserfrom
        typeimport : update : dbaseparserfrom was created for offline use, now reimport modified data in self.dbase
        typeimport : copy : copy dbase, keeping id values - used when pull of offline mode

        create new version : create new vrsion before import

        ressourcesimport : Full / thumbnails / none  : import all ressources files, or just thumbnails, or None
        """
        debug = True

        """
        if isinstance(typeimport,str):
            # offlineimport = TYPEIMPORT[typeimport]
            typeimport = TYPEIMPORT[typeimport]
        """

        # ****************** init
        self.backupBase()
        maxprogress = len(self.dbase.dbasetables.keys())
        self.dbase.messageinstance.createProgressBar(
            "Import des donnees...", maxprogress
        )
        confdatas = {}
        # confdatas['offlineimport'] = offlineimport
        confdatas["typeimport"] = typeimport
        dictconflicts = {}  # for offlineimport

        # add version in Main
        if createnewversion:
            datedebutimport = str(
                (datetime.datetime.now() - datetime.timedelta(seconds=2)).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )
            if typeimport == "update":
                comment = "import_from_offline"
            else:
                comment = "import"
            if self.dbase.base3version:
                sql = "INSERT INTO revision(datetimerevision, comment) "
                sql += " VALUES('" + str(datedebutimport) + "', '" + comment + "')"
            else:
                sql = "INSERT INTO Revision(datetimerevision, commentaire) "
                sql += " VALUES('" + str(datedebutimport) + "', '" + comment + "')"
            self.dbase.query(sql)

        # import db creation date
        datetravailhorsligne = None
        dateofflinedbasecreation = None

        importedobjetids = []
        # ************** search conflict if mode = 'update'
        # if offlineimport:
        if typeimport == "update":
            (
                dictconflicts,
                importedobjetids,
                dateofflinedbasecreation,
            ) = self._resolveConflict(dbaseparserfrom)
        if debug:
            logging.getLogger("Lamiaoffline").debug("dictconflicts %s", dictconflicts)

        # **************** start importdbase
        counter = 0
        for order in range(1, 10):
            for tablename in self.dbase.dbasetables:
                if self.dbase.dbasetables[tablename]["order"] == order:
                    counter += 1
                    if debug:
                        logging.getLogger("Lamiaoffline").debug(
                            " ******************* %s *********  ", tablename
                        )
                    self.dbase.messageinstance.updateProgressBar(counter)

                    # if tablename == "graphdata":
                    #     print("ok")

                    # * confdatas initialization
                    confdatas[tablename.lower()] = {}
                    dbconfdatas = confdatas[tablename.lower()]
                    # import dict : {tablename : {...{idfrom : idto} ...} }
                    dbconfdatas["importdictid"] = {}
                    # import dict : {tablename : {...{pkfrom : pkto} ...} }
                    dbconfdatas["importdictpk"] = {}
                    # import dict : {tablename : [pk1, pk2,..] }
                    dbconfdatas["importdictdeletedpk"] = []
                    # conflictobjetids dict : {..., idobjet:{fields : [], importvalue:[], mainvalue:[]},... }
                    dbconfdatas["conflictobjetids"] = {}

                    (
                        pkidfields,
                        noncriticalfields,
                    ) = self._getCriticalandNonCriticalFields(tablename)
                    dbconfdatas["pkidfields"], dbconfdatas["noncriticalfields"] = (
                        pkidfields,
                        noncriticalfields,
                    )

                    noncriticalresults, pkidresults = self._getValuesFromImportedTable(
                        typeimport,
                        dbaseparserfrom,
                        tablename,
                        pkidfields,
                        noncriticalfields,
                    )

                    self.dbase.beginTransaction()

                    for i, pkidresult in enumerate(pkidresults):
                        noncriticalresult = noncriticalresults[i]

                        if tablename[0:2].lower() != "tc":
                            index_pk_tablename = dbconfdatas["pkidfields"].index(
                                "pk_" + tablename.lower()
                            )
                            pk_tablename = pkidresult[index_pk_tablename]
                            if self.dbase.base3version:
                                if tablename.lower().endswith("data"):
                                    id_objet = None

                                else:
                                    (
                                        id_objet,
                                        rev_begin,
                                        rev_end,
                                        datetimedes,
                                    ) = dbaseparserfrom.getValuesFromPk(
                                        tablename + "_qgis",
                                        [
                                            "id_object",
                                            "lpk_revision_begin",
                                            "lpk_revision_end",
                                            "datetimedestruction",
                                        ],
                                        pk_tablename,
                                    )
                            else:
                                (
                                    id_objet,
                                    rev_begin,
                                    rev_end,
                                    datetimedes,
                                ) = dbaseparserfrom.getValuesFromPk(
                                    tablename + "_qgis",
                                    [
                                        "id_objet",
                                        "lpk_revision_begin",
                                        "lpk_revision_end",
                                        "datetimedestruction",
                                    ],
                                    pk_tablename,
                                )

                            if id_objet in importedobjetids:  # initial offline object
                                if debug:
                                    strdebug = f"Updated Objet : id_objet : {id_objet}, rev_beg : {rev_begin}, rev_end : {rev_end}"

                                if (
                                    rev_begin == 1
                                    and rev_end is None
                                    and datetimedes is None
                                ):  # subcase 1 or 2 do nothing
                                    pass
                                    if debug:
                                        logging.getLogger("Lamiaoffline").debug(
                                            "%s - %s ", strdebug, "subcase 1, 2"
                                        )

                                elif (
                                    rev_begin == 1
                                    and rev_end is None
                                    and datetimedes is not None
                                ):  # subcases 8,9
                                    if id_objet in dictconflicts.keys():
                                        conflictidcase = dictconflicts[id_objet]["case"]

                                        if (
                                            conflictidcase == 1
                                        ):  # updated in main and deleted in import subcase 8,9
                                            if debug:
                                                logging.getLogger("Lamiaoffline").debug(
                                                    "%s - %s ", strdebug, "subcase 8,9"
                                                )
                                            if (
                                                dictconflicts[id_objet][
                                                    "conflictresolved"
                                                ]
                                                == "import"
                                            ):
                                                # simple update with datetimedestructionvalue
                                                self.insertAndUpdateIdPkSqL(
                                                    mode="update",
                                                    fromparser=dbaseparserfrom,
                                                    toparser=self.dbase,
                                                    tablename=tablename,
                                                    confdatas=confdatas,
                                                    pkidresult=pkidresult,
                                                    noncriticalresult=noncriticalresult,
                                                )
                                            else:
                                                # do nothing
                                                pass

                                elif rev_begin == 1 and rev_end == 2:  # subcase 7
                                    pass
                                    # do nothing, wait for rev_begin == 2 and rev_end == None

                                elif (
                                    rev_begin == 2 and rev_end == None
                                ):  # subcase 3, 4, 5, 6  ,11
                                    if (
                                        id_objet in dictconflicts.keys()
                                    ):  # subcase 4,5,6,11
                                        conflictidcase = dictconflicts[id_objet]["case"]
                                        # case4 = subcase4, case3 = subcase 5, case2 = subcase6, 11
                                        if conflictidcase == 2:  # subcase 6,11
                                            if (
                                                dictconflicts[id_objet][
                                                    "conflictresolved"
                                                ]
                                                == "import"
                                            ):
                                                # update main with import value
                                                self.insertAndUpdateIdPkSqL(
                                                    mode="update",
                                                    fromparser=dbaseparserfrom,
                                                    toparser=self.dbase,
                                                    tablename=tablename,
                                                    confdatas=confdatas,
                                                    pkidresult=pkidresult,
                                                    noncriticalresult=noncriticalresult,
                                                )
                                            else:
                                                pass
                                                # do nothing keep main deleted
                                        elif conflictidcase == 3:  # subcase 5
                                            if (
                                                dictconflicts[id_objet][
                                                    "conflictresolved"
                                                ]
                                                == "import"
                                            ):
                                                # update main with import value
                                                self.insertAndUpdateIdPkSqL(
                                                    mode="update",
                                                    fromparser=dbaseparserfrom,
                                                    toparser=self.dbase,
                                                    tablename=tablename,
                                                    confdatas=confdatas,
                                                    pkidresult=pkidresult,
                                                    noncriticalresult=noncriticalresult,
                                                )
                                            else:
                                                # keep main value
                                                pass
                                        elif conflictidcase == 4:  # subcase 4
                                            if (
                                                dictconflicts[id_objet][
                                                    "conflictresolved"
                                                ]
                                                == "import"
                                            ):
                                                self.insertAndUpdateIdPkSqL(
                                                    mode="update",
                                                    fromparser=dbaseparserfrom,
                                                    toparser=self.dbase,
                                                    tablename=tablename,
                                                    confdatas=confdatas,
                                                    pkidresult=pkidresult,
                                                    noncriticalresult=noncriticalresult,
                                                )
                                            else:
                                                # keep main value
                                                pass

                                    else:  # no conflict, simple update subcase 3                       #subcase 3
                                        if debug:
                                            logging.getLogger("Lamiaoffline").debug(
                                                "%s - %s ", strdebug, "subcase 3"
                                            )
                                        self.insertAndUpdateIdPkSqL(
                                            mode="update",
                                            fromparser=dbaseparserfrom,
                                            toparser=self.dbase,
                                            tablename=tablename,
                                            confdatas=confdatas,
                                            pkidresult=pkidresult,
                                            noncriticalresult=noncriticalresult,
                                        )

                            else:  # new objet in offline
                                if debug:
                                    strdebug = f"New object : id_objet : {id_objet}, rev_beg : {rev_begin}, rev_end : {rev_end}"
                                    logging.getLogger("Lamiaoffline").debug(
                                        "%s", strdebug
                                    )

                                if typeimport == "update":
                                    typeinsert = "append"
                                else:
                                    typeinsert = typeimport

                                self.insertAndUpdateIdPkSqL(
                                    mode=typeinsert,
                                    fromparser=dbaseparserfrom,
                                    toparser=self.dbase,
                                    tablename=tablename,
                                    confdatas=confdatas,
                                    pkidresult=pkidresult,
                                    noncriticalresult=noncriticalresult,
                                    ressourcesimport=ressourcesimport,
                                )

                        else:  # tc tables
                            index_pk_tablename = dbconfdatas["pkidfields"].index(
                                "pk_" + tablename.lower()
                            )
                            pk_tablename = pkidresult[index_pk_tablename]
                            rev_begin, rev_end = dbaseparserfrom.getValuesFromPk(
                                tablename,
                                ["lpk_revision_begin", "lpk_revision_end"],
                                pk_tablename,
                            )
                            if typeimport in ["append", "copy"]:
                                if rev_end is None:
                                    self.insertAndUpdateIdPkSqL(
                                        mode=typeimport,
                                        fromparser=dbaseparserfrom,
                                        toparser=self.dbase,
                                        tablename=tablename,
                                        confdatas=confdatas,
                                        pkidresult=pkidresult,
                                        noncriticalresult=noncriticalresult,
                                    )
                            elif typeimport == "update":
                                if rev_begin == 2 and rev_end is None:
                                    self.insertAndUpdateIdPkSqL(
                                        mode="append",
                                        fromparser=dbaseparserfrom,
                                        toparser=self.dbase,
                                        tablename=tablename,
                                        confdatas=confdatas,
                                        pkidresult=pkidresult,
                                        noncriticalresult=noncriticalresult,
                                    )

                    self.dbase.commitTransaction()

                    # if tablename in confdatas.keys():
                    #     print("*****", tablename)
                    #     # print(confdatas[tablename]["importdictid"])

        if typeimport in ["append", "update"]:
            self.updateLidField(
                fromparser=dbaseparserfrom,
                toparser=self.dbase,
                confdatas=confdatas,
                typeimport=typeimport,
            )

        self.dbase.messageinstance.closeProgressBar()

    def updateLidField(self, fromparser, toparser, confdatas, typeimport):
        counter = 0
        for order in range(1, 10):
            for tablename in self.dbase.dbasetables:
                if self.dbase.dbasetables[tablename]["order"] != order:
                    continue

                counter += 1

                self.dbase.messageinstance.updateProgressBar(counter)

                # tablenewpks = list(confdatas[tablename]["importdictpk"].values())
                (
                    pkidfields,
                    noncriticalfields,
                ) = self._getCriticalandNonCriticalFields(tablename)
                lidfields = [fld for fld in pkidfields if fld.startswith("lid_")]
                lidtables = [fld.split("_")[1] for fld in lidfields]

                if not lidfields:
                    continue

                self.dbase.beginTransaction()

                for i, (frompk, topk) in enumerate(
                    confdatas[tablename]["importdictpk"].items()
                ):
                    frompkvals = fromparser.lamiaorm[tablename].read(frompk)
                    lidvals = [frompkvals[fld] for fld in lidfields]
                    tablelidvals = dict()
                    if typeimport == "append":
                        newlidsvals = [
                            confdatas[lidtables[i]]["importdictid"][lidvals[i]]
                            if lidvals[i]
                            in list(confdatas[lidtables[i]]["importdictid"].keys())
                            else None
                            for i in range(len(lidtables))
                        ]
                    elif typeimport == "update":
                        newlidsvals = [
                            confdatas[lidtables[i]]["importdictid"][lidvals[i]]
                            if lidvals[i]
                            in list(confdatas[lidtables[i]]["importdictid"].keys())
                            else lidvals[i]
                            for i in range(len(lidtables))
                        ]
                    # importdictid
                    valtoup = dict(zip(lidfields, newlidsvals))
                    toparser.lamiaorm[tablename].update(topk, valtoup)

                self.dbase.commitTransaction()

    def _resolveConflict(self, dbaseparserfrom):
        # get importedobjetids

        dictconflicts = {}

        if self.dbase.base3version:

            sql = "SELECT datetimerevision FROM revision WHERE pk_revision = 2"
            dateofflinedbasecreation = dbaseparserfrom.query(sql)[0][0]

            sql = f"SELECT id_object FROM object WHERE lpk_revision_begin = 1"
            importedobjetids = [elem[0] for elem in dbaseparserfrom.query(sql)]

            # get deleted objetids in import
            sql = "SELECT id_object FROM object WHERE lpk_revision_begin = 2 AND datetimedestruction  IS NOT NULL"
            importedobjetidsdeleted = [elem[0] for elem in dbaseparserfrom.query(sql)]

            # get updated objetids in import
            sql = "SELECT id_object FROM object WHERE lpk_revision_begin = 2 AND lpk_revision_end IS NULL"
            sql += " AND datetimedestruction  IS NULL "
            importedobjetidsupdated = [elem[0] for elem in dbaseparserfrom.query(sql)]

            # get still present in main that are present in import
            sql = "SELECT id_object FROM object "
            sql += " WHERE id_object IN ({})".format(
                ",".join([str(id) for id in importedobjetids])
            )
            mainobjetstillthere = [elem[0] for elem in self.dbase.query(sql)]

            # get modified ids in main since offineexport
            sql = "SELECT id_object FROM object WHERE lpk_revision_end IS NULL "
            sql += " AND datetimedestruction  IS NULL "
            sql += " AND datetimemodification > '{}'".format(dateofflinedbasecreation)
            sql += " AND id_object IN ({})".format(
                ",".join([str(id) for id in importedobjetids])
            )
            mainobjetidsupdated = [elem[0] for elem in self.dbase.query(sql)]

            # get deleted ids in main since offineexport
            sql = "SELECT id_object FROM object WHERE datetimedestruction  IS NOT NULL"
            sql += " AND datetimedestruction > '{}'".format(dateofflinedbasecreation)
            sql += " AND id_object IN ({})".format(
                ",".join([str(id) for id in importedobjetids])
            )
            mainobjetidsdeleted = [elem[0] for elem in self.dbase.query(sql)]

        else:

            sql = "SELECT datetimerevision FROM Revision WHERE pk_revision = 2"
            dateofflinedbasecreation = dbaseparserfrom.query(sql)[0][0]

            sql = f"SELECT id_objet FROM Objet WHERE lpk_revision_begin = 1"
            importedobjetids = [elem[0] for elem in dbaseparserfrom.query(sql)]

            # get deleted objetids in import
            sql = "SELECT id_objet FROM Objet WHERE lpk_revision_begin = 1 AND datetimedestruction  IS NOT NULL"
            importedobjetidsdeleted = [elem[0] for elem in dbaseparserfrom.query(sql)]

            # get updated objetids in import
            sql = "SELECT id_objet FROM Objet WHERE lpk_revision_begin = 2 AND lpk_revision_end IS NULL"
            sql += " AND datetimedestruction  IS NULL "
            importedobjetidsupdated = [elem[0] for elem in dbaseparserfrom.query(sql)]

            # get still present in main that are present in import
            sql = "SELECT id_objet FROM Objet "
            sql += " WHERE id_objet IN ({})".format(
                ",".join([str(id) for id in importedobjetids])
            )
            mainobjetstillthere = [elem[0] for elem in self.dbase.query(sql)]

            # get modified ids in main since offineexport
            sql = "SELECT id_objet FROM Objet WHERE lpk_revision_end IS NULL "
            sql += " AND datetimedestruction  IS NULL "
            sql += " AND datetimemodification > '{}'".format(dateofflinedbasecreation)
            sql += " AND id_objet IN ({})".format(
                ",".join([str(id) for id in importedobjetids])
            )
            mainobjetidsupdated = [elem[0] for elem in self.dbase.query(sql)]

            # get deleted ids in main since offineexport
            sql = "SELECT id_objet FROM Objet WHERE datetimedestruction  IS NOT NULL"
            sql += " AND datetimedestruction > '{}'".format(dateofflinedbasecreation)
            sql += " AND id_objet IN ({})".format(
                ",".join([str(id) for id in importedobjetids])
            )
            mainobjetidsdeleted = [elem[0] for elem in self.dbase.query(sql)]

        # * conflicts are those updated in main and deleted in import #case1
        # ** and those archived in main and created in import   #case2
        # and those updated in both     #case3
        # * and those deleted in main and created in import    #case4

        case1 = list(set(importedobjetidsdeleted) & set(mainobjetidsupdated))
        for id in case1:
            dictconflicts[id] = {
                "fields": "/",
                "valuemain": "updated",
                "valueimport": "deleted",
                "case": 1,
            }

        case2 = list(set(importedobjetidsupdated) & set(mainobjetidsdeleted))
        for id in case2:
            dictconflicts[id] = {
                "fields": "/",
                "valuemain": "deleted",
                "valueimport": "updated",
                "case": 2,
            }
        case3 = list(set(importedobjetidsupdated) & set(mainobjetidsupdated))
        for id in case3:
            (
                isinconflict,
                listfields,
                listvaluemain,
                listvalueimport,
            ) = self.isInConflict(dbaseparserfrom, id)
            if isinconflict:
                dictconflicts[id] = {
                    "fields": listfields,
                    "valuemain": listvaluemain,
                    "valueimport": listvalueimport,
                    "case": 3,
                }
        case4 = list(set(importedobjetids) - set(mainobjetstillthere))
        case4 = list(set(case4) - set(importedobjetidsdeleted))
        for id in case4:
            dictconflicts[id] = {
                "fields": "/",
                "valuemain": "deleted",
                "valueimport": "updated",
                "case": 4,
            }

        if self.RESOLVECONFLICTTYPE == "manual":
            # then resolve conflict
            for id, iddict in dictconflicts.items():
                # ui demande
                message = ["ID objet              : " + str(id) + "\n"]
                message += ["champs                : " + str(iddict["fields"]) + "\n"]
                message += [
                    "Imported table values : " + str(iddict["valueimport"]) + "\n"
                ]
                message += [
                    "Main table values     : " + str(iddict["valuemain"]) + "\n"
                ]

                reply = self.dbase.messageinstance.inputMessage(
                    listtext=message, title="Keep imported value ?", withinput=False
                )
                if reply:
                    iddict["conflictresolved"] = "import"
                else:
                    iddict["conflictresolved"] = "main"

        else:
            for id_objet in dictconflicts.keys():
                if not "conflictresolved" in dictconflicts[id_objet].keys():
                    dictconflicts[id_objet][
                        "conflictresolved"
                    ] = self.RESOLVECONFLICTCHOICE

        return dictconflicts, importedobjetids, dateofflinedbasecreation

    def insertAndUpdateIdPkSqL(
        self,
        mode=None,  # copy append update
        fromparser=None,
        toparser=None,
        tablename=None,
        confdatas={},
        pkidresult=[],
        noncriticalresult=[],
        ressourcesimport="Full",
    ):  # Full / thumbnails / None

        debug = False
        if False and debug:
            toparser.printsql = True
            fromparser.printsql = True

        pktable = None
        fields = []
        values = []

        if False and debug and tablename == "Graphiquedata":
            logging.getLogger("Lamia_unittest").debug("tablename %s", tablename)
            logging.getLogger("Lamia_unittest").debug("listoffields %s", listoffields)
            logging.getLogger("Lamia_unittest").debug(
                "listofrawvalues %s", listofrawvalues
            )
            logging.getLogger("Lamia_unittest").debug("dictpk %s", dictpk)
            logging.getLogger("Lamia_unittest").debug("dictid %s", dictid)

        dbconfdatas = confdatas[tablename.lower()]
        pkidfields = dbconfdatas.get("pkidfields", None)
        noncriticalfields = dbconfdatas.get("noncriticalfields", None)
        # pkidresult = dbconfdatas.get('pkidresult', None)
        # noncriticalresult = dbconfdatas.get('noncriticalresult', None)

        importdictpk = dbconfdatas.get("importdictpk", None)
        importdictid = dbconfdatas.get("importdictid", None)
        importdictdeletedpk = dbconfdatas.get("importdictdeletedpk", None)

        # first inserting new data
        # restemp = []
        finalnoncriticalvalues = []
        if noncriticalfields != ["*"]:
            # for l, res in enumerate(result):
            if False:
                for l, field in enumerate(noncriticalfields):
                    res = noncriticalresult[l]
                    # if noncriticalfields[l] == 'lpk_revision_begin':
                    #     restemp.append(str(1))
                    #     # elif isinstance(res, str) or  ( isinstance(res, unicode) and noncriticalfield[l] != 'geom') :
                    if (
                        isinstance(res, str) or isinstance(res, bytes)
                    ) and field != "geom":
                        finalnoncriticalvalues.append(
                            "'" + str(res).replace("'", "''") + "'"
                        )
                    elif "datetime" in field and res is not None and res != "None":
                        finalnoncriticalvalues.append("'" + str(res) + "'")
                    elif field == "geom" and res is not None:
                        finalnoncriticalvalues.append(
                            "ST_GeomFromText('"
                            + res
                            + "', "
                            + str(self.dbase.crsnumber)
                            + ")"
                        )
                    elif res is None or res == "":
                        finalnoncriticalvalues.append("NULL")
                    else:
                        finalnoncriticalvalues.append(str(res))

            finalnoncriticalvalues = noncriticalresult
            # ressource
            if tablename in ["Ressource", "resource"] and ressourcesimport not in [
                "None"
            ]:  # Full / thumbnails / None
                fileindex = noncriticalfields.index("file")
                filepath = noncriticalresult[fileindex]
                withthumbnail = None

                # only export reference rasters
                if self.dbase.base3version:
                    pkressourceindex = pkidfields.index("pk_resource")
                    pkressource = pkidresult[pkressourceindex]
                    pkobjet = fromparser.getValuesFromPk(
                        "resource_qgis", "pk_object", pkressource
                    )
                else:
                    pkressourceindex = pkidfields.index("pk_ressource")
                    pkressource = pkidresult[pkressourceindex]
                    pkobjet = fromparser.getValuesFromPk(
                        "Ressource_qgis", "pk_objet", pkressource
                    )
                childdbname, childpk = self.searchChildfeatureFromPkObjet(
                    fromparser, pkobjet
                )

                if childdbname.lower() == "rasters":
                    # sql = " SELECT typeraster FROM Rasters_qgis WHERE pk_rasters = " + str(childpk)
                    if self.dbase.base3version:
                        typeraster = self.dbase.getValuesFromPk(
                            "rasters", "rastertype", childpk
                        )
                    else:
                        typeraster = self.dbase.getValuesFromPk(
                            "Rasters", "typeraster", childpk
                        )
                    # typeraster = self.dbase.query(sql,docommit=False)[0][0]
                    if typeraster not in ["ORF", "IRF"]:
                        filepath = None
                        withthumbnail = 2

                if not self.dbase.utils.isAttributeNull(filepath):
                    fromfile = os.path.join(
                        fromparser.dbaseressourcesdirectory, filepath
                    )
                    tofile = os.path.join(toparser.dbaseressourcesdirectory, filepath)
                    if withthumbnail is None:
                        if ressourcesimport == "thumbnails":  # Full / thumbnails / None
                            withthumbnail = 1
                        else:
                            withthumbnail = 0
                    self.dbase.copyRessourceFile(
                        filetype=childdbname,
                        fromfile=fromfile,
                        tofile=tofile,
                        withthumbnail=withthumbnail,
                        copywholedirforraster=True,
                    )

            # copy les valeurs
            if False:
                sql = (
                    "INSERT INTO " + tablename + "(" + ",".join(noncriticalfields) + ")"
                )
                sql += " VALUES(" + ",".join(finalnoncriticalvalues) + ")"
                if debug:
                    logging.getLogger("Lamiaoffline").debug(
                        "non critical insert %s", sql
                    )
                toparser.query(sql, docommit=False)
            if True:
                sql = f"INSERT INTO {tablename} ( {', '.join(noncriticalfields)} ) "
                inter = ["?"] * len(finalnoncriticalvalues)
                sql += f" VALUES({', '.join(inter)})"
                argts = finalnoncriticalvalues
                toparser.query(sql, arguments=argts, docommit=False)

        else:
            sql = "INSERT INTO " + tablename + " DEFAULT VALUES"
            toparser.query(sql, docommit=False)

        # exportparser.commit()

        # then updating
        finalpkidfields = []  # former fields
        finalpkidsvalues = []  # former values
        pktoinsert = None
        idtoinsert = None
        for k, field in enumerate(pkidfields):

            if "pk_" == field[0:3]:
                pktoinsert = toparser.getLastPK(
                    tablename
                )  # get the pk of noncritical data inserted
                # print(pktable)
                # pkoldtable = listofrawvalues[k]
                pkoldtable = pkidresult[k]
                importdictpk[pkoldtable] = pktoinsert

            elif "id_" == field[0:3]:

                finalpkidfields.append(field)
                # if changeID :
                if mode in ["append"]:  # copy append update
                    # idtable = self.dbase.getLastPK(tablename) + 1
                    idtoinsert = (
                        toparser.getmaxColumnValue(tablename, "id_" + tablename.lower())
                        + 1
                    )
                else:  # so update copy
                    idtoinsert = pkidresult[k]
                finalpkidsvalues.append(str(idtoinsert))

                oldid = pkidresult[k]
                importdictid[oldid] = idtoinsert

            elif "lid_" == field[0:4]:
                if pkidresult[k] is None:
                    continue
                jointablename = field.split("_")[1]
                if (
                    jointablename in confdatas.keys()
                    and "importdictid" in confdatas[jointablename].keys()
                ):
                    joinedidsdict = confdatas[jointablename]["importdictid"]
                    if pkidresult[k] in joinedidsdict.keys():
                        finalpkidfields.append(field)
                        finalpkidsvalues.append(str(joinedidsdict[pkidresult[k]]))
                    else:
                        finalpkidfields.append(field)
                        # finalpkidsvalues.append(str(pkidresult[k]))
                        finalpkidsvalues.append("NULL")

                        print("error lid_")
                        # print(dictid[field.split('_')[1]].keys())
                        print(
                            "base : ",
                            tablename,
                            " - column : ",
                            field,
                            " - lid value : ",
                            pkidresult[k],
                        )

                else:
                    finalpkidfields.append(field)
                    finalpkidsvalues.append(str(pkidresult[k]))

            elif "lpk_" == field[0:4]:
                # if "lpk_revision_begin" in self.dbase.dbasetables[tablename]['fields'].keys():
                jointablename = field.split("_")[1]
                if field == "lpk_revision_begin":
                    if mode in ["append"]:  # export append update
                        finalpkidfields.append("lpk_revision_begin")
                        finalpkidsvalues.append(str(self.dbase.maxrevision))
                    elif mode in ["update"]:
                        finalpkidfields.append("lpk_revision_begin")
                        finalpkidsvalues.append(str(self.dbase.maxrevision))
                        if idtoinsert:
                            # check if id inserted is a new version of existing id - if so put rev end to former id
                            tn = tablename.lower()
                            idtable = idtoinsert
                            sql = (
                                f"SELECT pk_{tn} FROM {tn} WHERE id_{tn} = {idtable} "
                                "AND lpk_revision_end IS NULL and datetimedestruction IS NULL"
                            )
                            pk = toparser.query(sql)
                            if pk:
                                maxrev = self.dbase.maxrevision
                                pk = pk[0][0]
                                sql = f"UPDATE {tn} SET lpk_revision_end = {maxrev} WHERE pk_{tn} = {pk}"
                                toparser.query(sql)

                    else:  # "export mode"
                        finalpkidfields.append("lpk_revision_begin")
                        finalpkidsvalues.append(str(1))

                elif (
                    jointablename in confdatas.keys()
                    and "importdictpk" in confdatas[jointablename].keys()
                ):

                    if pkidresult[k] is None:
                        continue

                    joinedpksdict = confdatas[jointablename]["importdictpk"]
                    if pkidresult[k] in joinedpksdict.keys():
                        finalpkidfields.append(field)
                        finalpkidsvalues.append(str(joinedpksdict[pkidresult[k]]))
                    else:
                        print("error lpk_", pkidresult)

        if pktoinsert is not None and finalpkidfields:
            # update line
            setsentence = ""
            for j, field in enumerate(finalpkidfields):
                setsentence += (
                    finalpkidfields[j] + " = " + str(finalpkidsvalues[j]) + ","
                )
            setsentence = setsentence[:-1]

            sqlup = "UPDATE {} SET {} WHERE pk_{} = {}".format(
                tablename.lower(), setsentence, tablename.lower(), pktoinsert
            )
            if debug:
                logging.getLogger("Lamiaoffline").debug("pkid update :  %s", sqlup)
            toparser.query(sqlup)

        dbconfdatas["importdictpk"] = importdictpk
        dbconfdatas["importdictid"] = importdictid
        dbconfdatas["importdictdeletedpk"] = importdictdeletedpk

    def _getCriticalandNonCriticalFields(self, dbname):

        # * get non critical fields (not pk and non id)
        noncriticalfield = []  # the "non-critical" fields
        pkidfields = []  # the "critical" fields (pk; id, lpk, lid)
        for field in self.dbase.dbasetables[dbname]["fields"].keys():
            if field[0:3] in ["id_", "pk_"] or field[0:4] in ["lpk_", "lid_"]:
                pkidfields.append(field)
            else:
                noncriticalfield.append(field)

        # add geom at rank-1
        if "geom" in self.dbase.dbasetables[dbname].keys():
            # noncriticalfield.insert(-1, 'ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))')
            noncriticalfield.insert(-1, "geom")
        if not noncriticalfield:
            noncriticalfield = ["*"]

        return pkidfields, noncriticalfield

    def _verifyColumnThumbnailedImage(self, fromdbase):
        results = []
        sql = "SELECT pk_resource, thumbnail, file FROM media_qgis WHERE thumbnail IS NULL and file IS NOT NULL"
        res = fromdbase.query(sql)
        if not res:
            return results

        for pkressource, thumbnail, filepath in res:
            fromdbase.createBlobThumbnail(
                pkressource, fromdbase.completePathOfFile(filepath)
            )

    def _getValuesFromImportedTable(
        self, typeimport, dbaseparserfrom, dbname, pkidfields=[], noncriticalfield=[]
    ):
        # type import export append update

        # if typeimport == 'nouvelle' or typeimport == 0:
        if typeimport in ["append", "copy"]:
            sqlconstraint = []
            if dbname[0:2].lower() == "tc":
                sqlconstraint = " WHERE lpk_revision_end IS NULL"
            else:
                sqlconstraint = (
                    " WHERE lpk_revision_end IS NULL AND datetimedestruction is NULL"
                )

            # sqlconstraint = " WHERE lpk_revision_end IS NULL and datetimedestruction is NULL"
        # elif typeimport == 'import_terrain' or typeimport == 1:
        else:  # update
            if dbname[0:2].lower() == "tc":
                sqlconstraint = " WHERE lpk_revision_end IS NULL"
            else:
                # sqlconstraint = " WHERE lpk_revision_end IS NULL AND datetimedestruction is NULL"
                sqlconstraint = " WHERE lpk_revision_begin = 2 OR lpk_revision_end = 2 or datetimedestruction IS NOT NULL"

        # noncriticalfield.insert(-1, 'ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))')
        noncriticalfieldtemp = list(noncriticalfield)
        if False:
            if "geom" in noncriticalfieldtemp:
                noncriticalfieldtemp[noncriticalfieldtemp.index("geom")] = (
                    "ST_AsText(ST_Transform(geom," + str(self.dbase.crsnumber) + "))"
                )
        else:
            if "geom" in noncriticalfieldtemp:
                noncriticalfieldtemp[noncriticalfieldtemp.index("geom")] = (
                    "ST_Transform(geom," + str(self.dbase.crsnumber) + ")"
                )

        sql, sqlpk = "", ""
        if "Objet" in self.dbase.getParentTable(
            dbname
        ) or "object" in self.dbase.getParentTable(dbname):
            sql = (
                "SELECT "
                + ",".join(noncriticalfieldtemp)
                + " FROM "
                + dbname.lower()
                + "_qgis"
            )
            sql += sqlconstraint
            if pkidfields:
                sqlpk = (
                    "SELECT "
                    + ",".join(pkidfields)
                    + " FROM "
                    + dbname.lower()
                    + "_qgis"
                )
                sqlpk += sqlconstraint
        elif "lpk_revision_end" in self.dbase.dbasetables[dbname]["fields"].keys():
            sql = "SELECT " + ",".join(noncriticalfieldtemp) + " FROM " + dbname.lower()
            sql += sqlconstraint
            if pkidfields:
                sqlpk = "SELECT " + ",".join(pkidfields) + " FROM " + dbname.lower()
                sqlpk += sqlconstraint
        # elif  'onlyoneparenttable' in self.dbase.dbasetables[dbname].keys():
        elif dbname[-4:] == "data":
            for elem in pkidfields + noncriticalfield:
                if elem[0:4] == "lpk_":
                    parenttablename = elem.split("_")[1].title()
                    break
            sql = "SELECT " + ",".join(noncriticalfieldtemp) + " FROM " + dbname.lower()
            sql += " INNER JOIN {} ON {} = {} ".format(
                parenttablename + "_qgis",
                parenttablename + "_qgis.pk_" + parenttablename.lower(),
                dbname + ".lpk_" + parenttablename.lower(),
            )
            sql += sqlconstraint
            if pkidfields:
                sqlpk = "SELECT " + ",".join(pkidfields) + " FROM " + dbname.lower()
                sqlpk += " INNER JOIN {} ON {} = {} ".format(
                    parenttablename + "_qgis",
                    parenttablename + "_qgis.pk_" + parenttablename.lower(),
                    dbname + ".lpk_" + parenttablename.lower(),
                )
                sqlpk += sqlconstraint
        else:
            sql = "SELECT " + ",".join(noncriticalfieldtemp) + " FROM " + dbname.lower()
            if pkidfields:
                sqlpk = "SELECT " + ",".join(pkidfields) + " FROM " + dbname.lower()
        results = dbaseparserfrom.query(sql)
        resultpk = dbaseparserfrom.query(sqlpk)
        return results, resultpk

    def isInConflict(self, dbaseparserfrom, conflictobjetid):
        """
        cases: (datet : datetravail)
        MAin                                             Import
        case n° datem       revbegin    revend          datem       revbegin    revend      Action                              Action on import                    Action if main retained
        1       <datet      11                          <datet      1                       nothing modified                    /                                   /
        2       >datet      11                          <datet      1                       only main modified - ok             /                                   /
        3       <datet      11                          >datet      1           2           only import modified ok             close lastrev and create new rev    /
                                                        >datet      2
        4       suppr                                   >datet      1           2           conflict                            add new rev with same id            close new rev
                                                        >datet      2
        5       >datet      11          12              >datet      1           2           conflict                            rewrite main new rev                rewrite new rev with main
                >datet      12                          >datet      2
        6       >datet      11          12              >datet      1           2           conflict                            add new rev                         close new rev
                                                        >datet      2
        7       suppr                                   >datet      1           2           ok : deleted on main and import     /                                   /
        8       >datet      11          12              >datet      1           2           conflict                            close lastrev                      write new rev with main
                >datet      12
        9       >datet      11                          >datet      1           2           conflit                             close lastrev                       unclose lastrev
        10      >datet      11          12              >datet      1           2           ok : deleted on main and import     /                                   /
        11      >datet      11          12              >datet      1           2           conlit                              add new rev                         /  close las rev
                                                        >datet      2

        :param dbaseparserfrom:
        :param conflictobjetid:
        :return:
        """

        debug = False
        if debug:
            logging.getLogger("Lamiaoffline").debug(
                " isInConflict - idobjet : %s  ", str(conflictobjetid)
            )

        # get mainpkobjet and importpkobjet
        if self.dbase.base3version:
            sql = " SELECT MAX(pk_object) FROM object WHERE id_object = " + str(
                conflictobjetid
            )
        else:
            sql = " SELECT MAX(pk_objet) FROM Objet WHERE id_objet = " + str(
                conflictobjetid
            )
        mainpkobjetsql = self.dbase.query(sql)
        importpkobjetsql = dbaseparserfrom.query(sql)

        mainpkobjet = mainpkobjetsql[0][0]
        importpkobjet = importpkobjetsql[0][0]

        # get child table name and pk
        mainconflictdbname, mainconflictpk = self.searchChildfeatureFromPkObjet(
            self.dbase, mainpkobjet
        )
        importconflictdbname, importconflictpk = self.searchChildfeatureFromPkObjet(
            dbaseparserfrom, importpkobjet
        )

        # get revend of pk
        sql = "SELECT lpk_revision_end FROM " + mainconflictdbname.lower() + "_qgis"
        sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
        revendmain = self.dbase.query(sql)[0][0]
        sql = "SELECT lpk_revision_end FROM " + importconflictdbname.lower() + "_qgis"
        sql += (
            " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
        )
        revendimport = dbaseparserfrom.query(sql)[0][0]

        allfieldslist = self.dbase.getColumns(mainconflictdbname + "_qgis")

        # values from child table
        sql = (
            "SELECT "
            + ", ".join(allfieldslist)
            + " FROM "
            + mainconflictdbname.lower()
            + "_qgis"
        )
        sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
        resmain = self.dbase.query(sql)[0]
        sql = (
            "SELECT "
            + ", ".join(allfieldslist)
            + " FROM "
            + importconflictdbname.lower()
            + "_qgis"
        )
        sql += (
            " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
        )
        resimport = dbaseparserfrom.query(sql)[0]

        # fields = self.getColumns(mainconflictdbname.lower() + "_qgis")
        fields = allfieldslist

        # get geom
        resgeom1, resgeom2 = None, None
        if "geom" in fields:
            sql = " SELECT ST_AsText(geom) FROM " + mainconflictdbname.lower() + "_qgis"
            sql += (
                " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
            )
            resgeommain = self.dbase.query(sql)[0][0]
            sql = (
                " SELECT ST_AsText(geom) FROM " + importconflictdbname.lower() + "_qgis"
            )
            sql += (
                " WHERE pk_"
                + importconflictdbname.lower()
                + " = "
                + str(importconflictpk)
            )
            resgeomimport = dbaseparserfrom.query(sql)[0][0]

        # manage fields in conflict
        conflict1values = []  # conflict value in main table
        conflict2values = []  # conflict value in import table
        conflictfields = []  # conflict fields in import table

        for i, restemp in enumerate(resmain):

            if (
                fields[i] not in ["geom", "datetimecreation", "datetimemodification"]
                and fields[i][0:3] != "pk_"
                and fields[i][0:4] != "lpk_"
                and restemp != resimport[i]
            ):
                conflict1values.append(restemp)
                conflict2values.append(resimport[i])
                conflictfields.append(fields[i])
            elif fields[i] == "geom" and resgeommain != resgeomimport:
                conflict1values.append(resgeommain)
                conflict2values.append(resgeomimport)
                conflictfields.append(fields[i])

        if debug:
            logging.getLogger("Lamiaoffline").debug(
                " isInConflict - conflictfields : %s  ", str(conflictfields)
            )
            logging.getLogger("Lamiaoffline").debug(
                " isInConflict - conflict1values : %s  ", str(conflict1values)
            )
            logging.getLogger("Lamiaoffline").debug(
                " isInConflict - conflict2values : %s  ", str(conflict2values)
            )

        if len(conflict1values) > 0:
            return True, conflictfields, conflict1values, conflict2values
        else:
            return False, None, None, None

    def backupBase(self):

        debug = False
        if debug:
            logging.getLogger("Lamia").debug("Start ")

        datesuppr = str(datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S"))
        # fileexport = os.path.join(exportdir, 'backup_' + datesuppr + '.sqlite')
        exportdir = os.path.join(self.dbase.dbaseressourcesdirectory, "backup")
        if not os.path.exists(exportdir):
            os.makedirs(exportdir)

        fileexport = os.path.join(exportdir, "backup_" + datesuppr + ".sqlite")

        dbaseparserfact = self.dbase.parserfactory.__class__
        backupsqlitedbase = dbaseparserfact(
            "spatialite", self.dbase.messageinstance
        ).getDbaseParser()
        backupsqlitedbase.createDBase(
            crs=self.dbase.crsnumber,
            worktype=self.dbase.worktype,
            dbaseressourcesdirectory=None,
            variante=None,
            slfile=fileexport,
        )
        dbasetables = self.dbase.dbconfigreader.dbasetables
        counter = 0
        for order in range(0, 10):
            for dbname in dbasetables:
                if dbasetables[dbname]["order"] == order:
                    counter += 1
                    # self.dbase.setLoadingProgressBar(progress, counter)

                    if dbname.lower() == "basedonnees":
                        continue

                    # self.normalMessage.emit("Export de " + str(dbname))

                    noncriticalfield = []

                    for field in dbasetables[dbname]["fields"].keys():
                        noncriticalfield.append(field)

                    # add geom at rank-1
                    if "geom" in dbasetables[dbname].keys():
                        noncriticalfield.insert(
                            -1,
                            "ST_AsText(ST_Transform(geom,"
                            + str(self.dbase.crsnumber)
                            + "))",
                        )

                    sql = (
                        "SELECT "
                        + ",".join(noncriticalfield)
                        + " FROM "
                        + dbname.lower()
                    )

                    results = self.dbase.query(sql)

                    if (
                        "ST_AsText(ST_Transform(geom,"
                        + str(self.dbase.crsnumber)
                        + "))"
                        in noncriticalfield
                    ):
                        noncriticalfield[
                            noncriticalfield.index(
                                "ST_AsText(ST_Transform(geom,"
                                + str(self.dbase.crsnumber)
                                + "))"
                            )
                        ] = "geom"

                    if not results:
                        print("no res", dbname)
                        continue

                    for i, result in enumerate(results):
                        if dbname.lower() == "revision" and i == 0:
                            continue

                        # traite la mise en forme du result
                        sql = self.dbase.createSetValueSentence(
                            type="INSERT",
                            tablename=dbname,
                            listoffields=noncriticalfield,
                            listofrawvalues=result,
                        )
                        backupsqlitedbase.query(sql, docommit=False)

                    backupsqlitedbase.commit()

        # if progress is not None: self.qgsiface.messageBar().clearWidgets()
        # print(self.dbase.dbasetables)

    def createSetValueSentence(
        self, type="INSERT", tablename=None, listoffields=[], listofrawvalues=[]
    ):

        debug = False
        if debug:
            logging.getLogger("Lamia").debug(
                " fields / rawvalues %s %s  ", str(listoffields), str(listofrawvalues)
            )

        restemp = []

        for l, res in enumerate(listofrawvalues):
            if sys.version_info.major == 2:
                if isinstance(res, str) or (
                    isinstance(res, unicode) and listoffields[l] != "geom"
                ):
                    if isinstance(res, unicode):
                        restemp.append("'" + res.replace("'", "''") + "'")
                    else:
                        restemp.append("'" + str(res).replace("'", "''") + "'")

                elif listoffields[l] == "geom" and res is not None:
                    # print('geom', "ST_GeomFromText('" + res + "', " + str(self.dbase.crsnumber)  + ")")
                    restemp.append(
                        "ST_GeomFromText('"
                        + res
                        + "', "
                        + str(self.dbase.crsnumber)
                        + ")"
                    )
                elif res is None or res == "":
                    restemp.append("NULL")
                else:
                    restemp.append(str(res))

            elif sys.version_info.major == 3:
                # if ((isinstance(res, str)  or isinstance(res, unicode))  and listoffields[l] != 'geom'
                if (
                    (isinstance(res, str) or isinstance(res, bytes))
                    and listoffields[l] != "geom"
                    and "datetime" not in listoffields[l]
                ):
                    restemp.append("'" + str(res).replace("'", "''") + "'")
                elif (
                    "datetime" in listoffields[l] and res is not None and res != "None"
                ):
                    restemp.append("'" + str(res) + "'")
                elif listoffields[l] == "geom" and res is not None:
                    restemp.append(
                        "ST_GeomFromText('"
                        + res
                        + "', "
                        + str(self.dbase.crsnumber)
                        + ")"
                    )
                elif res is None or res == "":
                    restemp.append("NULL")
                elif (isinstance(res, str) or isinstance(res, bytes)) and "None" in res:
                    restemp.append("NULL")
                else:
                    restemp.append(str(res))

        if type == "INSERT":
            sql = "INSERT INTO " + tablename + "(" + ",".join(listoffields) + ")"
            sql += " VALUES(" + ",".join(restemp) + ")"

        elif type == "UPDATE":
            sql = " UPDATE " + tablename.lower() + " SET "
            for i, field in enumerate(listoffields):
                sql += field + " = " + str(restemp[i]) + ", "
            sql = sql[:-2]

        return sql

    def searchChildfeatureFromPkObjet(self, dbaseparser, pkobjet):

        # currentdbname = "Objet"
        currentdbname = "object"

        currentpk = pkobjet

        for order in range(1, 10):
            for dbname in self.dbase.dbasetables:
                if self.dbase.dbasetables[dbname]["order"] == order:
                    if (
                        "lpk_" + currentdbname.lower()
                        in self.dbase.dbasetables[dbname]["fields"].keys()
                    ):
                        sql = "SELECT pk_" + dbname.lower() + " FROM " + dbname.lower()
                        sql += (
                            " WHERE lpk_"
                            + currentdbname.lower()
                            + " = "
                            + str(currentpk)
                        )
                        result = dbaseparser.query(sql)
                        if len(result) == 1:
                            currentdbname = dbname
                            currentpk = result[0][0]
                            break

        return currentdbname, currentpk
