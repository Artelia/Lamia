# -*- coding: utf-8 -*-

import os
import sys
import qgis
import datetime
import qgis.gui
import qgis.utils
import shutil
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt

from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget

try:
    from qgis.PyQt.QtGui import (QWidget,QDialog,QMainWindow)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow)


# *********************************************************************************************************************
# ******************************************   MAIN      *************************************************************
# *********************************************************************************************************************

class Test(QtCore.QObject):

    def __init__(self):
        QtCore.QObject.__init__(self)
        self.wind = None
        self.dbase = None
        self.app = None





    def launchTest(self):

        try:
            qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
        except AttributeError:  #qgis 3
            qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT
        #print(qgisversion_int)

        if int(str(qgisversion_int)[0:3]) < 220:
            qgis_path = "C://OSGeo4W64//apps//qgis218"
            qgis_path = "C://Program Files//OSGeo4W64//apps//qgis-ltr"
        else:
            qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
            #os.environ["QT_QPA_PLATFORM"] = "offscreen"

        self.app = qgis.core.QgsApplication([], True)
        qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
        qgis.core.QgsApplication.initQgis()
        self.canvas = qgis.gui.QgsMapCanvas()
        self.canvas.enableAntiAliasing(True)
        self.canvas.setDestinationCrs(qgis.core.QgsCoordinateReferenceSystem(2154))

        self.loadLocale()


        self.testMethod()
        #program.run(self.canvas, True, "spatialite")
        self.app.exec_()
        qgis.core.QgsApplication.exitQgis()
        print('Test fini')

    def loadLocale(self):
        # initialize locale
        # locale = QSettings().value('locale/userLocale')[0:2]
        locale = 'fr'
        plugin_dir = os.path.join(os.path.dirname(__file__),'..', 'Lamia')
        locale_path = os.path.join(
            plugin_dir,
            'i18n',
            'Lamia_{}.qm'.format(locale))

        print(locale_path,qVersion() )

        if os.path.exists(locale_path):
            print('ok')
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
                #self.app.installTranslator(self.translator)

    def testMethod(self):
        pass


    def createWin(self):
        self.wind = InspectiondigueWindowWidget(self.canvas)
        self.wind.createDBase()

        stylesheet = """
                    QMainWindow{
                                background-color: rgba(0, 55, 90,80);
                                }
                    """
        stylesheet = ''
        self.wind.setStyleSheet(stylesheet)
        self.wind.setParent(None)
        self.dbase = self.wind.dbase
        self.mainwin = None


    def loadLayersInCanvas(self):



        layerstoadd = []
        for tablename in self.wind.dbase.dbasetables.keys():
            if sys.version_info.major == 2:
                layerstoadd.append(qgis.gui.QgsMapCanvasLayer(self.wind.dbase.dbasetables[tablename]['layerqgis']))
            elif sys.version_info.major == 3:
                layerstoadd.append(self.wind.dbase.dbasetables[tablename]['layerqgis'])

        if sys.version_info.major == 2:
            self.canvas.setLayerSet(layerstoadd)
        else:
            self.canvas.setLayers(layerstoadd)
        # canvas.show()
        # canvas.setExtent(qgis.core.QgsRectangle(0, 0, 1, 1))
        self.canvas.setExtent(self.wind.dbase.dbasetables['Infralineaire']['layer'].extent())
        self.canvas.refresh()

    def createMainWin(self):
        self.mainwin = UserUI()
        self.mainwin.frame.layout().addWidget(self.canvas)
        self.mainwin.frame_2.layout().addWidget(self.wind)
        if False:
            self.wind.loadUiDesktop()
            self.wind.applyVisualMode()
        self.mainwin.setParent(None)




class UserUI(QDialog):

    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'mainwindows_1.ui')
        uic.loadUi(uipath, self)