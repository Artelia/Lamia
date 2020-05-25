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

import qgis
from qgis.PyQt import QtCore
from qgis.PyQt.QtWidgets import (QWidget)

class CreateSubFeatureWidget(QtCore.QObject):

    def __init__(self, parentwdg,subwidget):
        super(CreateSubFeatureWidget, self).__init__()
        self.parentwdg = parentwdg
        self.subwidget = subwidget

        # self.dbase = parentwdg.dbase
        # self.formutils = parentwdg.formutils
        # self.mainifacewidget = parentwdg.mainifacewidget

    def postSelectFeature(self):
        pass

    def postSaveFeature(self, parentfeaturepk=None):
        self._createNewSubFeature(parentfeaturepk)
   
    def _createNewSubFeature(self, savedfeaturepk):

        if self.parentwdg.currentFeaturePK is None :  #very new equip, not newversion
            dbase = self.parentwdg.dbase
            self.subwidget.toolbarNew()

            if 'geom' in dbase.dbasetables[self.subwidget.DBASETABLENAME].keys():
                geomtext = dbase.getValuesFromPk(self.parentwdg.DBASETABLENAME + '_qgis',
                                                'ST_AsText(geom)',
                                                savedfeaturepk)
                qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext)

                if (dbase.dbasetables[self.parentwdg.DBASETABLENAME]['geom'] !=  
                         dbase.dbasetables[self.subwidget.DBASETABLENAME]['geom']):
                    selfgeomtype = dbase.dbasetables[self.parentwdg.DBASETABLENAME]['geom'].lower()
                    subwdggeomtype = dbase.dbasetables[self.subwidget.DBASETABLENAME]['geom'].lower()

                    if selfgeomtype == 'point' and subwdggeomtype == 'linestring':
                        qgsgeompoint = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
                        qgsgeomforsubwdg = [qgsgeompoint,qgsgeompoint]
                        self.subwidget.setTempGeometry(qgsgeomforsubwdg)
                else:
                    self.subwidget.tempgeometry = qgsgeom

            self.subwidget.parentWidget.currentFeaturePK = savedfeaturepk
            self.subwidget.toolbarSave()
            self.subwidget.parentWidget.currentFeaturePK = None

