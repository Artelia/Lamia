# -*- coding: utf-8 -*-
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


import logging
import os
from collections import OrderedDict
import qgis
from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)


from ..base2.lamiabase_infralineaire_tool import BaseInfraLineaireTool
from .lamiabaseeclairagepublic_photo_tool import BaseEclairagePublicPhotoTool as BasePhotoTool
from .lamiabaseeclairagepublic_croquis_tool import BaseEclairagePublicCroquisTool as BaseCroquisTool
from ..base2.lamiabase_photoviewer import PhotoViewer


class BaseEclairagePublicInfraLineaireTool(BaseInfraLineaireTool):


    def __init__(self, **kwargs):
        super(BaseEclairagePublicInfraLineaireTool, self).__init__(**kwargs)


    def initMainToolWidget(self):

        if self.dbase.variante in [None, 'Lamia']:

            self.toolwidgetmain = UserUIField()

            self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                        'widgets': OrderedDict([('typres', self.toolwidgetmain.comboBox_typres),
                                                                                ('neutre', self.toolwidgetmain.comboBox_neutre),
                                                                                ('typcab', self.toolwidgetmain.comboBox_typcab),

                                                                                ('natcond',self.toolwidgetmain.comboBox_natcond),
                                                                                ('nbresecti', self.toolwidgetmain.lineEdit_nbresecti),

                                                                                ('lid_descriptionsystem_1', self.toolwidgetmain.spinBox_lk_noeud1),
                                                                                ('lid_descriptionsystem_2', self.toolwidgetmain.spinBox_lk_noeud2),

                                                                                ('nomdepart', self.toolwidgetmain.comboBox_depart),

                                                                                ])},
                                        'Objet': {'linkfield': 'id_objet',
                                                'widgets': {
                                                            'commentaire':self.toolwidgetmain.textBrowser_commentaire}},
                                        'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                            'widgets': {
                                                                'annee_debut_pose': self.toolwidgetmain.dateTimeEdit_annee_debut_pose
                                                            }}}


            self.toolwidgetmain.toolButton_pickam.clicked.connect(self.pickToNode)
            self.toolwidgetmain.toolButton_pickav.clicked.connect(self.pickToNode)



            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self

            #if self.parentWidget is None:
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)



        # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        self.updateNomDepart()




    def pickToNode(self):
        # print('pick',self.sender())
        self.picksender = self.sender()
        self.mainifacewidget.qgiscanvas.pointEmitter.canvasClicked.connect(self.picknearestnode)
        self.mainifacewidget.qgiscanvas.canvas.setMapTool(self.mainifacewidget.qgiscanvas.pointEmitter)




    def picknearestnode(self, point):

        debug = False
        typenode = False

        if self.picksender == self.toolwidgetmain.toolButton_pickam:
            editingnode = 1
        elif self.picksender == self.toolwidgetmain.toolButton_pickav:
            editingnode = 2

        if debug: logging.getLogger("Lamia").debug('edit mode %s', str(editingnode))


        #if self.toolwidgetmain.comboBox_branch.currentText() in ['Faux','Non'] or editingnode == 1:
        #nearestnodeid, distance  = self.dbase.getNearestPk(self.dbase.dbasetables['Noeud'],
        #                                      'Noeud',
        #                                      point)
        #nearestnodefet = self.dbase.getLayerFeatureByPk('Noeud', nearestnodeid)
        #nearestnodepoint = nearestnodefet.geometry().asPoint()
        #typenode = 'NODE'
        nearestnodeid, distance  = self.mainifacewidget.qgiscanvas.getNearestPk('Noeud',
                                                                                point)
        #nearestnodefet = self.dbase.getLayerFeatureByPk('Noeud', nearestnodeid)
        nearestnodefet = self.mainifacewidget.qgiscanvas.layers['Noeud']['layer'].getFeature(nearestnodeid)
        nearestnodepoint = nearestnodefet.geometry().asPoint()


        if False:
            #if self.toolwidgetmain.comboBox_branch.currentText()=='Faux' or editingnode == 1:
            if self.toolwidgetmain.comboBox_branch.currentText() in ['Faux','Non'] or editingnode == 1:
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
            #self.toolwidgetmain.spinBox_lk_noeud1.setValue(nearestnodeid)
            self.toolwidgetmain.spinBox_lk_noeud1.setValue(nearestnodeiddessys)
        elif editingnode == 2:
            #self.toolwidgetmain.spinBox_lk_noeud2.setValue(nearestnodeid)
            self.toolwidgetmain.spinBox_lk_noeud2.setValue(nearestnodeiddessys)

        # get the geometry before editing
        tempgeom=[]
        if self.tempgeometry is not None :
            wkbtype = self.tempgeometry.wkbType()
            if wkbtype == qgis.core.QgsWkbTypes.Type.LineString :
                tempgeom = self.tempgeometry.asPolyline()
            elif wkbtype == qgis.core.QgsWkbTypes.Type.MultiLineString :
                tempgeom = self.tempgeometry.asMultiPolyline()[0]

        #elif self.currentFeature is not None and self.tempgeometry is  None:
        #    tempgeom = self.currentFeature.geometry().asPolyline()


        elif self.currentFeaturePK is not None and self.tempgeometry is  None:
            tempfeat = self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME]['layer'].getFeature(self.currentFeaturePK)
            tempgeom = tempfeat.geometry().asPolyline()


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
            #self.createorresetRubberband(1)
            #self.setTempGeometry(tempgeom, False)
            self.mainifacewidget.qgiscanvas.createorresetRubberband(1)
            self.setTempGeometry(tempgeom, False)

        # disconnect all
        #self.canvas.unsetMapTool(self.pointEmitter)
        #self.picksender = None
        #try:
        #    self.pointEmitter.canvasClicked.disconnect(self.picknearestnode)
        #except:
        #    pass

        self.mainifacewidget.qgiscanvas.canvas.unsetMapTool(self.mainifacewidget.qgiscanvas.pointEmitter)
        self.picksender = None
        try:
            self.mainifacewidget.qgiscanvas.pointEmitter.canvasClicked.disconnect(self.picknearestnode)
        except:
            pass

        self.updateNomDepart()



    def updateNomDepart(self):

        idnoeudmaont = int(self.toolwidgetmain.spinBox_lk_noeud1.value())
        sql = "SELECT dep_nom FROM Equipement_now "
        sql += "INNER JOIN Noeud_now ON Equipement_now.lid_descriptionsystem_1 = Noeud_now.id_descriptionsystem"
        sql+= " WHERE Noeud_now.id_descriptionsystem = " + str(idnoeudmaont)

        sql = self.dbase.updateQueryTableNow(sql)
        res = self.dbase.query(sql)

        # print('updateNomDepart', res)


        if len(res)==0:
            self.toolwidgetmain.comboBox_depart.setEnabled(False)
            self.toolwidgetmain.comboBox_depart.setCurrentIndex(0)
        else:
            self.toolwidgetmain.comboBox_depart.setEnabled(True)
            departspresents = [elem[0] for elem in res]
            for index in range(1, self.toolwidgetmain.comboBox_depart.count()):
                if self.toolwidgetmain.comboBox_depart.itemText(index) in departspresents:
                    self.toolwidgetmain.comboBox_depart.model().item(index).setEnabled(True)
                else:
                    self.toolwidgetmain.comboBox_depart.model().item(index).setEnabled(False)



    def postSaveFeature(self, savedfeaturepk=None):


        #self.currentFeature = self.dbase.getLayerFeatureByPk(self.dbasetablename, self.currentFeaturePK)
        #fetgeom = self.currentFeature.geometry().asPolyline()
        geomtext = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                        'ST_AsText(geom)',
                                        savedfeaturepk)
        fetgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()


        indexnodes = [1, 2]
        for indexnode in indexnodes:
            idnode = eval('self.toolwidgetmain.spinBox_lk_noeud{}.value()'.format(indexnode))
            if idnode > -1 :
                sql = "SELECT pk_noeud FROM Noeud_qgis WHERE id_descriptionsystem = {}".format(idnode)
                query = self.dbase.query(sql)
                pks = [row for row in query]
                if len(pks) == 1:
                    pknoeud = pks[0][0]
                    layer = self.mainifacewidget.qgiscanvas.layers['Noeud']['layer']
                    nearestnodepoint1 = layer.getFeature(pknoeud).geometry().asPoint()
                    if indexnode == 1:
                        order = [0,-1]
                    else:
                        order = [-1,0]
                    if not self.dbase.utils.areNodesEquals(fetgeom[order[0]], nearestnodepoint1):
                        if self.dbase.utils.areNodesEquals(fetgeom[order[1]], nearestnodepoint1):
                            fetgeom = fetgeom[::-1]
                            newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                            #layer = self.dbase.dbasetables['Infralineaire']['layer']
                            layer = self.mainifacewidget.qgiscanvas.layers['Infralineaire']['layer']
                            layer.startEditing()
                            success = layer.changeGeometry(self.currentFeaturePK, newgeom)
                            layer.commitChanges()
                        else:
                            self.toolwidgetmain.spinBox_lk_noeud1.setValue(-1)
                            exec('self.toolwidgetmain.spinBox_lk_noeud{}.setValue(-1)'.format(indexnode))
                            self.formutils.saveFeatureProperties(savedfeaturepk)



        """
        indexnode1 = self.toolwidgetmain.spinBox_lk_noeud1.value()
        if indexnode1 > -1 :
            #if self.toolwidgetmain.comboBox_branch.currentText() == 'Faux':
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
                        
                        self.toolwidgetmain.spinBox_lk_noeud1.setValue(-1)
                        self.saveFeatureProperties()

        indexnode2 = self.toolwidgetmain.spinBox_lk_noeud2.value()
        if indexnode2 > -1:
            #if self.toolwidgetmain.comboBox_branch.currentText() == 'Faux':
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
                        self.toolwidgetmain.spinBox_lk_noeud2.setValue(-1)
                        self.saveFeatureProperties()
        """

class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeclairagepublic_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)

