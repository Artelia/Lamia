import os, sys, logging
from threading import Thread

lamiapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lamiapath)
import Lamia
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.iface.qgscanvas.ifaceqgiscanvas import QgisCanvas
from Lamia.libslamia.dbaseutils.chooserid import IDChooser
from artelialogin.models import Project

# from ...test.test_utils import *
import pprint
import json

import threading


class LamiaSession:

    _instances = set()

    def __init__(self, idproject):
        # super()

        # app = initQGis()

        # logging.getLogger().debug(f"Init lamia session project n {idproject}")
        print(threading.current_thread().name)
        self.idproject = idproject
        self.locale = None

        # * var1 : load entire widget
        if False:
            self.mainwin, self.canvas, self.lamiawidget = getDisplayWidget()

            self.canvas.enableAntiAliasing(True)
            canvascrs = qgis.core.QgsCoordinateReferenceSystem()
            canvascrs.createFromString("EPSG:3857")
            self.canvas.setDestinationCrs(canvascrs)

            self.lamiaparser = self.lamiawidget.dbase
            self.qgscanvas = self.mainwin.qgiscanvas

            queryset = Project.objects.filter(id_project=idproject)
            queryval = queryset.values()[0]

            self._instances.add(self)

            logging.getLogger().debug(f"Init lamia session loading ... {idproject}")

            self.lamiawidget.loadDBase(
                dbtype="Postgis",
                host=queryval["pghost"],
                # host="localhost",
                port=int(queryval["pgport"]),
                dbname=queryval["pgdbname"],
                schema=queryval["pgschema"],
                user=queryval["pguser"],
                password=queryval["pgpassword"],
            )

        # * var2 : load dbaseparser and qgiscanvas
        if True:
            queryset = Project.objects.filter(id_project=idproject)
            queryval = queryset.values()[0]
            self.lamiaparser = DBaseParserFactory("django").getDbaseParser()
            if False:
                # create canvas and LamiaWindowWidget
                canvas = qgis.gui.QgsMapCanvas()
                canvas.enableAntiAliasing(True)
                canvascrs = qgis.core.QgsCoordinateReferenceSystem()
                canvascrs.createFromString("EPSG:3857")
                canvas.setDestinationCrs(canvascrs)

                self.qgscanvas = QgisCanvas(canvas)

                queryset = Project.objects.filter(id_project=idproject)
                queryval = queryset.values()[0]
                # print(queryval["qgisserverurl"])

                self._instances.add(self)

                logging.getLogger().debug(f"Init lamia session loading ... {idproject}")

            self.lamiaparser.loadDBase(
                dbtype="Postgis",
                host=queryval["pghost"],
                # host="localhost",
                port=int(queryval["pgport"]),
                dbname=queryval["pgdbname"],
                schema=queryval["pgschema"],
                user=queryval["pguser"],
                password=queryval["pgpassword"],
            )

            self._instances.add(self)

            # self.qgscanvas.createLayers(self.lamiaparser, alsoqgisjoined=False)

            # print("Init lamia session loading ... ", idproject)

        # * var3 django
        if False:
            queryset = Project.objects.filter(id_project=idproject)
            queryval = queryset.values()[0]
            self.lamiaparser = DBaseParserFactory("django").getDbaseParser()
            self.lamiaparser.loadDBase(schema=queryval["pgschema"])

            self._instances.add(self)
            # print("Init lamia session loading ... ", idproject)

        # self.idchooser = IDChooser(toolwidget=None, dbaseparser=self.lamiaparser,)
        self.cursors = {}
        # logging.getLogger().debug(f"Init lamia session loaded {idproject}")

        # exitQGis()

    def getInstance(idproject):
        inst = None
        for obj in __class__._instances:
            # print (obj.worktype) # prints 'a' and 'c'
            if obj.idproject == idproject:
                # logging.getLogger().debug(f"recycle  instance {idproject}")
                inst = obj
        if inst is None:
            # logging.getLogger().debug(f"create instance {idproject}")
            inst = LamiaSession(idproject)

        return inst

    def getNearestPk(self, layername, coords):
        # print("getNearestPk", threading.current_thread().name)

        coords = f"POINT({coords[0]} {coords[1]})"

        sql = f"""
        WITH closest_candidates AS (
        SELECT
            {layername}.pk_{layername},
            {layername}.geom
        FROM
            {layername}
        ORDER BY
            {layername}.geom <->
            ST_Transform(ST_GeomFromText('{coords}',3857), {self.lamiaparser.crsnumber})
        LIMIT 20
        )
        SELECT pk_{layername}
        FROM closest_candidates
        ORDER BY
        ST_Distance(
            geom,
            ST_Transform(ST_GeomFromText('{coords}',3857), {self.lamiaparser.crsnumber})
            )
        LIMIT 1
        """
        try:
            res = self.lamiaparser.query(sql)
            # self.lamiaparser.commitTransaction()
        except Exception as e:
            print("getNearestPk error", e)
        # print(res)
        return res[0][0]

    def getIds(self, confobject):
        # print("getIds", threading.current_thread().name)
        try:
            idchooser = IDChooser(toolwidget=confobject, dbase=self.lamiaparser)
            ids = idchooser.loadIds().to_json()
        except Exception as e:
            print("getIds error", e)
            ids = json.dumps({})
        return ids

    def updateLocale(self, locale):
        if locale != self.locale:
            self.lamiaparser.locale = locale.split("_")[0]
            self.lamiaparser.dbconfigreader.createDBDictionary(
                self.lamiaparser.worktype
            )
            self.lamiaparser.dbasetables = self.lamiaparser.dbconfigreader.dbasetables
            self.locale = locale

    def getThumbnail(self, pkres):
        sql = f"SELECT thumbnail FROM resource WHERE pk_resource = {pkres}"
        bindata = self.lamiaparser.query(sql)[0][0]
        return bindata

    def getStyles(self):
        sql = "SELECT businessline FROM database"
        worktype = self.lamiaparser.query(sql)[0][0]
        styledirectory = os.path.join(
            os.path.dirname(Lamia.__file__), "worktypeconf", worktype, "qgsstyles",
        )
        stylesdir = [
            os.path.basename(f.path) for f in os.scandir(styledirectory) if f.is_dir()
        ]

        returnstyle = {}
        for styledir in stylesdir:
            files = [x[2] for x in os.walk(os.path.join(styledirectory, styledir))][0]
            returnstyle[styledir] = [f.split(".")[0] for f in files]

        return returnstyle

    def getPksFromBBox(self, table, bbox):
        if len(bbox) == 4:
            sql = f"""
            SELECT pk_{table} FROM {table}_qgis 
            WHERE geom && ST_Transform(ST_MakeEnvelope (
                        {bbox[0]}, {bbox[1]},
                        {bbox[2]}, {bbox[3]}, 4326),
                        {self.lamiaparser.crsnumber})
            """
            # print(sql)
            res = self.lamiaparser.query(sql)
            res = [elem[0] for elem in res]
        else:
            res = []
        return res
