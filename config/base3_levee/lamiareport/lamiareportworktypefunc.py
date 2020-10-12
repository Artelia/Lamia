import os
import qgis, qgis.core
import Lamia
from lamiaqgisiface.iface.qgiswidget.tools.toolprepro.base2.lamiabase_graphique_tool import (
    BaseGraphiqueTool,
)
from lamiaapi.libslamia.lamiagraph.lamiagraph import GraphMaker


def profile(self):
    featgeom = self.currentatlasfeat.geometry()
    imageitem = self.currentimageItem

    point1 = [featgeom.asPolyline()[0].x(), featgeom.asPolyline()[0].y()]
    point2 = [featgeom.asPolyline()[-1].x(), featgeom.asPolyline()[-1].y()]

    # exportfile = os.path.join(os.path.dirname(__file__), '..','..','..', 'config', 'tempgraph.png')
    exportfile = os.path.join(
        os.path.dirname(Lamia.__file__), "config", "tempgraph.png"
    )

    # get pathtool and init it
    # pathtool = None
    # for i, tool in enumerate(self.windowdialog.tools):
    #    if 'PathTool' in tool.__class__.__name__ :
    #        pathtool = self.windowdialog.tools[i]

    # pathtool.exportCurrentGraph(point1, point2,
    # point1,point2, datatype, w,h,exportfile
    self.networkcore.exportCurrentGraph(
        point1=point1,
        point2=point2,
        datatype="topographie",
        graphtype="Profillong",
        w=imageitem.rect().width(),
        h=imageitem.rect().height(),
        exportfile=exportfile,
    )

    return os.path.abspath(exportfile)


# def profiltravers(self, atlasfeat, qrect):
def profiltravers(self):
    resfile = None

    graphmaker = GraphMaker(self.dbase)
    atlasfeat = self.currentatlasfeat
    qrect = self.currentimageItem.rect()

    # get graph pk
    resourceid = self.dbase.getValuesFromPk("edge", "lid_resource_4 ", atlasfeat.id())
    if resourceid is None:
        return None

    sql = "SELECT pk_graph FROM graph_now  WHERE id_resource = " + str(resourceid)
    sql = self.dbase.sqlNow(sql)
    result = self.dbase.query(sql)
    if len(result) == 0:
        return None
    graphpk = result[0][0]

    # make graph
    exportfile = os.path.join(
        os.path.dirname(Lamia.__file__), "config", "tempgraph.png"
    )
    graphmaker.exportgraph(graphpk, exportfile, qrect.width(), qrect.height())
    return exportfile
