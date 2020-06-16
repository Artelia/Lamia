import os, sys, qgis, qgis.core, platform

from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator, qVersion
from qgis.PyQt import QtCore, uic


lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..")
sys.path.append(lamiapath)
import Lamia
from test.settings import *

def initQGis():
    if platform.system() == "Windows":
        qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
    elif platform.system() == "Linux":
        qgis_path = "/usr"

    app = qgis.core.QgsApplication([], True)
    qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
    qgis.core.QgsApplication.initQgis()
    return app


def exitQGis():
    qgis.core.QgsApplication.exitQgis()


def getDisplayWidget():
    from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget

    # create canvas and LamiaWindowWidget
    canvas = qgis.gui.QgsMapCanvas()
    canvas.enableAntiAliasing(True)
    canvascrs = qgis.core.QgsCoordinateReferenceSystem()
    canvascrs.createFromString("EPSG:2154")
    canvas.setDestinationCrs(canvascrs)

    lamiawidget = LamiaWindowWidget()
    lamiawidget.qgiscanvas.setCanvas(canvas)

    stylesheet = """
                QMainWindow{
                            background-color: rgba(0, 55, 90,80);
                            }
                """
    stylesheet = ""
    lamiawidget.setStyleSheet(stylesheet)
    lamiawidget.setParent(None)
    # dbase = self.wind.dbase

    # add them in main widget
    mainwin = UserUI()
    mainwin.frame.layout().addWidget(canvas)
    mainwin.frame_2.layout().addWidget(lamiawidget)
    mainwin.setParent(None)
    mainwin.resize(QtCore.QSize(1600, 800))

    return mainwin, canvas, lamiawidget


def loadLocale():
    # initialize locale
    # locale = QSettings().value('locale/userLocale')[0:2]
    locale = LOCALE
    QtCore.QSettings().setValue("locale/userLocale", LOCALE)

    plugin_dir = os.path.join(os.path.dirname(Lamia.__file__))
    locale_path = os.path.join(plugin_dir, "i18n", "Lamia_{}.qm".format(locale))

    if os.path.exists(locale_path):
        translator = QTranslator()
        translator.load(locale_path)

        if qVersion() > "4.3.3":
            QCoreApplication.installTranslator(translator)
            # self.app.installTranslator(self.translator)
    return translator


class UserUI(QDialog):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "qtdialog", "mainwindows.ui")
        uic.loadUi(uipath, self)
