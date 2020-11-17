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


from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget

# # from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
# from ..base2.lamiabase_observation_tool import BaseObservationTool

# # from ..base.lamiabase_photo_tool import BasePhotoTool
# # from ..base.lamiabase_croquis_tool import BaseCroquisTool
# # from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
# # from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
# # from .lamiabaseassainissement_croquis_tool import BaseAssainissementCroquisTool as BaseCroquisTool

# from .lamiabaseparking_photo_tool import BaseParkingPhotoTool as BasePhotoTool
# from .lamiabaseparking_sketch_tool import BaseParkingCroquisTool as BaseCroquisTool

import os
import datetime

# *
from ...base3.qgswidgets.lamia_form_observation import BaseObservationTool
from .lamia_form_sketch import BaseCarparkSketchTool
from .lamia_form_camera import BaseCarparkCameraTool


class BaseCarparkObservationTool(BaseObservationTool):

    # dbasetablename = "Observation"

    # def __init__(
    #     self,
    #     dbase,
    #     dialog=None,
    #     linkedtreewidget=None,
    #     gpsutil=None,
    #     parentwidget=None,
    #     parent=None,
    # ):
    #     super(BaseParkingObservationTool, self).__init__(
    #         dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent
    #     )

    def __init__(self, **kwargs):
        super(BaseCarparkObservationTool, self).__init__(**kwargs)

    # def initTool(self):
    #     super(BaseParkingObservationTool, self).initTool()
    #     # self.NAME = 'Campagne de reconnaissance'
    #     # self.qtreewidgetfields = ['libelle']
    #     # self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
    #     self.NAME = "Observation immat"
    #     self.visualmode = [0, 1]

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Observation'
        self.dbasetablename = 'Observation'
        #self.visualmode = [1, 2]
        self.visualmode = []
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Desordre' : {'tabletc' : None,
                                           'idsource' : 'lk_desordre',
                                       'idtcsource' : None,
                                           'iddest' : 'id_desordre',
                                       'idtcdest' : None,
                                           'desttable' : ['Desordre']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lk_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_observation_tool_icon.png')

        # ****************************************************************************************
        #properties ui
        pass
    
    """

    # def initFieldUI(self):
    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "observation": {
                "linkfield": "id_observation",
                "widgets": {
                    "registrationnumber": self.toolwidgetmain.registrationnumber,
                    "illicit": self.toolwidgetmain.illicit,
                    "datetimeobservation": self.toolwidgetmain.datetimeobservation,
                },
            },
            "object": {"linkfield": "id_object", "widgets": {}},
        }

        self.toolwidgetmain.toolButton_immat.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.registrationnumber)
        )

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        self.propertieswdgPHOTOGRAPHIE = BaseCarparkCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
        self.propertieswdgCROQUIS = BaseCarparkSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
        # if self.parentWidget is not None:
        # self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(
        #     dbase=self.dbase, parentwidget=self
        # )
        # self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
        # self.propertieswdgCROQUIS = BaseCroquisTool(
        #     dbase=self.dbase, parentwidget=self
        # )
        # self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):

        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict(
                {"datetimeobservation": datecreation}, checkifinforgottenfield=False
            )

        # if self.currentFeature is None:
        #     datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #     # datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        #     self.initFeatureProperties(
        #         feat, self.dbasetablename, "datetimeobservation", datecreation
        #     )

    # def postSaveFeature(self, boolnewfeature):
    def postSaveFeature(self, featurepk=None):
        if (
            self.parentWidget is not None
            and self.parentWidget.currentFeaturePK is not None
        ):
            if self.parentWidget.DBASETABLENAME == "deficiency":
                self.parentWidget.updateDateCampagne()

    def showNumPad(self, finalwdg):
        # print('ok', finalwdg)

        # self.mainifacewidget.numpaddialog.exec_()
        # number = self.mainifacewidget.numpaddialog.dialogIsFinished()
        # # print(number)
        # if number:
        #     finalwdg.setValue(number)
        #     self.saveFeature()
        self.numpaddialog.exec_()
        number = self.numpaddialog.dialogIsFinished()
        if number:
            finalwdg.setValue(number)
            self.toolbarSave()


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_observation_ui.ui")
        uic.loadUi(uipath, self)
