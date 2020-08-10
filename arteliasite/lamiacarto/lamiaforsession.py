import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import Lamia
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from .models import Project


class LamiaSession:

    _instances = set()

    def __init__(self, idproject):
        self.idproject = idproject
        self._instances.add(self)
        self.lamiaparser = DBaseParserFactory("postgis").getDbaseParser()
        # print("**", list(queryset.values("id_projet", "qgisserverurl"))[0])
        # self.lamiaparser = DBaseParserFactory("spatialite").getDbaseParser()
        # self.lamiaparser.loadDBase(dbtype="Spatialite", slfile=SLFILE)
        queryset = Project.objects.filter(id_project=idproject)
        queryval = queryset.values()[0]
        print(queryval["qgisserverurl"])
        self.lamiaparser.loadDBase(
            dbtype="Postgis",
            host=queryval["pghost"],
            # host="localhost",
            port=queryval["pgport"],
            dbname=queryval["pgdbname"],
            schema=queryval["pgschema"],
            user=queryval["pguser"],
            password=queryval["pgpassword"],
        )

    def getInstance(idproject):
        inst = None
        for obj in __class__._instances:
            # print (obj.worktype) # prints 'a' and 'c'
            if obj.idproject == idproject:
                print("recycle  instance", idproject)
                inst = obj
        if inst is None:
            print("create instance", idproject)
            inst = LamiaSession(idproject)

        return inst

