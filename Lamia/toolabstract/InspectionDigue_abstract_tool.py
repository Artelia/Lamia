# -*- coding: utf-8 -*-

from __future__ import unicode_literals
# from PyQt4 import uic, QtCore, QtGui
from qgis.PyQt import uic, QtCore, QtGui


try:
    from qgis.PyQt.QtGui import (QWidget, QTreeWidgetItem, QMessageBox, QFileDialog, QTableWidget,
                                 QHeaderView, QComboBox, QSpinBox, QPushButton, QDateEdit, QTextEdit,
                                 QDoubleSpinBox, QDialog, QVBoxLayout, QTreeWidget, QLineEdit, QCheckBox,
                                 QLabel, QMessageBox, QTextBrowser, QTableWidgetItem)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QTreeWidgetItem, QMessageBox, QFileDialog, QTableWidget,
                                     QHeaderView, QComboBox, QSpinBox, QPushButton, QDateEdit, QTextEdit,
                                     QDoubleSpinBox, QDialog, QVBoxLayout, QTreeWidget, QLineEdit, QCheckBox,
                                     QLabel, QMessageBox, QTextBrowser, QTableWidgetItem)
import os
import sys
import qgis
import qgis.utils
from ..dialog.InspectionDigue_linkage import LinkageDialog
# from ..maptool.mapTools import mapToolAddFeature, mapToolAddLine, mapToolCapture
from ..maptool.mapTools import mapToolCapture
import shutil
import datetime

import time
import logging
debugtime = False


class AbstractInspectionDigueTool(QWidget):

    saveFeatureSignal = QtCore.pyqtSignal()
    currentFeatureChanged = QtCore.pyqtSignal()

    def __init__(self, dbase=None, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        """
        Abstract class for working on table
        @param dbase : The dbase class linked
        @param dialog : the main dialog widget
        @param linkedtreewidget  : the treewidget it interacts with
        @param parent : the parent widget (TODO : the same as dialog)
        """
        import time
        timestart = time.clock()
        if debugtime: logging.getLogger('Lamia').debug('Start init %.3f', time.clock() - timestart)

        super(AbstractInspectionDigueTool, self).__init__(parent)
        uipath = os.path.join(os.path.dirname(__file__), '..', 'dialog', 'InspectionDigue_propertieswidget.ui')
        uic.loadUi(uipath, self)

        # ***************************************************************
        # ******************   Variables def ****************************
        # ***************************************************************

        # ***** Data base var
        #  the dbaseparser
        self.dbase = dbase
        # the gpsutil
        self.gpsutil = gpsutil
        #  the current widget feature selected in self.linkedtreewidget
        self.currentFeature = None
        self.beforesavingFeature = None
        #  the current feature selected when widget is linked withh a parent feature
        self.currentparentfeature = None    # not used
        #  the FK tables
        self.fktables = []
        self.parentWidget = parentwidget
        #  ids to load
        self.idstoload = None
        self.dbasetablename = None
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
        self.dbtablename = None
        #  iconpath -  can be implemented
        self.iconpath = None
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
        # show only inside feature mapcanvas  in linkedtreewidget
        self.windowsonlyfeature = 0
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
        #  The main qfiledialog
        self.qfiledlg = QFileDialog()
        #  tablewidget - expert widget
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        header = self.tableWidget.horizontalHeader()
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            header.setResizeMode(1, QHeaderView.Stretch)
            header.setResizeMode(0, QHeaderView.ResizeToContents)
        else:
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

        # ***** QGis var
        #  qgis map canvas
        self.canvas = self.windowdialog.canvas
        if False:
            if self.windowdialog is not None:
                self.canvas = self.windowdialog.canvas
            elif self.parentWidget is not None:
                self.canvas = self.parentWidget.canvas
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
        self.pointEmitter = qgis.gui.QgsMapToolEmitPoint(self.canvas)   # maptoolused for picking
        self.currentmaptool = None      # qgsmaptoolcapture used for capturing
        self.visualmode = [0, 1, 2]

        # *******************************************************
        # raw connection

        # *******************************************************
        # load tools - must be kept in this order
        if debugtime: logging.getLogger('Lamia').debug('before initTool %.3f', time.clock() - timestart)
        self.initTool()
        if debugtime: logging.getLogger('Lamia').debug('After initTool %.3f', time.clock() - timestart)

        # *******************************************************
        # Post inittool things



        if self.dbasetablename is not None :
            self.pushButton_savefeature.clicked.connect(self.saveFeature)
            self.pushButton_addFeature.clicked.connect(self.addFeature)
            self.pushButton_delFeature.clicked.connect(self.deleteFeature)
            if self.dbasetablename in self.dbase.dbasetables.keys():
                self.dbasetable = self.dbase.dbasetables[self.dbasetablename]
            self.changePropertiesWidget()
            # connect signals of inherited widget
            if self.windowdialog is not None:
                self.windowdialog.MaintreeWidget.currentItemChanged.connect(self.onActivationRaw)
        """
        # widget connection
        if self.userwdgfield is not None:
            self.userwdg = self.userwdgfield
            self.linkuserwdg = self.linkuserwdgfield
        if self.dbasechildwdgfield is not None:
            self.dbasechildwdg = self.dbasechildwdgfield
        """


        if self.dbasetablename is not None:
            self.initWidgets()


        """
        #childwdg change
        if True:
            for childwdg in self.dbasechildwdg:
                self.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)
        """

        if debugtime: logging.getLogger('Lamia').debug('end init %.3f', time.clock() - timestart)


    # ******************************************************************************************************************
    # **********************************    Init methods        ********************************************************
    # ******************************************************************************************************************

    def initTool(self):
        """!
        Abstract method - must be implemented
        Load widget and icons and init things
        must contain :
            self.setupUi(self)
            self.iconpath = '...path to icon...'
        """
        pass

    def initFieldUI(self):
        pass

    def initDesktopUI(self):
        self.initFieldUI()

    # ******************************************************************************************************************
    # **********************************    on dbase loaded   methods        *******************************************
    # ******************************************************************************************************************

    def magicFunction(self):
        pass

    def changePropertiesWidget(self):
        """
        Function called when visual mode is changed
        """

        # clear groupBox_properties
        if self.groupBox_properties.layout().count() > 0:
            self.groupBox_properties.layout().itemAt(0).widget().setParent(None)

        # disconnect currentFeatureChanged signal to dbasechildwdg
        for childwdg in self.dbasechildwdg:
            try:
                self.currentFeatureChanged.disconnect(childwdg.loadChildFeatureinWidget)
            except:
                pass

        # load propoer widget
        if self.dbase.visualmode in [0, 1, 4]:
            # define self.userwdg, self.linkuserwdg and self.dbasechildwdg
            if self.dbase.visualmode == 0:
                self.initFieldUI()
                if self.userwdgfield is not None:
                    self.userwdg = self.userwdgfield
                    self.linkuserwdg = self.linkuserwdgfield
                if self.dbasechildwdgfield is not None:
                    self.dbasechildwdg = self.dbasechildwdgfield
            elif self.dbase.visualmode in [1,4]:
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
            # load userwdg
            if self.userwdg is not None:
                self.groupBox_properties.layout().addWidget(self.userwdg)

        elif self.dbase.visualmode == 2:
            self.groupBox_properties.layout().addWidget(self.tableWidget)

        # reconnect currentFeatureChanged signal to dbasechildwdg
        for childwdg in self.dbasechildwdg:
            self.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)

        # dbasechildwdg change
        for childwdg in self.dbasechildwdg:
            childwdg.changePropertiesWidget()

        # load the widgets in main tree
        if self.dbase.visualmode in self.visualmode:
            self.loadWidgetinMainTree()
        else:
            self.unloadWidgetinMainTree()

        # reload state (feature selected before changes)
        if self.linkedtreewidget is not None:
            tempitem = self.linkedtreewidget.currentItem()
            if tempitem is not None and self.windowdialog.MaintreeWidget.currentItem() == self.qtreewidgetitem:
                tempitemid = int(tempitem.text(0))
                self.onActivationRaw(self.windowdialog.MaintreeWidget.currentItem())
                self.comboBox_featurelist.setCurrentIndex(self.comboBox_featurelist.findText(str(tempitemid)))

    def loadWidgetinMainTree(self):
        """
        Called on the widget creation in windowsdialog
        DO:
        load the widget in the main stacked widget
        call onActivationRaw when qtreewidgetitem is clicked in MaintreeWidget
        """

        # add qtreewidget item in MaintreeWidget
        if self.windowdialog is not None and self.parentWidget is None:
            arb = [self.CAT, self.NAME]
            if self.qtreewidgetitem is None:
                self.qtreewidgetitem = QTreeWidgetItem()
                self.qtreewidgetitem.setText(0, arb[-1])
                self.qtreewidgetitem.setFlags(self.qtreewidgetitem.flags() | QtCore.Qt.ItemIsUserCheckable)
                self.qtreewidgetitem.setCheckState(0, QtCore.Qt.Unchecked)
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
            # print('unload', self.dbasetablename, wdgitem.text(0))
            wdgitem.removeChild(self.qtreewidgetitem)
            self.disconnectIdsGui()


    def initWidgets(self):
        """
        Init default table
            1
            when field contain 'Id...' : add show button
            when field contain 'Lk...' : add Pick button
            when field contain 'File...' : add File button
            2
            when field is integer : put spinbox
            when filed is text:
                when filed is 'Date...." : put qdateedit
                when constrained filed : put combo
                else : put textedit
        Init widget geometry buttons
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
                    # item.setFlags()

                    self.tableWidget.setItem(rowPosition, 0, item)
                    if 'Cst' in dbasetable['fields'][field].keys():
                        wdg = QComboBox()
                        wdg.addItems([description[0] for description in dbasetable['fields'][field]['Cst']])
                        if False:
                            if sys.version_info.major == 2:
                                wdg.addItems([str(description[0].encode('utf-8')) for description in dbasetable['fields'][field]['Cst']])
                            elif sys.version_info.major == 3:
                                wdg.addItems([description[0] for description in dbasetable['fields'][field]['Cst']])
                        self.tableWidget.setCellWidget(rowPosition, 1, wdg)

                        linkuserwdglist = []
                        if self.linkuserwdgfield is not None or self.linkuserwdgdesktop is not None:
                            if self.linkuserwdgfield is not None :
                                linkuserwdglist.append(self.linkuserwdgfield)
                            if self.linkuserwdgdesktop is not None:
                                linkuserwdglist.append(self.linkuserwdgdesktop)
                        elif self.linkuserwdg is not None:
                            #else :
                            linkuserwdglist.append(self.linkuserwdg)

                        for linkuserwdg in linkuserwdglist:
                            if (tablename in linkuserwdg.keys()
                                    and field in linkuserwdg[tablename]['widgets'].keys()
                                    and isinstance(linkuserwdg[tablename]['widgets'][field],QComboBox)):
                                # if linkuserwdg[] is not None and field in linkuserwdg.keys():
                                templist = [description[0] for description in dbasetable['fields'][field]['Cst']]
                                if False:
                                    if sys.version_info.major == 2:
                                        templist = [str(description[0].encode('utf-8')) for description in dbasetable['fields'][field]['Cst']]
                                    elif sys.version_info.major == 3:
                                        templist = [description[0] for description in dbasetable['fields'][field]['Cst']]
                                linkuserwdg[tablename]['widgets'][field].addItems(templist)

                            if 'ParFldCst' in dbasetable['fields'][field].keys():
                                # listfieldname = [fieldname for fieldname in dbasetable['fields'].keys()]
                                listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
                                #print(dbasetable['fields'])
                                #print(listfieldname)
                                # print(tablename + '.' + dbasetable['fields'][field]['ParFldCst'])
                                indexparentfield = listfieldname.index(tablename + '.' + dbasetable['fields'][field]['ParFldCst'])
                                nameparenttalbe, nameparentfield = listfieldname[indexparentfield].split('.')
                                # print('indexparentfield', indexparentfield)
                                comboparent = self.tableWidget.cellWidget(indexparentfield, 1)
                                # print('okok',comboparent.objectName() )
                                try:
                                    comboparent.currentIndexChanged.connect(self.comboparentValueChanged)
                                    if False:
                                        if isinstance(comboparent, QComboBox):
                                            comboparent.currentIndexChanged.connect(self.comboparentValueChanged)
                                        elif  isinstance(comboparent, QSpinBox):
                                            comboparent.valueChanged.connect(self.comboparentValueChanged)
                                except Exception as e:
                                    if self.dbase.qgsiface is None:
                                        logging.getLogger("Lamia").debug('error %s %s %s', e, tablename, field)
                                # userwidget
                                if (tablename in linkuserwdg.keys() and 'widgets' in linkuserwdg[tablename].keys()
                                        and nameparentfield in linkuserwdg[tablename]['widgets'].keys()
                                        and isinstance(linkuserwdg[tablename]['widgets'][nameparentfield], QComboBox)):
                                    linkuserwdg[tablename]['widgets'][nameparentfield].currentIndexChanged.connect(self.comboparentValueChanged)

                    elif 'INTEGER' in dbasetable['fields'][field]['SLtype']:
                        if field[0:2].lower() == 'id':
                            item = QTableWidgetItem()
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                            self.tableWidget.setItem(rowPosition, 1, item)
                        else:
                            wdg = QSpinBox()
                            wdg.setRange(-1, 9999999)
                            self.tableWidget.setCellWidget(rowPosition, 1, wdg)
                        if 'Lk' in field[0:2]:
                            wdg2 = QPushButton('Pick')
                            self.tableWidget.setCellWidget(rowPosition, 2, wdg2)
                            wdg2.clicked.connect(self.rawtablePushButtonClicked)
                        if 'Id' in field[0:2] and len(field) > 2:
                            wdg2 = QPushButton('Show')
                            self.tableWidget.setCellWidget(rowPosition, 2, wdg2)
                            wdg2.clicked.connect(self.rawtablePushButtonClicked)
                    elif 'TEXT' in dbasetable['fields'][field]['SLtype']:
                        if 'date' in field[0:4]:
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
                    elif 'REAL' in dbasetable['fields'][field]['SLtype']:
                        wdg = QDoubleSpinBox()
                        wdg.setRange(-1, 9999999)
                        self.tableWidget.setCellWidget(rowPosition, 1, wdg)

                    if 'FK' in dbasetable['fields'][field].keys():
                        # print(dbasetable['fields'][field]['FK'].split('(')[0])
                        self.fktables.append(dbasetable['fields'][field]['FK'].split('(')[0])

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
            if False:
                self.cadwdg = qgis.gui.QgsAdvancedDigitizingDockWidget(self.canvas)
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    self.mtoolpoint = mapToolCapture(self.canvas, self.cadwdg,
                                                     qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint)
                    self.mtoolline = mapToolCapture(self.canvas, self.cadwdg,
                                                    qgis.gui.QgsMapToolAdvancedDigitizing.CaptureLine)
                    self.mtoolpolygon = mapToolCapture(self.canvas, self.cadwdg,
                                                       qgis.gui.QgsMapToolAdvancedDigitizing.CapturePolygon)
                else:
                    self.mtoolpoint = mapToolCapture(self.canvas, self.cadwdg,
                                                     qgis.gui. QgsMapToolCapture.CapturePoint)
                    self.mtoolline = mapToolCapture(self.canvas, self.cadwdg,
                                                    qgis.gui. QgsMapToolCapture.CaptureLine)
                    self.mtoolpolygon = mapToolCapture(self.canvas, self.cadwdg,
                                                       qgis.gui. QgsMapToolCapture.CapturePolygon)
            if True:
                if self.windowdialog is not None:
                    self.mtoolpoint = self.windowdialog.mtoolpoint
                    self.mtoolline = self.windowdialog.mtoolline
                    self.mtoolpolygon = self.windowdialog.mtoolpolygon


        else:
            self.groupBox_geom.setParent(None)
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


    def manageLinkage(self):
        self.currentid = self.currentFeature.id()
        self.dlg_linkage = LinkageDialog(self)
        self.dlg_linkage.setWindowModality(2)
        self.dlg_linkage.exec_()
        self.loadFeaturesinTreeWdg()
        idwidgetindex = self.comboBox_featurelist.findText(str(self.currentid))
        # print('rawtablePushButtonClicked',idwidgetindex)
        if idwidgetindex >= 0:
            self.disconnectIdsGui()
            self.comboBox_featurelist.setCurrentIndex(idwidgetindex)
            self.connectIdsGui()
            self.comboBox_featurelist.currentIndexChanged.emit(idwidgetindex)


    def initLinkageFromGeometry(self, linkagekey, idsourcevalue=None):

        idslink = []
        linkagetemp = self.linkagespec[linkagekey]

        if idsourcevalue is None:
            idsourcevalue = self.currentFeature[linkagetemp['idsource']]

        sql = "DELETE FROM " + linkagetemp['tabletc']
        sql += " WHERE  " + linkagetemp['idtcsource'] + " =  " + str(idsourcevalue) + ";"
        # print(sql)
        self.dbase.query(sql)
        # self.dbase.commit()

        for table in self.linkagespec[linkagekey]['desttable']:
            sql = "SELECT " + table + "." + linkagetemp['iddest']  +" FROM " + table + "," + self.dbasetablename
            sql += " WHERE ST_Within(ST_MakeValid(" + table + ".geom),ST_MakeValid(" + self.dbasetablename + ".geom))"
            sql += " AND " + self.dbasetablename + '.id_' + self.dbasetablename.lower() + ' = ' + str(self.currentFeature.id()) + ";"
            # print(sql)
            query = self.dbase.query(sql)
            if len(query) > 0:
                idstemp = [row[0] for row in query]
                idslink += idstemp
        # print('idslink')
        for id in idslink:
            sql = "INSERT INTO " + linkagetemp['tabletc']
            sql += "(" + linkagetemp['idtcsource'] + "," + linkagetemp['idtcdest'] + ") "
            sql += "VALUES(" + str(idsourcevalue) + "," + str(id) + ");"
            # print('linkgeom',sql)
            self.dbase.query(sql)
            # self.dbase.commit()


    def rawtablePushButtonClicked(self):
        """!
        Raw table click manager
        """
        senderwdg = self.sender()
        # index = self.tableWidget.indexAt(senderwdg.pos())
        ind = self.tableWidget.indexAt(senderwdg.pos()).row()
        tablename, fieldname = self.tableWidget.item(ind, 0).text().split('.')
        # fieldname = self.tableWidget.item(ind, 0).text()

        if senderwdg.text() == 'File':
            file, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', None,
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
            # print('*************************** ' + str(FKtable))
            if 'widget' in self.dbase.dbasetables[FKtable].keys():
                wdg = self.dbase.dbasetables[FKtable]['widget']
                wdg.setParent(None)
                if True:
                    self.disconnectIdsGui()
                    wdg.disconnectIdsGui()
                    # wdg.comboBox_featurelist
                    wdg.featureSelected(idrequested, True)

                    # wdg.loadFeaturesinTreeWdg(notintreeview = True)

                    # wdg.connectIdsGui()
                    if False:
                        # print('rawtablePushButtonClicked', str(idrequested))
                        idwidgetindex = wdg.comboBox_featurelist.findText(str(idrequested))
                        # print('rawtablePushButtonClicked',idwidgetindex)
                        wdg.comboBox_featurelist.setCurrentIndex(idwidgetindex)
                        # wdg.featureSelected(idwidgetindex)
                        # wdg.featureSelected(idrequested)
                    self.connectIdsGui()
                self.dialog = QDialog()
                vboxlayout = QVBoxLayout()
                vboxlayout.addWidget(wdg)
                self.dialog.setLayout(vboxlayout)

                self.dialog.show()
                # dialog._exec()
            # print(qtreewdgitem.row(),qtreewdgitem.column())

    def comboparentValueChanged(self, index):
        """!
        manage constrained combobox
        """
        # table
        senderwdg = self.sender()
        if isinstance(senderwdg, QComboBox) and senderwdg.count() == 0: #case triple descendant and parent not filled
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



        # print(parenttablename, parentfieldname, senderwdg,senderwdg.currentText() )
        try:
            parentcstvalue = self.dbase.getConstraintRawValueFromText(parenttablename, parentfieldname, senderwdg.currentText())
        except Exception as e:
            if self.dbase.qgsiface is None:
                logging.getLogger("Lamia").debug('error %s %s %s', e, parenttablename, parentfieldname)
            return
        if False:
            if isinstance(senderwdg, QComboBox):
                parentcstvalue = self.dbase.getConstraintRawValueFromText(parenttablename, parentfieldname, senderwdg.currentText())
            elif isinstance(senderwdg, QSpinBox):
                parentcstvalue = self.dbase.getConstraintRawValueFromText(parenttablename, parentfieldname,senderwdg.value())

        dbasetable = self.dbase.dbasetables[parenttablename]
        # get child index and combochild
        listparentcst = [dbasetable['fields'][field]['ParFldCst']
                         if 'ParFldCst' in dbasetable['fields'][field].keys() else None
                         for field in dbasetable['fields'].keys()]


        if False:   # only python 2
            childfieldnames = [dbasetable['fields'].keys()[i] for i in range(len(listparentcst))
                               if parentfieldname == listparentcst[i]]
        else:
            childfieldnames = [list(dbasetable['fields'].keys())[i] for i in range(len(listparentcst))
                               if parentfieldname == listparentcst[i]]


        if comefromrawtable:
            listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
            for childfieldname in childfieldnames:
                if dbasetable['fields'][parentfieldname]['SLtype'] == 'INTEGER' and parentcstvalue != '' and parentcstvalue is not None:
                    parentcstvalue = int(parentcstvalue)
                listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if parentcstvalue in value[2]]
                if False:
                    if sys.version_info.major == 2:
                        listtoadd = [str(value[0].encode('utf-8')) for value in dbasetable['fields'][childfieldname]['Cst'] if
                                     parentcstvalue in value[2]]
                    elif sys.version_info.major == 3:
                        listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if
                                     parentcstvalue in value[2]]
                indexchildintable = listfieldname.index(parenttablename + '.' + childfieldname)
                combochild = self.tableWidget.cellWidget(indexchildintable, 1)
                combochild.clear()
                if len(listtoadd) > 0:
                    combochild.addItems(listtoadd)
        else:
            for childfieldname in childfieldnames:

                if dbasetable['fields'][parentfieldname]['SLtype'] == 'INTEGER' and parentcstvalue != '' and parentcstvalue is not None:
                    parentcstvalue = int(parentcstvalue)
                listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if parentcstvalue in value[2]]
                if False:
                    if sys.version_info.major == 2:
                        listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if parentcstvalue in value[2]]
                        # print(listtoadd)
                    elif sys.version_info.major == 3:
                        listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if parentcstvalue in value[2]]
                combochild = self.linkuserwdg[parenttablename]['widgets'][childfieldname]
                combochild.clear()
                if len(listtoadd) > 0:
                    combochild.addItems(listtoadd)

    # *******************************************************************************************************************
    # **********************************    on activation/des methods        *******************************************
    # ******************************************************************************************************************

    def onActivationRaw(self, param1, param2=None):
        """
        Mangage the activation of tool when tool's icon is clicked on main tree widget
        Do:
        display tool widget
        load features in ElemtreeWidget
        connect ElemtreeWidget click to featureSelected
        TODO : display or not the layer
        """
        debug = False
        # if debug: logging.getLogger("Lamia").debug('start')

        if isinstance(param1, QTreeWidgetItem) and (isinstance(param2, QTreeWidgetItem) or param2 is None):    # signal from treeWidget_utils
            # if debug: logging.getLogger("Lamia").debug('step 1 %s %s, %s', param1.text(0),param1 == self.qtreewidgetitem, param2)

            if param2 == self.qtreewidgetitem:
                self.onDesactivationRaw()
                self.postOnDesactivation()

            if param1 == self.qtreewidgetitem :
                if debug: logging.getLogger("Lamia").debug('step 2 %s %s', param1.text(0), param2)
                # manage display in canvas
                self._checkLayerVisibility()

                # add child widget
                self.loadChildWidgets()

                # manage widget display
                if self.windowdialog is not None :
                    if self.dbasetable is not None:
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
                        self.comboBox_featurelist.currentIndexChanged.emit(0)
                    else:
                        self.initFeatureProperties(None)

                #change active layer in canvas
                if qgis.utils.iface is not None and self.dbasetable is not None and self.dbasetable['showinqgis']:
                    qgis.utils.iface.setActiveLayer(self.dbasetable['layerqgis'])

                # Specific method
                self.postOnActivation()

    def loadChildWidgets(self):
        if True:  # TODO
            self.windowdialog.tabWidget_childs.clear()
            # childwdg change
            if True:
                for childwdg in self.dbasechildwdg:
                    if childwdg.NAME is not None:
                        self.windowdialog.tabWidget_childs.addTab(childwdg, childwdg.NAME)
            else:
                for childwdgname in self.dbasechildwdg.keys():
                    chldwdg = self.getDBaseChildWidget(childwdgname)
                    # print(chldwdg)
                    if chldwdg and childwdg.NAME:
                        self.windowdialog.tabWidget_childs.addTab(chldwdg,
                                                                  chldwdg.NAME)

    def postOnActivation(self):
        """!
        Abstract method - must be implemented
        called by onActivationRaw
        """
        pass

    def onDesactivationRaw(self):
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

        # disconnection
        try:
            self.linkedtreewidget.currentItemChanged.disconnect(self.featureSelected)
        except:
            pass




    def postOnDesactivation(self):
        """!
        Abstract method - must be implemented
        called by onDesactivationRaw
        """
        pass
        # simplewidget

    """
    def _getConstraintRawValueFromText(self, table, field, txt):
        # print('_getConstraintRawValueFromText',[value[0] for value in self.dbasetable['fields'][field]['Cst']], txt )
        dbasetable = self.dbase.dbasetables[table]
        index = [value[0] for value in dbasetable['fields'][field]['Cst']].index(txt)
        return dbasetable['fields'][field]['Cst'][index][1]


    def _getConstraintTextFromRawValue(self, table, field, rawvalue):
        # print('_getConstraintTextFromRawValue',self.dbasetablename, self.dbasetable['fields'][field], rawvalue,field)
        dbasetable = self.dbase.dbasetables[table]
        index = [value[1] for value in dbasetable['fields'][field]['Cst']].index(rawvalue)
        return dbasetable['fields'][field]['Cst'][index][0]
    """


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
        pass

        """
        debug = False
        if debug: logging.getLogger("Lamia").debug('Start %s',self.dbasetablename)

        self.loadFeaturesinTreeWdg()

        if (self.comboBox_featurelist.count() > 0 and self.comboBox_featurelist.itemText(0) != ''):
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
                self.setEnabled(False)
            else:
                self.setEnabled(True)
        self.currentFeatureChanged.emit()



    def loadFeaturesinTreeWdg(self):
        """!
        load features in self.linkedtreewidget
        called whenever the list need to be reinitialized (ex : click in maintreewidget,...)
        """
        debug = False
        self.disconnectIdsGui()

        if debug: logging.getLogger("Lamia").debug('Start %s %s', self.dbasetablename,self.parentWidget)

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
            for i in range(lenheaderlist):
                header.setResizeMode(i, QHeaderView.ResizeToContents)
            header.setResizeMode(lenheaderlist-1, QHeaderView.Stretch)
            parentitem = self.linkedtreewidget.invisibleRootItem()
        elif (self.parentWidget is not None and self.parentWidget.linkedtreewidget is not None
                and self.parentWidget.currentFeature is not None):
            root = self.parentWidget.linkedtreewidget.invisibleRootItem()
            indexchild = [root.child(i).text(0) for i in range(root.childCount())].index(str(self.parentWidget.dbasetablename))
            tempitem = root.child(indexchild)
            indexchild = [tempitem.child(i).text(0) for i in range(tempitem.childCount())].index(str(self.parentWidget.currentFeature.id()))
            parentitem = tempitem.child(indexchild)

        # selection of particular feature to load (if parentfeature, or window only mode)
        ids = self.loadIds()

        # creation de la liste des elements qui figurent dans le linkedtreewidget
        lenqtreewidg = len(self.qtreewidgetfields) + 1
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

        # enable/disable le widget selon que des ids ont ete trouves
        # print('load',self.dbasetablename,[str(elem[0]) for elem in self.treefeatlist] )

        if len(self.treefeatlist) > 0:
            self.groupBox_properties.setEnabled(True)
            self.groupBox_geom.setEnabled(True)
            self.comboBox_featurelist.addItems([str(elem[0]) for elem in self.treefeatlist])
        else:
            self.groupBox_properties.setEnabled(False)
            self.groupBox_geom.setEnabled(False)

        self.connectIdsGui()


    def disconnectIdsGui(self):
        """
        pass
        """
        try:
            self.linkedtreewidget.currentItemChanged.disconnect(self.featureSelected)
        except:
            pass
        try:
            self.comboBox_featurelist.currentIndexChanged.disconnect(self.featureSelected)
        except:
            pass


    def connectIdsGui(self):
        """
        pass
        """
        if False:
            if self.linkedtreewidget is not None:
                print('connect', self.dbasetablename, self.linkedtreewidget.objectName())
            else:
                print('connect', self.dbasetablename)

        if self.linkedtreewidget is not None and isinstance(self.linkedtreewidget, QTreeWidget):
            self.linkedtreewidget.currentItemChanged.connect(self.featureSelected)
        self.comboBox_featurelist.currentIndexChanged.connect(self.featureSelected)


    def _clearLinkedTreeWidget(self):
        """
        clear LinkedTreeWidget and linked combobox
        """
        # print('clear')
        if self.linkedtreewidget is not None and isinstance(self.linkedtreewidget, QTreeWidget):
            if False:
                for i in range(self.linkedtreewidget.invisibleRootItem().childCount()):
                    self.linkedtreewidget.invisibleRootItem().removeChild(self.linkedtreewidget.invisibleRootItem().child(0))
            if False:
                for topitemindex in range(self.linkedtreewidget.topLevelItemCount() ):
                    self.linkedtreewidget.takeTopLevelItem(topitemindex)
            if True:
                self.linkedtreewidget.clear()

        self.comboBox_featurelist.clear()

    def loadIds(self):

        ids = []
        if self.dbasetable is not None:
            strid = 'id_' + self.dbasetablename.lower()
            sql = "SELECT " + strid
            if len(self.qtreewidgetfields)>0 :
                sql += "," + ','.join(self.qtreewidgetfields)
            sql += " FROM " + self.dbasetablename + '_qgis'
            sql += ' WHERE datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN datedestruction IS NOT NULL  '
                sql += 'THEN DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN datedestruction IS NOT NULL  '
                sql += 'THEN DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'

            # if self.parentWidget is not None and self.linkagespec is not None and self.parentWidget.dbasetablename in sum([self.linkagespec[key]['desttable'] for key in self.linkagespec.keys()],[]):
            if (self.parentWidget is not None and self.linkagespec is not None
                    and self.parentWidget.currentFeature is not None):
                linkagespeckey = None
                for key in self.linkagespec.keys():
                    if self.parentWidget.dbasetablename in self.linkagespec[key]['desttable']:
                        linkagespeckey = key
                if linkagespeckey is not None:
                    linkagetemp = self.linkagespec[linkagespeckey]
                    if linkagetemp['tabletc'] is None:
                        sql += " AND " + linkagetemp['idsource'] + " = "
                        sql += str(self.parentWidget.currentFeature[linkagetemp['iddest']])
                    else:
                        sqltemp = "SELECT " + linkagetemp['idtcsource'] + " FROM " + linkagetemp['tabletc']
                        sqltemp += " WHERE " + linkagetemp['idtcdest'] + " = "
                        sqltemp += str(self.parentWidget.currentFeature[linkagetemp['iddest']])
                        # print(sqltemp)
                        query = self.dbase.query(sqltemp)
                        if not query == None :
                            idstemp = [str(row[0]) for row in query]
                            idssql = '(' + ','.join(idstemp) + ')'
                            sql += " AND " + linkagetemp['idsource'] + " IN " + idssql
                        else:
                            return ids

            sql = self.postloadIds(sql)

            sql += ';'
            # print('loadIds', sql)
            query = self.dbase.query(sql)
            #ids = [row[0:1] for row in query]
            ids = [row for row in query]

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
        return sqlin

    if False:
        def CheckBoxOnlyvisibleChecked(self, state):
            if self.windowdialog is not None:
                self.windowsonlyfeature = self.windowdialog.checkBox_onlyvisible.checkState()
                if self.windowsonlyfeature == 2:
                    qgis.utils.iface.mapCanvas().extentsChanged.connect(self.loadFeaturesinTreeWdg)
                else:
                    try:
                        qgis.utils.iface.mapCanvas().extentsChanged.disconnect(self.loadFeaturesinTreeWdg)
                    except:
                        pass
                self.loadFeaturesinTreeWdg()

    # *******************************************************************************************************************
    # **********************************    core methods        *******************************************
    # ******************************************************************************************************************

    def featureSelected(self, item=None, itemisid=False):
        """
        Action when a feature is selected somewhere
        @param item : if none, add new feature else show properties of id selected
        """
        debug = False
        if False:
            print('featureSelected',self.dbasetablename, self.sender().objectName(),item)
            if isinstance(item, QTreeWidgetItem ):
                print(item.text(0))


        if debug: logging.getLogger("Lamia").debug('start %s %s %s', self.dbasetablename, type(item), str(itemisid))

        # ************** init thing *********************************
        # remove selection in canvas
        if self.parentWidget is None and self.dbasetable is not None:
            self.dbasetable['layer'].removeSelection()
        # init thing
        self.disconnectIdsGui()
        self.beforesavingFeature = None
        # reinit current feature
        self.currentFeature = None
        # remove new entry if exists
        res = self.comboBox_featurelist.findText(self.newentrytext)
        if res >= 0:
            if self.linkedtreewidget is not None:
                itemintree = self.linkedtreewidget.findItems(self.newentrytext, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 0)[0]
                self.linkedtreewidget.invisibleRootItem().removeChild(itemintree)
            self.comboBox_featurelist.removeItem(self.comboBox_featurelist.count()-1)

        # ************** get id selected and link treewidget and combobox *********************************
        if isinstance(item, QTreeWidgetItem) and item.parent() is not None:
            # print('featsel',item.parent().text(0),self.dbasetablename)
            if item.parent().text(0) == self.dbasetablename:    # treewdgitem has no parent
                id = int(item.text(0))
                if self.windowdialog is not None:
                    self.windowdialog.MaintabWidget.setCurrentIndex(0)
                self.comboBox_featurelist.setCurrentIndex(self.comboBox_featurelist.findText(str(id)))
            elif item.parent().text(0) in [wdg.dbasetablename for wdg in self.dbasechildwdg]:   # treewdgitem has parent : child item
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
                childindex = [wdg.dbasetablename for wdg in self.dbasechildwdg].index(item.text(0))
                if self.windowdialog is not None:
                    self.windowdialog.MaintabWidget.setCurrentIndex(1)
                    self.windowdialog.tabWidget_childs.setCurrentIndex(childindex)
                self.connectIdsGui()
                return
            elif self.dbasetable is None:
                id = int(item.text(0))
            else:
                self.connectIdsGui()
                return
        elif isinstance(item, QTreeWidgetItem) and item.parent() is None:
            try:
                id = int(item.text(0))
            except ValueError:      # item text is not an id
                self.connectIdsGui()
                return
        elif isinstance(item, int) and not itemisid:        #feature selected with combobox
            # print('item', item)
            id = int(self.comboBox_featurelist.itemText(item))
            if self.linkedtreewidget is not None and isinstance(self.linkedtreewidget, QTreeWidget):
                parentitem = self.linkedtreewidget.findItems(self.dbasetablename, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 0)[0]
                indexchild = [parentitem.child(i).text(0) for i in range(parentitem.childCount())].index(str(id))
                itemtodisplay = parentitem.child(indexchild)
                self.linkedtreewidget.setCurrentItem(itemtodisplay)
        elif isinstance(itemisid, bool) and itemisid:
            id = item
        elif isinstance(itemisid, QTreeWidgetItem):
            self.connectIdsGui()
            return
        else:
            id = None

        # **************** gui things when selected ***************************************************************
        if self.dbasetable is not None:                             #widget has dbasetable linked
            if id is not None:        # item clicked in treewidget
                self.currentFeature = self.dbase.getLayerFeatureById(self.dbasetablename, id)
                if self.parentWidget is None:
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
                        self.dbasetable['layerqgis'].setSelectedFeatures([self.currentFeature.id()])
                    else:
                        self.dbasetable['layerqgis']. selectByIds([self.currentFeature.id()])
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
        pass

    def initFeatureProperties(self, feat, tablename=None, fieldname=None, value=None):
        """!
        Load the feature attributes in the widget - feat is None is a new feature and default values are loaded
        @param feat : the feature to be displayed
        """

        # print('initFeatureProperties',self.dbasetablename)

        if self.dbasetable is not None:
            if self.linkuserwdg is None:
                templinkuserwgd = {self.dbasetablename: None}
            else:
                templinkuserwgd = self.linkuserwdg

            listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]

            # print('initFeatureProperties',self.dbasetablename)

            for tablename in templinkuserwgd.keys():
                dbasetable = self.dbase.dbasetables[tablename]
                for i, field in enumerate(dbasetable['fields'].keys()):
                    # raw table
                    itemindex = listfieldname.index(tablename + '.' + field)
                    if fieldname is None or field == fieldname:
                        if feat is not None and value is None:
                            if tablename == self.dbasetablename:
                                workingfeat = feat
                            else:
                                parendid = feat[templinkuserwgd[tablename]['linkfield']]
                                # parentfeat = self.dbase.dbasetables[tablename]['layer'].getFeatures(qgis.core.QgsFeatureRequest(parendid)).next()
                                parentfeat = self.dbase.getLayerFeatureById(tablename, parendid)
                                workingfeat = parentfeat
                            try :
                                valuetoset = workingfeat[field]
                            except Exception as e :
                                print('initFeatureProperties - field ' + str(field) + ' not found')
                                valuetoset = None

                        else:
                            valuetoset = value

                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220 and isinstance(valuetoset, QtCore.QPyNullVariant):
                            valuetoset = None

                        if int(str(self.dbase.qgisversion_int)[0:3]) > 220 and isinstance(valuetoset, QtCore.QVariant):
                            if valuetoset.isNull():
                                valuetoset = None
                            else:
                                valuetoset = valuetoset.value()


                        if self.tableWidget.cellWidget(itemindex, 1) is not None:
                            self.setValueInWidget(self.tableWidget.cellWidget(itemindex, 1), valuetoset, tablename, field)

                            if tablename in templinkuserwgd.keys() and templinkuserwgd[tablename] is not None and 'widgets' in templinkuserwgd[tablename].keys() and field in templinkuserwgd[tablename]['widgets'].keys():
                                self.setValueInWidget(templinkuserwgd[tablename]['widgets'][field], valuetoset, tablename, field)
                        else:
                            if self.tableWidget.item(itemindex, 1) is not None:
                                if valuetoset is None:
                                    self.tableWidget.item(itemindex, 1).setText('')
                                else:
                                    self.tableWidget.item(itemindex, 1).setText(str(valuetoset))

            # current prestation case:
            self.pushButton_savefeature.setEnabled(True)

            if feat is not None and self.linkagespec is not None and 'Marche' in self.linkagespec.keys()  and self.dbase.currentprestationid is not None:
                # search table with lk prestation
                # qgis bug
                if True:
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
                        isspatial = self.dbasetable['layerqgis'].geometryType() < 3
                    else:
                        isspatial = self.dbasetable['layerqgis'].isSpatial()
                    if isspatial:
                        # if self.dbasetable['layerview'].isSpatial():
                        # lk_presta = self.dbasetable['layerview'].getFeatures(qgis.core.QgsFeatureRequest(feat.id())).next()['lk_marche']
                        lk_presta = self.dbase.getLayerFeatureById(self.dbasetablename, feat.id())['lk_marche']
                    else:
                        if True:
                            listfeat = list(self.dbasetable['layerqgis'].getFeatures())
                            featid = [fet.id() for fet in listfeat]
                            index = featid.index(feat.id())
                            lk_presta = listfeat[index]['lk_marche']
                        if False:
                            sql = "SELECT lk_marche FROM Ressource WHERE Ressource.id_ressource = " + str(feat['id_ressource'])
                            query = self.dbase.query(sql)
                            lk_presta = [row[0] for row in query][0]
                else:
                    # lk_presta = self.dbasetable['layerview'].getFeatures(qgis.core.QgsFeatureRequest(feat.id())).next()['lk_marche']
                    lk_presta = self.dbase.getLayerFeatureById(self.dbasetablename, feat.id())['lk_marche']
                if lk_presta != self.dbase.currentprestationid:
                    self.pushButton_savefeature.setEnabled(False)


    def setValueInWidget(self, wdg, valuetoset, table, field):

        """
        if isinstance(feat, qgis.core.QgsFeature):
            valuetoset = feat[field]
        else:
            valuetoset = feat
        """

        # print('setValueInWidget', field,valuetoset , type(valuetoset))

        if isinstance(wdg, QTextEdit) or isinstance(wdg, QLineEdit):
            # if valuetoset is not None and valuetoset is not None and not isinstance(valuetoset, QtCore.QPyNullVariant):
            if valuetoset is not None:
                wdg.setText(valuetoset)
            else:
                wdg.setText('')
        elif isinstance(wdg, QSpinBox) or isinstance(wdg, QDoubleSpinBox):
            # if valuetoset is not None and valuetoset is not None and not isinstance(valuetoset, QtCore.QPyNullVariant):
            try:
                if valuetoset is not None:
                    wdg.setValue(valuetoset)
                else:
                    wdg.setValue(-1)
            except Exception as e:
                if self.dbase.qgsiface is None:
                    logging.getLogger("Lamia").debug('error %s', e)
        elif isinstance(wdg, QComboBox):
            # if valuetoset is not None and valuetoset is not None and not isinstance(valuetoset, QtCore.QPyNullVariant):
            try:
                if valuetoset is not None:
                    # text = self._getConstraintTextFromRawValue(table, field, valuetoset)
                    text = self.dbase.getConstraintTextFromRawValue(table, field, valuetoset)
                    index = wdg.findText(text)
                    wdg.setCurrentIndex(index)
                else:
                    wdg.setCurrentIndex(0)
            except Exception as e:
                if self.dbase.qgsiface is None:
                    logging.getLogger("Lamia").debug('error %s', e)
        elif isinstance(wdg, QDateEdit):
            # if valuetoset is not None and not isinstance(valuetoset, QtCore.QPyNullVariant):
            if valuetoset is not None:
                # self.tableWidget.cellWidget(i, 1).setValue(feat[field])
                if isinstance(valuetoset, str) or isinstance(valuetoset, unicode):
                    wdg.setDate(QtCore.QDate.fromString(valuetoset, 'yyyy-MM-dd'))
                elif isinstance(valuetoset, QtCore.QDate):
                    wdg.setDate(valuetoset)
            else:
                wdg.setSpecialValueText(" ")
                wdg.setDate(QtCore.QDate.fromString('0001-01-01', 'yyyy-MM-dd'))

        elif isinstance(wdg, QCheckBox):
            # if valuetoset is not None and not isinstance(valuetoset, QtCore.QPyNullVariant):
            if valuetoset is not None:
                # self.tableWidget.cellWidget(i, 1).setValue(feat[field])
                if valuetoset:
                    wdg.setCheckState(2)
                else:
                    wdg.setCheckState(0)
            else:
                wdg.setCheckState(0)

        elif isinstance(wdg, QLabel):
            # if valuetoset is not None and valuetoset is not None and not isinstance(valuetoset, QtCore.QPyNullVariant):
            if valuetoset is not None:
                if 'Cst' in self.dbase.dbasetables[table]['fields'][field].keys():
                    # wdg.setText(self._getConstraintTextFromRawValue(table, field, valuetoset))
                    wdg.setText(self.dbase.getConstraintTextFromRawValue(table, field, valuetoset))
                else:
                    wdg.setText(valuetoset)
            else:
                wdg.setText('')


    def saveFeature(self,pushbuttonsignal=0, showsavemessage=True):
        """!
        Action when save feature is clicked
        """
        # *************************
        # save previous feature

        self.canvas.freeze(True)
        if self.dbasetable is not None :
            if self.currentFeature is not None:
                self.beforesavingFeature = qgis.core.QgsFeature(self.currentFeature)
            else:
                self.beforesavingFeature = None

        # *************************
        # set geometry

        # geometry conversion first
        if (self.tempgeometry is not None and self.dbasetable['geom'] in ['POINT', 'LINESTRING', 'POLYGON']
                 and self.tempgeometry.isMultipart()):
            success = self.tempgeometry.convertToSingleType()
        elif (self.tempgeometry is not None and self.dbasetable['geom'] in ['MULTIPOLYGON']
                and not self.tempgeometry.isMultipart()):
            success = self.tempgeometry.convertToMultiType()

        # print(self.dbasetable['geom'],self.tempgeometry.type() ,self.tempgeometry.asPoint())

        if (self.dbasetable is not None and 'geom' in self.dbasetable.keys() and self.dbasetable['geom'] == 'LINESTRING'
            and self.tempgeometry is not None and self.tempgeometry.type() == 0): # case point in linestring layer
            self.tempgeometry = qgis.core.QgsGeometry.fromPolyline([self.tempgeometry.asPoint(),
                                                                    self.tempgeometry.asPoint()])

        if self.dbasetable is not None:

            if self.currentFeature is None:
                self.currentFeature = qgis.core.QgsFeature(self.dbasetable['layer'].fields())

                if self.tempgeometry is not None:
                    self.currentFeature.setGeometry(self.tempgeometry)
                    pass
                else:
                    if 'geom' in self.dbasetable.keys() and self.groupBox_geom.parent() is not None:
                        self.windowdialog.errorMessage('Pas de geometrie selectionnee !!')
                        self.currentFeature = None
                        self.canvas.freeze(False)
                        return

                self.savingnewfeature = True
            else:
                if self.tempgeometry is not None:
                    self.currentFeature.setGeometry(self.tempgeometry)
                    pass

            # print(self.currentFeature.geometry().exportToWkt())
            self.currentFeature = self.saveTableFeature(self.dbasetablename, self.currentFeature)
            # print('curfeat1', self.currentFeature.id())

            # *************************
            # save attributes
            # first assure that parent features are created
            if self.savingnewfeature:
                self.createParentFeature()
            # Second save attributes
            # print('id', self.currentFeature.attributes())
            # self.currentFeature = self.dbasetable['layer'].getFeatures(qgis.core.QgsFeatureRequest(self.currentFeature.id())).next()
            self.currentFeature = self.dbase.getLayerFeatureById(self.dbasetablename, self.currentFeature.id())

            self.saveFeatureProperties()
            # self.currentFeature = self.dbasetable['layer'].getFeatures(qgis.core.QgsFeatureRequest(self.currentFeature.id())).next()
            self.currentFeature = self.dbase.getLayerFeatureById(self.dbasetablename, self.currentFeature.id())

            # then save properly ressource file if exists
            if self.linkuserwdg is not None and 'Ressource' in self.linkuserwdg.keys():
                self.saveRessourceFile()

            # self.currentFeature = self.dbasetable['layer'].getFeatures(qgis.core.QgsFeatureRequest(self.currentFeature.id())).next()
            self.currentFeature = self.dbase.getLayerFeatureById(self.dbasetablename, self.currentFeature.id())


            #  reload with saved attributes
            if self.savingnewfeature:
                self.loadFeaturesinTreeWdg()
                if self.comboBox_featurelist.count() > 1:
                    self.comboBox_featurelist.setCurrentIndex(self.comboBox_featurelist.count() - 1)
                else:
                    self.comboBox_featurelist.currentIndexChanged.emit(0)
            else:
                self.initFeatureProperties(self.currentFeature)
                self.postInitFeatureProperties(self.currentFeature)



            # do postsavefeature traitment
            self.postSaveFeature(self.savingnewfeature)
            # self.currentFeature = self.dbasetable['layer'].getFeatures(qgis.core.QgsFeatureRequest(self.currentFeature.id())).next()
            self.currentFeature = self.dbase.getLayerFeatureById(self.dbasetablename, self.currentFeature.id())

            # current prestation case:
            if self.savingnewfeature and self.linkagespec is not None and 'Marche' in self.linkagespec.keys()  and self.dbase.currentprestationid is not None:
                # search table with lk prestation
                actiontable = None
                for key in self.linkuserwdg.keys():
                    if self.linkagespec['Marche']['idsource'] in self.dbase.dbasetables[key]['fields'].keys():
                        actiontable = key
                        break
                if actiontable is not None:
                    sql = "UPDATE " + actiontable + " SET " + self.linkagespec['Marche']['idsource'] + " = "
                    sql += str(self.dbase.currentprestationid)
                    sql += " WHERE " + actiontable + "." + self.linkuserwdg[actiontable]['linkfield']
                    sql += " = " + str(self.currentFeature[self.linkuserwdg[actiontable]['linkfield']])
                    # print(sql)
                    self.dbase.query(sql)
                    # self.dbase.commit()

            # self.currentFeature = self.dbasetable['layer'].getFeatures(qgis.core.QgsFeatureRequest(self.currentFeature.id())).next()
            self.currentFeature = self.dbase.getLayerFeatureById(self.dbasetablename, self.currentFeature.id())

            # update datemodification
            if self.dbasetable is not None and 'id_objet' in self.dbasetable['fields'].keys() :
                idobjet = self.currentFeature['id_objet']
                datemodif = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
                sql = "UPDATE Objet SET datemodification = '" + datemodif + "'  WHERE id_objet = " + str(idobjet) + ";"
                self.dbase.query(sql)
                self.dbase.commit()

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
                self.windowdialog.normalMessage('Objet sauvegarde : ' + str(self.currentFeature.attributes()))
            self.dbasetable['layerqgis'].triggerRepaint()

            # *************************
            # reinit things
            if self.rubberBand is not None:
                self.rubberBand.reset(self.dbasetable['layer'].geometryType())
            self.tempgeometry = None
            self.savingnewfeature = False
            self.canvas.freeze(False)
            # self.canvas.refresh()
            self.dbasetable['layerqgis'].triggerRepaint()
            # self.linkageids = None

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

            # print(self.dbasefiledata)

            filedbase = open(self.dbasetablename, "w")
            for i, path in enumerate(self.dbasefiledata):
                filedbase.write(';'.join(self.dbasefiledata[i]) + '\n')
                # file.write(';'.join(self.dbasefiledata[i]))

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
            self.canvas.freeze(False)

            #self.recentDBaseChanged.emit()


    def saveTableFeature(self, table, feat):
        dbasetablelayer = self.dbase.dbasetables[table]['layer']
        dbasetablelayer.startEditing()
        # print('addedFeatureid', feat.id())
        if feat.id() == 0:  # new feature
            # self.addedFeatureid = None
            dbasetablelayer.addFeature(feat)
        success = dbasetablelayer.updateFeature(feat)

        self.addedFeatureid = None
        dbasetablelayer.raiseError.connect(self.windowdialog.errorMessage)
        dbasetablelayer.featureAdded.connect(self.getFeatureAddedId)
        dbasetablelayer.commitChanges()
        dbasetablelayer.rollBack()
        dbasetablelayer.raiseError.disconnect(self.windowdialog.errorMessage)
        dbasetablelayer.featureAdded.disconnect(self.getFeatureAddedId)

        # print('addedFeatureid',feat.id(),self.addedFeatureid)
        if self.addedFeatureid is not None:
            # return dbasetablelayer.getFeatures(qgis.core.QgsFeatureRequest(self.addedFeatureid)).next()
            return self.dbase.getLayerFeatureById(table, self.addedFeatureid)
        else:
            # return dbasetablelayer.getFeatures(qgis.core.QgsFeatureRequest(feat.id())).next()
            return self.dbase.getLayerFeatureById(table, feat.id())



    def saveFeatureProperties(self):
        """!
        Core method for saving feature properties

        """

        # pro editing
        # self.dbasetable['layer'].raiseError.connect(self.errorMessage)
        # with qgis.core.edit(self.dbasetable['layer']):


        # if self.tabWidget_properties.currentIndex() == 0 :
        self.dbasetable['layer'].startEditing()

        if self.dbase.visualmode in [0, 1]:
            if self.linkuserwdg is not None:
                for i, tablename in enumerate(self.linkuserwdg.keys()):
                    # print('attrs',self.currentFeature.attributes())
                    featid = self.currentFeature[self.linkuserwdg[tablename]['linkfield']]
                    # print('featid', featid)
                    # print(self.currentFeature.attributes())
                    # feature = self.dbase.dbasetables[tablename]['layer'].getFeatures(qgis.core.QgsFeatureRequest(featid)).next()
                    feature = self.dbase.getLayerFeatureById(tablename, featid)
                    for fieldname in self.linkuserwdg[tablename]['widgets'].keys():
                        fieldvaluetosave = self.getValueFromWidget(self.linkuserwdg[tablename]['widgets'][fieldname],
                                                                   tablename,
                                                                   fieldname)
                        if fieldvaluetosave is not None:
                            feature[fieldname] = fieldvaluetosave
                        else:
                            feature[fieldname] = None
                    self.saveTableFeature(tablename, feature)


        if self.dbase.visualmode == 2:
            if self.linkuserwdg is None:
                templinkuserwgd = {self.dbasetablename: {'linkfield': 'ID','widgets': {}}}
            else:
                templinkuserwgd = self.linkuserwdg

            listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
            for i, tablename in enumerate(templinkuserwgd.keys()):
                dbasetable = self.dbase.dbasetables[tablename]

                featid = self.currentFeature[templinkuserwgd[tablename]['linkfield']]
                # feature = self.dbase.dbasetables[tablename]['layer'].getFeatures(qgis.core.QgsFeatureRequest(featid)).next()
                feature = self.dbase.getLayerFeatureById(tablename, featid)

                for j, field in enumerate(dbasetable['fields'].keys()):
                    itemindex = listfieldname.index(tablename + '.' + field)
                    fieldvaluetosave = self.getValueFromWidget(self.tableWidget.cellWidget(itemindex, 1),
                                                               tablename,
                                                               field)
                    if fieldvaluetosave is not None:
                        feature.setAttribute(field, fieldvaluetosave)
                # print('save',tablename,feature.attributes())
                self.saveTableFeature(tablename, feature)

    def postSaveFeature(self, boolnewfeature):
        pass


    def getValueFromWidget(self, wdg, tablename, fieldname):

        fieldvaluetosave = None
        # print ('saveFeatureProperties - dbasekeys', self.dbasetable['fields'][fieldname].keys() )

        # if 'Cst' in self.dbasetable['fields'][fieldname].keys():
        if 'Cst' in self.dbase.dbasetables[tablename]['fields'][fieldname].keys():
            # fieldvaluetosave = self._getConstraintRawValueFromText(tablename,fieldname, wdg.currentText())
            fieldvaluetosave = self.dbase.getConstraintRawValueFromText(tablename, fieldname, wdg.currentText())

            if False:
                try:
                    fieldvaluetosave = self.dbase.getConstraintRawValueFromText(tablename, fieldname, wdg.currentText())
                except AttributeError as e:
                    print(self.dbase.dbasetables[tablename]['fields'][fieldname])
                    print('error',tablename, fieldname)
            if fieldvaluetosave == '':
                fieldvaluetosave = None
        else:
            # print ('saveFeatureProperties - instance', wdg)
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

        return fieldvaluetosave



    def deleteFeature(self):
        message = "Supprimer completement l'element (yes) ou l'archiver (no) ? "
        reply = QMessageBox.question(self, "Su",
                                           message,
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            # self.windowdialog.errorMessage("pas encore disponible")
            if self.deleteParentFeature():
                if False:
                    idobjet = self.currentFeature['id_objet']
                    sql = "DELETE FROM  " + self.dbasetablename + " WHERE id_objet = " + str(idobjet) + ";"
                    self.dbase.query(sql)
                if True:
                    fetid = self.currentFeature.id()
                    sql = "DELETE FROM  " + self.dbasetablename + " WHERE id_" + self.dbasetablename + " = " + str(fetid) + ";"
                    self.dbase.query(sql)

            else:
                self.windowdialog.errorMessage("pas encore disponible")


        elif reply == QMessageBox.No:
            idobjet = self.currentFeature['id_objet']
            datesuppr = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            sql = "UPDATE Objet SET datedestruction = '" + datesuppr + "'  WHERE id_objet = " + str(idobjet) + ";"
            self.dbase.query(sql)
            # self.dbase.commit()

        self.canvas.refresh()

    def deleteParentFeature(self):
        return False


    def getFeatureAddedId(self,id):
        # print('getFeatureAddedId',id)
        self.addedFeatureid = id

    def addFeature(self):
        self.featureSelected()

    """
    def errorMessage(self, text):
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().pushMessage("InspectionDigue", text,
                                                      level=qgis.gui.QgsMessageBar.CRITICAL, duration=3)
        else:
            print('ErrorMessage', text)

    def warningMessage(self, text):
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().pushMessage("InspectionDigue", text,
                                                      level=qgis.gui.QgsMessageBar.WARNING, duration=3)
        else:
            print('ErrorMessage', text)

    def normalMessage(self, text):
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().pushMessage("InspectionDigue", text,
                                                      level=qgis.gui.QgsMessageBar.INFO, duration=3)
        else:
            print('normalMessage', text)
    """

    def addGPSPoint(self):
        if self.gpsutil.currentpoint is None:
            self.windowdialog.errorMessage('GPS non connecte')
            return
        type = self.dbasetable['layer'].geometryType()

        if self.rubberBand is not None:
            self.rubberBand.reset(type)
        else:
            self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,type)
        self.rubberBand.setWidth(5)
        self.rubberBand.setColor(QtGui.QColor("magenta"))

        # xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs, self.canvas.mapSettings().destinationCrs())
        gpspoint = self.gpsutil.currentpoint
        mappoint = self.gpsutil.currentpoint
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            success = qgis.core.QgsGeometry.fromPoint(mappoint).transform(self.dbase.xform)
        else:
            success = qgis.core.QgsGeometry.fromPointXY(mappoint).transform(self.dbase.xform)



        # success = qgis.core.QgsGeometry.fromPoint(mappoint).transform(self.dbase.xformreverse)
        # print(qgis.core.QgsGeometry.fromPoint(mappoint).exportToWkt() )
        # mappointgeometry = qgis.core.QgsGeometry.fromPoint(mappoint)
       # mappoint =  mappoint.asPoint()

        if type == 0 :       # POINT
            self.setTempGeometry([mappoint])

        elif type == 1:      # LINE
            geom = None
            if self.currentFeature is not None:
                # print(self.currentFeature.geometry())
                pass
            if self.currentFeature is not None and self.currentFeature.geometry() is not None:
                geom = self.currentFeature.geometry()
                #print(geom.exportToWkt())
                # success = geom.transform(xform)
                # success = geom.transform(self.dbase.xform)
                geompoly = geom.asPolyline()
                geompoly.append(mappoint)
                self.setTempGeometry(geompoly)
            else:
                if self.tempgeometry is None:
                    self.setTempGeometry([mappoint,mappoint])
                else:
                    geompoly = self.tempgeometry.asMultiPolyline()[0]
                    if geompoly[0] == geompoly[1]:
                        del geompoly[0]
                    geompoly.append(mappoint)
                    self.setTempGeometry(geompoly)

    def addPoint(self):
        # print('addPoint')
        type = self.dbasetable['layer'].geometryType()

        if self.rubberBand is not None:
            self.rubberBand.reset(type)
        else:
            self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,type)
        self.rubberBand.setWidth(5)
        self.rubberBand.setColor(QtGui.QColor("magenta"))

        if type == 1:      # LINE
            initialgeom = self.currentFeature.geometry().asPolyline()
            # print(initialgeom)
            mapgeometry = []
            for point in initialgeom:
                mapgeometry.append(self.dbase.xform.transform(point))

            self.captureGeometry(listpointinitialgeometry=mapgeometry, type=1)


    def captureGeometry(self,connectint=0, listpointinitialgeometry=[], type=None):
        """!

        """


        source = self.sender()
        # print(source.objectName())

        if source.objectName() != 'pushButton_rajoutPoint':
            listpointinitialgeometry = []

        # print('captureGeometry', connectint, listpointinitialgeometry, type)

        if type is None:
            if 'Point' in source.objectName():
                type = 0
            elif 'Line' in source.objectName():
                type = 1
            elif 'Polygon' in source.objectName():
                type = 2


        # pushButton_rajoutPointGPS

        # self.actuallayerindex = self.dbaseused['type'].index(typename)

        # rubberband things
        if self.rubberBand is not None:
            self.rubberBand.reset(type)
        else:
            self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,type)
        self.rubberBand.setWidth(5)
        self.rubberBand.setColor(QtGui.QColor("magenta"))

        if False:

            try:
                if type == qgis.core.QgsWkbTypes.PointGeometry :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint
                elif type == qgis.core.QgsWkbTypes.LineGeometry  :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CaptureLine
                elif type == qgis.core.QgsWkbTypes.PolygonGeometry   :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CapturePolygon
                else:
                    return
            except:
                if type == qgis.core.QGis.Point :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint
                elif type == qgis.core.QGis.Line  :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CaptureLine
                elif type == qgis.core.QGis.Polygon   :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CapturePolygon
                else:
                    return

        # print('cadwdg')
        # self.cadwdg = qgis.gui.QgsAdvancedDigitizingDockWidget(self.canvas)
        # self.cadwdg.show()
        # print('capture')
        # self.mtool = mapToolCapture( self.canvas, qgis.utils.iface.cadDockWidget(), mode , self.layers[self.actuallayerindex] )
        if False:
            self.mtool = mapToolCapture(self.canvas, self.cadwdg, mode, self.dbasetable['layer'])
            # self.mtool = qgis.gui.QgsMapToolCapture(self.canvas, self.cadwdg, mode)
            self.canvas.setMapTool(self.mtool)
            self.mtool.stopCapture.connect(self.setTempGeometry)
            # self.mtool.activate()
            self.mtool.startCapturing()
        if True:
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
            # self.mtool.activate()
            self.currentmaptool.mappoints = listpointinitialgeometry
            # self.currentmaptool.setMapPoints(listpointinitialgeometry)
            self.currentmaptool.startCapturing()



    def setTempGeometry(self, points):
        #print('setTempGeometry',points)

        if self.currentmaptool is not None:
            try:
                self.currentmaptool.stopCapture.disconnect(self.setTempGeometry)
            except TypeError:
                pass

        pointsmapcanvas = []
        pointslayer=[]
        type = self.dbasetable['layer'].geometryType()

        if len(points)==2 and points[0] == points[1]:   #case point in line layer
            self.rubberBand.reset(0)
            type = 0.5

        if self.dbase.qgsiface is None: #for stadalone app bug
            for point in points:
                pointsmapcanvas.append(self.dbase.xform.transform(point))
            pointslayer = points
        else:
            pointsmapcanvas = points
            for point in points:
                pointslayer.append(self.dbase.xformreverse.transform(point))

        #self.currentmaptool.mappoints = []
        #print('pointslayer',pointslayer)
        #print('pointsmapcanvas', pointsmapcanvas)

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



        self.rubberBand.addGeometry(geometryformap, None)
        self.rubberBand.show()
        self.tempgeometry = geometryforlayer


        self.mtool = None


    def pickFeature(self):
        self.pointEmitter.canvasClicked.connect(self.selectPickedFeature)
        self.canvas.setMapTool(self.pointEmitter)

    def selectPickedFeature(self, point, button=None):

        # layername = self.picklayername

        # self.pickfield

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
            # print('selectPickedFeature',layernearist, idtoget ,nearattributevalue)
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
            print('selectPickedFeature no pickfield')
            # nearestid = self.getNearestId(point, layername)
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

    """
    def getNearestId(self, point, comefromcanvas=True):
        if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
            isspatial = self.dbasetable['layerqgis'].geometryType()  < 3
        else:
            isspatial = self.dbasetable['layerqgis'].isSpatial()
        if not isspatial:
            return None, None

        nearestid = []
        if comefromcanvas:
            point2 = self.pointEmitter.toLayerCoordinates(self.dbasetable['layerqgis'], point)
        else:
            point2 = point

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            point2geom = qgis.core.QgsGeometry.fromPoint(point2)
        else:
            point2geom = qgis.core.QgsGeometry.fromPointXY(point2)
        spIndex = qgis.core.QgsSpatialIndex(self.dbasetable['layerqgis'].getFeatures())
        layernearestids = spIndex.nearestNeighbor(point2, 5)
        # print('getNearestId',layernearestids)
        distance = None
        nearestindex = None
        # geom = None

        if len(layernearestids)>0:
            for layernearestid in layernearestids:
                # feat = self.dbasetable['layerview'].getFeatures(qgis.core.QgsFeatureRequest(layernearestid)).next()
                feat = self.getLayerFeatureById(self.dbasetablename, layernearestid)
                featgeom = feat.geometry()
                # print(featgeom.asPolyline())
                if featgeom.isGeosValid():   #if not valid, return dist = -1...
                    dist = featgeom.distance(point2geom)
                else:   #point
                    if featgeom.type() == 1 and not featgeom.isMultipart():
                        if len(featgeom.asPolyline()) == 1: #polyline of 1 point
                            dist = qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(featgeom.asPolyline()[0])).distance(point2geom)
                        elif len(featgeom.asPolyline()) == 2 and featgeom.asPolyline()[0] == featgeom.asPolyline()[1]:
                            dist = qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(featgeom.asPolyline()[0])).distance(point2geom)
                    else:
                        continue
                # print('getNearestId',feat.geometry().isGeosValid(), layernearestid,dist )
                if distance is None:
                    distance = dist
                    nearestindex = layernearestid
                elif dist < distance:
                    distance = dist
                    nearestindex = layernearestid
        return nearestindex, distance
    """


    def zoomToFeature(self,fid=None):
        #self.canvas.zoomToFeatureIds(self.layers[self.actuallayerindex], [self.currentFeature.id()] )
        #xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs, self.canvas.mapSettings().destinationCrs())
        if fid is None:
            feat = self.currentFeature
        else:
            feat = self.dbase.getLayerFeatureById(self.dbasetablename,fid )
        # point2 = xform.transform(feat.geometry().centroid().asPoint())
        if feat.geometry().centroid() is not None:
            point2 = self.dbase.xform.transform(feat.geometry().centroid().asPoint())
        else:
            point2 = self.dbase.xform.transform(feat.geometry().vertexAt(0) )
        self.canvas.setCenter(point2)
        self.canvas.refresh()



    def saveRessourceFile(self):
        # get date
        """
        self.dbaseressourcesfield = {'tablefilefield' : 'File',
                                     'idforparent' : 'IdObjet',
                                     'parenttablename' : 'OBJET',
                                     'datefield' : 'DateCreation'}
        """

        sql = "SELECT datecreation FROM Objet WHERE id_objet = " + str(self.currentFeature['id_objet'])
        query = self.dbase.query(sql)
        result = [row[0] for row in query]
        # print(result[0].__class__)

        if len(result) > 0:
            date = result[0]
            if isinstance(date, datetime.date):
                date = date.strftime('%Y-%m-%d')
        else:
            return

        date = ''.join(date.split('-'))

        sql = "SELECT id_ressource, file FROM Ressource WHERE id_ressource = " + str(self.currentFeature['id_ressource'])
        query = self.dbase.query(sql)
        result = [row[0:2] for row in query]
        if len(result) > 0:
            idressource, file = result[0]
        else:
            return

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220 and isinstance(file, QtCore.QPyNullVariant):
            file = None

        # if file is not None and not isinstance(file,QtCore.QPyNullVariant) and len(file) > 0:
        if file is not None and len(file) > 0:
            if file[0] == '.':
                file = os.path.join(self.dbase.dbaseressourcesdirectory,file)

            else:
                if os.path.isfile(file):
                    filename = os.path.basename(file)
                    filename = str(idressource) + '_' + filename
                    destinationdir = os.path.join(self.dbase.dbaseressourcesdirectory,self.dbasetablename,date)
                    if not os.path.exists(destinationdir):
                        os.makedirs(destinationdir)
                    # filename = self.currentFeature['ID']

                    destinationfile = os.path.join(destinationdir,filename)
                    shutil.copy(file,destinationfile)

                    finalname = os.path.join('.',os.path.relpath(destinationfile, self.dbase.dbaseressourcesdirectory ))
                    # print(finalname)

                    # sql = "INSERT INTO Ressource (File) VALUES('test1') WHERE ;"
                    sql = "UPDATE Ressource SET file = '" + finalname + "' WHERE id_ressource = " +  str(idressource) + ";"
                    query = self.dbase.query(sql)
                    # self.dbase.commit()

                    if False:
                        with qgis.core.edit(self.dbasetable['layer']):
                            self.currentFeature.setAttribute(self.dbaseressourcesfield['tablefilefield'], finalname)
                            success = self.dbasetable['layer'].updateFeature(self.currentFeature)

                    if self.beforesavingFeature is not None:
                        # oldfile = self.beforesavingFeature[self.dbaseressourcesfield['tablefilefield']]
                        sql = "SELECT file FROM Ressource  WHERE id_ressource = " +  str(idressource) + ";"
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
        file = self.dbase.completePathOfFile(savedfile)
        if os.path.isfile(file):
            wdg.clear()
            wdg.setPixmap(file)
        else:
            wdg.clear()
            wdg.setText('Image non trouvee')

    """
    def completePathOfFile(self,file):
        completefile = ''
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220 and isinstance(file, QtCore.QPyNullVariant):
            file = None

        #if file is None or isinstance(file,QtCore.QPyNullVariant):
        if file is None:
            return completefile
        if len(file)>0:
            if file[0] == '.':
                completefile = os.path.join(self.dbase.dbaseressourcesdirectory, file)
            else:
                completefile = file

            completefile = os.path.normpath(completefile)
        return completefile
    """

    """
    def isAttributeNull(self,attr):
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220 and isinstance(attr, QtCore.QPyNullVariant):
            return True
        elif int(str(self.dbase.qgisversion_int)[0:3]) > 220 and isinstance(attr, QtCore.QVariant) and attr.isNull():
            return True
        elif attr is None:
            return True
        else:
            return False
    """

    def goToFeaturePressed(self):

        if self.currentFeature is not None:
            self.zoomToFeature()
            """
            xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs, self.canvas.mapSettings().destinationCrs())
            point2 = xform.transform(self.currentFeature.geometry().centroid().asPoint())
            self.canvas.setCenter(point2)
            self.canvas.refresh()
            """
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                selectedfeatureids = self.dbasetable['layer'].selectedFeaturesIds()
            else:
                selectedfeatureids = self.dbasetable['layer'].selectedFeatureIds()

            if not self.currentFeature.id() in selectedfeatureids:
                type = self.dbasetable['layer'].geometryType()
                geom = qgis.core.QgsGeometry(self.currentFeature.geometry())
                if type == 1 and len(geom.asPolyline()) == 2 and geom.asPolyline()[0] == geom.asPolyline()[1] :
                    #case when point stored in polyline
                    type = 0
                    geom = qgis.core.QgsGeometry.fromPoint(geom.asPolyline()[0])
                if self.rubberBandBlink is not None:
                    self.rubberBandBlink.reset(type)
                else:
                    self.rubberBandBlink = qgis.gui.QgsRubberBand(self.canvas, type)
                self.rubberBandBlink.setWidth(5)
                self.rubberBandBlink.setColor(QtGui.QColor("magenta"))
                # xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs,self.canvas.mapSettings().destinationCrs())
                # geom = qgis.core.QgsGeometry(self.currentFeature.geometry())
                # print(geom.exportToWkt())
                # success = geom.transform(xform)
                success = geom.transform(self.dbase.xform)
                # print(geom.exportToWkt())
                self.rubberBandBlink.addGeometry(geom, None)
                self.rubberBandBlink.show()
                self.canvas.refresh()

    def goToFeatureReleased(self):
        if self.rubberBandBlink is not None:
            type = self.dbasetable['layer'].geometryType()
            self.rubberBandBlink.reset(type)



    def displayGPS(self, active):
        if active:
            #self.normalMessage('GPS connecte')
            #print('acative', self.dbasetablename, self.gpswidget)
            if self.gpswidget is not None:
                #print('active gps',self.dbasetablename)
                for key in self.gpswidget.keys():
                    if self.gpswidget[key]['widget'] is not None:
                        self.gpswidget[key]['widget'].setEnabled(True)
                self.gpsutil.ggasentence.connect(self.displayGGA)
                self.gpsutil.gstsentence.connect(self.displayGST)
            self.pushButton_rajoutPointGPS.setEnabled(True)
        else:
            #self.warningMessage('GPS deconnecte')
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
        for key in self.gpswidget.keys():
            if 'gga' in self.gpswidget[key].keys() and self.gpswidget[key]['widget'] is not None:
                if key == 'zmNGF' :
                    try:
                        self.gpswidget[key]['widget'].setText(str(round(dictgga[self.gpswidget[key]['gga']] - self.dbase.hauteurperche,2)))
                    except KeyError:
                        pass
                elif key == 'zgps' :
                    try:
                        self.gpswidget[key]['widget'].setText(str(round(dictgga[self.gpswidget[key]['gga']] - self.dbase.hauteurperche,2)))
                    except KeyError:
                        pass
                elif key == 'hauteurperche' :
                    try:
                        self.gpswidget[key]['widget'].setText(str(round(self.dbase.hauteurperche,2)))
                    except KeyError:
                        pass
                else:
                    try:
                        self.gpswidget[key]['widget'].setText(str(round(dictgga[self.gpswidget[key]['gga']],2)))
                    except KeyError:
                        pass

    def displayGST(self, dictgst):
        for key in self.gpswidget.keys():
            if 'gst' in self.gpswidget[key].keys() and self.gpswidget[key]['widget'] is not None:
                self.gpswidget[key]['widget'].setText(str(round(dictgst[self.gpswidget[key]['gst']],2)))
    """
    def getLayerFeatureById(self,layername,fid):
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            return self.dbase.dbasetables[layername]['layer'].getFeatures(qgis.core.QgsFeatureRequest(fid)).next()
        else:
            return self.dbase.dbasetables[layername]['layer'].getFeature(fid)
    """

    def getDBaseChildWidget(self,keywidget):
        wdg = self.dbasechildwdg[keywidget]
        # print(self.dbasechildwdg)
        # print(keywidget, wdg, isinstance(wdg,list))
        # print(self.dbase.dbasetables['Photo']['widget'])

        if isinstance(wdg,list) and len(wdg)>0:
            return wdg[self.dbasechildwdg[keywidget][1]]
        elif not isinstance(wdg,list) and wdg is not None:
            return wdg
        else:
            return None