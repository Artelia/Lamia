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

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)

from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool

"""
from .lamiadigue_photos_tool import PhotosTool
from .lamiadigue_rapport_tool import RapportTool
from .lamiadigue_tronconemprise_tool  import TronconEmpriseTool
from .lamiadigue_croquis_tool import CroquisTool
from .lamiadigue_profil_tool import ProfilTool
# from ..InspectionDigue_graphique_tool import GraphiqueTool
# from .InspectionDigue_profiltravers_tool  import ProfilTraversTool
from ...toolpostpro.InspectionDigue_path_tool import PathTool
from .lamiadigue_graphique_tool  import GraphiqueTool
"""

from .lamiavnf_equipement_tool import EquipementTool
from .lamiavnf_photos_tool import PhotosTool

import os
import datetime
import logging
import time
debugtime = False



class InfraLineaireTool(AbstractInspectionDigueTool):

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
        self.NAME = 'Bief'
        self.dbasetablename = 'Infralineaire'
        # self.visualmode = [0, 1, 2]
        # self.PointEnabled = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        """
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_objet',
                                            'idtcsource' : 'id_tcobjet',
                                           'iddest' : 'id_intervenant',
                                           'idtcdest' : 'id_tcintervenant',
                                           'desttable' : ['Intervenant']}
                                            }
        """
        self.pickTable = {'LkZoneGeo': {'ZONEGEO': 'ID'}}
        self.debug = False

        self.qtreewidgetfields = ['ouvrage', 'art_pk_debut', 'art_pk_fin']


        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            self.userwdgfield = UserUIField()

            self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                       'widgets': {
                                                                    'ouvrage': self.userwdgfield.spinBox_num_ouvrage,
                                                                    'commentaire': self.userwdgfield.textBrowser_comm,
                                                                    'art_pk_debut': self.userwdgfield.doubleSpinBox_pkdebut,
                                                                    'art_pk_fin': self.userwdgfield.doubleSpinBox_pkfin,
                                                                   'nbre_pass': self.userwdgfield.spinBox_nbre_pass,
                                                                   'lst_gabarit': self.userwdgfield.spinBox_id_lst_gabarit,
                                                                   'gabarit_passe': self.userwdgfield.spinBox_gabarit_passe,
                                                                   'mode_expl_manuel_barrage': self.userwdgfield.textBrowser_mode_expl_manuel_barrage,
                                                                   'nb_vannes': self.userwdgfield.spinBox_nb_vannes}},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {}},
                                     'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                           'widgets': {}}}

            self.dbasechildwdgfield = []

            self.propertieswdgEquipement = EquipementTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgEquipement)

            self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.userwdgfield.toolButton_numouvrage.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_num_ouvrage))
            self.userwdgfield.toolButton_pkdebut.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_pkdebut))
            self.userwdgfield.toolButton_pkfin.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_pkfin))


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def postSaveFeature(self,newfeature):
        # print('postsaveinf')

        itemintree =  self.linkedtreewidget.findItems(self.dbasetablename, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 0)[0]
        itemtochange = None
        for childitemindex in range(itemintree.childCount()):
            if itemintree.child(childitemindex).text(0) == str(self.currentFeature['id_infralineaire']):
                itemtochange = itemintree.child(childitemindex)

        for i, elem in enumerate(self.qtreewidgetfields):
            if itemtochange is not None:
                txttemp = self.dbase.getConstraintTextFromRawValue('Infralineaire', elem, self.currentFeature[elem])
                itemtochange.setText(i+1, str(txttemp))






    def postInitFeatureProperties(self, feat):
        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')


        if False:
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

        sql = "UPDATE Infralineaire SET id_objet = " + str(idobjet) + ",id_descriptionsystem = " + str(idsys) + ", modified=1, nature=60 WHERE id_infralineaire = " + str(idtroncon) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()

        if False:
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



class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiavnf_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)
