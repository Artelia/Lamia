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
import numpy as np
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
        self.resultlayer = qgis.core.QgsVectorLayer("None", "result", "memory")
        # self.qgiscanvas.layers["mcaresultlayer"] = {}
        # self.qgiscanvas.layers["mcaresultlayer"]["qgislayer"] = resultlayer
        # project = qgis.core.QgsProject.instance()
        # if project:
        #     project.addMapLayer(
        #         self.qgiscanvas.layers["mcaresultlayer"]["qgislayer"], False
        #     )

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
            if isinstance(subdict, dict) and idx.isdigit():
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

    def checkVLayerUpdate(self, confname, jsondict=None):
        if not jsondict:
            jsondict = self.getJsonDict(confname)
        fromupdate, selectupdate = self.mcavirtualayerFactory.checkVLayerUpdate(
            jsondict
        )
        return fromupdate, selectupdate

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

    def computeNodeScore(self, confname, jsondict=None, nodeid=None):
        self.mcavirtualayerFactory.setConfName(confname)
        fromup, selectup = self.checkVLayerUpdate(confname, jsondict)
        if not fromup or not selectup:
            print("update first")
            return None
        if not jsondict:
            jsondict = self.getJsonDict(confname)
        subdict = jsondict
        if nodeid:
            for i in range(1, len(nodeid) + 1):
                subdict = subdict[nodeid[0:i]]

        data, resultqgslayer = self.mcavirtualayerFactory.createMcaDB(jsondict)

        dfresult = McaScoreCalculation(self).computeScore(data, subdict)
        return dfresult

    def getJsonSubJson(self, jsondict):
        res = {}
        for idx, subdict in jsondict.items():
            # if isinstance(subdict, dict) and idx.isdigit():
            if isinstance(subdict, dict) and idx != "bareme":
                res[idx] = subdict
        return res

    def joinResultToQgslayer(self, confname, results):
        self.mcavirtualayerFactory.setConfName(confname)
        # datas, resultqgslayer = self.mcavirtualayerFactory.createMcaDB(jsondict)
        self.resultlayer = self.mcavirtualayerFactory.createResultQgsLayer(results)

        maintablename = results.columns[0]
        maintablename = maintablename.split(".")[0].split("_")[0]
        qgislayer = self.qgiscanvas.layers[maintablename]["layerqgis"]

        for join in qgislayer.vectorJoins():
            qgislayer.removeJoin(join.joinLayerId())

        joinObject = qgis.core.QgsVectorLayerJoinInfo()
        joinObject.setJoinFieldName("amc_pk")
        joinObject.setTargetFieldName("pk_" + maintablename)
        joinObject.setJoinLayerId(self.resultlayer.id())
        joinObject.setUsingMemoryCache(True)
        joinObject.setJoinLayer(self.resultlayer)

        qgislayer.addJoin(joinObject)

        target_field = "result_amc_val"
        myRangeList = []

        myRenderer = qgis.core.QgsGraduatedSymbolRenderer()
        # symbol
        if qgislayer.geometryType() == qgis.core.QgsWkbTypes.PointGeometry:
            symbol = qgis.core.QgsMarkerSymbol()
            symbol.setSize(3.0)
            symbol.setSizeUnit(qgis.core.QgsUnitTypes.RenderMillimeters)
        elif qgislayer.geometryType() == qgis.core.QgsWkbTypes.LineGeometry:
            symbol = qgis.core.QgsLineSymbol()
            symbol.setWidth(2.0)
            symbol.setSizeUnit(qgis.core.QgsUnitTypes.RenderMillimeters)
        elif qgislayer.geometryType() == qgis.core.QgsWkbTypes.PolygonGeometry:
            symbol = qgis.core.QgsFillSymbol()

        myRenderer.setSourceSymbol(symbol.clone())

        myStyle = qgis.core.QgsStyle().defaultStyle()
        defaultColorRampNames = myStyle.colorRampNames()
        ramp = myStyle.colorRamp("Spectral")
        ramp.invert()

        myRenderer.updateColorRamp(ramp)
        myRenderer.setClassAttribute("result_amc_val")
        myRenderer.setClassificationMethod(qgis.core.QgsClassificationEqualInterval())
        myRenderer.updateClasses(qgislayer, 5)

        qgislayer.setRenderer(myRenderer)
        qgislayer.repaintRequested.emit()


class McaScoreCalculation:
    def __init__(self, mcacore):
        self.mcacore = mcacore

    def computeScore(self, data, jsondict):
        scoredata = self._computeScoreRecursive(data, jsondict)
        finaldata = pd.DataFrame(data.iloc[:, 0])
        finaldata["result"] = scoredata
        return finaldata

    def _computeScoreRecursive(self, data, jsondict):
        subdicts = self.mcacore.getJsonSubJson(jsondict)
        if len(subdicts) > 0:  # node
            stockChildValue = pd.DataFrame()
            for ids, subdict in subdicts.items():
                weighting = subdict["weighting"] if "weighting" in subdict.keys() else 1
                if subdict["name"] in stockChildValue.columns:  # for no duplicate
                    columnname = subdict["name"] + "-" + str(ids)
                else:
                    columnname = subdict["name"]

                stockChildValue[columnname] = self._computeScoreRecursive(data, subdict)
                stockChildValue[columnname] = stockChildValue[columnname] * weighting

            stockChildValue["total"] = stockChildValue.sum(axis=1)
            return stockChildValue["total"]

        else:  # leaf
            return self._leafscorecalculation(data, jsondict)

    def _leafscorecalculation(self, data, subdict):
        dummyDF = pd.DataFrame()

        selects = subdict["select"].split(", ")
        bareme = subdict["bareme"]
        try:
            defaultValue = bareme["default"]
        except KeyError:
            defaultValue = 0
        except TypeError:
            defaultValue = 0

        for select in selects:
            dummyDF[select] = data[select]
        dftonumpy = dummyDF.values

        # Get type of columns of dftonumpy
        typelist = self.getTypeList(dftonumpy)
        res = []
        for line in dftonumpy:
            # on s'en tirera à coup de boucle for .... il y a peut etre mieux mais ca marche
            result = self.someFct(line, bareme, typelist, defaultValue)
            res.append(result)
        return pd.DataFrame(res).iloc[:, 0]

        # return dummyDF

    def calculus(self, node):
        # Get data
        # if hasattr(self, "createdataframe"):
        fromup, selectup = self.mcacore.checkVLayerUpdate(
            self.confname, self.getJsonDict()
        )
        if not fromup or not selectup or self.df is None:
            print("update DB first")
            return

        # if not self.createdataframe.getVirtualLayerUpdateStatus:
        #     self.createDataFrame()
        #     return None
        # else:
        #     if not self.createdataframe2.getVirtualLayerUpdateStatus:
        #         self.createDataFrame2()
        #         return None

        dummyDF = pd.DataFrame()

        # Get current selects
        selectsAsStr = self.treeWidget.itemWidget(node, 1)
        selects = selectsAsStr.text().split(", ")

        # Get bareme as dict
        bareme = self.getBareme(node)

        try:
            defaultValue = bareme["default"]
        except KeyError:
            defaultValue = 0
        except TypeError:
            defaultValue = 0

        # Create df with only selects from current line
        for select in selects:
            dummyDF[select] = self.df[select]

        dftonumpy = dummyDF.values

        # Get type of columns of dftonumpy
        typelist = self.getTypeList(dftonumpy)
        res = []
        for (
            line
        ) in (
            dftonumpy
        ):  # on s'en tirera à coup de boucle for .... il y a peut etre mieux mais ca marche
            result = self.someFct(line, bareme, typelist, defaultValue)
            res.append(result)

        return res

    def someFct(self, value, dct, typelist, defaultValue=0):
        """
        :param value: int, str, value to test
        :param dct: dict, bareme
        :return: int, evaluation of value in regards of dict
        """

        if len(typelist) > 0 and typelist[0] in [
            int,
            float,
            np.int8,
            np.int16,
            np.int32,
            np.int64,
            np.float32,
            np.float64,
        ]:
            for key in dct.keys():
                if (
                    isinstance(dct[key], dict) and value[0] <= dct[key]["value"]
                ):  # "value" in dct.keys() and
                    # if self.legitChildren(dct[key]):
                    if self.mcacore.getJsonSubJson(dct[key]):
                        return self.someFct(
                            value[1:],
                            # self.legitChildren2(dct[key]),
                            self.mcacore.getJsonSubJson(dct[key]),
                            typelist[1:],
                            defaultValue,
                        )
                    else:
                        return dct[key]["weighting"]

        elif len(typelist) > 0 and typelist[0] == str:
            for key in dct.keys():
                if self.mcacore.dbase.utils.isAttributeNull(value[0]):
                    value[0] = "None"
                if isinstance(dct[key], dict) and value[0] in dct[key]["value"]:
                    # if self.legitChildren(dct[key]):
                    if self.mcacore.getJsonSubJson(dct[key]):
                        return self.someFct(
                            value[1:],
                            # self.legitChildren2(dct[key]),
                            self.mcacore.getJsonSubJson(dct[key]),
                            typelist[1:],
                            defaultValue,
                        )
                    else:
                        return dct[key]["weighting"]

        try:
            return int(defaultValue)
        except ValueError:
            return 0
        except KeyError:
            return 0

    def getTypeList(self, df):
        typevalues = []
        dfT = df.transpose()
        for col in dfT:
            for elem in col:
                if not self.mcacore.dbase.utils.isAttributeNull(elem):
                    typevalues.append(type(elem))
                    break
        return typevalues


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

    def createResultQgsLayer(self, results):
        resultlayer = qgis.core.QgsVectorLayer("None", "result", "memory")
        resultlayer.startEditing()
        provider = resultlayer.dataProvider()
        provider.addAttributes(
            [
                qgis.core.QgsField("amc_pk", QtCore.QVariant.Int),
                qgis.core.QgsField("amc_val", QtCore.QVariant.Double),
            ]
        )
        resultlayer.updateFields()

        # maintable, pkmaintable = self.getMainTable()
        # maintablepks = self.df[maintable + "." + pkmaintable]
        featstosave = []
        # for i, pk in enumerate(maintablepks):
        for idx, row in results.iterrows():
            pk = row[0]
            score = row[1]
            feat = qgis.core.QgsFeature(resultlayer.fields())
            feat.setAttributes([int(pk), float(score)])
            featstosave.append(feat)
        resultlayer.addFeatures(featstosave)
        resultlayer.commitChanges()

        return resultlayer

    def createTable(self):
        if not os.path.isfile(self.filename):
            originalfile = os.path.join(
                os.path.dirname(Lamia.api.__file__), "assets", "DBase_ind0.sqlite"
            )
            shutil.copyfile(originalfile, self.filename)

            self.virtuallayerdbase.connectToDBase(slfile=self.filename)
            sql = "CREATE TABLE lamiaconfig (fromsql TEXT, selectsql TEXT)"
            res = self.virtuallayerdbase.query(sql)
            sql = "INSERT INTO  lamiaconfig (fromsql, selectsql) VALUES ('', '')"
            self.virtuallayerdbase.query(sql)
        else:
            self.virtuallayerdbase.connectToDBase(slfile=self.filename)
        self.emitMessage(".sqlite créé")

    def setStatus(self, newstatus):

        self.virtuallayerdbase.connectToDBase(slfile=self.filename)
        sql = "UPDATE 'lamiaconfig' SET updatestatus = '" + str(newstatus) + "'"
        self.virtuallayerdbase.query(sql)
        if newstatus == "True":
            self.dbasestatus.emit("DBase updated")
        else:
            self.dbasestatus.emit("DBase modified - needs an update")

    def testDB(self, jsondict=None):
        if not jsondict:
            jsondict = self.mcacore.getJsonDict(self.confname)

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

        # restrict query to fist row of main table
        # construct where clause

        sqlfinal = self._makeTestSql(jsondict, sqltxt)

        # self.starttime = time.time()
        # self.testsql = True  # before prepareVLayerScript
        # self.scriptvl = sqlfinal
        # self.qgsvectorlay = qgsvectorlay
        # self.createdataframe.filename = self.filevirtuallayer
        # self.thread.start()
        # self.buildResultLayer()
        sqlsplitted = self.mcacore.dbase.utils.splitSQLSelectFromWhereOrderby(sqlfinal)
        fromsql, selsql = self.getVirtualLayerUpdateStatus()
        if sqlsplitted["FROM"] != fromsql:
            self._importFromLayer(qgsvectorlay)
            self.virtuallayerdbase.query(
                f"UPDATE lamiaconfig SET fromsql='{sqlsplitted['FROM']}' "
            )

        res = self.virtuallayerdbase.query(sqlfinal)
        if res is not None:
            rawData = list(res)

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
        # build FROM part and get qgsvectorlayers needed
        # layersql, sentencesql = self._getSqlQgislayerFromTxt(sqlsict["final"])
        layersql, sentencesql = self._getSqlQgislayerFromTxt(jsondict["mainsql"])

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
                    tabletype, tablename = sqlsplitspace.split(".")[0:2]
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
                        vectorlayer = qgis.core.QgsVectorLayer(
                            self.mcacore.qgiscanvas.layers[rawtablename]["layerqgis"]
                            .dataProvider()
                            .uri()
                            .uri(),
                            tablenamevlayer,
                            "spatialite",
                        )
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

        return layersql, sentencesql

    def checkVLayerUpdate(self, jsondict):
        lay, jsonsql = self._getQgslayerSqlFromDict(jsondict)
        fromsql, selsql = self.getVirtualLayerUpdateStatus()
        sqlsplitted = self.mcacore.dbase.utils.splitSQLSelectFromWhereOrderby(jsonsql)
        fromupdate, selectupdate = True, True

        if sqlsplitted["FROM"] != fromsql:
            fromupdate = False

        if sqlsplitted["SELECT"] != selsql:
            selectupdate = False

        return fromupdate, selectupdate

    # def buildResultLayer(self):
    def createMcaDB(self, jsondict):
        lay, jsonsql = self._getQgslayerSqlFromDict(jsondict)
        fromsql, selsql = self.getVirtualLayerUpdateStatus()
        sqlsplitted = self.mcacore.dbase.utils.splitSQLSelectFromWhereOrderby(jsonsql)
        if sqlsplitted["FROM"] != fromsql:
            self._importFromLayer(lay)
            self.virtuallayerdbase.query(
                f"UPDATE lamiaconfig SET fromsql='{sqlsplitted['FROM']}' "
            )

        if sqlsplitted["SELECT"] != selsql:
            sql = "DROP TABLE results"
            self.virtuallayerdbase.query(sql)
            sql = "CREATE TABLE results AS  "
            sql += jsonsql
            self.virtuallayerdbase.query(sql)

            self.virtuallayerdbase.query(
                f"UPDATE lamiaconfig SET selectsql='{sqlsplitted['SELECT']}' "
            )

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
        # print("Tables importées")

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
        sql = "SELECT * FROM lamiaconfig"
        fromsql, selectsql = self.virtuallayerdbase.query(sql, docommit=False)[0]
        return fromsql, selectsql
        # if os.path.isfile(self.filename):
        #     self.virtuallayerdbase.connectToDBase(self.filename)
        #     sql = "SELECT updatestatus FROM 'Lamia.config'"
        #     res = self.virtuallayerdbase.query(sql, docommit=False)
        #     if res is not None:
        #         if res[0][0] == "True":
        #             return True
        #         else:
        #             return False
        #     else:
        #         return False
        # else:
        #     return False
