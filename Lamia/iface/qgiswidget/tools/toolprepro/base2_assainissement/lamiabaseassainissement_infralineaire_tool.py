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


from ..base2.lamiabase_infralineaire_tool import BaseInfraLineaireTool
import os
import datetime
import qgis
from qgis.PyQt.QtWidgets import (QWidget)
from qgis.PyQt import uic, QtCore


class BaseAssainissementInfraLineaireTool(BaseInfraLineaireTool):

    DBASETABLENAME = 'Infralineaire'
    LOADFIRST = True

    tooltreewidgetCAT = 'Description'
    tooltreewidgetSUBCAT = 'Troncon'

    def __init__(self,**kwargs):
        super(BaseAssainissementInfraLineaireTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        if self.dbase.variante in [None, 'Lamia','2018_SNCF']:
            #if self.userwdgfield is None:
            self.toolwidgetmain = UserUIField()
            self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                        'widgets': { 'typeReseau': self.toolwidgetmain.comboBox_typeReseau,
                                                                    'branchement': self.toolwidgetmain.comboBox_branch,
                                                                    'modeCirculation': self.toolwidgetmain.comboBox_typeecoul,
                                                                    'formecanalisation': self.toolwidgetmain.comboBox_formecana,

                                                                    'materiau': self.toolwidgetmain.comboBox_materiau,
                                                                    #'anPoseInf': self.toolwidgetmain.dateEdit_anneepose,


                                                                    'diametreNominal': self.toolwidgetmain.doubleSpinBox_diametreNominal,
                                                                    'hauteur': self.toolwidgetmain.doubleSpinBox_haut,
                                                                    # 'largeur': self.toolwidgetmain.doubleSpinBox_larg,

                                                                    # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAmont,
                                                                    # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAval,
                                                                    'profamont': self.toolwidgetmain.doubleSpinBox_profamont,
                                                                    'profaval': self.toolwidgetmain.doubleSpinBox_profaval,
                                                                    'lid_descriptionsystem_1': self.toolwidgetmain.spinBox_lk_noeud1,
                                                                    'lid_descriptionsystem_2': self.toolwidgetmain.spinBox_lk_noeud2
                                                                    }},
                                        'Objet': {'linkfield': 'id_objet',
                                                'widgets': {'commentaire':self.toolwidgetmain.textBrowser_commentaire}},
                                        'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                            'widgets': {
                                                                'annee_debut_pose': self.toolwidgetmain.dateEdit_anneepose,

                                                            }}}


        elif self.dbase.variante in ['CD41']:

            # if self.userwdgfield is None:
            self.toolwidgetmain = UserUIField_2()

            self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                        'widgets': {
                                                            'typeReseau': self.toolwidgetmain.comboBox_typeReseau,
                                                            'branchement': self.toolwidgetmain.comboBox_branch,

                                                            'domaine': self.toolwidgetmain.comboBox_domaine,
                                                            'implantation': self.toolwidgetmain.comboBox_implant,
                                                            'modeCirculation': self.toolwidgetmain.comboBox_typeecoul,
                                                            'fonctionCannAss': self.toolwidgetmain.comboBox_fonction,





                                                            'materiau': self.toolwidgetmain.comboBox_materiau,
                                                            # 'anPoseInf': self.toolwidgetmain.dateEdit_anneepose,

                                                            'diametreNominal': self.toolwidgetmain.doubleSpinBox_diametreNominal,
                                                            'hauteur': self.toolwidgetmain.doubleSpinBox_haut,
                                                            # 'largeur': self.toolwidgetmain.doubleSpinBox_larg,

                                                            # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAmont,
                                                            # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAval,
                                                            'profamont': self.toolwidgetmain.doubleSpinBox_profamont,
                                                            'profaval': self.toolwidgetmain.doubleSpinBox_profaval,
                                                            'lid_descriptionsystem_1': self.toolwidgetmain.spinBox_lk_noeud1,
                                                            'lid_descriptionsystem_2': self.toolwidgetmain.spinBox_lk_noeud2
                                                            }},
                                        'Objet': {'linkfield': 'id_objet',
                                                'widgets': {
                                                    'commentaire': self.toolwidgetmain.textBrowser_commentaire}},
                                        'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                            'widgets': {
                                                                'annee_debut_pose': self.toolwidgetmain.dateEdit_anneepose,

                                                            }}}
            
            self.toolwidgetmain.toolButton_calc_diam.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diametreNominal))

            self.toolwidgetmain.toolButton_calc_haut.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_haut))

            self.toolwidgetmain.toolButton_prof_amont.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profamont))

            self.toolwidgetmain.toolButton_prof_aval.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profaval))

        self.toolwidgetmain.toolButton_pickam.clicked.connect(self.pickToNode)
        self.toolwidgetmain.toolButton_pickav.clicked.connect(self.pickToNode)

    def initAdvancedToolWidget(self):
        pass


    def _____________________widgetspecificfunctions(self):
        pass

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

        #if self.toolwidgetmain.comboBox_branch.currentText()=='Faux' or editingnode == 1:
        if self.toolwidgetmain.comboBox_branch.currentText() in ['Faux','Non'] or editingnode == 1:
            nearestnodeid, distance  = self.mainifacewidget.qgiscanvas.getNearestPk('Noeud',
                                                                                    point)
            #nearestnodefet = self.dbase.getLayerFeatureByPk('Noeud', nearestnodeid)
            nearestnodefet = self.mainifacewidget.qgiscanvas.layers['Noeud']['layer'].getFeature(nearestnodeid)
            nearestnodepoint = nearestnodefet.geometry().asPoint()
            typenode = 'NODE'
        else:
            nearestnodeid, distance  = self.mainifacewidget.qgiscanvas.getNearestPk('Infralineaire',
                                                                                    point)
            nearestnodeid2, distance2  = self.mainifacewidget.qgiscanvas.getNearestPk('Noeud',
                                                                                        point)
            if distance2 < distance * 1.1 :
                #nearestnodefet = self.dbase.getLayerFeatureByPk('Noeud', nearestnodeid2)
                nearestnodefet = self.mainifacewidget.qgiscanvas.layers['Noeud']['layer'].getFeature(nearestnodeid2)
                nearestnodepoint = nearestnodefet.geometry().asPoint()
                typenode = 'NODE'
            else:
                # nearestnodefet = self.dbase.getLayerFeatureByPk('Infralineaire', nearestnodeid)
                nearestnodefet = self.mainifacewidget.qgiscanvas.layers['Infralineaire']['layer'].getFeature(nearestnodeid)
                #if self.dbase.qgsiface is not None:
                point = self.mainifacewidget.qgiscanvas.xformreverse.transform(point)
                nearestnodepoint = nearestnodefet.geometry().nearestPoint(qgis.core.QgsGeometry.fromPointXY(point)).asPoint()
                typenode = 'INF'
        # nearestnodeiddessys = nearestnodefet['id_descriptionsystem']
        
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
            if wkbtype == qgis.core.QgsWkbTypes.LineString :
                tempgeom = self.tempgeometry.asPolyline()
            elif wkbtype == qgis.core.QgsWkbTypes.MultiLineString :
                tempgeom = self.tempgeometry.asMultiPolyline()[0]

        elif self.currentFeaturePK is not None and self.tempgeometry is  None:
            tempfeat = self.mainifacewidget.qgiscanvas.layers[self.DBASETABLENAME]['layer'].getFeature(self.currentFeaturePK)
            tempgeom = tempfeat.geometry().asPolyline()

        if debug: logging.getLogger("Lamia").debug('geombeforeediting %s', tempgeom)

        #modify geometry
        if False and len(tempgeom)>0:
            geomlist = self.checkGeometry(tempgeom)

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
            self.mainifacewidget.qgiscanvas.createorresetRubberband(1)
            self.setTempGeometry(tempgeom, False)

        # disconnect all
        self.mainifacewidget.qgiscanvas.canvas.unsetMapTool(self.mainifacewidget.qgiscanvas.pointEmitter)
        self.picksender = None
        try:
            self.mainifacewidget.qgiscanvas.pointEmitter.canvasClicked.disconnect(self.picknearestnode)
        except:
            pass


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


class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)


class UserUIField_2(QWidget):
    def __init__(self, parent=None):
        super(UserUIField_2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_infralineaire_tool_ui_CD41.ui')
        uic.loadUi(uipath, self)