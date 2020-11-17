# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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


from collections import OrderedDict
import os
import logging

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)


from ..base2.lamiabase_infralineaire_tool import BaseInfraLineaireTool
from .lamiabasedigue_photo_tool import BaseDiguePhotoTool as BasePhotoTool
from .lamiabasedigue_croquis_tool import BaseDigueCroquisTool as BaseCroquisTool
from ..base2.lamiabase_photoviewer import PhotoViewer
from .lamiabasedigue_graphique_tool import BaseGraphiqueTool as GraphiqueTool
from .lamiabasedigue_profil_tool import BaseDigueProfilTool as ProfilTool




class BaseDigueInfraLineaireTool(BaseInfraLineaireTool):


    def __init__(self, **kwargs):
        super(BaseDigueInfraLineaireTool, self).__init__(**kwargs)

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






    def initMainToolWidget(self):

        self.toolwidgetmain  = UserUIField()

        self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                    'widgets': OrderedDict([('description1', self.toolwidgetmain .comboBox_type),
                                                                            ('description2', self.toolwidgetmain .comboBox_contitution),
                                                                            ('aubaredelargeur', self.toolwidgetmain .comboBox_aubaredelargeur),
                                                                            ('aubaredevegherbacee', self.toolwidgetmain .comboBox_aubaredevegherbacee),
                                                                            ('aubaredevegarbustive', self.toolwidgetmain .comboBox_aubaredevegarbustive),
                                                                            ('aubaredevegarboree', self.toolwidgetmain .comboBox_aubaredevegarboree),
                                                                            ('aubaredecommentaire', self.toolwidgetmain .textBrowser_aubaredecommentaire)])},
                                            'Objet': {'linkfield': 'id_objet',
                                                    'widgets': {'libelle': self.toolwidgetmain .lineEdit_nom,
                                                                'commentaire':self.toolwidgetmain .textBrowser_commentaire}},
                                            'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                                'widgets': {'annee_fin_pose' : self.toolwidgetmain .dateEdit_datecontruct,
                                                                            'etatfonct': self.toolwidgetmain .comboBox_etat_fonc}}}

        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        #if self.parentWidget is None:
        self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


        self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)







    def initAdvancedToolWidget(self):

        self.toolwidgetadvanced = UserUIDesktop()

        self.formtoolwidgetconfdictadvanced = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                        'widgets': OrderedDict([('description1', self.toolwidgetadvanced.comboBox_type),
                                                                            ('description2', self.toolwidgetadvanced.comboBox_contitution),
                                                                            ('classement', self.toolwidgetadvanced.comboBox_classement),
                                                                            ('aubaredelargeur', self.toolwidgetadvanced.comboBox_aubaredelargeur),
                                                                            ('aubaredevegherbacee', self.toolwidgetadvanced.comboBox_aubaredevegherbacee),
                                                                            ('aubaredevegarbustive', self.toolwidgetadvanced.comboBox_aubaredevegarbustive),
                                                                            ('aubaredevegarboree', self.toolwidgetadvanced.comboBox_aubaredevegarboree),
                                                                            ('aubaredecommentaire', self.toolwidgetadvanced.textBrowser_aubaredecommentaire)])},
                                                'Objet': {'linkfield': 'id_objet',
                                                            'widgets': {'libelle': self.toolwidgetadvanced.lineEdit_nom,
                                                                        'commentaire': self.toolwidgetadvanced.textBrowser_comm}},
                                                'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                                        'widgets': {'annee_fin_pose' : self.toolwidgetmain .dateEdit_datecontruct,
                                                                                    'etatfonct': self.toolwidgetadvanced.comboBox_etat_fonc}}}
        # TODO
        #self.toolwidgetadvanced.pushButton_defineinter.clicked.connect(self.manageLinkage)
        self.dbasechildwdgdesktop = []
        self.instancekwargs['parentwidget'] = self

        if True:
            self.photowdg = PhotoViewer()
            self.toolwidgetadvanced.tabWidget.widget(0).layout().addWidget(self.photowdg)
        if True:
            self.croquisprofilwdg = PhotoViewer()
            self.toolwidgetadvanced.stackedWidget_profiltravers.widget(0).layout().addWidget(self.croquisprofilwdg)
        if True:
            self.graphprofil = GraphiqueTool(**self.instancekwargs)
            self.graphprofil.initMainToolWidget()
            #self.graphprofil.formtoolwidgetconfdict = self.graphprofil.formtoolwidgetconfdictmain
            #self.graphprofil.dbasechildwdg = self.graphprofil.dbasechildwdgfield
            #self.graphprofil.toolwidget = self.graphprofil.toolwidgetmain
            self.toolwidgetadvanced.stackedWidget_profiltravers.widget(1).layout().addWidget(self.graphprofil.mplfigure)
            # self.userwdg.frame_graph.layout().addWidget(self.pyqtgraphwdg)
            #self.dbasechildwdgdesktop.append(self.graphprofil)

        if False:
            pathtool = None
            for i, tool in enumerate(self.windowdialog.tools):
                if 'PathTool' in tool.__class__.__name__:
                    pathtool = self.windowdialog.tools[i]

            self.propertieswdgPROFILLONG = pathtool.__class__(dbase=self.dbase, parentwidget=self)
            # self.toolwidgetadvanced.tabWidget.widget(2).layout().addWidget(self.propertieswdgPROFILLONG.plotWdg)
            self.toolwidgetadvanced.tabWidget.widget(2).layout().addWidget(self.propertieswdgPROFILLONG.mplfigure)
        else:
            self.propertieswdgPROFILLONG = None

        
        
        if False:
            self.propertieswdgPROFIL = ProfilTool(**self.instancekwargs)
            self.dbasechildwdgdesktop.append(self.propertieswdgPROFIL)

        #self.initWidgets()



    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')

        if self.currentFeaturePK is None:
            pass
        else:
            if self.toolwidget == self.toolwidgetadvanced:
                #* intervenants
                #pkobjet
                sql = "SELECT id_objet FROM Infralineaire_qgis WHERE pk_infralineaire = " + str(self.currentFeaturePK)
                idobjet = self.dbase.query(sql)[0][0]

                sql = "SELECT Tcobjetintervenant.fonction, Intervenant.nom,Intervenant.societe  FROM Tcobjetintervenant "
                sql += " INNER JOIN Intervenant ON Tcobjetintervenant.lid_intervenant = Intervenant.id_intervenant "
                #sql += "WHERE id_tcobjet = " + str(self.currentFeature['id_objet'])
                sql += "WHERE lid_objet = " + str(idobjet)
                query = self.dbase.query(sql)
                result = "\n".join([str(row) for row in query])
                self.toolwidgetadvanced.textBrowser_intervenants.clear()
                self.toolwidgetadvanced.textBrowser_intervenants.append(result)

                #* photo
                #lkressource = self.currentFeature['lk_ressource2']
                #lkressource
                sql = "SELECT lid_ressource_2 FROM Infralineaire_qgis WHERE pk_infralineaire = " + str(self.currentFeaturePK)
                lkressource = self.dbase.query(sql)[0][0]


                if not self.dbase.utils.isAttributeNull(lkressource):
                    #sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_objet = "
                    # sql += str(self.currentFeature['lk_photo'])
                    sql = "SELECT file FROM Ressource  WHERE id_ressource = " + str(lkressource)
                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    filephoto = result[0][0]
                    completefilephoto = self.dbase.completePathOfFile(filephoto)
                    self.showImageinLabelWidget(self.photowdg, completefilephoto)
                else:
                    self.photowdg.clear()

                #* profil travers
                # lkressourceprofile = self.currentFeature['lk_ressource4']
                #lkressourceprofile
                sql = "SELECT lid_ressource_4 FROM Infralineaire_qgis WHERE pk_infralineaire = " + str(self.currentFeaturePK)
                lkressourceprofile = self.dbase.query(sql)[0][0]

                if not self.dbase.utils.isAttributeNull(lkressourceprofile):
                    #sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_ressource = "
                    #sql += str(lkressourceprofile)
                    sql = "SELECT file FROM Ressource  WHERE id_ressource = " + str(lkressourceprofile)
                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    if len(result)>0:
                        self.toolwidgetadvanced.stackedWidget_profiltravers.setCurrentIndex(0)
                        filephoto = result[0][0]
                        completefilephoto = self.dbase.completePathOfFile(filephoto)
                        self.showImageinLabelWidget(self.croquisprofilwdg, completefilephoto)
                    else:
                        self.croquisprofilwdg.clear()

                    sql = "SELECT pk_graphique FROM Graphique_qgis  WHERE id_ressource = " + str(lkressourceprofile)
                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    if len(result) > 0:
                        self.toolwidgetadvanced.stackedWidget_profiltravers.setCurrentIndex(1)
                        pkgraphique = result[0][0]
                        self.graphprofil.currentFeaturePK = pkgraphique
                        #self.graphprofil.selectFeature(pk=pkgraphique)
                        self.graphprofil.postSelectFeature()
                        #postSelectFeature
                else:
                    self.toolwidgetadvanced.stackedWidget_profiltravers.setCurrentIndex(0)
                    self.croquisprofilwdg.clear()

                #* profil long
                if self.propertieswdgPROFILLONG is not None:
                    #self.propertieswdgPROFILLONG.activateMouseTracking(0)
                    self.propertieswdgPROFILLONG.rubberbandtrack.hide()
                    self.propertieswdgPROFILLONG.rubberBand.reset(self.dbase.dbasetables['Infralineaire']['layer'].geometryType())
                    currentgeom = self.currentFeature.geometry().asPolyline()
                    self.propertieswdgPROFILLONG.computePath(list(currentgeom[0]), list(currentgeom[-1]))
                    #self.propertieswdgPROFILLONG.activateMouseTracking(2)
                    self.propertieswdgPROFILLONG.rubberbandtrack.hide()
                    self.propertieswdgPROFILLONG.rubberBand.reset(self.dbase.dbasetables['Infralineaire']['layer'].geometryType())






class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUIDesktop(QWidget):
    def __init__(self, parent=None):
        super(UserUIDesktop, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_infralineaire_tooldesktop_ui.ui')
        uic.loadUi(uipath, self)