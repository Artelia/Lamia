# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_infralineaire_tool import AbstractInfraLineaireTool
from .lamiadigue_photos_tool import PhotosTool
from .lamiadigue_rapport_tool import RapportTool
from .lamiadigue_tronconemprise_tool  import TronconEmpriseTool
from .lamiadigue_croquis_tool import CroquisTool
from .lamiadigue_profil_tool import ProfilTool
from .lamiadigue_desordre_tool import DesordreTool
# from ..InspectionDigue_graphique_tool import GraphiqueTool
# from .InspectionDigue_profiltravers_tool  import ProfilTraversTool
from ...toolpostpro.InspectionDigue_path_tool import PathTool
from .lamiadigue_graphique_tool  import GraphiqueTool
from ..abstract.lamia_photoviewer import PhotoViewer
import os
import datetime
import logging
import time
debugtime = False



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


        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            self.userwdgfield = UserUIField()

            self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                       'widgets': {'description1': self.userwdgfield.comboBox_type,
                                                                   'description2': self.userwdgfield.comboBox_contitution,
                                                                   'aubaredelargeur': self.userwdgfield.comboBox_aubaredelargeur,
                                                                   'aubaredevegherbacee': self.userwdgfield.comboBox_aubaredevegherbacee,
                                                                   'aubaredevegarbustive': self.userwdgfield.comboBox_aubaredevegarbustive,
                                                                   'aubaredevegarboree': self.userwdgfield.comboBox_aubaredevegarboree,
                                                                   'aubaredecommentaire': self.userwdgfield.textBrowser_aubaredecommentaire
                                                                   }},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {'libelle': self.userwdgfield.lineEdit_nom,
                                                           'commentaire': self.userwdgfield.textBrowser_comm}},
                                     'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                           'widgets': {}}}

            self.dbasechildwdgfield = []

            self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgDesordre = DesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)



    def initDesktopUI(self):

        # ****************************************************************************************
        # userui Desktop
        if self.userwdgdesktop is None:
            self.userwdgdesktop = UserUI()

            self.linkuserwdgdesktop = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                         'widgets': {'description1': self.userwdgdesktop.comboBox_type,
                                                                     'description2': self.userwdgdesktop.comboBox_contitution,
                                                                     'classement': self.userwdgdesktop.comboBox_classement,
                                                                     'aubaredelargeur': self.userwdgdesktop.comboBox_aubaredelargeur,
                                                                     'aubaredevegherbacee': self.userwdgdesktop.comboBox_aubaredevegherbacee,
                                                                     'aubaredevegarbustive': self.userwdgdesktop.comboBox_aubaredevegarbustive,
                                                                     'aubaredevegarboree': self.userwdgdesktop.comboBox_aubaredevegarboree,
                                                                     'aubaredecommentaire': self.userwdgdesktop.textBrowser_aubaredecommentaire
                                                                     }},
                                       'Objet': {'linkfield': 'id_objet',
                                                 'widgets': {'libelle': self.userwdgdesktop.lineEdit_nom,
                                                             'commentaire': self.userwdgdesktop.textBrowser_comm}},
                                       'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                             'widgets': {}}}

            self.userwdgdesktop.pushButton_defineinter.clicked.connect(self.manageLinkage)

            if True:
                self.photowdg = PhotoViewer()
                self.userwdgdesktop.tabWidget.widget(0).layout().addWidget(self.photowdg)
            if True:
                self.croquisprofilwdg = PhotoViewer()
                self.userwdgdesktop.stackedWidget_profiltravers.widget(0).layout().addWidget(self.croquisprofilwdg)

                self.graphprofil = GraphiqueTool(dbase=self.dbase, parentwidget=self)
                self.userwdgdesktop.stackedWidget_profiltravers.widget(1).layout().addWidget(self.graphprofil.pyqtgraphwdg)
                # self.userwdg.frame_graph.layout().addWidget(self.pyqtgraphwdg)

            if True:
                self.propertieswdgPROFILLONG = PathTool(dbase=self.dbase, parentwidget=self)
                self.userwdgdesktop.tabWidget.widget(2).layout().addWidget(self.propertieswdgPROFILLONG.plotWdg)
            else:
                self.propertieswdgPROFILLONG = None

            self.dbasechildwdgdesktop = []
            if True:

                self.propertieswdgRAPPORT = RapportTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgdesktop.append(self.propertieswdgRAPPORT)

                self.propertieswdgTRONCONEMPRISE = TronconEmpriseTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgdesktop.append(self.propertieswdgTRONCONEMPRISE)


                self.propertieswdgPROFIL = ProfilTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgdesktop.append(self.propertieswdgPROFIL)

            self.initWidgets()


        if False:
            # ****************************************************************************************
            #   userui Field
            self.userwdgfield = UserUIField()

            self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                       'widgets': {'description1':self.userwdgfield.comboBox_type,
                                                              'description2': self.userwdgfield.comboBox_contitution}},
                                'Objet': {'linkfield': 'id_objet',
                                          'widgets': {'libelle': self.userwdgfield.lineEdit_nom,
                                                       'commentaire': self.userwdgfield.textBrowser_comm}},
                                'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                      'widgets': {}}}

            # ****************************************************************************************
            # userui Desktop
            self.userwdgdesktop = UserUI()

            self.linkuserwdgdesktop = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                  'widgets': {'description1':self.userwdgdesktop.comboBox_type,
                                                              'description2': self.userwdgdesktop.comboBox_contitution,
                                                              'classement': self.userwdgdesktop.comboBox_classement}},
                                'Objet': {'linkfield': 'id_objet',
                                          'widgets': {'libelle': self.userwdgdesktop.lineEdit_nom,
                                                       'commentaire': self.userwdgdesktop.textBrowser_comm}},
                                'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                      'widgets': {}}}


            self.userwdgdesktop.pushButton_defineinter.clicked.connect(self.manageLinkage)

            if True:
                self.photowdg = Label()
                self.userwdgdesktop.tabWidget.widget(0).layout().addWidget(self.photowdg)
            if True:
                self.croquisprofilwdg = Label()
                self.userwdgdesktop.stackedWidget_profiltravers.widget(0).layout().addWidget(self.croquisprofilwdg)

                self.graphprofil = GraphiqueTool(dbase=self.dbase, parentwidget=self)
                self.userwdgdesktop.stackedWidget_profiltravers.widget(1).layout().addWidget(self.graphprofil.pyqtgraphwdg)
                #self.userwdg.frame_graph.layout().addWidget(self.pyqtgraphwdg)



            if True:
                self.propertieswdgPROFILLONG = PathTool(dbase=self.dbase, parentwidget=self)
                self.userwdgdesktop.tabWidget.widget(2).layout().addWidget(self.propertieswdgPROFILLONG.plotWdg)
            else:
                self.propertieswdgPROFILLONG = None








            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.dbasechildwdgdesktop = []
            if True:
                self.dbasechildwdg=[]
                self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
                self.dbasechildwdgdesktop.append(self.propertieswdgPHOTOGRAPHIE)

                self.propertieswdgRAPPORT = RapportTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgdesktop.append(self.propertieswdgRAPPORT)

                self.propertieswdgTRONCONEMPRISE = TronconEmpriseTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgdesktop.append(self.propertieswdgTRONCONEMPRISE)

                self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
                self.dbasechildwdgdesktop.append(self.propertieswdgCROQUIS)

                self.propertieswdgPROFIL = ProfilTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgdesktop.append(self.propertieswdgPROFIL)

            if False:
                self.dbasechildwdg = [self.dbase.dbasetables['Photo']['widget'],
                                      self.dbase.dbasetables['Rapport']['widget']]

            if False:
                self.dbasechildwdg = {'photo': [self.dbase.dbasetables['Photo']['widget'], 0]
                                      }



            if False:
                self.propertieswdgPROFILTRAVERS = ProfilTraversTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdg.append(self.propertieswdgPROFILTRAVERS)

            if debugtime: logging.getLogger('Lamia').debug('End init %s', str(round(time.clock() - timestart, 3)))

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
            if self.userwdg == self.userwdgdesktop:
                # intervenants
                sql = "SELECT Tcobjetintervenant.fonction, Intervenant.nom,Intervenant.societe  FROM Tcobjetintervenant "
                sql += " INNER JOIN Intervenant ON Tcobjetintervenant.id_tcintervenant = Intervenant.id_intervenant "
                sql += "WHERE id_tcobjet = " + str(self.currentFeature['id_objet'])
                query = self.dbase.query(sql)
                result = "\n".join([str(row) for row in query])
                self.userwdgdesktop.textBrowser_intervenants.clear()
                self.userwdgdesktop.textBrowser_intervenants.append(result)

                #photo
                lkphoto = self.currentFeature['lk_photo']
                if not self.dbase.isAttributeNull(lkphoto):
                    sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_objet = "
                    sql += str(self.currentFeature['lk_photo'])
                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    filephoto = result[0][0]
                    completefilephoto = self.dbase.completePathOfFile(filephoto)
                    self.showImageinLabelWidget(self.photowdg, completefilephoto)
                else:
                    self.photowdg.clear()

                #profil travers
                lkressourceprofile = self.currentFeature['lk_profil']
                if not self.dbase.isAttributeNull(lkressourceprofile):
                    sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_ressource = "
                    sql += str(lkressourceprofile)
                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    if len(result)>0:
                        self.userwdgdesktop.stackedWidget_profiltravers.setCurrentIndex(0)
                        filephoto = result[0][0]
                        completefilephoto = self.dbase.completePathOfFile(filephoto)
                        self.showImageinLabelWidget(self.croquisprofilwdg, completefilephoto)
                    else:
                        self.croquisprofilwdg.clear()

                    sql = "SELECT id_graphique FROM Graphique  WHERE id_ressource = " + str(lkressourceprofile)
                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    if len(result) > 0:
                        self.userwdgdesktop.stackedWidget_profiltravers.setCurrentIndex(1)
                        idgraphique = result[0][0]
                        self.graphprofil.featureSelected(idgraphique,True)
                else:
                    self.userwdgdesktop.stackedWidget_profiltravers.setCurrentIndex(0)
                    self.croquisprofilwdg.clear()



                if not self.dbase.isAttributeNull(lkphoto):
                    sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_objet = "
                    sql += str(self.currentFeature['lk_photo'])
                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    filephoto = result[0][0]
                    completefilephoto = self.dbase.completePathOfFile(filephoto)
                    self.showImageinLabelWidget(self.photowdg, completefilephoto)
                else:
                    self.photowdg.clear()


                #profil long
                if self.propertieswdgPROFILLONG is not None:
                    self.propertieswdgPROFILLONG.activateMouseTracking(0)
                    self.propertieswdgPROFILLONG.rubberbandtrack.hide()
                    self.propertieswdgPROFILLONG.rubberBand.reset(self.dbase.dbasetables['Infralineaire']['layer'].geometryType())
                    currentgeom = self.currentFeature.geometry().asPolyline()
                    self.propertieswdgPROFILLONG.computePath(list(currentgeom[0]), list(currentgeom[-1]))
                    self.propertieswdgPROFILLONG.activateMouseTracking(2)
                    self.propertieswdgPROFILLONG.rubberbandtrack.hide()
                    self.propertieswdgPROFILLONG.rubberBand.reset(self.dbase.dbasetables['Infralineaire']['layer'].geometryType())



    """
    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idsys = self.dbase.getLastRowId('Descriptionsystem')

        idtroncon = self.currentFeature.id()

        sql = "UPDATE Infralineaire SET id_objet = " + str(idobjet) + ",id_descriptionsystem = " + str(idsys) + " WHERE id_infralineaire = " + str(idtroncon) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()

        geom = self.currentFeature.geometry().buffer(10.0, 12)
        geom.convertToMultiType()
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            geombase = geom.exportToWkt()
        else:
            geombase = geom.asWkt()
        crs = self.dbasetable['layer'].crs().authid().split(':')[1]
        sql = "INSERT INTO Infralinemprise (lk_infralineaire,geom) VALUES(" + str(idtroncon) + ",ST_GeomFromText('" + geombase + "'," + crs + "));"
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



    def showImageinLabelWidget(self,wdg,savedfile):
        file = self.dbase.completePathOfFile(savedfile)
        if os.path.isfile(file):
            #wdg.clear()
            wdg.setPixmap(file)
        else:
            wdg.clear()
            wdg.setText('Image non trouvee')

    """
    def postDeleteFeature(self):
        idobjet = self.currentFeature['IdObjet']
        datesuppr = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "UPDATE Objet SET datedestruction = '" + datesuppr + "'  WHERE id = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()
    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiadigue_infralineaire_tooldesktop_ui.ui')
        uic.loadUi(uipath, self)

class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiadigue_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)
