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

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QPushButton)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base.lamiabase_noeud_tool import BaseNoeudTool

import os
import qgis
import datetime
from ..base.lamiabase_photo_tool import BasePhotoTool
from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
from ..base.lamiabase_croquis_tool import BaseCroquisTool
from .lamiabaseassainissement_desordre_tool import BaseAssainissementDesordreTool
from .lamiabaseassainissement_equipement_tool import BaseAssainissementEquipementTool




class BaseAssainissementNoeudTool(BaseNoeudTool):

    LOADFIRST = True
    dbasetablename = 'Noeud'


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseAssainissementNoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)



    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Noeud'
        self.dbasetablename = 'Noeud'
        self.visualmode = [0, 1, 2]
        self.PointENABLED = True
        # self.LineENABLED = False
        # self.PolygonENABLED = True
        self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__),'..','base', 'lamiabase_noeud_tool_icon.svg')


        # ****************************************************************************************
        #properties ui
        pass



    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Noeud' : {'linkfield' : 'id_noeud',
                                             'widgets' : {
                                                         'typeReseau': self.userwdgfield.comboBox_typeReseau,
                                                         'typeOuvrageAss': self.userwdgfield.comboBox_typeOuvrageAss,
                                                         'accessibilite': self.userwdgfield.comboBox_accessibilite,
                                                         'cloisonsiphoide': self.userwdgfield.comboBox_cloisonsiphoide,
                                                        'couvercle': self.userwdgfield.comboBox_couvercle,

                                                         'X': self.userwdgfield.doubleSpinBox_X,
                                                         'dX': self.userwdgfield.doubleSpinBox_dX,
                                                         'Y': self.userwdgfield.doubleSpinBox_Y,
                                                         'dY': self.userwdgfield.doubleSpinBox_dY,
                                                         'Z': self.userwdgfield.doubleSpinBox_Z,
                                                         'dZ': self.userwdgfield.doubleSpinBox_dZ,

                                                         'profradierouvrage': self.userwdgfield.doubleSpinBox_profradierouvrage
                                                        }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire' : self.userwdgfield.textBrowser_commentaire}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}

            self.userwdgfield.toolButton_calc.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_profradierouvrage))

            self.userwdgfield.pushButton_getGPS.clicked.connect(self.getGPSValue)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgDesordre = BaseAssainissementDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            self.propertieswdgDesordre.groupBox_elements.setParent(None)
            self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)

            self.propertieswdgEquipement = BaseAssainissementEquipementTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgEquipement)


            self.gpswidget = {'x' : {'widget' : self.userwdgfield.label_X,
                                     'gga' : 'Xcrs'},
                              'y': {'widget': self.userwdgfield.label_Y,
                                    'gga': 'Ycrs'},
                              'zmngf': {'widget': self.userwdgfield.label_Z,
                                    'gga': 'zmNGF'},
                              'dx': {'widget': self.userwdgfield.label_dX,
                                    'gst': 'xprecision'},
                              'dy': {'widget': self.userwdgfield.label_dY,
                                    'gst': 'yprecision'},
                              'dz': {'widget': self.userwdgfield.label_dZ,
                                    'gst': 'zprecision'},
                              'zgps': {'widget': self.userwdgfield.label_zgps,
                                     'gga': 'elevation'},
                              'zwgs84': {'widget': self.userwdgfield.label_zwgs84,
                                       'gga': 'deltageoid'},
                              'raf09': {'widget': self.userwdgfield.label_raf09,
                                       'gga': 'RAF09'},
                              'hauteurperche': {'widget': self.userwdgfield.label_hautperche,
                                        'gga': 'hauteurperche'}
                              }





    def addGPSPoint(self):
        if self.gpsutil.currentpoint is None:
            self.windowdialog.errorMessage('GPS non connecte')
            return

        self.createorresetRubberband(0)

        layerpoint = self.gpsutil.currentpoint


        self.setTempGeometry([layerpoint],False)

        self.getGPSValue()



    def magicFunction(self):
        self.featureSelected()
        #self.lastPhoto()
        self.addGPSPoint()
        self.saveFeature()


    def getGPSValue(self):
        self.assignValue(self.userwdgfield.label_X, self.userwdgfield.doubleSpinBox_X)
        self.assignValue(self.userwdgfield.label_dX, self.userwdgfield.doubleSpinBox_dX)
        self.assignValue(self.userwdgfield.label_Y, self.userwdgfield.doubleSpinBox_Y)
        self.assignValue(self.userwdgfield.label_dY, self.userwdgfield.doubleSpinBox_dY)
        self.assignValue(self.userwdgfield.label_Z, self.userwdgfield.doubleSpinBox_Z)
        self.assignValue(self.userwdgfield.label_dZ, self.userwdgfield.doubleSpinBox_dZ)


    def assignValue(self,wdgfrom, wdgto):
        if self.isfloat(wdgfrom.text()):
            wdgto.setValue(float(wdgfrom.text()))

    def isfloat(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    def postSaveFeature(self, boolnewfeature):


        #adapt linked infralin geoemtry
        if self.currentFeature is not None:
            nodeid = self.currentFeature.id()
            nodedesys = self.currentFeature['id_descriptionsystem']
            nodegeom = self.currentFeature.geometry().asPoint()
            movebranchement = False

            sql = "SELECT id_infralineaire, lk_descriptionsystem1 FROM Infralineaire WHERE lk_descriptionsystem1 = " + str(nodedesys)
            query = self.dbase.query(sql)
            result = [row for row in query]
            for fetid,lknoeud1 in result:
                infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid)
                infrafetgeom = infrafet.geometry().asPolyline()
                infrafetgeom[0] = nodegeom
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    newgeom = qgis.core.QgsGeometry.fromPolyline(infrafetgeom)
                else:
                    newgeom = qgis.core.QgsGeometry.fromPolylineXY(infrafetgeom)

                dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                dbasetablelayer.startEditing()
                if not self.dbase.revisionwork:
                    success = dbasetablelayer.changeGeometry(fetid, newgeom)
                else:
                    success = dbasetablelayer.changeGeometry(infrafet.id(), newgeom)

                dbasetablelayer.commitChanges()

                #move branchement
                sql = "SELECT id_infralineaire FROM Infralineaire WHERE lk_descriptionsystem2 = " + str(infrafet['id_descriptionsystem'])
                query = self.dbase.query(sql)
                result2 = [row[0] for row in query]
                for fetid2 in result2:
                    infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid2)
                    infrafetpoint1 = qgis.core.QgsGeometry().fromPoint(infrafet.geometry().asPolyline()[0])
                    # newgeom2 = newgeom.shortestLine(infrafetpoint1)
                    newgeom2 = infrafetpoint1.shortestLine(newgeom)
                    dbasetablelayer.startEditing()
                    if not self.dbase.revisionwork:
                        success = dbasetablelayer.changeGeometry(fetid2, newgeom2)
                    else:
                        success = dbasetablelayer.changeGeometry(infrafet.id(), newgeom2)
                    dbasetablelayer.commitChanges()




                movebranchement = True
                # print('lk1', success, fetid, newgeom.asPolyline())

            sql = "SELECT id_infralineaire, lk_descriptionsystem2 FROM Infralineaire WHERE lk_descriptionsystem2 = " + str(nodedesys)
            query = self.dbase.query(sql)
            result = [row for row in query]

            for fetid,lknoeud2 in result:
                infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid)
                infrafetgeom = infrafet.geometry().asPolyline()
                infrafetgeom[1] = nodegeom

                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    newgeom = qgis.core.QgsGeometry.fromPolyline(infrafetgeom)
                else:
                    newgeom = qgis.core.QgsGeometry.fromPolylineXY(infrafetgeom)

                dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                dbasetablelayer.startEditing()
                if not self.dbase.revisionwork:
                    success = dbasetablelayer.changeGeometry(fetid, newgeom)
                else:
                    success = dbasetablelayer.changeGeometry(infrafet.id(), newgeom)
                dbasetablelayer.commitChanges()

                sql = "SELECT id_infralineaire FROM Infralineaire WHERE lk_descriptionsystem2 = " + str(infrafet['id_descriptionsystem'])
                query = self.dbase.query(sql)
                result2 = [row[0] for row in query]
                for fetid2 in result2:
                    infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid2)
                    infrafetpoint1 = qgis.core.QgsGeometry().fromPoint(infrafet.geometry().asPolyline()[0])
                    # newgeom2 = newgeom.shortestLine(infrafetpoint1)
                    newgeom2 = infrafetpoint1.shortestLine(newgeom)
                    dbasetablelayer.startEditing()
                    if not self.dbase.revisionwork:
                        success = dbasetablelayer.changeGeometry(fetid2, newgeom2)
                    else:
                        success = dbasetablelayer.changeGeometry(infrafet.id(), newgeom2)
                    dbasetablelayer.commitChanges()



            sql = "SELECT id_equipement FROM Equipement WHERE lk_descriptionsystem = " + str(nodedesys)
            query = self.dbase.query(sql)
            result = [row[0] for row in query]

            for fetid in result:
                equipfet = self.dbase.getLayerFeatureById('Equipement', fetid)
                #infrafetgeom = equipfet.geometry().asPoint()
                #infrafetgeom[1] = nodegeom


                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    newgeom = qgis.core.QgsGeometry.fromPolyline([nodegeom,nodegeom])
                else:
                    newgeom = qgis.core.QgsGeometry.fromPolylineXY([nodegeom,nodegeom])

                dbasetablelayer = self.dbase.dbasetables['Equipement']['layer']
                dbasetablelayer.startEditing()
                if not self.dbase.revisionwork:
                    success = dbasetablelayer.changeGeometry(fetid, newgeom)
                else:
                    success = dbasetablelayer.changeGeometry(equipfet.id(), newgeom)
                dbasetablelayer.commitChanges()





        #self.canvas.freeze(False)
        #self.canvas.refresh()
        self.dbase.dbasetables['Infralineaire']['layerqgis'].triggerRepaint()

        #create desordre
        # if boolnewfeature and self.currentFeature['categorie'] == 'OUH':
        if boolnewfeature :
            self.propertieswdgDesordre.featureSelected()
            self.propertieswdgDesordre.tempgeometry = self.currentFeature.geometry()
            combocrtindex = self.propertieswdgDesordre.userwdgfield.comboBox_groupedes.findText('Noeud')
            self.propertieswdgDesordre.userwdgfield.comboBox_groupedes.setCurrentIndex(combocrtindex)
            self.propertieswdgDesordre.saveFeature()
        #self.dbase.printsql = False

    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):
        lastrevision = self.dbase.maxrevision
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

        idnoeud = self.currentFeature.id()
        lastidnoeud = self.dbase.getLastId('Noeud') + 1


        sql = "UPDATE Noeud SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_descriptionsystem = " + str(lastdescriptionsystemid)   + ","
        sql += "id_noeud = " + str(lastidnoeud)  + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_noeud = " + str(idnoeud) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()




    def postSaveFeature(self, boolnewfeature):
        pass


    def postDeleteFeature(self):
        pass

    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']
        # idnoeud= self.currentFeature['id_noeud']


        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        return True
    """

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)