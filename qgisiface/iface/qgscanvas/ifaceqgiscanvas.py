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
import os, sys, io, logging, datetime, re, json, platform
import qgis, qgis.core, qgis.utils, qgis.gui
from qgis.PyQt import QtGui, QtCore
import Lamia.config
from ..ifaceabstractcanvas import LamiaAbstractIFaceCanvas
from .maptool.mapTools import mapToolCapture, mapToolEdit


class QgisCanvas(LamiaAbstractIFaceCanvas):
    """Class managing what happens in gis 2D map. It manages mainly:
        - the layers displayed
        - the click in the draw area
        - all crs transformation
        - rubberband (temp displayed layer)
        Here, no dbase in class var, and as few qt as possible
    """

    def __init__(self, canvas=None):
        """[summary]

        :param canvas: The qgismapcanvas used (either from qgsproject or specific one), defaults to None
        :type canvas: QgsMapCanvas, optional
        """

        LamiaAbstractIFaceCanvas.__init__(self)
        self.canvas = canvas
        self.mtooltorestore = None
        self.mtoolpoint = None
        self.mtoolline = None
        self.mtoolpolygon = None

        self.mtoolPan = None

        self.currentmaptool = None  # the maptool in use

        self.maptools = {
            "mtooltorestore": self.mtooltorestore,
            "mtoolpoint": self.mtoolpoint,
            "mtoolline": self.mtoolline,
            "mtoolpolygon": self.mtoolpolygon,
            "mtoolPan": self.mtoolPan,
            "currentmaptool": self.currentmaptool,
        }

        self.rubberbands = {"main": None, "child": None, "capture": None}

        # self.rubberBand = None          #the main parent ruberband
        # self.rubberbandchild = None     #the child rubberband
        # self.rubberbandcapture = None   #the capture rubberband
        self.dbaseqgiscrs = None

        if canvas is None and qgis.utils.iface is not None:
            self.setCanvas(qgis.utils.iface.mapCanvas())
        elif canvas is None and qgis.utils.iface is None:
            canvas = qgis.gui.QgsMapCanvas()
            canvas.enableAntiAliasing(True)
            canvascrs = qgis.core.QgsCoordinateReferenceSystem()
            canvascrs.createFromString("EPSG:2154")
            canvas.setDestinationCrs(canvascrs)
            self.setCanvas(canvas)

        self.layers = {}
        self.qgislegendnode = None

        self.xform = None
        self.xformreverse = None

        # behaviour
        self.editingrawlayer = None

    def setCanvas(self, qgscanvas):
        """Init method when a canvas is assigned to this class

        :param qgscanvas: The qgismapcanvas used 
        :type qgscanvas: QgsMapCanvas
        """
        if self.canvas:
            try:
                self.canvas.destinationCrsChanged.disconnect(
                    self.updateQgsCoordinateTransform
                )
            except TypeError:
                pass

        self.canvas = qgscanvas

        # init maptools
        self.cadwdg = qgis.gui.QgsAdvancedDigitizingDockWidget(self.canvas)
        self.cadwdg.enable()
        self.mtoolpoint = mapToolCapture(
            self.canvas, self.cadwdg, qgis.gui.QgsMapToolCapture.CapturePoint
        )
        self.mtoolline = mapToolCapture(
            self.canvas, self.cadwdg, qgis.gui.QgsMapToolCapture.CaptureLine
        )
        self.mtoolpolygon = mapToolCapture(
            self.canvas, self.cadwdg, qgis.gui.QgsMapToolCapture.CapturePolygon
        )
        self.pointEmitter = qgis.gui.QgsMapToolEmitPoint(self.canvas)
        self.pointEmitter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.mtoolPan = qgis.gui.QgsMapToolPan(self.canvas)

        self.updateQgsCoordinateTransform()

        self.canvas.destinationCrsChanged.connect(self.updateQgsCoordinateTransform)
        self.canvas.mapToolSet.connect(self.toolsetChanged)

        self.currentmaptool = self.mtoolPan
        self.mtooltorestore = self.currentmaptool

    def ____________layersManagement(self):
        pass

    def createLayersForQgisServer(self, dbaseparser, specifichost=None):
        """used for creating a qgis project configured for using in postgis server

        :param dbaseparser: The dbase parser to work with
        :param specifichost: if host for pg_config.conf is not the same as postgis host (docker use)
        """

        if dbaseparser.TYPE == "spatialite":
            return
        # * create pg_config.conf

        # [qgisservertest]
        # host=docker.for.win.localhost
        # port=5432
        # user=pvr
        # password=pvr
        # dbname=lamiaunittest

        dbqgisserverdirectory = os.path.join(
            dbaseparser.dbaseressourcesdirectory, "qgisserver"
        )
        if not os.path.isdir(dbqgisserverdirectory):
            os.mkdir(dbqgisserverdirectory)

        pg_configfile = os.path.join(dbqgisserverdirectory, "pg_service.conf")

        filewriter = open(pg_configfile, "w", newline="\n")
        dbaseconf = dbaseparser.connectconf
        filewriter.write("[qgisserver]\n")
        if specifichost:
            filewriter.write("host=" + specifichost + "\n")
        else:
            filewriter.write("host=" + dbaseconf["host"] + "\n")
        filewriter.write("port=" + dbaseconf["port"] + "\n")
        filewriter.write("user=" + dbaseconf["user"] + "\n")
        filewriter.write("password=" + dbaseconf["password"] + "\n")
        filewriter.write("dbname=" + dbaseconf["dbname"] + "\n")
        filewriter.close()

        # SET PGSERVICEFILE=C:\PGSERVICEFILE\pg_service.conf

        # create project with layers inside
        layers = {}
        project = qgis.core.QgsProject.instance()
        projectcrs = qgis.core.QgsCoordinateReferenceSystem()
        projectcrs.createFromString("EPSG:" + str(dbaseparser.crsnumber))
        project.setCrs(projectcrs)

        print(project.dataDefinedServerProperties().referencedFields())

        return

        for rawtablename, rawdict in dbaseparser.dbasetables.items():
            # if 'geom' not in rawdict:
            #     continue
            tablenames = [rawtablename]
            tabletypes = ["layer"]
            if "djangoviewsql" in rawdict.keys():
                tabletypes += ["layerdjango"]
                tablenames += [rawtablename + "_django"]
            if "qgisPGviewsql" in rawdict.keys() or "qgisviewsql" in rawdict.keys():
                tabletypes += ["layerqgis"]
                tablenames += [rawtablename + "_qgis"]

            layers[rawtablename] = {}
            for i, tablename in enumerate(tablenames):
                tablenamelower = tablename.lower()
                tabletype = tabletypes[i]
                # rawlayers
                uri = qgis.core.QgsDataSourceUri()
                uri.setConnection(
                    "qgisserver",  # the service name
                    dbaseparser.pgdb.lower(),
                    dbaseparser.pguser,
                    dbaseparser.pgpassword,
                    qgis.core.QgsDataSourceUri.SslDisable,
                )

                if dbaseparser.isTableSpatial(tablenamelower):
                    uri.setDataSource(
                        dbaseparser.pgschema.lower(),
                        str(tablenamelower),
                        "geom",
                        "",
                        "pk_" + rawtablename.lower(),
                    )
                    geomtype = dbaseparser.dbasetables[rawtablename]["geom"]
                    if geomtype == "POINT":
                        qgsgeomtype = qgis.core.QgsWkbTypes.Point
                    elif geomtype == "LINESTRING":
                        qgsgeomtype = qgis.core.QgsWkbTypes.LineString
                    elif geomtype == "MULTIPOLYGON":
                        qgsgeomtype = qgis.core.QgsWkbTypes.MultiPolygon
                    # print(geomtype)
                    uri.setWkbType(qgsgeomtype)
                    uri.setSrid(str(dbaseparser.crsnumber))
                else:
                    uri.setDataSource(
                        dbaseparser.pgschema.lower(),
                        str(tablenamelower),
                        None,
                        "",
                        "pk_" + rawtablename.lower(),
                    )
                layers[rawtablename][tabletype] = qgis.core.QgsVectorLayer(
                    uri.uri(), tablename, "postgres"
                )
                layers[rawtablename][tabletype].dataProvider().setEncoding("UTF-8")
                layers[rawtablename][tabletype].setCrs(projectcrs)

        # load layers and set style
        root = project.layerTreeRoot()
        styledirectory = self._getStyleDirectory(dbaseparser.worktype)
        if dbaseparser.base3version:
            defaultstyledirectory = os.path.join(styledirectory, "0_default",)
        else:
            defaultstyledirectory = os.path.join(styledirectory, "0_Defaut",)

        for tablename in layers:
            if (
                "layerqgis"
                in layers[tablename].keys()
                # and layers[tablename]["layerqgis"].geometryType()
                != qgis.core.QgsWkbTypes.NullGeometry
            ):
                stylesdir = [
                    os.path.basename(f.path)
                    for f in os.scandir(styledirectory)
                    if f.is_dir()
                ]

                for styledir in stylesdir:

                    stylepath = os.path.normpath(
                        os.path.join(styledirectory, styledir, tablename + ".qml")
                    )
                    if os.path.isfile(stylepath):
                        print(
                            "stylepath",
                            tablename,
                            stylepath,
                            layers[tablename][
                                "layerqgis"
                            ].wkbType(),  # wkbType()  geometryType()
                        )
                        stylemng = layers[tablename]["layerqgis"].styleManager()
                        xmldata = None
                        with open(stylepath, "r", encoding="utf8") as xmlfile:
                            xmldata = xmlfile.read()
                        stylemng.addStyle(styledir, qgis.core.QgsMapLayerStyle(xmldata))
                        # txt, res = layers[tablename]["layerqgis"].loadNamedStyle(
                        #     stylepath, qgis.core.QgsMapLayer.Symbology
                        # )
                        # stylemng.
                        # print(txt, res)
                project.addMapLayer(layers[tablename]["layerqgis"], True)
                # root.addLayer(layers[tablename]["layerqgis"])
                # root.addLayer(layers[tablename]['layerqgis'])
                # stylepath = os.path.join(styledirectory, tablename + '.qml')
                # stylepath = os.path.realpath(stylepath)
                layers[tablename]["layerqgis"].triggerRepaint()
                layers[tablename]["layerqgis"].dataProvider().reloadData()

        if self.canvas:
            self.canvas.refreshAllLayers()
            self.canvas.refresh()

        if False:
            for tablename in layers:
                if (
                    "layerqgis"
                    in layers[tablename].keys()
                    # and layers[tablename]["layerqgis"].geometryType()
                    # != qgis.core.QgsWkbTypes.NullGeometry
                ):
                    stylepath = os.path.normpath(
                        os.path.join(defaultstyledirectory, tablename + ".qml")
                    )
                    print("stylepath", stylepath)
                    if os.path.isfile(stylepath):
                        print("ok")
                        txt, res = layers[tablename]["layerqgis"].loadNamedStyle(
                            stylepath, loadFromLocalDb=False
                        )
                        if (
                            False and not res
                        ):  # TODO style do not apply arg !!!!! geometryType() not recognized
                            print(stylepath, os.path.isfile(stylepath))
                            print(layers[tablename]["layerqgis"].geometryType())
                            print(
                                layers[tablename]["layerqgis"].dataProvider().wkbType()
                            )
                            print(txt, res)

        projectfile = os.path.join(dbqgisserverdirectory, "project.qgs")
        project.write(projectfile)

        propro = qgis.core.QgsProject.instance()
        propro.read(projectfile)
        print(propro.fileName())

        # layers = QgsProject.instance().mapLayers()
        for layid in propro.mapLayers():
            # print(lay)

            lay = propro.mapLayer(layid)
            db = lay.dataProvider()
            print(lay.featureCount())
            print(db.uri().wkbType(), lay.wkbType())

            # print("la", lay.name(), lay.wkbType())
            stylepath = os.path.normpath(
                os.path.join(defaultstyledirectory, lay.name().split("_")[0] + ".qml")
            )

            if False and os.path.isfile(stylepath):
                print(stylepath)
                txt, res = lay.loadNamedStyle(stylepath, loadFromLocalDb=False)
                print(txt, res)

        project.clear()

        # finaly write dbasedbasetables
        jsonfile = os.path.join(dbqgisserverdirectory, "dbasetables.json")
        with open(jsonfile, "w") as outfile:
            json.dump(dbaseparser.dbasetables, outfile, indent=2)

    def createLayers(self, dbaseparser, alsoqgisjoined=True):
        """create QgsVectorLayer from dbaseparser database
        store the in self.layers :
        dict {... {rawtablename : {'layer' : the qgis layer without parent join,
                                                'layerqgis': the qgis layer from qgis view,
                                                'layerdjango': the django layer from django view,
                                        }
                }
        :param dbaseparser: the dbaseparser used

        """

        debug = False

        if dbaseparser.__class__.__name__ == "SpatialiteDBaseParser":
            dbtype = "spatialite"
        elif dbaseparser.__class__.__name__ == "PostGisDBaseParser":
            dbtype = "postgres"

        for rawtablename, rawdict in dbaseparser.dbasetables.items():
            # old way for qgislayer
            # if 'geom' not in rawdict:
            #     continue
            if debug:
                logging.getLogger(__name__).debug(f"createLayers {rawtablename}")

            tablenames = [rawtablename]
            tabletypes = ["layer"]
            if "djangoviewsql" in rawdict.keys():
                tabletypes += ["layerdjango"]
                tablenames += [rawtablename + "_django"]
            if "qgisPGviewsql" in rawdict.keys() or "qgisviewsql" in rawdict.keys():
                tabletypes += ["layerqgis"]
                tablenames += [rawtablename + "_qgis"]

            self.layers[rawtablename] = {}
            for i, tablename in enumerate(tablenames):
                tablenamelower = tablename.lower()
                tabletype = tabletypes[i]
                # rawlayers
                uri = qgis.core.QgsDataSourceUri()
                if dbtype == "spatialite":
                    uri.setDatabase(dbaseparser.spatialitefile)
                    if dbaseparser.isTableSpatial(tablename):
                        uri.setDataSource("", str(tablename), "geom")
                    else:
                        uri.setDataSource("", str(tablename), "")
                elif dbtype == "postgres":
                    uri.setConnection(
                        dbaseparser.pghost,
                        # "docker.for.win.localhost",
                        str(dbaseparser.pgport),
                        # dbaseparser.pgport,
                        dbaseparser.pgdb.lower(),
                        dbaseparser.pguser,
                        dbaseparser.pgpassword,
                    )
                    if dbaseparser.isTableSpatial(tablenamelower):
                        uri.setDataSource(
                            dbaseparser.pgschema.lower(),
                            str(tablenamelower),
                            "geom",
                            "",
                            "pk_" + rawtablename.lower(),
                        )
                    else:
                        uri.setDataSource(
                            dbaseparser.pgschema.lower(),
                            str(tablenamelower),
                            None,
                            "",
                            "pk_" + rawtablename.lower(),
                        )

                self.layers[rawtablename][tabletype] = qgis.core.QgsVectorLayer(
                    uri.uri(), tablename, dbtype
                )
                if debug:
                    # print("createLayers raw created", rawtablename)
                    logging.getLogger(__name__).debug(
                        f"createLayers {tablename} {uri.uri()}"
                    )
                    logging.getLogger(__name__).debug(
                        f"createLayers isvalid : {self.layers[rawtablename][tabletype].isValid()}"
                    )

            # ValueMap for qgislayer - not done because layer loading is too long
            if "layerqgis" in self.layers[rawtablename].keys():
                workingvl = self.layers[rawtablename]["layerqgis"]
                cstdict = self._getConstraintFromDBaseTables(dbaseparser, rawtablename)
                for i, field in enumerate(workingvl.fields()):
                    if field.name() in cstdict.keys():
                        config = {"map": cstdict[field.name()]}
                        widget_setup = qgis.core.QgsEditorWidgetSetup(
                            "ValueMap", config
                        )
                        workingvl.setEditorWidgetSetup(i, widget_setup)

                if debug:
                    print("createLayers qgisview created", rawtablename)

            # new way for qgislayer
            tabletype = "layerqgisjoined"
            # self.layers[rawtablename][tabletype] = qgis.core.QgsVectorLayer(self.layers[rawtablename]['layer'] )
            if (
                alsoqgisjoined and platform.system() == "Windows"
            ):  # bug with ubuntu when cloning
                self.layers[rawtablename][tabletype] = self.layers[rawtablename][
                    "layer"
                ].clone()

                currentlayername = rawtablename

                for parentable in dbaseparser.getParentTable(rawtablename):
                    currentField = "lpk_" + parentable.lower()
                    joinedField = "pk_" + parentable.lower()
                    joinObject = qgis.core.QgsVectorLayerJoinInfo()
                    joinObject.setJoinFieldName(joinedField)
                    joinObject.setTargetFieldName(currentField)
                    joinObject.setJoinLayerId(self.layers[parentable]["layer"].id())
                    joinObject.setUsingMemoryCache(True)
                    joinObject.setJoinLayer(self.layers[parentable]["layer"])
                    joinObject.setEditable(True)
                    joinObject.setPrefix("")
                    joinObject.setDynamicFormEnabled(True)
                    self.layers[rawtablename][tabletype].addJoin(joinObject)
                    currentlayername = parentable

                # ValueMap for qgislayerjoined
                workingvl = self.layers[rawtablename]["layerqgisjoined"]
                cstdict = self._getConstraintFromDBaseTables(dbaseparser, rawtablename)
                for i, field in enumerate(workingvl.fields()):
                    if field.name() in cstdict.keys():
                        config = {"map": cstdict[field.name()]}
                        widget_setup = qgis.core.QgsEditorWidgetSetup(
                            "ValueMap", config
                        )
                        workingvl.setEditorWidgetSetup(i, widget_setup)

        self.dbaseqgiscrs = qgis.core.QgsCoordinateReferenceSystem()
        self.dbaseqgiscrs.createFromString("EPSG:" + str(dbaseparser.crsnumber))
        self.updateQgsCoordinateTransform()

    def _getConstraintFromDBaseTables(self, dbaseparser, tablename):
        dictcst = {}
        parenttables = dbaseparser.getParentTable(tablename) + [tablename]
        parenttables = parenttables[::-1]
        for tablename in parenttables:
            for fieldname, fielddict in dbaseparser.dbasetables[tablename][
                "fields"
            ].items():
                if "Cst" in fielddict:
                    valuesformap = [[lst[0], lst[1]] for lst in fielddict["Cst"]]
                    qgisvaluesformat = [{var[0]: var[1]} for var in valuesformap]
                    dictcst[fieldname] = qgisvaluesformat
        return dictcst

    def createSingleQgsVectorLayer(
        self,
        dbaseparser,
        tablename="tempvectorlayer",
        isspatial=True,
        sql="",
        tableid=None,
    ):
        layer = None

        if tableid is not None:
            finaltableid = tableid
        else:
            finaltableid = "id_" + str(tablename.lower())
        if dbaseparser.__class__.__name__ == "SpatialiteDBaseParser":
            dbtype = "spatialite"
        elif dbaseparser.__class__.__name__ == "PostGisDBaseParser":
            dbtype = "postgres"

        uri = qgis.core.QgsDataSourceUri()

        if dbtype == "spatialite":
            # uri.setDataSource("public","japan_ver52","the_geom","","gid")
            # uri.setDataSource("",sql,"the_geom","","gid")
            uri.setDatabase(dbaseparser.spatialitefile)
            if isspatial:
                uri.setDataSource("", f"({sql})", "geom", "", finaltableid)
            else:
                uri.setDataSource("", f"({sql})", "", "", finaltableid)

            layer = qgis.core.QgsVectorLayer(uri.uri(), tablename, "spatialite")

        elif dbtype == "postgres":
            uri.setConnection(
                dbaseparser.pghost,
                str(dbaseparser.pgport),
                dbaseparser.pgdb.lower(),
                dbaseparser.pguser,
                dbaseparser.pgpassword,
            )

            # qgis bug _ need to add schema name
            sqlsplitted = re.split("[ \n]", sql)
            finalsql = []
            for word in sqlsplitted:
                if (
                    word.split(".")[0].split("_qgis")[0]
                    in dbaseparser.dbasetables.keys()
                ):
                    word = dbaseparser.pgschema.lower() + "." + word
                finalsql.append(word)
            finalsql = " ".join(finalsql)

            if isspatial:
                # uri.setDataSource(dbaseparser.pgschema.lower(), str(tablenamelower), 'geom', '', "pk_" + rawtablename.lower())
                # uri.setDataSource(dbaseparser.pgschema.lower(), f'({sql})', 'geom','' , finaltableid)
                uri.setDataSource("", f"({finalsql})", "geom", "", finaltableid)
            else:
                # uri.setDataSource(dbaseparser.pgschema.lower(), f'({sql})', None, '' , finaltableid )
                uri.setDataSource("", f"({finalsql})", None, "", finaltableid)

            layer = qgis.core.QgsVectorLayer(uri.uri(), tablename, "postgres")
        """
        uri = qgis.core.QgsDataSourceUri()
        uri.setConnection('localhost', 
                        '5432', 
                        'lamiaunittest', 
                        'pvr', 
                        'pvr')
        sql = "SELECT * FROM Infralineaire"
        print(f'({sql})')
        uri.setDataSource('', f'({sql})' , 'geom' ,'','pk_infralineaire')
        uri.setSchema('base2_digue_lamia')
        #base2_digue_lamia
        layer = qgis.core.QgsVectorLayer(uri.uri(), 'tt', 'postgres')
        print(uri.uri())
        QgsProject.instance().addMapLayer(layer)
        print([fet.id() for fet in layer.getFeatures()])
        """

        return layer

    def loadLayersInCanvas(self, dbaseparser):
        if qgis.utils.iface is not None:
            # create node in legend
            root = qgis.core.QgsProject.instance().layerTreeRoot()
            groupname = "Lamia_" + dbaseparser.getDBName().lower()
            lamialegendgroup = root.findGroup(groupname)
            if lamialegendgroup is None:
                lamialegendgroup = root.insertGroup(0, groupname)
            self.qgislegendnode = lamialegendgroup

            dbasetables = self.layers
            # #old way
            # for tablename in dbasetables:
            #     if ('layerqgis' in dbasetables[tablename].keys()
            #             and dbasetables[tablename]['layerqgis'].geometryType() != qgis.core.QgsWkbTypes.NullGeometry ):
            #         qgis.core.QgsProject.instance().addMapLayer(dbasetables[tablename]['layerqgis'], False)
            #         lamialegendgroup.addLayer(dbasetables[tablename]['layerqgis'])
            # new way
            ordergeomtypes = [
                qgis.core.QgsWkbTypes.PointGeometry,
                qgis.core.QgsWkbTypes.LineGeometry,
                qgis.core.QgsWkbTypes.PolygonGeometry,
                qgis.core.QgsWkbTypes.NullGeometry,
            ]
            for geomtype in ordergeomtypes:
                for tablename in self.layers:
                    if (
                        "layerqgis" in self.layers[tablename].keys()
                        and self.layers[tablename]["layerqgisjoined"].geometryType()
                        == geomtype
                    ):
                        qgis.core.QgsProject.instance().addMapLayer(
                            self.layers[tablename]["layerqgis"], False
                        )
                        lamialegendgroup.addLayer(self.layers[tablename]["layerqgis"])

        else:
            layerstoadd = []
            # dbasetables = self.layers
            goodtablekey = [
                val
                for val in self.layers.keys()
                if "layerqgis" in self.layers[val].keys()
            ]
            for tablename in goodtablekey:
                layerstoadd.append(self.layers[tablename]["layerqgis"])
            self.canvas.setLayers(layerstoadd)
            if "edge" in self.layers.keys():
                self.canvas.setExtent(self.layers["edge"]["layer"].extent())
            else:
                self.canvas.setExtent(self.layers["Infralineaire"]["layer"].extent())
            self.canvas.refresh()

    def unloadLayersInCanvas(self):
        if self.qgislegendnode is not None:
            try:
                self.qgislegendnode.removeAllChildren()
                root = qgis.core.QgsProject.instance().layerTreeRoot()
                root.removeChildNode(self.qgislegendnode)

                if self.layers:
                    lamiaqgislay = [lay["layerqgis"] for lay in self.layers.values()]
                    print(lamiaqgislay)
                    for layname, lay in qgis.core.QgsProject.instance().mapLayers().items():
                        print(lay)
                        if lay in lamiaqgislay:
                            qgis.core.QgsProject.instance().removeMapLayer(lay)

            except RuntimeError:
                self.qgislegendnode = None
        elif qgis.utils.iface is None:
            print("***", qgis.core.QgsProject.instance().mapLayers().values())
            if self.layers:
                lamiaqgislay = [lay["layerqgis"] for lay in self.layers.values()]
                print(lamiaqgislay)
            self.canvas.setLayers([])
            self.canvas.refresh()

        del self.layers
        self.layers = {}
        self.canvas.refreshAllLayers()

    def applyStyle(self, worktype, styledir):

        styledirectory = os.path.join(self._getStyleDirectory(worktype), styledir)

        allfiles = [x[2] for x in os.walk(styledirectory)][0]
        qmlfiles = [
            uknfile.split(".")[0]
            for uknfile in allfiles
            if uknfile.split(".")[1] == "qml"
        ]
        for tablename in self.layers.keys():
            if "layerqgis" in self.layers[tablename].keys():
                # apply style
                stylepath = os.path.join(styledirectory, tablename + ".qml")
                # self.layers[tablename]['layerqgis'].loadNamedStyle(stylepath)
                self.layers[tablename]["layerqgis"].loadNamedStyle(
                    stylepath, qgis.core.QgsMapLayer.Symbology
                )
                self.layers[tablename]["layerqgis"].loadNamedStyle(
                    stylepath, qgis.core.QgsMapLayer.Labeling
                )

                # setvisibility
                ltl = (
                    qgis.core.QgsProject.instance()
                    .layerTreeRoot()
                    .findLayer(self.layers[tablename]["layerqgis"].id())
                )
                if tablename in qmlfiles:
                    if ltl:
                        ltl.setItemVisibilityChecked(True)
                else:
                    if ltl:
                        ltl.setItemVisibilityChecked(False)

        if self.canvas:
            self.canvas.refreshAllLayers()
            self.canvas.refresh()

    def updateQgsCoordinateTransform(self):
        """
        Methode appellée lorsque le crs du canvas qgis change
        met à jour self.xform et self.xformreverse pour effectuer les transformations crs canvas <-> crs lamia
        """

        if self.dbaseqgiscrs is not None and self.canvas is not None:
            self.xform = qgis.core.QgsCoordinateTransform(
                self.dbaseqgiscrs,
                self.canvas.mapSettings().destinationCrs(),
                qgis.core.QgsProject.instance(),
            )
            self.xformreverse = qgis.core.QgsCoordinateTransform(
                self.canvas.mapSettings().destinationCrs(),
                self.dbaseqgiscrs,
                qgis.core.QgsProject.instance(),
            )

    def addRawLayerInCanvasForEditing(self, dbaseparser, layername):

        if self.editingrawlayer:
            return

        self.editingrawlayer = None
        self.editlayer = self.layers[layername]["layerqgisjoined"].clone()

        subsetstring = self._getSubsetStringForWorkingDate(dbaseparser)
        self.layers["object"]["layer"].setSubsetString(subsetstring)
        # self.editlayer.setSubsetString(subsetstring)
        self.editlayer.triggerRepaint()

        qgis.core.QgsProject.instance().addMapLayer(self.editlayer, False)
        if self.qgislegendnode is None:  # outsideqgis case
            return
        self.editfeaturetreelayer = self.qgislegendnode.insertLayer(0, self.editlayer)
        if qgis.utils.iface is not None:
            qgis.utils.iface.setActiveLayer(self.editlayer)
            self.editlayer.startEditing()
            for parentable in dbaseparser.getParentTable(layername):
                self.layers[parentable]["layer"].startEditing()
            qgis.utils.iface.actionVertexTool().trigger()

        self.editingrawlayer = layername

    def saveRawLayerInCanvasForEditing(self, dbaseparser, savechanges=False):

        if self.editingrawlayer:

            if isinstance(savechanges, bool) and savechanges:
                for parentable in dbaseparser.getParentTable(self.editingrawlayer):
                    self.layers[parentable]["layer"].commitChanges()
                self.editlayer.commitChanges()
            else:
                for parentable in dbaseparser.getParentTable(self.editingrawlayer):
                    self.layers[parentable]["layer"].rollBack()
                self.editlayer.rollBack()

            # self.qgislegendnode.removeLayer(self.editlayer)
            self.qgislegendnode.removeLayer(self.editlayer)
            self.layers["object"]["layer"].setSubsetString("")
            self.editingrawlayer = None

    def updateWorkingDate(self, dbaseparser, datetimearg=None, revision=None):
        """
        Methode appelée lorsque la date de travail (self.workingdate) ou la version de travail (self.currentrevision)
        est modifiée
        Change les filtres de toutes les tables qgis en fonction
        """

        subsetstring = self._getSubsetStringForWorkingDate(
            dbaseparser, datetimearg, revision
        )

        for tablename, tabledict in self.layers.items():
            if "layerqgis" in tabledict.keys():
                fieldnames = [
                    field.name().lower() for field in tabledict["layerqgis"].fields()
                ]
                if "datecreation" in fieldnames or "datetimecreation" in fieldnames:
                    tabledict["layerqgis"].setSubsetString(subsetstring)
                    tabledict["layerqgis"].triggerRepaint()

    def _getSubsetStringForWorkingDate(
        self, dbaseparser, datetimearg=None, revision=None
    ):
        if datetimearg:
            workingdatemodif = datetimearg
        else:
            workingdatemodif = dbaseparser.workingdate
        if revision:
            revision = revision
        else:
            revision = dbaseparser.currentrevision

        if dbaseparser.__class__.__name__ == "SpatialiteDBaseParser":
            parsertruevalue = "1"
        elif dbaseparser.__class__.__name__ == "PostGisDBaseParser":
            parsertruevalue = "TRUE"

        subsetstringtemp = (
            """  "datetimecreation" <= '{workingdate}' """
            """ AND CASE WHEN "datetimedestruction" IS NOT NULL  THEN "datetimedestruction" > '{workingdate}' ELSE {truevalue} END """
            """ AND "lpk_revision_begin" <= '{currentrevision}' """
            """ AND CASE WHEN "lpk_revision_end" IS NOT NULL  THEN "lpk_revision_end" > '{currentrevision}' ELSE {truevalue} END """
        )
        # print(subsetstringtemp)
        # print(workingdatemodif, parsertruevalue, revision)
        subsetstring = subsetstringtemp.format(
            workingdate=workingdatemodif,
            truevalue=parsertruevalue,
            currentrevision=str(revision),
        )

        return subsetstring

    def _____________________________maptoolsManagement(self):
        pass

    def panCanvas(self):
        # self.mtoolPan = None
        self.canvas.setMapTool(self.mtoolPan)

        # self.canvas.panActionStart(self.canvas.mouseLastXY())

    def toolsetChanged(self, newtool, oldtool=None):

        self.mtooltorestore = oldtool

    def captureGeometry(
        self, capturetype=0, fctonstopcapture=None, listpointinitialgeometry=[]
    ):
        """
        Method called when capturing geometry is needed (add/extent point, line, polygon...)
        Launch the capture tool

        :param connectint: Catching widget signal
        :param listpointinitialgeometry: list of geometry to be extended, if new empty list
        :param type: geom type (point, line, polygone)
        """
        """
        source = self.sender()

        if source is not None and source.objectName() != 'pushButton_rajoutPoint':
            listpointinitialgeometry = []
        

        if type is None:
            if 'Point' in source.objectName():
                type = 0
            elif 'Line' in source.objectName():
                type = 1
            elif 'Polygon' in source.objectName():
                type = 2
        """
        debug = False
        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "\n  %s \n  %s \n  %s",
                str(listpointinitialgeometry),
                # type=None,
                str(capturetype),
                str(fctonstopcapture),
            )

        self.createorresetRubberband(capturetype, rubtype="capture")
        if capturetype == qgis.core.QgsWkbTypes.PointGeometry:
            self.currentmaptool = self.mtoolpoint
        elif capturetype == qgis.core.QgsWkbTypes.LineGeometry:
            self.currentmaptool = self.mtoolline
        elif capturetype == qgis.core.QgsWkbTypes.PolygonGeometry:
            self.currentmaptool = self.mtoolpolygon
        else:
            return

        if self.canvas.mapTool() != self.currentmaptool:
            self.canvas.setMapTool(self.currentmaptool)
            self.currentmaptool.activate()
            # print(self.currentmaptool.cadDockWidget().cadEnabled())
            self.currentmaptool.cadDockWidget().enable()
            # print(self.currentmaptool.cadDockWidget().cadEnabled())
            self.currentmaptool.activate()

        self.currentmaptool.stopCapture.connect(fctonstopcapture)
        self.currentmaptool.setMapPoints(listpointinitialgeometry)
        self.currentmaptool.startCapturing()

    def stopCapture(self, **kwargs):
        if self.currentmaptool is not None:
            try:
                self.currentmaptool.stopCapture.disconnect()
            except (TypeError, AttributeError):
                pass
        self.currentmaptool = self.mtooltorestore
        self.canvas.setMapTool(self.mtooltorestore)

    def ______________________________RubberbandManagement(self):
        pass

        """
        self.rubberBand = None          #the main parent ruberband
        self.rubberbandchild = None     #the child rubberband
        self.rubberbandcapture = None   #the capture rubberband

        self.rubberbands = {'main': None,
                            'child': None,
                            'capture': None}

        """

    def createorresetRubberband(self, type=0, instance=None, rubtype="main"):
        """[summary]

        :param type: QgsGeometry type, defaults to 0
        :param instance: the instance where rubberband is created, defaults to None
        :param rubtype: the ruberband type, can be main, child, capture, all , defaults to 'main'
        """

        rbcolors = {"main": "red", "child": "blue", "capture": "magenta"}

        if instance is None:
            instance = self

        if not hasattr(instance, "rubberbands"):
            instance.rubberbands = {"main": None, "child": None, "capture": None}

        if rubtype == "all":
            rubtypelist = ["main", "child", "capture"]
        else:
            rubtypelist = [rubtype]

        for rubtyp in rubtypelist:
            if instance.rubberbands[rubtyp] is not None:
                instance.rubberbands[rubtyp].reset(type)
            else:
                instance.rubberbands[rubtyp] = qgis.gui.QgsRubberBand(self.canvas, type)
                instance.rubberbands[rubtyp].setWidth(5)
                instance.rubberbands[rubtyp].setColor(QtGui.QColor(rbcolors[rubtyp]))

    def createRubberBandForSelection(
        self, qgsgeom, instance=None, distpixel=4.0, rubtype="main"
    ):

        if not instance:
            instance = self

        self.createorresetRubberband(
            qgis.core.QgsWkbTypes.LineGeometry, instance=instance, rubtype=rubtype
        )
        canvasscale = self.canvas.scale()
        dist = distpixel * canvasscale / 1000.0

        if not isinstance(qgsgeom, list):
            qgsgeom = [qgsgeom]

        for geom in qgsgeom:
            bufferedgeom = geom.buffer(dist, 12).convertToType(
                qgis.core.QgsWkbTypes.LineGeometry
            )
            instance.rubberbands[rubtype].addGeometry(bufferedgeom, self.dbaseqgiscrs)
        instance.rubberbands[rubtype].show()

    def getQgsGeomFromPk(self, dbaseparser, tablename, pk):
        wkt = dbaseparser.getWktGeomFromPk(tablename, pk)
        geom = qgis.core.QgsGeometry.fromWkt(wkt)
        return geom

    def _____________________________Functions(self):
        pass

    # def getNearestPk(self, dbasetable, dbasetablename, point, comefromcanvas=True):
    def getNearestPk(
        self, tablename, point, comefromcanvas=True, fieldconstraint=None, spindex=None
    ):
        """
        Permet d'avoir le pk du feature le plus proche du qgsvectorlayer correspondant à dbasetablename
        pas besoin de filtre sur les dates et versions on travaille avec le qgsectorlyaer de la table
        qui dispose déjà d'un filtre en fonction de la date et de la version
        :param dbasetable: la dbasetable considérée
        :param dbasetablename:  le nom de la dbasetable
        :param point: le point dont on veut connaitre le plus proche élément
        :param comefromcanvas: spécifie sir le point provient du canvas qgis (nécessité de trasformation) ou non
        :return: le pk de la table dbasetablenamele plus proche du point
        """
        debug = False
        if debug:
            # logging.getLogger(__name__).setLevel(logging.DEBUG)
            logging.getLogger().debug(f"START {tablename}")
            # print(self.layers.keys())
            # print(__name__, point)

        layertoprocess = self.layers[tablename][
            "layerqgis"
        ]  # layer qgis has conf with only good versions
        # checking if layer is spatial one
        # isspatial = dbasetable['layerqgis'].isSpatial()
        # print(self.layers[tablename]["layer"].dataProvider().sourceName())
        # self.layers[tablename]["layer"].triggerRepaint()
        # print(self.layers[tablename]["layer"].featureCount())
        # dp = self.layers[tablename]["layer"].dataProvider()

        # print(type(layertoprocess))
        # print([fl.name() for fl in layertoprocess.fields()])

        if isinstance(point, list):
            point = qgis.core.QgsPointXY(point[0], point[1])
        isspatial = layertoprocess.isSpatial()
        if not isspatial:
            return None, None

        # crs transform if needed
        if debug:
            logging.getLogger().debug("pointbefore %s", str(point))
        if comefromcanvas:
            point2 = self.xformreverse.transform(point)
        else:
            point2 = point
        if debug:
            logging.getLogger("__name__").debug("pointafter %s", str(point2))

        # spatialindex creation
        # spindex = qgis.core.QgsSpatialIndex(dbasetable['layerqgis'].getFeatures())
        expr = []
        if spindex is None:
            if fieldconstraint:
                expr = []
                for k, v in fieldconstraint.items():
                    expr.append(f""" "{k}" = '{v}'  """)
                expr = " and ".join(expr)

                req = qgis.core.QgsFeatureRequest().setFilterExpression(expr)
                req.setInvalidGeometryCheck(False)
                # req.setSubsetOfAttributes([])
                req.setNoAttributes()
                if qgis.utils.iface:
                    canvasrect = self.xformreverse.transform(self.canvas.extent())
                    req.setFilterRect(canvasrect)
                spindex = qgis.core.QgsSpatialIndex(layertoprocess.getFeatures(req))
            else:
                spindex = qgis.core.QgsSpatialIndex(layertoprocess.getFeatures())

        # spindex = qgis.core.QgsSpatialIndex(layertoprocess.getFeatures())
        layernearestid = spindex.nearestNeighbor(point2, 1)
        # print("layernearestid", layernearestid)
        if not layernearestid:
            return None, None

        point2geom = qgis.core.QgsGeometry.fromPointXY(point2)

        """
        if not self.revisionwork:
            nearestfet = self.getLayerFeatureById(dbasetablename, layernearestid[0])
        else:
            nearestfet = self.getLayerFeatureByPk(dbasetablename, layernearestid[0])
        """
        nearestfet = layertoprocess.getFeature(layernearestid[0])
        nearestfetgeom = nearestfet.geometry()

        # if point layer : nearestNeighbor gives the right value
        # if dbasetable['layerqgis'].geometryType() == 0:
        if layertoprocess.geometryType() == 0:
            disfrompoint = nearestfetgeom.distance(point2geom)
            return layernearestid[0], disfrompoint

        # if line or polygon layer : as the nearestNeighbor is with a bounding box, we need to filter
        # the elements in this boundingbox
        else:
            # clean nearestfet geometry if not valid
            if not nearestfetgeom.isGeosValid() and nearestfetgeom.type() == 1:
                nearestfetgeom = qgis.core.QgsGeometry.fromPointXY(
                    qgis.core.QgsPointXY(nearestfetgeom.asPolyline()[0])
                )

            disfrompoint = nearestfetgeom.distance(point2geom)

            if debug:
                logging.getLogger("__name__").debug(
                    "nearestfetgeom - dist %s %s",
                    str(nearestfetgeom.asWkt()),
                    str(disfrompoint),
                )
            if disfrompoint < 0.1:
                disfrompoint = 0.1

            bboxtofilter = point2geom.buffer(disfrompoint * 1.2, 12).boundingBox()
            idsintersectingbbox = spindex.intersects(bboxtofilter)

            if debug:
                logging.getLogger("__name__").debug(
                    "idsintersectingbbox %s", str(idsintersectingbbox)
                )

            # search nearest geom in bbox
            distance = None
            nearestindex = None
            finalgeomispoint = False
            distanceratio = 1.2

            for intersectingid in idsintersectingbbox:
                ispoint = False
                # feat = self.getLayerFeatureByPk(dbasetablename, intersectingid)
                feat = layertoprocess.getFeature(intersectingid)
                featgeom = feat.geometry()

                if debug:
                    logging.getLogger("__name__").debug(
                        "intersectingid %s  - is valid : %s - type : %s - multi : %s",
                        str(intersectingid),
                        str(featgeom.isGeosValid()),
                        str(featgeom.type()),
                        str(featgeom.isMultipart()),
                    )

                if featgeom.isGeosValid():  # if not valid, return dist = -1...
                    dist = featgeom.distance(point2geom)
                else:  # point
                    if featgeom.type() == 1 and not featgeom.isMultipart():

                        ispoint = True
                        if len(featgeom.asPolyline()) == 1:  # polyline of 1 point
                            dist = qgis.core.QgsGeometry.fromPointXY(
                                qgis.core.QgsPointXY(featgeom.asPolyline()[0])
                            ).distance(point2geom)
                        elif (
                            len(featgeom.asPolyline()) == 2
                            and featgeom.asPolyline()[0] == featgeom.asPolyline()[1]
                        ):
                            dist = qgis.core.QgsGeometry.fromPointXY(
                                qgis.core.QgsPointXY(featgeom.asPolyline()[0])
                            ).distance(point2geom)
                    else:
                        continue
                if debug:
                    logging.getLogger("__name__").debug(
                        "distance : %s - ispoint : %s", str(dist), str(ispoint)
                    )
                # algo for keeping point in linestring layer as nearest
                # if point is nearest than 1.2 x dist from nearest line
                if debug:
                    logging.getLogger("__name__").debug(
                        "distance : %s - ispoint : %s - geomfinalispoint : %s - finaldist : %s",
                        str(dist),
                        str(ispoint),
                        str(finalgeomispoint),
                        str(distance),
                    )
                if distance is None:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = ispoint
                elif (
                    not finalgeomispoint and ispoint and dist < distance * distanceratio
                ):
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = True
                elif (
                    finalgeomispoint and not ispoint and dist < distance / distanceratio
                ):
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = False
                elif finalgeomispoint == ispoint and dist < distance:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = ispoint
        if debug:
            logging.getLogger(__name__).debug(
                "nearestpk, dist %s %s", str(nearestindex), str(distance)
            )
        return nearestindex, distance

    def zoomToFeature(self, tablename, pk):

        if (
            tablename in self.layers.keys()
            and "layerqgis" in self.layers[tablename].keys()
        ):
            layerqgis = self.layers[tablename]["layerqgis"]
            featgeom = layerqgis.getFeature(pk).geometry()

            if featgeom.centroid() is not None and not featgeom.centroid().isNull():
                point2 = self.xform.transform(featgeom.centroid().asPoint())
            else:
                # print(featgeom.asWkt())
                point2 = self.xform.transform(
                    qgis.core.QgsPointXY(featgeom.vertexAt(0))
                )

            self.canvas.setCenter(point2)
            self.canvas.refresh()

    def _getStyleDirectory(self, worktype):
        styledirectory = os.path.join(
            os.path.dirname(Lamia.config.__file__), worktype, "qgsstyles",
        )

        return styledirectory

