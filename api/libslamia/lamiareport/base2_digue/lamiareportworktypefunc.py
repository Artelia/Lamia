import os
import qgis, qgis.core

from Lamia.qgisiface.iface.qgiswidget.tools.toolprepro.base2.lamiabase_graphique_tool import (
    BaseGraphiqueTool,
)


def profile(self):
    featgeom = self.currentatlasfeat.geometry()
    imageitem = self.currentimageItem

    point1 = [featgeom.asPolyline()[0].x(), featgeom.asPolyline()[0].y()]
    point2 = [featgeom.asPolyline()[-1].x(), featgeom.asPolyline()[-1].y()]

    exportfile = os.path.join(
        os.path.dirname(__file__), "..", "..", "..", "config", "tempgraph.png"
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
    atlasfeat = self.currentatlasfeat
    qrect = self.currentimageItem.rect()

    resfile = None
    # print([field.name() for field in reportdic['atlaslayer'].fields()])
    # if isinstance(atlasfeat, qgis.core.QgsFeature):
    #    currentfeatureid = atlasfeat[self.atlasconfData['atlaslayerid']]
    # elif isinstance(atlasfeat, int):
    #    currentfeatureid = atlasfeat

    # sql = "SELECT lid_ressource_4 FROM Infralineaire WHERE id_infralineaire = " + str(currentfeatureid)
    # query = self.dbase.query(sql)
    # result = [row for row in query]
    # if len(result)==0:
    #    return None
    # lkressourceprofile = result[0][0]
    # print('getPhoto',lkphoto )
    lkressourceprofile = self.dbase.getValuesFromPk(
        "Infralineaire", "lid_ressource_4 ", atlasfeat.id()
    )

    if not self.dbase.utils.isAttributeNull(lkressourceprofile):
        # sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_ressource = "
        sql = "SELECT file FROM Photo_qgis  WHERE id_ressource = "
        sql += str(lkressourceprofile)
        query = self.dbase.query(sql)
        result = [row for row in query]
        if len(result) > 0:
            filephoto = result[0][0]
            resfile = self.dbase.completePathOfFile(filephoto)

        # sql = "SELECT typegraphique, id_graphique FROM Graphique  WHERE id_ressource = " + str(lkressourceprofile)
        sql = (
            "SELECT typegraphique, pk_graphique FROM Graphique_qgis  WHERE id_ressource = "
            + str(lkressourceprofile)
        )
        query = self.dbase.query(sql)
        result = [row for row in query]
        if len(result) > 0:
            # self.userwdgdesktop.stackedWidget_profiltravers.setCurrentIndex(1)
            # print('ok')
            typegraphique = result[0][0]
            pkgraphique = result[0][1]
            # print(idgraphique)

            # self.graphprofil.featureSelected(idgraphique, True)
            """
                             dbaseparser=None, 
                 mainifacewidget=None, 
                 choosertreewidget=None, 
                 parentwidget=None, 
                 parent=None
            """
            graphtool = BaseGraphiqueTool(dbaseparser=self.dbase)
            # graphtool.initMainToolWidget()
            # datas = self.dbase.dbasetables['Graphique']['widget'][0].getGraphData(idgraphique)
            datas = graphtool.getGraphData(pkgraphique)
            exportfile = os.path.join(
                os.path.dirname(__file__), "..", "..", "..", "config", "tempgraph.png"
            )
            graphtool.exportgraph(
                typegraphique, datas, exportfile, qrect.width(), qrect.height()
            )
            resfile = exportfile

    # print('resfile', resfile)
    if resfile is None:
        pass

    return resfile

