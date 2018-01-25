# -*- coding: utf-8 -*-

import os

from qgis.PyQt import uic, QtGui

from InspectionDigueV2.src.toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__),'..','dialog', 'InspectionDigue_propertieswidget.ui'))
FORM_CLASS2, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'analysedesordresTool.ui'))



class SyntheseZonegeoTool(AbstractInspectionDigueTool, FORM_CLASS):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(SyntheseZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Synthese'
        self.NAME = 'Zone geographique'

        self.userwdg = UserUI()

        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)


        #self.dbasetablename = 'ZONEGEO'
        #self.PolygonENABLED = True
        #self.visualmode = [1, 2]

    def postOnActivation(self):
        print('post')
        self._clearLinkedTreeWidget()

        self.disconnectIdsGui()

        if True and self.linkedtreewidget is not None:

            headerlist = list(self.qtreewidgetfields)
            headerlist.insert(0,'ID')
            # print(headerlist)
            self.linkedtreewidget.setColumnCount(len(headerlist))
            self.linkedtreewidget.header().setVisible(True)
            self.linkedtreewidget.setHeaderItem(QtGui.QTreeWidgetItem(headerlist))
            header = self.linkedtreewidget.header()
            lenheaderlist = len(headerlist)
            for i in range(lenheaderlist):
                header.setResizeMode(i, QtGui.QHeaderView.ResizeToContents)
            header.setResizeMode(lenheaderlist-1, QtGui.QHeaderView.Stretch)
            parentitem = self.linkedtreewidget.invisibleRootItem()

        parentitem = self.linkedtreewidget.invisibleRootItem()
        for i in range(parentitem.childCount()):
            parentitem.child(i).takeChildren()

        ids = []
        print(self.userwdg.comboBox_objetrequest.currentText())
        if self.userwdg.comboBox_objetrequest.currentText() == 'Troncon':

            sql = 'SELECT ID FROM TRONCON'
            query = self.dbase.query(sql)
            ids = [row[0:1] for row in query]

        lenqtreewidg = len(self.qtreewidgetfields) + 1
        self.treefeatlist = [[id[0], QtGui.QTreeWidgetItem([str(id[i]) for i in range(lenqtreewidg)])] for id in ids]
        parentitem.addChildren([elem[1] for elem in self.treefeatlist])
        self.connectIdsGui()

    def featureSelected(self,item=None,itemisid = False):

        if item is None:
            return

        objetid = int(item.text(0))
        print('featureSelected',objetid)

        try:
            self.userwdg.treeWidget_desordres.currentItemChanged.disconnect(self.showDesordres)
        except:
            pass

        parentitem = self.userwdg.treeWidget_desordres.invisibleRootItem()
        #parentitem.clear()
        parentitem.takeChildren()
        if False:

            print('parentitem.childCount()', parentitem.childCount())
            for i in range(parentitem.childCount()):
                parentitem.child(i).takeChildren()

        if self.userwdg.comboBox_objetrequest.currentText() == 'Troncon':

            sql = 'SELECT IdSys FROM TRONCON WHERE ID = ' + str(objetid)
            query = self.dbase.query(sql)
            idsys = [row[0] for row in query][0]
            #print('idsys',idsys )


            sql = 'SELECT DESORDRE.ID FROM DESORDRE WHERE DESORDRE.LkDesSys = ' + str(idsys)
            #print(sql)
            query = self.dbase.query(sql)
            ids = [row[0:1] for row in query]
            #print(ids)

        lenqtreewidg = len(self.qtreewidgetfields) + 1
        self.treefeatlistchild = [[id[0], QtGui.QTreeWidgetItem([str(id[i]) for i in range(lenqtreewidg)])] for id in ids]
        parentitem.addChildren([elem[1] for elem in self.treefeatlistchild])


        self.userwdg.treeWidget_desordres.currentItemChanged.connect(self.showDesordres)


    def showDesordres(self,item):
        desordreid = int(item.text(0))
        print(desordreid)



    def postOnDesactivation(self):
        print('postOnDesactivation')
        try:
            self.userwdg.treeWidget_desordres.currentItemChanged.disconnect(self.showDesordres)
        except:
            pass


    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):
        pass

    def postSaveFeature(self, boolnewfeature):
        pass


    def selectPickedFeature(self, point):

        if self.userwdg.comboBox_objetrequest.currentText() == 'Troncon':
            layer = self.dbase.dbasetables['TRONCON']['layerview']
            wdg = self.dbase.dbasetables['TRONCON']['widget']

        nearestid, dist = wdg.getNearestId(point)

        treewdgnindex = [elem[0] for elem in self.treefeatlist].index(nearestid)
        self.linkedtreewidget.setCurrentItem(self.treefeatlist[treewdgnindex][1])
        layer.setSelectedFeatures([nearestid])


class UserUI(QtGui.QWidget, FORM_CLASS2):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        self.setupUi(self)