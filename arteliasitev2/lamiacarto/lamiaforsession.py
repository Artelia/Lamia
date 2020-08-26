import os, sys, logging
from threading import Thread

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import Lamia
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.iface.qgscanvas.ifaceqgiscanvas import QgisCanvas
from .models import Project
from test.test_utils import *

import threading


class LamiaSession(Thread):

    _instances = set()

    def __init__(self, idproject):
        super()

        # app = initQGis()

        logging.getLogger().debug(f"Init lamia session project n {idproject}")
        print(threading.current_thread().name)
        self.idproject = idproject

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
        else:
            queryset = Project.objects.filter(id_project=idproject)
            queryval = queryset.values()[0]
            self.lamiaparser = DBaseParserFactory("postgis").getDbaseParser()
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

            print("Init lamia session loading ... ", idproject)

        logging.getLogger().debug(f"Init lamia session loaded {idproject}")

        # exitQGis()

    def getInstance(idproject):
        inst = None
        for obj in __class__._instances:
            # print (obj.worktype) # prints 'a' and 'c'
            if obj.idproject == idproject:
                logging.getLogger().debug(f"recycle  instance {idproject}")
                inst = obj
        if inst is None:
            logging.getLogger().debug(f"create instance {idproject}")
            inst = LamiaSession(idproject)

        return inst

    def getNearestPk_(self, layername, coords):
        print("init")
        print(threading.current_thread().name)
        app = initQGis()  #  why ?
        print("done")
        print(threading.current_thread().name)
        pk, dist = self.qgscanvas.getNearestPk(layername, coords, comefromcanvas=True)
        # pk, dist = 2, None
        return pk, dist
        # self._return = (pk, dist)

    def getNearestPk(self, layername, coords):
        coords = f"POINT({coords[0]} {coords[1]})"

        # sql = f"SELECT  ST_AsText(ST_Transform(ST_GeomFromText('{coords}',3857), {self.lamiaparser.crsnumber}))"
        # res = self.lamiaparser.query(sql)[0][0]
        # print(res)

        # 'SRID=26918;POINT(583571.905921312 4506714.34119218)'::geometry

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

        res = self.lamiaparser.query(sql)
        self.lamiaparser.commitTransaction()
        print(res)
        return res[0][0]

    def join(self, *args):
        Thread.join(self, *args)
        return self._return
