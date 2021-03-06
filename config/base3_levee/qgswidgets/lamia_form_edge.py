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
from qgis.PyQt.QtWidgets import QWidget, QLabel, QFrame


from ...base3.qgswidgets.lamia_form_edge import BaseEdgeTool
from .lamia_form_camera import BaseLeveeCameraTool
from .lamia_form_sketch import BaseLeveeSketchTool
from ...base3.qgswidgets.lamia_form_pictureviewer import PictureViewer
from .lamia_form_graph import BaseLeveeGraphTool
from .lamia_form_profile import BaseLeveeProfileTool

from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_tcmanytomany import (
    TcmanytomanyChooserWidget,
)


class BaseLeveeEdgeTool(BaseEdgeTool):

    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Section")

    def __init__(self, **kwargs):
        super(BaseLeveeEdgeTool, self).__init__(**kwargs)

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

        self.toolwidgetmain = UserUIField()

        self.formtoolwidgetconfdictmain = {
            "edge": {
                "linkfield": "id_edge",
                "widgets": {
                    "edgetype": self.toolwidgetmain.comboBox_type,
                    "edgesubtype": self.toolwidgetmain.comboBox_contitution,
                    "setbackwidth": self.toolwidgetmain.comboBox_aubaredelargeur,
                    "setbackvegetationherbaceous": self.toolwidgetmain.comboBox_aubaredevegherbacee,
                    "setbackvegetationshrub": self.toolwidgetmain.comboBox_aubaredevegarbustive,
                    "setbackvegetationtree": self.toolwidgetmain.comboBox_aubaredevegarboree,
                    "setbackcomment": self.toolwidgetmain.textBrowser_aubaredecommentaire,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {
                    "name": self.toolwidgetmain.lineEdit_nom,
                    "comment": self.toolwidgetmain.textBrowser_commentaire,
                },
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "dateoperationalcreation": self.toolwidgetmain.dateEdit_datecontruct,
                    "fonctionnalcondition": self.toolwidgetmain.comboBox_etat_fonc,
                },
            },
        }

        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        # if self.parentWidget is None:
        self.propertieswdgPHOTOGRAPHIE = BaseLeveeCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

        self.propertieswdgCROQUIS = BaseLeveeSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        if self.dbase.variante in ["SIRS"]:
            self.toolwidgetmain.tabWidget.tabBar().setTabEnabled(1, False)
            self.toolwidgetmain.comboBox_contitution.setEnabled(False)
            self.toolwidgetmain.dateEdit_datecontruct.setEnabled(False)
            self.toolwidgetmain.comboBox_etat_fonc.setEnabled(False)
        elif self.dbase.variante in ["Lamia", None]:
            self.propertieswdgProfile = BaseLeveeProfileTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgProfile)

    def initAdvancedToolWidget(self):

        self.toolwidgetadvanced = UserUIDesktop()

        self.formtoolwidgetconfdictadvanced = {
            "edge": {
                "linkfield": "id_edge",
                "widgets": {
                    "edgetype": self.toolwidgetadvanced.comboBox_type,
                    "edgesubtype": self.toolwidgetadvanced.comboBox_contitution,
                    "regulatorycategory": self.toolwidgetadvanced.comboBox_classement,
                    "setbackwidth": self.toolwidgetadvanced.comboBox_aubaredelargeur,
                    "setbackvegetationherbaceous": self.toolwidgetadvanced.comboBox_aubaredevegherbacee,
                    "setbackvegetationshrub": self.toolwidgetadvanced.comboBox_aubaredevegarbustive,
                    "setbackvegetationtree": self.toolwidgetadvanced.comboBox_aubaredevegarboree,
                    "setbackcomment": self.toolwidgetadvanced.textBrowser_aubaredecommentaire,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {
                    "name": self.toolwidgetadvanced.lineEdit_nom,
                    "comment": self.toolwidgetadvanced.textBrowser_comm,
                },
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "dateoperationalcreation": self.toolwidgetmain.dateEdit_datecontruct,
                    "fonctionnalcondition": self.toolwidgetadvanced.comboBox_etat_fonc,
                },
            },
        }
        # TODO
        # self.toolwidgetadvanced.pushButton_defineinter.clicked.connect(self.manageLinkage)
        self.dbasechildwdgdesktop = []
        self.instancekwargs["parentwidget"] = self

        if True:
            self.photowdg = PictureViewer()
            self.toolwidgetadvanced.tabWidget.widget(0).layout().addWidget(
                self.photowdg
            )
        if True:
            self.croquisprofilwdg = PictureViewer()
            self.toolwidgetadvanced.stackedWidget_profiltravers.widget(
                0
            ).layout().addWidget(self.croquisprofilwdg)
        if True:
            self.graphprofil = BaseLeveeGraphTool(**self.instancekwargs)
            self.graphprofil.initMainToolWidget()
            # self.graphprofil.formtoolwidgetconfdict = self.graphprofil.formtoolwidgetconfdictmain
            # self.graphprofil.dbasechildwdg = self.graphprofil.dbasechildwdgfield
            # self.graphprofil.toolwidget = self.graphprofil.toolwidgetmain
            self.toolwidgetadvanced.stackedWidget_profiltravers.widget(
                1
            ).layout().addWidget(self.graphprofil.mplfigure)
            # self.userwdg.frame_graph.layout().addWidget(self.pyqtgraphwdg)
            # self.dbasechildwdgdesktop.append(self.graphprofil)

        if False:
            pathtool = None
            for i, tool in enumerate(self.windowdialog.tools):
                if "PathTool" in tool.__class__.__name__:
                    pathtool = self.windowdialog.tools[i]

            self.propertieswdgPROFILLONG = pathtool.__class__(
                dbase=self.dbase, parentwidget=self
            )
            # self.toolwidgetadvanced.tabWidget.widget(2).layout().addWidget(self.propertieswdgPROFILLONG.plotWdg)
            self.toolwidgetadvanced.tabWidget.widget(2).layout().addWidget(
                self.propertieswdgPROFILLONG.mplfigure
            )
        else:
            self.propertieswdgPROFILLONG = None

        if True:
            self.propertieswdgPROFIL = BaseLeveeProfileTool(**self.instancekwargs)
            self.dbasechildwdgdesktop.append(self.propertieswdgPROFIL)

        # actors
        if True:
            self.tcsubwidget = TcmanytomanyChooserWidget(
                parentwdg=self,
                tcmanytomanyname="tcobjectactor",
                childtablename="actor",
                parentmanytomanyfield="id_object",
                childmanytomanyfield="id_actor",
                childdisplayfields=["actorname", "society"],
                tcmanytomanydisplayfields=["role"],
                parentframe=self.toolwidgetadvanced.frame_actor,
            )
            self.lamiawidgets.append(self.tcsubwidget)

        # self.initWidgets()

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        debug = False
        if debug:
            logging.getLogger("Lamia").debug("Start ")

        if self.currentFeaturePK is None:
            pass
        else:
            if self.toolwidget == self.toolwidgetadvanced:
                self.postSelectFeatureAdvanced()

    def postSelectFeatureAdvanced(self):

        # * photo
        lkressource = self.dbase.getValuesFromPk(
            "edge_qgis", "lid_resource_2", self.currentFeaturePK
        )
        if not self.dbase.utils.isAttributeNull(lkressource):
            sql = f"SELECT file FROM resource  WHERE id_resource = {lkressource}"
            query = self.dbase.query(sql)
            result = [row for row in query]
            filephoto = result[0][0]
            completefilephoto = self.dbase.completePathOfFile(filephoto)
            self.showImageinLabelWidget(self.photowdg, completefilephoto)
        else:
            self.photowdg.clear()

        # * profil travers
        lkressourceprofile = self.dbase.getValuesFromPk(
            "edge_qgis", "lid_resource_4", self.currentFeaturePK
        )

        if not self.dbase.utils.isAttributeNull(lkressourceprofile):
            sql = f"SELECT file FROM resource  WHERE id_resource = {lkressourceprofile}"
            query = self.dbase.query(sql)
            result = [row for row in query]

            if len(result) > 0:
                self.toolwidgetadvanced.stackedWidget_profiltravers.setCurrentIndex(0)
                filephoto = result[0][0]
                completefilephoto = self.dbase.completePathOfFile(filephoto)
                self.showImageinLabelWidget(self.croquisprofilwdg, completefilephoto)
            else:
                self.croquisprofilwdg.clear()

            sql = f"SELECT pk_graph FROM graph_qgis  WHERE id_resource = {lkressourceprofile}"
            query = self.dbase.query(sql)
            result = [row for row in query]
            if len(result) > 0:
                self.toolwidgetadvanced.stackedWidget_profiltravers.setCurrentIndex(1)
                pkgraphique = result[0][0]
                self.graphprofil.currentFeaturePK = pkgraphique
                self.graphprofil.postSelectFeature()
        else:
            self.toolwidgetadvanced.stackedWidget_profiltravers.setCurrentIndex(0)
            self.croquisprofilwdg.clear()

        # * profil long
        if self.propertieswdgPROFILLONG is not None:
            # self.propertieswdgPROFILLONG.activateMouseTracking(0)
            self.propertieswdgPROFILLONG.rubberbandtrack.hide()
            self.propertieswdgPROFILLONG.rubberBand.reset(
                self.dbase.dbasetables["Infralineaire"]["layer"].geometryType()
            )
            currentgeom = self.currentFeature.geometry().asPolyline()
            self.propertieswdgPROFILLONG.computePath(
                list(currentgeom[0]), list(currentgeom[-1])
            )
            # self.propertieswdgPROFILLONG.activateMouseTracking(2)
            self.propertieswdgPROFILLONG.rubberbandtrack.hide()
            self.propertieswdgPROFILLONG.rubberBand.reset(
                self.dbase.dbasetables["Infralineaire"]["layer"].geometryType()
            )


class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_edge_ui.ui")
        uic.loadUi(uipath, self)


class UserUIDesktop(QWidget):
    def __init__(self, parent=None):
        super(UserUIDesktop, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_edge_desktop_ui.ui"
        )
        uic.loadUi(uipath, self)
