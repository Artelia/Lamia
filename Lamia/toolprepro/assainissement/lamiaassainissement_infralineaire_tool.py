# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_infralineaire_tool import AbstractInfraLineaireTool
from .lamiaassainissement_photos_tool import PhotosTool

from .lamiaassainissement_croquis_tool import CroquisTool

# from ..InspectionDigue_graphique_tool import GraphiqueTool
# from .InspectionDigue_profiltravers_tool  import ProfilTraversTool
from ...toolpostpro.InspectionDigue_path_tool import PathTool

from ..abstract.lamia_photoviewer import PhotoViewer
from .lamiaassainissement_desordre_tool import DesordreTool
import os
import datetime
import logging
import time
debugtime = False
import qgis



class InfraLineaireTool(AbstractInfraLineaireTool):

    LOADFIRST = True
    dbasetablename = 'Infralineaire'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(InfraLineaireTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

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
        self.picksender = None

        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiaassainissement_infralineaire_tool_icon.svg')


        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            self.userwdgfield = UserUIField()
            # self.pushButton_addLine.setEnabled(False)

            self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                       'widgets': {'typeReseau': self.userwdgfield.comboBox_typeReseau,
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
                                                                   'lk_noeud1': self.userwdgfield.spinBox_lk_noeud1,
                                                                   'lk_noeud2': self.userwdgfield.spinBox_lk_noeud2,

                                                                   'infracommentaire': self.userwdgfield.textBrowser_commentaire,

                                                                   }},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {}},
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

            self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgDesordre = DesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            if False:
                self.propertieswdgDesordre.groupBox_elements.setParent(None)
                self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
                self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
                self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
                self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')

        if self.currentFeature is None:
            pass
        else:
            pass


    def pickToNode(self):
        print('pick',self.sender())
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
            nearestnodeid, distance  = self.dbase.getNearestId(self.dbase.dbasetables['Noeud'],
                                                  'Noeud',
                                                  point)
            nearestnodefet = self.dbase.getLayerFeatureById('Noeud', nearestnodeid)
            nearestnodepoint = nearestnodefet.geometry().asPoint()
        else:
            nearestnodeid, distance  = self.dbase.getNearestId(self.dbase.dbasetables['Infralineaire'],
                                                  'Infralineaire',
                                                  point)
            nearestnodefet = self.dbase.getLayerFeatureById('Infralineaire', nearestnodeid)
            nearestnodepoint = nearestnodefet.geometry().nearestPoint(qgis.core.QgsGeometry.fromPoint(point)).asPoint()

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
            if len(geomlist)>=2:
                if editingnode == 1:
                    geomlist[0] = nearestnodepoint
                    # geomlist.insert(0,nearestnodepoint )
                elif editingnode == 2:
                    geomlist[-1] = nearestnodepoint
                    # geomlist.insert(-1, nearestnodepoint)
            else:
                if len(geomlist) == 0 :
                    geomlist.append(nearestnodepoint)
                elif len(geomlist) == 1 :
                    if editingnode == 1:
                        geomlist.insert(0,nearestnodepoint)
                    elif editingnode == 2:
                        geomlist.insert(-1,nearestnodepoint)
        if False:

            if editingnode == 1:
                geomlist[0] = nearestnodepoint
                # geomlist.insert(0,nearestnodepoint )
            elif editingnode == 2:
                geomlist[-1] = nearestnodepoint
                # geomlist.insert(-1, nearestnodepoint)
        if True :
            geomlist=[None,None]

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


        #update canvas
        self.createorresetRubberband(1)
        self.setTempGeometry(geomlist,False)

        # disconnect all
        self.canvas.unsetMapTool(self.pointEmitter)
        self.picksender = None
        try:
            self.pointEmitter.canvasClicked.disconnect(self.picknearestnode)
        except:
            pass

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

        mapgeometry = [mapgeometry[0]]

        self.captureGeometry(listpointinitialgeometry=mapgeometry, type=1)



    def postSaveFeature(self, boolnewfeature):

        self.currentFeature = self.dbase.getLayerFeatureById(self.dbasetablename, self.currentFeature.id())
        fetgeom = self.currentFeature.geometry().asPolyline()



        print('**********   postSaveFeature  *******************')
        print(fetgeom)



        if True:
            indexnode1 = self.userwdgfield.spinBox_lk_noeud1.value()
            if indexnode1 > -1 :
                sql = "SELECT id_noeud FROM Noeud WHERE id_descriptionsystem = " + str(indexnode1)
                query = self.dbase.query(sql)
                ids = [row for row in query]
                # print(sql,ids )
                if len(ids) == 1:
                    iddessys = ids[0][0]
                    nearestnodefet1 = self.dbase.getLayerFeatureById('Noeud', iddessys)
                    nearestnodepoint1 = nearestnodefet1.geometry().asPoint()
                    # print('indexnode1',iddessys,nearestnodepoint1)

                    #if nearestnodepoint1 != fetgeom[0] :
                    if not self.dbase.areNodesEquals(fetgeom[0], nearestnodepoint1):
                        # print('areNodesEquals')
                        # if nearestnodepoint1 == fetgeom[-1] :
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


            indexnode2 = self.userwdgfield.spinBox_lk_noeud2.value()
            # print(self.userwdgfield.comboBox_branch.currentText(), self.userwdgfield.spinBox_lk_noeud2.value())
            if indexnode2 > -1:
                if self.userwdgfield.comboBox_branch.currentText() == 'Faux':
                    sql = "SELECT id_noeud FROM Noeud WHERE id_descriptionsystem = " + str(indexnode2)
                    query = self.dbase.query(sql)
                    ids = [row for row in query]
                    # print(sql,ids )
                    if len(ids) == 1:
                        iddessys = ids[0][0]
                        nearestnodefet2 = self.dbase.getLayerFeatureById('Noeud', iddessys)
                        nearestnodepoint2 = nearestnodefet2.geometry().asPoint()
                        # print('indexnode2', iddessys, nearestnodepoint2)
                        #print(nearestnodepoint2,fetgeom[0], fetgeom[0] ==  nearestnodepoint2)
                        # print(self.dbase.areNodesEquals(fetgeom[0],nearestnodepoint2 ))

                        #if nearestnodepoint2 != fetgeom[-1]:
                        if not self.dbase.areNodesEquals(fetgeom[-1], nearestnodepoint2):
                            #if nearestnodepoint2 == fetgeom[0] :
                            if self.dbase.areNodesEquals(fetgeom[0],nearestnodepoint2 ):
                                # print('av', fetgeom)
                                fetgeom = fetgeom[::-1]
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    newgeom = qgis.core.QgsGeometry.fromPolyline(fetgeom)
                                else:
                                    newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                                dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                                dbasetablelayer.startEditing()
                                success = dbasetablelayer.changeGeometry(self.currentFeature.id(), newgeom)
                                dbasetablelayer.commitChanges()
                                # print('av', self.currentFeature.geometry().asPolyline())
                            else:
                                self.userwdgfield.spinBox_lk_noeud2.setValue(-1)
                                self.saveFeatureProperties()

                else:
                    sql = "SELECT id_infralineaire FROM Infralineaire WHERE id_descriptionsystem = " + str(indexnode2)
                    query = self.dbase.query(sql)
                    ids = [row for row in query]
                    # print(sql,ids )
                    if len(ids) == 1:
                        iddessys = ids[0][0]
                        nearestnodefet2 = self.dbase.getLayerFeatureById('Infralineaire', iddessys)
                        nearestnodepoint2 = nearestnodefet2.geometry()
                        # print('indexnode2', iddessys, nearestnodepoint2)
                        # print(nearestnodepoint2.exportToWkt(), self.currentFeature.geometry().exportToWkt())
                        resultintersect = nearestnodepoint2.buffer(0.01,12).intersects(self.currentFeature.geometry())
                        # print('resultintersect',resultintersect)
                        if not resultintersect:
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



class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiaassainissement_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)
