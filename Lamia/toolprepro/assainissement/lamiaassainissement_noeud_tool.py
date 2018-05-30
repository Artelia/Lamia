# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QPushButton)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_noeud_tool import AbstractNoeudTool

from .lamiaassainissement_photos_tool import PhotosTool

from .lamiaassainissement_croquis_tool import CroquisTool
from .lamiaassainissement_desordre_tool import DesordreTool
from .lamiaassainissement_equipement_tool import EquipementTool

import os
import datetime
import qgis



class NoeudTool(AbstractNoeudTool):

    LOADFIRST = True
    dbasetablename = 'Noeud'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(NoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)


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
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiaassainissement_noeud_tool_icon.svg')


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
                                             'widgets' : {'typeReseau': self.userwdgfield.comboBox_typeReseau,
                                                            'typeOuvrageAss': self.userwdgfield.comboBox_typeOuvrageAss,
                                                          'accessibilite': self.userwdgfield.comboBox_accessibilite,
                                                          'cloisonsiphoide': self.userwdgfield.comboBox_cloisonsiphoide,

                                                          'X' : self.userwdgfield.doubleSpinBox_X,
                                                          'dX': self.userwdgfield.doubleSpinBox_dX,
                                                          'Y': self.userwdgfield.doubleSpinBox_Y,
                                                          'dY': self.userwdgfield.doubleSpinBox_dY,
                                                          'Z': self.userwdgfield.doubleSpinBox_Z,
                                                          'dZ': self.userwdgfield.doubleSpinBox_dZ,

                                                          'profradierouvrage': self.userwdgfield.doubleSpinBox_profradierouvrage


                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}

            self.userwdgfield.toolButton_calc.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_profradierouvrage))

            self.userwdgfield.pushButton_getGPS.clicked.connect(self.getGPSValue)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgDesordre = DesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            self.propertieswdgDesordre.groupBox_elements.setParent(None)
            self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)

            self.propertieswdgEquipement = EquipementTool(dbase=self.dbase, parentwidget=self)
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

    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postSaveFeature(self, boolnewfeature):


        #adapt linked infralin geoemtry
        if self.currentFeature is not None:
            nodeid = self.currentFeature.id()
            nodedesys = self.currentFeature['id_descriptionsystem']
            nodegeom = self.currentFeature.geometry().asPoint()
            movebranchement = False

            sql = "SELECT id_infralineaire, lk_noeud1 FROM Infralineaire WHERE lk_noeud1 = " + str(nodedesys)
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
                success = dbasetablelayer.changeGeometry(fetid, newgeom)

                dbasetablelayer.commitChanges()

                sql = "SELECT id_infralineaire FROM Infralineaire WHERE lk_noeud2 = " + str(infrafet['id_descriptionsystem'])
                query = self.dbase.query(sql)
                result2 = [row[0] for row in query]
                for fetid2 in result2:
                    infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid2)
                    infrafetpoint1 = qgis.core.QgsGeometry().fromPoint(infrafet.geometry().asPolyline()[0])
                    # newgeom2 = newgeom.shortestLine(infrafetpoint1)
                    newgeom2 = infrafetpoint1.shortestLine(newgeom)
                    dbasetablelayer.startEditing()
                    success = dbasetablelayer.changeGeometry(fetid2, newgeom2)
                    dbasetablelayer.commitChanges()




                movebranchement = True
                # print('lk1', success, fetid, newgeom.asPolyline())

            sql = "SELECT id_infralineaire, lk_noeud2 FROM Infralineaire WHERE lk_noeud2 = " + str(nodedesys)
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
                success = dbasetablelayer.changeGeometry(fetid, newgeom)
                dbasetablelayer.commitChanges()

                sql = "SELECT id_infralineaire FROM Infralineaire WHERE lk_noeud2 = " + str(infrafet['id_descriptionsystem'])
                query = self.dbase.query(sql)
                result2 = [row[0] for row in query]
                for fetid2 in result2:
                    infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid2)
                    infrafetpoint1 = qgis.core.QgsGeometry().fromPoint(infrafet.geometry().asPolyline()[0])
                    # newgeom2 = newgeom.shortestLine(infrafetpoint1)
                    newgeom2 = infrafetpoint1.shortestLine(newgeom)
                    dbasetablelayer.startEditing()
                    success = dbasetablelayer.changeGeometry(fetid2, newgeom2)
                    dbasetablelayer.commitChanges()









        #self.canvas.freeze(False)
        #self.canvas.refresh()
        self.dbase.dbasetables['Infralineaire']['layerqgis'].triggerRepaint()

        #create desordre
        # if boolnewfeature and self.currentFeature['categorie'] == 'OUH':
        if boolnewfeature :
            self.propertieswdgDesordre.featureSelected()
            self.propertieswdgDesordre.tempgeometry = self.currentFeature.geometry()
            self.propertieswdgDesordre.saveFeature()
        #self.dbase.printsql = False

    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']
        iddescriptionsystem = self.currentFeature['id_descriptionsystem']
        # idnoeud= self.currentFeature['id_noeud']


        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Desordre WHERE lk_descriptionsystem = " + str(iddescriptionsystem) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        return True


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiaassainissement_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)
