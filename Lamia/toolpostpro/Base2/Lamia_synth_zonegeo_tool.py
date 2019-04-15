# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView,QComboBox,QAbstractItemView )
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView,QComboBox,QAbstractItemView )
import re
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import glob
import numpy as np
import os, logging, sys
if False:
    from ..toolprepro.InspectionDigue_photos_tool import PhotosTool
    from ..toolprepro.InspectionDigue_observation_tool import ObservationTool
    from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
if True:
    from ...toolprepro.base2.lamiabase_photo_tool  import BasePhotoTool
    from ...toolprepro.base.lamiabase_observation_tool import BaseObservationTool
    #from ...toolabstract.inspectiondigue_abstractworker import AbstractWorker
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class SyntheseZonegeoTool(AbstractLamiaTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(SyntheseZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Synthese'
        self.NAME = 'Desordres'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        self.multipleselection = True

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)
        
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_croquis_tool_icon.png')
        self.qtreewidgetfields = ['libelle']


    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            if False:
                self.userwdgfield.comboBox_objetrequest.clear()
                self.userwdgfield.comboBox_objetrequest.addItems(['Zone geographique', 'Troncon'])
                self.userwdgfield.comboBox_objetrequest.currentIndexChanged.connect(self.postOnActivation)

            if True:

                self.combowdg = QComboBox()
                self.windowdialog.frame_4.layout().insertWidget(0, self.combowdg)
                self.combowdg.setVisible(False)


                self.propertieswdgDESORDRE = DesordreSyntheseTool(dbase=self.dbase,
                                                                  linkedtreewidget=self.userwdgfield.treeWidget_desordres,
                                                                  # dialog = self.windowdialog,
                                                                  parentwidget=self)

                self.userwdgfield.frame_2.layout().addWidget(self.propertieswdgDESORDRE)

                self.userwdgfield.splitter.setSizes([80, 200])
                #  itemSelectionChanged ()

                self.userwdgfield.lineEdit_option.returnPressed.connect(self.propertieswdgDESORDRE.getSyntheticResults)





    def postOnActivation(self):

        if True:
            self.disconnectIdsGui()
            self._clearLinkedTreeWidget()
            self.userwdgfield.treeWidget_desordres.clear()

            # self.combowdg = QComboBox()
            self.combowdg.clear()
            self.combowdg.addItems(['Zone geographique','Troncon'])
            #self.windowdialog.frame_4.layout().insertWidget(0,self.combowdg )
            self.combowdg.setVisible(True)
            self.combowdg.currentIndexChanged.connect(self.comboWidgetTypeChanged)
            self.combowdg.currentIndexChanged.emit(0)

            self.linkedtreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
            self.linkedtreewidget.itemSelectionChanged.connect(self.propertieswdgDESORDRE.itemChanged)

            if False and qgis.utils.iface is not None :
                qgis.utils.iface.setActiveLayer(self.dbasetables['Zonegeo']['layerqgis'])



            self.connectIdsGui()

        if False:
            self.disconnectIdsGui()
            self._clearLinkedTreeWidget()
            self.userwdgfield.treeWidget_desordres.clear()

            if self.linkedtreewidget is not None:
                headerlist = list(self.qtreewidgetfields)
                headerlist.insert(0,'ID')
                self.linkedtreewidget.setColumnCount(len(headerlist))
                self.linkedtreewidget.header().setVisible(True)
                self.linkedtreewidget.setHeaderItem(QTreeWidgetItem(headerlist))
                header = self.linkedtreewidget.header()
                lenheaderlist = len(headerlist)
                for i in range(lenheaderlist):
                    header.setResizeMode(i, QHeaderView.ResizeToContents)
                header.setResizeMode(lenheaderlist-1, QHeaderView.Stretch)
                parentitem = self.linkedtreewidget.invisibleRootItem()

            ids = []
            # ******************************************************************
            # combo : infralineaire
            if self.userwdgfield.comboBox_objetrequest.currentText() == 'Troncon':
                # sql = 'SELECT id_infralineaire FROM Infralineaire_view'
                sql = 'SELECT id_infralineaire FROM Infralineaire_qgis'
                #query = self.dbase.query(sql)
                # ids = [row[0:1] for row in query]
            # ******************************************************************
            # combo : zonegeo
            if self.userwdgfield.comboBox_objetrequest.currentText() == 'Zone geographique':
                # sql = 'SELECT id_zonegeo FROM zonegeo_view'
                sql = 'SELECT id_zonegeo FROM zonegeo_qgis'

                # query = self.dbase.query(sql)
                # ids = [row[0:1] for row in query]

            if True:
                sql += ' WHERE  datecreation <= ' + "'" + self.dbase.workingdate + "'"
                if self.dbase.dbasetype == 'postgis':
                    sql += ' AND CASE WHEN datedestruction IS NOT NULL  '
                    sql += 'THEN DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END;'
                elif self.dbase.dbasetype == 'spatialite':
                    sql += ' AND CASE WHEN datedestruction IS NOT NULL  '
                    sql += 'THEN DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END;'

            query = self.dbase.query(sql)
            ids = [row[0:1] for row in query]

            lenqtreewidg = len(self.qtreewidgetfields) + 1
            self.treefeatlist = [[id[0], QTreeWidgetItem([str(id[i]) for i in range(lenqtreewidg)])] for id in ids]
            parentitem.addChildren([elem[1] for elem in self.treefeatlist])
            # self.comboBox_featurelist.addItems([str(elem[0]) for elem in self.treefeatlist])
            self.connectIdsGui()
            # self.comboBox_featurelist.currentIndexChanged.emit(0)

            if True:
                try:
                    self.currentFeatureChanged.disconnect()
                except:
                    pass



    def comboWidgetTypeChanged(self, index ):
        if False:
            self.loadFeaturesinTreeWdg()
            self.disconnectIdsGui()
        if True:
            self.disconnectIdsGui()
            self._clearLinkedTreeWidget()


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



            self.propertieswdgDESORDRE.reloadgraphtype()


            self.connectIdsGui()







    def postInitFeatureProperties(self, feat):
        if True:
            self.propertieswdgDESORDRE.loadFeaturesinTreeWdg()
            for i in range(self.userwdg.treeWidget_desordres.invisibleRootItem().childCount()):
                item = self.userwdg.treeWidget_desordres.invisibleRootItem().child(i)
                item.setExpanded(True)
            if False:
                if self.userwdgfield.treeWidget_desordres_2.currentItem():
                    self.propertieswdgDESORDRE.getSyntheticResults(self.userwdgfield.treeWidget_desordres_2.currentItem())


    def postOnDesactivation(self):

        #self.combowdg.setParent(None)
        self.combowdg.setVisible(False)

        self.linkedtreewidget.setSelectionMode(QAbstractItemView.SingleSelection)

        try:
            self.userwdg.treeWidget_desordres.currentItemChanged.disconnect(self.showDesordres)
        except:
            pass

        try:
            self.linkedtreewidget.itemSelectionChanged.disconnect(self.propertieswdgDESORDRE.itemChanged)
        except:
            pass



    def createParentFeature(self):
        pass

    def postSaveFeature(self, boolnewfeature):
        pass

    def selectPickedFeature(self, point):
        # ******************************************************************
        # combo : infralineaire
        if self.userwdgfield.comboBox_objetrequest.currentText() == 'Troncon':
            layer = self.dbase.dbasetables['Infralineaire']['layerqgis']
            wdg = self.dbase.dbasetables['Infralineaire']['widget']
        # ******************************************************************
        # combo : zone geo
        if self.userwdgfield.comboBox_objetrequest.currentText() == 'Zone geographique':
            layer = self.dbase.dbasetables['Zonegeo']['layerqgis']
            wdg = self.dbase.dbasetables['Zonegeo']['widget']
        nearestid, dist = wdg.getNearestId(point)
        treewdgnindex = [elem[0] for elem in self.treefeatlist].index(nearestid)
        self.linkedtreewidget.setCurrentItem(self.treefeatlist[treewdgnindex][1])

        if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
            layer.setSelectedFeatures([nearestid])
        else:
            layer.selectByIds([nearestid])


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'synthesedesordre','analysedesordresTool.ui')
        uic.loadUi(uipath, self)



# ********************************************************************************************************************
# ********************************* Desordre widget            *******************************************************
# ********************************************************************************************************************

class DesordreSyntheseTool(AbstractLamiaTool):
    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(DesordreSyntheseTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)

        #exec('from ...toolprepro.' + dbase.type.lower() + '.lamia' + dbase.type.lower() + '_photos_tool import PhotosTool')
        #exec('from ...toolprepro.' + dbase.type.lower() + '.lamia' + dbase.type.lower() + '_observation_tool import ObservationTool')

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = None
        self.dbasetablename = 'Desordre'
        # self.visualmode = [1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True

        # ****************************************************************************************
        #properties ui
        self.groupBox_elements.setParent(None)
        self.groupBox_geom.setParent(None)

        #itemSelectionChanged currentItemChanged itemClicked


        self.activegraphcat = None

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = DesordreUserUI()
            self.linkuserwdgfield = {'Desordre': {'linkfield': 'id_desordre',
                                             'widgets': {'cote': self.userwdgfield.label_cote,
                                                         'position': self.userwdgfield.label_position,
                                                         'catdes': self.userwdgfield.label_catdes,
                                                         'typedes': self.userwdgfield.label_typedes}},
                                'Objet': {'linkfield': 'id_objet',
                                          'widgets': {}}}

            try:
                self.figuretype = plt.figure()
                # self.canvastype = FigureCanvas(self.figuretype)
                #layout = QtGui.QVBoxLayout()

                # self.parentWidget.userwdgfield.frame_chart.layout().addWidget(self.canvastype)
                # self.userwdgfield.frame_type.setLayout(layout)
                self.axtype = self.figuretype.add_subplot(111)
            except NameError:
                print('no matplotlib')

            self.graphwdg = Label()
            self.parentWidget.userwdgfield.frame_chart.layout().addWidget(self.graphwdg)

            self.graphdata = self.readSyntheticResultFiles()

            """
            self.synteticresultfields = {'Categorie': 'Desordre.catdes',
                                    'Type': 'Desordre.typedes',
                                    'Urgence': 'Observation.gravite'}
            """
            self.reloadgraphtype()
            #self.parentWidget.userwdgfield.comboBox_chart_theme.addItems(list(self.synteticresultfields.keys()))
            #for key in
            # self.parentWidget.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(self.getSyntheticResults)


            # ****************************************************************************************
            # child widgets
            if True:
                self.propertieswdgOBSERVATION = ObservationSyntheseTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgOBSERVATION.NAME = None
                self.propertieswdgOBSERVATION.frame_edit.setParent(None)
                self.userwdgfield.frame_observ.layout().addWidget(self.propertieswdgOBSERVATION)
                self.dbasechildwdg.append(self.propertieswdgOBSERVATION)
            if True:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self.propertieswdgOBSERVATION)
                self.propertieswdgPHOTOGRAPHIE.NAME = None
                self.propertieswdgPHOTOGRAPHIE.groupBox_geom.setParent(None)
                self.propertieswdgPHOTOGRAPHIE.frame_edit.setParent(None)
                self.propertieswdgPHOTOGRAPHIE.userwdgfield.pushButton_lastph.setParent(None)
                self.propertieswdgPHOTOGRAPHIE.userwdgfield.label_5.setParent(None)
                self.propertieswdgPHOTOGRAPHIE.userwdgfield.lineEdit_file.setParent(None)
                self.propertieswdgPHOTOGRAPHIE.userwdgfield.pushButton_chooseph.setParent(None)
                #self.propertieswdgPHOTOGRAPHIE.userwdgfield.dateEdit.setEnabled(False)
                self.propertieswdgPHOTOGRAPHIE.userwdgfield.dateTimeEdit_date.setEnabled(False)
                self.userwdgfield.frame_photo.layout().addWidget(self.propertieswdgPHOTOGRAPHIE)
                self.propertieswdgOBSERVATION.dbasechildwdg = [self.propertieswdgPHOTOGRAPHIE]
                try:
                    self.propertieswdgOBSERVATION.currentFeatureChanged.disconnect()
                except:
                    pass
                for childwdg in self.propertieswdgOBSERVATION.dbasechildwdg:
                    self.propertieswdgOBSERVATION.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)

    if False:
        def loadIds(self):
            objetid = int(self.parentWidget.linkedtreewidget.currentItem().text(0))
            ids = []
            # ******************************************************************
            # combo : infralineaire
            if self.parentWidget.userwdgfield.comboBox_objetrequest.currentText() == 'Troncon':
                #sql = 'SELECT id_descriptionsystem FROM Infralineaire_view WHERE id_objet = ' + str(objetid)
                sql = 'SELECT id_descriptionsystem FROM Infralineaire WHERE id_objet = ' + str(objetid)
                query = self.dbase.query(sql)
                if len(query) > 0:
                    idsys = [row[0] for row in query][0]
                else:
                    return ids
                # sql = "SELECT Desordre_view.id_desordre FROM Desordre_view "
                # sql += "INNER JOIN Tcdesordredescriptionsystem ON Tcdesordredescriptionsystem.id_tcdesordre = Desordre_view.id_desordre "

                sql = "SELECT Desordre.id_desordre FROM Desordre "
                sql += "INNER JOIN Tcdesordredescriptionsystem ON Tcdesordredescriptionsystem.id_tcdesordre = Desordre.id_desordre "
                sql += "WHERE Tcdesordredescriptionsystem.id_tcdescriptionsystem = " + str(idsys)
                # query = self.dbase.query(sql)
                # ids = [row[0:1] for row in query]
            # ******************************************************************
            # combo : zone geo
            if self.parentWidget.userwdgfield.comboBox_objetrequest.currentText() == 'Zone geographique':
                #sql = "SELECT ST_AsText(geom) FROM Zonegeo_view WHERE id_zonegeo = " + str(objetid)
                sql = "SELECT ST_AsText(geom) FROM Zonegeo WHERE id_zonegeo = " + str(objetid)
                query = self.dbase.query(sql)
                zonegeogeom = [row[0] for row in query][0]

                # sql = "SELECT Desordre_view.id_desordre  FROM Desordre_view "
                # sql += "INNER JOIN Tcdesordredescriptionsystem ON Tcdesordredescriptionsystem.id_tcdesordre = Desordre_view.id_desordre "

                sql = "SELECT Desordre_qgis.id_desordre  FROM Desordre_qgis "
                sql += "INNER JOIN Tcdesordredescriptionsystem ON Tcdesordredescriptionsystem.id_tcdesordre = Desordre_qgis.id_desordre "
                sql += " INNER JOIN ("
                sql += "SELECT id_descriptionsystem AS dessys, geom FROM ("
                sql += "SELECT Infralineaire.id_descriptionsystem, Infralineaire.geom FROM Descriptionsystem INNER JOIN Infralineaire ON Infralineaire.id_descriptionsystem = Descriptionsystem.id_descriptionsystem"
                sql += " UNION ALL"
                sql += " SELECT Equipement.id_descriptionsystem, Equipement.geom FROM Descriptionsystem INNER JOIN Equipement ON Equipement.id_descriptionsystem = Descriptionsystem.id_descriptionsystem"
                #sql += ")"
                sql += ") AS test1 "
                # sql += ") ON Tcdesordredescriptionsystem.id_tcdesordredescriptionsystem = dessys"
                sql += ") AS test2 ON Tcdesordredescriptionsystem.id_tcdesordredescriptionsystem = dessys"
                # sql += " WHERE ST_WITHIN(ST_MakeValid(Desordre_view.geom),ST_GeomFromText('" + str(zonegeogeom) + "'," + str(self.dbase.crsnumber) + "))"
                sql += " WHERE ST_WITHIN(ST_MakeValid(Desordre_qgis.geom),ST_GeomFromText('" + str(zonegeogeom) + "'," + str(self.dbase.crsnumber) + "))"

            if True:
                sql += ' AND  Datecreation <= ' + "'" + self.dbase.workingdate + "'"
                if self.dbase.dbasetype == 'postgis':
                    sql += ' AND CASE WHEN Datedestruction IS NOT NULL  '
                    sql += 'THEN DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
                elif self.dbase.dbasetype == 'spatialite':
                    sql += ' AND CASE WHEN datedestruction IS NOT NULL  '
                    sql += 'THEN dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'

            sql += ";"

            query = self.dbase.query(sql)
            if len(query) > 0:
                ids = [row[0:1] for row in query]
                return ids
            else:
                return ids



    def reloadgraphtype(self):
        try:
            #self.parentWidget.userwdgfield.comboBox_chart_theme.currentIndexChanged.disconnect(self.getSyntheticResults)
            self.parentWidget.userwdgfield.treeWidget_desordres_2.currentItemChanged.disconnect(self.getSyntheticResults)
        except:
            pass

        if self.parentWidget is not None:
            self.activegraphcat = None

            if self.parentWidget.combowdg.currentText() == 'Troncon':
                self.activegraphcat = 'infralineaire'
            elif self.parentWidget.combowdg.currentText() == 'Zone geographique':
                self.activegraphcat = 'zonegeo'

            # self.parentWidget.userwdgfield.comboBox_chart_theme.clear()
            self.parentWidget.userwdgfield.treeWidget_desordres_2.clear()
            parentitem = self.parentWidget.userwdgfield.treeWidget_desordres_2.invisibleRootItem()
            if self.activegraphcat in self.graphdata.keys():
                self.parentWidget.userwdgfield.treeWidget_desordres_2.setColumnCount(1)
                # itemstoload = list(self.graphdata[self.activegraphcat].keys())
                currentgraphdata = self.graphdata[self.activegraphcat]
                for key in  currentgraphdata.keys():
                    #treeitem = QTreeWidgetItem(parentitem,[currentgraphdata[key]['Title'],key])
                    treeitem = QTreeWidgetItem(parentitem)
                    treeitem.setText(1,key)
                    label = QLabel(currentgraphdata[key]['Title'])
                    label.setWordWrap(True)
                    self.parentWidget.userwdgfield.treeWidget_desordres_2.setItemWidget(treeitem, 0, label)



                #itemstoload = [QTreeWidgetItem(parentitem,[currentgraphdata[key]['Title'],key]) for key in  currentgraphdata.keys()]
                #print([item.text(0) for item in itemstoload])
                # parentitem.addChildren(itemstoload)
                parentitem.setExpanded(True)
            if False:
                if self.activegraphcat in self.graphdata.keys():
                    itemstoload = list(self.graphdata[self.activegraphcat].keys())
                    self.parentWidget.userwdgfield.comboBox_chart_theme.addItems(itemstoload)


        #self.parentWidget.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(self.getSyntheticResults)
        # currentItemChanged  itemSelectionChanged
        self.parentWidget.userwdgfield.treeWidget_desordres_2.currentItemChanged.connect(self.getSyntheticResults)



    def readSyntheticResultFiles(self):
        debug = False

        if debug: logging.getLogger("Lamia").debug('started')


        graphdata = {}
        graphdir = os.path.join(os.path.dirname(__file__),'..',self.dbase.type, 'synthesegraphiques')
        for filename in glob.glob(os.path.join(graphdir, '*.txt')):
            basename = os.path.basename(filename).split('.')[0]
            if debug: logging.getLogger("Lamia").debug('basename : %s',basename )
            if  basename.split('_')[0] not in graphdata.keys():
                graphdata[basename.split('_')[0]] = {}
            graphdata[basename.split('_')[0]]['_'.join(basename.split('_')[1:])] = {}

            currentgraphdata = graphdata[basename.split('_')[0]]['_'.join(basename.split('_')[1:])]
            #self.confData[basename] = {}
            if sys.version_info.major == 2:
                filetoread = open(filename, 'r')
            elif sys.version_info.major == 3:
                filetoread = open(filename, 'r',encoding="utf-8")
                #file = open(filename, 'rb')
            compt = 0
            if True:
                for line in filetoread:
                    if line[0:3] == '###':  # new field
                        actualdictkey = line[3:].strip().split(' ')[0]
                        if actualdictkey in ['Graphsql', 'Graphpython']:
                            currentgraphdata[actualdictkey] = ''
                        elif actualdictkey in ['Graphtype','Graphoption','Title','Graphcumulatif']:
                            currentgraphdata[actualdictkey] = ' '.join(line[3:].strip().split(' ')[1:]).strip()
                        elif actualdictkey in ['Cst','Color']:
                            currentgraphdata[actualdictkey] = {}
                        else:
                            currentgraphdata[actualdictkey] = {}
                    elif line.strip() == '' or line[0] == '#':
                        continue

                    else:
                        if actualdictkey in ['Graphsql'] :
                            currentgraphdata[actualdictkey] += line.strip() + ' '
                        if actualdictkey in [ 'Graphpython'] :
                            currentgraphdata[actualdictkey] += line
                        elif actualdictkey in ['Cst']:
                            currentgraphdata[actualdictkey][int(line.split(';')[0].strip())] =  line.split(';')[1].strip()
                        elif actualdictkey in ['Color']:
                            currentgraphdata[actualdictkey][line.split(';')[0].strip()] =  line.split(';')[1].strip()

            filetoread.close()


        return graphdata



    def itemChanged(self,item=None):
        if not item :
            #return
            item = self.parentWidget.linkedtreewidget.currentItem()
            if not item or item.text(0) == '':
                return

        self.getSyntheticResults()

        if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
            self.dbasetable['layerqgis'].setSelectedFeatures([int(item.text(0))])
        else:
            self.dbasetable['layerqgis'].selectByIds([int(item.text(0))])

        # self.dbasetable['layerview'].setSelectedFeatures([int(item.text(0))])
        self.zoomToFeature(int(item.text(0)))


    def postInitFeatureProperties(self, feat):
        pass

    def getSyntheticResults(self, itemselected=None):
        debug = False

        self.axtype.cla()
        self.figuretype.canvas.draw()

        if not itemselected:
            itemselected = self.parentWidget.userwdgfield.treeWidget_desordres_2.currentItem()
            if not itemselected :
                return


        if debug: logging.getLogger("Lamia").debug('started')
        self.axtype.cla()

        if not self.parentWidget.linkedtreewidget.currentItem():
            return


        objetid = [int(item.text(0)) for item in self.parentWidget.linkedtreewidget.selectedItems()]

        # print(objetid)

        if len(objetid) == 0:
            return

        currentgraphdata = None
        if (self.activegraphcat in self.graphdata.keys()
                and itemselected.text(1) in self.graphdata[self.activegraphcat]):
            currentgraphdata = self.graphdata[self.activegraphcat][itemselected.text(1)]
        if debug: logging.getLogger("Lamia").debug('currentgraphdata : %s', str(currentgraphdata))
        if not currentgraphdata:
            return

        optiondict = {}
        labels = None
        # PROCESS SQL
        if 'Graphsql' in currentgraphdata.keys():

            sql = currentgraphdata['Graphsql']

            if len(objetid)==1:
                tupleobjetid = '(' + str(objetid[0]) + ')'
            else:
                tupleobjetid = tuple(objetid)

            sqlid = " AND " + self.activegraphcat.title() + '_qgis.id_' + self.activegraphcat.lower() + " IN " + str(tupleobjetid)
            sqlid += " AND " + self.activegraphcat.title() + "_qgis.lpk_revision_end IS NULL "

            # add activegraphcat in where clause

            sqltemp1 = self.dbase.splitSQLSelectFromWhereOrderby(sql)

            if debug: logging.getLogger("Lamia").debug('sqlsplit : %s', str(sqltemp1))

            sqlstandard = ''
            if 'WITH' in sqltemp1.keys():
                sqlstandard += "WITH " + sqltemp1['WITH']
            sqlstandard += " SELECT " + sqltemp1['SELECT']
            sqlstandard += " FROM " + sqltemp1['FROM'] + ', ' + self.activegraphcat.title() + "_qgis "
            sqlstandard += " WHERE " + sqltemp1['WHERE'] + sqlid
            if 'GROUP' in sqltemp1.keys():
                sqlstandard += ' GROUP BY ' + sqltemp1['GROUP']




            #Process Options
            optiontext = self.parentWidget.userwdgfield.lineEdit_option.text()

            if optiontext != '':
                optiontxttemp1 = optiontext.split(';')
                for option in optiontxttemp1:
                    if len(option.split('=')) == 2 :
                        optiondict[option.split('=')[0]] = option.split('=')[1:][0]
                    else:
                        print('error', option)


            if 'date' in optiondict.keys():
                sqlfinal =[]
                for date in optiondict['date'].split(','):
                    sqlfinal.append(self.dbase.updateQueryTableNow(sqlstandard,date))
            else:
                sqlfinal = [self.dbase.updateQueryTableNow(sqlstandard)]

            if debug: logging.getLogger("Lamia").debug('sql : %s', str(sqlfinal))
            # print('sqlfinal', sqlfinal)

            #process results
            result = []
            names = None

            for sqltemp in sqlfinal :
                query = self.dbase.query(sqltemp)
                result.append([])
                #tempresult = result[-1]

                for row in query:
                    if row[0] is None:
                        continue
                    result[-1].append([])
                    for i, res in enumerate(row):

                        if 'Cst' in currentgraphdata.keys() and i in currentgraphdata['Cst'].keys():
                            table, field = currentgraphdata['Cst'][i].split('.')
                            val = self.dbase.getConstraintTextFromRawValue(table, field, res)
                            result[-1][-1].append(val)
                        else:
                            result[-1][-1].append(res)

        elif 'Graphpython' in currentgraphdata.keys():
            result=None

            ns = {}
            exec(currentgraphdata['Graphpython'], {'self': self},ns)
            # print('res', ns)
            tempfunction = ns['getResult']
            result,labels = tempfunction(objetid)
            # print('res2', result)




        if debug: logging.getLogger("Lamia").debug('sql result : %s', str(result))
        if debug: logging.getLogger("Lamia").debug('sql labels : %s', str(labels))

        if currentgraphdata['Graphtype'] == 'pie':
            result = result[0]
            labels = [row[0] for row in result]
            sizes = [row[1] for row in result]
            explode = [0.05] * len(labels)

            if debug: logging.getLogger("Lamia").debug('pie result : %s %s', str(labels), str(sizes))

            # self.axtype.clear()
            self.axtype.cla()

            # plt.cla()
            self.axtype.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
            self.axtype.axis('equal')
            self.axtype.set_title(itemselected.text(0))
            self.figuretype.canvas.draw()

        if currentgraphdata['Graphtype'] == 'stackedbar':
            # https://stackoverflow.com/questions/11273196/stacked-bar-chart-with-differently-ordered-colors-using-matplotlib
            # self.axtype.clear()
            self.axtype.cla()
            if 'Graphcumulatif' in currentgraphdata.keys() and currentgraphdata['Graphcumulatif'] =='True' :
                #get common label
                resforbar=[]
                for row in result:
                    resforbar.append({})
                    for res in row:
                        resforbar[-1][str(res[0])] = res[1]
                names = sorted(resforbar[0].keys())
                values = np.array([[data[name] if name in data.keys() else 0 for name in names ] for data in resforbar ])
                bottoms = np.insert(np.cumsum(values, axis=1), 0, 0, axis=1)[:, :-1]

                #labels:
                if 'date' in optiondict.keys():
                    labels = optiondict['date'].split(',')
                elif labels is not None:
                    labels = labels
                else:
                    pass

                abscisse = np.arange(len(result))

                if debug: logging.getLogger("Lamia").debug('bar result : %s %s', str(names), str(values))

                for i, name in enumerate(names):
                    value = values[:,i]
                    bottom = bottoms[:,i]
                    # color
                    color = None
                    if 'Color' in currentgraphdata.keys():
                        if name in currentgraphdata['Color'].keys():
                            color = currentgraphdata['Color'][name]

                    if color:
                        self.axtype.bar(abscisse, value, 0.8, bottom=bottom, label=name, color=color)
                    else:
                        self.axtype.bar(abscisse, value, 0.8, bottom=bottom, label=name)


                if labels is not None:
                    self.axtype.set_xticks(abscisse)
                    self.axtype.set_xticklabels(tuple(labels))
                else:
                    self.axtype.set_xticks([])


            else:
                pass

            self.axtype.axis('auto')

            self.axtype.legend()
            self.axtype.grid(which='both', axis='y', linestyle='--')
            #self.axtype.set_xlim([0,len(result)])
            self.axtype.autoscale()
            self.figuretype.canvas.draw()





            if False:
                for i, res in enumerate(result):

                    labels = [row[0] for row in res]
                    sizes = [row[1] for row in res]
                    explode = [0.05] * len(labels)

                    if debug: logging.getLogger("Lamia").debug('bar result : %s %s', str(labels), str(sizes))



                    # plt.cla()
                    y_offset = 0
                    for j, label in enumerate(labels):
                        self.axtype.bar(i, sizes[j], 0.8 , bottom=y_offset, label=label)
                        y_offset += sizes[j]
                    if 'date' in optiondict.keys():
                        self.axtype.set_xticks(np.arange(len(result)))
                        self.axtype.set_xticklabels(tuple(optiondict['date'].split(',')))
                    else:
                        self.axtype.set_xticks([])

                    self.axtype.legend()
                    self.axtype.grid(which='both', axis='y', linestyle='--')
                    self.axtype.relim()
                    self.axtype.autoscale_view()
                    self.figuretype.canvas.draw()




            """
            self.axtype.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
            self.axtype.axis('equal')
            self.axtype.set_title('Desordre :' + self.parentWidget.userwdg.comboBox_chart_theme.currentText())
            """


        buf = io.BytesIO()
        self.figuretype.savefig(buf, bbox_inches='tight')
        buf.seek(0)
        pix = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(buf.getvalue()))
        self.graphwdg.setPixmap(pix)



        if False:

            #if self.parentWidget.userwdg.comboBox_objetrequest.currentText() == 'Zone geographique':
            if self.parentWidget.combowdg.currentText() == 'Zone geographique':

                sql = "SELECT ST_AsText(geom) FROM Zonegeo WHERE id_zonegeo = " + str(objetid)
                query = self.dbase.query(sql)
                zonegeogeom = [row[0] for row in query][0]

                desordrefield = self.synteticresultfields[self.parentWidget.userwdg.comboBox_chart_theme.currentText()]

                if False:
                    #sql = "SELECT Desordre.id_desordre  FROM Desordre "
                    sql = "SELECT DISTINCT("+ desordrefield + "), COUNT(" + desordrefield + ")  FROM Desordre "
                    sql += "INNER JOIN Observation ON Observation.lk_desordre = Desordre.id_desordre  "
                    # sql += "INNER JOIN (SELECT Observation.* FROM Observation GROUP BY lk_desordre   ORDER by date DESC ) ON Observation.lk_desordre = Desordre.id_desordre  "
                    sql += "INNER JOIN Tcdesordredescriptionsystem ON Tcdesordredescriptionsystem.id_tcdesordre = Desordre.id_desordre "
                    sql += " INNER JOIN ("
                    sql += "SELECT id_descriptionsystem AS dessys, geom FROM ("
                    sql += "SELECT Infralineaire.id_descriptionsystem, Infralineaire.geom FROM Descriptionsystem INNER JOIN Infralineaire ON Infralineaire.id_descriptionsystem = Descriptionsystem.id_descriptionsystem"
                    sql += " UNION ALL"
                    sql += " SELECT Equipement.id_descriptionsystem, Equipement.geom FROM Descriptionsystem INNER JOIN Equipement ON Equipement.id_descriptionsystem = Descriptionsystem.id_descriptionsystem"
                    sql += ") AS test1"
                    sql += ") AS test2 ON Tcdesordredescriptionsystem.id_tcdesordredescriptionsystem = dessys"
                    sql += " WHERE ST_WITHIN(ST_MakeValid(Desordre.geom),ST_GeomFromText('" + str(zonegeogeom) + "'," + str(
                        self.dbase.crsnumber) + "))"
                    sql += " GROUP BY " + desordrefield  + ";"

                if True:
                    sql = "SELECT DISTINCT("+ desordrefield + "), COUNT(" + desordrefield + ")  FROM Desordre "
                    sql += "INNER JOIN Observation ON Observation.lid_desordre = Desordre.id_desordre  "
                    sql += " WHERE ST_WITHIN(ST_MakeValid(Desordre.geom),ST_GeomFromText('" + str(zonegeogeom) + "'," + str(
                        self.dbase.crsnumber) + "))"
                    sql += " GROUP BY " + desordrefield  + ";"

                # print(sql)

                query = self.dbase.query(sql)
                # print('getSyntheticResults query', query)
                result = [row[0:2] for row in query]

                onlyfield = desordrefield.split('.')[1]
                onlytable = desordrefield.split('.')[0]
                if 'Cst' in self.dbase.dbasetables[onlytable]['fields'][onlyfield].keys():
                    if True:
                        try:
                            labels = [self.dbase.getConstraintTextFromRawValue(onlytable, onlyfield, row[0] ) for row in result]
                        except ValueError as e:
                            print('cst',e)
                            labels = [row[0] for row in result]
                    if False:
                        dbtablewdg = self.dbase.dbasetables[onlytable]['widget'][0]
                        try:
                            labels = [dbtablewdg.dbase.getConstraintTextFromRawValue(onlytable, onlyfield, row[0] ) for row in result]
                        except ValueError as e:
                            print('cst',e)
                            labels = [row[0] for row in result]
                else:
                    labels = [row[0] for row in result]
                sizes = [row[1] for row in result]
                explode = [0.05] * len(labels)
                # print(sizes,labels )


                # self.axtype.clear()
                self.axtype.cla()

                # plt.cla()
                self.axtype.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
                self.axtype.axis('equal')
                self.axtype.set_title('Desordre :' + self.parentWidget.userwdg.comboBox_chart_theme.currentText())
                buf = io.BytesIO()
                self.figuretype.savefig(buf, bbox_inches='tight')
                buf.seek(0)
                pix = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(buf.getvalue()))
                self.graphwdg.setPixmap(pix)







class DesordreUserUI(QWidget):
    def __init__(self, parent=None):
        super(DesordreUserUI, self).__init__(parent=parent)
        path = os.path.join(os.path.dirname(__file__), 'synthesedesordre','DesordreSyntheseToolUser.ui')
        uic.loadUi(path, self)

# ********************************************************************************************************************
# ********************************* Desordre widget            *******************************************************
# ********************************************************************************************************************


class ObservationSyntheseTool(AbstractLamiaTool):
    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(ObservationSyntheseTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = None
        self.dbasetablename = 'Observation'
        # self.visualmode = [1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Desordre' : {'tabletc' : None,
                                           'idsource' : 'lk_desordre',
                                       'idtcsource' : None,
                                           'iddest' : 'id_desordre',
                                       'idtcdest' : None,
                                           'desttable' : ['Desordre']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lk_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }

        # ****************************************************************************************
        #properties ui
        self.groupBox_geom.setParent(None)

        # ****************************************************************************************
        # userui
        self.userwdg = ObservationUserUI()
        self.linkuserwdg = {'Observation' : {'linkfield' : 'id_observation',
                                         'widgets' : {'date' : self.userwdg.dateEdit,
                                                    'gravite': self.userwdg.label_urgence,
                                                    'evolution': self.userwdg.label_evolution,
                                                    'commentaires': self.userwdg.label_comm,
                                                    'suite': self.userwdg.label_suite}},
                            'Objet' : {'linkfield' : 'id_objet',
                                      'widgets' : {}}}




    def postInitFeatureProperties(self, feat):
        pass

    def postloadIds(self,sqlin):
        if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
            sqlin += " ORDER BY dateobservation DESC"
        return sqlin




class ObservationUserUI(QWidget):
    def __init__(self, parent=None):
        super(ObservationUserUI, self).__init__(parent=parent)
        path = os.path.join(os.path.dirname(__file__), 'synthesedesordre','ObservationSyntheseToolUser.ui')
        uic.loadUi(path, self)


class Label(QLabel):
    def __init__(self, img = None):
        super(Label, self).__init__()
        self.setFrameStyle(QFrame.StyledPanel)
        self.pixmap = QtGui.QPixmap(img)

    def paintEvent(self, event):
        size = self.size()
        painter = QtGui.QPainter(self)
        point = QtCore.QPoint(0,0)
        if not self.pixmap.isNull() :
            scaledPix = self.pixmap.scaled(size, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
            # start painting the label from left upper corner
            point.setX((size.width() - scaledPix.width())/2)
            point.setY((size.height() - scaledPix.height())/2)
            painter.drawPixmap(point, scaledPix)


    def setPixmap(self, img):
        self.pixmap = QtGui.QPixmap(img)
        self.repaint()

    def clear(self):
        self.pixmap = QtGui.QPixmap()
        self.repaint()