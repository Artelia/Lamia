import os, sys, logging

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import Lamia
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.iface.qgscanvas.ifaceqgiscanvas import QgisCanvas
from .models import Project
from test.test_utils import *


class LamiaSession:

    _instances = set()

    def __init__(self, idproject):
        app = initQGis()

        logging.getLogger().debug(f"Init lamia session project n {idproject}")
        self.idproject = idproject

        # self.mainwin, self.canvas, self.lamiawidget = getDisplayWidget()

        self.lamiaparser = DBaseParserFactory("postgis").getDbaseParser()

        # create canvas and LamiaWindowWidget
        canvas = qgis.gui.QgsMapCanvas()
        canvas.enableAntiAliasing(True)
        canvascrs = qgis.core.QgsCoordinateReferenceSystem()
        canvascrs.createFromString("EPSG:3857")
        canvas.setDestinationCrs(canvascrs)

        # self.qgscanvas.setCanvas(canvas)
        self.qgscanvas = QgisCanvas(canvas)

        # self.lamiaparser = self.lamiawidget.dbase
        # print("**", list(queryset.values("id_projet", "qgisserverurl"))[0])
        # self.lamiaparser = DBaseParserFactory("spatialite").getDbaseParser()
        # self.lamiaparser.loadDBase(dbtype="Spatialite", slfile=SLFILE)
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

        self.qgscanvas.createLayers(self.lamiaparser, alsoqgisjoined=False)

        # print("Init lamia session loading ... ", idproject)
        # print(
        #     "Postgis",
        #     "host",
        #     queryval["pghost"],
        #     # host="localhost",
        #     "port",
        #     queryval["pgport"],
        #     "dbname",
        #     queryval["pgdbname"],
        #     "schema",
        #     queryval["pgschema"],
        #     "user",
        #     queryval["pguser"],
        #     "password",
        #     queryval["pgpassword"],
        # )
        # self.lamiawidget.loadDBase(
        #     dbtype="Postgis",
        #     host=queryval["pghost"],
        #     # host="localhost",
        #     port=queryval["pgport"],
        #     dbname=queryval["pgdbname"],
        #     schema=queryval["pgschema"],
        #     user=queryval["pguser"],
        #     password=queryval["pgpassword"],
        # )

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

    def getNearestPk(self, layername, coords):
        app = initQGis()  #  why ?
        pk, dist = self.qgscanvas.getNearestPk(layername, coords, comefromcanvas=True)
        return pk, dist

