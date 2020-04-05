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

import datetime, os, sys
import logging

from . import dbaseutils


class DBaseOfflineManager():

    def __init__(self, dbase):
        self.dbase = dbase



    def importDbase(self, dbaseparserfrom, typeimport='nouvelle'):
        """

        :param dbaseparserfrom:
        :param typeimport:  nouvelle import_terrain
        :return:
        """

        debug = False

        dbaseutils.isAttributeNull('None')

        self.backupBase()
        """
        if self.qgsiface is not None:
            #if not self.dbase.standalone:
            progressMessageBar = self.qgsiface.messageBar().createMessage("Import des donnees...")
            progress = QProgressBar()
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.qgisversion_int)[0:3]) < 220:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, self.qgsiface.messageBar().INFO)
            else:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
            #len
            maxprogress = len(self.dbase.dbasetables.keys())
            progress.setMaximum(maxprogress)
        else:
            progress = None
        """

        # ********** Variables générales ***********************************
        # import dict : {tablename : {...{idfrom : idto} ...} }
        # utilise pour la correspondance entre les id de la table d'import et les id de la table main
        importdictid = {}
        # import dict : {tablename : {...{pkfrom : pkto} ...} }
        # utilise pour la correspondance entre les pk de la table d'import et les pk de la table main
        importdictpk = {}
        # import dict : {tablename : [pk1, pk2,..] }
        # utilise pour se souvenir des pk qui ont un revsionend
        importdictdeletedpk = {}
        #conflictobjetids dict : {..., idobjet:{fields : [], importvalue:[], mainvalue:[]},... }
        conflictobjetids = {}

        # ************** add version
        datedebutimport = str((datetime.datetime.now() - datetime.timedelta(seconds=2)).strftime("%Y-%m-%d %H:%M:%S"))
        if typeimport == 'nouvelle':
            comment = 'import'
        elif typeimport == 'import_terrain':
            comment = 'import_terrain'
        sql = "INSERT INTO Revision(datetimerevision, commentaire) "
        sql += " VALUES('" + str(datedebutimport) + "', '" + comment + "')"
        self.dbase.query(sql)

        #self.maxrevision = self.dbase.getMaxRevision()
        self.maxrevision = self.dbase.getLastPK('Revision')
        self.currentrevision = int(self.maxrevision)
        # self.updateWorkingDate() TODO

        # **************** date de la version d'import
        datetravailhorsligne = None
        if typeimport == 'import_terrain':
            # datetravailhorsligne
            sql = "SELECT datetimerevision FROM Revision WHERE pk_revision = 2"
            datetravailhorsligne = dbaseparserfrom.query(sql)[0][0]

        # **************** debut de l'iteration sur les tables à importer
        counter = 0
        for order in range(1, 10):
            for dbname in self.dbase.dbasetables:
                if self.dbase.dbasetables[dbname]['order'] == order:

                    counter += 1

                    # if progress: progressMessageBar.setText("Import des donnees... : " + dbname)
                    # self.setLoadingProgressBar(progress, counter)



                    if debug: logging.getLogger("Lamia").debug(' ******************* %s *********  ', dbname)
                    logging.getLogger("Lamia_unittest").debug(' ******************* %s *********  ', dbname)

                    # initialisation des variables génerales
                    importdictid[dbname.lower()] = {}
                    importdictpk[dbname.lower()] = {}
                    importdictdeletedpk[dbname.lower()] = []

                    # get non critical fields (not pk and non id)
                    noncriticalfield = []           # the "non-critical" fields
                    pkidfields = []                 # the "critical" fields (pk; id, lpk, lid)
                    for field in self.dbase.dbasetables[dbname]['fields'].keys():
                        if field[0:3] in ['id_', 'pk_'] or field[0:4] in ['lpk_', 'lid_']:
                            pkidfields.append(field)
                        else:
                            noncriticalfield.append(field)
                    #add geom at rank-1
                    if 'geom' in self.dbase.dbasetables[dbname].keys():
                        noncriticalfield.insert(-1, 'ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))')
                    if not noncriticalfield:
                        noncriticalfield = ['*']
                    if debug: logging.getLogger("Lamia").debug(' fields, critical : %s %s ',
                                                               str(noncriticalfield),str(pkidfields))

                    # request results from dbaseparserfrom
                    if typeimport == 'nouvelle':
                        sqlconstraint = " WHERE lpk_revision_end IS NULL"
                    elif typeimport == 'import_terrain':
                        sqlconstraint = " WHERE lpk_revision_begin = 2 OR lpk_revision_end = 2"

                    sql, sqlpk = '', ''
                    if 'Objet' in self.dbase.getParentTable(dbname):
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower() + "_qgis"
                        sql += sqlconstraint
                        sqlpk = "SELECT " + ','.join(pkidfields) + " FROM " + dbname.lower() + "_qgis"
                        sqlpk += sqlconstraint
                    elif 'lpk_revision_end' in self.dbase.dbasetables[dbname]['fields'].keys():
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()
                        sql += sqlconstraint
                        sqlpk = "SELECT " + ','.join(pkidfields) + " FROM " + dbname.lower()
                        sqlpk += sqlconstraint
                    else:
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()
                        sqlpk = "SELECT " + ','.join(pkidfields) + " FROM " + dbname.lower()
                    results = dbaseparserfrom.query(sql)
                    resultpk = dbaseparserfrom.query(sqlpk)


                    strtofind = 'ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))'
                    if strtofind in noncriticalfield:
                        noncriticalfield[noncriticalfield.index(strtofind)] = 'geom'

                    # get previoux existing id and other things for import terrain
                    resultsid = None            # the existing id in main table
                    indexidfield = None         # the index of id_ column
                    indexrevisionend = None     # the index of lpk_revision_end
                    indexpkdbase = None         # the index of pk_ column
                    importid = None             # the id in the table lines iteration
                    parenttable = None          # the parent table of actual table - defined as lpk_(parenttable)
                    indexlkparenttable = None   # the index of parent table in pkidfields

                    if typeimport == 'import_terrain':
                        # get resultsid and indexidfield
                        if "id_" + dbname.lower() in pkidfields:
                            if True:
                                sqlid = "SELECT id_" + dbname.lower() + " FROM " + dbname.lower() + "_qgis"
                                sqlid += " WHERE lpk_revision_begin = 1 "
                                resultsid = [elem[0] for elem in dbaseparserfrom.query(sqlid)]

                            if False:
                                sqlid = "SELECT id_" + dbname.lower() + " FROM " + dbname.lower() + "_qgis"
                                sqlid += " WHERE datetimecreation < '" + str(datetravailhorsligne) + "'"
                                resultsid = [elem[0] for elem in self.dbase.query(sqlid)]
                            indexidfield = pkidfields.index("id_" + dbname.lower())
                        # get indexrevisionend
                        if "lpk_revision_end" in pkidfields:
                            indexrevisionend = pkidfields.index('lpk_revision_end')
                        indexpkdbase = pkidfields.index("pk_" + dbname.lower())
                        # get eventual parenttable
                        for j, fieldname in enumerate(pkidfields):
                            if fieldname[0:4] == 'lpk_':
                                parenttable = fieldname.split('_')[1]
                                indexlkparenttable = j
                        if debug: logging.getLogger("Lamia").debug(' parenttable, index : %s %s ',
                                                                   str(parenttable),
                                                                   str(indexlkparenttable))

                    # start the iteration in table lines
                    # if results is not None:
                    for i, result in enumerate(results):

                        if i % 50 == 0 and debug: logging.getLogger("Lamia").debug(' result : %s  ', str(result))

                        if resultsid is not None:
                            importid = resultpk[i][indexidfield]

                        # id already exists before - search if it was modified
                        if resultsid is not None and importid in resultsid:
                            # get its  datemodif
                            if False:
                                sqldate = " SELECT datetimemodification FROM " + dbname.lower() + "_qgis"
                                sqldate += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                sqldate += " AND lpk_revision_end IS NULL"
                            if True:
                                sqldate = " SELECT MAX(datetimemodification) FROM " + dbname.lower() + "_qgis"
                                sqldate += " WHERE id_" + dbname.lower() + " = " + str(importid)
                            resultdatesql = self.dbase.query(sqldate)
                            resultdate = None
                            if resultdatesql : # cases 3, 5, 6, 8, 9
                                resultdate = self.dbase.query(sqldate)[0][0]
                            else:       # case 4 or 7 : line deleted in main
                                pass

                            if debug:  logging.getLogger("Lamia").debug('**** existing id : %s / date main : %s / date2 : %s', str(importid), str(resultdate), str(datetravailhorsligne))

                            # Search if possible conflict
                            # isinconflict = False
                            if resultdate is None :  # case 4 or 7
                                # not modified while field investigation- create new version - done
                                if dbname.lower() == 'objet':
                                    if debug: self.printsql = False
                                    isinconflict, listfields, listvaluemain, listvalueimport = self.isInConflict(dbaseparserfrom, importid)
                                    if debug: self.printsql = True
                                    if debug: logging.getLogger("Lamia").debug('in conflict : %s', str(isinconflict))
                                    if debug: logging.getLogger("Lamia").debug('date : %s %s', str(resultdate), str(datetravailhorsligne))
                                    if isinconflict:
                                        conflictobjetids[importid]={}
                                        conflictobjetids[importid]['fields'] =  listfields
                                        conflictobjetids[importid]['mainvalue'] = listvaluemain
                                        conflictobjetids[importid]['importvalue'] = listvalueimport

                            elif resultdate < datetravailhorsligne or resultdate > datedebutimport:     #case 1, 3 - no conflict
                                pass






                            else:     # cases  5, 6, 8, 9
                                if dbname.lower() == 'objet':
                                    if debug: self.printsql = False
                                    isinconflict, listfields, listvaluemain, listvalueimport = self.isInConflict(dbaseparserfrom, importid)
                                    if debug: self.printsql = True
                                    if debug: logging.getLogger("Lamia").debug('in conflict : %s', str(isinconflict))
                                    if debug: logging.getLogger("Lamia").debug('date : %s %s', str(resultdate), str(datetravailhorsligne))
                                    if isinconflict:
                                        conflictobjetids[importid]={}
                                        conflictobjetids[importid]['fields'] =  listfields
                                        conflictobjetids[importid]['mainvalue'] = listvaluemain
                                        conflictobjetids[importid]['importvalue'] = listvalueimport

                            # **** in all cases, create a new line or set revisionend  with import table value *****
                            #   eventualy rewrite it when conflict process

                            # deleted id case
                            # its sure its an existing pk
                            # case 3a, 4a, 5a, 6a, 7a, 8a, 9a
                            if (typeimport == 'import_terrain' and indexrevisionend is not None
                                    and resultpk[i][indexrevisionend] == 2):

                                if debug: logging.getLogger("Lamia").debug(' set revisionend id, date: %s %s', str(importid), str(resultdate))

                                # case 4a or 7a
                                if not resultdate:
                                    sql = " SELECT pk_" + dbname.lower() + "FROM " + dbname.lower() + "_qgis"
                                    sql += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                    sql += " AND lpk_revision_end IS NULL"
                                    resultcase = dbaseparserfrom.query(sql)
                                    if resultcase:  # case 4a : do nothing - wait for active rev line
                                        pass
                                    else:    # case 7a : do nothing
                                        pass

                                # cases 3a, 5a, 6a, 8a, 9a, 10a, 11a
                                else:
                                    # simply set lpk_revision_end to main table
                                    if 'lpk_revision_end' in self.dbase.dbasetables[dbname]['fields'].keys():
                                        # search latest pk in main with same id
                                        sql = "SELECT pk_" + dbname.lower() + " FROM  " + dbname.lower()
                                        sql += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                        sql += " AND lpk_revision_end IS NULL"
                                        sqlpkmain = self.dbase.query(sql)
                                        # sqlpkimport = dbaseparserfrom.query(sql)

                                        # add pk to importdictdeletedpk
                                        importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])

                                        if sqlpkmain:
                                            self.printsql = True
                                            pkmain = sqlpkmain[0][0]
                                            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                            sql = "UPDATE " + dbname.lower() + " SET lpk_revision_end = " + str(self.maxrevision)
                                            sql += " , datetimemodification = '" + datesuppr + "'"
                                            sql += " WHERE pk_" + dbname.lower() + " = " + str(pkmain)
                                            self.dbase.query(sql, docommit=False)


                                    if False:

                                        sql = " SELECT pk_" + dbname.lower() + "FROM " + dbname.lower() + "_qgis"
                                        sql += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                        sql += " AND lpk_revision_end IS NULL "
                                        sql += "AND datetimemodification > '"  + str(datetravailhorsligne) + "'"
                                        resultcase = self.dbase.query(sql)

                                        if resultcase:  #case 3a, 6a, 9a : revend to main line without possible conflict
                                            pass
                                        else:
                                            pass


                                        if 'lpk_revision_end' in self.dbase.dbasetables[dbname]['fields'].keys():
                                            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                            sql = "UPDATE " + dbname.lower() + " SET lpk_revision_end = " + str(self.maxrevision)
                                            sql += " , datetimemodification = '" + datesuppr + "'"
                                            sql += " WHERE pk_" + dbname.lower() + " = " + str(resultpk[i][indexpkdbase])
                                            self.dbase.query(sql, docommit=False)

                                            # add pk to importdictdeletedpk
                                            importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])

                                            if True:
                                                # search if another id is in main and not in import
                                                sql = "SELECT pk_" + dbname.lower() + " FROM  " + dbname.lower()
                                                sql += " WHERE id_" + dbname.lower() + " = " + str(importid)
                                                sql += " AND lpk_revision_end IS NULL"
                                                idmain = self.dbase.query(sql)
                                                idimport = dbaseparserfrom.query(sql)

                                                if not idimport and idmain:        # simple delete from import and remain in main
                                                    pkmain = idmain[0][0]
                                                    sql = "UPDATE " + dbname.lower() + " SET lpk_revision_end = " + str(self.maxrevision)
                                                    sql += " , datetimemodification = '" + datesuppr + "'"
                                                    sql += " WHERE pk_" + dbname.lower() + " = " + str(pkmain)
                                                    self.dbase.query(sql, docommit=False)





                            # if parent table pk is in  importdictdeletedpk
                            elif (parenttable is not None
                                  and parenttable in importdictdeletedpk.keys()
                                  and resultpk[i][indexlkparenttable] in importdictdeletedpk[parenttable]):
                                if debug: logging.getLogger("Lamia").debug(' parent revisionend : %s', str(importid))
                                importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])


                            # new version case
                            # case 3b, 4b, 5b, 6b, 11b
                            else:
                                if debug: logging.getLogger("Lamia").debug(' new elem : %s', str(importid))
                                # insert new line in main table
                                sql = self.createSetValueSentence(type='INSERT',
                                                                  tablename=dbname,
                                                                  listoffields=noncriticalfield,
                                                                  listofrawvalues=result)
                                self.dbase.query(sql, docommit=True)
                                # udpate id/pk fields without changing id_table value
                                sqlup = self.updateIdPkSqL(tablename=dbname,
                                                           listoffields=pkidfields,
                                                           listofrawvalues=resultpk[i],
                                                           dictpk=importdictpk,
                                                           dictid=importdictid,
                                                           changeID=False)
                                self.dbase.query(sqlup, docommit=False)



                        # id does not exists before - create new line or for tc
                        else:
                            if debug: logging.getLogger("Lamia").debug('****  new elem id : %s',str(importid))

                            if (typeimport == 'import_terrain' and indexrevisionend is not None
                                    and resultpk[i][indexrevisionend] == 2):
                                # case of line deleted in main and deleted in import - dont t process it
                                importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])



                            elif (parenttable is not None
                                  and parenttable in importdictdeletedpk.keys()
                                  and resultpk[i][indexlkparenttable] in importdictdeletedpk[parenttable]):
                                if debug: logging.getLogger("Lamia").debug(' parent revisionend : %s', str(importid))
                                importdictdeletedpk[dbname.lower()].append(resultpk[i][indexpkdbase])

                            else:
                                # traite la mise en forme du result
                                if noncriticalfield != ['*']:
                                    sql = self.createSetValueSentence(type='INSERT',
                                                                      tablename=dbname,
                                                                      listoffields=noncriticalfield,
                                                                      listofrawvalues=result)
                                else:
                                    sql = "INSERT INTO " + dbname + " DEFAULT VALUES"
                                self.dbase.query(sql, docommit=False)

                                # traite les id, pk et lid et lpk
                                if True:
                                    sqlup = self.updateIdPkSqL(tablename=dbname,
                                                               listoffields=pkidfields,
                                                               listofrawvalues=resultpk[i],
                                                               dictpk=importdictpk,
                                                               dictid=importdictid,
                                                               changeID=True)

                                    self.dbase.query(sqlup, docommit=False)

                                # Ressource case : copy file
                                if dbname == 'Ressource':
                                    indexfile = noncriticalfield.index('file')
                                    filepath = result[indexfile]
                                    if not dbaseutils.isAttributeNull(filepath):
                                        filefrom = dbaseparserfrom.completePathOfFile(filepath)
                                        fileto = os.path.join(self.dbase.dbaseressourcesdirectory, filepath)
                                        self.dbase.copyRessourceFile(fromfile=filefrom,
                                                               tofile=fileto,
                                                               withthumbnail=0,
                                                               copywholedirforraster=False)
                    # Finaly commit all
                    self.dbase.commit()

                    if debug: logging.getLogger("Lamia").debug(' importdictid %s  ', str(importdictid[dbname.lower()]))
                    if debug: logging.getLogger("Lamia").debug(' importdictpk %s  ', str(importdictpk[dbname.lower()]))
                    if debug: logging.getLogger("Lamia").debug(' importdictdeletedpk %s  ', str(importdictdeletedpk[dbname.lower()]))
                    if debug: logging.getLogger("Lamia").debug(' conflictobjetids %s  ', str(conflictobjetids))

        self.resolveConflict(dbaseparserfrom,conflictobjetids )




        # if progress is not None: self.qgsiface.messageBar().clearWidgets() TODO
        self.normalMessage.emit("Import termine")

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
        if debug: logging.getLogger("Lamia").debug(' isInConflict - idobjet : %s  ', str(conflictobjetid))

        # get mainpkobjet and importpkobjet
        sql = " SELECT MAX(pk_objet) FROM Objet WHERE id_objet = " + str(conflictobjetid)
        mainpkobjetsql = self.dbase.query(sql)
        importpkobjetsql = dbaseparserfrom.query(sql)





        if False:
            sql = " SELECT pk_objet FROM Objet WHERE id_objet = " + str(conflictobjetid)
            sql += " AND lpk_revision_end IS NULL"
            mainpkobjet = None
            resmain = self.dbase.query(sql)
            if resmain:
                mainpkobjet = resmain[0][0]
            importpkobjet = None
            resimport = dbaseparserfrom.query(sql)
            if resimport:
                importpkobjet = resimport[0][0]

            if mainpkobjet is None:
                sql = " SELECT pk_objet FROM Objet WHERE id_objet = " + str(conflictobjetid)
                sql += " AND lpk_revision_end = MAX(lpk_revision_end)"


        # print('mainpkobjetsql',mainpkobjetsql,conflictobjetid)
        if mainpkobjetsql[0][0] is not None: #cases 3, 5, 6, 8, 9

            mainpkobjet = mainpkobjetsql[0][0]
            importpkobjet = importpkobjetsql[0][0]

            # get child table name and pk
            mainconflictdbname, mainconflictpk = self.searchChildfeatureFromPkObjet(self, mainpkobjet)
            importconflictdbname, importconflictpk = self.searchChildfeatureFromPkObjet(dbaseparserfrom, importpkobjet)

            #get revend of pk
            sql = "SELECT lpk_revision_end FROM " + mainconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
            revendmain = self.dbase.query(sql)[0][0]
            sql = "SELECT lpk_revision_end FROM " + importconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
            revendimport = dbaseparserfrom.query(sql)[0][0]


            if revendimport is not None and revendmain is not None:     # main and import has been deleted - non conflict
                return False, None, None, None

            # construct column names (usefull if both tables are not in same order)
            # allfields = ', '.join(self.getAllFields(mainconflictdbname))
            allfieldslist = self.getAllFields(mainconflictdbname)


            # values from child table
            sql = "SELECT " + ', '.join(allfieldslist) + " FROM " + mainconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
            resmain = self.dbase.query(sql)[0]
            sql = "SELECT " + ', '.join(allfieldslist) + " FROM " + importconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
            resimport = dbaseparserfrom.query(sql)[0]

            # fields = self.getColumns(mainconflictdbname.lower() + "_qgis")
            fields = allfieldslist

            # get geom
            resgeom1, resgeom2 = None, None
            if 'geom' in fields:
                sql = " SELECT ST_AsText(geom) FROM " + mainconflictdbname.lower() + "_qgis"
                sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
                resgeommain = self.dbase.query(sql)[0][0]
                sql = " SELECT ST_AsText(geom) FROM " + importconflictdbname.lower() + "_qgis"
                sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
                resgeomimport = dbaseparserfrom.query(sql)[0][0]

            if False:
                print('resmain',resmain)
                print('resimport',resimport)
                print('resgeommain',resgeommain)
                print('resgeomimport', resgeomimport)


        else:

            sql = " SELECT pk_objet FROM Objet WHERE id_objet = " + str(conflictobjetid)
            sql += " AND lpk_revision_end = 2"
            mainpkobjetsql = dbaseparserfrom.query(sql)

            mainpkobjet = mainpkobjetsql[0][0]
            importpkobjet = importpkobjetsql[0][0]

            if mainpkobjet == importpkobjet:   #main was deleted and import also - no conflict
                return False, None, None, None



            mainconflictdbname, mainconflictpk = self.searchChildfeatureFromPkObjet(dbaseparserfrom, mainpkobjet)
            importconflictdbname, importconflictpk = self.searchChildfeatureFromPkObjet(dbaseparserfrom, importpkobjet)

            # construct column names (usefull if both tables are not in same order)
            allfieldslist = self.getAllFields(mainconflictdbname)

            # values from child table
            sql = "SELECT " + ', '.join(allfieldslist) + " FROM " + mainconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
            resmain = dbaseparserfrom.query(sql)[0]
            sql = "SELECT " + ', '.join(allfieldslist) + " FROM " + importconflictdbname.lower() + "_qgis"
            sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
            resimport = dbaseparserfrom.query(sql)[0]

            # fields = self.getColumns(mainconflictdbname.lower() + "_qgis")
            fields = allfieldslist

            # get geom
            resgeom1, resgeom2 = None, None
            if 'geom' in fields:
                sql = " SELECT ST_AsText(geom) FROM " + mainconflictdbname.lower() + "_qgis"
                sql += " WHERE pk_" + mainconflictdbname.lower() + " = " + str(mainconflictpk)
                resgeommain = dbaseparserfrom.query(sql)[0][0]
                sql = " SELECT ST_AsText(geom) FROM " + importconflictdbname.lower() + "_qgis"
                sql += " WHERE pk_" + importconflictdbname.lower() + " = " + str(importconflictpk)
                resgeomimport = dbaseparserfrom.query(sql)[0][0]




        # manage fields in conflict
        conflict1values = []  # conflict value in main table
        conflict2values = []  # conflict value in import table
        conflictfields = []  # conflict fields in import table


        for i, restemp in enumerate(resmain):

            if (fields[i] not in ['geom', 'datetimecreation', 'datetimemodification']
                    and fields[i][0:3] != "pk_" and fields[i][0:4] != "lpk_"
                    and restemp != resimport[i]):
                conflict1values.append(restemp)
                conflict2values.append(resimport[i])
                conflictfields.append(fields[i])
            elif fields[i] == 'geom' and resgeommain != resgeomimport:
                conflict1values.append(resgeommain)
                conflict2values.append(resgeomimport)
                conflictfields.append(fields[i])

        if debug:
            logging.getLogger("Lamia").debug(' isInConflict - conflictfields : %s  ', str(conflictfields))
            logging.getLogger("Lamia").debug(' isInConflict - conflict1values : %s  ', str(conflict1values))
            logging.getLogger("Lamia").debug(' isInConflict - conflict2values : %s  ', str(conflict2values))


        if len(conflict1values)>0:
            return True, conflictfields, conflict1values, conflict2values
        else:
            return False, None, None, None
  
    def resolveConflict(self,dbaseparserfrom,conflictobjetids ):
        """
                conflictobjetpks[importid]['fields'] =  listfields
        conflictobjetpks[importid]['mainvalue'] = listvaluemain
        conflictobjetpks[importid]['importvalue'] = listvalueimport
        :param dbaseparserfrom:
        :param conflictobjetpks:
        :return:
        """

        debug = False

        for conflictobjetid in conflictobjetids.keys():

            # cas ou la ligne main a ete supprimee
            sql = "SELECT lpk_revision_end FROM Objet WHERE id_objet = " + str(conflictobjetid)
            resendpks = self.dbase.query(sql)
            listrevendpks = [res[0] for res in resendpks]
            # id was suppressed before import - re delet it
            # print('listrevendpks', listrevendpks)
            if not self.maxrevision in listrevendpks:
                conflictobjetids[conflictobjetid]['mainvalue'] = 'Supprime'

            # cas ou la ligne import a ete supprimee
            sql = " SELECT MAX(pk_objet) FROM Objet WHERE id_objet = " + str(conflictobjetid)
            pkobjet = self.dbase.query(sql)[0][0]
            if pkobjet is not None:
                sql = " SELECT  lpk_revision_end FROM Objet WHERE pk_objet = " + str(pkobjet)
                mainrevend  = self.dbase.query(sql)[0][0]
                if mainrevend is not None:
                    conflictobjetids[conflictobjetid]['importvalue'] = 'Supprime'

            # ui demande
            message =  "ID objet       : " + str(conflictobjetid) + '\n'
            message += "champs         : " + str(conflictobjetids[conflictobjetid]['fields']) + '\n'
            message += "valeurs import : " + str(conflictobjetids[conflictobjetid]['importvalue']) + '\n'
            message += "valeurs main   : " + str(conflictobjetids[conflictobjetid]['mainvalue']) + '\n'

            reply = QMessageBox.question(None, 'Keep import values ?',
                                            message, QMessageBox.Yes, QMessageBox.No)

            # retour a la valeur du main
            if reply == QMessageBox.No:
                if debug : self.printsql = True

                if conflictobjetids[conflictobjetid]['mainvalue'] == 'Supprime':
                    datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    sql = " UPDATE Objet SET "
                    sql += "lpk_revision_begin = " + str(self.maxrevision - 1)
                    sql += ", lpk_revision_end = " + str(self.maxrevision)
                    sql += ", datetimedestruction = '" + str(datesuppr) + "'"
                    sql += " WHERE pk_objet = " + str(pkobjet)
                    self.dbase.query(sql, docommit=True)
                    continue

                if conflictobjetids[conflictobjetid]['importvalue'] == 'Supprime':
                    # to know if deleted object - case of deleted objet in import and not in main
                    # sql = " SELECT  lpk_revision_end FROM Objet WHERE pk_objet = " + str(pkobjet)
                    # mainrevend  = self.dbase.query(sql)[0][0]
                    # if mainrevend is not None:
                    sql = " UPDATE Objet SET lpk_revision_end = NULL, datetimedestruction = NULL WHERE pk_objet = " + str(pkobjet)
                    self.dbase.query(sql, docommit=False)


                childdbname, childpk = self.searchChildfeatureFromPkObjet(self.dbase, pkobjet)
                parenttables = [childdbname] + self.dbase.getParentTable(childdbname)

                for tablename in parenttables:
                    sql = " SELECT pk_" + tablename.lower() + " FROM " +  childdbname.lower() + "_qgis"
                    sql += " WHERE pk_" + childdbname.lower() + " = " + str(childpk)
                    pktable = self.dbase.query(sql)[0][0]
                    fieldstomodif = []
                    valuetoinsert=[]
                    for i, field in enumerate(conflictobjetids[conflictobjetid]['fields']):
                        #for i, field in enumerate(self.dbase.dbasetables[tablename]['fields']):
                        #if field in conflictobjetids[conflictobjetid]['fields']:
                        if field in self.dbase.dbasetables[tablename]['fields'].keys():
                            # print(i, field, conflictobjetids[conflictobjetid]['mainvalue'])
                            fieldstomodif.append(field)
                            valuetoinsert.append(conflictobjetids[conflictobjetid]['mainvalue'][i])
                        elif field == 'geom' and 'geom' in self.dbase.dbasetables[tablename].keys():
                            fieldstomodif.append(field)
                            valuetoinsert.append(conflictobjetids[conflictobjetid]['mainvalue'][i])

                    if fieldstomodif:
                        sql = self.createSetValueSentence(type='UPDATE',
                                                            tablename=tablename,
                                                            listoffields=fieldstomodif,
                                                            listofrawvalues=valuetoinsert)
                        sql += " WHERE pk_" + tablename.lower() + " = " + str(pktable)
                        self.dbase.query(sql, docommit=False)
                self.commit()
                if debug: self.printsql = False


            else:
                continue

    def exportDbase(self,  exportfile=None ):

        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')
        """
        if self.qgsiface is not None: TODO
            # if not self.dbase.standalone:
            progressMessageBar = self.qgsiface.messageBar().createMessage("Backup...")
            progress = QProgressBar()
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.qgisversion_int)[0:3]) < 220:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, self.qgsiface.messageBar().INFO)
            else:
                self.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
            # len
            maxprogress = len(self.dbase.dbasetables.keys())
            progress.setMaximum(maxprogress)
        else:
            progress = None
        """
        dbaseparserfact = self.dbase.parserfactory.__class__
        exportparser = dbaseparserfact('spatialite').getDbaseParser()

        #exportparser = DBaseParser(self.canvas)
        #exportparser.createDbase(slfile=exportfile,
        #                         crs = self.dbase.crsnumber,
        #                         worktype = self.type)
        exportparser.createDbase(crs=self.dbase.crsnumber, 
                                worktype=self.dbase.worktype, 
                                dbaseressourcesdirectory=None, 
                                variante=None,
                                slfile=exportfile)
        exportparser.loadDBase(slfile=exportfile)

        counter = 0
        for order in range(1,10):

            for dbname in self.dbase.dbasetables:

                if self.dbase.dbasetables[dbname]['order'] == order:
                    counter += 1
                    # if progress: progressMessageBar.setText("Import des donnees... : " + dbname) TODO
                    # self.setLoadingProgressBar(progress, counter) TODO
                    logging.getLogger("Lamia_unittest").debug(' ******************* %s *********  ', dbname)


                    noncriticalfield = []

                    for field in self.dbase.dbasetables[dbname]['fields'].keys():
                            noncriticalfield.append(field)


                    #add geom at rank-1
                    if 'geom' in self.dbase.dbasetables[dbname].keys():
                        noncriticalfield.insert(-1, 'ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))')


                    sql = ''
                    if 'Objet' in self.dbase.getParentTable(dbname):
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower() + "_qgis"
                        sql += " WHERE lpk_revision_end IS NULL"


                    elif 'lpk_revision_end' in self.dbase.dbasetables[dbname]['fields'].keys():
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()
                        sql += " WHERE lpk_revision_end IS NULL"


                    else:
                        sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()

                    results = self.dbase.query(sql)

                    if 'ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))' in noncriticalfield :
                        noncriticalfield[noncriticalfield.index('ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))')] = 'geom'


                    # noncriticalfield.insert(0, "id_" + dbname)

                    for i, result in enumerate(results):

                        #traite la mise en forme du result
                        restemp = []
                        if  noncriticalfield != ['*']:
                            for l, res in enumerate(result):
                                if noncriticalfield[l] == 'lpk_revision_begin':
                                    restemp.append(str(1))
                                    # elif isinstance(res, str) or  ( isinstance(res, unicode) and noncriticalfield[l] != 'geom') :
                                elif (isinstance(res, str) or isinstance(res, bytes)) and noncriticalfield[l] != 'geom':
                                    restemp.append("'" + str(res).replace("'", "''") + "'")
                                elif 'datetime' in noncriticalfield[l] and res is not None and res != 'None':
                                    restemp.append("'" + str(res) + "'")
                                elif noncriticalfield[l] == 'geom' and res is not None:
                                    # print('geom', "ST_GeomFromText('" + res + "', " + str(self.dbase.crsnumber)  + ")")
                                    restemp.append("ST_GeomFromText('" + res + "', " + str(self.dbase.crsnumber)  + ")")

                                elif res is None or res == '':
                                    restemp.append('NULL')
                                else:
                                    restemp.append(str(res))

                            # copy les valeurs
                            if True:
                                sql = "INSERT INTO " + dbname + '(' + ','.join(noncriticalfield) + ')'
                                sql += " VALUES(" + ','.join(restemp) + ")"
                                exportparser.query(sql,docommit=False)



                            #ressource
                            if dbname == 'Ressource':
                                fileindex = noncriticalfield.index('file')
                                filepath = result[fileindex]

                                pkobjetindex = noncriticalfield.index('lpk_objet')
                                pkobjet = result[pkobjetindex]

                                childdbname, childpk = self.searchChildfeatureFromPkObjet(self.dbase, pkobjet)

                                # only export reference rasters
                                if childdbname.lower() == 'rasters':
                                    sql = " SELECT typeraster FROM Rasters_qgis WHERE pk_rasters = " + str(childpk)
                                    typeraster = self.dbase.query(sql,docommit=False)[0][0]
                                    if typeraster not in ['ORF', 'IRF']:
                                        continue


                                if not dbaseutils.isAttributeNull(filepath):

                                    # print(self.dbaseressourcesdirectory,filepath,  exportparser.dbaseressourcesdirectory)

                                    fromfile = os.path.join(self.dbase.dbaseressourcesdirectory, filepath)
                                    tofile = os.path.join(exportparser.dbaseressourcesdirectory, filepath)

                                    self.dbase.copyRessourceFile(fromfile=fromfile,
                                                           tofile=tofile,
                                                           withthumbnail=1,
                                                           copywholedirforraster = True)


                        else:
                            sql = "INSERT INTO " + dbname + " DEFAULT VALUES"
                            exportparser.query(sql,docommit=False)


                    exportparser.commit()


        #update seq file to remember last pk of each table
        for tablename in self.dbase.dbasetables.keys():
            if tablename == 'Revision':
                continue
            lastpk = self.dbase.getLastPK(tablename)
            if lastpk > 0:
                sql = "UPDATE sqlite_sequence SET seq = " + str(lastpk)
                sql += " WHERE name = '" + str(tablename) + "'"
                exportparser.query(sql)

        """
        if self.dbasetype == 'spatialite':

            sql = "SELECT * FROM sqlite_sequence "
            results = self.dbase.query(sql)
            for res in results:
                if res[0] == 'Revision':
                    continue
                sql = "UPDATE sqlite_sequence SET seq = " + str(res[1])
                sql += " WHERE name = '" + str(res[0]) + "'"
                exportparser.query(sql)
        elif self.dbasetype == 'postgis':
            for tablename in self.dbase.dbasetables.keys():
                lastpk = self.dbase.getLastPK('Revision')

                
                sql = "SELECT last_value FROM " + self.pgschema + '.' 
                sql +=  tablename.lower() + '_pk_' + tablename.lower() + '_seq'
                try:
                    result = self.dbase.query(sql)[0]
                    if tablename == 'Revision':
                        continue
                    sql = "UPDATE sqlite_sequence SET seq = " + str(result)
                    sql += " WHERE name = '" + str(tablename) + "'"
                except TypeError as e:
                    print('no seq for ' + tablename)
                except Exception as e:
                    print(e, ' - no seq for ' + tablename)
        """



        datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sql = "INSERT INTO Revision(datetimerevision, commentaire)  "
        sql += " VALUES('" + datecreation + "','travail horsligne')"
        exportparser.query(sql)

        # if progress is not None: self.qgsiface.messageBar().clearWidgets() TODO


    def backupBase(self):

        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')


        datesuppr = str(datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S"))
        # fileexport = os.path.join(exportdir, 'backup_' + datesuppr + '.sqlite')
        exportdir = os.path.join(self.dbase.dbaseressourcesdirectory , 'backup')
        if not os.path.exists(exportdir):
            os.makedirs(exportdir)

        fileexport = os.path.join(exportdir, 'backup_' + datesuppr + '.sqlite')

        dbaseparserfact = self.dbase.parserfactory.__class__
        backupsqlitedbase = dbaseparserfact('spatialite').getDbaseParser()
        backupsqlitedbase.createDbase(crs=self.dbase.crsnumber, 
                                worktype=self.dbase.worktype, 
                                dbaseressourcesdirectory=None, 
                                variante=None,
                                slfile=fileexport)
        dbasetables = self.dbase.dbconfigreader.dbasetables
        counter = 0
        for order in range(0, 10):
            for dbname in dbasetables:
                if dbasetables[dbname]['order'] == order:
                    counter += 1
                    # self.dbase.setLoadingProgressBar(progress, counter)

                    if dbname.lower() == 'basedonnees':
                        continue

                    # self.normalMessage.emit("Export de " + str(dbname))

                    noncriticalfield = []

                    for field in dbasetables[dbname]['fields'].keys():
                            noncriticalfield.append(field)

                    #add geom at rank-1
                    if 'geom' in dbasetables[dbname].keys():
                        noncriticalfield.insert(-1, 'ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))')

                    sql = "SELECT " + ','.join(noncriticalfield) + " FROM " + dbname.lower()

                    results = self.dbase.query(sql)

                    if 'ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))' in noncriticalfield :
                        noncriticalfield[noncriticalfield.index('ST_AsText(ST_Transform(geom,' + str(self.dbase.crsnumber) + '))')] = 'geom'

                    for i, result in enumerate(results):
                        if dbname.lower() == 'revision' and i == 0:
                            continue

                        #traite la mise en forme du result
                        sql = self.dbase.createSetValueSentence(type='INSERT',
                                                          tablename=dbname,
                                                          listoffields=noncriticalfield,
                                                          listofrawvalues=result)
                        backupsqlitedbase.query(sql, docommit=False)

                    backupsqlitedbase.commit()

        # if progress is not None: self.qgsiface.messageBar().clearWidgets()
        # print(self.dbase.dbasetables)

    def updateIdPkSqL(self,tablename=None, listoffields=[], listofrawvalues=[], dictpk = {}, dictid = {}, changeID = True):
        pktable = None
        fields = []
        values = []


        for k, field in enumerate(listoffields):

            if "pk_" == field[0:3]:
                pktable = self.dbase.getLastPK(tablename)
                # print(pktable)
                pkoldtable = listofrawvalues[k]
                dictpk[tablename.lower()][pkoldtable] = pktable


            elif "id_" == field[0:3]:

                fields.append(field)
                if changeID :
                    idtable = self.dbase.getLastPK(tablename) + 1
                else:
                    idtable = listofrawvalues[k]
                values.append(str(idtable))

                oldid = listofrawvalues[k]
                dictid[tablename.lower()][oldid] = idtable

            elif "lid_" == field[0:4]:
                if field.split('_')[1] in dictid.keys():
                    if listofrawvalues[k] is not None:
                        if listofrawvalues[k] in dictid[field.split('_')[1]].keys():
                            fields.append(field)
                            values.append(str(dictid[field.split('_')[1]][listofrawvalues[k]]))
                        else:
                            fields.append(field)
                            values.append(str(  listofrawvalues[k]    ))

                            print('error lid_' )
                            # print(dictid[field.split('_')[1]].keys())
                            print('base : ' ,tablename, ' - column : ', field, ' - lid value : ',listofrawvalues[k]  )

                else:
                    if listofrawvalues[k] is not None:
                        fields.append(field)
                        values.append(str(listofrawvalues[k]))

            elif "lpk_" == field[0:4]:

                #if "lpk_revision_begin" in self.dbase.dbasetables[tablename]['fields'].keys():
                if field == "lpk_revision_begin":
                    fields.append('lpk_revision_begin')
                    values.append(str(self.maxrevision))



                elif field.split('_')[1] in dictpk.keys():
                    if listofrawvalues[k] is not None:
                        if listofrawvalues[k] in dictpk[field.split('_')[1]].keys():
                            fields.append(field)
                            values.append(str(dictpk[field.split('_')[1]][listofrawvalues[k]]))
                        else:
                            print('error lpk_', listofrawvalues)


        if "lpk_revision_begin" in listoffields and not changeID:
            #pkcurrentable
            sql = " SELECT pk_" + tablename.lower() + " FROM " + tablename.lower()
            sql += " WHERE id_" + tablename.lower() + " = " + str(idtable)
            sql += " AND lpk_revision_end IS NULL"

            tempres = self.dbase.query(sql)

            if len(tempres)>0:
                pkcurrenttable = self.dbase.query(sql)[0][0]


                sql = "UPDATE " + tablename.lower() + " SET lpk_revision_end = " + str(self.maxrevision)
                sql += " WHERE pk_" + tablename.lower() + " = " + str(pkcurrenttable)
                self.dbase.query(sql, docommit=False)

        # if i % 50 == 0:
            # if debug: logging.getLogger("Lamia").debug(' field, value : %s %s  ', str(fields), str(values))

        if pktable is not None:
            # update line
            sqlup = "UPDATE " + tablename.lower() + " SET "
            for j, field in enumerate(fields):
                sqlup += field + " = " + str(values[j]) + ","
            sqlup = sqlup[:-1]
            sqlup += " WHERE pk_" + tablename.lower() + ' = ' + str(pktable)

            #self.dbase.query(sqlup, docommit=False)



        return sqlup

    def createSetValueSentence(self,type='INSERT',tablename=None, listoffields=[], listofrawvalues=[]):

        debug = False
        if debug : logging.getLogger("Lamia").debug(' fields / rawvalues %s %s  ', str(listoffields), str(listofrawvalues))

        restemp = []

        for l, res in enumerate(listofrawvalues):
            if sys.version_info.major == 2:
                if isinstance(res, str) or (isinstance(res, unicode) and listoffields[l] != 'geom'):
                    if isinstance(res, unicode):
                        restemp.append("'" + res.replace("'", "''") + "'")
                    else:
                        restemp.append("'" + str(res).replace("'", "''") + "'")

                elif listoffields[l] == 'geom' and res is not None:
                    # print('geom', "ST_GeomFromText('" + res + "', " + str(self.dbase.crsnumber)  + ")")
                    restemp.append("ST_GeomFromText('" + res + "', " + str(self.dbase.crsnumber) + ")")
                elif res is None or res == '':
                    restemp.append('NULL')
                else:
                    restemp.append(str(res))

            elif sys.version_info.major == 3:             
                # if ((isinstance(res, str)  or isinstance(res, unicode))  and listoffields[l] != 'geom' 
                if ((isinstance(res, str)  or isinstance(res, bytes))  and listoffields[l] != 'geom' 
                        and 'datetime' not in listoffields[l]) :
                    restemp.append("'" + str(res).replace("'", "''") + "'")
                elif 'datetime' in listoffields[l] and  res is not None and res != 'None':
                        restemp.append("'" + str(res) + "'")
                elif listoffields[l] == 'geom' and res is not None:
                    restemp.append("ST_GeomFromText('" + res + "', " + str(self.dbase.crsnumber) + ")")
                elif res is None or res == ''  :
                    restemp.append('NULL')
                elif (isinstance(res, str)  or isinstance(res, bytes)) and 'None' in res:
                    restemp.append('NULL')
                else:
                    restemp.append(str(res))

        if type == 'INSERT':
            sql = "INSERT INTO " + tablename + '(' + ','.join(listoffields) + ')'
            sql += " VALUES(" + ','.join(restemp) + ")"

        elif type == 'UPDATE':
            sql = " UPDATE " + tablename.lower() + " SET "
            for i, field in enumerate(listoffields):
                sql += field + " = " + str(restemp[i]) + ', '
            sql = sql[:-2]

        return sql




    def searchChildfeatureFromPkObjet(self,dbaseparser, pkobjet):

        currentdbname = "Objet"
        currentpk = pkobjet

        for order in range(1,10):
            for dbname in self.dbase.dbasetables:
                if self.dbase.dbasetables[dbname]['order'] == order :
                    if "lpk_" + currentdbname.lower() in self.dbase.dbasetables[dbname]['fields'].keys():
                        sql = "SELECT pk_" + dbname.lower() + " FROM " + dbname.lower()
                        sql += " WHERE lpk_" + currentdbname.lower() + " = " + str(currentpk)
                        result = dbaseparser.query(sql)
                        if len(result)== 1 :
                            currentdbname = dbname
                            currentpk = result[0][0]
                            break

        return currentdbname, currentpk
