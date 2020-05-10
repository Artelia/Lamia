# -*- coding: utf-8 -*-
"""


import datetime
import logging
import time
debugtime = False
"""

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
import os
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_infralineaire_tool import BaseInfraLineaireTool
import logging
# from ..base.lamiabase_photo_tool import BasePhotoTool
from .lamiabaseeclairagepublic_photo_tool import BaseEclairagePublicPhotoTool as BasePhotoTool
from .lamiabaseeclairagepublic_croquis_tool import BaseEclairagePublicCroquisTool as BaseCroquisTool
from ..base2.lamiabase_photoviewer import PhotoViewer
if False:
    from .lamiabasedigue_graphique_tool import BaseGraphiqueTool as GraphiqueTool
    from .lamiabasedigue_profil_tool import BaseDigueProfilTool as ProfilTool
from collections import OrderedDict
import qgis


class BaseEclairagePublicInfraLineaireTool(BaseInfraLineaireTool):


    LOADFIRST = True
    dbasetablename = 'Infralineaire'
    # specialfieldui=['2']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseEclairagePublicInfraLineaireTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)









    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.dbase.variante in [None, 'Lamia']:
            if self.userwdgfield is None:
                self.userwdgfield = UserUIField()

                self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                           'widgets': OrderedDict([('typres', self.userwdgfield.comboBox_typres),
                                                                                   ('neutre', self.userwdgfield.comboBox_neutre),
                                                                                   ('typcab', self.userwdgfield.comboBox_typcab),

                                                                                   ('natcond',self.userwdgfield.comboBox_natcond),
                                                                                   ('nbresecti', self.userwdgfield.lineEdit_nbresecti),

                                                                                   ('lid_descriptionsystem_1', self.userwdgfield.spinBox_lk_noeud1),
                                                                                   ('lid_descriptionsystem_2', self.userwdgfield.spinBox_lk_noeud2),

                                                                                   ('nomdepart', self.userwdgfield.comboBox_depart),

                                                                                   ])},
                                         'Objet': {'linkfield': 'id_objet',
                                                   'widgets': {
                                                               'commentaire':self.userwdgfield.textBrowser_commentaire}},
                                         'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                               'widgets': {
                                                                   'annee_debut_pose': self.userwdgfield.dateTimeEdit_annee_debut_pose
                                                               }}}


                self.userwdgfield.toolButton_pickam.clicked.connect(self.pickToNode)
                self.userwdgfield.toolButton_pickav.clicked.connect(self.pickToNode)



                self.dbasechildwdgfield = []

                if self.parentWidget is None:
                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)



    def postInitFeatureProperties(self, feat):
        self.updateNomDepart()




    def pickToNode(self):
        # print('pick',self.sender())
        self.picksender = self.sender()
        self.pointEmitter.canvasClicked.connect(self.picknearestnode)
        self.canvas.setMapTool(self.pointEmitter)




    def picknearestnode(self, point):

        debug = False
        typenode = False

        if self.picksender == self.userwdgfield.toolButton_pickam:
            editingnode = 1
        elif self.picksender == self.userwdgfield.toolButton_pickav:
            editingnode = 2

        if debug: logging.getLogger("Lamia").debug('edit mode %s', str(editingnode))


        #if self.userwdgfield.comboBox_branch.currentText() in ['Faux','Non'] or editingnode == 1:
        nearestnodeid, distance  = self.dbase.getNearestPk(self.dbase.dbasetables['Noeud'],
                                              'Noeud',
                                              point)
        nearestnodefet = self.dbase.getLayerFeatureByPk('Noeud', nearestnodeid)
        nearestnodepoint = nearestnodefet.geometry().asPoint()
        #typenode = 'NODE'


        if False:
            #if self.userwdgfield.comboBox_branch.currentText()=='Faux' or editingnode == 1:
            if self.userwdgfield.comboBox_branch.currentText() in ['Faux','Non'] or editingnode == 1:
                nearestnodeid, distance  = self.dbase.getNearestPk(self.dbase.dbasetables['Noeud'],
                                                      'Noeud',
                                                      point)
                nearestnodefet = self.dbase.getLayerFeatureByPk('Noeud', nearestnodeid)
                nearestnodepoint = nearestnodefet.geometry().asPoint()
                typenode = 'NODE'


            else:
                nearestnodeid, distance  = self.dbase.getNearestPk(self.dbase.dbasetables['Infralineaire'],
                                                      'Infralineaire',
                                                      point)
                nearestnodeid2, distance2  = self.dbase.getNearestPk(self.dbase.dbasetables['Noeud'],
                                                      'Noeud',
                                                      point)
                if distance2 < distance * 1.1 :
                    nearestnodefet = self.dbase.getLayerFeatureByPk('Noeud', nearestnodeid2)
                    nearestnodepoint = nearestnodefet.geometry().asPoint()
                    typenode = 'NODE'
                else:
                    nearestnodefet = self.dbase.getLayerFeatureByPk('Infralineaire', nearestnodeid)
                    if self.dbase.qgsiface is not None:
                        point = self.dbase.xformreverse.transform(point)
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        nearestnodepoint = nearestnodefet.geometry().nearestPoint(qgis.core.QgsGeometry.fromPoint(point)).asPoint()
                    else:
                        nearestnodepoint = nearestnodefet.geometry().nearestPoint(qgis.core.QgsGeometry.fromPointXY(point)).asPoint()
                    typenode = 'INF'
        # nearestnodeiddessys = nearestnodefet['id_descriptionsystem']

        sql = "SELECT id_descriptionsystem FROM Noeud_qgis WHERE pk_noeud = " + str(nearestnodefet.id())
        nearestnodeiddessys = self.dbase.query(sql)[0][0]

        if False:
            if typenode == 'NODE':
                sql = "SELECT id_descriptionsystem FROM Noeud_qgis WHERE pk_noeud = " + str(nearestnodefet.id())
            elif typenode == 'INF':
                sql = "SELECT id_descriptionsystem FROM Infralineaire_qgis WHERE pk_infralineaire = " + str(nearestnodefet.id())
            nearestnodeiddessys = self.dbase.query(sql)[0][0]

        if debug: logging.getLogger("Lamia").debug('id,dist  %s %s', str(nearestnodeid), str(distance))

        #nearestnodefet = self.dbase.getLayerFeatureById('Noeud', nearestnodeid)
        #nearestnodepoint = nearestnodefet.geometry().asPoint()

        if debug: logging.getLogger("Lamia").debug('id  %s', str(nearestnodepoint) )

        #gui things
        if editingnode == 1:
            #self.userwdgfield.spinBox_lk_noeud1.setValue(nearestnodeid)
            self.userwdgfield.spinBox_lk_noeud1.setValue(nearestnodeiddessys)
        elif editingnode == 2:
            #self.userwdgfield.spinBox_lk_noeud2.setValue(nearestnodeid)
            self.userwdgfield.spinBox_lk_noeud2.setValue(nearestnodeiddessys)

        # get the geometry before editing
        tempgeom=[]
        if self.tempgeometry is not None :
            wkbtype = self.tempgeometry.wkbType()
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                if len(self.tempgeometry.asPolyline()) > 0:
                    tempgeom = self.tempgeometry.asPolyline()
                else:
                    tempgeom = self.tempgeometry.asMultiPolyline()[0]
            else:
                if wkbtype == qgis.core.QgsWkbTypes.Type.LineString :
                    tempgeom = self.tempgeometry.asPolyline()
                elif wkbtype == qgis.core.QgsWkbTypes.Type.MultiLineString :
                    tempgeom = self.tempgeometry.asMultiPolyline()[0]

        elif self.currentFeature is not None and self.tempgeometry is  None:
            tempgeom = self.currentFeature.geometry().asPolyline()

        if debug: logging.getLogger("Lamia").debug('geombeforeediting %s', tempgeom)


        if True:
            if len(tempgeom) >= 2:
                if editingnode == 1:
                    tempgeom[0] = nearestnodepoint
                    #geomlist[1] = tempgeom[-1]
                    # geomlist.insert(0,nearestnodepoint )
                elif editingnode == 2:
                    tempgeom[-1] = nearestnodepoint
                    #geomlist[0] = tempgeom[0]
                    # geomlist.insert(-1, nearestnodepoint)

            elif len(tempgeom) == 0:
                tempgeom.insert(-1, nearestnodepoint)
                tempgeom.insert(-1, nearestnodepoint)

            elif len(tempgeom) == 1:
                if editingnode == 1:
                    # geomlist.insert(0,nearestnodepoint)
                    tempgeom[0] = nearestnodepoint
                    #geomlist[1] = tempgeom[0]
                elif editingnode == 2:
                    # geomlist.insert(-1,nearestnodepoint)
                    #tempgeom[1] = nearestnodepoint
                    tempgeom.insert(-1, nearestnodepoint)
                    #geomlist[0] = tempgeom[0]

            if debug: logging.getLogger("Lamia").debug('geomafterediting %s', tempgeom)


            # update canvas
            self.createorresetRubberband(1)
            self.setTempGeometry(tempgeom, False)

        # disconnect all
        self.canvas.unsetMapTool(self.pointEmitter)
        self.picksender = None
        try:
            self.pointEmitter.canvasClicked.disconnect(self.picknearestnode)
        except:
            pass

        self.updateNomDepart()



    def updateNomDepart(self):

        idnoeudmaont = int(self.userwdgfield.spinBox_lk_noeud1.value())
        sql = "SELECT dep_nom FROM Equipement_now "
        sql += "INNER JOIN Noeud_now ON Equipement_now.lid_descriptionsystem_1 = Noeud_now.id_descriptionsystem"
        sql+= " WHERE Noeud_now.id_descriptionsystem = " + str(idnoeudmaont)

        sql = self.dbase.updateQueryTableNow(sql)
        res = self.dbase.query(sql)

        # print('updateNomDepart', res)


        if len(res)==0:
            self.userwdgfield.comboBox_depart.setEnabled(False)
            self.userwdgfield.comboBox_depart.setCurrentIndex(0)
        else:
            self.userwdgfield.comboBox_depart.setEnabled(True)
            departspresents = [elem[0] for elem in res]
            for index in range(1, self.userwdgfield.comboBox_depart.count()):
                if self.userwdgfield.comboBox_depart.itemText(index) in departspresents:
                    self.userwdgfield.comboBox_depart.model().item(index).setEnabled(True)
                else:
                    self.userwdgfield.comboBox_depart.model().item(index).setEnabled(False)



    def postSaveFeature(self, boolnewfeature):


        self.currentFeature = self.dbase.getLayerFeatureByPk(self.dbasetablename, self.currentFeaturePK)
        fetgeom = self.currentFeature.geometry().asPolyline()

        indexnode1 = self.userwdgfield.spinBox_lk_noeud1.value()
        if indexnode1 > -1 :
            #if self.userwdgfield.comboBox_branch.currentText() == 'Faux':
            sql = "SELECT id_noeud FROM Noeud_qgis WHERE id_descriptionsystem = " + str(indexnode1)
            query = self.dbase.query(sql)
            ids = [row for row in query]
            if len(ids) == 1:
                iddessys = ids[0][0]
                idnoeud = ids[0][0]

                nearestnodefet1 = self.dbase.getLayerFeatureById('Noeud', idnoeud)

                nearestnodepoint1 = nearestnodefet1.geometry().asPoint()

                if not self.dbase.areNodesEquals(fetgeom[0], nearestnodepoint1):

                    if self.dbase.areNodesEquals(fetgeom[-1], nearestnodepoint1):
                        fetgeom = fetgeom[::-1]
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            newgeom = qgis.core.QgsGeometry.fromPolyline(fetgeom)
                        else:
                            newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                        dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                        dbasetablelayer.startEditing()
                        success = dbasetablelayer.changeGeometry(self.currentFeature.id(), newgeom)
                        dbasetablelayer.commitChanges()
                    else:
                        self.userwdgfield.spinBox_lk_noeud1.setValue(-1)
                        self.saveFeatureProperties()



            if False:
                if self.userwdgfield.comboBox_branch.currentText() in ['Faux','Non']:
                    sql = "SELECT id_noeud FROM Noeud_qgis WHERE id_descriptionsystem = " + str(indexnode1)
                    #sql = "SELECT pk_noeud FROM Noeud_qgis WHERE id_descriptionsystem = " + str(indexnode1)
                    #sql += " AND "
                    #sql += self.dbase.dateVersionConstraintSQL()
                    query = self.dbase.query(sql)
                    ids = [row for row in query]
                    #pks = [row for row in query]
                    if len(ids) == 1:
                        # if len(pks) == 1:
                        iddessys = ids[0][0]
                        idnoeud = ids[0][0]
                        # pknoeud = pks[0][0]

                        nearestnodefet1 = self.dbase.getLayerFeatureById('Noeud', idnoeud)
                        #nearestnodefet1 = self.dbase.getLayerFeatureByPk('Noeud', iddessys)

                        nearestnodepoint1 = nearestnodefet1.geometry().asPoint()

                        if not self.dbase.areNodesEquals(fetgeom[0], nearestnodepoint1):

                            if self.dbase.areNodesEquals(fetgeom[-1], nearestnodepoint1):
                                fetgeom = fetgeom[::-1]
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    newgeom = qgis.core.QgsGeometry.fromPolyline(fetgeom)
                                else:
                                    newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                                dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                                dbasetablelayer.startEditing()
                                success = dbasetablelayer.changeGeometry(self.currentFeature.id(), newgeom)
                                dbasetablelayer.commitChanges()
                            else:
                                self.userwdgfield.spinBox_lk_noeud1.setValue(-1)
                                self.saveFeatureProperties()


                else:
                    sql = "SELECT id_infralineaire FROM Infralineaire_qgis WHERE id_descriptionsystem = " + str(indexnode1)
                    query = self.dbase.query(sql)
                    ids = [row for row in query]

                    if len(ids) == 1:
                        iddessys = ids[0][0]
                        nearestnodefet2 = self.dbase.getLayerFeatureById('Infralineaire', iddessys)
                        nearestnodepoint2 = nearestnodefet2.geometry()
                        if False:
                            resultintersect = nearestnodepoint2.buffer(0.01,12).intersects(self.currentFeature.geometry())

                            if not resultintersect:
                                self.userwdgfield.spinBox_lk_noeud2.setValue(-1)
                                self.saveFeatureProperties()

                        #if not nearestnodepoint2.buffer(0.01,12).intersects(self.currentFeature.geometry()):
                        if not nearestnodepoint2.buffer(0.01, 12).intersects(qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(fetgeom[0]))):

                            #if nearestnodepoint2.buffer(0.01,12).intersects(self.currentFeature.geometry()):
                            if nearestnodepoint2.buffer(0.01, 12).intersects(qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(fetgeom[-1]))):

                                fetgeom = fetgeom[::-1]
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    newgeom = qgis.core.QgsGeometry.fromPolyline(fetgeom)
                                else:
                                    newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                                dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                                dbasetablelayer.startEditing()
                                success = dbasetablelayer.changeGeometry(self.currentFeature.id(), newgeom)
                                dbasetablelayer.commitChanges()
                            else:
                                self.userwdgfield.spinBox_lk_noeud1.setValue(-1)
                                self.saveFeatureProperties()






        indexnode2 = self.userwdgfield.spinBox_lk_noeud2.value()
        if indexnode2 > -1:
            #if self.userwdgfield.comboBox_branch.currentText() == 'Faux':
            sql = "SELECT id_noeud FROM Noeud_qgis WHERE id_descriptionsystem = " + str(indexnode2)
            query = self.dbase.query(sql)
            ids = [row for row in query]
            if len(ids) == 1:
                iddessys = ids[0][0]
                nearestnodefet2 = self.dbase.getLayerFeatureById('Noeud', iddessys)
                nearestnodepoint2 = nearestnodefet2.geometry().asPoint()

                if not self.dbase.areNodesEquals(fetgeom[-1], nearestnodepoint2):

                    if self.dbase.areNodesEquals(fetgeom[0], nearestnodepoint2):

                        fetgeom = fetgeom[::-1]
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            newgeom = qgis.core.QgsGeometry.fromPolyline(fetgeom)
                        else:
                            newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                        dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                        dbasetablelayer.startEditing()
                        success = dbasetablelayer.changeGeometry(self.currentFeature.id(), newgeom)
                        dbasetablelayer.commitChanges()
                    else:
                        self.userwdgfield.spinBox_lk_noeud2.setValue(-1)
                        self.saveFeatureProperties()





            if False:
                if self.userwdgfield.comboBox_branch.currentText() in ['Faux','Non']:
                    sql = "SELECT id_noeud FROM Noeud_qgis WHERE id_descriptionsystem = " + str(indexnode2)
                    query = self.dbase.query(sql)
                    ids = [row for row in query]
                    if len(ids) == 1:
                        iddessys = ids[0][0]
                        nearestnodefet2 = self.dbase.getLayerFeatureById('Noeud', iddessys)
                        nearestnodepoint2 = nearestnodefet2.geometry().asPoint()

                        if not self.dbase.areNodesEquals(fetgeom[-1], nearestnodepoint2):

                            if self.dbase.areNodesEquals(fetgeom[0],nearestnodepoint2 ):

                                fetgeom = fetgeom[::-1]
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    newgeom = qgis.core.QgsGeometry.fromPolyline(fetgeom)
                                else:
                                    newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                                dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                                dbasetablelayer.startEditing()
                                success = dbasetablelayer.changeGeometry(self.currentFeature.id(), newgeom)
                                dbasetablelayer.commitChanges()
                            else:
                                self.userwdgfield.spinBox_lk_noeud2.setValue(-1)
                                self.saveFeatureProperties()

                else:
                    sql = "SELECT id_infralineaire FROM Infralineaire_qgis WHERE id_descriptionsystem = " + str(indexnode2)
                    query = self.dbase.query(sql)
                    ids = [row for row in query]

                    if len(ids) == 1:
                        iddessys = ids[0][0]
                        nearestnodefet2 = self.dbase.getLayerFeatureById('Infralineaire', iddessys)
                        nearestnodepoint2 = nearestnodefet2.geometry()
                        if False:
                            resultintersect = nearestnodepoint2.buffer(0.01,12).intersects(self.currentFeature.geometry())

                            if not resultintersect:
                                self.userwdgfield.spinBox_lk_noeud2.setValue(-1)
                                self.saveFeatureProperties()
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            #if not nearestnodepoint2.buffer(0.01,12).intersects(self.currentFeature.geometry()):
                            if not nearestnodepoint2.buffer(0.01, 12).intersects(qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(fetgeom[-1]))):

                                #if nearestnodepoint2.buffer(0.01,12).intersects(self.currentFeature.geometry()):
                                if nearestnodepoint2.buffer(0.01, 12).intersects(qgis.core.QgsGeometry.fromPoint(qgis.core.QgsPoint(fetgeom[0]))):

                                    fetgeom = fetgeom[::-1]
                                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                        newgeom = qgis.core.QgsGeometry.fromPolyline(fetgeom)
                                    else:
                                        newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                                    dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                                    dbasetablelayer.startEditing()
                                    success = dbasetablelayer.changeGeometry(self.currentFeature.id(), newgeom)
                                    dbasetablelayer.commitChanges()
                                else:
                                    self.userwdgfield.spinBox_lk_noeud2.setValue(-1)
                                    self.saveFeatureProperties()
                        else:
                            #if not nearestnodepoint2.buffer(0.01,12).intersects(self.currentFeature.geometry()):
                            if not nearestnodepoint2.buffer(0.01, 12).intersects(qgis.core.QgsGeometry.fromPointXY(qgis.core.QgsPointXY(fetgeom[-1]))):

                                #if nearestnodepoint2.buffer(0.01,12).intersects(self.currentFeature.geometry()):
                                if nearestnodepoint2.buffer(0.01, 12).intersects(qgis.core.QgsGeometry.fromPointXY(qgis.core.QgsPointXY(fetgeom[0]))):

                                    fetgeom = fetgeom[::-1]
                                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                        newgeom = qgis.core.QgsGeometry.fromPolyline(fetgeom)
                                    else:
                                        newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                                    dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                                    dbasetablelayer.startEditing()
                                    success = dbasetablelayer.changeGeometry(self.currentFeature.id(), newgeom)
                                    dbasetablelayer.commitChanges()
                                else:
                                    self.userwdgfield.spinBox_lk_noeud2.setValue(-1)
                                    self.saveFeatureProperties()












class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeclairagepublic_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)

