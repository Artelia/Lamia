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


from ...base3.qgswidgets.lamia_form_actor import BaseActorTool
from qgis.PyQt import uic, QtCore, QtWidgets


class BaseFaunafloraActorTool(BaseActorTool):
    LOADFIRST = True

    def __init__(self, **kwargs):
        super(BaseFaunafloraActorTool, self).__init__(**kwargs)


    def initMainToolWidget(self):
        super().initMainToolWidget()

        # self.spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.mainifacewidget.statusBar().layout().addSpacerItem(self.spacer)
        self.actorlabel = QtWidgets.QLabel(self.tr("Pas d'inspecteur actif"))
        self.mainifacewidget.statusBar().addWidget(self.actorlabel,50)

        self.activeactorbutton = QtWidgets.QPushButton("Set as active")
        self.toolwidgetmain.frame_2.layout().addWidget(self.activeactorbutton)

        self.activeactorbutton.clicked.connect(self.setActor)
        self.mainifacewidget.closingProject.connect(self.removeActor)

    def setActor(self):
        print('ok',self.currentFeaturePK)
        actordata = self.dbase.lamiaorm['actor'].read(self.currentFeaturePK)
        print('ok',actordata)
        self.dbase.currentprestationid = actordata['id_actor']
        self.actorlabel.setText(str("Inspecteur : " + actordata['actorname']))
        self.actorlabel.setStyleSheet(
                "QLabel { background-color : rgb(85, 255, 0);  }"
            )  # vert

    def removeActor(self):
        self.mainifacewidget.statusBar().removeWidget(self.actorlabel)

