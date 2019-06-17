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


# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView,QComboBox)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView,QComboBox)

from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
if False:
    from ..toolprepro.InspectionDigue_photos_tool import PhotosTool
    from ..toolprepro.InspectionDigue_observation_tool import ObservationTool
    from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
if True:
    from ...toolprepro.base.lamiabase_photo_tool  import BasePhotoTool
    from ...toolprepro.base.lamiabase_observation_tool import BaseObservationTool
    #from ...toolabstract.inspectiondigue_abstractworker import AbstractWorker
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class SyntheseZonegeoTool(AbstractInspectionDigueTool):

    DBASES = ['base_digue']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(SyntheseZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

        """
        exec('from ..toolprepro.' + dbase.type.lower() + '.lamia' + dbase.type.lower() + '_photos_tool import PhotosTool')
        exec('from ..toolprepro.' + dbase.type.lower() + '.lamia' + dbase.type.lower() + '_observation_tool import ObservationTool')
        """
        # from ..toolprepro.InspectionDigue_photos_tool import PhotosTool
        # from ..toolprepro.InspectionDigue_observation_tool import ObservationTool
        # from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Synthese'
        self.NAME = 'Desordres'
        self.visualmode = [1]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)


    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        print('initFieldUI')
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            if False:
                self.userwdgfield.comboBox_objetrequest.clear()
                self.userwdgfield.comboBox_objetrequest.addItems(['Zone geographique', 'Troncon'])
                self.userwdgfield.comboBox_objetrequest.currentIndexChanged.connect(self.postOnActivation)

            if True:
                self.propertieswdgDESORDRE = DesordreSyntheseTool(dbase=self.dbase,
                                                                  linkedtreewidget=self.userwdgfield.treeWidget_desordres,
                                                                  # dialog = self.windowdialog,
                                                                  parentwidget=self)

                self.userwdgfield.frame_2.layout().addWidget(self.propertieswdgDESORDRE)




    def postOnActivation(self):

        if True:
            self.disconnectIdsGui()
            self._clearLinkedTreeWidget()
            self.userwdgfield.treeWidget_desordres.clear()

            self.combowdg = QComboBox()
            self.combowdg.addItems(['Zone geographique','Troncon'])
            self.windowdialog.frame_4.layout().insertWidget(0,self.combowdg )
            self.combowdg.currentIndexChanged.connect(self.comboWidgetTypeChanged)
            self.combowdg.currentIndexChanged.emit(0)



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
        self.disconnectIdsGui()
        self._clearLinkedTreeWidget()
        parentitem = self.linkedtreewidget.invisibleRootItem()

        if self.combowdg.currentText() == 'Troncon':
            # sql = 'SELECT id_infralineaire FROM Infralineaire_view'
            sql = 'SELECT id_infralineaire FROM Infralineaire_qgis'
            # query = self.dbase.query(sql)
            # ids = [row[0:1] for row in query]
        # ******************************************************************
        # combo : zonegeo
        if self.combowdg.currentText() == 'Zone geographique':
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



        self.connectIdsGui()



    def postInitFeatureProperties(self, feat):
        if True:
            self.propertieswdgDESORDRE.loadFeaturesinTreeWdg()
            for i in range(self.userwdg.treeWidget_desordres.invisibleRootItem().childCount()):
                item = self.userwdg.treeWidget_desordres.invisibleRootItem().child(i)
                item.setExpanded(True)
            self.propertieswdgDESORDRE.getSyntheticResults()


    def postOnDesactivation(self):

        self.combowdg.setParent(None)

        try:
            self.userwdg.treeWidget_desordres.currentItemChanged.disconnect(self.showDesordres)
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

class DesordreSyntheseTool(AbstractInspectionDigueTool):
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
        self.linkedtreewidget.currentItemChanged.connect(self.itemChanged)

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


            self.synteticresultfields = {'Categorie': 'Desordre.catdes',
                                    'Type': 'Desordre.typedes',
                                    'Urgence': 'Observation.gravite'}

            self.parentWidget.userwdgfield.comboBox_chart_theme.addItems(list(self.synteticresultfields.keys()))
            self.parentWidget.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(self.getSyntheticResults)


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
                self.propertieswdgPHOTOGRAPHIE.userwdgfield.dateEdit.setEnabled(False)
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
            print('sql',sql)
            query = self.dbase.query(sql)
            if len(query) > 0:
                ids = [row[0:1] for row in query]
                return ids
            else:
                return ids


    def itemChanged(self,item):
        # print(int(item.text(0)))
        self.getSyntheticResults()
        if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
            self.dbasetable['layerqgis'].setSelectedFeatures([int(item.text(0))])
        else:
            self.dbasetable['layerqgis'].selectByIds([int(item.text(0))])
        # self.dbasetable['layerview'].setSelectedFeatures([int(item.text(0))])
        self.zoomToFeature(int(item.text(0)))


    def postInitFeatureProperties(self, feat):
        pass

    def getSyntheticResults(self):
        # print('getSyntheticResults')
        objetid = int(self.parentWidget.linkedtreewidget.currentItem().text(0))

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
                sql += "INNER JOIN Observation ON Observation.lk_desordre = Desordre.id_desordre  "
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


class ObservationSyntheseTool(AbstractInspectionDigueTool):
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