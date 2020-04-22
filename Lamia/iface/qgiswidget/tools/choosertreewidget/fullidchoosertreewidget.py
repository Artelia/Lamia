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
import logging
from qgis.PyQt.QtWidgets import  QTreeWidgetItem, QHeaderView
from qgis.PyQt import QtCore

from ..lamia_abstractchoosertreewidget import AbstractChooserTreeWidget

class FullIDChooserTreeWidget(AbstractChooserTreeWidget):

    NEWFEATURETXT = 'Nouveau'

    def __init__(self, **kwargs):
        super(FullIDChooserTreeWidget, self).__init__(**kwargs)
        #self.treewidget = kwargs.get('choosertreewidget', None)
        #self.dbase = kwargs.get('dbaseparser', None)
        #self.mainifacewidget = kwargs.get('mainifacewidget', None)
        self.toolwidget = kwargs.get('toolwidget', None)

    def onActivation(self, initfeatureselection=True):
        self.treewidget.clear()

        headerlist = [self.toolwidget.DBASETABLENAME]
        #headerlist.insert(0, 'ID')
        self.treewidget.setColumnCount(len(headerlist))
        self.treewidget.header().setVisible(True)
        self.treewidget.setHeaderItem(QTreeWidgetItem(headerlist))

        # print('onActivation', self.toolwidget.DBASETABLENAME)
        self.loadFeaturesinTreeWdg()
        self.disconnectTreewidget()
        self.toolwidget.frametoolwidg.setEnabled(True)
        """
        if self.toolwidget.lastselectedpk is not None and self.selectItemfromPK(self.toolwidget.lastselectedpk):
            print('***', self.toolwidget.DBASETABLENAME, self.toolwidget.lastselectedpk)
        
            
        if self.treewidget.topLevelItemCount() == 0 :
            self.toolwidget.frametoolwidg.setEnabled(False)
        """
        if initfeatureselection:
            if self.treewidget.topLevelItemCount() > 0 :
                if self.toolwidget.lastselectedpk is None: 
                    self.treewidget.setCurrentItem(self.treewidget.invisibleRootItem().child(0))
                else:
                    indexids = self.ids.index[self.ids['pk'] == self.toolwidget.lastselectedpk][0]
                    self.treewidget.setCurrentItem(self.treewidget.invisibleRootItem().child(indexids))

        self.connectTreewidget()

    def loadFeaturesinTreeWdg(self):
        self.disconnectTreewidget()
        self.treewidget.clear()
        ids = self.loadIds()
        self._manageTreeWidgetHeader()
        parentitem = self.treewidget.invisibleRootItem()

        parentitem.addChildren([QTreeWidgetItem([str(val) for val in row[1:]]) for row in self.ids.values])
        self.connectTreewidget()


    def _manageTreeWidgetHeader(self):
        
        # headerlist = list(self.qtreewidgetfields)
        headerlist = list(self.ids.columns)[1:] 
        #headerlist.insert(0, 'spec')
        self.treewidget.setColumnCount(len(headerlist))
        self.treewidget.header().setVisible(True)
        self.treewidget.setHeaderItem(QTreeWidgetItem(headerlist))
        header = self.treewidget.header()
        lenheaderlist = len(headerlist)
        for i in range(lenheaderlist):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(lenheaderlist-1, QHeaderView.Stretch)


    def selectItemfromPK(self,pk ):
        id = self.toolwidget.dbase.getValuesFromPk(self.toolwidget.DBASETABLENAME,
                                            'id_' + self.toolwidget.DBASETABLENAME.lower(),
                                            pk)
        founditems = self.treewidget.findItems(str(id), 
                                                QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 
                                                0)
        if len(founditems) > 0:
            founditem = founditems[0]
            self.treewidget.setCurrentItem(founditem)
            return True 
        else:
            return False

    def loadIds(self):
        debug = False
        # CHOOSERTREEWDG_COLSHOW = ['datetimeobservation']
        dbnamelower = self.toolwidget.DBASETABLENAME.lower()
        fields_to_request = ['pk_' + dbnamelower, 'id_' + dbnamelower]
        pandascolumns = ['pk', 'id']
        if (hasattr(self.toolwidget, 'CHOOSERTREEWDG_COLSHOW') 
                and len(self.toolwidget.CHOOSERTREEWDG_COLSHOW) > 0 ):
            fields_to_request += self.toolwidget.CHOOSERTREEWDG_COLSHOW
            pandascolumns += self.toolwidget.CHOOSERTREEWDG_COLSHOW

        sql = "SELECT {} FROM {}_now ".format(', '.join(fields_to_request),
                                                        self.toolwidget.DBASETABLENAME    )
        
        if self.toolwidget.parentWidget is not None and self.toolwidget.parentWidget.currentFeaturePK is not None:
            parenttablename = self.toolwidget.parentWidget.DBASETABLENAME
            if self.toolwidget.PARENTJOIN and parenttablename in  self.toolwidget.PARENTJOIN.keys():
                joindict = self.toolwidget.PARENTJOIN[parenttablename]
                thistablename = self.toolwidget.DBASETABLENAME
                if joindict['tctable'] is None:
                    if parenttablename != thistablename:
                        sql += "JOIN {}_now ON {} = {}"\
                                " WHERE pk_{} = {}".format(parenttablename,
                                                            parenttablename + '_now.' + joindict['colparent'],
                                                            thistablename + '_now.' + joindict['colthistable'],
                                                            parenttablename.lower(),
                                                            self.toolwidget.parentWidget.currentFeaturePK)
                    else:
                        valsearched = self.toolwidget.dbase.getValuesFromPk(thistablename + '_qgis',
                                                                            joindict['colparent'],
                                                                            self.toolwidget.parentWidget.currentFeaturePK)
                        if valsearched is not None:
                            sql += " WHERE {} = {}".format(joindict['colthistable'],
                                                            valsearched)
                            #print('***', sql)
                        else:
                            sql = None
                else:
                    
                    sql += "INNER JOIN {} ON {} = {} "\
                        "INNER JOIN {}_now ON {} = {} "\
                        "WHERE pk_{} = {} ".format(joindict['tctable'],
                                                    thistablename + '_now.' + joindict['colthistable'],
                                                    joindict['tctable'] + '.' + joindict['tctablecolthistable'],
                                                    parenttablename,
                                                    joindict['tctable'] + '.' + joindict['tctablecolparent'],
                                                    parenttablename + '_now.' + joindict['colparent'],
                                                        parenttablename.lower(),
                                                        self.toolwidget.parentWidget.currentFeaturePK)

            if sql is not None:
                sql = self.dbase.sqlNow(sql)
            #query = self.dbase.query(sql)
            #self.ids = pd.DataFrame(query, columns = ['pk', 'id']) 
            #print(self.ids)
            #return query
        elif self.toolwidget.parentWidget is not None :
            sql = None
        else:
            sql = self.dbase.sqlNow(sql)

        if sql:
            if hasattr(self.toolwidget, 'TABLEFILTERFIELD') and self.toolwidget.TABLEFILTERFIELD is not None:
                for fieldname, fieldvalue in self.toolwidget.TABLEFILTERFIELD.items():
                    if isinstance(fieldvalue,str):
                        fieldvalue = "'" + fieldvalue + "'"
                    sqlsplitted = self.toolwidget.dbase.utils.splitSQLSelectFromWhereOrderby(sql)
                    if 'WHERE' in sqlsplitted.keys():
                        sql += " AND {} = {}".format(fieldname,fieldvalue)
                    else:
                        sql += " WHERE  {} = {}".format(fieldname,fieldvalue)
            if debug: logging.getLogger("Lamia_unittest").debug('sql : %s', sql)
            if debug: logging.getLogger("Lamia_unittest").debug('search : %s', self.dbase.query('show search_path'))
            
            query = self.dbase.query(sql)
            self.ids = pd.DataFrame(query, columns = pandascolumns) 
        else:
            self.ids = pd.DataFrame(columns = pandascolumns) 

        if debug: logging.getLogger("Lamia_unittest").debug('ids : %s', self.ids)

    def loadFeaturesinTreeWdg_caduc(self):
        """
        load features in self.linkedtreewidget
        called whenever the list need to be reinitialized (ex : click in maintreewidget,...)
        """

        debug = False

        if debug: timestart = self.dbase.getTimeNow()

        self.disconnectIdsGui()

        if debug: logging.getLogger("Lamia").debug('Start %s %s %s', self.dbasetablename, self.NAME, self.parentWidget)

        # clear treewidget
        self._clearLinkedTreeWidget()

        # mise en forme du linkedtreewidget et definition du "parentitem" qui correspond au nom de la table
        parentitem = None
        if self.linkedtreewidget is not None:
            headerlist = list(self.qtreewidgetfields)
            headerlist.insert(0, 'ID')
            self.linkedtreewidget.setColumnCount(len(headerlist))
            self.linkedtreewidget.header().setVisible(True)
            self.linkedtreewidget.setHeaderItem(QTreeWidgetItem(headerlist))
            header = self.linkedtreewidget.header()
            lenheaderlist = len(headerlist)
            if sys.version_info.major == 2:
                for i in range(lenheaderlist):
                    header.setResizeMode(i, QHeaderView.ResizeToContents)
                header.setResizeMode(lenheaderlist-1, QHeaderView.Stretch)
            elif  sys.version_info.major == 3:
                for i in range(lenheaderlist):
                    header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
                header.setSectionResizeMode(lenheaderlist-1, QHeaderView.Stretch)

            parentitem = self.linkedtreewidget.invisibleRootItem()
        elif (self.parentWidget is not None and self.parentWidget.linkedtreewidget is not None
                and self.parentWidget.currentFeature is not None):
            root = self.parentWidget.linkedtreewidget.invisibleRootItem()
            indexchild = [root.child(i).text(0) for i in range(root.childCount())].index(str(self.parentWidget.dbasetablename))
            tempitem = root.child(indexchild)
            if self.dbase.revisionwork:
                parentfeat = self.dbase.getLayerFeatureByPk( self.parentWidget.dbasetablename, self.parentWidget.currentFeature.id() )
                parentid = parentfeat['id_' + self.parentWidget.dbasetablename]
                indexchild = [tempitem.child(i).text(0) for i in range(tempitem.childCount())].index(str(parentid))
            else:
                indexchild = [tempitem.child(i).text(0) for i in range(tempitem.childCount())].index(str(self.parentWidget.currentFeature.id()))
            parentitem = tempitem.child(indexchild)

        # selection of particular feature to load (if parentfeature, or window only mode)
        ids = self.loadIds()

        # creation de la liste des elements qui figurent dans le linkedtreewidget
        lenqtreewidg = len(self.qtreewidgetfields) + 1
        if sys.version_info.major == 2:
            self.treefeatlist = [[id[0], QTreeWidgetItem([str(id[i]) if not isinstance(id[i], unicode) else id[i] for i in range(lenqtreewidg)])] for id in ids]
        else:
            self.treefeatlist = [[id[0], QTreeWidgetItem([str(id[i]) for i in range(lenqtreewidg)])] for id in ids]

        # ajout des ids dans le qtreewidgetitem parent
        if parentitem is not None:
            parentqtreewdgitem = None
            if parentitem.parent() is not None:
                for i in range(parentitem.parent().childCount()):
                    if parentitem.parent().child(i) != parentitem:
                        parentitem.parent().child(i).takeChildren()
                if self.dbasetablename in [parentitem.child(i).text(0) for i in range(parentitem.childCount())]:
                    index = [parentitem.child(i).text(0) for i in range(parentitem.childCount())].index(self.dbasetablename)
                    parentitem.child(index).takeChildren()
                    parentqtreewdgitem = parentitem.child(index)
                else:
                    parentqtreewdgitem = QTreeWidgetItem(parentitem, [self.dbasetablename])
            else:
                parentqtreewdgitem = QTreeWidgetItem(parentitem, [self.dbasetablename])
                # print(parentqtreewdgitem.text(0))

            parentqtreewdgitem.addChildren([elem[1] for elem in self.treefeatlist])

        if debug: logging.getLogger('Lamia').debug('feat list %s', str(self.treefeatlist))

        # enable/disable le widget selon que des ids ont ete trouves
        if len(self.treefeatlist) > 0:
            self.groupBox_properties.setEnabled(True)
            self.groupBox_geom.setEnabled(True)
            self.comboBox_featurelist.addItems([str(elem[0]) for elem in self.treefeatlist])
        else:
            self.groupBox_properties.setEnabled(False)
            self.groupBox_geom.setEnabled(False)
            self.currentFeature = None
            self.initFeatureProperties(None)

        if debug: logging.getLogger('Lamia').debug('end  %.3f', self.dbase.getTimeNow()  - timestart)
        self.connectIdsGui()

    def loadIds_caduc(self):
        """
        Called by loadFeaturesinTreeWdg

        :return: ids : an array of the wanted ids, with eventualy more value defined in self.qtreewidgetfields
        """

        ids = []
        if self.dbasetablename is not None:
                
            strid = 'id_' + self.dbasetablename.lower()
            sql = "SELECT " + strid
            if len(self.qtreewidgetfields)>0 :
                sql += "," + ','.join(self.qtreewidgetfields)
            sql += " FROM " + self.dbasetablename.lower() + '_now'
            sql = self.dbase.updateQueryTableNow(sql)

            if (self.parentWidget is not None and self.linkagespec is not None
                    and self.parentWidget.currentFeature is not None):
                linkagespeckey = None
                for key in self.linkagespec.keys():
                    if self.parentWidget.dbasetablename in self.linkagespec[key]['desttable']:
                        linkagespeckey = key
                if linkagespeckey is not None:
                    linkagetemp = self.linkagespec[linkagespeckey]

                    if linkagetemp['tabletc'] is None:

                        #linkagedest
                        sqltemp = " SELECT " + linkagetemp['iddest'] + " FROM " + self.parentWidget.dbasetablename.lower() + '_qgis'
                        sqltemp += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)

                        linkagedest = self.dbase.query(sqltemp)[0][0]
                        if linkagedest is None:
                            # print('None find')
                            return []
                        sql += " AND " + linkagetemp['idsource'] + " = " + str(linkagedest)
                        #TODO versionning

                    elif linkagetemp['tabletc'] == 'within':
                        sqltemp = " SELECT "+ linkagetemp['iddest']
                        if len(self.qtreewidgetfields) > 0:
                            sqltemp += "," + ','.join(self.qtreewidgetfields)
                        sqltemp += " FROM " + self.dbasetablename.lower() + "_now" + ', ' + self.parentWidget.dbasetablename.lower()
                        sqltemp += " WHERE ST_WITHIN(ST_MakeValid(" + self.parentWidget.dbasetablename.lower() + ".geom) , "
                        sqltemp += "ST_MakeValid(" + self.dbasetablename.lower() + "_now.geom) )"
                        sqltemp += " AND pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
                        sqltemp = self.dbase.updateQueryTableNow(sqltemp)
                        sql = sqltemp
                    else:
                        #get parent feature field for link
                        sqltemp = "SELECT " + linkagetemp['iddest']
                        sqltemp += " FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
                        sqltemp += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = "
                        sqltemp += str(self.parentWidget.currentFeaturePK)
                        res = self.dbase.query(sqltemp)
                        linkidparent = res[0][0]

                        sqltemp = "SELECT " + linkagetemp['idtcsource'] + " FROM " + linkagetemp['tabletc']
                        sqltemp += " WHERE " + linkagetemp['idtcdest'] + " = "
                        #sqltemp += str(self.parentWidget.currentFeature[linkagetemp['iddest']])
                        sqltemp += str(linkidparent)
                        sqltemp += " AND lpk_revision_begin <= " + str(self.dbase.currentrevision)
                        if self.dbase.dbasetype == 'postgis':
                            sqltemp += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
                            sqltemp += " lpk_revision_end > " + str(self.dbase.currentrevision)
                            sqltemp += " ELSE TRUE END "
                        elif self.dbase.dbasetype == 'spatialite':
                            sqltemp += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
                            sqltemp += " lpk_revision_end > " + str(self.dbase.currentrevision)
                            sqltemp += " ELSE 1 END"

                        query = self.dbase.query(sqltemp)

                        if len(query) > 0 :
                            idstemp = [str(row[0]) for row in query]
                            idssql = '(' + ','.join(idstemp) + ')'
                            sql += " AND " + linkagetemp['idsource'] + " IN " + idssql
                        else:
                            return ids

            sqlbeforepost = str(sql)
            sql = self.postloadIds(sql)
            if sql == sqlbeforepost and self.dbasetablename is not None:
                strid = 'id_' + self.dbasetablename.lower()
                sql += ' ORDER BY ' + strid

            sql += ';'
            query = self.dbase.query(sql)

            if query != None:
                ids = [row for row in query]
                i=0
                j=0
                res=[]
                for row in ids :
                    j=0
                    res=res+[[]]
                    for id in row :
                        if j>0:
                            res[i] += [self.dbase.getConstraintTextFromRawValue(self.dbasetablename,
                                                                                self.qtreewidgetfields[j - 1],
                                                                                ids[i][j])]
                        else :
                            res[i]+=[ids[i][j]]
                        j=j+1
                    i=i+1
                ids=res


        return ids

    def onDesactivation(self):
        pass

    def selectFeature(self,pk=None):
        self.selectItemfromPK(pk)

    def toolbarNew(self):
        self.disconnectTreewidget()
        self.toolwidget.frametoolwidg.setEnabled(True)
        parentitem = self.treewidget.invisibleRootItem()
        newitem = QTreeWidgetItem([self.NEWFEATURETXT])
        parentitem.addChildren([newitem])
        self.treewidget.setCurrentItem(newitem)
        #newitem.setSelected(True)
        self.connectTreewidget()

    def toolbarUndo(self):
        pass

    def toolbarDelete(self):
        if self.toolwidget.currentFeaturePK is None:    #feature not correctly saved
            return

        id = self.toolwidget.dbase.getValuesFromPk(self.toolwidget.DBASETABLENAME,
                                            'id_' + self.toolwidget.DBASETABLENAME.lower(),
                                            self.toolwidget.currentFeaturePK)
        founditems = self.treewidget.findItems(str(id), 
                                                QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 
                                                0)
        if len(founditems)>0:
            idx = self.treewidget.invisibleRootItem().indexOfChild(founditems[0])
            self.treewidget.invisibleRootItem().takeChild(idx)
            # self.ids.remove(id)
            self.ids = self.ids[self.ids.id != id]

    def toolbarSave(self):
        #if self.toolwidget.currentFeaturePK is None:    #feature not correctly saved
        #    return
        
        self.disconnectTreewidget()
        selecteditems = self.treewidget.selectedItems()
        #if len(selecteditems) > 0 and selecteditems[0].text(0) == self.NEWFEATURETXT:
        if len(selecteditems) > 0 :
            fieldtorequest = ['id_' + self.toolwidget.DBASETABLENAME.lower()]
            if hasattr(self.toolwidget, 'CHOOSERTREEWDG_COLSHOW') :
                fieldtorequest += self.toolwidget.CHOOSERTREEWDG_COLSHOW

            res = self.toolwidget.dbase.getValuesFromPk(self.toolwidget.DBASETABLENAME + '_qgis',
                                                        fieldtorequest,
                                                        self.toolwidget.currentFeaturePK)
            if isinstance(res, int):
                res = [res]
            res = [self.toolwidget.currentFeaturePK] + list(res)
            if selecteditems[0].text(0) == self.NEWFEATURETXT:
                self.ids.append(res)
            else:
                self.ids.loc[self.ids['pk'] == self.toolwidget.currentFeaturePK] = res


            selecteditem = selecteditems[0]
            for i, val in enumerate(res[1:]):
                selecteditem.setText(i, str(val))
            #self.ids.append([self.toolwidget.currentFeaturePK, id])
            #self.ids.append((id,))
            #
            #if self.ids.index.max() :
            #    self.ids.loc[self.ids.index.max()+1].append([id])
            #else:
            #    self.ids.loc[0].append([id])
        self.connectTreewidget()


    def qtreeitemSelected(self, **kwargs):
        currentiditem = self.treewidget.currentItem().text(0)
        if currentiditem.isdigit():
            sql = "SELECT pk_{namelower} "\
                "FROM {name} WHERE id_{namelower} = {id}".format(name=self.toolwidget.DBASETABLENAME,
                                                                    namelower=self.toolwidget.DBASETABLENAME.lower(),
                                                                    id= currentiditem  )

            pk = self.toolwidget.dbase.query(sql)[0][0]
            self.toolwidget.selectFeature(pk=pk)

    def disconnectTreewidget(self):
        try:
            self.treewidget.itemSelectionChanged.disconnect()
        except TypeError:
            pass


    def connectTreewidget(self):
        pass
        self.treewidget.itemSelectionChanged.connect(self.qtreeitemSelected)

    