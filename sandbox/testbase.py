import os, sys
import inspect

lamiapath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(lamiapath)

# from Lamia.config.base3.dbase.base3_0_1 import *
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

SLFILE = r"C:\01_WORKINGDIR\canejean2\Canejan.sqlite"
SLFILE = (
    r"C:\111_GitProjects\Lamia\testfiles\c_creation\sl_base3_levee_Lamia\test01.sqlite"
)

tempparser = DBaseParserFactory("spatialite").getDbaseParser()
tempparser.loadDBase(dbtype="Spatialite", slfile=SLFILE)


# node = node(tempparser)
# print(node.linkedtables)


# node.update(
#     2, {"pk_object": 1, "lid_descriptionsystem_1": 2, "datetimecreation": "2020-01-01"}
# )
# print(node.read(2))

tt = tempparser.lamiaorm

# tt.node.create()

pk = tt.node.create()
tt.node.update(pk, {"id_node": 13, "geom": "Point(1.  1.)"})


# pk = tt.equipment.create()
# print(pk)
# tt.equipment.update(pk, {"equipmentcategory": "OUH"})
# print(tt.equipment["id_equipment =9999"])
# print(tt.equipment.)
# print(inspect.getmembers(tt))
# print(tt["node"].read(99999)["geom"])
# print(dir(tt))
# tt.node.read(2)
# tt.get("node")
# tt.node.create()
# print(dir(tt))

# print(tt.edge)
# print(tt.edge.read(3))

# print(tt.__dir__)
# print(tt.gre)

# ppo = getattr(tt, "node")

# tt.node.read(2)
# print(tt.node.create())
