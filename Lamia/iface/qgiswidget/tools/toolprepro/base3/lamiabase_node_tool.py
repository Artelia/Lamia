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


import os
import datetime

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget, QPushButton)

from ...lamia_abstractformtool import AbstractLamiaFormTool
from .lamiabase_camera_tool import BaseCameraTool
from .lamiabase_sketch_tool import BaseSketchTool


def tr(msg):
    return QtCore.QCoreApplication.translate('BaseNodeTool',msg)

class BaseNodeTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'node'
    LOADFIRST = True

    tooltreewidgetCAT = tr('Facilities')
    tooltreewidgetSUBCAT = tr('Nodes')
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_node_tool_icon.svg')

    def __init__(self, **kwargs):
        super(BaseNodeTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs
        


    def initMainToolWidget(self):

        self.toolwidgetmain= UserUI()
        self.formtoolwidgetconfdictmain = {'node' : {'linkfield' : 'id_node',
                                                            'widgets' : {}},
                                            'object' : {'linkfield' : 'id_object',
                                                        'widgets' : {'name': self.toolwidgetmain.lineEdit_libelle}},
                                            'descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                        'widgets' : {}}}



        # ****************************************************************************************
        # child widgets

        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self
        if self.parentWidget is None:
            self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def postSelectFeature(self):
        pass

    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:
            # lastrevision = self.dbase.maxrevision
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')



        #sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pksys = self.dbase.getLastRowId('Descriptionsystem')

        #idnoeud = self.currentFeature.id()
        pknoeud = self.currentFeaturePK
        lastidnoeud = self.dbase.getLastId('Noeud') + 1
        sql = "UPDATE Noeud SET id_noeud = " + str(lastidnoeud)  + ","
        sql += "lpk_descriptionsystem = " + str(pksys)
        sql += " WHERE pk_noeud = " + str(pknoeud) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if  self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            # if "lid_descriptionsystem" in self.dbase.dbasetables[self.parentWidget.dbasetablename]['fields'].keys():
            if 'Descriptionsystem' in self.dbase.getParentTable(self.parentWidget.dbasetablename):

                #parentid
                sql = "SELECT id_descriptionsystem FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
                sql += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
                parentid = self.dbase.query(sql)[0][0]
                #currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
                sql = "UPDATE Noeud SET lid_descriptionsystem_1 = " + str(parentid)
                sql += " WHERE pk_noeud = " + str(pknoeud)
                self.dbase.query(sql)
                self.dbase.commit()
    """




    def postSaveFeature(self, savedfeaturepk=None):
        pass


    def postDeleteFeature(self):
        pass

    def _createDeficiency(self, deficiencywdg):
        if self.currentFeaturePK is None :  #very new equip, not newversion
            deficiencywdg.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('node_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)
            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
            qgsgeomfordesordre = [qgsgeom,qgsgeom]
            deficiencywdg.setTempGeometry(qgsgeomfordesordre)

            deficiencywdg.parentWidget.currentFeaturePK = savedfeaturepk
            deficiencywdg.toolbarSave()
    
    def _moveLinkedTopologicalEdge(self):

        if self.currentFeaturePK is not None:
            nodeiddessys = self.dbase.getValuesFromPk('node_qgis',['id_descriptionsystem'],self.currentFeaturePK )
            nodegeom = self.formutils.getQgsGeomFromPk(self.currentFeaturePK).asPoint()

            # iterate on lid_descriptionsystem_1 and lid_descriptionsystem_2
            valuetoiterate = [1, 2]
            for indexnode in valuetoiterate:
                sql = "SELECT pk_edge, id_edge FROM edge_now "\
                      "WHERE lid_descriptionsystem_{} = {} ".format(str(indexnode ),
                                                                    str(nodeiddessys))
                sql = self.dbase.sqlNow(sql)
                result = self.dbase.query(sql)
                if indexnode == 1 :
                    indexgeom = 0
                elif indexnode == 2:
                    indexgeom = -1

                for fetpk, fetid in result:
                    geomtext = self.dbase.getValuesFromPk('edge',
                                'ST_AsText(geom)',
                                fetpk)
                    infrafetgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()

                    if not self.dbase.utils.areNodesEquals(infrafetgeom[indexgeom], nodegeom):
                        # fetpk = self.mainifacewidget.toolwidgets['toolprepro']['Troncon'][0].formutils.manageFeatureCreationOrUpdate(fetpk)
                        fetpk = self.dbase.manageFeatureCreationOrUpdate('edge', fetpk)

                        infrafetgeom[indexgeom] = nodegeom
                        newgeom = qgis.core.QgsGeometry.fromPolylineXY(infrafetgeom)

                        sql = "UPDATE edge SET geom = ST_GeomFromText('{}',{}) "\
                              " WHERE pk_edge = {}".format(newgeom.asWkt(),
                                                                    self.dbase.crsnumber,
                                                                    fetpk)
                        self.dbase.query(sql)

                        # move laterals
                        self._moveLaterals(fetpk, newgeom)

        self.mainifacewidget.qgiscanvas.layers['edge']['layerqgis'].triggerRepaint()

    def _moveLaterals(self, pkinfralin, newgeom):

        fetiddessys = self.dbase.getValuesFromPk('edge_qgis', 'id_descriptionsystem', pkinfralin)
        dbasetablelayer = self.mainifacewidget.qgiscanvas.layers['edge']['layer']
        sql = "SELECT pk_edge, id_edge FROM edge_now "\
              " WHERE lid_descriptionsystem_2 = {} ".format( str(fetiddessys))
        sql = self.dbase.sqlNow(sql)
        result2 = self.dbase.query(sql)
        for fetpk2, fetid2 in result2:
            # infrafetpk = self.mainifacewidget.toolwidgets['toolprepro']['Troncon'][0].formutils.manageFeatureCreationOrUpdate(fetpk2)
            fetpk = self.dbase.manageFeatureCreationOrUpdate('edge', fetpk)
            geomtext = self.dbase.getValuesFromPk('edge',
                        'ST_AsText(geom)',
                        infrafetpk)
            infrafetgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
            infrafetpoint1 = qgis.core.QgsGeometry().fromPointXY(infrafetgeom[0])
            newgeom2 = infrafetpoint1.shortestLine(newgeom)

            sql = "UPDATE edge SET geom = ST_GeomFromText('{}',{}) "\
                    " WHERE pk_edge = {}".format(newgeom2.asWkt(),
                                                        self.dbase.crsnumber,
                                                        infrafetpk)
            self.dbase.query(sql)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_node_tool_ui.ui')
        uic.loadUi(uipath, self)