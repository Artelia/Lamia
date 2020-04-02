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

from qgis.PyQt.QtWidgets import (QWidget, QTreeWidgetItem, QAbstractItemView)
import os, sys, logging

from ..subdialogs.lamia_linkage import LinkageDialog
# from ..maptool.mapTools import mapToolCapture TODO

class AbstractLamiaTool(QWidget):
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
    
    DBASETABLENAME = None
    LOADFIRST=False
    POSTPROTOOLNAME = None

    # tooltreewidget conf
    tooltreewidgetCAT = None
    tooltreewidgetSUBCAT = None
    tooltreewidgetICONPATH = None
    # choosertreewidget conf
    choosertreewidgetMUTIPLESELECTION = False

    def __init__(self, 
                 dbaseparser=None, 
                 mainifacewidget=None, 
                 choosertreewidget=None, 
                 parentwidget=None, 
                 parent=None):
        """
        Initialisation of AbstractLamiaTool

        :param dbaseparser:              The DBaseParser class
        :param mainifacewidget:             The mainifacewidget class
        :param choosertreewidget:   The QTreeWidget Wwhee the ids appears
        :param parentwidget:       the parentWidget class
        :param parent:             the Qt parent

        ***************************************************************
        ******************      mainifacewidget************************
        ***************************************************************
        *           *                                                 *
        * tool      *    mainifacewidget.toolframe.addWidget(self)    *
        * treewidget*                                                 *
        *           *                                                 *
        *           *                                                 *
        *           *                                                 *
        *************                                                 *
        *           *                                                 *
        * chooser   *                                                 *
        * treewidget*                                                 *
        *           *                                                 *
        *           *                                                 *
        ***************************************************************
        ***************************************************************

        """
        super(AbstractLamiaTool, self).__init__(parent)
        self._loadUIForm()

        # ***** main var
        self.dbase = dbaseparser
        self.parentWidget = parentwidget
        self.mainifacewidget = mainifacewidget
        self.tooltreewidget = self.mainifacewidget.MaintreeWidget
        self.choosertreewidget = choosertreewidget

        # var used by tooltreewidget
        if self.mainifacewidget is not None:
            self.mainifacewidget.MaintreeWidget.currentItemChanged.connect(self.loadWidgetInToolFrame)
        self.qtreewidgetitem = None     #the tool treewidgetitem in tooltreewidget

    
    def _loadUIForm(self):
        pass

    def ___________________widgetBehaviourWithToolTreeWidget(self):
        pass

    def changeInterfaceMode(self, interfacename=None, preloadwidgfunc=None, postloadwidgfunc=None):
        self.manageLoadingInToolTreeWidget()

    def manageLoadingInToolTreeWidget(self):
        
        if self.mainifacewidget.interfacemode == 0:
            if self.DBASETABLENAME and self.LOADFIRST:
                self.loadWidgetinToolTree()
            else:
                self.unloadWidgetinToolTree()
        elif self.mainifacewidget.interfacemode == 1:
            if self.DBASETABLENAME:
                self.loadWidgetinToolTree()
            else:
                self.unloadWidgetinToolTree()
        elif self.mainifacewidget.interfacemode == 4:
            if self.POSTPROTOOLNAME:
                self.loadWidgetinToolTree()
            else:
                self.unloadWidgetinToolTree()

    def loadWidgetinToolTree(self):
        """
        Called on the widget creation in windowsdialog
        load the widget in the main stacked widget
        call onActivationRaw when qtreewidgetitem is clicked in MaintreeWidget
        """
        # add qtreewidget item in MaintreeWidget
        
        if self.mainifacewidget is not None and self.parentWidget is None:
            
            arb = [self.tooltreewidgetCAT, self.tooltreewidgetSUBCAT]
            if self.qtreewidgetitem is None:
                self.qtreewidgetitem = QTreeWidgetItem()
                self.qtreewidgetitem.setText(0, arb[-1])
                self.qtreewidgetitem.setFlags(self.qtreewidgetitem.flags())
                if self.tooltreewidgetICONPATH is not None:
                    self.qtreewidgetitem.setIcon(0, QtGui.QIcon(self.tooltreewidgetICONPATH))
            wdgitem = None
            root = self.tooltreewidget.invisibleRootItem()
            child_count = root.childCount()
            for i in range(child_count):
                item = root.child(i)
                if item.text(0) == arb[0]:
                    wdgitem = item
                    break
            if wdgitem is None:
                wdgitem = QTreeWidgetItem()
                wdgitem.setText(0, arb[0])
                self.tooltreewidget.addTopLevelItems([wdgitem])
            if self.qtreewidgetitem not in [wdgitem.child(i) for i in range(wdgitem.childCount())]:
                wdgitem.addChild(self.qtreewidgetitem)
            wdgitem.setExpanded(True)

    def unloadWidgetinToolTree(self):
        """
        Unload the widget in the main stacked widget
        """
        arb = [self.tooltreewidgetCAT, self.tooltreewidgetSUBCAT]
        if self.mainifacewidget is not None:
            wdgitem = None
            root = self.tooltreewidget.invisibleRootItem()
            child_count = root.childCount()
            for i in range(child_count):
                item = root.child(i)
                if item.text(0) == arb[0]:
                    wdgitem = item
                    break
            if wdgitem is None:
                wdgitem = root
            wdgitem.removeChild(self.qtreewidgetitem)
            if wdgitem != self.tooltreewidget.invisibleRootItem() and wdgitem.childCount() == 0:
                self.tooltreewidget.invisibleRootItem().removeChild(wdgitem)

            # self.disconnectIdsGui()

    def loadWidgetInToolFrame(self, param1, param2=None):
        """
        Manage the activation of widget when tool's icon is clicked on main QTreeWidget

        Do:

        - display tool widget

        - load features in ElemtreeWidget

        - connect ElemtreeWidget click to featureSelected

        - Finaly, call postOnActivation method, which is a function to be overloaded

        TODO : display or not the layer


        :param param1:  a QTreeWidgetItem (the one activated in main QTreeWidget)
        :param param2: a QTreeWidgetItem (the one desactivated in main QTreeWidget)

        """

        debug = False


        if isinstance(param1, QTreeWidgetItem) and (isinstance(param2, QTreeWidgetItem) or param2 is None):    # signal from treeWidget_utils
            if debug: logging.getLogger("Lamia").debug('step 1 %s %s, %s', param1.text(0),param1 == self.qtreewidgetitem, param2)

            if param2 == self.qtreewidgetitem:  #the closed qtreewidgetitem
                if debug and param2 : logging.getLogger("Lamia").debug('step 2 desactivation %s ', param2.text(0))
                self.unloadWidgetInToolFrame()
                # self.postOnDesactivation()    TODO
                # if param2 == param1:      TODO
                #    self.lastidselected = None

            if param1 == self.qtreewidgetitem : #the openend qtreewidgetitem
                if debug: logging.getLogger("Lamia").debug('step 3 activation %s %s', param1.text(0), param2)
                # manage display in canvas
                # self._checkLayerVisibility() TODO
                self.updateToolbarOnToolFrameLoading()
                
                
                if self.choosertreewidget is not None :
                    if self.choosertreewidgetMUTIPLESELECTION  :
                        self.choosertreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
                    else:
                        self.choosertreewidget.setSelectionMode(QAbstractItemView.SingleSelection)
                
                # add child widget
                # self.loadChildWidgets() TODO

                # manage widget display
                if self.mainifacewidget is not None :
                    self.mainifacewidget.stackedWidget_main.setCurrentIndex(1)
                    if self.mainifacewidget.stackedWidget_main.widget(1).layout().count() > 0:
                        self.mainifacewidget.stackedWidget_main.widget(1).layout().itemAt(0).widget().setParent(None)
                    self.mainifacewidget.stackedWidget_main.widget(1).layout().addWidget(self)
                    """
                    if self.dbasetable is not None and not hasattr(self, 'POSTPROTOOLNAME'):
                        self.windowdialog.stackedWidget_main.setCurrentIndex(0)
                        if self.windowdialog.MaintabWidget.widget(0).layout().count() > 0:
                            self.windowdialog.MaintabWidget.widget(0).layout().itemAt(0).widget().setParent(None)
                        self.windowdialog.MaintabWidget.widget(0).layout().addWidget(self)
                        self.windowdialog.MaintabWidget.setCurrentIndex(0)
                    else:
                        self.windowdialog.stackedWidget_main.setCurrentIndex(1)
                        if self.windowdialog.stackedWidget_main.widget(1).layout().count() > 0:
                            self.windowdialog.stackedWidget_main.widget(1).layout().itemAt(0).widget().setParent(None)
                        self.windowdialog.stackedWidget_main.widget(1).layout().addWidget(self)
                    """
                # load feature in bottom qtreewidget
                """
                if (self.dbasetable is not None
                        or (self.dbasetablename is not None and os.path.isfile(self.dbasetablename))):
                    self.loadFeaturesinTreeWdg()
                    if self.comboBox_featurelist.count() > 0:
                        if self.parentWidget is None and self.lastidselected is not None :
                            idwidgetindex = self.comboBox_featurelist.findText(str(self.lastidselected))
                            if idwidgetindex >= 0 : #-1 not found
                                self.comboBox_featurelist.setCurrentIndex(idwidgetindex)
                            else:
                                self.comboBox_featurelist.currentIndexChanged.emit(0)
                        else:
                            self.comboBox_featurelist.currentIndexChanged.emit(0)
                        if self.linkedtreewidget is not None :
                            self.linkedtreewidget.invisibleRootItem().child(0).setExpanded(True)
                    else:
                        self.initFeatureProperties(None)

                elif hasattr(self, 'combotypeitems'):
                    self.combowdg.clear()
                    self.combowdg.addItems(self.combotypeitems)
                    self.combowdg.setVisible(True)
                    self.combowdg.currentIndexChanged.connect(self.combotypeitemsChanged)
                    self.combowdg.currentIndexChanged.emit(0)

                else:
                    self.linkedtreewidget.clear()
                """
                """
                #change active layer in canvas
                if qgis.utils.iface is not None and self.dbasetable is not None and self.dbasetable['showinqgis']:
                    qgis.utils.iface.setActiveLayer(self.dbasetable['layerqgis'])

                # Specific method
                self.postOnActivation()
                """

    def unloadWidgetInToolFrame(self):
        pass

    def populateChooserTreeWidget(self, populatefunction=None):
        self.disconnectChooserTreeWidget()
        if populatefunction:
            populatefunction()
        self.connectChooserTreeWidget()

    def connectChooserTreeWidget(self):
        self.choosertreewidget.itemSelectionChanged.connect(self.chooserTreeWidgetClcked)

    def disconnectChooserTreeWidget(self):
        try:
            self.choosertreewidget.itemSelectionChanged.disconnect(self.chooserTreeWidgetClcked)
        except:
            pass

    def chooserTreeWidgetClcked(self, selectedqtreewidgetitem):
        pass

    def updateToolbarOnToolFrameLoading(self):
        self.mainifacewidget.currenttoolwidget = self
        if self.mainifacewidget is not None:
            self.mainifacewidget.toolBarFormCreation.setEnabled(False)
            self.mainifacewidget.toolBarFormGeom.setEnabled(False)

