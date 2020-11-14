# -*- coding: utf-8 -*-

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


import os, importlib
from collections import OrderedDict
import sys, glob, inspect, logging, textwrap, re, time, json, shutil
import pandas as pd
import Lamia
from ..abstractlibslamia import AbstractLibsLamia

import qgis
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory


class McaCore(AbstractLibsLamia):

    POSTPROTOOLNAME = "lamiamca"
    SHOWSQL = False
    fileext = ".json"

    def __init__(self, dbaseparser, messageinstance=None, qgiscanvas=None):
        super(McaCore, self).__init__(dbaseparser, messageinstance)
        # self.virtuallayerdbase = DBaseParserFactory("spatialite").getDbaseParser()
        self.mcavirtualayerFactory = MCAVirtualLayerFactory(mcacore=self)
        self.qgiscanvas = qgiscanvas
        self.processlayerthread = QtCore.QThread()
        self.mcavirtualayerFactory.moveToThread(self.processlayerthread)
        # self.mcavirtualayerFactory.finished.connect(self.postVLayerProcessed)
        # self.mcavirtualayerFactory.finished.connect(self.processlayerthread.quit)
        # self.mcavirtualayerFactory.dbasestatus.connect(self.showStatus)
        # self.mcavirtualayerFactory.message.connect(self.appendMessage)
        # self.processlayerthread.started.connect(
        #     self.mcavirtualayerFactory.buildResultLayer
        # )

    def new(self, confpath):

        if not os.path.exists(self.confdatadirproject):
            os.mkdir(self.confdatadirproject)

        conf_file = open(confpath, "w", encoding="utf-8")
        conf_file.close()

    def getSqliteFileFromConf(self, configname):
        return os.path.splitext(self.getConfFilePath(configname))[0] + ".sqlite"

    def process(self, configname):
        pass

    def getJsonDict(self, jsonthing=None):
        if isinstance(jsonthing, dict):
            jsondict = jsonthing
        else:
            jsonpath = self.getConfFilePath(jsonthing)
            with open(jsonpath, "r") as file:
                jsondict = json.load(file)
        return jsondict

    def getSelects(self, jsonthing=None):
        jsondict = self.getJsonDict(jsonthing)
        maintable, pkmaintable = self.getMainTable(jsonthing)
        selects = [maintable + "." + pkmaintable]
        self._recursiveselect(jsondict, selects)
        finalselects = []
        for sel in selects:
            if sel not in finalselects:
                finalselects.append(sel)

        return finalselects

    def _recursiveselect(self, jsondict, result=None):
        # if result is None:
        #     result = []
        if "select" in jsondict.keys() and jsondict["select"]:
            result.append(jsondict["select"])
        for idx, subdict in jsondict.items():
            if isinstance(subdict, dict):
                print("*", subdict)
                self._recursiveselect(subdict, result)

    def getMainTable(self, jsonthing):
        jsondict = self.getJsonDict(jsonthing)
        # sqlfrom = self.lineEdit_sqlfinal.text()
        # sqlfrom = self.textBrowser_sqlfinal.toPlainText()
        sqlfrom = jsondict["mainsql"]

        maintable, pkmaintable = None, None
        for elem in re.split("([ ._])", sqlfrom):
            if elem in self.dbase.dbasetables.keys():
                maintable, pkmaintable = elem, "pk_" + str(elem).lower()
                break
        for elem in re.split("([ .])", sqlfrom):
            if maintable in elem:
                maintable = elem
                break

        return maintable, pkmaintable

    def testDB(self, confname, jsondict=None):
        if not jsondict:
            jsondict = self.getJsonDict(confname)
        self.mcavirtualayerFactory.setConfName(confname)
        success, message = self.mcavirtualayerFactory.testDB(jsondict)
        return success, message

    def createMcaDB(self, confname, jsondict=None):
        if not jsondict:
            jsondict = self.getJsonDict(confname)
        self.mcavirtualayerFactory.setConfName(confname)
        data, resultqgslayer = self.mcavirtualayerFactory.createMcaDB(jsondict)
        return data, resultqgslayer


class MCAVirtualLayerFactory(QtCore.QObject):

    finished = QtCore.pyqtSignal(list)
    dbasestatus = QtCore.pyqtSignal(str)
    message = QtCore.pyqtSignal(str)

    # def __init__(self, mcacore=None, confname=None, scriptvl=None, filename=None):
    def __init__(self, mcacore=None, confname=None, scriptvl=None):
        super(MCAVirtualLayerFactory, self).__init__()
        self.mcacore = mcacore

        self.scriptvl = scriptvl
        # self.filename = self.mcacore.getSqliteFileFromConf(confname)
        # self.virtuallayerdbase = DBaseParser()
        self.virtuallayerdbase = DBaseParserFactory("spatialite").getDbaseParser()
        self.testsql = False
        self.qgsvectorlay = None
        self.projectcrs = self.mcacore.dbase.crsnumber
        self.setConfName(confname)
        # self.createTable()

    def setConfName(self, confname):
        if confname:
            self.confname = confname
            self.filename = self.mcacore.getSqliteFileFromConf(confname)
            self.createTable()

    def createTable(self):
        if not os.path.isfile(self.filename):
            originalfile = os.path.join(
                os.path.dirname(Lamia.api.__file__), "assets", "DBase_ind0.sqlite"
            )
            shutil.copyfile(originalfile, self.filename)

            self.virtuallayerdbase.connectToDBase(slfile=self.filename)
            sql = "CREATE TABLE 'Lamia.config' (updatestatus TEXT)"
            res = self.virtuallayerdbase.query(sql)
            sql = "INSERT INTO  'Lamia.config' (updatestatus) VALUES ('False')"
            self.virtuallayerdbase.query(sql)
        else:
            self.virtuallayerdbase.connectToDBase(slfile=self.filename)
        self.emitMessage(".sqlite créé")

    def setStatus(self, newstatus):
        # print("**", self.filename)

        self.virtuallayerdbase.connectToDBase(slfile=self.filename)
        sql = "UPDATE 'Lamia.config' SET updatestatus = '" + str(newstatus) + "'"
        self.virtuallayerdbase.query(sql)
        if newstatus == "True":
            self.dbasestatus.emit("DBase updated")
        else:
            self.dbasestatus.emit("DBase modified - needs an update")

    def testDB(self, jsondict=None):
        if not jsondict:
            jsondict = self.mcacore.getJsonDict(self.confname)

        # selects = self.mcacore.getSelects(jsondict)
        # print("::", selects)
        # # selects = self.getSelects()
        # # print("::", selects)
        # if not selects:
        #     # self.appendMessage("sql not ok - do not find main table")
        #     # self.toolButton_updatedb.setEnabled(False)
        #     return False, "sql not ok - do not find main table"

        # sql = {
        #     # "final": self.lineEdit_sqlfinal.text(),
        #     # "final": sqlfinal,
        #     # "final": self.textBrowser_sqlfinal.toPlainText() + " LIMIT 1",
        #     "final": jsondict["mainsql"],
        #     "critere": selects,
        # }

        try:
            qgsvectorlay, sqltxt = self._getQgslayerSqlFromDict(jsondict)
        except Exception as e:
            # self.appendMessage("sql not ok")
            # self.toolButton_updatedb.setEnabled(False)
            return False, "sql not ok"

        if not sqltxt:
            # self.appendMessage("sql not ok - do not find main table")
            # self.toolButton_updatedb.setEnabled(False)
            return False, "sql not ok - do not find main table"
        print("sqltxt", sqltxt)

        # restrict query to fist row of main table
        # construct where clause

        sqlfinal = self._makeTestSql(jsondict, sqltxt)

        print("sqlfinal", sqlfinal)

        # self.starttime = time.time()
        # self.testsql = True  # before prepareVLayerScript
        # self.scriptvl = sqlfinal
        # self.qgsvectorlay = qgsvectorlay
        # self.createdataframe.filename = self.filevirtuallayer
        # self.thread.start()
        # self.buildResultLayer()

        self._importFromLayer(qgsvectorlay)

        res = self.virtuallayerdbase.query(sqlfinal)
        if res is not None:
            rawData = list(res)
        print("rawData", rawData)

        return True, "sql ok"

    def _makeTestSql(self, jsondict, sqltxt):
        maintable, pkmaintable = self.mcacore.getMainTable(jsondict)
        sql = "SELECT Min(" + pkmaintable + ") FROM " + maintable
        sql = self.mcacore.dbase.updateQueryTableNow(sql)
        res = self.mcacore.dbase.query(sql)
        sentence = maintable + "." + pkmaintable + " = " + str(res[0][0])
        # insert it in sql
        sqlsplitted = self.mcacore.dbase.utils.splitSQLSelectFromWhereOrderby(sqltxt)
        if "WHERE" in sqlsplitted.keys():
            sqlsplitted["WHERE"] += " AND " + sentence
        else:
            sqlsplitted["WHERE"] = sentence
        sqlfinal = self.mcacore.dbase.utils.rebuildSplittedQuery(sqlsplitted)

        sqlfinal += " LIMIT 1"

        return sqlfinal

    def _getQgslayerSqlFromDict(self, jsondict):
        """

        :param sqlsict:
        :return: sqlrequest, qgsvectorlayerslist
        """
        debug = False

        selects = self.mcacore.getSelects(jsondict)
        if not selects:
            return None, None
        layers = {}
        # build SELECT part
        sqlfinal = " SELECT "
        # for sql in sqlsict["critere"]:
        for sql in selects:
            layersql, sentencesql = self._getSqlQgislayerFromTxt(sql)
            for vlayername, vlayersql in layersql:
                if vlayername not in layers.keys():
                    layers[vlayername] = vlayersql
            sqlfinal += sentencesql + ", "
        sqlfinal = sqlfinal[:-2]
        print("analyseRawSQL", sqlfinal)
        # build FROM part and get qgsvectorlayers needed
        # layersql, sentencesql = self._getSqlQgislayerFromTxt(sqlsict["final"])
        layersql, sentencesql = self._getSqlQgislayerFromTxt(jsondict["mainsql"])
        print(layersql, sentencesql)

        sqlfinal += sentencesql
        sqlfinal = self.mcacore.dbase.updateQueryTableNow(sqlfinal)

        return layersql, sqlfinal

    def _getSqlQgislayerFromTxt(self, sql):
        """
        Preparing data to be inserted in a virtual layer - process the FROM part of sql sentence

        :param sql: sql sentence startig from FROM
        :return: layersql, sentencesql :
        * layer sql : list of [tablenamevlayer, vlayerlayer] : name of layer in virtual table , and associated qggsvectorlayer
        * sentencesql : text to be inserted in virtual layer creation
        """

        debug = False

        layersql, sentencesql = [], ""

        if "#" in sql:
            sqlssplitspace = sql.split(" ")
            for sqlsplitspace in sqlssplitspace:
                if "#" in sqlsplitspace:
                    print("*", sqlsplitspace)
                    # tabletype, tablename = sqlsplitspace.split(".")
                    tabletype, tablename = sqlsplitspace.split(".")[0:2]
                    # print(tabletype, tablename)
                    # print(self.qgiscanvas.layers)
                    vlayerlayer = ""
                    if tabletype == "#lamia":
                        if "_now" in tablename:
                            rawtablename = "_".join(tablename.split("_")[:-1])
                            tablenamevlayer = (
                                "_".join(tablename.split("_")[:-1]) + "_qgis"
                            )
                        elif "_qgis" in tablename:
                            rawtablename = "_".join(tablename.split("_")[:-1])
                            tablenamevlayer = (
                                "_".join(tablename.split("_")[:-1]) + "_qgis"
                            )
                        else:
                            rawtablename = tablename
                            tablenamevlayer = tablename
                        # print(
                        #     self.qgiscanvas.layers[rawtablename]["layerqgis"]
                        #     .dataProvider()
                        #     .uri()
                        #     .uri()
                        # )
                        vectorlayer = qgis.core.QgsVectorLayer(
                            self.mcacore.qgiscanvas.layers[rawtablename]["layerqgis"]
                            .dataProvider()
                            .uri()
                            .uri(),
                            tablenamevlayer,
                            "spatialite",
                        )
                        # print(vectorlayer, vectorlayer.isValid())
                        vectorlayer.setSubsetString("")

                    elif tabletype == "#lamiashp":
                        # searchfilepath of tablename
                        sql = (
                            "SELECT file FROM Rasters_now WHERE libelle = '"
                            + str(tablename)
                            + "'"
                        )
                        sql = self.dbase.updateQueryTableNow(sql)
                        res = self.dbase.query(sql)
                        if res and len(res) > 0:
                            shppath = res[0][0]
                            shpcompletepath = str(
                                self.dbase.completePathOfFile(shppath)
                            )
                            if sys.version_info.major == 3:
                                tablenamevlayer = tablename
                                vectorlayer = qgis.core.QgsVectorLayer(
                                    shpcompletepath, tablenamevlayer, "ogr"
                                )
                                vectorlayer.setProviderEncoding("UTF-8")

                    layersql.append([tablenamevlayer, vectorlayer])
                    sentencesql += " " + tablename

                else:
                    sentencesql += " " + sqlsplitspace
                    continue
        else:
            sentencesql = sql

        print("**", layersql, sentencesql)
        return layersql, sentencesql

    # def buildResultLayer(self):
    def createMcaDB(self, jsondict):
        lay, jsonsql = self._getQgslayerSqlFromDict(jsondict)
        self._importFromLayer(lay)

        sql = "DROP TABLE results"
        self.virtuallayerdbase.query(sql)
        sql = "CREATE TABLE results AS  "
        sql += jsonsql
        self.virtuallayerdbase.query(sql)

        sql = "SELECT * FROM results"
        rawData = self.virtuallayerdbase.query(sql)
        selects = self.mcacore.getSelects(jsondict)
        rawDataDf = self.cleanData(rawData, selects)

        uri = qgis.core.QgsDataSourceUri()
        uri.setDatabase(self.filename)
        # schema = ""
        # table = "results"
        # geom_column = ""
        uri.setDataSource("", "results", "")

        resultlayer = qgis.core.QgsVectorLayer(uri.uri(), "temp", "spatialite")
        resultlayer.setProviderEncoding("UTF-8")

        return rawDataDf, resultlayer

        if False:
            rawData = []
            if not self.testsql:
                self.dbasestatus.emit("DBase updating...")
                if os.path.isfile(self.filename):
                    # get update
                    self.virtuallayerdbase.connectToDBase(slfile=self.filename)
                    updated = self.getVirtualLayerUpdateStatus()

                    if updated:
                        pass
                    else:
                        self._importFromLayer()
                        sql = "DROP TABLE results"
                        self.virtuallayerdbase.query(sql)
                        sql = "CREATE TABLE results AS  "
                        sql += self.scriptvl
                        self.virtuallayerdbase.query(sql)
                else:
                    self.createTable()

                # * get resultts
                sql = "SELECT * FROM result"
                rawData = self.virtuallayerdbase.query(sql)

                uri = qgis.core.QgsDataSourceUri()
                uri.setDatabase(self.filename)
                # schema = ""
                # table = "results"
                # geom_column = ""
                uri.setDataSource("", "results", "")

                resultlayer = qgis.core.QgsVectorLayer(uri.uri(), "temp", "spatialite")
                resultlayer.setProviderEncoding("UTF-8")

                return rawData, resultlayer

                # for fet in resultlayer.getFeatures():
                #     # self.textBrowser_res.append(str(fet.attributes()))
                #     rawData.append(fet.attributes())

            # else:
            #     if not os.path.isfile(self.filename):
            #         self.createTable()
            #     # another test
            #     self.virtuallayerdbase.connectToDBase(slfile=self.filename)
            #     sql = "SELECT updatestatus FROM  'Lamia.config'"
            #     res = self.virtuallayerdbase.query(sql)
            #     if res is None:
            #         self.createTable()
            #     self._importFromLayer()
            #     self.virtuallayerdbase.connectToDBase(slfile=self.filename)
            #     # self.virtuallayerdbase.errorquerymessage.connect(self.emitMessage)
            #     # self.virtuallayerdbase.messageinstance.showErrorMessage()
            #     # self.emitMessage("Debut de la requete ... ")
            #     sql = self.scriptvl
            #     res = self.virtuallayerdbase.query(sql)
            #     if res is not None:
            #         rawData = list(res)
            #     # self.virtuallayerdbase.errorquerymessage.disconnect(self.emitMessage)

            # self.finished.emit(rawData)

    def postVLayerProcessed_old(self, rawdata):
        """
         Called when the creation of virtual layer is done
         :param rawdata: list of results of sql request
         """

        selects = self.mcacore.getSelects(self.getJsonDict())
        rawdatadf = None
        if self.createdataframe.testsql:
            self.createdataframe.testsql = False
            self.appendMessage(" : " + "results : ")
            if len(rawdata) > 0:
                tempdf = pd.DataFrame(rawdata)
                tempdf.columns = selects
                txttoshow = str(tempdf)
                self.appendMessage(txttoshow)
                self.toolButton_updatedb.setEnabled(True)
            else:
                txttoshow = "Requete mal construite"
                self.toolButton_updatedb.setEnabled(False)
                self.appendMessage(txttoshow)
                sql = {
                    # "final": self.lineEdit_sqlfinal.text(),
                    "final": self.textBrowser_sqlfinal.toPlainText(),
                    "critere": selects,
                }
                scriptvl, sqltxt = self.prepareVLayerScript(sql)
                # self.appendMessage(scriptvl)
                self.appendMessage(sqltxt)

        else:
            rawdatadf = self.cleanData(rawdata, selects)

        return rawdatadf
        # pprint(self.df)
        # self.createdataframe.setStatus("True")

        # if self.starttime is not None:
        #     self.appendMessage(
        #         "end update  "
        #         + str(round(time.time() - self.starttime, 2))
        #         + " seconds"
        #     )
        #     self.starttime = None

    def cleanData(self, rawdata, selects):
        """
        Clean data, dataFrame and rename headers
        :param rawdata: 2D array,
        :param selects: list, selects (columns name)
        """
        df = pd.DataFrame(rawdata)
        nbrecolumn1 = len(df.columns)
        nbrecolumn2 = len(selects)
        # Rename self.df headers
        if nbrecolumn1 == nbrecolumn2:
            df.columns = selects
        else:
            print("Error cleaing datas")
            pprint(df)
            print(selects)
        return df

    def emitMessage(self, message):
        self.message.emit(message)

    def _importFromLayer(self, qgsvectorlay):

        self.virtuallayerdbase.connectToDBase(slfile=self.filename)

        for layname, lay in qgsvectorlay:
            # saveresults
            options = qgis.core.QgsVectorFileWriter.SaveVectorOptions()
            if os.path.isfile(self.filename):
                options.actionOnExistingFile = (
                    qgis.core.QgsVectorFileWriter.CreateOrOverwriteLayer
                )
            options.layerName = layname
            options.driverName = "sqlite"
            options.fileEncoding = "UTF-8"
            try:
                writer = qgis.core.QgsVectorFileWriter.writeAsVectorFormat(
                    lay, self.filename, options
                )
            except exception as e:
                print("error import in vlayer", e)

        self.emitMessage("Tables importées")
        print("Tables importées")

    def writeResults(self, vlayer, filename):
        # saveresults
        options = qgis.core.QgsVectorFileWriter.SaveVectorOptions()
        options.actionOnExistingFile = (
            qgis.core.QgsVectorFileWriter.CreateOrOverwriteLayer
        )
        options.layerName = "results"
        options.driverName = "sqlite"
        options.fileEncoding = "UTF-8"
        writer = qgis.core.QgsVectorFileWriter.writeAsVectorFormat(
            vlayer, filename, options
        )

    def getVirtualLayerUpdateStatus(self):
        if os.path.isfile(self.filename):
            self.virtuallayerdbase.connectToDBase(self.filename)
            sql = "SELECT updatestatus FROM 'Lamia.config'"
            res = self.virtuallayerdbase.query(sql, docommit=False)
            if res is not None:
                if res[0][0] == "True":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
