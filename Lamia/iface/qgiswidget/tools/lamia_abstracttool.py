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

from qgis.PyQt.QtWidgets import (QWidget, QTreeWidgetItem, QAbstractItemView, QVBoxLayout )
from qgis.PyQt import QtGui
import os, sys, logging

from ..subdialogs.lamia_linkage import LinkageDialog
from .subwidgets.lamia_numpad import NumPadDialog
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
                 parent=None,
                 **kwargs):
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
        self.setObjectName('lamiatoolwidget')
        self._loadUI()
        # ***** main var
        self.dbase = dbaseparser
        self.parentWidget = parentwidget
        self.mainifacewidget = mainifacewidget
        
        self.choosertreewidget = choosertreewidget

        # var used by tooltreewidget
        if self.mainifacewidget is not None:
            self.tooltreewidget = self.mainifacewidget.MaintreeWidget
            self.tooltreewidget.currentItemChanged.connect(self.toolTreeWidgetCurrentItemChanged)
            
        self.qtreewidgetitem = None     #the tool treewidgetitem in tooltreewidget



        self.toolwidget = None      #the widget loaded in self.toolwidgetmainlayout defined in inherited class
        self.toolwidgetmain = None  #the widget defined in inherited class - become self.toolwidget when loaded in layout

        # subwidgets
        self.numpaddialog = NumPadDialog()

    def _loadUI(self):
        #qwidgetconf
        toolwidgetmainlayout = QVBoxLayout()
        toolwidgetmainlayout.setMargin(0)
        self.setLayout(toolwidgetmainlayout)
        #uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_observation_tool_ui_CD41.ui')
        #uic.loadUi(uipath, self)

    def ___________________widgetBehaviourWithToolTreeWidget(self):
        pass

    def changeInterfaceMode(self):
        self.manageLoadingInToolTreeWidget()
        self.manageWidgetToLoadInMainLayout()

    def manageLoadingInToolTreeWidget(self):
        if self.mainifacewidget.interfacemode == 0:
            if  hasattr(self, 'PREPROTOOLNAME') and self.PREPROTOOLNAME  and self.LOADFIRST:
                self.loadWidgetinToolTree()
            else:
                self.unloadWidgetinToolTree()
        elif self.mainifacewidget.interfacemode == 1:
            if hasattr(self, 'PREPROTOOLNAME') and  self.PREPROTOOLNAME:
                self.loadWidgetinToolTree()
            else:
                self.unloadWidgetinToolTree()
        elif self.mainifacewidget.interfacemode == 4:
            if hasattr(self, 'POSTPROTOOLNAME') and  self.POSTPROTOOLNAME:
                self.loadWidgetinToolTree()
            else:
                self.unloadWidgetinToolTree()

    def manageWidgetToLoadInMainLayout(self):
        if self.toolwidgetmain is None:
            self.initMainToolWidget()                                   
        if self.toolwidgetmain is not None:    
            #former self.userwdg = self.userwdgfield
            self.toolwidget = self.toolwidgetmain  
        if self.layout().count() > 0:
            #self.frametoolwidg.layout().itemAt(0).widget().setVisible(False)
            self.layout().itemAt(0).widget().setParent(None)
        self.layout().addWidget(self.toolwidget)


    def initMainToolWidget(self):
        pass

    def loadWidgetinToolTree(self):
        """
        Called on the widget creation in windowsdialog
        load the widget in the main stacked widget
        call onActivationRaw when qtreewidgetitem is clicked in MaintreeWidget
        """
        # add qtreewidget item in MaintreeWidget
        
        if self.mainifacewidget is not None and self.parentWidget is None:
            
            arb = [self.tooltreewidgetCAT, self.tooltreewidgetSUBCAT]
            if hasattr(self, 'qtreewidgetitem') and self.qtreewidgetitem is None:
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

    #def loadWidgetInToolFrame(self, param1, param2=None):
    def toolTreeWidgetCurrentItemChanged(self, param1, param2=None):
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

        #before all
        

        if isinstance(param1, QTreeWidgetItem) and (isinstance(param2, QTreeWidgetItem) or param2 is None):    # signal from treeWidget_utils
            if debug: logging.getLogger("Lamia").debug('step 1 %s %s, %s', param1.text(0),param1 == self.qtreewidgetitem, param2)

            if param2 == self.qtreewidgetitem:  #the closed qtreewidgetitem
                if debug and param2 : logging.getLogger("Lamia").debug('step 2 desactivation %s ', param2.text(0))
                self.updateToolbarOnToolFrameUnloading()
                self.unloadWidgetInToolFrame()

                # self.postOnDesactivation()    TODO
                # if param2 == param1:      TODO
                #    self.lastidselected = None

            if param1 == self.qtreewidgetitem : #the openend qtreewidgetitem
                if debug: logging.getLogger("Lamia").debug('step 3 activation %s %s', param1.text(0), param2)
                # manage display in canvas
                # self._checkLayerVisibility() TODO
                self.mainifacewidget.qgiscanvas.createorresetRubberband()
                self.mainifacewidget.currenttoolwidget = self
                self.updateToolbarOnToolFrameLoading()
                self.activateChooserTreeWidget()
                self._displayWidget()
                self.postToolTreeWidgetCurrentItemChanged()
                

    def unloadWidgetInToolFrame(self):
        pass

    def updateToolbarOnToolFrameLoading(self):
        
        if self.mainifacewidget is not None:
            self.mainifacewidget.lamiatoolBarFormCreation.setEnabled(False)
            self.mainifacewidget.lamiatoolBarFormGeom.setEnabled(False)

    def updateToolbarOnToolFrameUnloading(self):
        pass

    def _displayWidget(self):
        # manage widget display
        if self.mainifacewidget is not None :
            self.mainifacewidget.stackedWidget_main.setCurrentIndex(1)
            if self.mainifacewidget.stackedWidget_main.widget(1).layout().count() > 0:
                currentwdg = self.mainifacewidget.stackedWidget_main.widget(1).layout().itemAt(0).widget()
                self.mainifacewidget.stackedWidget_main.widget(1).layout().removeWidget(currentwdg)
                currentwdg.setVisible(False)
                # self.mainifacewidget.stackedWidget_main.widget(1).layout().itemAt(0).widget().setParent(None)


            # if not self in self.mainifacewidget.stackedWidget_main.widget(1).layout():
            self.mainifacewidget.stackedWidget_main.widget(1).layout().addWidget(self)
            self.setVisible(True)

    def activateChooserTreeWidget(self, **kwargs):
        #choosertreewdg things
        if self.choosertreewidget is not None and hasattr(self.choosertreewidget,'treewidget'):
            if self.choosertreewidgetMUTIPLESELECTION  :
                self.choosertreewidget.treewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
            else:
                self.choosertreewidget.treewidget.setSelectionMode(QAbstractItemView.SingleSelection)
            if self.mainifacewidget.currentchoosertreewidget is not None:
                self.mainifacewidget.currentchoosertreewidget.disconnectTreewidget()
            self.mainifacewidget.currentchoosertreewidget = self.choosertreewidget
            self.choosertreewidget.onActivation(**kwargs)
        else:
            if self.mainifacewidget is not None:
                self.mainifacewidget.ElemtreeWidget.clear()

    def postToolTreeWidgetCurrentItemChanged(self):
        pass

    def _____________________subwidgets(self):
        pass

    def showNumPad(self, finalwdg):
        self.numpaddialog.exec_()
        number = self.numpaddialog.dialogIsFinished()
        if number:
            finalwdg.setValue(number)


    def showImageinLabelWidget(self,wdg,savedfile):
        """
        Show the image file in the text widget
        Manage thumbnail image

        :param wdg: the text widget
        :param savedfile: the image file

        """
        filetoshow = self.dbase.completePathOfFile(savedfile)
        possiblethumbnail,ext = os.path.splitext(filetoshow)
        if os.path.isfile(possiblethumbnail + "_thumbnail.png"):
            filetoshow = possiblethumbnail + "_thumbnail.png"

        if os.path.isfile(filetoshow):
            wdg.clear()
            wdg.setPixmap(filetoshow)
        else:
            wdg.clear()
            wdg.setText('Image non trouvee')