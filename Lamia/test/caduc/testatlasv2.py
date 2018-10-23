# -*- coding: utf-8 -*-
"""
import sys
sys.path.append('C://OSGeo4W64//apps//qgis//python')
sys.path.append('C://OSGeo4W64//apps//Python27//Lib//site-packages')
"""
import os
import sys
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
    error = QtCore.pyqtSignal(Exception, basestring)
    progress = QtCore.pyqtSignal(float)
    toggle_show_progress = QtCore.pyqtSignal(bool)
    set_message = QtCore.pyqtSignal(str)
    toggle_show_cancel = QtCore.pyqtSignal(bool)

    # private signal, don't use in concrete workers this is automatically
    # emitted if the result is not None
    successfully_finished = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QObject.__init__(self)
        self.killed = False

    def run(self):
        try:
            result = self.work()
            self.finished.emit(result)
        except UserAbortedNotification:
            self.finished.emit(None)
        except Exception, e:
            # forward the exception upstream
            self.error.emit(e, traceback.format_exc())
            self.finished.emit(None)

    def work(self):
        """ Reimplement this putting your calculation here
            available are:
                self.progress.emit(0-100)
                self.killed
            :returns a python object - use None if killed is true
        """

        raise NotImplementedError

    def kill(self):
        self.is_killed = True
        self.set_message.emit('Aborting...')
        self.toggle_show_progress.emit(False)


class UserAbortedNotification(Exception):
    pass


#def start_worker(worker, iface, message, with_progress=True):
def start_worker(worker):
    # configure the QgsMessageBar
    print('start_worker')
    if False:
        message_bar_item = iface.messageBar().createMessage(message)
        progress_bar = QtGui.QProgressBar()
        progress_bar.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        if not with_progress:
            progress_bar.setMinimum(0)
            progress_bar.setMaximum(0)
        cancel_button = QtGui.QPushButton()
        cancel_button.setText('Cancel')
        cancel_button.clicked.connect(worker.kill)
        message_bar_item.layout().addWidget(progress_bar)
        message_bar_item.layout().addWidget(cancel_button)
        iface.messageBar().pushWidget(message_bar_item, iface.messageBar().INFO)

    # start the worker in a new thread
    # let Qt take ownership of the QThread
    # thread = QtCore.QThread(iface.mainWindow())
    thread = QtCore.QThread()
    worker.moveToThread(thread)

    if False:
        worker.set_message.connect(lambda message: set_worker_message(
            message, message_bar_item))

        worker.toggle_show_progress.connect(lambda show: toggle_worker_progress(
            show, progress_bar))

        worker.toggle_show_cancel.connect(lambda show: toggle_worker_cancel(
            show, cancel_button))



        worker.error.connect(lambda e, exception_str: worker_error(
            e, exception_str, iface))


    if True:
        # worker.finished.connect(lambda result: worker_finished(result, thread, worker, iface, message_bar_item))
        worker.finished.connect(worker_finished)

    # worker.progress.connect(progress_bar.setValue)

    thread.started.connect(worker.run)
    print('start_worker - connect')

    thread.start()
    print('start_worker - start')
    # return thread, message_bar_item
    # return thread


# def worker_finished(result, thread, worker, iface, message_bar_item):
def worker_finished(result):
    # remove widget from message bar
    print('finnished')
    if False:
        iface.messageBar().popWidget(message_bar_item)
        if result is not None:
            # report the result
            iface.messageBar().pushMessage('The result is: %s.' % result)
            worker.successfully_finished.emit(result)

    # clean up the worker and thread
    worker.deleteLater()
    thread.quit()
    thread.wait()
    thread.deleteLater()


def worker_error(e, exception_string, iface):
    # notify the user that something went wrong
    iface.messageBar().pushMessage(
        'Something went wrong! See the message log for more information.',
        level=qgis.gui.QgsMessageBar.CRITICAL,
        duration=3)
    qgis.gui.QgsMessageLog.logMessage(
        'Worker thread raised an exception: %s' % exception_string,
        'SVIR worker',
        level=qgis.gui.QgsMessageLog.CRITICAL)


def set_worker_message(message, message_bar_item):
    message_bar_item.setText(message)


def toggle_worker_progress(show_progress, progress_bar):
    progress_bar.setMinimum(0)
    if show_progress:
        progress_bar.setMaximum(100)
    else:
        # show an undefined progress
        progress_bar.setMaximum(0)


def toggle_worker_cancel(show_cancel, cancel_button):
    cancel_button.setVisible(show_cancel)



# *********************************************************************************************************
# *********************************************************************************************************
# *********************************************************************************************************

class ExampleWorker(AbstractWorker):
    """worker, implement the work method here and raise exceptions if needed"""

    def __init__(self):
        AbstractWorker.__init__(self)
        # self.steps = steps

        # if a worker cannot define the length of the work it can set an
        # undefined progress by using
        # self.toggle_show_progress.emit(False)

    def work(self):
        print('begin job')
        outsideqgis = True
        if outsideqgis:
            if True:
                qgis_path = "C://OSGeo4W64//apps//qgis"
            else:
                qgis_path = "C://OSGeo4W64//apps//qgis-dev"
            app = qgis.core.QgsApplication([], True)
            qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
            qgis.core.QgsApplication.initQgis()



        # create project
        project = qgis.core.QgsProject.instance()
        # project = qgis.core.QgsProject()
        canvas = qgis.gui.QgsMapCanvas()




        # inspectiondigue
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
        maplayerstoadd = []
        for tablename in wind.dbase.dbasetables.keys():
            maplayerstoadd.append(wind.dbase.dbasetables[tablename]['layerqgis'])

        # project layers
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

        templatepath = "C://00_Base.qpt"
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
            # atlasLayer = iface.activeLayer()
            atlas.setCoverageLayer(wind.dbase.dbasetables['Infralineaire']['layerqgis'])
            atlas.setEnabled(True)
            atlas.setSingleFile(True)
            ret = newComposition.setAtlasMode(qgis.core.QgsComposition.ExportAtlas)
            if int(str(wind.dbase.qgisversion_int)[0:3]) < 220:
                atlas.setComposerMap(newComposition.composerMapItems()[0])
            else:
                pass

            num = atlas.numFeatures()

            print('mapitems', newComposition.composerMapItems())
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
                    print('num', i, painter.isActive())
                    # painter = QtGui.QPainter()
                    atlas.prepareForFeature(i)
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
                    print('i', i)
                    ret = atlas.prepareForFeature(i)

                    # printer = QtGui.QPrinter()
                    # printer.setOutputFormat(QtGui.QPrinter.PdfFormat)

                    # newComposition.beginPrintAsPDF(printer, "C:\\test.pdf")

                    newComposition.exportAsPDF("C:\\test_" + str(i) + ".pdf")
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

        return True

    def cleanup(self):
        print "cleanup here"



def launch():

    print('begin')
    outsideqgis = True
    # app = QtGui.QApplication(sys.argv)
    if False:
        if outsideqgis:
            if True:
                qgis_path = "C://OSGeo4W64//apps//qgis"
            else:
                qgis_path = "C://OSGeo4W64//apps//qgis-dev"
            app = qgis.core.QgsApplication([], True)
            qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
            qgis.core.QgsApplication.initQgis()

    #doPrintingJob()
    # app.exec_()
    worker = ExampleWorker()
    start_worker(worker)

    if False:
        if outsideqgis:
            qgis.core.QgsApplication.exitQgis()
        # sys.exit(app.exec_())

    print('end')


if __name__ == '__main__':
    launch()
else:
    launch()

