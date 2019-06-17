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
"""


import datetime

import time
debugtime = False
"""

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
import os
import logging
import qgis
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base.lamiabase_infralineaire_tool import BaseInfraLineaireTool

from ..base.lamiabase_photo_tool import BasePhotoTool
from ..base.lamiabase_croquis_tool import BaseCroquisTool




class BaseAssainissementInfraLineaireTool(BaseInfraLineaireTool):


    LOADFIRST = True
    dbasetablename = 'Infralineaire'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseAssainissementInfraLineaireTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        timestart = time.clock()
        if debugtime: logging.getLogger('Lamia').debug('Start init %s',str(round(time.clock() - timestart, 3)))

        self.CAT = 'Description'
        self.NAME = 'Troncon'
        self.dbasetablename = 'Infralineaire'
        # self.visualmode = [0, 1, 2]
        # self.PointEnabled = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_objet',
                                            'idtcsource' : 'id_tcobjet',
                                           'iddest' : 'id_intervenant',
                                           'idtcdest' : 'id_tcintervenant',
                                           'desttable' : ['Intervenant']}
                                            }
        self.pickTable = {'LkZoneGeo': {'ZONEGEO': 'ID'}}
        self.debug = False
        self.qtreewidgetfields = ['revisionbegin']

        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_infralineaire_tool_icon.svg')


        # ****************************************************************************************
        #properties ui
        pass


    
    """
    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            self.userwdgfield = UserUIField()

            self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                       'widgets': { 'typeReseau': self.userwdgfield.comboBox_typeReseau,
                                                                   'branchement': self.userwdgfield.comboBox_branch,
                                                                   'modeCirculation': self.userwdgfield.comboBox_typeecoul,
                                                                   'formecanalisation': self.userwdgfield.comboBox_formecana,

                                                                 'materiau': self.userwdgfield.comboBox_materiau,
                                                                   'anPoseInf': self.userwdgfield.dateEdit_anneepose,


                                                                   'diametreNominal': self.userwdgfield.doubleSpinBox_diametreNominal,
                                                                   'hauteur': self.userwdgfield.doubleSpinBox_haut,
                                                                   # 'largeur': self.userwdgfield.doubleSpinBox_larg,

                                                                   # 'altAmont': self.userwdgfield.doubleSpinBox_altAmont,
                                                                   # 'altAmont': self.userwdgfield.doubleSpinBox_altAval,
                                                                   'profamont': self.userwdgfield.doubleSpinBox_profamont,
                                                                   'profaval': self.userwdgfield.doubleSpinBox_profaval,
                                                                   'lk_descriptionsystem1': self.userwdgfield.spinBox_lk_noeud1,
                                                                   'lk_descriptionsystem2': self.userwdgfield.spinBox_lk_noeud2
                                                                 }},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {'commentaire':self.userwdgfield.textBrowser_commentaire}},
                                     'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                           'widgets': {}}}




            self.userwdgfield.toolButton_calc_diam.clicked.connect(lambda : self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_diametreNominal))

            self.userwdgfield.toolButton_calc_haut.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_haut))


            self.userwdgfield.toolButton_prof_amont.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_profamont))

            self.userwdgfield.toolButton_prof_aval.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_profaval))

            self.userwdgfield.toolButton_pickam.clicked.connect(self.pickToNode)
            self.userwdgfield.toolButton_pickav.clicked.connect(self.pickToNode)


            self.dbasechildwdgfield = []

            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def pickToNode(self):
        # print('pick',self.sender())
        self.picksender = self.sender()
        self.pointEmitter.canvasClicked.connect(self.picknearestnode)
        self.canvas.setMapTool(self.pointEmitter)

    def picknearestnode(self, point):

        debug = False

        if self.picksender == self.userwdgfield.toolButton_pickam:
            editingnode = 1
        elif self.picksender == self.userwdgfield.toolButton_pickav:
            editingnode = 2

        if debug: logging.getLogger("Lamia").debug('edit mode %s', str(editingnode))

        if self.userwdgfield.comboBox_branch.currentText()=='Faux' or editingnode == 1:
            nearestnodeid, distance  = self.dbase.getNearestPk(self.dbase.dbasetables['Noeud'],
                                                  'Noeud',
                                                  point)
            if not self.dbase.revisionwork:
                nearestnodefet = self.dbase.getLayerFeatureById('Noeud', nearestnodeid)
            else:
                nearestnodefet = self.dbase.getLayerFeatureByPk('Noeud', nearestnodeid)

            nearestnodepoint = nearestnodefet.geometry().asPoint()
        else:
            nearestnodeid, distance  = self.dbase.getNearestPk(self.dbase.dbasetables['Infralineaire'],
                                                  'Infralineaire',
                                                  point)

            nearestnodeid2, distance2  = self.dbase.getNearestPk(self.dbase.dbasetables['Noeud'],
                                                  'Noeud',
                                                  point)

            if distance2 < distance * 1.1 :
                if not self.dbase.revisionwork:
                    nearestnodefet = self.dbase.getLayerFeatureById('Noeud', nearestnodeid2)
                else:
                    nearestnodefet = self.dbase.getLayerFeatureByPk('Noeud', nearestnodeid2)

                nearestnodepoint = nearestnodefet.geometry().asPoint()

            else:
                if not self.dbase.revisionwork:
                    nearestnodefet = self.dbase.getLayerFeatureById('Infralineaire', nearestnodeid)
                else:
                    nearestnodefet = self.dbase.getLayerFeatureByPk('Infralineaire', nearestnodeid)


                if self.dbase.qgsiface is not None:
                    point = self.dbase.xformreverse.transform(point)
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    nearestnodepoint = nearestnodefet.geometry().nearestPoint(qgis.core.QgsGeometry.fromPoint(point)).asPoint()
                else:
                    nearestnodepoint = nearestnodefet.geometry().nearestPoint(qgis.core.QgsGeometry.fromPointXY(point)).asPoint()

        nearestnodeiddessys = nearestnodefet['id_descriptionsystem']

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
            if len(self.tempgeometry.asPolyline())>0:
                tempgeom = self.tempgeometry.asPolyline()
            else:
                tempgeom = self.tempgeometry.asMultiPolyline()[0]
        elif self.currentFeature is not None and self.tempgeometry is  None:
            tempgeom = self.currentFeature.geometry().asPolyline()

        if debug: logging.getLogger("Lamia").debug('geombeforeediting %s', tempgeom)

        #modify geometry
        if False and len(tempgeom)>0:
            geomlist = self.checkGeometry(tempgeom)



        if False:
            geomlist = [None, None]
            if len(tempgeom)>=2:
                if editingnode == 1:
                    geomlist[0] = nearestnodepoint
                    geomlist[1] = tempgeom[-1]
                    # geomlist.insert(0,nearestnodepoint )
                elif editingnode == 2:
                    geomlist[1] = nearestnodepoint
                    geomlist[0] = tempgeom[0]
                    # geomlist.insert(-1, nearestnodepoint)

            elif len(tempgeom) == 0 :
                geomlist[0] = nearestnodepoint
                geomlist[1] = nearestnodepoint

            elif len(tempgeom) == 1 :
                if editingnode == 1:
                    #geomlist.insert(0,nearestnodepoint)
                    geomlist[0] = nearestnodepoint
                    geomlist[1] = tempgeom[0]
                elif editingnode == 2:
                    #geomlist.insert(-1,nearestnodepoint)
                    geomlist[1] = nearestnodepoint
                    geomlist[0] = tempgeom[0]

            if debug: logging.getLogger("Lamia").debug('geomafterediting %s', geomlist)

            print('geomlist', geomlist)

            #update canvas
            self.createorresetRubberband(1)
            self.setTempGeometry(geomlist,False)


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

    """
    def addPoint(self):

        self.createorresetRubberband(1)

        # get the geometry before editing
        initialgeom = [None, None]
        if self.tempgeometry is not None:
            if len(self.tempgeometry.asPolyline()) > 0:
                initialgeom = self.tempgeometry.asPolyline()
            else:
                initialgeom = self.tempgeometry.asMultiPolyline()[0]
        elif self.currentFeature is not None and self.tempgeometry is None:
            initialgeom = self.currentFeature.geometry().asPolyline()

        mapgeometry = []
        for point in initialgeom:
            if self.dbase.qgsiface is None:  # bug for standalone
                mapgeometry = initialgeom
            else:
                mapgeometry.append(self.dbase.xform.transform(point))

        # mapgeometry = self.checkGeometry(mapgeometry)

        # mapgeometry = [mapgeometry[0]]

        self.captureGeometry(listpointinitialgeometry=mapgeometry, type=1)

    """

    def postSaveFeature(self, boolnewfeature):
        if not self.dbase.revisionwork:
            self.currentFeature = self.dbase.getLayerFeatureById(self.dbasetablename, self.currentFeature.id())
        else:
            self.currentFeature = self.dbase.getLayerFeatureByPk(self.dbasetablename, self.currentFeature.id())


        fetgeom = self.currentFeature.geometry().asPolyline()

        indexnode1 = self.userwdgfield.spinBox_lk_noeud1.value()

        if indexnode1 > -1 :
            if self.userwdgfield.comboBox_branch.currentText() == 'Faux':
                sql = "SELECT id_noeud FROM Noeud_qgis WHERE id_descriptionsystem = " + str(indexnode1)
                query = self.dbase.query(sql)
                ids = [row for row in query]
                if len(ids) == 1:
                    iddessys = ids[0][0]

                    nearestnodefet1 = self.dbase.getLayerFeatureById('Noeud', iddessys)

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
                sql = "SELECT id_infralineaire FROM Infralineaire WHERE id_descriptionsystem = " + str(indexnode1)
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
            if self.userwdgfield.comboBox_branch.currentText() == 'Faux':
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
                sql = "SELECT id_infralineaire FROM Infralineaire WHERE id_descriptionsystem = " + str(indexnode2)
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




    def checkGeometry(self,geomtocheck):
        indexnode1 = self.userwdgfield.spinBox_lk_noeud1.value()
        indexnode2 = self.userwdgfield.spinBox_lk_noeud2.value()

        print('checkGeometry', indexnode1,indexnode2, geomtocheck )

        nearestnodepoint1 = None
        nearestnodepoint2 = None
        if indexnode1 > -1 :
            nearestnodefet1 = self.dbase.getLayerFeatureById('Noeud', indexnode1)
            nearestnodepoint1 = nearestnodefet1.geometry().asPoint()
        if indexnode2 > -1 :
            nearestnodefet2 = self.dbase.getLayerFeatureById('Noeud', indexnode2)
            nearestnodepoint2 = nearestnodefet2.geometry().asPoint()

        print(nearestnodepoint1, nearestnodepoint2,geomtocheck )

        if nearestnodepoint1 :
            if nearestnodepoint1 == geomtocheck[0]:
                print('ok 1')
            elif nearestnodepoint1 in geomtocheck:
                print('ok 1 replace')
                # index1 = geomtocheck.index(nearestnodepoint1)
                geomtocheck.remove(nearestnodepoint1)
                geomtocheck.insert(0, nearestnodepoint1)
            else:
                self.userwdgfield.spinBox_lk_noeud1.setValue(-1)

        if nearestnodepoint2:
            if nearestnodepoint2 == geomtocheck[-1]:
                print('ok 2')
            elif nearestnodepoint2 in geomtocheck:
                print('ok 2 replace')
                geomtocheck.remove(nearestnodepoint2)
                geomtocheck.insert(-1, nearestnodepoint2)
            else:
                self.userwdgfield.spinBox_lk_noeud2.setValue(-1)

        if len(geomtocheck) > 2 :
            geomtocheck = [geomtocheck[0], geomtocheck[-1]]






        return geomtocheck

    """
    
    
    

    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        strid = 'id_' + self.dbasetablename.lower()
        sqlin += ' ORDER BY ' + strid
        return sqlin



    def postInitFeatureProperties(self, feat):
        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')

        pass


    def createParentFeature(self):
        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idobjet = self.dbase.getLastRowId('Objet')



        #sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, id_revisionbegin, id_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(lastrevision) +  "," + str(lastobjetid) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idsys = self.dbase.getLastRowId('Descriptionsystem')

        idtroncon = self.currentFeature.id()
        lastidinfralineaire = self.dbase.getLastId('Infralineaire') + 1



        sql = "UPDATE Infralineaire SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_descriptionsystem = " + str(lastdescriptionsystemid)   + ","
        sql += "id_infralineaire = " + str(lastidinfralineaire)  + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_infralineaire = " + str(idtroncon) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']
        idinfralin= self.currentFeature['id_infralineaire']


        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Infralinemprise WHERE lk_infralineaire = " + str(idinfralin) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True

    """


class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)

