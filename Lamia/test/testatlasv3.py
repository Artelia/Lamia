# -*- coding: utf-8 -*-
"""
import sys
sys.path.append('C://OSGeo4W64//apps//qgis//python')
sys.path.append('C://OSGeo4W64//apps//Python27//Lib//site-packages')
"""
import os
import sys
if False:
    pathinspec = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..'))
    print(pathinspec)
    sys.path.append(pathinspec)
import traceback
import qgis
from qgis.PyQt import QtXml, QtCore, QtGui
try:
    from InspectionDigueV2.src.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget
except ImportError:
    from InspectionDigue.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget

try:
    from qgis.PyQt.QtGui import  QPrinter
except ImportError:
    from qgis.PyQt.QtPrintSupport import QPrinter




class AbstractWorker(QtCore.QObject):
    """Abstract worker, ihnerit from this and implement the work method"""

    # available signals to be used in the concrete worker
    finished = QtCore.pyqtSignal(object)
    error = QtCore.pyqtSignal(Exception)
    progress = QtCore.pyqtSignal(float)
    message = QtCore.pyqtSignal(str)
    toggle_show_progress = QtCore.pyqtSignal(bool)
    set_message = QtCore.pyqtSignal(str)
    toggle_show_cancel = QtCore.pyqtSignal(bool)

    # private signal, don't use in concrete workers this is automatically
    # emitted if the result is not None
    # successfully_finished = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QObject.__init__(self)
        self.killed = False

    def run(self):
        result = self.work()
        self.finished.emit(result)


        if False:
            try:
                result = self.work()
                self.finished.emit(result)
            except Exception as e:
                # forward the exception upstream
                self.error.emit(e)
                self.finished.emit(None)

    def work(self):
        """ Reimplement this putting your calculation here
            available are:
                self.progress.emit(0-100)
                self.killed
            :returns a python object - use None if killed is true
        """

        raise NotImplementedError

def printError(errorstr):
    print('error', errorstr)

def printMessage(message):
    print('message', message)


#def start_worker(worker, iface, message, with_progress=True):
def start_worker(worker,canvas):
    # configure the QgsMessageBar
    print('start_worker')

    # start the worker in a new thread
    # let Qt take ownership of the QThread
    # thread = QtCore.QThread(iface.mainWindow())
    thread = QtCore.QThread(canvas)
    worker.moveToThread(thread)




    # worker.finished.connect(lambda result: worker_finished(result, thread, worker, iface, message_bar_item))
    worker.finished.connect(lambda result: worker_finished(result, thread, worker))
    worker.error.connect(printError)
    worker.message.connect(printMessage)
    # worker.progress.connect(progress_bar.setValue)

    thread.started.connect(worker.run)
    print('start_worker - connect')

    thread.start()
    print('start_worker - start')
    # return thread, message_bar_item
    # return thread



# def worker_finished(result, thread, worker, iface, message_bar_item):
def worker_finished(result, thread, worker):
    # remove widget from message bar
    print('finnished')
    # clean up the worker and thread
    worker.deleteLater()
    thread.quit()
    thread.wait()
    thread.deleteLater()




# *********************************************************************************************************
# *********************************************************************************************************
# *********************************************************************************************************

class ExampleWorker(AbstractWorker):
    """worker, implement the work method here and raise exceptions if needed"""

    def __init__(self,project, canvas,wind):
        AbstractWorker.__init__(self)
        # self.steps = steps
        self.project = project
        self.canvas = canvas
        self.wind = wind

        # if a worker cannot define the length of the work it can set an
        # undefined progress by using
        # self.toggle_show_progress.emit(False)

    def work(self):
        self.message.emit('begin job')
        outsideqgis = False
        if outsideqgis:
            if True:
                qgis_path = "C://OSGeo4W64//apps//qgis"
            else:
                qgis_path = "C://OSGeo4W64//apps//qgis-dev"
            app = qgis.core.QgsApplication([], True)
            qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
            qgis.core.QgsApplication.initQgis()

        if False:
            print('project')
            # create project
            project = qgis.core.QgsProject.instance()
            # project = qgis.core.QgsProject()
            canvas = qgis.gui.QgsMapCanvas()


        if False:

            # inspectiondigue
            try:
                self.message.emit('load inspectiondigue')
                wind = InspectiondigueWindowWidget(self.canvas)
                path = os.path.normpath('c://000_testdigue//testdbase.sqlite')
                # path = os.path.normpath('C:\\000_testimportBM\\BD_BM_ind3.sqlite')
                self.message.emit('load inspectiondigue2')
                wind.dbase.loadQgisVectorLayers(path)
            except Exception as e:
                self.error.emit(e)

        if True:
            path = os.path.normpath('c://000_testdigue//testdbase.sqlite')
            # path = os.path.normpath('C:\\000_testimportBM\\BD_BM_ind3.sqlite')
            self.message.emit('load inspectiondigue2')
            self.wind.dbase.loadQgisVectorLayers(path)

        if True:
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
            maplayerstoadd = []
            for tablename in self.wind.dbase.dbasetables.keys():
                maplayerstoadd.append(self.wind.dbase.dbasetables[tablename]['layerqgis'])

            # project layers
            if int(str(self.wind.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().addMapLayers(maplayerstoadd)
            else:
                qgis.core.QgsProject.instance().addMapLayers(maplayerstoadd)
            root = self.project.layerTreeRoot()
            bridge = qgis.gui.QgsLayerTreeMapCanvasBridge(root, self.canvas)
            bridge.setCanvasLayers()
            # canvas.setExtent(wind.dbase.dbasetables['Infralineaire']['layer'].extent())
            # canvas.show()

            # ******************* composition
            self.message.emit('crate comp')

            mapsettings = self.canvas.mapSettings()
            if int(str(self.wind.dbase.qgisversion_int)[0:3]) < 220:
                newComposition = qgis.core.QgsComposition(mapsettings)
            else:
                newComposition = qgis.core.QgsComposition(project)

            templatepath = "C://00_Base.qpt"
            template_file = QtCore.QFile(templatepath)
            template_file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text)
            template_content = template_file.readAll()
            template_file.close()
            document = QtXml.QDomDocument()
            document.setContent(template_content)

            newComposition.loadFromTemplate(document)
            if int(str(self.wind.dbase.qgisversion_int)[0:3]) < 220:
                newComposition.composerMapItems()[0].setMapCanvas(self.canvas)
            else:
                pass

            self.message.emit('create atlas')

        if True:

            # ******************* ATLAS
            try:
                atlas = newComposition.atlasComposition()
                # atlasLayer = iface.activeLayer()
                atlas.setCoverageLayer(self.wind.dbase.dbasetables['Infralineaire']['layerqgis'])
                atlas.setEnabled(True)
                atlas.setSingleFile(True)
                ret = newComposition.setAtlasMode(qgis.core.QgsComposition.ExportAtlas)
                if int(str(self.wind.dbase.qgisversion_int)[0:3]) < 220:
                    atlas.setComposerMap(newComposition.composerMapItems()[0])
                else:
                    pass

                num = atlas.numFeatures()

                self.message.emit('mapitems' + str( newComposition.composerMapItems()))
                newComposition.composerMapItems()[0].setAtlasDriven(True)
                newComposition.composerMapItems()[0].setAtlasScalingMode(qgis.core.QgsComposerMap.Auto)
            except Exception as e:
                self.error.emit(e)

            self.message.emit('render atlas')

            try:
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
                        self.message.emit('num' + str(i) +  str(painter.isActive()))
                        # painter = QtGui.QPainter()
                        atlas.prepareForFeature(i)
                        # newComposition.beginPrintAsPDF(printer, "C:\\test.pdf")
                        # newComposition.beginPrint(printer)
                        # printReady = painter.begin(printer)
                        if i > 0:
                            printer.newPage()
                        newComposition.doPrint(printer, painter)
                        # painter.end()
                    self.message.emit('end print')
                    atlas.endRender()
                    painter.end()

                if False:
                    for i in range(0, num):
                        print('i', i)
                        ret = atlas.prepareForFeature(i)

                        # printer = QtGui.QPrinter()
                        # printer.setOutputFormat(QtGui.QPrinter.PdfFormat)

                        # newComposition.beginPrintAsPDF(printer, "C:\\test.pdf")

                        newComposition.exportAsPDF("C:\\test_" + str(i) + ".pdf")
                        # newComposition.print(printer)
                if False:
                    newComposition.exportAsPDF("C:\\test.pdf")

            except Exception as e:
                self.error.emit(e)

            if False:
                # atlas.beginRender()
                # printer = QtGui.QPrinter()
                # printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
                newComposition.exportAsPDF("C:\\testatals.pdf")

            # atlas.endRender()
            qgis.core.QgsProject.instance().clear()

        return True

    def cleanup(self):
        print "cleanup here"



def launch():
    if False:
        try:
            sys.stdout.close()
        except:
            pass
        try:
            sys.stderr.close()
        except:
            pass

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
    else:
        app = None

    #doPrintingJob()
    # app.exec_()

    print('project')
    # create project
    project = qgis.core.QgsProject.instance()
    # project = qgis.core.QgsProject()
    if outsideqgis:
        canvas = qgis.gui.QgsMapCanvas()
    else:
        canvas = qgis.utils.iface.mapCanvas()
    wind = InspectiondigueWindowWidget(canvas)

    worker = ExampleWorker(project, canvas, wind)
    start_worker(worker,app)
    if outsideqgis:
        app.exec_()

    if False:
        if outsideqgis:
            qgis.core.QgsApplication.exitQgis()
    # sys.exit(app.exec_())

    print('end')


if __name__ == '__main__':
    launch()
else:
    launch()

