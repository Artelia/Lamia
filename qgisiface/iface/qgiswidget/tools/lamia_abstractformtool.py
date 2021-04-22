# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """


import qgis
import qgis.utils
from qgis.PyQt import uic, QtCore, QtGui
import logging
"""
try:
    from qgis.PyQt.QtGui import (QWidget, QTreeWidgetItem, QMessageBox, QFileDialog, QTableWidget,
                                 QHeaderView, QComboBox, QSpinBox, QCheckBox, QPushButton, QDateEdit,QDateTimeEdit, QTextEdit,
                                 QDoubleSpinBox, QDialog, QVBoxLayout, QTreeWidget, QLineEdit, QCheckBox,
                                 QLabel, QMessageBox, QTextBrowser, QTableWidgetItem,QApplication,QToolButton, QAbstractItemView)
except ImportError:
"""
from qgis.PyQt.QtWidgets import (
    QWidget,
    QTreeWidgetItem,
    QMessageBox,
    QFileDialog,
    QTableWidget,
    QHeaderView,
    QComboBox,
    QSpinBox,
    QCheckBox,
    QPushButton,
    QDateEdit,
    QDateTimeEdit,
    QTextEdit,
    QDoubleSpinBox,
    QDialog,
    QVBoxLayout,
    QTreeWidget,
    QLineEdit,
    QCheckBox,
    QFrame,
    QLabel,
    QMessageBox,
    QTextBrowser,
    QTableWidgetItem,
    QApplication,
    QToolButton,
    QAbstractItemView,
)
import os, sys, logging, pprint, shutil, datetime, time

from ..subdialogs.lamia_linkage import LinkageDialog

# from ..maptool.mapTools import mapToolCapture TODO
from .lamia_abstracttool import AbstractLamiaTool
from .lamia_abstractformutils import FormToolUtils
from .choosertreewidget.fullidchoosertreewidget import FullIDChooserTreeWidget
from .general_subwidgets.lamia_linkeditor import LamiaLinkEditor

debugconnector = False


class AbstractLamiaFormTool(AbstractLamiaTool):
    """
    This class is the abstract class for every widget loaded in the right part of te dockwidget.
    If you want another widget, you have :

    - create a file in Lamia.toolpostpro.[the_job]

    - Fill it with the following code :


    .. code-block:: python

        class ExampleTool(AbstractLamiaTool):
            TOOLNAME = 'test_module'          #is TOOLNAME exists, lamia recognize it as postpro tool

            def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
                super(ExampleTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

            def initTool(self):     # it s inside this function that we configure the minimal behaviour
                self.CAT = 'Synthese'       #The first col tree widget in the left side of lamia dock
                self.NAME = 'Couts'        #The second col tree widget in the left side of lamia dock
                self.visualmode = [4]       # put in list in which visual mode you want to see the widget (4 for post pro)

                self.groupBox_elements.setParent(None)      # disable managing part of he widget
                self.frame_editing.setParent(None)          # disable editing part of he widget

            def initFieldUI(self):      # load the widget to appear
                if self.userwdgfield is None:
                    self.userwdgfield = UserUI()

        class UserUI(QWidget):                  #load the ui made with QT Designer
            def __init__(self, parent=None):
                super(UserUI, self).__init__(parent=parent)
                uipath = os.path.join(os.path.dirname(__file__), 'test_module.ui')
                uic.loadUi(uipath, self)


    """

    saveFeatureSignal = QtCore.pyqtSignal()
    currentFeatureChanged = QtCore.pyqtSignal()
    lamiageomChanged = QtCore.pyqtSignal()
    postInitFeaturePropertiesActivated = QtCore.pyqtSignal()

    specialfieldui = []

    PARENTJOIN = None
    TABLEFILTERFIELD = {}
    SKIP_LOADING_UI = False
    # GEOMETRYSKIP = True
    CASCADEFEATURESELECTION = (
        False  # select child feature when parent feature is selected - slower
    )

    def __init__(
        self,
        dbaseparser=None,
        mainifacewidget=None,
        choosertreewidget=None,
        parentwidget=None,
        parent=None,
    ):
        """
        Initialisation of AbstractLamiaTool

        :param dbase:              The DBaseParser class
        :param dialog:             The LamiaWindowWidget class
        :param linkedtreewidget:   The QTreeWidget Wwhee the ids appears
        :param gpsutil:            the GpsUtil class for maning GPS connexion
        :param parentwidget:       the parentWidget class, in case of use in prepro
        :param parent:             the Qt parent
        """
        super(AbstractLamiaFormTool, self).__init__(
            dbaseparser=dbaseparser,
            mainifacewidget=mainifacewidget,
            choosertreewidget=choosertreewidget,
            parentwidget=parentwidget,
            parent=parent,
        )

        self.installEventFilter(self)
        # utils class
        self.formutils = FormToolUtils(self)
        # choosertreewdg
        if self.mainifacewidget is not None:
            self.choosertreewidget = FullIDChooserTreeWidget(
                toolwidget=self,
                dbaseparser=self.dbase,
                mainifacewidget=self.mainifacewidget,
            )
            self.gpsutil = self.mainifacewidget.gpsutil

        # var for widgets loaded in self.toolwidgetmainlayout

        # layoutconf
        # self.toolwidgetmainlayout = QVBoxLayout()
        # self.toolwidgetmainlayout.setMargin(0)
        # self.setLayout(self.toolwidgetmainlayout)

        self.toolwidget = None  # the widget loaded in self.toolwidgetmainlayout
        self.toolwidgetmain = None  # the widget defined in inherited class - become self.toolwidget when loaded in layout
        self.toolwidgetadvanced = None  # the widget defined in inherited class - become self.toolwidget when loaded in layout
        self.formtoolwidgetconfdict = (
            None  # dict used to link dbase column name to qtwidget objectname
        )
        self.formtoolwidgetconfdictmain = None  # dict for toolwidgetmain
        self.formtoolwidgetconfdictadvanced = None  # dict for toolwidgetadvanced
        self.dbasechildwdg = []
        self.dbasechildwdgfield = []
        self.dbasechildwdgdesktop = []

        self.lamiawidgets = []  # subwidgets defined in lamia

        # behaviour var
        self.currentFeaturePK = None  # the pk of selected feature
        self.tempgeometry = None  # the geometry edited while defining new geom
        self.activatesubwidgetchangelistener = False
        self.lastselectedpk = None
        self.tabWidgetbaralreadyconnected = False

    def _________________widgetinitialization(self):
        pass

    def _loadUI(self):
        pass
        uipath = os.path.join(os.path.dirname(__file__), "lamia_abstractformtool.ui")
        uic.loadUi(uipath, self)

        # self.titlelabel = QLabel('temp')
        ##self.titlelabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        # self.titlelabel.setAlignment(QtCore.Qt.AlignVCenter)
        # self.titlelabel.setFrameShape(QFrame.Panel)
        ##self.titlelabel.setFrameShadow(QFrame.Sunken)
        # self.titlelabel.setLineWidth(2)
        # self.frametoolwidgindicator.layout().addWidget(self.titlelabel)
        # self.frametoolwidgindicator.layout().update()

    def toolTreeWidgetCurrentItemChanged(self, param1, param2=None):
        super().toolTreeWidgetCurrentItemChanged(param1, param2=None)

        if isinstance(param1, QTreeWidgetItem) and (
            isinstance(param2, QTreeWidgetItem) or param2 is None
        ):
            if param1 == self.qtreewidgetitem:  # the openend qtreewidgetitem
                if (
                    qgis.utils.iface is not None
                    and self.DBASETABLENAME
                    in self.mainifacewidget.qgiscanvas.layers.keys()
                    and "layerqgis"
                    in self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME]
                ):
                    qgis.utils.iface.setActiveLayer(
                        self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
                            "layerqgis"
                        ]
                    )
            else:
                if self.DBASETABLENAME in self.mainifacewidget.qgiscanvas.layers.keys():
                    self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
                        "layerqgis"
                    ].removeSelection()

    def manageWidgetToLoadInMainLayout(self):
        if self.mainifacewidget.interfacemode in [0, 4]:
            if self.toolwidgetmain is None:  # first loading
                # former initFieldUI
                self.initMainToolWidget()
                if self.toolwidgetmain:
                    self.toolwidget = self.toolwidgetmain
                    self.formtoolwidgetconfdict = self.formtoolwidgetconfdictmain
                    self.formutils.initWidgetBehaviour()
                    self.formutils.connectSubWidgetModifications()
            if self.toolwidgetmain is not None:  # non first loading
                # former self.userwdg = self.userwdgfield
                self.toolwidget = self.toolwidgetmain
                # former self.linkuserwdg = self.linkuserwdgfield
                self.formtoolwidgetconfdict = self.formtoolwidgetconfdictmain
                self.dbasechildwdg = self.dbasechildwdgfield

        elif self.mainifacewidget.interfacemode == 1:
            if self.toolwidgetadvanced is None:  # first loading
                # former self.initDesktopUI()
                self.initAdvancedToolWidget()
                if self.toolwidgetadvanced:
                    self.toolwidget = self.toolwidgetadvanced
                    self.formtoolwidgetconfdict = self.formtoolwidgetconfdictadvanced
                    self.formutils.initWidgetBehaviour()
                else:
                    self.toolwidgetadvanced = self.toolwidgetmain
                    self.formtoolwidgetconfdictadvanced = (
                        self.formtoolwidgetconfdictmain
                    )
                    self.dbasechildwdgdesktop = self.dbasechildwdgfield
            if self.toolwidgetadvanced is not None:  # non first loading
                # former self.userwdg = self.userwdgdesktop
                self.toolwidget = self.toolwidgetadvanced
                # former self.linkuserwdg = self.linkuserwdgdesktop
                self.formtoolwidgetconfdict = self.formtoolwidgetconfdictadvanced
                self.dbasechildwdg = self.dbasechildwdgdesktop
            # else:
            #    self.toolwidget = self.toolwidgetmain
            #    self.formtoolwidgetconfdict = self.formtoolwidgetconfdictmain
            #    self.dbasechildwdg = self.dbasechildwdgfield

        if self.frametoolwidg.layout().count() > 0:
            # self.frametoolwidg.layout().itemAt(0).widget().setVisible(False)
            self.frametoolwidg.layout().itemAt(0).widget().setParent(None)
        # if not self.toolwidget.isVisible():
        #    self.toolwidget.setVisible(True)
        if self.toolwidget is None:  # case toolwidget deactivated for variante
            return

        self.frametoolwidg.layout().addWidget(self.toolwidget)
        if hasattr(self, "SKIP_LOADING_UI") and self.SKIP_LOADING_UI:
            pass
        else:
            self._defineQTabWidgetTabBehaviour()
            # self.toolwidget.mouseReleaseEvent=self.widgetClicked

        # propagate to childwidgets
        try:
            self.currentFeatureChanged.disconnect()
        except TypeError:
            pass
            # print('error disconnect currentFeatureChanged')

        for childwdg in self.dbasechildwdg:
            # if hasattr(childwdg,'SKIP_LOADING_UI') and childwdg.SKIP_LOADING_UI:
            #    childwdg.manageWidgetToLoadInMainLayout()
            # else:
            childwdg.manageWidgetToLoadInMainLayout()
            self.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)

    def _defineQTabWidgetTabBehaviour(self):
        self.tabWidgetmain.tabBar().setObjectName("lamia_tabbar")
        self.tabWidget.tabBar().setObjectName("lamia_tabbar")

        self.tabWidgetmain.setTabText(0, self.tooltreewidgetSUBCAT)
        self.tabWidgetmain.setTabIcon(0, QtGui.QIcon(self.tooltreewidgetICONPATH))
        self.tabWidget.setTabIcon(0, QtGui.QIcon(self.tooltreewidgetICONPATH))

        if self.parentWidget is not None:
            # parentwdg=self
            # parentlist=[]
            if (
                hasattr(self.parentWidget, "SKIP_LOADING_UI")
                and self.parentWidget.SKIP_LOADING_UI
            ):
                parenttab = self.parentWidget.parentWidget.tabWidget
            else:
                parenttab = self.parentWidget.tabWidget
            if self.tabWidget.count() > 0:
                if self.tabWidgetmain.widget(0):
                    self.tabWidgetmain.widget(0).setObjectName(
                        self.tooltreewidgetSUBCAT
                    )
                indexinserted = parenttab.addTab(
                    self.tabWidgetmain.widget(0),
                    QtGui.QIcon(self.tooltreewidgetICONPATH),
                    self.tooltreewidgetSUBCAT,
                )
            else:
                return

            def selectFirstTab(idx):
                if idx == indexinserted:
                    self.tabWidget.setCurrentIndex(0)
                    self.widgetClicked(event=None)

            parenttab.tabBarClicked.connect(lambda idx: selectFirstTab(idx))

        else:
            self.tabWidgetmain.tabBarClicked.connect(
                lambda idx: self.tabWidget.setCurrentIndex(0)
            )
            self.tabWidgetmain.tabBarClicked.connect(lambda idx: self.widgetClicked())

        def onlyFirstTabClicked(idx):
            if idx == 0:
                self.widgetClicked()

        if not self.tabWidgetbaralreadyconnected:
            self.tabWidget.tabBarClicked.connect(lambda idx: onlyFirstTabClicked(idx))
            self.tabWidgetbaralreadyconnected = True

    def eventFilter(self, obj, event):  # to work also on disabled widget
        if event.type() == QtCore.QEvent.MouseButtonRelease and event.button() == 1:
            # print('eventFilter')
            self.toolwidget.mouseReleaseEvent(event)
            # self._click.emit(self)
            return True

        return QWidget.eventFilter(self, obj, event)

    def widgetClicked(self, event=None, **kwargs):
        debug = False
        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "tablename : %s, kwargs : %s", self.DBASETABLENAME, kwargs
            )

        if (self.mainifacewidget.currenttoolwidget and 
            self.mainifacewidget.currenttoolwidget.DBASETABLENAME
            in self.mainifacewidget.qgiscanvas.layers.keys()
        ):
            self.mainifacewidget.qgiscanvas.layers[
                self.mainifacewidget.currenttoolwidget.DBASETABLENAME
            ]["layerqgis"].removeSelection()

        self.mainifacewidget.currenttoolwidget = self

        parentwidget = self
        lastparentwdgpk = None
        while parentwidget.parentWidget is not None:
            lastparentwdgpk = parentwidget.parentWidget.currentFeaturePK
            parentwidget = parentwidget.parentWidget

        if (
            self.parentWidget is not None and lastparentwdgpk is not None
        ) or self.parentWidget is None:
            self.activateChooserTreeWidget(initfeatureselection=True)
        else:
            pass

        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "%s - last sel pk : %s - lenids : %i",
                self.DBASETABLENAME,
                self.lastselectedpk,
                len(self.choosertreewidget.ids),
            )
        self._widgetClicked_manageFeatureSelectionAndChooserWidget(**kwargs)
        # select feature and update choosertreewidget
        self._widgetClicked_manageToolBar()

    def _widgetClicked_manageFeatureSelectionAndChooserWidget(self, **kwargs):

        if (
            self.lastselectedpk is not None
            and len(self.choosertreewidget.ids) > 0
            and self.lastselectedpk in self.choosertreewidget.ids.pk.values
        ):
            self.selectFeature(pk=self.lastselectedpk)
            self.choosertreewidget.selectItemfromPK(self.lastselectedpk)
        else:
            if len(self.choosertreewidget.ids) > 0:
                pk = self.choosertreewidget.ids["pk"].values[0]
                self.selectFeature(pk=pk)
                self.choosertreewidget.selectItemfromPK(pk)
            else:
                self.currentFeaturePK = None
                self.updateFormTitle(pk=None, disabletitle=True)
                # self.selectFeature(pk=None)
                self.frametoolwidg.setEnabled(False)

    def _widgetClicked_manageToolBar(self):

        # toolbar geom part
        if "geom" in self.dbase.dbasetables[self.DBASETABLENAME].keys():
            self.mainifacewidget.lamiatoolBarFormGeom.setEnabled(True)

            toolbaractions = [
                self.mainifacewidget.actiontoobargeomnewpoint,
                self.mainifacewidget.actiontoobargeomnewline,
                self.mainifacewidget.actiontoobargeomnewpolygon,
                self.mainifacewidget.actiontoobargeomaddpoint,
                # self.mainifacewidget.actiontoobargeomaddGPSpoint,
                # self.mainifacewidget.actiontoobargeomeditlayer
            ]
            dbaselayertype = self.dbase.dbasetables[self.DBASETABLENAME]["geom"]
            if "POINT" in dbaselayertype:
                conf = [True, False, False, False]
            elif "LINESTRING" in dbaselayertype:
                if self.DBASETABLENAME in [
                    "Equipement",
                    "Desordre",
                    "equipment",
                    "deficiency",
                ]:
                    conf = [True, True, False, True]
                else:
                    conf = [False, True, False, True]
            elif "POLYGON" in dbaselayertype:
                conf = [False, False, True, True]
            dictwhattodo = dict(zip(toolbaractions, conf))
            for action, boolenabled in dictwhattodo.items():
                action.setEnabled(boolenabled)
        else:
            self.mainifacewidget.lamiatoolBarFormGeom.setEnabled(False)

        # lamiatoolBarFormCreation part
        # toolbar form creation
        if "toolbarMagic" in self.__class__.__dict__:  # implemented
            self.mainifacewidget.actiontoolbarmagic.setEnabled(True)
        else:
            self.mainifacewidget.actiontoolbarmagic.setEnabled(False)

        if self.parentWidget is not None and self.parentWidget.currentFeaturePK is None:
            self.mainifacewidget.lamiatoolBarFormCreation.setEnabled(False)
        else:
            self.mainifacewidget.lamiatoolBarFormCreation.setEnabled(True)

        # lamiatoolBarTools part
        if self.currentFeaturePK is not None:
            self.mainifacewidget.lamiatoolBartools.setEnabled(True)
            if "printWidget" in self.__class__.__dict__:  # implemented
                self.mainifacewidget.actiontoolbartoolsprint.setEnabled(True)
            else:
                self.mainifacewidget.actiontoolbartoolsprint.setEnabled(False)

        else:
            self.mainifacewidget.lamiatoolBartools.setEnabled(False)

    def loadChildFeatureinWidget(self):
        debug = False
        # print('loadChildFeatureinWidget', self.DBASETABLENAME)
        self.choosertreewidget.loadIds()
        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "%s - pk:%s / %s \n %s",
                self.parentWidget.DBASETABLENAME,
                self.parentWidget.currentFeaturePK,
                self.DBASETABLENAME,
                self.choosertreewidget.ids,
            )
        if self.CASCADEFEATURESELECTION or self.SKIP_LOADING_UI:
            if len(self.choosertreewidget.ids) == 0:
                self.selectFeature(pk=None, disabletitle=True)
            else:
                self.selectFeature(pk=self.choosertreewidget.ids["pk"][0])

    def initMainToolWidget(self):
        pass

    def initAdvancedToolWidget(self):
        pass

    def postToolTreeWidgetCurrentItemChanged(self):
        self.tabWidget.setCurrentIndex(0)
        self.widgetClicked()
        """
        if self.lastselectedpk is not None:
            self.setEnabled(True)
            self.selectFeature(pk=self.lastselectedpk)
        elif len(self.choosertreewidget.ids)>0:
            self.setEnabled(True)
            self.selectFeature(pk=self.choosertreewidget.ids['pk'].values[0])
        else:
            self.setEnabled(False)
        """

    def updateToolbarOnToolFrameLoading(self):
        if self.mainifacewidget is not None:
            self.mainifacewidget.lamiatoolBarFormCreation.setEnabled(True)
            self.mainifacewidget.lamiatoolBarFormGeom.setEnabled(True)

    def subwidgetChanged(self):
        if self.activatesubwidgetchangelistener:
            self.updateFormTitleBackground(subwidgethaschanged=True)

    # *************************************************************
    # toolbar
    # *************************************************************

    def ____________________ToolBarActions():
        pass

    def selectFeature(self, **kwargs):
        # print('selectFeature',self.DBASETABLENAME, kwargs)
        debug = False
        self.setEnabled(True)

        self.activatesubwidgetchangelistener = False
        self.tempgeometry = None
        if debug:
            logging.getLogger("Lamia_unittest").debug("kwargs %s", str(kwargs))
        self.currentFeaturePK = kwargs.get("pk", None)
        # rubberband actions
        # if self.parentWidget is None:
        self._manageRubberbandOnSelectFeature(self.currentFeaturePK)

        # remember feature pk
        if self.currentFeaturePK:
            self.lastselectedpk = self.currentFeaturePK
            self.mainifacewidget.actiontoolbarnew.setEnabled(True)

        # layer action
        if self.parentWidget is None and self.DBASETABLENAME is not None:
            if self.DBASETABLENAME in self.mainifacewidget.qgiscanvas.layers.keys():
                self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
                    "layer"
                ].removeSelection()
            # self.dbasetable['layer'].removeSelection()
        # form title action
        self.updateFormTitle(**kwargs)
        # load values in form
        resultdict = self.formutils.getDictValuesForWidget(
            featurepk=self.currentFeaturePK
        )
        if debug:
            logging.getLogger("Lamia_unittest").debug("resultdict %s", str(resultdict))
        self.formutils.applyResultDict(resultdict)
        # end actions
        self.postSelectFeature()
        for lidchooser in self.lamiawidgets:
            lidchooser.postSelectFeature()
        if (
            self.currentFeaturePK is not None
        ):  # activate listener only with existing feat
            self.activatesubwidgetchangelistener = True

        self.currentFeatureChanged.emit()

    def toolbarNew(self):
        self.mainifacewidget.actiontoolbarnew.setEnabled(False)
        self._manageRubberbandOnSelectFeature(None)
        self.selectFeature()

    def toolbarMagic(self):
        pass

    def toolbarZoomTo(self):
        if self.currentFeaturePK is not None:
            qgiscanvas = self.mainifacewidget.qgiscanvas
            qgiscanvas.zoomToFeature(self.DBASETABLENAME, self.currentFeaturePK)
            qgslayer = qgiscanvas.layers[self.DBASETABLENAME]["layerqgis"]
            qgiscanvas.canvas.flashFeatureIds(qgslayer, [self.currentFeaturePK])

    def toolbarEditLink(self):
        self.linkeditor = LamiaLinkEditor(self, self.currentFeaturePK)
        if qgis.utils.iface is not None:
            self.linkeditor.setWindowModality(QtCore.Qt.NonModal)
            self.linkeditor.show()
        else:
            self.mainifacewidget.parent().layout().addWidget(self.linkeditor)

    def toolbarUndo(self):
        if self.currentFeaturePK is not None:
            self.selectFeature(pk=self.currentFeaturePK)
        elif self.lastselectedpk is not None:
            self.selectFeature(pk=self.lastselectedpk)
        else:
            pass

    def toolbarSave(self):
        self.formutils.saveFeature(featurepk=self.currentFeaturePK)

    def toolbarGeom(self):

        sender = self.mainifacewidget.sender()
        if sender is not None:
            logging.getLogger("Lamia_unittest").debug(
                "toolbarGeom %s", str(sender.objectName())
            )

        if sender is not None and "addpoint" not in sender.objectName():
            listpointinitialgeometry = []
        else:
            listpointinitialgeometry = self._getCurrentGeomasList()

        if "point" in sender.objectName():
            capturetype = 0
        elif "line" in sender.objectName():
            capturetype = 1
        elif "polygon" in sender.objectName():
            capturetype = 2

        self.mainifacewidget.qgiscanvas.captureGeometry(
            capturetype=capturetype,
            listpointinitialgeometry=listpointinitialgeometry,
            fctonstopcapture=self.setTempGeometry,
        )

    def toolbarGeomAddGPS(self):
        """
        Method called by add GPS Point Button

        """
        if self.gpsutil and self.gpsutil.currentpoint is None:
            self.mainifacewidget.connector.showErrorMessage(
                self.tr("GPS not connected")
            )
            return

        geomtype = self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
            "layer"
        ].geometryType()
        self.mainifacewidget.qgiscanvas.createorresetRubberband(
            geomtype, rubtype="capture"
        )
        layerpoint = self.gpsutil.currentpoint

        if geomtype == 0:  # POINT
            self.setTempGeometry([layerpoint], False)

        elif geomtype == 1:  # LINE
            geom = None
            geompoly = self._getCurrentGeomasList()
            if not geompoly:
                self.setTempGeometry([layerpoint, layerpoint], False)
            else:
                # geompoly = self.tempgeometry.asMultiPolyline()[0]
                if geompoly[0] == geompoly[1]:
                    del geompoly[0]
                geompoly.append(layerpoint)
                self.setTempGeometry(geompoly, False)
            """
            if self.currentFeaturePK is not None and self.currentFeature.geometry() is not None:
                # geom = self.currentFeature.geometry()
                # geompoly = geom.asPolyline()
                geompoly = self._getCurrentGeomasList()
                geompoly.append(layerpoint)
                self.setTempGeometry(geompoly,False)
            else:
                if self.tempgeometry is None:
                    self.setTempGeometry([layerpoint,layerpoint],False)
                else:
                    geompoly = self.tempgeometry.asMultiPolyline()[0]
                    if geompoly[0] == geompoly[1]:
                        del geompoly[0]
                    geompoly.append(layerpoint)
                    self.setTempGeometry(geompoly,False)
            """

    def _getCurrentGeomasList(self):
        geomtype = self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
            "layer"
        ].geometryType()
        # self.createorresetRubberband(type)
        initialgeom = []
        if geomtype == 0:
            if self.tempgeometry is not None:
                initialgeom = self.tempgeometry.asPoint()
            else:
                initialgeomwkt = self.dbase.getValuesFromPk(
                    self.DBASETABLENAME, "ST_AsText(geom)", self.currentFeaturePK
                )
                initialgeom = qgis.core.QgsGeometry.fromWkt(initialgeomwkt).asPoint()

        elif geomtype == 1:  # LINE
            # get the geometry before editing
            if self.tempgeometry is not None:
                if not self.tempgeometry.isMultipart():
                    initialgeom = self.tempgeometry.asPolyline()
                else:
                    initialgeom = self.tempgeometry.asMultiPolyline()[0]
            elif self.currentFeaturePK is not None and self.tempgeometry is None:

                # initialgeom = self.currentFeature.geometry().asPolyline()
                initialgeomwkt = self.dbase.getValuesFromPk(
                    self.DBASETABLENAME, "ST_AsText(geom)", self.currentFeaturePK
                )
                initialgeom = qgis.core.QgsGeometry.fromWkt(initialgeomwkt).asPolyline()

        return initialgeom

    def toolbarDelete(self):

        # message = self.tr("Supprimer completement l'element (yes) ou l'archiver (no) ? ")
        if self.dbase.offlinemode:
            self.formutils.archiveFeature()
        else:
            message = self.tr("Delete feature (yes) or archive (no) ? ")
            reply = QMessageBox.question(
                self,
                "Su",
                message,
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
            )
            if reply == QMessageBox.Yes:
                self.formutils.deleteFeature()

            elif reply == QMessageBox.No:
                self.formutils.archiveFeature()

        if self.DBASETABLENAME in self.mainifacewidget.qgiscanvas.layers.keys():
            self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
                "layerqgis"
            ].triggerRepaint()
        # self.canvas.refresh()
        # self.loadChildFeatureinWidget()

    def printWidget(self):
        pass

    def ____________________________________ToolBarActionsFunctions(self):
        pass

    def updateFormTitle(self, **kwargs):
        # self.toolBoxmain

        if self.currentFeaturePK:
            # featureid = self.dbase.getValuesFromPk(self.DBASETABLENAME,
            #                                     'id_' + self.DBASETABLENAME.lower(),
            #                                         self.currentFeaturePK)
            for i in range(1, self.tabWidget.count()):
                self.tabWidget.setTabEnabled(i, True)
        else:
            # featureid = 'New'
            for i in range(1, self.tabWidget.count()):
                self.tabWidget.setTabEnabled(i, False)

        if False:
            parentwidget = self
            while parentwidget.parentWidget is not None:
                parentwidget = parentwidget.parentWidget

            toolbox = parentwidget.toolBoxmain
            finalpageindex = 0
            for pageindex in range(toolbox.count()):
                print("po", pageindex, toolbox.widget(pageindex).parent().__dict__)
                if toolbox.widget(pageindex) == self.frametoolwidg:
                    finalpageindex == pageindex
                    break
            toolbox.setItemText(
                finalpageindex, "{}({})".format(self.DBASETABLENAME, featureid)
            )
            # self.toolBoxmain.setItemText(0,'{}({})'.format(self.DBASETABLENAME,
            #                                              featureid) )
            # self.titlelabel.setText('{}({})'.format(self.DBASETABLENAME,
            #                                              featureid) )
        self.updateFormTitleBackground(**kwargs)

    def updateFormTitleBackground(
        self, subwidgethaschanged=False, disabletitle=False, **kwargs
    ):
        # print('updateFormTitleBackground', self.DBASETABLENAME, subwidgethaschanged,disabletitle)
        # styling = '.QTabBar::tab:selected , QTabBar * {border-color: rgb(0, 0, 0);'
        # tabbarname = self.tabWidget.tabBar().objectName()
        tabbarname = "lamia_tabbar"
        styling = ".QTabBar::tab:selected#{}".format(tabbarname)
        styling += " {border-color: rgb(0, 0, 0);"
        tabwidgetlist = [self.tabWidget]

        if subwidgethaschanged or disabletitle:
            if subwidgethaschanged:
                styling += " background-color : rgb(0, 0, 255) }"
                self.activatesubwidgetchangelistener = False
            if disabletitle:
                styling += " background-color : rgb(150, 150, 150) }"
            for wdg in tabwidgetlist:
                wdg.setStyleSheet(styling)

        else:
            if self.currentFeaturePK is not None:
                styling += " background-color : rgb(0, 255, 0) }"
            else:
                styling += " background-color : rgb(255, 0, 0) }"
            for wdg in tabwidgetlist:
                wdg.setStyleSheet(styling)

    def _manageRubberbandOnSelectFeature(self, pkfeature=None):

        self.mainifacewidget.qgiscanvas.createorresetRubberband(rubtype="capture")
        if pkfeature:
            self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
                "layerqgis"
            ].removeSelection()
            self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
                "layerqgis"
            ].select(pkfeature)
        else:
            self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
                "layerqgis"
            ].removeSelection()

        if self.parentWidget is None:
            if (
                "geom" in self.dbase.dbasetables[self.DBASETABLENAME].keys()
                and pkfeature
            ):
                currentgeom = self.formutils.getQgsGeomFromPk(pkfeature)
                self.mainifacewidget.qgiscanvas.createRubberBandForSelection(
                    currentgeom, rubtype="main"
                )
                # self.mainifacewidget.qgiscanvas.rubberBand.show()
            else:
                self.mainifacewidget.qgiscanvas.createorresetRubberband(rubtype="main")
            self.mainifacewidget.qgiscanvas.createorresetRubberband(rubtype="child")
        else:
            crtwdg = self.mainifacewidget.currenttoolwidget
            if crtwdg and crtwdg == self:
                if (
                    "geom" in self.dbase.dbasetables[self.DBASETABLENAME].keys()
                    and pkfeature
                ):
                    currentgeom = self.formutils.getQgsGeomFromPk(pkfeature)
                    self.mainifacewidget.qgiscanvas.createRubberBandForSelection(
                        currentgeom, distpixel=1.0, rubtype="child"
                    )
                    # self.rubberBand.show()
                else:
                    self.mainifacewidget.qgiscanvas.createorresetRubberband(
                        rubtype="child"
                    )

    def postSelectFeature(self):
        pass

    def postSaveFeature(self, pkfeature=None):
        pass

    def postDeleteFeature(self):
        pass

    def setTempGeometry(self, points, comefromcanvas=True, showinrubberband=True):
        """
        Called when self.currentmaptool has finished capturing

        Assign the geometry to self.tempgeometry

        :param points: the list of points coming from the currentmaptool
        :param comefromcanvas: True if come from canvas (need od reprojection)
        :param showinrubberband: True if the temp geometry will be visible with the rubberband

        """
        debug = False

        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "start points : %s %s", self.DBASETABLENAME, points
            )
        self.mainifacewidget.qgiscanvas.stopCapture()

        pointsmapcanvas = []
        pointslayer = []

        #* Define maptoolcapturetype : the geomtypecaptured & capturetype : geomtype of layer
        try:
            maptoolcapturetype = int(self.sender().mode())     #1 point 2 line 3 polygon
        except AttributeError:  #no sender - debug mode
            maptoolcapturetype = self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME]["layer"].geometryType()
            # logging.getLogger("Lamiaoffline").debug(maptoolcapturetypestring)

        capturetype = self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME][
            "layer"
        ].geometryType()        # 0 point 1 line 2 polygone 3 unknow 4 null geom


        #* Modify captured geom to fit the layer geom
        if maptoolcapturetype == 1 and capturetype == 1:
            points.append(points[0])
        elif maptoolcapturetype == 1 and capturetype == 2:
                points = [
                    qgis.core.QgsPointXY(points[0].x() - 1.0, points[0].y() - 1.0),
                    qgis.core.QgsPointXY(points[0].x() - 1.0, points[0].y() + 1.0),
                    qgis.core.QgsPointXY(points[0].x() + 1.0, points[0].y() + 1.0),
                    qgis.core.QgsPointXY(points[0].x() + 1.0, points[0].y() - 1.0),
                ]
        elif maptoolcapturetype == 3 and capturetype == 1:
            points.append(points[0])


        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "type/point : %s %s", str(capturetype), points
            )
        #* crs transformation
        if comefromcanvas:
            pointsmapcanvas = points
            for point in points:
                pointslayer.append(
                    self.mainifacewidget.qgiscanvas.xformreverse.transform(point)
                )
        else:
            pointslayer = points
            for point in points:
                pointsmapcanvas.append(
                    self.mainifacewidget.qgiscanvas.xform.transform(point)
                )

        #* process geom depending use : for rubberband or for layer storage
        if capturetype == 0:
            geometryformap = qgis.core.QgsGeometry.fromPointXY(pointsmapcanvas[0])
            geometryforlayer = qgis.core.QgsGeometry.fromPointXY(pointslayer[0])
        elif capturetype == 1 and maptoolcapturetype == 1:   
            geometryformap = qgis.core.QgsGeometry.fromPointXY(pointsmapcanvas[0])
            geometryforlayer = qgis.core.QgsGeometry.fromMultiPolylineXY([pointslayer])
        elif capturetype == 1:
            geometryformap = qgis.core.QgsGeometry.fromMultiPolylineXY(
                [pointsmapcanvas]
            )
            geometryforlayer = qgis.core.QgsGeometry.fromMultiPolylineXY([pointslayer])
        elif capturetype == 2 and maptoolcapturetype in [1,3]:     
            geometryformap = qgis.core.QgsGeometry.fromPolygonXY([pointsmapcanvas])
            geometryforlayer = qgis.core.QgsGeometry.fromPolygonXY([pointslayer])

        #* show geom in rubberband
        if showinrubberband:
            if capturetype == 1 and maptoolcapturetype == 1:   
                self.mainifacewidget.qgiscanvas.createorresetRubberband(
                    0, rubtype="capture"
                )
            elif capturetype  in [1,2,3]:
                self.mainifacewidget.qgiscanvas.createorresetRubberband(
                    capturetype, rubtype="capture"
                )

            else:
                self.mainifacewidget.qgiscanvas.createorresetRubberband(
                    0, rubtype="capture"
                )

            self.mainifacewidget.qgiscanvas.rubberbands["capture"].addGeometry(
                geometryformap, None
            )
            self.mainifacewidget.qgiscanvas.rubberbands["capture"].show()

        #* final : set self.tempgeometry
        self.tempgeometry = geometryforlayer
        self.lamiageomChanged.emit()

        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "end layer points : %s", pointslayer
            )
        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "end canvas points : %s", pointsmapcanvas
            )
