# -*- coding: utf-8 -*-
"""
import sys
sys.path.append('C://OSGeo4W64//apps//qgis//python')
sys.path.append('C://OSGeo4W64//apps//Python27//Lib//site-packages')
"""
import os
import sys
#pathinspec = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..'))
#print(pathinspec)
#sys.path.append(pathinspec)

import qgis
from qgis.PyQt import QtXml, QtCore, QtGui
try:
    from InspectionDigueV2.src.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget
except ImportError:
    from InspectionDigueV2.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget

try:
    from qgis.PyQt.QtGui import  QPrinter
except ImportError:
    from qgis.PyQt.QtPrintSupport import QPrinter





def doPrintingJob():
    print('begin job')
    #create project
    project = qgis.core.QgsProject.instance()
    # project = qgis.core.QgsProject()
    canvas = qgis.gui.QgsMapCanvas()

    #inspectiondigue
    print('load inspectiondigue')
    wind = InspectiondigueWindowWidget(canvas)
    path = os.path.normpath('c://000_testdigue//testdbase.sqlite')
    # path = os.path.normpath('C:\\000_testimportBM\\BD_BM_ind3.sqlite')
    wind.dbase.loadQgisVectorLayers(path)
    
    if False:
        if int(str(wind.dbase.qgisversion_int)[0:3]) < 220:
            project = qgis.core.QgsProject.instance()
        else:
            project = qgis.core.QgsProject()

    # add layers
    """
    canvaslayerstoadd=[]
    for tablename in wind.dbase.dbasetables.keys():
        canvaslayerstoadd.append(qgis.gui.QgsMapCanvasLayer(wind.dbase.dbasetables[tablename]['layerqgis']))
    """
    maplayerstoadd=[]
    for tablename in wind.dbase.dbasetables.keys():
        maplayerstoadd.append(wind.dbase.dbasetables[tablename]['layerqgis'])

    #project layers
    if int(str(wind.dbase.qgisversion_int)[0:3]) < 220:
        qgis.core.QgsMapLayerRegistry.instance().addMapLayers(maplayerstoadd)
    else:
        qgis.core.QgsProject.instance().addMapLayers(maplayerstoadd)
    root = project.layerTreeRoot()
    bridge = qgis.gui.QgsLayerTreeMapCanvasBridge(root, canvas)
    bridge.setCanvasLayers()
    # canvas.setExtent(wind.dbase.dbasetables['Infralineaire']['layer'].extent())
    # canvas.show()

    # ******************* composition
    print('crate comp')

    mapsettings = canvas.mapSettings()
    if int(str(wind.dbase.qgisversion_int)[0:3]) < 220:
        newComposition = qgis.core.QgsComposition(mapsettings)
    else:
        newComposition = qgis.core.QgsComposition(project)

    # templatepath = "C://00_Base.qpt"
    templatepath = "C://Users//patrice.verchere//Documents//GitHub//InspectionDigueV2//src//compositions//00_Base.qpt"
    template_file = QtCore.QFile(templatepath)
    template_file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text)
    template_content = template_file.readAll()
    template_file.close()
    document = QtXml.QDomDocument()
    document.setContent(template_content)

    newComposition.loadFromTemplate(document)
    if int(str(wind.dbase.qgisversion_int)[0:3]) < 220:
        newComposition.composerMapItems()[0].setMapCanvas(canvas)
    else:
        pass

    print('create atlas')
    # ******************* ATLAS
    if True:
        atlas = newComposition.atlasComposition()
        #atlasLayer = iface.activeLayer()
        atlas.setCoverageLayer(wind.dbase.dbasetables['Infralineaire']['layerqgis'])
        atlas.setEnabled( True )
        atlas.setSingleFile(True)
        ret = newComposition.setAtlasMode( qgis.core.QgsComposition.ExportAtlas )
        if int(str(wind.dbase.qgisversion_int)[0:3]) < 220:
            atlas.setComposerMap(newComposition.composerMapItems()[0])
        else:
            pass

        num = atlas.numFeatures()

        print('mapitems',newComposition.composerMapItems())
        newComposition.composerMapItems()[0].setAtlasDriven(True)
        newComposition.composerMapItems()[0].setAtlasScalingMode(qgis.core.QgsComposerMap.Auto)

    print('render atlas')
    if True:
        printer = QPrinter()
        # newComposition.beginPrintAsPDF(printer, "C:\\test.pdf")
        # painter = QtGui.QPainter(printer)
        painter = QtGui.QPainter()
        # atlas.beginRender()

        if True:
            newComposition.setUseAdvancedEffects(False)
            atlas.beginRender()
            newComposition.beginPrintAsPDF(printer, "C:\\test.pdf")
            printReady = painter.begin(printer)
            # newComposition.beginPrint(printer)
            for i in range(0, num):
                print('num',i,  painter.isActive() )
                # painter = QtGui.QPainter()
                atlas.prepareForFeature(i)
                image = newComposition.getComposerItemById('graph')
                image.setPicturePath('c://Artelia.jpg')
                image.updateItem()
                # newComposition.beginPrintAsPDF(printer, "C:\\test.pdf")
                # newComposition.beginPrint(printer)
                # printReady = painter.begin(printer)
                if i > 0:
                    printer.newPage()
                newComposition.doPrint(printer, painter)
                # painter.end()
            print('end print')
            atlas.endRender()
            painter.end()

        if False:
            for i in range(0, num):
                print('i',i)
                ret = atlas.prepareForFeature(i)

                #printer = QtGui.QPrinter()
                #printer.setOutputFormat(QtGui.QPrinter.PdfFormat)

                #newComposition.beginPrintAsPDF(printer, "C:\\test.pdf")

                newComposition.exportAsPDF("C:\\test_" +str(i) + ".pdf")
                # newComposition.print(printer)
        if False:
            newComposition.exportAsPDF("C:\\test.pdf")


    if False:
        # atlas.beginRender()
        # printer = QtGui.QPrinter()
        # printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        newComposition.exportAsPDF("C:\\testatals.pdf")

    # atlas.endRender()
    qgis.core.QgsProject.instance().clear()


def launch():

    print('begin')
    outsideqgis = False
    # app = QtGui.QApplication(sys.argv)

    if outsideqgis:
        if True:
            qgis_path = "C://OSGeo4W64//apps//qgis"
        else:
            qgis_path = "C://OSGeo4W64//apps//qgis-dev"
        app = qgis.core.QgsApplication([], True)
        qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
        qgis.core.QgsApplication.initQgis()

    doPrintingJob()
    # app.exec_()

    if outsideqgis:
        qgis.core.QgsApplication.exitQgis()
    # sys.exit(app.exec_())

    print('end')


if __name__ == '__main__':
    launch()
else:
    launch()

