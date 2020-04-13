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
"""
try:
    from qgis.PyQt.QtGui import (QWidget, QTreeWidgetItem, QMessageBox, QFileDialog, QTableWidget,
                                 QHeaderView, QComboBox, QSpinBox, QCheckBox, QPushButton, QDateEdit,QDateTimeEdit, QTextEdit,
                                 QDoubleSpinBox, QDialog, QVBoxLayout, QTreeWidget, QLineEdit, QCheckBox,
                                 QLabel, QMessageBox, QTextBrowser, QTableWidgetItem,QApplication,QToolButton, QAbstractItemView)
except ImportError:
"""
from qgis.PyQt.QtWidgets import (QWidget, QTreeWidgetItem, QMessageBox, QFileDialog, QTableWidget,
                                    QHeaderView, QComboBox, QSpinBox,QCheckBox, QPushButton, QDateEdit,QDateTimeEdit, QTextEdit,
                                    QDoubleSpinBox, QDialog, QVBoxLayout, QTreeWidget, QLineEdit, QCheckBox, QFrame,
                                    QLabel, QMessageBox, QTextBrowser, QTableWidgetItem,QApplication,QToolButton, QAbstractItemView)
import os, sys, logging, pprint, shutil, datetime, time

from ..subdialogs.lamia_linkage import LinkageDialog
# from ..maptool.mapTools import mapToolCapture TODO
from .lamia_abstracttool import AbstractLamiaTool
from .lamia_abstractformutils import FormToolUtils
from .choosertreewidget.fullidchoosertreewidget import FullIDChooserTreeWidget



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

    def __init__(self,                  
                 dbaseparser=None, 
                 mainifacewidget=None, 
                 choosertreewidget=None, 
                 parentwidget=None, 
                 parent=None):
        """
        Initialisation of AbstractLamiaTool

        :param dbase:              The DBaseParser class
        :param dialog:             The LamiaWindowWidget class
        :param linkedtreewidget:   The QTreeWidget Wwhee the ids appears
        :param gpsutil:            the GpsUtil class for maning GPS connexion
        :param parentwidget:       the parentWidget class, in case of use in prepro
        :param parent:             the Qt parent
        """
        super(AbstractLamiaFormTool, self).__init__(dbaseparser=dbaseparser, 
                                                    mainifacewidget=mainifacewidget, 
                                                    choosertreewidget=choosertreewidget, 
                                                    parentwidget=parentwidget, 
                                                    parent=parent)
        self.installEventFilter(self) 
        # utils class
        self.formutils = FormToolUtils(self)
        # choosertreewdg
        self.choosertreewidget = FullIDChooserTreeWidget(toolwidget=self,
                                                         dbaseparser = self.dbase,
                                                         mainifacewidget = self.mainifacewidget)


        # var for widgets loaded in self.toolwidgetmainlayout

        #layoutconf
        #self.toolwidgetmainlayout = QVBoxLayout()
        #self.toolwidgetmainlayout.setMargin(0)
        #self.setLayout(self.toolwidgetmainlayout)


        self.toolwidget = None          #the widget loaded in self.toolwidgetmainlayout
        self.toolwidgetmain = None      #the widget defined in inherited class - become self.toolwidget when loaded in layout
        self.toolwidgetadvanced = None  #the widget defined in inherited class - become self.toolwidget when loaded in layout
        self.formtoolwidgetconfdict = None       #dict used to link dbase column name to qtwidget objectname 
        self.formtoolwidgetconfdictmain = None   #dict for toolwidgetmain
        self.formtoolwidgetconfdictadvanced = None   #dict for toolwidgetadvanced
        self.dbasechildwdg = []
        self.dbasechildwdgfield = []
        self.dbasechildwdgdesktop = []


        # behaviour var
        self.currentFeaturePK = None    # the pk of selected feature
        self.tempgeometry = None        #the geometry edited while defining new geom
        self.activatesubwidgetchangelistener=False
        self.lastselectedpk = None




        if False:
            self._init_loadWidgetDependentResolution()


            # ***************************************************************
            # ******************   Variables def ****************************
            # ***************************************************************

            # ***** Data base var
            #  the dbaseparser
            self.dbase = dbase
            # TODO
            # the gpsutil
            self.gpsutil = gpsutil
            #  the current widget feature selected in self.linkedtreewidget
            self.currentFeature = None
            self.currentFeaturePK = None
            self.beforesavingFeature = None
            #  the parent widget if exists
            self.parentWidget = parentwidget
            #  ids to load
            self.idstoload = None
            
            self.linkagespec = None
            # self.linkageids = None
            # data for datas in config file
            self.dbasefiledata = None

            # ***** Ui var
            #  Name used for rool tree in main qtreewidget - must be implemented
            self.CAT = None
            #  Name used for child tree in main qtreewidget - must be implemented
            self.NAME = None
            #  Table name linked with widget
            self.dbasetablename = None
            #  iconpath -  can be implemented
            self.iconpath = None
            # enable multipleselection in ElemtreeWidget
            self.multipleselection = False
            #  Main window widget
            self.windowdialog = None
            if dialog is not None:
                self.windowdialog = dialog
            elif self.parentWidget is not None and self.parentWidget.windowdialog is not None:
                self.windowdialog = self.parentWidget.windowdialog
            #  MaintreeWidget qtreewidgetitem
            self.qtreewidgetitem = None
            #  the qtreewidget within the features are displayed
            self.linkedtreewidget = linkedtreewidget
            # list of feature in linkedtreewidget : [...[id,QTreeWidgetItem([str(id)])] ...]
            self.treefeatlist = None
            #  the child widgets
            #whildwdg change
            self.dbasechildwdg = []
            self.dbasechildwdgfield = None
            self.dbasechildwdgdesktop = None
            # user widget
            self.userwdgfield = None
            self.linkuserwdgfield = None
            self.userwdgdesktop = None
            self.linkuserwdgdesktop = None
            self.userwdg = None             #current userwdg
            self.linkuserwdg = None             #current linkuserwdg
            # wile saving new feature
            self.savingnewfeature = False
            self.savingnewfeatureVersion = False
            #lastidselected
            self.lastidselected = None
            # linked disorder
            #self.linkeddisorder = None
            # self.linkeddisorder = {'specificfield': 'OUH',
            #                         'groupedesordre': 'NOD'}
            # linked geom : [..[tablename,linkfield of tablename],...]
            self.linkedgeom = None
            self.dicttablefieldtoinit = {}

            #  tablewidget - expert widget
            self.tableWidget = QTableWidget()
            self.tableWidget.setColumnCount(4)
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            self.tableWidget.setColumnWidth(2, 48)
            self.tableWidget.setColumnWidth(3, 48)

            # header.setResizeMode(2, QHeaderView.ResizeToContents)
            # header.setResizeMode(3, QHeaderView.ResizeToContents)
            self.newentrytext = 'Nouvelle entree'
            # user widget
            self.userwdg = None
            #  field name to be displayd in qtreewidget
            self.qtreewidgetfields = []
            #  when gps info need to be displayed
            self.gpswidget = None

            # self.dbaseressourcesfield = None
            self.mtool = None
            self.rubberBandBlink = None
            self.capturetype = None

            # ***** QGis var
            #  qgis map canvas
            if self.windowdialog is not None:
                self.canvas = self.windowdialog.canvas
            else:
                self.canvas = None
            # layer shown in cnvas or not
            self.layerdisplayed = False
            # capture mode
            self.PointENABLED = False
            self.LineENABLED = False
            self.PolygonENABLED = False
            self.magicfunctionENABLED = False
            # ruberband
            self.rubberBand = None
            # captured geoemtry
            self.tempgeometry = None
            # the dbasetable - loaded once a dbase is loaded in DBaseParser
            self.dbasetable = None
            # use for picking
            if self.canvas is not None:
                self.pointEmitter = qgis.gui.QgsMapToolEmitPoint(self.canvas)   # maptoolused for picking
            self.currentmaptool = None      # qgsmaptoolcapture used for capturing
            self.visualmode = [0, 1, 2]
            #for coping
            self.deepcopy = []
            #for lid choosers
            self.lamiawidgets = []

            #for copy purpose
            self.templinkuserwdg = None

            # *******************************************************
            # raw connection
            # *******************************************************
            # load tools - must be kept in this order
            # if debugtime: logging.getLogger('Lamia').debug('before initTool %s %.3f',self.dbasetablename, self.dbase.getTimeNow()  - timestart)
            self.initTool()
            # if debugtime: logging.getLogger('Lamia').debug('After initTool %s %.3f',self.dbasetablename, self.dbase.getTimeNow()  - timestart)

            # *******************************************************
            # Post inittool things

            if self.dbasetablename is not None :
                self.pushButton_savefeature.clicked.connect(self.saveFeature)
                self.pushButton_addFeature.clicked.connect(self.addFeature)
                self.pushButton_delFeature.clicked.connect(self.deleteFeature)
                self.pushButton_deselect.clicked.connect(self.deselectFeature)

                self.pushButton_copy.clicked.connect(self.copyAtributes)
                self.pushButton_paste.clicked.connect(self.pasteAtributes)

                self.pushButton_impression.clicked.connect(self.printWidget)

                if self.dbasetablename in self.dbase.dbasetables.keys():
                    self.dbasetable = self.dbase.dbasetables[self.dbasetablename]

            if len(self.deepcopy) == 0 :
                self.frame_deepcopy.setVisible(False)
            else:
                self.pushButton_deepcopy.clicked.connect(self.deepCopy)
                self.pushButton_deepcopyselect.clicked.connect(self.deepCopy)

            #work even with postpro tool
            self.changePropertiesWidget()
            # connect signals of inherited widget
            if self.windowdialog is not None:
                self.windowdialog.MaintreeWidget.currentItemChanged.connect(self.onActivationRaw)

            if self.dbasetablename is not None:
                self.initWidgets()
    
    def _________________widgetinitialization(self):
        pass

    def _loadUI(self):
        pass
        uipath = os.path.join(os.path.dirname(__file__), 'lamia_abstractformtool.ui')
        uic.loadUi(uipath, self)

        #self.titlelabel = QLabel('temp')
        ##self.titlelabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        #self.titlelabel.setAlignment(QtCore.Qt.AlignVCenter)
        #self.titlelabel.setFrameShape(QFrame.Panel)
        ##self.titlelabel.setFrameShadow(QFrame.Sunken)
        #self.titlelabel.setLineWidth(2)
        #self.frametoolwidgindicator.layout().addWidget(self.titlelabel)
        #self.frametoolwidgindicator.layout().update()

    def manageWidgetToLoadInMainLayout(self):
        if self.mainifacewidget.interfacemode in [0,4]:
            if self.toolwidgetmain is None: #first loading
                #former initFieldUI
                self.initMainToolWidget()
                if self.toolwidgetmain:
                    self.toolwidget = self.toolwidgetmain 
                    self.formtoolwidgetconfdict = self.formtoolwidgetconfdictmain
                    self.formutils.initWidgetBehaviour()  
                    self.formutils.connectSubWidgetModifications()                           
            if self.toolwidgetmain is not None:    #non first loading
                #former self.userwdg = self.userwdgfield
                self.toolwidget = self.toolwidgetmain     
                #former self.linkuserwdg = self.linkuserwdgfield              
                self.formtoolwidgetconfdict = self.formtoolwidgetconfdictmain
                self.dbasechildwdg = self.dbasechildwdgfield


        elif self.mainifacewidget.interfacemode == 1:
            if self.toolwidgetadvanced is None: #first loading
                # former self.initDesktopUI()
                self.initAdvancedToolWidget()
                if self.toolwidgetadvanced:
                    self.toolwidget = self.toolwidgetadvanced
                    self.formtoolwidgetconfdict = self.formtoolwidgetconfdictadvanced
                    self.formutils.initWidgetBehaviour(self.toolwidgetadvanced) 
            if self.toolwidgetadvanced is not None:    #non first loading
                # former self.userwdg = self.userwdgdesktop
                self.toolwidget = self.toolwidgetadvanced
                # former self.linkuserwdg = self.linkuserwdgdesktop
                self.formtoolwidgetconfdict = self.formtoolwidgetconfdictadvanced
                self.dbasechildwdg = self.dbasechildwdgdesktop   
            else:
                self.toolwidget = self.toolwidgetmain
                self.formtoolwidgetconfdict = self.formtoolwidgetconfdictmain
                self.dbasechildwdg = self.dbasechildwdgfield
        
        #var1
        if False:
            parentitem = self.treeWidgetmain.invisibleRootItem()
            if len(self.dbasechildwdg) == 0 :
                self.toolBoxmain.removeItem(1)
            if self.parentWidget is not None:
                parentwdg=self
                parentlist=[]
                while parentwdg is not None:
                    parentlist.append(parentwdg.DBASETABLENAME)
                    parenttoolbox = parentwdg.toolBoxmain
                    parentwdgnotnone = parentwdg
                    parentwdg = parentwdg.parentWidget
                    
                name = '/'.join(parentlist[::-1])
                name = '    '*len(parentlist) + name

                parentitem = self.parentWidget.newitem
                self.newitem = QTreeWidgetItem([self.DBASETABLENAME])
                parentitem.addChildren([self.newitem ])
                parentwdgnotnone.treeWidgetmain.setItemWidget(self.newitem , 1, self.toolwidget)
            else:
                parentitem = self.treeWidgetmain.invisibleRootItem()
                self.newitem = QTreeWidgetItem([self.DBASETABLENAME])
                parentitem.addChildren([self.newitem ])
                self.treeWidgetmain.setItemWidget(self.newitem , 1, self.toolwidget)
        #var2
        if False:
            self.treeWidgetmain.setVisible(False)
            self.frametoolwidg.layout().addWidget(self.toolwidget)
            if len(self.dbasechildwdg) == 0 :
                #self.toolBoxchildwdg.setParent(None)
                self.toolBoxmain.removeItem(1)
            if self.parentWidget is not None:
                # print('additem {} in {}'.format(self.DBASETABLENAME,self.parentWidget.DBASETABLENAME ))
                # self.toolBoxmain.widget(0).setParent(None)
                #index = self.parentWidget.toolBoxchildwdg.addItem(self,self.DBASETABLENAME)
                parentwdg=self
                parentlist=[]
                while parentwdg is not None:
                    parentlist.append(parentwdg.tooltreewidgetSUBCAT)
                    parenttoolbox = parentwdg.toolBoxmain
                    parentwdgnotnone = parentwdg
                    parentwdg = parentwdg.parentWidget
                    
                name = '/'.join(parentlist[::-1])
                name = '    '*len(parentlist) + name

                index = parenttoolbox.addItem(self.frametoolwidg,name)
                #self.toolBoxmain.widget(0).setParent(self.parentWidget.toolBoxchildwdg.widget(index))
                #self.parentWidget.toolBoxchildwdg.insertItem(-1,self.frametoolwidg,self.DBASETABLENAME)
            else:
                self.frame.setParent(None)
        self.tabWidgetmain.tabBar().setObjectName('lamia_tabbar')
        self.tabWidget.tabBar().setObjectName('lamia_tabbar')
        
        self._defineQTabWidgetTabBehaviour()
        #var3
        if False:
            self.frametoolwidg.layout().addWidget(self.toolwidget)
            self.tabWidgetmain.setTabText(0, self.tooltreewidgetSUBCAT)

            if self.parentWidget is not None:
                parentwdg=self
                parentlist=[]
                parenttab = self.parentWidget.tabWidget
                indexinserted = parenttab.addTab(self.tabWidgetmain.widget(0),
                                                  QtGui.QIcon(self.tooltreewidgetICONPATH),
                                                   self.tooltreewidgetSUBCAT)

                def selectFirstTab(idx):
                    if idx == indexinserted:
                        self.tabWidget.setCurrentIndex(0)
                        self.widgetClicked(event=None)

                parenttab.tabBarClicked.connect(lambda idx : selectFirstTab(idx))
                parenttab.tabBarClicked.connect(lambda idx : selectFirstTab(idx))
            else:
                self.frame.setParent(None)
                self.tabWidgetmain.tabBarClicked.connect(lambda idx : self.tabWidget.setCurrentIndex(0))

            self.tabWidgetmain.setTabIcon(0, QtGui.QIcon(self.tooltreewidgetICONPATH))
            self.tabWidget.setTabIcon(0, QtGui.QIcon(self.tooltreewidgetICONPATH))

            self.tabWidget.tabBarClicked.connect(lambda idx : self.widgetClicked)

        if False:
            #if self.parentWidget is None:
            #self.frametoolwidg.layout().insertWidget(1,self.toolwidget)
            #if self.parentWidget is None:
            #self.frametoolwidg.layout().addWidget(self.toolwidget)
            parentitem = self.treeWidgetmain.invisibleRootItem()

            #self.treeWidgetmain.
            #self.toolwidgetmainlayout.addWidget(self.toolwidget)
            #self.frametoolwidg.layout().update()
            if len(self.dbasechildwdg) == 0 :
                #self.toolBoxchildwdg.setParent(None)
                self.toolBoxmain.removeItem(1)
            
            if self.parentWidget is not None:
                # print('additem {} in {}'.format(self.DBASETABLENAME,self.parentWidget.DBASETABLENAME ))
                # self.toolBoxmain.widget(0).setParent(None)
                #index = self.parentWidget.toolBoxchildwdg.addItem(self,self.DBASETABLENAME)
                parentwdg=self
                parentlist=[]
                while parentwdg is not None:
                    parentlist.append(parentwdg.DBASETABLENAME)
                    parenttoolbox = parentwdg.toolBoxmain
                    parentwdgnotnone = parentwdg
                    parentwdg = parentwdg.parentWidget
                    
                name = '/'.join(parentlist[::-1])
                name = '    '*len(parentlist) + name
                #self.toolBoxmain
                #index = parenttoolbox.addItem(self.frametoolwidg,name)

                parentitem = self.parentWidget.newitem
                self.newitem = QTreeWidgetItem([self.DBASETABLENAME])
                parentitem.addChildren([self.newitem ])
                #treeWidget->setItemWidget(childItem1, 0, childButton1)
                parentwdgnotnone.treeWidgetmain.setItemWidget(self.newitem , 1, self.toolwidget)

                # print('**', index)
                #self.toolBoxmain.widget(0).setParent(self.parentWidget.toolBoxchildwdg.widget(index))
                #self.parentWidget.toolBoxchildwdg.insertItem(-1,self.frametoolwidg,self.DBASETABLENAME)
                #if True and self.parentWidget.toolBoxmain.widget(0).objectName() == 'page_to_remove':
                #    self.parentWidget.toolBoxchildwdg.removeItem(0)


                """
                if self.parentWidget.framechildwdg.layout().count()==0:
                    self.toolBoxmain.setParent(self.parentWidget.framechildwdg)
                else:
                    self.parentWidget.toolBoxmain.addItem(self.toolBoxmain.widget(0))
                """
            else:
                #self.frame.setParent(None)
                parentitem = self.treeWidgetmain.invisibleRootItem()
            
                self.newitem = QTreeWidgetItem([self.DBASETABLENAME])
                parentitem.addChildren([self.newitem ])
                #treeWidget->setItemWidget(childItem1, 0, childButton1)
                self.treeWidgetmain.setItemWidget(self.newitem , 1, self.toolwidget)


        self.toolwidget.mouseReleaseEvent=self.widgetClicked

        #propagate to childwidgets
        try:
            self.currentFeatureChanged.disconnect()
        except TypeError:
            pass
            #print('error disconnect currentFeatureChanged')

        for childwdg in self.dbasechildwdg:
            childwdg.manageWidgetToLoadInMainLayout()
            self.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)

    def _defineQTabWidgetTabBehaviour(self):
        self.frametoolwidg.layout().addWidget(self.toolwidget)
        self.tabWidgetmain.setTabText(0, self.tooltreewidgetSUBCAT)
        self.tabWidgetmain.setTabIcon(0, QtGui.QIcon(self.tooltreewidgetICONPATH))
        self.tabWidget.setTabIcon(0, QtGui.QIcon(self.tooltreewidgetICONPATH))

        if self.parentWidget is not None:
            parentwdg=self
            parentlist=[]
            parenttab = self.parentWidget.tabWidget
            indexinserted = parenttab.addTab(self.tabWidgetmain.widget(0),
                                                QtGui.QIcon(self.tooltreewidgetICONPATH),
                                                self.tooltreewidgetSUBCAT)

            def selectFirstTab(idx):
                if idx == indexinserted:
                    self.tabWidget.setCurrentIndex(0)
                    self.widgetClicked(event=None)

            #parenttab.tabBarClicked.connect(lambda idx : selectFirstTab(idx))
            parenttab.tabBarClicked.connect(lambda idx : selectFirstTab(idx))
        else:
            #self.frame.setParent(None)
            self.tabWidgetmain.tabBarClicked.connect(lambda idx : self.tabWidget.setCurrentIndex(0))
            self.tabWidgetmain.tabBarClicked.connect(lambda idx: self.toolwidget.mouseReleaseEvent(None))

        def onlyFirstTabClicked(idx):
            if idx == 0:
                self.widgetClicked()

        self.tabWidget.tabBarClicked.connect(lambda idx : onlyFirstTabClicked(idx))

    def eventFilter(self, obj, event):  #to work also on disabled widget
        if event.type() == QtCore.QEvent.MouseButtonRelease and event.button() == 1:
            # print('eventFilter')
            self.toolwidget.mouseReleaseEvent(event)
            #self._click.emit(self)
            return True

        return QWidget.eventFilter(self, obj, event)

    def widgetClicked(self, event=None, **kwargs):
        debug = False
        # print('*******',self.DBASETABLENAME, kwargs)
        self.mainifacewidget.currenttoolwidget = self

        parentwidget = self
        lastparentwdgpk = None
        while parentwidget.parentWidget is not None:
            # print('disable ', parentwidget.parentWidget.DBASETABLENAME)
            #self._setWidgetEnabled(False, parentwidget.parentWidget)
            lastparentwdgpk = parentwidget.parentWidget.currentFeaturePK
            parentwidget = parentwidget.parentWidget


        if ((self.parentWidget is not None and lastparentwdgpk is not None)
                or self.parentWidget is None):
            #self._setWidgetEnabled(True, self)
            if self.mainifacewidget.currentchoosertreewidget:
                self.mainifacewidget.currentchoosertreewidget.disconnectTreewidget()
            self.mainifacewidget.currentchoosertreewidget = self.choosertreewidget
            self.mainifacewidget.currentchoosertreewidget.onActivation()
            #res = 
        else:
            pass
            #self._setWidgetEnabled(False, self)
        lastselectedid = None
        if self.lastselectedpk is not None:
            lastselectedid = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                                      'id_' + self.DBASETABLENAME.lower(),
                                                      self.lastselectedpk)
        if debug :
            logging.getLogger("Lamia_unittest").debug('%s - last sel pk : %s - lenids : %i',
                                                        self.DBASETABLENAME,
                                                        self.lastselectedpk,
                                                        len(self.choosertreewidget.ids) )

        if (self.lastselectedpk is not None and len(self.choosertreewidget.ids)>0 
                and lastselectedid in self.choosertreewidget.ids.id.values):
            self.selectFeature(pk=self.lastselectedpk)
            self.choosertreewidget.selectItemfromPK(self.lastselectedpk)
        else:
            if len(self.choosertreewidget.ids)>0:
                pk = self.choosertreewidget.ids['pk'].values[0]
                self.selectFeature(pk=pk)
                self.choosertreewidget.selectItemfromPK(pk)
            else:
                self.currentFeaturePK = None
                self.updateFormTitle(pk=None, disabletitle=True)
                self.frametoolwidg.setEnabled(False)



    """
    def _disableChildWidgets(self,childwdgs):
        if hasattr(self.toolwidget,'framechildtoolwidg'):
            print('disab')
            self.toolwidget.framechildtoolwidg.setEnabled(False)
        for childwdg in childwdgs:
            self._disableChildWidgets(childwdg.dbasechildwdg)
            self._setWidgetEnabled(False,childwdg)
            childwdg.updateFormTitleBackground(disabletitle=True)
            #childwdg.toolwidget.setEnabled(False)

    def _setWidgetEnabled(self, boolstate, wdg):
        framenametoenable = 'frametoolwidg'
        if boolstate:
            wdg.toolwidget.setEnabled(True)
            #wdg.toolwidget
            if hasattr(wdg.toolwidget,framenametoenable):
                wdg.toolwidget.frametoolwidg.setEnabled(True)
                wdg.toolwidget.frametoolwidg.setVisible(True)
        else:
            wdg.updateFormTitleBackground(disabletitle=True)
            if hasattr(wdg.toolwidget,framenametoenable):
                wdg.toolwidget.frametoolwidg.setEnabled(False)
                wdg.toolwidget.frametoolwidg.setVisible(False)
                if hasattr(wdg.toolwidget,'framechildtoolwidg'):
                    wdg.toolwidget.framechildtoolwidg.setEnabled(True)
            else:
                wdg.toolwidget.setEnabled(False)
    """


    def loadChildFeatureinWidget(self):
        debug = False
        #print('loadChildFeatureinWidget', self.DBASETABLENAME)
        self.choosertreewidget.loadIds()
        if debug :
            logging.getLogger("Lamia_unittest").debug('%s - pk:%s / %s \n %s',
                                                        self.parentWidget.DBASETABLENAME,
                                                        self.parentWidget.currentFeaturePK,
                                                        self.DBASETABLENAME,
                                                        self.choosertreewidget.ids )
        if len(self.choosertreewidget.ids)==0:
            self.selectFeature(pk=None, disabletitle=True)
        else:
            self.selectFeature(pk=self.choosertreewidget.ids['pk'][0])


        if False:
            res = self.choosertreewidget.loadIds()
            # print('***', self.DBASETABLENAME, res)
            if len(res)==0:
                self.selectFeature(disabletitle=True)
                #self.currentFeaturePK = None
                #self.updateFormTitle(disabletitle=True)
            else:
                sql = "SELECT pk_{} FROM {}_now WHERE id_{} = {}".format(self.DBASETABLENAME.lower(),
                                                                    self.DBASETABLENAME,
                                                                    self.DBASETABLENAME.lower(),
                                                                    res[0][0] )
                sql = self.dbase.sqlNow(sql)
                pk = self.dbase.query(sql)[0][0]
                self.selectFeature(pk=pk)
                #self.currentFeaturePK = pk
                #self.updateFormTitle()

        if False:
            minsql = "SELECT min(pk_{}) FROM {}".format(self.DBASETABLENAME.lower(),
                                                        self.DBASETABLENAME)
            minpk = self.dbase.query(minsql)
            if minpk:
                minpk =  minpk[0][0]
                self.selectFeature(pk=minpk)




    def initMainToolWidget(self):
        pass
            
    def initAdvancedToolWidget(self):
        pass

    def postToolTreeWidgetCurrentItemChanged(self):
        if self.lastselectedpk is not None:
            self.setEnabled(True)
            self.selectFeature(pk=self.lastselectedpk)
        elif len(self.choosertreewidget.ids)>0:
            self.setEnabled(True)
            self.selectFeature(pk=self.choosertreewidget.ids['pk'].values[0])
        else:
            self.setEnabled(False)



    def updateToolbarOnToolFrameLoading(self):
        if self.mainifacewidget is not None:
            self.mainifacewidget.toolBarFormCreation.setEnabled(True)
            self.mainifacewidget.toolBarFormGeom.setEnabled(True)

        
    def subwidgetChanged(self):
        if self.activatesubwidgetchangelistener:
            self.updateFormTitleBackground(subwidgethaschanged=True)




    #*************************************************************
    # toolbar
    #*************************************************************

    def ____________________________________ToolBarActions(self):
        pass

    def selectFeature(self, **kwargs):
        debug = False
        self.setEnabled(True)
        self.activatesubwidgetchangelistener = False
        if debug: logging.getLogger("Lamia_unittest").debug('kwargs %s', str(kwargs))
        self.currentFeaturePK = kwargs.get('pk', None)
        #rubberband actions
        self._manageRubberbandOnSelectFeature(self.currentFeaturePK)
        #remember feature pk
        if self.currentFeaturePK:
            self.lastselectedpk = self.currentFeaturePK
        #layer action
        if self.parentWidget is None and self.DBASETABLENAME is not None:
            self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME]['layer'].removeSelection()
            # self.dbasetable['layer'].removeSelection()
        #form title action
        self.updateFormTitle(**kwargs)
        #load values in form
        resultdict = self.formutils.getDictValuesForWidget(featurepk=self.currentFeaturePK)
        if debug: logging.getLogger("Lamia_unittest").debug('resultdict %s', str(resultdict))
        self.formutils.applyResultDict(resultdict)
        #end actions
        self.postSelectFeature()
        if self.currentFeaturePK is not None:   #activate listener only with existing feat
            self.activatesubwidgetchangelistener = True
        self.currentFeatureChanged.emit()

    def toolbarNew(self):
        self.selectFeature()

    def toolbarUndo(self):
        self.selectFeature(pk=self.currentFeaturePK)

    def toolbarSave(self):
        self.formutils.saveFeature(featurepk=self.currentFeaturePK)

    def toolbarGeom(self):
        sender = self.mainifacewidget.sender()
        if sender is not None:
            logging.getLogger("Lamia_unittest").debug('toolbarGeom %s', str(sender.objectName()))
        if sender is not None and sender.objectName() != 'pushButton_rajoutPoint':
            listpointinitialgeometry = []
        if 'point' in sender.objectName():
            capturetype = 0
        elif 'line' in sender.objectName():
            capturetype = 1
        elif 'polygon' in sender.objectName():
            capturetype = 2

        self.mainifacewidget.qgiscanvas.captureGeometry(capturetype=capturetype,
                                                        listpointinitialgeometry=listpointinitialgeometry,
                                                        fctonstopcapture=self.setTempGeometry)

    def toolbarDelete(self):

        message = "Supprimer completement l'element (yes) ou l'archiver (no) ? "
        reply = QMessageBox.question(self, "Su",
                                           message,
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.formutils.deleteFeature()

        elif reply == QMessageBox.No:
            self.formutils.archiveFeature()

        self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME]['layerqgis'].triggerRepaint()
        #self.canvas.refresh()
        #self.loadChildFeatureinWidget()

    def ____________________________________ToolBarActionsFunctions(self):
        pass

    def updateFormTitle(self, **kwargs):
        #self.toolBoxmain

        if self.currentFeaturePK:
            featureid = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                                'id_' + self.DBASETABLENAME.lower(),
                                                    self.currentFeaturePK)
            for i in range(1,self.tabWidget.count()):
                self.tabWidget.setTabEnabled(i, True)
        else:
            featureid = 'New'
            for i in range(1,self.tabWidget.count()):
                self.tabWidget.setTabEnabled(i, False)

        if False:
            parentwidget=self
            while parentwidget.parentWidget is not None:
                parentwidget = parentwidget.parentWidget

            toolbox = parentwidget.toolBoxmain
            finalpageindex=0
            for pageindex in range(toolbox.count()):
                print('po',pageindex,toolbox.widget(pageindex).parent().__dict__)
                if toolbox.widget(pageindex) == self.frametoolwidg:
                    finalpageindex == pageindex
                    break
            toolbox.setItemText(finalpageindex,'{}({})'.format(self.DBASETABLENAME,
                                                        featureid) )
            #self.toolBoxmain.setItemText(0,'{}({})'.format(self.DBASETABLENAME,
            #                                              featureid) )
            #self.titlelabel.setText('{}({})'.format(self.DBASETABLENAME,
            #                                              featureid) )
        self.updateFormTitleBackground(**kwargs)

    
    def updateFormTitleBackground(self, subwidgethaschanged=False, disabletitle=False, **kwargs):
        # print('updateFormTitleBackground', self.DBASETABLENAME, subwidgethaschanged,disabletitle)
        #styling = '.QTabBar::tab:selected , QTabBar * {border-color: rgb(0, 0, 0);'
        #tabbarname = self.tabWidget.tabBar().objectName()
        tabbarname = 'lamia_tabbar'
        styling = '.QTabBar::tab:selected#{}'.format(tabbarname)
        styling += ' {border-color: rgb(0, 0, 0);'
        tabwidgetlist = [self.tabWidget]
        if False and self.parentWidget is None:
            tabwidgetlist.insert(0,self.tabWidgetmain)

        if subwidgethaschanged or disabletitle:
            if subwidgethaschanged:
                styling += ' background-color : rgb(0, 0, 255) }'
            if disabletitle:
                styling += ' background-color : rgb(150, 150, 150) }'
            for wdg in tabwidgetlist:
                wdg.setStyleSheet(styling)

        else:
            if self.currentFeaturePK is not None:
                styling += ' background-color : rgb(0, 255, 0) }'
            else:
                styling += ' background-color : rgb(255, 0, 0) }'
            for wdg in tabwidgetlist:
                wdg.setStyleSheet(styling)



    def _manageRubberbandOnSelectFeature(self, pkfeature=None):
        if (self.parentWidget is None 
                and 'geom' in self.dbase.dbasetables[self.DBASETABLENAME]['fields'].keys()
                and pkfeature):
            currentgeom = self.formutils.getQgsGeomFromPk(pkfeature)
            self.mainifacewidget.qgiscanvas.createRubberBandForSelection(currentgeom)
            self.mainifacewidget.qgiscanvas.rubberBand.show()

        else:
            self.mainifacewidget.qgiscanvas.createorresetRubberband()

    def postSelectFeature(self):
        pass

    def postSaveFeature(self,pkfeature=None):
        pass

    def postDeleteFeature(self):
        pass

    def setTempGeometry(self, 
                        points, 
                        comefromcanvas=True, 
                        showinrubberband=True ):
        """
        Called when self.currentmaptool has finished capturing

        Assign the geometry to self.tempgeometry

        :param points: the list of points coming from the currentmaptool
        :param comefromcanvas: True if come from canvas (need od reprojection)
        :param showinrubberband: True if the temp geometry will be visible with the rubberband

        """
        debug = False

        if debug: logging.getLogger("Lamia").debug('start points : %s %s', self.dbasetablename, points)

        if self.mainifacewidget.qgiscanvas.currentmaptool is not None:
            try:
                self.mainifacewidget.qgiscanvas.currentmaptool.stopCapture.disconnect()
            except TypeError:
                pass

        pointsmapcanvas = []
        pointslayer=[]
        """
        if self.capturetype is None:
            type = self.dbasetable['layer'].geometryType()
        else:
            type = self.capturetype
        """
        #capturetype = self.dbasetable['layer'].geometryType()
        capturetype = self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME]['layer'].geometryType()

        # case point in line layer
        dbasetable = self.dbase.dbasetables[self.DBASETABLENAME]
        if len(points)==2 and points[0] == points[1]:
            #self.rubberBand.reset(0)
            self.mainifacewidget.qgiscanvas.createorresetRubberband(0)
            capturetype = 0.5
        elif len(points) == 1 and dbasetable['geom'] == 'LINESTRING':
            points.append(points[0])
            self.mainifacewidget.qgiscanvas.createorresetRubberband(0)
            capturetype = 0.5
        else:
            self.mainifacewidget.qgiscanvas.createorresetRubberband(capturetype)

        if debug: logging.getLogger("Lamia").debug('type/point : %s %s', str(capturetype), points)

        if comefromcanvas:
            pointsmapcanvas = points
            for point in points:
                pointslayer.append(self.mainifacewidget.qgiscanvas.xformreverse.transform(point))
        else:
            pointslayer = points
            for point in points:
                pointsmapcanvas.append(self.mainifacewidget.qgiscanvas.xform.transform(point))

        if capturetype == 0:
            geometryformap = qgis.core.QgsGeometry.fromPointXY(pointsmapcanvas[0])
            geometryforlayer = qgis.core.QgsGeometry.fromPointXY(pointslayer[0])
        elif capturetype == 0.5:
            geometryformap = qgis.core.QgsGeometry.fromPointXY(pointsmapcanvas[0])
            geometryforlayer = qgis.core.QgsGeometry.fromMultiPolylineXY([pointslayer])
        elif capturetype == 1:
            geometryformap = qgis.core.QgsGeometry.fromMultiPolylineXY([pointsmapcanvas])
            geometryforlayer = qgis.core.QgsGeometry.fromMultiPolylineXY([pointslayer])
        elif capturetype == 2:
            geometryformap = qgis.core.QgsGeometry.fromPolygonXY([pointsmapcanvas])
            geometryforlayer = qgis.core.QgsGeometry.fromPolygonXY([pointslayer])

        #outside qgis bug
        if showinrubberband:
            self.mainifacewidget.qgiscanvas.rubberBand.addGeometry(geometryformap, None)
            self.mainifacewidget.qgiscanvas.rubberBand.show()
        self.tempgeometry = geometryforlayer
        self.lamiageomChanged.emit()

        if debug: logging.getLogger("Lamia").debug('end layer points : %s', pointslayer)
        if debug: logging.getLogger("Lamia").debug('end canvas points : %s', pointsmapcanvas)
        if debug: logging.getLogger("Lamia").debug('end tempgeom : %s', self.toWKT(self.tempgeometry))

        #self.mtool = None


    def ___________________________oldThings(self):
        pass

    if False:
        def _init_loadWidgetDependentResolution(self):
            # adapt to screen res
            app = QApplication.instance()
            screen_resolution = app.desktop().screenGeometry()
            width, height = screen_resolution.width(), screen_resolution.height()
            if width < 1500 and height<1000:
                uipath = os.path.join(os.path.dirname(__file__), 'lamia_propertieswidget.ui')
            else:
                uipath = os.path.join(os.path.dirname(__file__), 'lamia_propertieswidget_resizable.ui')
            uic.loadUi(uipath, self)
            QApplication.processEvents()




        def initTool(self):
            """
            Function to be overloaded in herited class. thie function is called during he __init__ function.
            You can specify :

            - self.CAT = 'Ressources' # the name of the fist column QTreeWidget in upper left part of Lamia dock

            - self.NAME = 'Croquis'     # the name of the second column QTreeWidget in upper left part of Lamia dock

            - self.visualmode = [ 1, 2] # the visual modes you want this widget to appear (1 : prepro, 2 desktop, 4 postpro)

            - self.iconpath = [file_path]     # the file path of the Icon of the second column QTreeWidget in upper left part of Lamia dock

            """

            pass

        def initFieldUI(self):
            """
            Function called during the first loading of the lamia dbase. It loads the widgets in self.userwdgfield variable

            Exemple of minimal code :

            .. code-block:: python

                if self.userwdgfield is None:       #prevent to load multiple times
                    self.userwdgfield = UserUI()
            """
            pass

        def initDesktopUI(self):
            """
            Function called When destop visual mode is loaded. function to be overload if desktop widget is different from
            base widget. You must load the widget in  self.userwdgdesktop variable

            """
            self.initFieldUI()

        # ******************************************************************************************************************
        # **********************************    on dbase loaded   methods        *******************************************
        # ******************************************************************************************************************

        def magicFunction(self):
            """
            Function called when the magic icon is clicked. function to be overload you want a special action
            """
            pass

        def changePropertiesWidget(self, interfacename=None):
            """
            Function activated when visual mode is changed. Assign self.userwdgfield  or self.userwdgdesktop  to
            self.userwdg which is the current widget used.
            Activate changePropertiesWidget for the self.dbasechildwdg also.

            visualmode = 0 is for base interface
            visualmode = 1 is for destop interface
            visualmode = 4 is for postpro interface

            :param interfacename: TODO

            """

            debug = False
            #timestart = self.dbase.getTimeNow()

            if debug:
                QApplication.processEvents()
                #logging.getLogger('Lamia').debug('Start init %s %.3f',self.dbasetablename,  self.dbase.getTimeNow()  - timestart)

            # clear groupBox_properties
            if self.groupBox_properties.layout().count() > 0:
                self.groupBox_properties.layout().itemAt(0).widget().setParent(None)

            # disconnect currentFeatureChanged signal to dbasechildwdg
            for childwdg in self.dbasechildwdg:
                try:
                    self.currentFeatureChanged.disconnect(childwdg.loadChildFeatureinWidget)
                except:
                    pass

            if debug:
                QApplication.processEvents()
                logging.getLogger('Lamia').debug('befor  set wdg  %s %.3f',self.dbasetablename,  self.dbase.getTimeNow()  - timestart)

            if True:
                # load proper widget
                if self.dbase.visualmode in [0, 1, 4]:
                    # define self.userwdg, self.linkuserwdg and self.dbasechildwdg
                    if self.dbase.visualmode == 0:
                        if (interfacename is None
                                or (interfacename is not None
                                        and (len(interfacename.split('_')) == 1
                                            or interfacename.split('_')[1] not in self.specialfieldui) )):
                            self.initFieldUI()
                            if self.userwdgfield is not None:
                                self.userwdg = self.userwdgfield
                                self.linkuserwdg = self.linkuserwdgfield

                            if self.dbasechildwdgfield is not None:
                                self.dbasechildwdg = self.dbasechildwdgfield

                            self.dicttablefieldtoinit = {}
                            if self.linkuserwdg is not None:
                                for key in self.linkuserwdg.keys():
                                    self.dicttablefieldtoinit[key] = self.linkuserwdg[key]['widgets'].keys()
                        else:
                            typeinterface = interfacename.split('_')[1]
                            exec('self.initFieldUI_' + str(typeinterface) + '()')
                            exec('self.userwdg = self.userwdgfield_' + str(typeinterface))
                            exec ('self.linkuserwdg = self.linkuserwdgfield_' + str(typeinterface))
                            self.dbasechildwdg = self.dbasechildwdgfield

                            self.dicttablefieldtoinit = {}
                            if self.linkuserwdg is not None:
                                for key in self.linkuserwdg.keys():
                                    self.dicttablefieldtoinit[key] = self.linkuserwdg[key]['widgets'].keys()
                    elif self.dbase.visualmode == 1:
                        self.initDesktopUI()
                        if self.userwdgdesktop is not None:
                            self.userwdg = self.userwdgdesktop
                            self.linkuserwdg = self.linkuserwdgdesktop
                        else:
                            self.userwdg = self.userwdgfield
                            self.linkuserwdg = self.linkuserwdgfield
                        if self.dbasechildwdgdesktop is not None:
                            self.dbasechildwdg = self.dbasechildwdgfield + self.dbasechildwdgdesktop
                        elif self.dbasechildwdgfield is not None:
                            self.dbasechildwdg = self.dbasechildwdgfield
                        else:
                            self.dbasechildwdg = []
                    elif self.dbase.visualmode == 4:
                        self.initDesktopUI()
                        if self.userwdgfield is not None:
                            self.userwdg = self.userwdgfield
                            self.linkuserwdg = self.linkuserwdgfield
                        if self.dbasechildwdgfield is not None:
                            self.dbasechildwdg = self.dbasechildwdgfield
                        self.dicttablefieldtoinit = {}
                        if self.linkuserwdg is not None:
                            for key in self.linkuserwdg.keys():
                                self.dicttablefieldtoinit[key] = self.linkuserwdg[key]['widgets'].keys()
                    #init fields
                    self.initWidgetUI()
                    # load userwdg
                    if self.userwdg is not None:
                        self.groupBox_properties.layout().addWidget(self.userwdg)
                    self.dicttablefieldtoinit = {}
                    if self.linkuserwdg is not None:
                        for key in self.linkuserwdg.keys():
                            self.dicttablefieldtoinit[key] = self.linkuserwdg[key]['widgets'].keys()
                elif self.dbase.visualmode == 2:
                    self.groupBox_properties.layout().addWidget(self.tableWidget)
                    if self.linkuserwdg is not None:
                        for key in self.linkuserwdg.keys():
                            self.dicttablefieldtoinit[key] = self.dbase.dbasetables[key]['fields'].keys()

            # reconnect currentFeatureChanged signal to dbasechildwdg
            for childwdg in self.dbasechildwdg:
                self.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)

                if debugconnector:
                    tempparentwdg = self
                    tempresult = str(childwdg.dbasetablename) + ',' + str(childwdg.NAME)
                    while tempparentwdg is not None:
                        tempresult += ' - ' + str(tempparentwdg.dbasetablename) + ',' + str(tempparentwdg.NAME)
                        tempparentwdg = tempparentwdg.parentWidget
                    logging.getLogger('Lamia').debug('currentFeatureChanged connection : %s', tempresult)

            if debug:
                QApplication.processEvents()
                logging.getLogger('Lamia').debug('befor  changePropertiesWidget %s %.3f',self.dbasetablename, self.dbase.getTimeNow()  - timestart)

            # dbasechildwdg change
            for childwdg in self.dbasechildwdg:
                childwdg.changePropertiesWidget(interfacename=interfacename)

            if debug:
                QApplication.processEvents()
                logging.getLogger('Lamia').debug('after  changePropertiesWidget %s %.3f',self.dbasetablename,  self.dbase.getTimeNow()  - timestart)

            # load the widgets in main tree
            if self.dbase.visualmode in self.visualmode:
                self.loadWidgetinMainTree()
            else:
                self.unloadWidgetinMainTree()

            # reload state (feature selected before changes)
            if self.linkedtreewidget is not None:
                tempitem = self.linkedtreewidget.currentItem()
                if tempitem is not None and self.windowdialog.MaintreeWidget.currentItem() == self.qtreewidgetitem:
                    try:
                        tempitemid = int(tempitem.text(0))
                        self.onActivationRaw(self.windowdialog.MaintreeWidget.currentItem())
                        self.comboBox_featurelist.setCurrentIndex(self.comboBox_featurelist.findText(str(tempitemid)))
                    except ValueError as e:
                        pass

            if debug:
                QApplication.processEvents()
                logging.getLogger('Lamia').debug('end init %s %.3f',self.dbasetablename,  self.dbase.getTimeNow()  - timestart)


        def loadWidgetinMainTree(self):
            """
            Called on the widget creation in windowsdialog
            load the widget in the main stacked widget
            call onActivationRaw when qtreewidgetitem is clicked in MaintreeWidget
            """

            # add qtreewidget item in MaintreeWidget
            if self.windowdialog is not None and self.parentWidget is None:
                arb = [self.CAT, self.NAME]
                if self.qtreewidgetitem is None:
                    self.qtreewidgetitem = QTreeWidgetItem()
                    if sys.version_info.major == 2:
                        if  isinstance(arb[-1], unicode):
                            self.qtreewidgetitem.setText(0, arb[-1])
                        else:
                            self.qtreewidgetitem.setText(0, str(arb[-1]))
                    else:
                        self.qtreewidgetitem.setText(0, arb[-1])
                    self.qtreewidgetitem.setFlags(self.qtreewidgetitem.flags())
                    if self.iconpath is not None:
                        self.qtreewidgetitem.setIcon(0, QtGui.QIcon(self.iconpath))
                wdgitem = None
                root = self.windowdialog.MaintreeWidget.invisibleRootItem()
                child_count = root.childCount()
                for i in range(child_count):
                    item = root.child(i)
                    if item.text(0) == arb[0]:
                        wdgitem = item
                        break
                if wdgitem is None:
                    wdgitem = QTreeWidgetItem()
                    wdgitem.setText(0, arb[0])
                    self.windowdialog.MaintreeWidget.addTopLevelItems([wdgitem])
                if self.qtreewidgetitem not in [wdgitem.child(i) for i in range(wdgitem.childCount())]:
                    wdgitem.addChild(self.qtreewidgetitem)
                wdgitem.setExpanded(True)


        def unloadWidgetinMainTree(self):
            """
            Unload the widget in the main stacked widget
            """

            arb = [self.CAT, self.NAME]
            if self.windowdialog is not None:
                wdgitem = None
                root = self.windowdialog.MaintreeWidget.invisibleRootItem()
                child_count = root.childCount()
                for i in range(child_count):
                    item = root.child(i)
                    if item.text(0) == arb[0]:
                        wdgitem = item
                        break
                if wdgitem is None:
                    wdgitem = root
                wdgitem.removeChild(self.qtreewidgetitem)
                if wdgitem != self.windowdialog.MaintreeWidget.invisibleRootItem() and wdgitem.childCount() == 0:
                    self.windowdialog.MaintreeWidget.invisibleRootItem().removeChild(wdgitem)

                self.disconnectIdsGui()


        def initWidgets(self):
            """
            Called by  __init__
            Init QTableWidget for "pro" interface
            Init widget geometry buttons
            Init GPS management
            Init magic function
            """

            # **********************************************************
            # PRO Table Things

            if self.linkuserwdg is None:
                templinkuserwgd = {self.dbasetablename: None}
            else:
                templinkuserwgd = self.linkuserwdg

            for tablename in templinkuserwgd:
                if tablename in self.dbase.dbasetables.keys():
                    dbasetable = self.dbase.dbasetables[tablename]
                    for field in dbasetable['fields'].keys():
                        rowPosition = self.tableWidget.rowCount()
                        self.tableWidget.insertRow(rowPosition)
                        item = QTableWidgetItem(tablename + "." + field)
                        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.tableWidget.setItem(rowPosition, 0, item)
                        if 'Cst' in dbasetable['fields'][field].keys():
                            wdg = QComboBox()
                            wdg.addItems([description[0] for description in dbasetable['fields'][field]['Cst']])
                            self.tableWidget.setCellWidget(rowPosition, 1, wdg)
                            if 'ParFldCst' in dbasetable['fields'][field].keys():
                                listfieldname = [self.tableWidget.item(row, 0).text() for row in
                                                range(self.tableWidget.rowCount())]
                                indexparentfield = listfieldname.index(
                                    tablename + '.' + dbasetable['fields'][field]['ParFldCst'])
                                nameparenttalbe, nameparentfield = listfieldname[indexparentfield].split('.')
                                comboparent = self.tableWidget.cellWidget(indexparentfield, 1)
                                try:
                                    comboparent.currentIndexChanged.connect(self.comboparentValueChanged)
                                except Exception as e:
                                    if self.dbase.qgsiface is None:
                                        logging.getLogger("Lamia").debug('error %s %s %s', e, tablename, field)
                        elif 'INTEGER' in dbasetable['fields'][field]['PGtype']:
                            if field[0:3].lower() in ['id_', 'pk_'] or field[0:4].lower() in ['lpk_']:
                                item = QTableWidgetItem()
                                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                                self.tableWidget.setItem(rowPosition, 1, item)

                                wdg2 = QPushButton('Show')
                                wdg2.setEnabled(False)
                                self.tableWidget.setCellWidget(rowPosition, 2, wdg2)
                                wdg2.clicked.connect(self.rawtablePushButtonClicked)
                            else:
                                wdg = QSpinBox()
                                wdg.setRange(-1, 9999999)
                                self.tableWidget.setCellWidget(rowPosition, 1, wdg)
                            if field[0:4].lower() in ['lid_']:
                                wdg2 = QPushButton('Pick')
                                wdg2.setEnabled(False)
                                self.tableWidget.setCellWidget(rowPosition, 2, wdg2)
                                wdg2.clicked.connect(self.rawtablePushButtonClicked)
                        elif 'VARCHAR' in dbasetable['fields'][field]['PGtype']:
                            if 'datetime' in field[0:8]:
                                wdg = QDateTimeEdit()
                                wdg.setSpecialValueText(" ")
                                wdg.setCalendarPopup(True)
                                self.tableWidget.setCellWidget(rowPosition, 1, wdg)
                            elif 'date' in field[0:4]:
                                wdg = QDateEdit()
                                wdg.setSpecialValueText(" ")
                                wdg.setCalendarPopup(True)
                                self.tableWidget.setCellWidget(rowPosition, 1, wdg)
                            else:
                                wdg = QTextEdit()
                                self.tableWidget.setCellWidget(rowPosition, 1, wdg)
                                self.tableWidget.setRowHeight(rowPosition, 60)
                                if 'File' in field:
                                    wdg = QPushButton('File')
                                    self.tableWidget.setCellWidget(rowPosition, 2, wdg)
                                    wdg.clicked.connect(self.rawtablePushButtonClicked)
                                    wdg = QPushButton('Open')
                                    self.tableWidget.setCellWidget(rowPosition, 3, wdg)
                                    wdg.clicked.connect(self.rawtablePushButtonClicked)
                        elif ('NUMERIC'  in dbasetable['fields'][field]['PGtype']
                                    or 'REAL' in dbasetable['fields'][field]['PGtype']):
                            wdg = QDoubleSpinBox()
                            wdg.setRange(-1, 9999999)
                            self.tableWidget.setCellWidget(rowPosition, 1, wdg)
                        if 'FK' in dbasetable['fields'][field].keys():
                            # print(dbasetable['fields'][field]['FK'].split('(')[0])
                            #self.fktables.append(dbasetable['fields'][field]['FK'].split('(')[0])
                            pass    #TODO
                elif os.path.isfile(tablename):
                    print(tablename)

            # **********************************************************
            # geoemtry:

            if self.dbasetable is not None and 'geom' in self.dbasetable.keys():
                self.pushButton_goto.pressed.connect(self.goToFeaturePressed)
                self.pushButton_goto.released.connect(self.goToFeatureReleased)
                self.pushButton_rajoutPointGPS.setEnabled(False)

                self.pushButton_rajoutPointGPS.clicked.connect(self.addGPSPoint)
                self.pushButton_rajoutPoint.clicked.connect(self.addPoint)
                # self.pushButton_rajoutPointGPS.clicked.connect(self.captureGeometry)

                if self.LineENABLED or self.PolygonENABLED:
                    self.pushButton_editgeom.setEnabled(True)
                    self.pushButton_editgeom.clicked.connect(self.windowdialog.editFeature)
                else:
                    self.pushButton_editgeom.setEnabled(False)


                if self.PointENABLED:
                    self.pushButton_addPoint.clicked.connect(self.captureGeometry)
                else:
                    self.pushButton_addPoint.setEnabled(False)

                if self.LineENABLED:
                    self.pushButton_addLine.clicked.connect(self.captureGeometry)
                else:
                    self.pushButton_addLine.setEnabled(False)
                if self.PolygonENABLED:
                    self.pushButton_addPolygon.clicked.connect(self.captureGeometry)
                else:
                    self.pushButton_addPolygon.setEnabled(False)

                # map tool for capturing
                if self.windowdialog is not None:
                    """
                    self.mtoolpoint = self.windowdialog.mtoolpoint
                    self.mtoolline = self.windowdialog.mtoolline
                    self.mtoolpolygon = self.windowdialog.mtoolpolygon
                    """
                    self.mtoolpoint = self.windowdialog.qgiscanvas.mtoolpoint
                    self.mtoolline = self.windowdialog.qgiscanvas.mtoolline
                    self.mtoolpolygon = self.windowdialog.qgiscanvas.mtoolpolygon
            else:
                self.groupBox_geom.setParent(None)
                #self.groupBox_geom.setVisible(False)
                self.pushButton_goto.setEnabled(False)

            # GPS
            if self.gpsutil is not None and (self.gpswidget is not None or (self.dbasetable is not None and 'geom' in self.dbasetable.keys())):
                self.gpsutil.GPSConnected.connect(self.displayGPS)

            # Magic button
            if self.magicfunctionENABLED:
                self.pushButton_magic.clicked.connect(self.magicFunction)
            else:
                self.pushButton_magic.setEnabled(False)

            if self.linkagespec is not None:
                self.pushButton_linkage.clicked.connect(self.manageLinkage)
                self.pushButton_linkage.setEnabled(True)
            else:
                self.pushButton_linkage.setEnabled(False)


        def initWidgetUI(self):
            """
            Called by changePropertiesWidget

            - Init combobox with default values

            - Init Parent/child combobox behaviour
            """

            if self.linkuserwdg is None:
                templinkuserwgd = {self.dbasetablename: None}
            else:
                templinkuserwgd = self.linkuserwdg


            for tablename in templinkuserwgd:
                if tablename in self.dbase.dbasetables.keys():
                    dbasetable = self.dbase.dbasetables[tablename]
                    for field in dbasetable['fields'].keys():
                        for linkuserwdg in [self.linkuserwdg]:
                            if linkuserwdg is None or linkuserwdg.keys() is None:
                                continue

                            if (tablename in linkuserwdg.keys()
                                    and field in linkuserwdg[tablename]['widgets'].keys()):
                                wdgs = linkuserwdg[tablename]['widgets'][field]
                                if 'Cst' in dbasetable['fields'][field].keys():
                                    # combox filling with constraints
                                    if isinstance(wdgs, QComboBox) or (
                                            isinstance(wdgs, list) and isinstance(wdgs[0], QComboBox)):

                                        templist = [description[0] for description in
                                                    dbasetable['fields'][field]['Cst']]
                                        if isinstance(wdgs, QComboBox):
                                            wdgs = [wdgs]
                                        for wdg in wdgs:
                                            wdg.clear()
                                            wdg.addItems(templist)

                                if 'ParFldCst' in dbasetable['fields'][field].keys():
                                    nameparentfield = dbasetable['fields'][field]['ParFldCst']
                                    # userwidget
                                    if (tablename in linkuserwdg.keys() and 'widgets' in linkuserwdg[tablename].keys()
                                            and nameparentfield in linkuserwdg[tablename]['widgets'].keys()
                                            and isinstance(linkuserwdg[tablename]['widgets'][nameparentfield], QComboBox)):
                                        linkuserwdg[tablename]['widgets'][nameparentfield].currentIndexChanged.connect(self.comboparentValueChanged)

                                # multiple wdg for field management
                                if isinstance(wdgs, list):
                                    if isinstance(wdgs[0], QComboBox):
                                        for wdg in wdgs:
                                            wdg.currentIndexChanged.connect(self.manageMultipleWidgetField)
                                    elif isinstance(wdgs[0], QSpinBox) or isinstance(wdgs[0], QDoubleSpinBox):
                                        for wdg in wdgs:
                                            wdg.valueChanged.connect(self.manageMultipleWidgetField)


        def manageMultipleWidgetField(self):
            """
            Activated by widget.valueChanged or widget.currentIndexChanged signal

            Manage multiple combobox or spinbox linked to one table field
            """
            senderwdg = self.sender()

            for tablename in self.linkuserwdg:
                for fieldname in self.linkuserwdg[tablename]['widgets'].keys():
                    wdgs = self.linkuserwdg[tablename]['widgets'][fieldname]
                    if isinstance(wdgs, list) and senderwdg in wdgs:
                        if isinstance(senderwdg, QComboBox):
                            for wdg in wdgs:
                                if wdg != senderwdg:
                                    try:
                                        wdg.currentIndexChanged.disconnect(self.manageMultipleWidgetField)
                                    except:
                                        pass
                                    wdg.setCurrentIndex(senderwdg.currentIndex())
                                    wdg.currentIndexChanged.connect(self.manageMultipleWidgetField)
                            break
                        elif isinstance(senderwdg, QSpinBox) or isinstance(senderwdg, QDoubleSpinBox):
                            for wdg in wdgs:
                                if wdg != senderwdg:
                                    try:
                                        wdg.valueChanged.disconnect(self.manageMultipleWidgetField)
                                    except:
                                        pass
                                    wdg.setValue(senderwdg.value())
                                    wdg.valueChanged.connect(self.manageMultipleWidgetField)
                            break


        def comboparentValueChanged(self, index):
            """
            Activated by currentIndexChanged

            Manage paret/child combobox
            """

            debug = False
            if debug:
                senderwdg = self.sender()
                print('**', senderwdg.objectName())

            senderwdg = self.sender()
            if isinstance(senderwdg, QComboBox) and senderwdg.count() == 0:  # case triple descendant and parent not filled
                return

            if self.groupBox_properties.layout().itemAt(0) is None:
                return

            parenttablename = None
            parentfieldname = None

            if self.groupBox_properties.layout().itemAt(0).widget() == self.userwdg:
                comefromrawtable = False
                if self.linkuserwdg is not None:
                    for tablename in self.linkuserwdg.keys():
                        for fieldname in self.linkuserwdg[tablename]['widgets'].keys():
                            if senderwdg == self.linkuserwdg[tablename]['widgets'][fieldname]:
                                parenttablename = tablename
                                parentfieldname = fieldname
                                break

            elif self.groupBox_properties.layout().itemAt(0).widget() == self.tableWidget:
                ind = self.tableWidget.indexAt(senderwdg.pos()).row()
                parenttablename, parentfieldname = self.tableWidget.item(ind, 0).text().split('.')
                comefromrawtable = True

            if parenttablename is None:
                return

            try:
                parentcstvalue = self.dbase.getConstraintRawValueFromText(parenttablename, parentfieldname,
                                                                        senderwdg.currentText())
            except Exception as e:
                if self.dbase.qgsiface is None:
                    logging.getLogger("Lamia").debug('error %s %s %s', e, parenttablename, parentfieldname)
                return

            dbasetable = self.dbase.dbasetables[parenttablename]
            # get child index and combochild
            listparentcst = [dbasetable['fields'][field]['ParFldCst']
                            if 'ParFldCst' in dbasetable['fields'][field].keys() else None
                            for field in dbasetable['fields'].keys()]

            childfieldnames = [list(dbasetable['fields'].keys())[i] for i in range(len(listparentcst))
                            if parentfieldname == listparentcst[i]]

            if debug: print('**', listparentcst)
            if debug: print('***', childfieldnames)

            if comefromrawtable:
                listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
                for childfieldname in childfieldnames:
                    if dbasetable['fields'][parentfieldname][
                        'PGtype'] == 'INT' and parentcstvalue != '' and parentcstvalue is not None:
                        parentcstvalue = int(parentcstvalue)
                    listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if
                                parentcstvalue in value[2]]
                    indexchildintable = listfieldname.index(parenttablename + '.' + childfieldname)
                    combochild = self.tableWidget.cellWidget(indexchildintable, 1)
                    combochild.clear()
                    if len(listtoadd) > 0:
                        combochild.addItems(listtoadd)
            else:
                for childfieldname in childfieldnames:
                    if dbasetable['fields'][parentfieldname]['PGtype'] == 'INT' and parentcstvalue != '' and parentcstvalue is not None:
                        parentcstvalue = int(parentcstvalue)


                    listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if (value[2] is None or parentcstvalue in value[2])]

                    if debug: print('****', listtoadd)

                    if childfieldname in self.linkuserwdg[parenttablename]['widgets']:
                        combochild = self.linkuserwdg[parenttablename]['widgets'][childfieldname]
                        combochild.clear()
                        if len(listtoadd) > 0:
                            combochild.addItems(listtoadd)



        def manageLinkage(self):
            """
            Called by self.pushButton_linkage.clicked.connect(self.manageLinkage)

            Open dialog when linkage button is clicked
            """
            if self.currentFeature is None:
                return

            if self.dbase.revisionwork:
                self.currentid = int(self.currentFeature['id_' + self.dbasetablename.lower()])
            else:
                self.currentid = self.currentFeature.id()

            self.dlg_linkage = LinkageDialog(self)
            self.dlg_linkage.setWindowModality(2)
            self.dlg_linkage.exec_()
            self.loadFeaturesinTreeWdg()
            idwidgetindex = self.comboBox_featurelist.findText(str(self.currentid))
            if idwidgetindex >= 0:
                self.disconnectIdsGui()
                self.comboBox_featurelist.setCurrentIndex(idwidgetindex)
                self.connectIdsGui()
                self.comboBox_featurelist.currentIndexChanged.emit(idwidgetindex)


        def initLinkageFromGeometry(self, linkagekey, idsourcevalue=None):
            """
            ?
            :param linkagekey:
            :param idsourcevalue:
            """
            idslink = []
            linkagetemp = self.linkagespec[linkagekey]

            if idsourcevalue is None:
                idsourcevalue = self.currentFeature[linkagetemp['idsource']]

            sql = "DELETE FROM " + linkagetemp['tabletc']
            sql += " WHERE  " + linkagetemp['idtcsource'] + " =  " + str(idsourcevalue) + ";"
            # print(sql)
            self.dbase.query(sql)

            for table in self.linkagespec[linkagekey]['desttable']:
                sql = "SELECT " + table + "." + linkagetemp['iddest']  +" FROM " + table + "," + self.dbasetablename
                sql += " WHERE ST_Within(ST_MakeValid(" + table + ".geom),ST_MakeValid(" + self.dbasetablename + ".geom))"
                sql += " AND " + self.dbasetablename + '.id_' + self.dbasetablename.lower() + ' = ' + str(self.currentFeature.id()) + ";"
                query = self.dbase.query(sql)
                if len(query) > 0:
                    idstemp = [row[0] for row in query]
                    idslink += idstemp
            for id in idslink:
                sql = "INSERT INTO " + linkagetemp['tabletc']
                sql += "(" + linkagetemp['idtcsource'] + "," + linkagetemp['idtcdest'] + ") "
                sql += "VALUES(" + str(idsourcevalue) + "," + str(id) + ");"
                self.dbase.query(sql)



        def rawtablePushButtonClicked(self):
            """
            Pro interface - click manager

            """

            senderwdg = self.sender()
            ind = self.tableWidget.indexAt(senderwdg.pos()).row()
            tablename, fieldname = self.tableWidget.item(ind, 0).text().split('.')

            if senderwdg.text() == 'File':
                file, extension = self.dialog.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', None,
                                                                        'All (*.*)', '')
                if file:
                    self.setValueInWidget(self.tableWidget.cellWidget(ind, 1), file, tablename, fieldname)
            if senderwdg.text() == 'Open':
                filepath = self.getValueFromWidget(self.tableWidget.cellWidget(ind, 1), tablename, fieldname)
                os.startfile(self.dbase.completePathOfFile(filepath))
            elif senderwdg.text() == 'Pick':
                self.pickfield = fieldname
                # print('pick', self.pickfield )
                self.pickFeature()
            elif senderwdg.text() == 'Show':
                idrequested = int(self.tableWidget.item(ind, 1).text())
                FKtable = self.dbasetable['fields'][fieldname]['FK'].split('(')[0]
                if 'widget' in self.dbase.dbasetables[FKtable].keys():
                    wdg = self.dbase.dbasetables[FKtable]['widget']
                    wdg.setParent(None)
                    if True:
                        self.disconnectIdsGui()
                        wdg.disconnectIdsGui()
                        wdg.featureSelected(idrequested, True)
                        self.connectIdsGui()
                    self.dialog = QDialog()
                    vboxlayout = QVBoxLayout()
                    vboxlayout.addWidget(wdg)
                    self.dialog.setLayout(vboxlayout)
                    self.dialog.show()



        # *******************************************************************************************************************
        # **********************************    on activation/des methods        *******************************************
        # ******************************************************************************************************************

        def onActivationRaw(self, param1, param2=None):
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

                if param2 == self.qtreewidgetitem:
                    if debug and param2 : logging.getLogger("Lamia").debug('step 2 desactivation %s ', param2.text(0))
                    self.onDesactivationRaw()
                    self.postOnDesactivation()
                    if param2 == param1:
                        self.lastidselected = None

                if param1 == self.qtreewidgetitem :
                    if debug: logging.getLogger("Lamia").debug('step 3 activation %s %s', param1.text(0), param2)
                    # manage display in canvas
                    self._checkLayerVisibility()
                    if self.linkedtreewidget is not None :
                        if self.multipleselection  :
                            self.linkedtreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
                        else:
                            self.linkedtreewidget.setSelectionMode(QAbstractItemView.SingleSelection)

                    # add child widget
                    self.loadChildWidgets()

                    # manage widget display
                    if self.windowdialog is not None :
                        if self.dbasetable is not None and not hasattr(self, 'TOOLNAME'):
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

                    # load feature in bottom qtreewidget
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

                    #change active layer in canvas
                    if qgis.utils.iface is not None and self.dbasetable is not None and self.dbasetable['showinqgis']:
                        qgis.utils.iface.setActiveLayer(self.dbasetable['layerqgis'])

                    # Specific method
                    self.postOnActivation()

        def getcombotypeitemsWhereClause(self):
            ids = [item.text(0) for item in self.linkedtreewidget.selectedItems() ]
            sqlwhereclause =  self.combowdg.currentText() + "_now.id_" + self.combowdg.currentText().lower() + " IN (" + ','.join(ids) + ')'
            return sqlwhereclause

        def combotypeitemsChanged(self, indexitem):

            self.disconnectIdsGui()
            self._clearLinkedTreeWidget()

            headerlist = ['libelle']
            headerlist.insert(0, 'ID')
            self.linkedtreewidget.setColumnCount(len(headerlist))
            self.linkedtreewidget.header().setVisible(True)
            self.linkedtreewidget.setHeaderItem(QTreeWidgetItem(headerlist))
            header = self.linkedtreewidget.header()
            lenheaderlist = len(headerlist)
            if sys.version_info.major == 2:
                for i in range(lenheaderlist):
                    header.setResizeMode(i, QHeaderView.ResizeToContents)
                header.setResizeMode(lenheaderlist - 1, QHeaderView.Stretch)
            elif sys.version_info.major == 3:
                for i in range(lenheaderlist):
                    header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
                header.setSectionResizeMode(lenheaderlist - 1, QHeaderView.Stretch)

            parentitem = self.linkedtreewidget.invisibleRootItem()

            tabletoshow = self.combowdg.currentText()
            if tabletoshow == '':
                return



            sql = "SELECT id_" + tabletoshow.lower() + " ,"
            if len(self.qtreewidgetfields) > 0:
                sql += ','.join(self.qtreewidgetfields)
            sql += " FROM " + tabletoshow  + "_now"
            self.dbasetablename = tabletoshow



            if False:
                if self.combowdg.currentText() == 'Troncon':
                    sql = "SELECT id_infralineaire "
                    if len(self.qtreewidgetfields) > 0:
                        sql += "," + ','.join(self.qtreewidgetfields)
                    sql += " FROM Infralineaire_now"

                    self.dbasetablename = 'Infralineaire'

                elif self.combowdg.currentText() == 'Zone geographique':
                    sql = "SELECT id_zonegeo "
                    if len(self.qtreewidgetfields) > 0:
                        sql += "," + ','.join(self.qtreewidgetfields)
                    sql += " FROM zonegeo_qgis WHERE lpk_revision_end IS NULL"

                    self.dbasetablename = 'Zonegeo'

            sql = self.dbase.updateQueryTableNow(sql)
            query = self.dbase.query(sql)
            ids = [list(row) for row in query]

            lenqtreewidg = len(self.qtreewidgetfields) + 1
            self.treefeatlist = [[id[0], QTreeWidgetItem([str(id[i]) for i in range(lenqtreewidg)])] for id in ids]
            parentitem.addChildren([elem[1] for elem in self.treefeatlist])

            # self.propertieswdgDESORDRE.reloadgraphtype()

            self.connectIdsGui()



        def loadChildWidgets(self):
            """
            Load the childs widgets - called by onActivationRaw

            """

            self.windowdialog.tabWidget_childs.clear()
            # childwdg change
            for childwdg in self.dbasechildwdg:
                if childwdg.NAME is not None:
                    self.windowdialog.tabWidget_childs.addTab(childwdg, QtGui.QIcon(childwdg.iconpath), childwdg.NAME)


        def postOnActivation(self):
            """
            Abstract method - must be implemented
            called by onActivationRaw
            """
            pass

        def onDesactivationRaw(self):
            """
            Called by onActivationRaw when idetifying he deselected item

            Reinit things (rubberband, disconnect signals)

            """
            # reinit
            self.currentFeature = None
            if self.dbasetable is not None and 'layerqgis' in self.dbasetable.keys():
                try :
                    self.dbasetable['layerqgis'].removeSelection()
                except RuntimeError:
                    pass

            if self.rubberBand is not None:
                self.rubberBand.reset(0)
            # self.rubberBand = None
            self.tempgeometry = None

            if hasattr(self, 'combotypeitems'):
                self.dbasetablename = None
                self.combowdg.setVisible(False)
                self._clearLinkedTreeWidget()

            # disconnection
            self.disconnectIdsGui()



        def postOnDesactivation(self):
            """!
            Abstract method - must be implemented
            called by onDesactivationRaw
            """
            pass




        def _checkLayerVisibility(self):
            if self.layerdisplayed:
                qgis.utils.iface.setActiveLayer(self.dbasetable['layer'])
            if self.qtreewidgetitem.checkState(0) == 2 and not self.layerdisplayed:
                # qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbasetable['layer'],True)
                qgis.utils.iface.legendInterface().setLayerVisible(self.dbasetable['layer'], True)
                # self.dbasetable['layer'].setOpacity(1.0)
                # print('active')
                self.layerdisplayed = True
            elif self.qtreewidgetitem.checkState(0) == 0 and self.layerdisplayed:
                # qgis.core.QgsMapLayerRegistry.instance().removeMapLayer (self.dbasetable['layer'])
                qgis.utils.iface.legendInterface().setLayerVisible(self.dbasetable['layer'], False)
                # self.dbasetable['layer'].setOpacity(0.0)
                # print('unactive')
                self.layerdisplayed = False



        def loadChildFeatureinWidget(self):
            """
            Called by currentFeatureChanged emited by parent widget if it exists
            Call loadFeaturesinTreeWdg
            Manage behaviour of the widget
            emit currentFeatureChanged for child widgets

            """


            debug = False

            if debug: logging.getLogger("Lamia").debug('Start %s',self.dbasetablename)
            if debug: starttime = time.time()

            self.loadFeaturesinTreeWdg()

            if (self.comboBox_featurelist.count() > 0 and self.comboBox_featurelist.itemText(0) != '') or hasattr(self, 'TOOLNAME'):
                self.setEnabled(True)
                self.comboBox_featurelist.currentIndexChanged.emit(0)
            else:
                self.initFeatureProperties(None)
                self.postInitFeatureProperties(None)
                self.currentFeature = None

            if self.parentWidget is not None:
                if (( self.parentWidget.comboBox_featurelist.count() == 0
                        and self.parentWidget.comboBox_featurelist.itemText(0) == '')
                        or self.parentWidget.comboBox_featurelist.currentText() == self.newentrytext
                        or self.parentWidget.isEnabled() == False):
                    self.initFeatureProperties(None)
                    self.setEnabled(False)
                else:
                    self.setEnabled(True)

            if debug: logging.getLogger("Lamia").debug('End %s %s', self.dbasetablename, str(time.time() -starttime ))

            self.currentFeatureChanged.emit()



        def loadFeaturesinTreeWdg(self):
            """
            load features in self.linkedtreewidget
            called whenever the list need to be reinitialized (ex : click in maintreewidget,...)
            """

            debug = False

            if debug: timestart = self.dbase.getTimeNow()

            self.disconnectIdsGui()

            if debug: logging.getLogger("Lamia").debug('Start %s %s %s', self.dbasetablename, self.NAME, self.parentWidget)

            # clear treewidget
            self._clearLinkedTreeWidget()

            # mise en forme du linkedtreewidget et definition du "parentitem" qui correspond au nom de la table
            parentitem = None
            if self.linkedtreewidget is not None:
                headerlist = list(self.qtreewidgetfields)
                headerlist.insert(0, 'ID')
                self.linkedtreewidget.setColumnCount(len(headerlist))
                self.linkedtreewidget.header().setVisible(True)
                self.linkedtreewidget.setHeaderItem(QTreeWidgetItem(headerlist))
                header = self.linkedtreewidget.header()
                lenheaderlist = len(headerlist)
                if sys.version_info.major == 2:
                    for i in range(lenheaderlist):
                        header.setResizeMode(i, QHeaderView.ResizeToContents)
                    header.setResizeMode(lenheaderlist-1, QHeaderView.Stretch)
                elif  sys.version_info.major == 3:
                    for i in range(lenheaderlist):
                        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(lenheaderlist-1, QHeaderView.Stretch)

                parentitem = self.linkedtreewidget.invisibleRootItem()
            elif (self.parentWidget is not None and self.parentWidget.linkedtreewidget is not None
                    and self.parentWidget.currentFeature is not None):
                root = self.parentWidget.linkedtreewidget.invisibleRootItem()
                indexchild = [root.child(i).text(0) for i in range(root.childCount())].index(str(self.parentWidget.dbasetablename))
                tempitem = root.child(indexchild)
                if self.dbase.revisionwork:
                    parentfeat = self.dbase.getLayerFeatureByPk( self.parentWidget.dbasetablename, self.parentWidget.currentFeature.id() )
                    parentid = parentfeat['id_' + self.parentWidget.dbasetablename]
                    indexchild = [tempitem.child(i).text(0) for i in range(tempitem.childCount())].index(str(parentid))
                else:
                    indexchild = [tempitem.child(i).text(0) for i in range(tempitem.childCount())].index(str(self.parentWidget.currentFeature.id()))
                parentitem = tempitem.child(indexchild)

            # selection of particular feature to load (if parentfeature, or window only mode)
            ids = self.loadIds()

            # creation de la liste des elements qui figurent dans le linkedtreewidget
            lenqtreewidg = len(self.qtreewidgetfields) + 1
            if sys.version_info.major == 2:
                self.treefeatlist = [[id[0], QTreeWidgetItem([str(id[i]) if not isinstance(id[i], unicode) else id[i] for i in range(lenqtreewidg)])] for id in ids]
            else:
                self.treefeatlist = [[id[0], QTreeWidgetItem([str(id[i]) for i in range(lenqtreewidg)])] for id in ids]

            # ajout des ids dans le qtreewidgetitem parent
            if parentitem is not None:
                parentqtreewdgitem = None
                if parentitem.parent() is not None:
                    for i in range(parentitem.parent().childCount()):
                        if parentitem.parent().child(i) != parentitem:
                            parentitem.parent().child(i).takeChildren()
                    if self.dbasetablename in [parentitem.child(i).text(0) for i in range(parentitem.childCount())]:
                        index = [parentitem.child(i).text(0) for i in range(parentitem.childCount())].index(self.dbasetablename)
                        parentitem.child(index).takeChildren()
                        parentqtreewdgitem = parentitem.child(index)
                    else:
                        parentqtreewdgitem = QTreeWidgetItem(parentitem, [self.dbasetablename])
                else:
                    parentqtreewdgitem = QTreeWidgetItem(parentitem, [self.dbasetablename])
                    # print(parentqtreewdgitem.text(0))

                parentqtreewdgitem.addChildren([elem[1] for elem in self.treefeatlist])

            if debug: logging.getLogger('Lamia').debug('feat list %s', str(self.treefeatlist))

            # enable/disable le widget selon que des ids ont ete trouves
            if len(self.treefeatlist) > 0:
                self.groupBox_properties.setEnabled(True)
                self.groupBox_geom.setEnabled(True)
                self.comboBox_featurelist.addItems([str(elem[0]) for elem in self.treefeatlist])
            else:
                self.groupBox_properties.setEnabled(False)
                self.groupBox_geom.setEnabled(False)
                self.currentFeature = None
                self.initFeatureProperties(None)

            if debug: logging.getLogger('Lamia').debug('end  %.3f', self.dbase.getTimeNow()  - timestart)
            self.connectIdsGui()


        def disconnectIdsGui(self):
            """
            Disconnect self.featureSelected from main QTreeWidget and comboBox_featurelist
            """
            try:
                #self.linkedtreewidget.currentItemChanged.disconnect(self.featureSelected)
                self.linkedtreewidget.itemSelectionChanged.disconnect(self.featureSelected)
            except:
                pass
            try:
                self.comboBox_featurelist.currentIndexChanged.disconnect(self.featureSelected)
            except:
                pass


        def connectIdsGui(self):
            """
            Connect self.featureSelected from main QTreeWidget and comboBox_featurelist
            """

            if self.linkedtreewidget is not None and isinstance(self.linkedtreewidget, QTreeWidget):
                self.linkedtreewidget.itemSelectionChanged.connect(self.featureSelected)

            self.comboBox_featurelist.currentIndexChanged.connect(self.featureSelected)


        def _clearLinkedTreeWidget(self):
            """
            Clear LinkedTreeWidget and linked combobox
            """

            if self.linkedtreewidget is not None and isinstance(self.linkedtreewidget, QTreeWidget):
                self.linkedtreewidget.clear()
            self.comboBox_featurelist.clear()


        def updateWorkingDate(self):
            """
            No more used
            """
            subsetstring = None
            if self.dbasetype == 'spatialite':
                subsetstring = '"datetimecreation" <= ' + "'" + self.workingdate + "'"
                subsetstring += ' AND CASE WHEN "datetimedestruction" IS NOT NULL  THEN "datetimedestruction" > ' + "'" + self.workingdate + "'" + ' ELSE 1 END'
            elif self.dbasetype == 'postgis':
                subsetstring = '"datetimecreation" <= ' + "'" + self.workingdate + "'"
                subsetstring += ' AND CASE WHEN "datetimedestruction" IS NOT NULL  THEN "datetimedestruction" > ' + "'" + self.workingdate + "'" + ' ELSE TRUE END'
            return subsetstring



        def loadIds(self):
            """
            Called by loadFeaturesinTreeWdg

            :return: ids : an array of the wanted ids, with eventualy more value defined in self.qtreewidgetfields
            """

            ids = []
            if self.dbasetablename is not None:
                if False:
                    strid = 'id_' + self.dbasetablename.lower()
                    sql = "SELECT " + strid
                    if len(self.qtreewidgetfields)>0 :
                        sql += "," + ','.join(self.qtreewidgetfields)
                    sql += " FROM " + self.dbasetablename.lower() + '_qgis'
                    sql += ' WHERE '
                    sql += self.dbase.dateVersionConstraintSQL()
                    
                strid = 'id_' + self.dbasetablename.lower()
                sql = "SELECT " + strid
                if len(self.qtreewidgetfields)>0 :
                    sql += "," + ','.join(self.qtreewidgetfields)
                sql += " FROM " + self.dbasetablename.lower() + '_now'
                sql = self.dbase.updateQueryTableNow(sql)

                if (self.parentWidget is not None and self.linkagespec is not None
                        and self.parentWidget.currentFeature is not None):
                    linkagespeckey = None
                    for key in self.linkagespec.keys():
                        if self.parentWidget.dbasetablename in self.linkagespec[key]['desttable']:
                            linkagespeckey = key
                    if linkagespeckey is not None:
                        linkagetemp = self.linkagespec[linkagespeckey]

                        if linkagetemp['tabletc'] is None:

                            #linkagedest
                            sqltemp = " SELECT " + linkagetemp['iddest'] + " FROM " + self.parentWidget.dbasetablename.lower() + '_qgis'
                            sqltemp += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)

                            linkagedest = self.dbase.query(sqltemp)[0][0]
                            if linkagedest is None:
                                # print('None find')
                                return []
                            sql += " AND " + linkagetemp['idsource'] + " = " + str(linkagedest)
                            #TODO versionning

                        elif linkagetemp['tabletc'] == 'within':
                            sqltemp = " SELECT "+ linkagetemp['iddest']
                            if len(self.qtreewidgetfields) > 0:
                                sqltemp += "," + ','.join(self.qtreewidgetfields)
                            sqltemp += " FROM " + self.dbasetablename.lower() + "_now" + ', ' + self.parentWidget.dbasetablename.lower()
                            sqltemp += " WHERE ST_WITHIN(ST_MakeValid(" + self.parentWidget.dbasetablename.lower() + ".geom) , "
                            sqltemp += "ST_MakeValid(" + self.dbasetablename.lower() + "_now.geom) )"
                            sqltemp += " AND pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
                            sqltemp = self.dbase.updateQueryTableNow(sqltemp)
                            sql = sqltemp
                        else:
                            #get parent feature field for link
                            sqltemp = "SELECT " + linkagetemp['iddest']
                            sqltemp += " FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
                            sqltemp += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = "
                            sqltemp += str(self.parentWidget.currentFeaturePK)
                            res = self.dbase.query(sqltemp)
                            linkidparent = res[0][0]

                            sqltemp = "SELECT " + linkagetemp['idtcsource'] + " FROM " + linkagetemp['tabletc']
                            sqltemp += " WHERE " + linkagetemp['idtcdest'] + " = "
                            #sqltemp += str(self.parentWidget.currentFeature[linkagetemp['iddest']])
                            sqltemp += str(linkidparent)
                            sqltemp += " AND lpk_revision_begin <= " + str(self.dbase.currentrevision)
                            if self.dbase.dbasetype == 'postgis':
                                sqltemp += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
                                sqltemp += " lpk_revision_end > " + str(self.dbase.currentrevision)
                                sqltemp += " ELSE TRUE END "
                            elif self.dbase.dbasetype == 'spatialite':
                                sqltemp += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
                                sqltemp += " lpk_revision_end > " + str(self.dbase.currentrevision)
                                sqltemp += " ELSE 1 END"

                            query = self.dbase.query(sqltemp)

                            if len(query) > 0 :
                                idstemp = [str(row[0]) for row in query]
                                idssql = '(' + ','.join(idstemp) + ')'
                                sql += " AND " + linkagetemp['idsource'] + " IN " + idssql
                            else:
                                return ids

                sqlbeforepost = str(sql)
                sql = self.postloadIds(sql)
                if sql == sqlbeforepost and self.dbasetablename is not None:
                    strid = 'id_' + self.dbasetablename.lower()
                    sql += ' ORDER BY ' + strid

                sql += ';'
                query = self.dbase.query(sql)

                if query != None:
                    ids = [row for row in query]
                    i=0
                    j=0
                    res=[]
                    for row in ids :
                        j=0
                        res=res+[[]]
                        for id in row :
                            if j>0:
                                res[i] += [self.dbase.getConstraintTextFromRawValue(self.dbasetablename,
                                                                                    self.qtreewidgetfields[j - 1],
                                                                                    ids[i][j])]
                            else :
                                res[i]+=[ids[i][j]]
                            j=j+1
                        i=i+1
                    ids=res

            elif os.path.isfile(self.dbasetablename):
                # print('load ids file')
                self.dbasefiledata = []
                #pathrecentproject = os.path.join(os.path.dirname(__file__), '..', 'config', 'path.txt')
                file = open(self.dbasetablename, "r")
                lines = file.readlines()
                file.close()
                for line in lines:
                    if line != '':
                        self.dbasefiledata.append(line.strip().split(';') )
                # ids = range(len(self.dbasefiledata))
                ids = [[i] for i in range(len(self.dbasefiledata))]

            return ids


        def postloadIds(self,sqlin):
            """
            Enable to modify the sql used to get ids

            :param sqlin: the normal sql generated by loadIds

            :return: the modified sql tu use in loadIds
            """
            return sqlin



        # *******************************************************************************************************************
        # **********************************    core methods        *******************************************
        # ******************************************************************************************************************

        def featureSelected(self, item=None, itemisid=False):
            """
            Action when a feature is selected somewhere (Main QTreeWidget, ids-Combobox)

            :param item: a QTreeWidgetItem or a Combobox index
            :param itemisid: if True, item is an pk

            """
            debug = False

            if self.linkedtreewidget is not None and self.sender() == self.linkedtreewidget:
                item = self.linkedtreewidget.currentItem()

            if debug: logging.getLogger("Lamia").debug('*******')
            #if debug : logging.getLogger("Lamia").debug('start sender : %s', self.sender(), self.sender().objectName())
            if debug: logging.getLogger("Lamia").debug('start %s %s %s %s', self.dbasetablename, item, type(item), str(itemisid))
            if debug and isinstance(item, QTreeWidgetItem) : logging.getLogger("Lamia").debug('start item.text : %s', item.text(0))


            # ************** init thing *********************************
            # remove selection in canvas
            if self.parentWidget is None and self.dbasetable is not None:
                self.dbasetable['layer'].removeSelection()
            # init thing
            self.disconnectIdsGui()
            self.beforesavingFeature = None
            #case deep copy
            self.deepCopyDisconnect()

            # remove new entry if exists
            res = self.comboBox_featurelist.findText(self.newentrytext)
            if res >= 0:
                if self.linkedtreewidget is not None:
                    itemintree = self.linkedtreewidget.findItems(self.newentrytext, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 0)[0]
                    self.linkedtreewidget.invisibleRootItem().removeChild(itemintree)
                self.comboBox_featurelist.removeItem(self.comboBox_featurelist.count()-1)

            # ************** get id selected and link treewidget and combobox *********************************
            id = None

            if isinstance(item, QTreeWidgetItem) and item.parent() is not None:
                # print('featsel',item.parent().text(0),self.dbasetablename)
                if item.parent().text(0) == self.dbasetablename:    # treewdgitem has no parent
                    if debug: logging.getLogger("Lamia").debug('item with parent as current widget')
                    self.currentFeature = None
                    self.currentFeaturePK = None
                    id = int(item.text(0))
                    if self.windowdialog is not None:
                        self.windowdialog.MaintabWidget.setCurrentIndex(0)
                    self.comboBox_featurelist.setCurrentIndex(self.comboBox_featurelist.findText(str(id)))
                elif item.parent().text(0) in [wdg.dbasetablename for wdg in self.dbasechildwdg]:   # treewdgitem has parent : child item
                    if debug: logging.getLogger("Lamia").debug('item with parent as child widget')
                    # self.currentFeature = savedcurrentFeature
                    childindex = [wdg.dbasetablename for wdg in self.dbasechildwdg].index(item.parent().text(0))
                    if self.windowdialog is not None:
                        self.windowdialog.MaintabWidget.setCurrentIndex(1)
                        self.windowdialog.tabWidget_childs.setCurrentIndex(childindex)
                    id = item.text(0)
                    childcomboindex = self.dbasechildwdg[childindex].comboBox_featurelist.findText(str(id))
                    self.dbasechildwdg[childindex].comboBox_featurelist.setCurrentIndex(childcomboindex)
                    self.connectIdsGui()
                    return
                elif item.text(0) in [wdg.dbasetablename for wdg in self.dbasechildwdg]:
                    if debug: logging.getLogger("Lamia").debug('generic child widget selected')
                    # self.currentFeature = savedcurrentFeature
                    childindex = [wdg.dbasetablename for wdg in self.dbasechildwdg].index(item.text(0))
                    if self.windowdialog is not None:
                        self.windowdialog.MaintabWidget.setCurrentIndex(1)
                        self.windowdialog.tabWidget_childs.setCurrentIndex(childindex)
                    self.connectIdsGui()
                    return
                elif self.dbasetable is None:
                    if debug: logging.getLogger("Lamia").debug('no self.dbasetable')
                    id = int(item.text(0))
                else:
                    self.connectIdsGui()
                    return
            elif isinstance(item, QTreeWidgetItem) and item.parent() is None:
                if debug: logging.getLogger("Lamia").debug('no item.parent()')
                try:
                    id = int(item.text(0))
                except ValueError:      # item text is not an id
                    self.connectIdsGui()
                    return
            elif isinstance(item, int) and not itemisid:        #feature selected with combobox
                if debug: logging.getLogger("Lamia").debug('come from combobox')

                if item >= 0:
                    id = int(self.comboBox_featurelist.itemText(item))
                    if self.linkedtreewidget is not None and isinstance(self.linkedtreewidget, QTreeWidget) :

                        parentitem = self.linkedtreewidget.findItems(self.dbasetablename, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 0)[0]
                        indexchild = [parentitem.child(i).text(0) for i in range(parentitem.childCount())].index(str(id))
                        itemtodisplay = parentitem.child(indexchild)
                        self.linkedtreewidget.setCurrentItem(itemtodisplay)

            elif isinstance(itemisid, bool) and itemisid:
                id = item
            elif isinstance(itemisid, QTreeWidgetItem):
                self.connectIdsGui()
                return
            else:   #new feature
                self.currentFeature = None
                self.currentFeaturePK = None
                id = None



            # **************** gui things when selected ***************************************************************
            if self.dbasetable is not None :
                try:
                    test = id
                except UnboundLocalError:
                    return

                if id is not None:        # item clicked in treewidget
                    self.lastidselected = id
                    # print('self.lastidselected', self.dbasetablename, self.lastidselected)
                    #print('ok', self.dbasetable['fields'].keys())
                    pk = self.getPkFromId(self.dbasetablename, id)
                    self.currentFeature = self.dbase.getLayerFeatureByPk(self.dbasetablename, pk)
                    self.currentFeaturePK = self.currentFeature.id()

                    # print('id', id, pk,self.currentFeaturePK)

                    if self.parentWidget is None:
                        if self.multipleselection :
                            ids = [int(item.text(0)) for item in self.linkedtreewidget.selectedItems()]
                            pks = [self.dbase.getLayerFeatureById(self.dbasetablename, id).id() for id in ids]

                            self.dbasetable['layerqgis'].selectByIds(pks)
                            # print('***', ids, pk)
                        else:
                            self.dbasetable['layerqgis'].selectByIds([self.currentFeature.id()])

                    if self.linkagespec is not None:
                        self.pushButton_linkage.setEnabled(True)

                else:                       # new item
                    if self.linkedtreewidget is not None and isinstance(self.linkedtreewidget, QTreeWidget):
                        itemtemp = QTreeWidgetItem([self.newentrytext])
                        self.linkedtreewidget.addTopLevelItems([itemtemp])
                        self.linkedtreewidget.setCurrentItem(itemtemp)
                    self.comboBox_featurelist.addItem(self.newentrytext)
                    self.comboBox_featurelist.setCurrentIndex(self.comboBox_featurelist.findText(self.newentrytext))
                    self.groupBox_properties.setEnabled(True)
                    self.groupBox_geom.setEnabled(True)
                    if self.linkagespec is not None:
                        self.pushButton_linkage.setEnabled(False)
            elif self.dbasetablename is not None and os.path.isfile(self.dbasetablename): #widget has file linked
                if id is not None:  # item clicked in treewidget
                    for i, wdg in enumerate(self.linkuserwdg[self.dbasetablename]):
                        self.currentFeature = [id] + self.dbasefiledata[id]
                        # self.currentFeaturePK =
                        wdg.setText(self.dbasefiledata[id][i])
                else:  # new item
                    if self.linkedtreewidget is not None and isinstance(self.linkedtreewidget, QTreeWidget):
                        itemtemp = QTreeWidgetItem([self.newentrytext])
                        self.linkedtreewidget.addTopLevelItems([itemtemp])
                        self.linkedtreewidget.setCurrentItem(itemtemp)
                    self.comboBox_featurelist.addItem(self.newentrytext)
                    self.comboBox_featurelist.setCurrentIndex(self.comboBox_featurelist.findText(self.newentrytext))
                    self.groupBox_properties.setEnabled(True)
                    self.groupBox_geom.setEnabled(True)

            # init raw table with attributes
            self.initFeatureProperties(self.currentFeature)
            self.postInitFeatureProperties(self.currentFeature)

            # signals
            self.currentFeatureChanged.emit()
            self.connectIdsGui()



        def createParentFeature(self):
            """
            Create a new line in Objet table

            """
            pkobjet = self.dbase.createNewObjet()




        def initFeatureProperties(self, feat, inputtablename=None, fieldname=None, value=None):
            """
            Called by featureSelected
            Fill the fields in the widget

            :param feat: the selected  QgsFeature - if None it s a new feature
            :param inputtablename:  To init a specific table with specific field and a specific value
            :param fieldname:  specific field
            :param value:  specific value
            :return:
            """

            
            if feat is not None and feat.id() == 0:
                return

            if self.dbasetable is not None:
                if self.linkuserwdg is None:
                    templinkuserwgd = {self.dbasetablename: None}
                else:
                    templinkuserwgd = self.linkuserwdg

                if inputtablename is None:
                    tablestoiterate = self.dicttablefieldtoinit.keys()
                else:
                    tablestoiterate = [inputtablename]

                #Then get values
                for tablename in tablestoiterate:
                    dbasetable = self.dbase.dbasetables[tablename]
                    if len(self.dicttablefieldtoinit[tablename]) == 0 :
                        continue
                    if feat is not None:
                        if fieldname is None:
                            fieldstoiterate = self.dicttablefieldtoinit[tablename]
                        else:
                            fieldstoiterate = [fieldname]
                        sql = "SELECT " + ','.join(fieldstoiterate) + " FROM " + self.dbasetablename + "_qgis "
                        sql += " WHERE pk_" + self.dbasetablename.lower() + " = " + str(feat.id())
                        result = self.dbase.query(sql)[0]

                    else:
                        if fieldname is None:
                            fieldstoiterate = self.dicttablefieldtoinit[tablename]
                        else:
                            fieldstoiterate = [fieldname]

                    for i, field in enumerate(fieldstoiterate):
                        # raw table
                        if feat is not None and value is None:
                            valuetoset = result[i]
                        else:
                            valuetoset = value

                        if self.dbase.utils.isAttributeNull(valuetoset):
                            valuetoset = None

                        if self.dbase.visualmode in [0, 1]:
                            if (tablename in templinkuserwgd.keys()
                                    and templinkuserwgd[tablename] is not None
                                    and 'widgets' in templinkuserwgd[tablename].keys()
                                    and field in  templinkuserwgd[tablename]['widgets'].keys()):
                                if isinstance(templinkuserwgd[tablename]['widgets'][field], list):
                                    self.setValueInWidget(templinkuserwgd[tablename]['widgets'][field][0], valuetoset, tablename, field)
                                else:
                                    self.setValueInWidget(templinkuserwgd[tablename]['widgets'][field], valuetoset, tablename,field)

                        if self.dbase.visualmode == 2 :
                            listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
                            itemindex = listfieldname.index(tablename + '.' + field)

                            if self.tableWidget.cellWidget(itemindex, 1) is not None:
                                self.setValueInWidget(self.tableWidget.cellWidget(itemindex, 1), valuetoset, tablename, field)
                            else:
                                if self.tableWidget.item(itemindex, 1) is not None:
                                    if valuetoset is None:
                                        self.tableWidget.item(itemindex, 1).setText('')
                                    else:
                                        self.tableWidget.item(itemindex, 1).setText(str(valuetoset))

            #lidchoosers
            for lidchooser in self.lamiawidgets:
                lidchooser.initProperties()

            # current prestation case:
            self.pushButton_savefeature.setEnabled(True)

            if feat is not None and self.linkagespec is not None and 'Marche' in self.linkagespec.keys()  and self.dbase.currentprestationid is not None:
                # search table with lk prestation
                if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
                    isspatial = self.dbasetable['layerqgis'].geometryType() < 3
                else:
                    isspatial = self.dbasetable['layerqgis'].isSpatial()
                if isspatial:
                    # if self.dbasetable['layerview'].isSpatial():
                    # lk_presta = self.dbasetable['layerview'].getFeatures(qgis.core.QgsFeatureRequest(feat.id())).next()['lk_marche']
                    lk_presta = self.dbase.getLayerFeatureById(self.dbasetablename, feat.id())['lk_marche']
                else:
                    listfeat = list(self.dbasetable['layerqgis'].getFeatures())
                    featid = [fet.id() for fet in listfeat]
                    index = featid.index(feat.id())
                    lk_presta = listfeat[index]['lk_marche']

                if lk_presta != self.dbase.currentprestationid:
                    self.pushButton_savefeature.setEnabled(False)



        def setValueInWidget(self, wdg, valuetoset, table, field):
            """
            Called by initFeatureProperties when iterating the fields

            :param wdg:         the widget to set a value to
            :param valuetoset:  the value
            :param table:       the table of the value
            :param field:       the field of the value
            """

            if isinstance(wdg, QTextEdit) or isinstance(wdg, QLineEdit):
                if valuetoset is not None:
                    wdg.setText(valuetoset)
                else:
                    wdg.setText('')
            elif isinstance(wdg, QSpinBox) or isinstance(wdg, QDoubleSpinBox):
                try:
                    if valuetoset is not None:
                        wdg.setValue(valuetoset)
                    else:
                        wdg.setValue(-1)
                except Exception as e:
                    if self.dbase.qgsiface is None:
                        logging.getLogger("Lamia").debug('error %s %s %s %s', table,field , str(valuetoset), e)
            elif isinstance(wdg, QComboBox):
                try:
                    if valuetoset is not None:
                        text = self.dbase.getConstraintTextFromRawValue(table, field, valuetoset)
                        index = wdg.findText(text)
                        wdg.setCurrentIndex(index)
                    else:
                        wdg.setCurrentIndex(0)
                except Exception as e:
                    if self.dbase.qgsiface is None:
                        logging.getLogger("Lamia").debug('error %s %s %s',table,field ,  e)
            elif isinstance(wdg, QDateEdit):
                if valuetoset is not None:
                    if isinstance(valuetoset, str) or isinstance(valuetoset, unicode):
                        wdg.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd'))

                    elif isinstance(valuetoset, QtCore.QDate):
                        wdg.setDate(valuetoset)
                else:
                    wdg.setSpecialValueText(" ")
                    wdg.setDate(QtCore.QDate.fromString('0001-01-01', 'yyyy-MM-dd'))

            elif isinstance(wdg, QDateTimeEdit):
                if valuetoset is not None:
                    if isinstance(valuetoset, str) or isinstance(valuetoset, unicode):
                        wdg.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd hh:mm:ss'))

                    elif isinstance(valuetoset, QtCore.QDate):
                        wdg.setDate(valuetoset)
                    elif isinstance(valuetoset, datetime.datetime):
                        wdg.setDateTime(QtCore.QDateTime.fromString(str(valuetoset), 'yyyy-MM-dd hh:mm:ss'))
                else:
                    wdg.setSpecialValueText(" ")
                    wdg.setDate(QtCore.QDate.fromString('0001-01-01', 'yyyy-MM-dd'))

            elif isinstance(wdg, QCheckBox):
                if valuetoset is not None:
                    if valuetoset:
                        wdg.setCheckState(2)
                    else:
                        wdg.setCheckState(0)
                else:
                    wdg.setCheckState(0)

            elif isinstance(wdg, QLabel):
                if valuetoset is not None:
                    if 'Cst' in self.dbase.dbasetables[table]['fields'][field].keys():
                        wdg.setText(self.dbase.getConstraintTextFromRawValue(table, field, valuetoset))
                    else:
                        wdg.setText(valuetoset)
                else:
                    wdg.setText('')


        def saveFeature(self,pushbuttonsignal=0, showsavemessage=True):
            """
            Action when save feature is clicked

            1. Create feat and save properties. Manage versioning:

                    new version : save old version(just revision_end) -> create new and copy old feat to new -> save properties

                    new : createnew and save properties

                    existing : save properties

            2. reload treewidget and widget with new feat properties


            :param pushbuttonsignal: to catch a button signal
            :param showsavemessage:  show save message in qgis interface

            """

            # *************************
            # save previous feature

            debug = False
            if debug :
                timestart = self.dbase.getTimeNow()
            if debug: logging.getLogger("Lamia").debug('start')


            self.canvas.freeze(True)

            if self.dbasetable is not None :
                if self.currentFeature is not None:
                    self.currentFeature = self.dbase.getLayerFeatureByPk(self.dbasetablename, self.currentFeaturePK)
                    self.beforesavingFeature = qgis.core.QgsFeature(self.currentFeature)
                    self.beforesavingFeaturePK = self.currentFeature.id()
                else:
                    self.beforesavingFeature = None
                    self.beforesavingFeaturePK = None

            # *************************
            # set geometry first - if geometry false or error :  return and noing is created/modified
            # create self.currentFeature if newfeature case (with only geometry info)

            if self.windowdialog.editfeatureworking:
                #tempgeom = self.windowdialog.editfeaturelayer.selectedFeatures()[0].geometry()
                self.windowdialog.closeEditFeature(savechanges=True)
                self.currentFeaturePK = self.currentFeature.id()
                self.currentFeature = self.dbase.getLayerFeatureByPk(self.dbasetablename, self.currentFeaturePK)

            else:
                geometryisvalid = self.setGeometryToFeature()
                if not geometryisvalid:
                    return

            if self.dbasetable is not None:
                # manage version
                self.currentFeature, self.currentFeaturePK = self.manageFeatureCreationOrUpdate()

                #get feature of dbasetablename saved (only geom saved)
                self.currentFeature = self.saveQGisFeature(self.dbasetablename, self.currentFeature)
                self.currentFeaturePK = self.currentFeature.id()


                # if debug: logging.getLogger("Lamia").debug('saveQGisFeature done with geom  : %s',self.currentFeature.geometry().exportToWkt())
                if debug: logging.getLogger('Lamia').debug('time  %.3f', self.dbase.getTimeNow()  - timestart)

                # *************************
                # save attributes
                # first assure that parent features are created

                if self.beforesavingFeature is None:
                    self.createParentFeature()

                if self.savingnewfeatureVersion :
                    self.createParentFeature()
                    self.updateParentFeature()

                    if debug: logging.getLogger("Lamia").debug('createParentFeature ok')
                    if debug: logging.getLogger('Lamia').debug('time  %.3f', self.dbase.getTimeNow()  - timestart)

                self.saveFeatureProperties()

                # then save properly ressource file if exists
                if self.linkuserwdg is not None and 'Ressource' in self.linkuserwdg.keys():
                    self.saveRessourceFile()

                # do postsavefeature traitment
                self.manageGeomOfLinkedFeat()
                self.postSaveFeature(self.savingnewfeature)

                if debug: logging.getLogger("Lamia").debug('postSaveFeature done')
                if debug: logging.getLogger('Lamia').debug('time  %.3f', self.dbase.getTimeNow()  - timestart)

                # update datemodification
                if self.dbasetable is not None and 'Objet' in self.dbase.getParentTable(self.dbasetablename):
                    #get pk_objet
                    sql = " SELECT pk_objet FROM " + self.dbasetablename.lower() + "_qgis "
                    sql += " WHERE pk_" + self.dbasetablename.lower() + "=" + str(self.currentFeaturePK)
                    pkobjet = self.dbase.query(sql)[0][0]

                    datemodif = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    sql = "UPDATE Objet SET datetimemodification = '" + datemodif + "'  WHERE pk_objet = " + str(pkobjet) + ";"
                    self.dbase.query(sql)
                    self.dbase.commit()



                # then reload with saved attributes
                if self.savingnewfeature or self.savingnewfeatureVersion :
                    self.loadFeaturesinTreeWdg()
                    if debug: logging.getLogger('Lamia').debug('new feat loadFeaturesinTreeWdg  %.3f', self.dbase.getTimeNow()  - timestart)
                    if self.comboBox_featurelist.count() > 1:
                        #get id
                        sql = "SELECT id_" + self.dbasetablename.lower() + " FROM " + self.dbasetablename.lower() + "_qgis"
                        sql += " WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
                        newfeatureid = self.dbase.query(sql)[0][0]
                        indexnewfeature = self.comboBox_featurelist.findText(str(newfeatureid))
                        self.comboBox_featurelist.setCurrentIndex(indexnewfeature)
                        self.comboBox_featurelist.currentIndexChanged.emit(indexnewfeature)
                    else:
                        self.comboBox_featurelist.currentIndexChanged.emit(0)
                else:
                    self.initFeatureProperties(self.currentFeature)
                    self.postInitFeatureProperties(self.currentFeature)

                if showsavemessage:
                    self.windowdialog.normalMessage('Objet sauvegarde : ' + str(self.currentFeature.attributes()))

                if debug: logging.getLogger('Lamia').debug('wait for repaint  %.3f', self.dbase.getTimeNow()  - timestart)

                self.dbasetable['layerqgis'].triggerRepaint()

                if debug: logging.getLogger('Lamia').debug('end time  %.3f', self.dbase.getTimeNow()  - timestart)

                # *************************
                # reinit things
                if self.rubberBand is not None:
                    self.rubberBand.reset(self.dbasetable['layer'].geometryType())
                self.tempgeometry = None
                self.savingnewfeature = False
                self.savingnewfeatureVersion = False
                # self.currentFeatureChanged.emit()
                self.canvas.freeze(False)
                self.canvas.refresh()
                self.dbasetable['layerqgis'].triggerRepaint()


            elif os.path.isfile(self.dbasetablename):
                values = []
                for elem in self.linkuserwdg[self.dbasetablename]:
                    values.append(elem.text())

                if self.currentFeature is None:
                    self.dbasefiledata.append(values)
                    self.savingnewfeature = True
                    self.currentFeature = [len(self.dbasefiledata)] + values
                else:
                    currentFeatureid = self.currentFeature[0]
                    self.dbasefiledata[currentFeatureid] = values
                    self.currentFeature = [self.currentFeature[0]] + values

                filedbase = open(self.dbasetablename, "w")
                for i, path in enumerate(self.dbasefiledata):
                    filedbase.write(';'.join(self.dbasefiledata[i]) + '\n')

                filedbase.close()

                # then reload with saved attributes
                if self.savingnewfeature:
                    self.loadFeaturesinTreeWdg()
                    if self.comboBox_featurelist.count() > 1:
                        self.comboBox_featurelist.setCurrentIndex(self.comboBox_featurelist.count() - 1)
                    else:
                        self.comboBox_featurelist.currentIndexChanged.emit(0)
                else:
                    self.initFeatureProperties(self.currentFeature)
                    self.postInitFeatureProperties(self.currentFeature)

                if showsavemessage:
                    self.windowdialog.normalMessage('Objet sauvegarde : ' + str(self.currentFeature))
                self.savingnewfeature = False
                self.currentFeatureChanged.emit()
                self.canvas.freeze(False)
                self.canvas.refresh()



        def manageFeatureCreationOrUpdate(self):
            """
            Called by saveFeature - Manage versioning

            """

            currentFeature = None


            if self.currentFeaturePK is not None :

                sql = "SELECT lpk_revision_begin FROM " + self.dbasetablename + "_qgis"
                sql += " WHERE pk_" + self.dbasetablename.lower() + ' = ' + str(self.currentFeaturePK)
                result = self.dbase.query(sql)
                featlastrevision = self.dbase.query(sql)[0][0]

                if featlastrevision != self.dbase.getLatestVersion():   #new version feature
                    # assign revisionend to old version feature
                    if 'Objet' in self.dbase.getParentTable(self.dbasetablename):
                        #getpkobjet
                        sql = "SELECT pk_objet FROM " + self.dbasetablename + "_qgis"
                        sql += " WHERE pk_" + self.dbasetablename.lower()  + " = " + str(self.currentFeaturePK)
                        pk_objet = self.dbase.query(sql)[0][0]

                        datemodif = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                        sql = "UPDATE Objet SET lpk_revision_end = " + str(self.dbase.maxrevision)
                        sql += " , datetimemodification = '" + str(datemodif) + "'"
                        sql += " WHERE pk_objet = " + str(pk_objet)
                        self.dbase.query(sql)
                        self.dbase.commit()

                        # create new feat from oldfeat
                        currentFeature = qgis.core.QgsFeature(self.currentFeature.fields())
                        if self.currentFeature.geometry() is not None:
                            currentFeature.setGeometry(self.currentFeature.geometry())
                        # currentFeature['pk_' + self.dbasetablename.lower()] = 0
                        currentFeaturePK = None

                        self.savingnewfeatureVersion = True
                else:       #simple feature update
                    currentFeature = self.currentFeature
                    currentFeaturePK = self.currentFeature.id()

            else:           # feature creation
                currentFeature = self.currentFeature
                currentFeaturePK = self.currentFeature.id()

            return currentFeature, currentFeaturePK



        def manageGeomOfLinkedFeat(self):
            """
            Manage linked geom between parent table and chidl table
            linkage eom is defined by self.linkedgeom variable

            """

            if self.linkedgeom is not None:
                for tablename,linkedfield  in self.linkedgeom:

                    sourcevalue = self.dbase.getValuesFromPk(self.dbasetablename + '_qgis',
                                                            str("id_" + linkedfield.split('_')[1]),
                                                            self.currentFeaturePK)
                    sql = "SELECT pk_" + tablename.lower() + ", id_" + tablename.lower()
                    sql += " FROM " + tablename + "_qgis "
                    sql += " WHERE " + linkedfield + " = " + str(sourcevalue)
                    sql += " AND "
                    sql += self.dbase.dateVersionConstraintSQL()
                    result = self.dbase.query(sql)

                    # for fetid in result:
                    for fetpk, fetid in result:
                        sourcegeomtext = self.dbase.getValuesFromPk(self.dbasetablename + '_qgis',
                                                                ['ST_AsText(geom)'],
                                                                    self.currentFeaturePK)
                        targetgeomtext = self.dbase.getValuesFromPk(tablename + '_qgis',
                                                                ['ST_AsText(geom)'],
                                                                    fetpk)
                        sourceqgsgeom = qgis.core.QgsGeometry.fromWkt(sourcegeomtext)
                        targetqgsgeom = qgis.core.QgsGeometry.fromWkt(targetgeomtext)

                        #test if nexw geom needed
                        targetgeomtext = None
                        if sourceqgsgeom.type() == 0:
                            sourceval = sourceqgsgeom.asPoint()
                            if targetqgsgeom.type() == 0:
                                targetval = targetqgsgeom.asPoint()
                                targetgeomtext = sourcegeomtext
                            elif targetqgsgeom.type() == 1:
                                targetval = targetqgsgeom.asPolyline()[0]
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    newgeom = qgis.core.QgsGeometry.fromPolyline([sourceqgsgeom.asPoint(), sourceqgsgeom.asPoint()])
                                    targetgeomtext = newgeom.exportToWkt()
                                else:
                                    newgeom = qgis.core.QgsGeometry.fromPolylineXY([sourceqgsgeom.asPoint(), sourceqgsgeom.asPoint()])
                                    targetgeomtext = newgeom.asWkt()
                        elif sourceqgsgeom.type() == 1:
                            sourceval = sourceqgsgeom.asPolyline()[0]
                            if targetqgsgeom.type() == 0:
                                targetval = targetqgsgeom.asPoint()
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    newgeom = qgis.core.QgsGeometry.fromPolyline([sourceqgsgeom.asPoint(), sourceqgsgeom.asPoint()])
                                    targetgeomtext = newgeom.exportToWkt()
                                else:
                                    newgeom = qgis.core.QgsGeometry.fromPolylineXY([sourceqgsgeom.asPoint(), sourceqgsgeom.asPoint()])
                                    targetgeomtext = newgeom.asWkt()
                            elif targetqgsgeom.type() == 1:
                                targetval = targetqgsgeom.asPolyline()[0]
                                targetgeomtext = sourcegeomtext

                        if not self.dbase.areNodesEquals(sourceval, targetval) and targetgeomtext:
                            self.dbase.createNewLineVersion(tablename, fetpk)
                            desfeature = self.dbase.getLayerFeatureById(tablename, fetid)
                            #newgeom
                            sql = self.dbase.createSetValueSentence(type='UPDATE',
                                                                    tablename=tablename,
                                                                    listoffields=['geom'],
                                                                    listofrawvalues=[targetgeomtext])
                            sql += " WHERE pk_" + tablename.lower() + " = " + str(desfeature.id())
                            self.dbase.query(sql)



        def manageLinkedDesorder(self):


            if self.linkeddisorder is not None:

                if self.savingnewfeature and self.savingnewfeatureVersion == False:
                    # categorie
                    # sql = "SELECT Categorie FROM Equipement WHERE pk_equipement = " + str(self.currentFeaturePK)
                    categ = None
                    if self.linkeddisorder['specificfield'] is not None:
                        sql = "SELECT " + self.linkeddisorder['specificfield']
                        sql += " FROM " + self.dbasetablename
                        sql += " WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
                        categ = self.dbase.query(sql)[0][0]
                        # print('categ', categ)
                    # if categ == 'OUH':
                    if categ == self.linkeddisorder['specificfieldvalue'] :
                        pkobjet = self.dbase.createNewObjet()
                        lastiddesordre = self.dbase.getLastId('Desordre') + 1
                        geomtext, iddessys = self.dbase.getValuesFromPk(self.dbasetablename + '_qgis',
                                                                        ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                                        self.currentFeaturePK)

                        if self.dbasetable['geom'] == 'POINT':
                            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext)
                            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                newgeom = qgis.core.QgsGeometry.fromPolyline([qgsgeom.asPoint(), qgsgeom.asPoint()])
                                geomtext = newgeom.exportToWkt()
                            else:
                                newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
                                geomtext = newgeom.asWkt()

                        sql = self.dbase.createSetValueSentence(type='INSERT',
                                                                tablename='Desordre',
                                                                listoffields=['id_desordre', 'lpk_objet',
                                                                            'groupedesordre',
                                                                            'lid_descriptionsystem', 'geom'],
                                                                listofrawvalues=[lastiddesordre, pkobjet,
                                                                                self.linkeddisorder['groupedesordre'],
                                                                                iddessys, geomtext])
                        self.dbase.query(sql)


                else:
                    # move related desordre
                    categ = None
                    if self.linkeddisorder['specificfield'] is not None:
                        categ, iddessys = self.dbase.getValuesFromPk(self.dbasetablename + '_qgis',
                                                                    [self.linkeddisorder['specificfield'], 'id_descriptionsystem'],
                                                                    self.currentFeaturePK)
                    else:
                        iddessys = self.dbase.getValuesFromPk(self.dbasetablename + '_qgis',
                                                                    [ 'id_descriptionsystem'],
                                                                    self.currentFeaturePK)

                    if categ == self.linkeddisorder['specificfieldvalue'] and iddessys is not None:

                        sql = "SELECT id_desordre FROM Desordre_qgis WHERE lid_descriptionsystem = " + str(iddessys)
                        sqlres = self.dbase.query(sql)
                        if sqlres:
                            iddes = sqlres[0][0]
                            desfeature = self.dbase.getLayerFeatureById('Desordre', iddes)
                            # revibegin
                            desgeomtext = self.dbase.getValuesFromPk('Desordre_qgis',
                                                                    ['ST_AsText(geom)'],
                                                                    desfeature.id())
                            equipgeomtext = self.dbase.getValuesFromPk(self.dbasetablename + '_qgis',
                                                                    ['ST_AsText(geom)'],
                                                                    self.currentFeaturePK)

                            if self.dbasetable['geom'] == 'POINT':
                                qgsgeom = qgis.core.QgsGeometry.fromWkt(equipgeomtext)
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    newgeom = qgis.core.QgsGeometry.fromPolyline([qgsgeom.asPoint(), qgsgeom.asPoint()])
                                    equipgeomtext = newgeom.exportToWkt()
                                else:
                                    # newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPointXY(), qgsgeom.asPointXY()])
                                    newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
                                    equipgeomtext = newgeom.asWkt()

                            if equipgeomtext != desgeomtext:
                                self.dbase.createNewLineVersion('Desordre', desfeature.id())
                                desfeature = self.dbase.getLayerFeatureById('Desordre', iddes)

                                sql = self.dbase.createSetValueSentence(type='UPDATE',
                                                                        tablename='Desordre',
                                                                        listoffields=['geom'],
                                                                        listofrawvalues=[equipgeomtext])
                                sql += " WHERE pk_desordre = " + str(desfeature.id())
                                self.dbase.query(sql)





        def setGeometryToFeature(self):

            """
            Methode pour assigner le self.tempgeometry au self.currenfeature
            cree le self.currenfeature si besoin

            """

            # geometry conversion first
            if (self.tempgeometry is not None and self.dbasetable['geom'] in ['POINT', 'LINESTRING', 'POLYGON']
                    and self.tempgeometry.isMultipart()):
                success = self.tempgeometry.convertToSingleType()
            elif (self.tempgeometry is not None and self.dbasetable['geom'] in ['MULTIPOLYGON']
                    and not self.tempgeometry.isMultipart()):
                success = self.tempgeometry.convertToMultiType()

            if (self.dbasetable is not None and 'geom' in self.dbasetable.keys() and self.dbasetable['geom'] == 'LINESTRING'
                and self.tempgeometry is not None and self.tempgeometry.type() == 0): # case point in linestring layer
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    self.tempgeometry = qgis.core.QgsGeometry.fromPolyline([self.tempgeometry.asPoint(),
                                                                            self.tempgeometry.asPoint()])
                else:
                    self.tempgeometry = qgis.core.QgsGeometry.fromPolylineXY([self.tempgeometry.asPoint(),
                                                                            self.tempgeometry.asPoint()])

            #remove duplicate from linestring
            if True:
                if self.tempgeometry is not None and self.dbasetable['geom'] in [ 'LINESTRING'] :
                    if sys.version_info.major == 3:
                        geomaspoly  = self.tempgeometry.asPolyline()
                        geomfinal = [geomaspoly[0]]
                        if not self.dbase.areNodesEquals(geomaspoly[0], geomaspoly[-1]):
                            for index in range(len(geomaspoly) -1 ):
                                if not self.dbase.areNodesEquals(geomaspoly[index], geomaspoly[index +1] ):
                                    geomfinal.append(geomaspoly[index +1])
                        self.tempgeometry = qgis.core.QgsGeometry.fromPolylineXY(geomfinal)


            if self.dbasetable is not None:

                if self.currentFeature is None:
                    self.currentFeature = qgis.core.QgsFeature(self.dbasetable['layer'].fields())

                    if self.tempgeometry is not None:
                        self.currentFeature.setGeometry(self.tempgeometry)
                        pass
                    else:
                        """
                        if ('geom' in self.dbasetable.keys()  
                                and (self.groupBox_geom.parent() is not None or self.groupBox_geom.isVisible()
                                    or self.frame_editing.isVisible())):
                        """
                        if ('geom' in self.dbasetable.keys()
                                and (self.frame_editing.isVisible() and self.groupBox_geom.isVisible() and self.groupBox_geom.parent() )
                                and ((hasattr(self,'CHECKGEOM') and self.CHECKGEOM == True) or not hasattr(self,'CHECKGEOM'))):
                            self.windowdialog.errorMessage('Pas de geometrie selectionnee !!')
                            self.currentFeature = None
                            self.canvas.freeze(False)
                            return False

                    self.savingnewfeature = True
                else:
                    if self.tempgeometry is not None:
                        self.currentFeature.setGeometry(self.tempgeometry)
                        pass
            
            
            return True


        def updateParentFeature(self):
            """
            Method called by saveFeature
            Update the parent tables and manage versioning

            """

            #setlastid
            sql = "SELECT id_" + self.dbasetablename.lower()
            sql += " FROM " + self.dbasetablename.lower()
            sql += " WHERE pk_" + self.dbasetablename.lower()  + " = " + str(self.beforesavingFeaturePK)
            lastid = self.dbase.query(sql)[0][0]


            sql = " UPDATE " + self.dbasetablename.lower()
            sql += " SET id_" + self.dbasetablename.lower() + " = " + str(lastid)
            sql += " WHERE pk_" + self.dbasetablename.lower()  + " = " + str(self.currentFeaturePK)
            self.dbase.query(sql)

            tables = [self.dbasetablename] + self.dbase.getParentTable(self.dbasetablename)
            for table in tables:
                sql = "SELECT pk_" + str(table).lower() + "  FROM " + str(self.dbasetablename).lower() + "_qgis"
                sql += " WHERE pk_" + str(self.dbasetablename.lower()) + " = " + str(self.beforesavingFeaturePK)
                pkoldtable = self.dbase.query(sql)[0][0]

                sql = "SELECT pk_" + str(table).lower() + "  FROM " + str(self.dbasetablename).lower() + "_qgis"
                sql += " WHERE pk_" + str(self.dbasetablename.lower()) + " = " + str(self.currentFeaturePK)
                pknewtable = self.dbase.query(sql)[0][0]

                sql = "SELECT * FROM " + str(table)
                sql += " WHERE pk_" + str(table).lower() + " = " + str(pkoldtable)
                result = self.dbase.query(sql)[0]

                fieldslist = self.dbase.getColumns(table)
                #update sql
                sql = "UPDATE "+ str(table).lower()  + " SET "

                for i, field in enumerate(fieldslist):
                    if 'pk_' in field or 'geom' in field :
                        continue

                    resulttemp = 'NULL'
                    if isinstance(result[i ], str) or isinstance(result[i ], unicode):
                        resulttemp = "'" + result[i ] + "'"
                    elif result[i ] is None:
                        resulttemp = 'NULL'
                    else:
                        # print(type(result[i+1]))
                        resulttemp = str(result[i ])

                    sql += str(field) + " = " + resulttemp + ','

                sql = sql[:-1]  #remove last ,
                sql += " WHERE pk_" + str(table) + " = " + str(pknewtable)

                self.dbase.query(sql)

                if table == 'Objet':
                    sql = "UPDATE Objet SET lpk_revision_begin = " + str(self.dbase.maxrevision) + ","
                    sql += " lpk_revision_end = NULL WHERE pk_objet = " + str(pknewtable)
                    self.dbase.query(sql)



        def saveQGisFeature(self, table, feat):
            """
            Method called by saveFeature

            Save the edited QgsFeature

            :param table: the edited table
            :param feat:  the edited QgsFeature
            :return:    the saved QgsFeature with geometry
            """

            debug = False

            dbasetablelayer = self.dbase.dbasetables[table]['layer']

            if debug: logging.getLogger("Lamia").debug('start : %s %s %s %s',
                                                    table, str(feat.id()) , feat.attributes(), feat.geometry())

            dbasetablelayer.startEditing()

            if feat.id() == 0:  # new feature
                success = dbasetablelayer.addFeature(feat)
            else:
                success = dbasetablelayer.updateFeature(feat)

            self.addedFeatureid = None
            dbasetablelayer.raiseError.connect(self.windowdialog.errorMessage)
            dbasetablelayer.featureAdded.connect(self.getFeatureAddedId)
            dbasetablelayer.commitChanges()
            dbasetablelayer.rollBack()
            dbasetablelayer.raiseError.disconnect(self.windowdialog.errorMessage)
            dbasetablelayer.featureAdded.disconnect(self.getFeatureAddedId)

            if debug: logging.getLogger("Lamia").debug('table, feat.id addedfeatureid : %s %s %s', table, str(feat.id()), str(self.addedFeatureid))

            if self.addedFeatureid is not None:
                return self.dbase.getLayerFeatureByPk(table, self.addedFeatureid)
            else:
                return self.dbase.getLayerFeatureByPk(table, feat.id())


        def saveFeatureProperties(self):
            """
            Method called by saveFeature

            Method for saving feature properties of the ui in the tables
            """

            debug = False


            self.dbasetable['layer'].startEditing()

            if self.dbase.visualmode in [0, 1]:
                if self.linkuserwdg is not None:
                    for i, tablename in enumerate(self.linkuserwdg.keys()):
                        if debug: logging.getLogger("Lamia").debug('start : %s', tablename)
                        featpk = self.currentFeaturePK
                        fieldnames = self.linkuserwdg[tablename]['widgets'].keys()
                        if len(fieldnames) == 0:
                            continue
                        result = []
                        for fieldname in fieldnames:
                            fieldvaluetosave = self.getValueFromWidget(self.linkuserwdg[tablename]['widgets'][fieldname],
                                                                    tablename,
                                                                    fieldname)
                            if fieldvaluetosave is not None:
                                result.append(fieldvaluetosave)
                            else:
                                result.append(None)
                        #tablepk
                        sql = "SELECT pk_" + str(tablename).lower() + " FROM " + str(self.dbasetablename).lower() + "_qgis"
                        sql += "  WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
                        tablepk = self.dbase.query(sql)[0][0]

                        # update sql
                        sql = "UPDATE " + str(tablename).lower() + " SET "
                        for i, field in enumerate(fieldnames):
                            if isinstance(result[i], str) or isinstance(result[i], unicode) :
                                if result[i] != '':
                                    resultstring = result[i]
                                    if "'" in resultstring:
                                        resultstring = "''".join(resultstring.split("'"))
                                    resulttemp = "'" + resultstring + "'"
                                else:
                                    resulttemp = 'NULL'
                            elif result[i ] is None:
                                resulttemp = 'NULL'
                            else:
                                # print(type(result[i ]))
                                resulttemp = str(result[i ])

                            sql += str(field) + " = " + resulttemp + ','

                        sql = sql[:-1]  # remove last ,

                        sql += " WHERE pk_" + str(tablename) + " = " + str(tablepk)
                        self.dbase.query(sql)

                # lidchoosers
                for lidchooser in self.lamiawidgets:
                    lidchooser.saveProperties()



            if self.dbase.visualmode == 2:
                if self.linkuserwdg is None:
                    templinkuserwgd = {self.dbasetablename: {'linkfield': 'ID','widgets': {}}}
                else:
                    templinkuserwgd = self.linkuserwdg

                listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]

                for i, tablename in enumerate(templinkuserwgd.keys()):
                    dbasetable = self.dbase.dbasetables[tablename]
                    result = []
                    for j, field in enumerate(dbasetable['fields'].keys()):
                        itemindex = listfieldname.index(tablename + '.' + field)
                        fieldvaluetosave = self.getValueFromWidget(self.tableWidget.cellWidget(itemindex, 1),
                                                                tablename,
                                                                field)
                        if fieldvaluetosave is not None:
                            result.append(fieldvaluetosave)
                        else:
                            result.append(None)

                    #tablepk
                    sql = "SELECT pk_" + str(tablename).lower() + " FROM " + str(self.dbasetablename).lower() + "_qgis"
                    sql += "  WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
                    tablepk = self.dbase.query(sql)[0][0]

                    # update sql
                    sql = "UPDATE " + str(tablename).lower() + " SET "
                    for i, field in enumerate(dbasetable['fields'].keys()):
                        if field[0:3] in ['pk_', 'id_'] or field[0:4] in ['lpk_']:
                            continue
                        if isinstance(result[i], str):
                            if result[i] != '':
                                resulttemp = "'" + result[i] + "'"
                            else:
                                resulttemp = 'NULL'
                        elif isinstance(result[i], unicode):
                            if result[i] != u'':
                                resulttemp = "'" + result[i] + "'"
                            else:
                                resulttemp = 'NULL'
                        elif result[i ] is None:
                            resulttemp = 'NULL'
                        else:
                            resulttemp = str(result[i])
                        sql += str(field) + " = " + resulttemp + ','

                    sql = sql[:-1]  # remove last ,
                    sql += " WHERE pk_" + str(tablename) + " = " + str(tablepk)
                    self.dbase.query(sql)



        def postSaveFeature(self, boolnewfeature):
            """
            Method called by saveFeature

            To be overloaded if special actions have to be done after raw savin of the feature

            :param boolnewfeature: if it s a new feature
            """
            pass


        def getValueFromWidget(self, wdg, tablename, fieldname):
            """
            Method to obtain the savable value of a property widget

            :param wdg: the property widget
            :param tablename: the table name  linked with th widget
            :param fieldname: the field name  linked with th widget
            :return: The value of the widget, in good format for saving
            """

            fieldvaluetosave = None
            if 'Cst' in self.dbase.dbasetables[tablename]['fields'][fieldname].keys():
                try:
                    if isinstance(wdg, list):
                        wdg = wdg[0]
                    fieldvaluetosave = self.dbase.getConstraintRawValueFromText(tablename, fieldname, wdg.currentText())
                except Exception as e:
                    print('error getValueFromWidget', tablename, fieldname, e)
                if fieldvaluetosave == '':
                    fieldvaluetosave = None
            else:
                if isinstance(wdg, list):
                    wdg = wdg[0]
                if isinstance(wdg, QSpinBox) and wdg.value() > -1:
                    fieldvaluetosave = int(wdg.value() )
                elif isinstance(wdg, QDoubleSpinBox) and wdg.value() > -1:
                    fieldvaluetosave = float(wdg.value())
                elif isinstance(wdg, QTextEdit) or isinstance(wdg, QTextBrowser):
                    fieldvaluetosave = wdg.toPlainText()
                elif isinstance(wdg, QLineEdit):
                    fieldvaluetosave = wdg.text()
                elif isinstance(wdg, QCheckBox) :
                    value = wdg.checkState()
                    if int(value):
                        fieldvaluetosave = 1
                    else:
                        fieldvaluetosave = 0
                elif isinstance(wdg, QDateEdit) and wdg.findChild(QLineEdit).text() != ' ':
                    fieldvaluetosave = wdg.date().toString('yyyy-MM-dd')
                elif isinstance(wdg, QDateTimeEdit) and wdg.findChild(QLineEdit).text() != ' ':
                    fieldvaluetosave = wdg.dateTime().toString( 'yyyy-MM-dd hh:mm:ss')

            return fieldvaluetosave



        def deleteFeature(self, signalreceiver=None, showmessage=True):
            """
            Method called by cliking on Save Button

            :param signalreceiver: the signal emited by the button
            :param showmessage: show a confirmation dialog or not
            :return:
            """
            
            if self.currentFeaturePK is None:
                return

            if showmessage :
                message = "Supprimer completement l'element (yes) ou l'archiver (no) ? "
                reply = QMessageBox.question(self, "Su",
                                                message,
                                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            else:
                reply = QMessageBox.Yes

            # current version
            sql = "SELECT lpk_revision_begin, pk_objet FROM " + self.dbasetablename.lower() + "_qgis"
            sql += " WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
            lpkrevbegin, pkobjet = self.dbase.query(sql)[0]


            if reply == QMessageBox.Yes:
                if lpkrevbegin == self.dbase.maxrevision:
                    if self.deleteParentFeature():
                        sql = "DELETE FROM  " + self.dbasetablename + " WHERE pk_" + self.dbasetablename + " = " + str(self.currentFeaturePK)
                        self.dbase.query(sql)
                    else:
                        self.windowdialog.errorMessage("pas encore disponible")
                else:
                    datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    sql = "UPDATE Objet SET lpk_revision_end = " + str(self.dbase.maxrevision)
                    sql += " , datetimedestruction = '" + str(datesuppr) + "'"
                    sql += " , datetimemodification = '" + str(datesuppr) + "'"
                    sql += " WHERE pk_objet = " + str(pkobjet)
                    self.dbase.query(sql)


            elif reply == QMessageBox.No:
                sql = "SELECT pk_objet FROM " + self.dbasetablename.lower() + "_qgis"
                sql += " WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
                pkobjet = self.dbase.query(sql)[0][0]
                datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                sql = "UPDATE Objet SET datetimedestruction = '" + datesuppr + "'"
                sql += "  , datetimemodification = '" + datesuppr + "'"
                sql += " WHERE pk_objet = " + str(pkobjet)

                self.dbase.query(sql)

            self.canvas.refresh()
            self.loadChildFeatureinWidget()



        def deleteParentFeature(self):
            """
            Method called by deleteFeature

            To be overloaded if the parents tables need deleting also

            :return: True if method is overloaded, else False
            """

            return False


        def getFeatureAddedId(self,id):
            """
            Simple method to catch he id of the fresh saved qgsfeature

            :param id: the id send by qgis signal
            :return: the QgsFeature id
            """

            self.addedFeatureid = id

        def deselectFeature(self):
            """
            Method called by deselect Button

            """
            self.windowdialog.closeEditFeature()
            #case deepcopy
            self.deepCopyDisconnect()

            if self.currentFeature is not None:
                if self.rubberBand:
                    self.rubberBand.reset(0)
                self.featureSelected(self.currentFeature.id(),True)
            else:
                if self.lastidselected is not None:
                    if self.rubberBand:
                        self.rubberBand.reset(0)
                    if self.parentWidget is None and self.lastidselected is not None:
                        idwidgetindex = self.comboBox_featurelist.findText(str(self.lastidselected))
                        self.comboBox_featurelist.setCurrentIndex(idwidgetindex)
                    else:
                        self.comboBox_featurelist.currentIndexChanged.emit(0)


        def addFeature(self):
            """
            Method called by add Feature Button

            """
            self.featureSelected()


        def addGPSPoint(self):
            """
            Method called by add GPS Point Button

            """
            if self.gpsutil and self.gpsutil.currentpoint is None:
                self.windowdialog.errorMessage('GPS non connecte')
                return

            type = self.dbasetable['layer'].geometryType()
            self.createorresetRubberband(type)
            layerpoint = self.gpsutil.currentpoint

            if type == 0:       # POINT
                self.setTempGeometry([layerpoint],False)

            elif type == 1:      # LINE
                geom = None
                if self.currentFeature is not None:
                    # print(self.currentFeature.geometry())
                    pass
                if self.currentFeature is not None and self.currentFeature.geometry() is not None:
                    geom = self.currentFeature.geometry()
                    geompoly = geom.asPolyline()
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




        def addPoint(self):
            """
            Method called by Add Point Button
            """

            type = self.dbasetable['layer'].geometryType()
            self.createorresetRubberband(type)

            if type == 1:      # LINE
                # get the geometry before editing
                initialgeom = []
                if self.tempgeometry is not None:
                    if sys.version_info.major == 2:
                        if len(self.tempgeometry.asPolyline()) > 0:
                            initialgeom = self.tempgeometry.asPolyline()
                        else:
                            initialgeom = self.tempgeometry.asMultiPolyline()[0]
                    else:
                        if not self.tempgeometry.isMultipart () :
                            initialgeom = self.tempgeometry.asPolyline()
                        else:
                            initialgeom = self.tempgeometry.asMultiPolyline()[0]
                elif self.currentFeature is not None and self.tempgeometry is None:
                    initialgeom = self.currentFeature.geometry().asPolyline()

                mapgeometry = []
                for point in initialgeom:
                    if self.dbase.qgsiface is None and int(str(self.dbase.qgisversion_int)[0:3]) < 220 : #bug for standalone
                        mapgeometry = initialgeom
                    else:
                        mapgeometry.append(self.dbase.xform.transform(point))

                self.captureGeometry(listpointinitialgeometry=mapgeometry, type=1)


        def captureGeometry(self,connectint=0, listpointinitialgeometry=[], type=None):
            """
            Method called when capturing geometry is needed (add/extent point, line, polygon...)
            Launch the capture tool

            :param connectint: Catching widget signal
            :param listpointinitialgeometry: list of geometry to be extended, if new empty list
            :param type: geom type (point, line, polygone)
            """

            source = self.sender()

            if source is not None and source.objectName() != 'pushButton_rajoutPoint':
                listpointinitialgeometry = []

            if type is None:
                if 'Point' in source.objectName():
                    type = 0
                elif 'Line' in source.objectName():
                    type = 1
                elif 'Polygon' in source.objectName():
                    type = 2

            self.createorresetRubberband(type)

            try:
                if type == qgis.core.QgsWkbTypes.PointGeometry:
                    self.currentmaptool = self.mtoolpoint
                elif type == qgis.core.QgsWkbTypes.LineGeometry:
                    self.currentmaptool = self.mtoolline
                elif type == qgis.core.QgsWkbTypes.PolygonGeometry:
                    self.currentmaptool = self.mtoolpolygon
                else:
                    return
            except:
                if type == qgis.core.QGis.Point:
                    self.currentmaptool = self.mtoolpoint
                elif type == qgis.core.QGis.Line:
                    self.currentmaptool = self.mtoolline
                elif type == qgis.core.QGis.Polygon:
                    self.currentmaptool = self.mtoolpolygon
                else:
                    return

            if self.canvas.mapTool() != self.currentmaptool:
                self.canvas.setMapTool(self.currentmaptool)
            self.currentmaptool.stopCapture.connect(self.setTempGeometry)
            self.currentmaptool.mappoints = listpointinitialgeometry
            self.currentmaptool.startCapturing()


        def createorresetRubberband(self,type=0):
            """
            Reset the rubberband

            :param type: geom type
            """
            if self.rubberBand is not None:
                self.rubberBand.reset(type)
            else:
                self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,type)
                self.rubberBand.setWidth(5)
                self.rubberBand.setColor(QtGui.QColor("magenta"))



        def setTempGeometry(self, points, comefromcanvas=True, showinrubberband=True):
            """
            Called when self.currentmaptool has finished capturing

            Assign the geometry to self.tempgeometry

            :param points: the list of points coming from the currentmaptool
            :param comefromcanvas: True if come from canvas (need od reprojection)
            :param showinrubberband: True if the temp geometry will be visible with the rubberband

            """


            debug = False

            if debug: logging.getLogger("Lamia").debug('start points : %s %s', self.dbasetablename, points)

            if self.currentmaptool is not None:
                try:
                    self.currentmaptool.stopCapture.disconnect(self.setTempGeometry)
                except TypeError:
                    pass

            pointsmapcanvas = []
            pointslayer=[]
            if self.capturetype is None:
                type = self.dbasetable['layer'].geometryType()
            else:
                type = self.capturetype

            # case point in line layer
            if len(points)==2 and points[0] == points[1]:
                #self.rubberBand.reset(0)
                self.createorresetRubberband(0)
                type = 0.5
            elif len(points) == 1 and self.dbasetable['geom'] == 'LINESTRING':
                points.append(points[0])
                self.createorresetRubberband(0)
                type = 0.5
            else:
                self.createorresetRubberband(type)

            if debug: logging.getLogger("Lamia").debug('type/point : %s %s', str(type), points)

            if self.dbase.qgsiface is None and int(str(self.dbase.qgisversion_int)[0:3]) < 220: #for stadalone app bug
                for point in points:
                    pointsmapcanvas.append(self.dbase.xform.transform(point))
                pointslayer = points
            else:
                if comefromcanvas:
                    pointsmapcanvas = points
                    for point in points:
                        pointslayer.append(self.dbase.xformreverse.transform(point))
                else:
                    pointslayer = points
                    for point in points:
                        pointsmapcanvas.append(self.dbase.xform.transform(point))

            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                if type == 0:
                    geometryformap = qgis.core.QgsGeometry.fromPoint(pointsmapcanvas[0])
                    geometryforlayer = qgis.core.QgsGeometry.fromPoint(pointslayer[0])
                elif type == 0.5:
                    geometryformap = qgis.core.QgsGeometry.fromPoint(pointsmapcanvas[0])
                    geometryforlayer = qgis.core.QgsGeometry.fromMultiPolyline([pointslayer])
                elif type == 1:
                    geometryformap = qgis.core.QgsGeometry.fromMultiPolyline([pointsmapcanvas])
                    geometryforlayer = qgis.core.QgsGeometry.fromMultiPolyline([pointslayer])
                elif type == 2:
                    geometryformap = qgis.core.QgsGeometry.fromPolygon([pointsmapcanvas])
                    geometryforlayer = qgis.core.QgsGeometry.fromPolygon([pointslayer])
            else:
                if type == 0:
                    geometryformap = qgis.core.QgsGeometry.fromPointXY(pointsmapcanvas[0])
                    geometryforlayer = qgis.core.QgsGeometry.fromPointXY(pointslayer[0])
                elif type == 0.5:
                    geometryformap = qgis.core.QgsGeometry.fromPointXY(pointsmapcanvas[0])
                    geometryforlayer = qgis.core.QgsGeometry.fromMultiPolylineXY([pointslayer])
                elif type == 1:
                    geometryformap = qgis.core.QgsGeometry.fromMultiPolylineXY([pointsmapcanvas])
                    geometryforlayer = qgis.core.QgsGeometry.fromMultiPolylineXY([pointslayer])
                elif type == 2:
                    geometryformap = qgis.core.QgsGeometry.fromPolygonXY([pointsmapcanvas])
                    geometryforlayer = qgis.core.QgsGeometry.fromPolygonXY([pointslayer])

            #outside qgis bug
            if showinrubberband:
                if self.dbase.qgsiface is None and int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    self.rubberBand.addGeometry(geometryforlayer, None)
                else:
                    self.rubberBand.addGeometry(geometryformap, None)

                self.rubberBand.show()
            self.tempgeometry = geometryforlayer
            self.lamiageomChanged.emit()

            if debug: logging.getLogger("Lamia").debug('end layer points : %s', pointslayer)
            if debug: logging.getLogger("Lamia").debug('end canvas points : %s', pointsmapcanvas)
            if debug: logging.getLogger("Lamia").debug('end tempgeom : %s', self.toWKT(self.tempgeometry))

            self.mtool = None




        def pickFeature(self):
            """
            Called by button of pro interface for picking a feature


            """
            self.pointEmitter.canvasClicked.connect(self.selectPickedFeature)
            self.canvas.setMapTool(self.pointEmitter)


        def selectPickedFeature(self, point, button=None):
            """
            Method of pro interface

            :param point:
            :param button:
            :return:
            """

            if self.pickfield is not None:
                distance = None
                nearestid = None
                layernearist = None
                for layername in self.pickTable[self.pickfield].keys():
                    nearid, dist = self.dbase.dbasetables[layername]['widget'].getNearestId(point)
                    if distance is None:
                        layernearist = layername
                        distance = dist
                        nearestid = nearid
                    elif dist < distance:
                        layernearist = layername
                        distance = dist
                        nearestid = nearid
                layer = self.dbase.dbasetables[layernearist]['layer']
                idtoget = self.pickTable[self.pickfield][layernearist]
                # nearestfeature = layer.getFeatures(qgis.core.QgsFeatureRequest(nearestid)).next()
                nearestfeature = self.dbase.getLayerFeatureById(layernearist, nearestid)
                nearattributevalue = nearestfeature[idtoget]
                if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
                    layer.setSelectedFeatures([nearestfeature.id()])
                else:
                    layer.selectByIds([nearestfeature.id()])
                self.initFeatureProperties(self.currentFeature,
                                        tablename=self.dbasetablename,
                                        fieldname=self.pickfield,
                                        value=nearattributevalue)
                self.pickfield = None
                self.canvas.unsetMapTool(self.pointEmitter)
                try:
                    self.pointEmitter.canvasClicked.disconnect(self.selectPickedFeature)
                except:
                    pass

            else:
                # not used yet
                nearestid = self.getNearestId(point)
                if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
                    layer.setSelectedFeatures([nearestid])
                else:
                    layer.selectByIds([nearestid])
                self.pickspinbox.setValue(nearestid)

                self.canvas.unsetMapTool(self.pointEmitter)
                try:
                    self.pointEmitter.canvasClicked.disconnect(self.selectPickedFeature)
                except:
                    pass
                self.picklayername = None
                self.pickspinbox = None



        def zoomToFeature(self,fid=None):
            """
            Called by zoom to Button

            :param fid: the id of feature we want to zoom to
            :return:
            """

            if fid is None:
                feat = self.currentFeature
            else:
                pk = self.getPkFromId(self.dbasetablename,fid)
                feat = self.dbase.getLayerFeatureByPk(self.dbasetablename,pk )
            # point2 = xform.transform(feat.geometry().centroid().asPoint())

            if feat.geometry().centroid() is not None and not feat.geometry().centroid().isNull():
                point2 = self.dbase.xform.transform(feat.geometry().centroid().asPoint())
            else:
                print(feat.geometry().asWkt())
                if sys.version_info.major == 2:
                    point2 = self.dbase.xform.transform(feat.geometry().vertexAt(0) )
                elif sys.version_info.major == 3:
                    point2 = self.dbase.xform.transform(qgis.core.QgsPointXY(feat.geometry().vertexAt(0)))
                    # print('**', point2)
            self.canvas.setCenter(point2)
            self.canvas.refresh()



        def saveRessourceFile(self):
            """
            Called by saveFeature
            If ressource file is not in the dbase directory, save it in the dbase directory

            """
            # get date
            sql = "SELECT datetimecreation FROM " + self.dbasetablename.lower() + "_qgis"
            sql += " WHERE pk_"+ self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
            query = self.dbase.query(sql)
            result = [row[0] for row in query]

            if len(result) > 0:
                # date = result[0]
                datevalue = datetime.datetime.strptime(str(result[0]), "%Y-%m-%d %H:%M:%S").date()
                # print(result[0], datevalue, type(result[0]), isinstance(datevalue, datetime.date))
                if isinstance(datevalue, datetime.date):
                    datevalue = datevalue.strftime('%Y-%m-%d')
            else:
                return

            date = ''.join(datevalue.split('-'))

            sql = "SELECT pk_ressource, id_ressource, file FROM " + self.dbasetablename.lower() + "_qgis"
            sql += " WHERE pk_"+ self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
            query = self.dbase.query(sql)
            result = [row[0:3] for row in query]
            if len(result) > 0:
                pkressource, idressource, file = result[0]
            else:
                return

            if int(str(self.dbase.qgisversion_int)[0:3]) < 220 and isinstance(file, QtCore.QPyNullVariant):
                file = None

            if file is not None and len(file) > 0:
                if file[0] == '.':
                    file = os.path.join(self.dbase.dbaseressourcesdirectory,file)
                else:
                    if os.path.isfile(file):
                        filename = os.path.basename(file)
                        filename = str(idressource) + '_' + filename
                        destinationdir = os.path.join(self.dbase.dbaseressourcesdirectory,self.dbasetablename,date)
                        destinationfile = os.path.join(destinationdir, filename)

                        self.dbase.copyRessourceFile(fromfile= file,
                                                    tofile=destinationfile,
                                                    withthumbnail=0,
                                                    copywholedirforraster=False)


                        finalname = os.path.join('.',os.path.relpath(destinationfile, self.dbase.dbaseressourcesdirectory ))
                        sql = "UPDATE Ressource SET file = '" + finalname + "' WHERE pk_ressource = " +  str(pkressource) + ";"
                        query = self.dbase.query(sql)

                        if self.beforesavingFeature is not None:
                            sql = "SELECT file FROM Ressource  WHERE pk_ressource = " + str(pkressource) + ";"
                            query = self.dbase.query(sql)
                            result = [row[0] for row in query]
                            oldfile = result[0]
                        else:
                            oldfile = ''

                        newfile = finalname

                        if os.path.isfile(self.dbase.completePathOfFile(oldfile)) and oldfile != newfile:
                            os.remove(self.dbase.completePathOfFile(oldfile))
                        else:
                            pass




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



        def copyAtributes(self):
            """
            Copy he atributes of the ui in self.templinkuserwdg

            :return: self.templinkuserwdg
            """

            self.templinkuserwdg = {}

            for tablename in self.linkuserwdg.keys():
                for field in self.linkuserwdg[tablename]['widgets'].keys():
                    if field in ['X', 'Y', 'Z', 'dX', 'dY', 'dZ']:
                        continue

                    wdg = self.linkuserwdg[tablename]['widgets'][field]
                    if isinstance(wdg, QComboBox):
                        self.templinkuserwdg[wdg] = wdg.currentIndex()
                    elif isinstance(wdg, QSpinBox) or isinstance(wdg, QDoubleSpinBox):
                        self.templinkuserwdg[wdg] = wdg.value()
                    elif isinstance(wdg, QTextEdit) or isinstance(wdg, QTextBrowser):
                        self.templinkuserwdg[wdg] = wdg.toPlainText()
                    elif isinstance(wdg, QLineEdit):
                        self.templinkuserwdg[wdg] = wdg.text()
                    elif isinstance(wdg, QCheckBox) :
                        self.templinkuserwdg[wdg] = wdg.checkState()
                    elif isinstance(wdg, QDateEdit) :
                        self.templinkuserwdg[wdg] = wdg.date()
                    elif isinstance(wdg, QDateTimeEdit):
                        self.templinkuserwdg[wdg] = wdg.dateTime()

            return self.templinkuserwdg


        def pasteAtributes(self, signalclick=None, dicttopaste=None):
            """
            Paste atributes saved in self.templinkuserwdg

            :param signalclick: catch emitter signal
            :param dicttopaste: the dictionnary to paste

            """
            if dicttopaste is None:
                dicttopaste = self.templinkuserwdg
                
            
            if dicttopaste is not None:
                for tablename in self.linkuserwdg.keys():
                    for field in self.linkuserwdg[tablename]['widgets'].keys():
                        wdg = self.linkuserwdg[tablename]['widgets'][field]
                        print(dicttopaste)
                        if wdg not in list(dicttopaste.keys()):
                            continue
                        if isinstance(wdg, QComboBox):
                            wdg.setCurrentIndex(dicttopaste[wdg])
                        elif isinstance(wdg, QSpinBox) or isinstance(wdg, QDoubleSpinBox):
                            wdg.setValue(dicttopaste[wdg])
                        elif isinstance(wdg, QTextEdit) or isinstance(wdg, QTextBrowser):
                            wdg.setText(dicttopaste[wdg])
                        elif isinstance(wdg, QLineEdit):
                            wdg.setText(dicttopaste[wdg])
                        elif isinstance(wdg, QCheckBox) :
                            wdg.setCheckState(dicttopaste[wdg])
                        elif isinstance(wdg, QDateEdit) :
                            wdg.setDate(dicttopaste[wdg])
                        elif isinstance(wdg, QDateTimeEdit):
                            wdg.setDateTime(dicttopaste[wdg])


        def goToFeaturePressed(self):
            """
            Called on gotofeature Button pressed
            Show featue in rubberband

            """

            if self.currentFeature is not None:
                self.zoomToFeature()

                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    selectedfeatureids = self.dbasetable['layer'].selectedFeaturesIds()
                else:
                    selectedfeatureids = self.dbasetable['layer'].selectedFeatureIds()

                if not self.currentFeature.id() in selectedfeatureids:
                    type = self.dbasetable['layer'].geometryType()
                    geom = qgis.core.QgsGeometry(self.currentFeature.geometry())
                    if type == 1 and ((len(geom.asPolyline()) == 2 and geom.asPolyline()[0] == geom.asPolyline()[1])
                                        or len(geom.asPolyline()) == 1):
                        #case when point stored in polyline
                        type = 0
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            geom = qgis.core.QgsGeometry.fromPoint(geom.asPolyline()[0])
                        else:
                            geom = qgis.core.QgsGeometry.fromPointXY(geom.asPolyline()[0])
                    if self.rubberBandBlink is not None:
                        self.rubberBandBlink.reset(type)
                    else:
                        self.rubberBandBlink = qgis.gui.QgsRubberBand(self.canvas, type)
                    self.rubberBandBlink.setWidth(5)
                    self.rubberBandBlink.setColor(QtGui.QColor("magenta"))
                    success = geom.transform(self.dbase.xform)
                    self.rubberBandBlink.addGeometry(geom, None)
                    self.rubberBandBlink.show()
                    self.canvas.refresh()



        def goToFeatureReleased(self):
            """
            Called on gotofeature Button released
            Reset ruberband

            """
            if self.rubberBandBlink is not None:
                type = self.dbasetable['layer'].geometryType()
                self.rubberBandBlink.reset(type)



        def displayGPS(self, active):
            """
            Called on GPs connection
            Print GPS things in widgets defined by self.gpswidget

            :param active: True ig a NMEA sentence is received in less than 5 s, else False

            """
            if active:
                if self.gpswidget is not None:
                    for key in self.gpswidget.keys():
                        if self.gpswidget[key]['widget'] is not None:
                            self.gpswidget[key]['widget'].setEnabled(True)
                    self.gpsutil.ggasentence.connect(self.displayGGA)
                    self.gpsutil.gstsentence.connect(self.displayGST)
                self.pushButton_rajoutPointGPS.setEnabled(True)
            else:
                self.pushButton_rajoutPointGPS.setEnabled(False)
                if self.gpswidget is not None:
                    try:
                        self.gpsutil.ggasentence.disconnect(self.displayGGA)
                    except:
                        pass
                    try:
                        self.gpsutil.gstsentence.disconnect(self.displayGST)
                    except:
                        pass
                    for key in self.gpswidget.keys():
                        if self.gpswidget[key]['widget'] is not None:
                            self.gpswidget[key]['widget'].setText('/')
                            self.gpswidget[key]['widget'].setEnabled(False)



        def displayGGA(self, dictgga):
            """
            Called by displayGPS

            :param dictgga: the dict where widgets to display gga are defined
            """
            for key in self.gpswidget.keys():
                if 'gga' in self.gpswidget[key].keys() and self.gpswidget[key]['widget'] is not None:
                    if dictgga[self.gpswidget[key]['gga']] is not None:
                        try:
                            self.gpswidget[key]['widget'].setText(str(round(dictgga[self.gpswidget[key]['gga']], 2)))
                        except KeyError:
                            pass
                    else:
                        self.gpswidget[key]['widget'].setText('/')


        def displayGST(self, dictgst):
            """
            Called by displayGPS

            :param dictgst: the dict where widgets to display gst are defined
            """
            for key in self.gpswidget.keys():
                if 'gst' in self.gpswidget[key].keys() and self.gpswidget[key]['widget'] is not None:
                    if dictgst[self.gpswidget[key]['gst']] is not None:
                        self.gpswidget[key]['widget'].setText(str(round(dictgst[self.gpswidget[key]['gst']],2)))
                    else:
                        self.gpswidget[key]['widget'].setText('/')



        def getPkFromId(self, layername, inputid):
            """
            Method to get pk of feature by id

            :param layername:
            :param inputid:
            :return:
            """

            sql = "SELECT pk_" + str(layername).lower() + " FROM " + str(layername).lower() + "_qgis "
            sql += "WHERE id_" + str(layername).lower() + " = " + str(inputid)
            sql += " AND "
            sql += self.dbase.dateVersionConstraintSQL()

            pk = self.dbase.query(sql)[0][0]

            return pk


        def getDBaseChildWidget(self,keywidget):
            wdg = self.dbasechildwdg[keywidget]

            if isinstance(wdg,list) and len(wdg)>0:
                return wdg[self.dbasechildwdg[keywidget][1]]
            elif not isinstance(wdg,list) and wdg is not None:
                return wdg
            else:
                return None


        def themechanged(self,iconwidth):
            """
            Change icon width - activated by windowswidget

            :param iconwidth: the icon width we want
            """

            if isinstance(iconwidth, int):
                newsize = QtCore.QSize(iconwidth, iconwidth)
            elif isinstance(iconwidth, QtCore.QSize):
                newsize = iconwidth
            newsizeicon = QtCore.QSize(newsize)
            newsizeicon.scale(newsize.width() * 0.8, newsize.width() * 0.8, QtCore.Qt.KeepAspectRatio)

            butttons = self.findChildren(QPushButton)
            for button in butttons:
                # print('button', button.icon())
                if button.icon() is not None:
                    button.setIconSize(newsizeicon)
                    button.setBaseSize(newsize)
                    button.setFixedSize(newsize)
            butttons = self.findChildren(QToolButton)
            for button in butttons:
                if button.icon() is not None:
                    button.setIconSize(newsizeicon)
                    button.setBaseSize(newsize)
                    button.setFixedSize(newsize)

            for wdg in self.dbasechildwdg:
                wdg.themechanged(iconwidth)

        def toWKT(self, geom):
            """
            convenient method working for qgis 2 and 3

            :param geom: the QgsGeometry
            :return: the wkt
            """
            returnstr = ''
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                returnstr = geom.exportToWkt()
            else:
                returnstr = geom.asWkt()

            return returnstr

        def deepCopy(self):
            """
            Called by deep copy Button

            """
            self.deepCopySave()

            tempsender = self.sender()

            if tempsender == self.pushButton_deepcopy :
                self.deepCopyLoad()
            elif tempsender == self.pushButton_deepcopyselect :
                currentpk = self.currentFeaturePK
                self.capturetype = 2
                self.captureGeometry(type=2)
                self.lamiageomChanged.connect(self.deepcopymultipleselection)


        def deepcopymultipleselection(self):
            """
            Called by deepCopy

            copy to multiple objects

            """
            try:
                self.lamiageomChanged.disconnect(self.deepcopymultipleselection)
            except:
                pass
            self.capturetype = None

            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                geomtext = self.tempgeometry.exportToWkt()
            else:
                geomtext = self.tempgeometry.asWkt()

            self.tempgeometry = None
            currentid = self.dbase.getValuesFromPk(self.dbasetablename, 'id_' + self.dbasetablename.lower(),self.currentFeaturePK)

            sql = "SELECT id_" + self.dbasetablename.lower() + " FROM " + self.dbasetablename
            sql += " WHERE ST_WITHIN(ST_MakeValid(geom), ST_GeomFromText('" + geomtext + "',"+str(self.dbase.crsnumber) + "))"
            ressql = self.dbase.query(sql)
            if len(ressql)>0 :
                res = [elem[0] for elem in ressql]

                for feat_id in res :
                    if feat_id != currentid :
                        idselected = feat_id
                        self.deepCopyLoad(parentIdtocopyinto=idselected)

            self.createorresetRubberband(2)
            self.featureSelected(item=currentid, itemisid=True)
            self.dbasetable['layerqgis'].triggerRepaint()


        def deepCopySave(self, signalclik=None, table=None,deepcopydict=None,parentwidg=None):
            """
            Save properties of the copied feature


            :param signalclik: catch emitter signal
            :param table:
            :param deepcopydict:
            :param parentwidg:
            :return:
            """

            debug = False
            if debug: print('**** deepCopy ****', table,deepcopydict,parentwidg  )

            if table is None:
                self.deepcopydict = {}
                self.deepcopydict[self.dbasetablename] = [{'pk': None, 'attributes':None, 'childs': {}}]
                self.deepcopydict[self.dbasetablename][-1]['pk'] = self.currentFeaturePK
                self.deepcopydict[self.dbasetablename][-1]['attributes'] = self.copyAtributes()

                self.deepCopySave(table=self.deepcopy, deepcopydict=self.deepcopydict[self.dbasetablename][-1]['childs'],parentwidg=self)


            elif isinstance(table, list) and len(table) >0 and isinstance(table[0],list):
                for elemlist in table:
                    self.deepCopySave(table=elemlist, deepcopydict=deepcopydict, parentwidg=parentwidg)

            else:
                currentable = table[0]

                for tempwdg in parentwidg.dbasechildwdg:
                    if tempwdg.dbasetablename == currentable:
                        ids = [elem[0] for elem in tempwdg.treefeatlist]
                        deepcopydict[currentable] =  []
                        for id in ids:
                            tempwdg.featureSelected(item=id, itemisid=True)
                            deepcopydict[currentable].append({'pk': None, 'attributes':None, 'childs': {}})
                            deepcopydict[currentable][-1]['attributes'] = tempwdg.copyAtributes()

                            if isinstance(table,list) and len(table)>1:
                                self.deepCopySave(table=table[1:], deepcopydict=deepcopydict[currentable][-1]['childs'],parentwidg=tempwdg)




            if debug and table is None:
                pprint.pprint( self.deepcopydict)



        def deepCopyLoad(self, deepcopydict=None, parentwdg=None,parentIdtocopyinto=None):

            debug = False
            debugsavedelete=False

            if debug :
                if deepcopydict :
                    print('deepCopyLoad', deepcopydict.keys(), parentwdg)
                else:
                    print('deepCopyLoad', deepcopydict, parentwdg)


            if deepcopydict is None:

                if parentIdtocopyinto is None:
                    deepcopydict = self.deepcopydict
                    self.featureSelected()
                else:
                    deepcopydict = self.deepcopydict
                    self.featureSelected(item=parentIdtocopyinto, itemisid=True)

                attributes = deepcopydict[self.dbasetablename][0]['attributes']
                self.pasteAtributes(dicttopaste=attributes)

                if debug: pprint.pprint(self.deepcopydict)

                if 'childs' in deepcopydict[self.dbasetablename][0].keys():
                    dicttosend = deepcopydict[self.dbasetablename][0]['childs']
                else:
                    dicttosend = None

                if self.tempgeometry is None and parentIdtocopyinto is None:
                    if debug : print('No geom')
                    self.captureGeometry(type=0)
                    self.currentmaptool.stopCapture.connect(lambda: self.deepCopySaveFeat(self,dicttosend))
                    if debugsavedelete: print('capture', self.dbasetablename, 'dictnone')
                else:
                    if debug: print('geom')
                    self.deepCopySaveFeat(self,dicttosend)


            else:
                for tablename in deepcopydict.keys():
                    for tempwdg in parentwdg.dbasechildwdg:
                        if tempwdg.dbasetablename == tablename:
                            originaltreefeatlist = list(tempwdg.treefeatlist)
                            lastcount = 0
                            for i, elem in enumerate(deepcopydict[tablename]):
                                lastcount = i
                                if 'childs' in elem.keys():
                                    dicttosend = elem['childs']
                                else:
                                    dicttosend = None

                                attributes = deepcopydict[tablename][i]['attributes']

                                if i<len(originaltreefeatlist):
                                    if debug : print('geom already')
                                    tempwdg.featureSelected( item=originaltreefeatlist[i][0], itemisid=True)
                                    tempwdg.pasteAtributes(dicttopaste=attributes)
                                    if debugsavedelete: print('ecrase', tempwdg.dbasetablename, i,len(originaltreefeatlist) )
                                    self.deepCopySaveFeat(tempwdg, dicttosend)
                                else:
                                    tempwdg.featureSelected()
                                    tempwdg.pasteAtributes(dicttopaste=attributes)
                                    if debugsavedelete: print('cree', tempwdg.dbasetablename, i, len(originaltreefeatlist))

                                    if tempwdg.tempgeometry is None and self.dbase.isTableSpatial(tablename):
                                        if debug: print('No geom')
                                        tempwdg.captureGeometry(type=0)
                                        tempwdg.currentmaptool.stopCapture.connect(lambda: self.deepCopySaveFeat(tempwdg, dicttosend))
                                    else:
                                        if debug: print('geom already')
                                        self.deepCopySaveFeat(tempwdg, dicttosend)

                            if lastcount < len(originaltreefeatlist)-1 and parentIdtocopyinto is None:
                                for j in list(range(lastcount+1,len(originaltreefeatlist))):
                                    if debugsavedelete:  print('delete', tempwdg.dbasetablename, j,
                                                                    len(originaltreefeatlist),
                                                                    originaltreefeatlist,
                                                                    originaltreefeatlist[j][0])
                                    tempwdg.featureSelected(item=originaltreefeatlist[j][0], itemisid=True)

                                    tempwdg.deleteFeature(showmessage=False)





        def deepCopySaveFeat(self,currentwdg, deepcopydict):
            try:
                currentwdg.stopCapture.disconnect()
            except:
                pass

            # print('save', currentwdg.dbasetablename, currentwdg.tempgeometry)

            if currentwdg == self:
                currentwdg.saveFeature(showsavemessage=True)
            else:
                currentwdg.saveFeature(showsavemessage=False)

            if deepcopydict is not None and deepcopydict != {}:
                self.deepCopyLoad(deepcopydict=deepcopydict, parentwdg=currentwdg)


        def deepCopyDisconnect(self):
            try:
                self.currentmaptool.stopCapture.disconnect()
            except:
                pass

        def printWidget(self):
            pass

        def tr(self, message):
            return QtCore.QCoreApplication.translate('AbstractLamiaTool', message)

