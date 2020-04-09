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


import os
import qgis
from qgis.PyQt import uic, QtGui
from qgis.PyQt.QtWidgets import (QWidget)

from ...lamia_abstractformtool import AbstractLamiaFormTool


class BasePointtopoTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'Pointtopo'
    LOADFIRST = False

    tooltreewidgetCAT = 'Ressources'
    tooltreewidgetSUBCAT = 'Points topo'
    tooltreewidgetICONPATH = None


    def __init__(self, **kwargs):
        super(BasePointtopoTool, self).__init__(**kwargs)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Points topo'
        self.dbasetablename = 'Pointtopo'
        self.visualmode = [1,2]        # important : must be child of topographie class, do not use elsewhere
        self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True

        self.linkagespec = {'Topographie' :{'tabletc' : None,
                                              'idsource' : 'lpk_topographie',
                                            'idtcsource' : None,
                                           'iddest' : 'pk_topographie',
                                           'idtcdest' : None,
                                           'desttable' : ['Topographie']} }

        self.magicfunctionENABLED = True

        # ****************************************************************************************
        #properties ui
        pass
    """

    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {'Pointtopo' : {'linkfield' : 'id_pointtopo',
                                                    'widgets' : {'typepointtopo': self.toolwidgetmain.comboBox_position,
                                                                'x': self.toolwidgetmain.doubleSpinBox_X,
                                                                'y': self.toolwidgetmain.doubleSpinBox_Y,
                                                                'zmngf': self.toolwidgetmain.doubleSpinBox_Zngf,
                                                                'dx': self.toolwidgetmain.doubleSpinBox_dX,
                                                                'dy': self.toolwidgetmain.doubleSpinBox_dY,
                                                                'dz': self.toolwidgetmain.doubleSpinBox_dZ,
                                                                'zwgs84': self.toolwidgetmain.doubleSpinBox_Zwgs84,
                                                                'zgps': self.toolwidgetmain.doubleSpinBox_Zgps,
                                                                'raf09': self.toolwidgetmain.doubleSpinBox_raf09,
                                                                'hauteurperche': self.toolwidgetmain.doubleSpinBox_hautperche}}
                                                                }
        # if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Topographie':
        #     self.pushButton_addFeature.setEnabled(True)
        # else:
        #     self.pushButton_addFeature.setEnabled(False)

        self.toolwidgetmain.pushButton_catchvalues.clicked.connect(self.getGPSValues)

        self.gpswidget = {'x' : {'widget' : self.toolwidgetmain.label_X,
                                    'gga' : 'Xcrs'},
                            'y': {'widget': self.toolwidgetmain.label_Y,
                                'gga': 'Ycrs'},
                            'zmngf': {'widget': self.toolwidgetmain.label_Z,
                                'gga': 'zmNGF'},
                            'dx': {'widget': self.toolwidgetmain.label_dX,
                                'gst': 'xprecision'},
                            'dy': {'widget': self.toolwidgetmain.label_dY,
                                'gst': 'yprecision'},
                            'dz': {'widget': self.toolwidgetmain.label_dZ,
                                'gst': 'zprecision'},
                            'zgps': {'widget': self.toolwidgetmain.label_zgps,
                                    'gga': 'elevation'},
                            'zwgs84': {'widget': self.toolwidgetmain.label_zwgs84,
                                    'gga': 'deltageoid'},
                            'raf09': {'widget': self.toolwidgetmain.label_raf09,
                                    'gga': 'RAF09'},
                            'hauteurperche': {'widget': self.toolwidgetmain.label_hautperche,
                                    'gga': 'hauteurperche'}
                            }

    """
    def postloadIds(self,sqlin):
        sqlin += " ORDER BY id_pointtopo "
        if False:
            # sqlin=''
            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                sqlin = "SELECT id_pointtopo FROM Pointtopo_qgis WHERE lpk_topographie = " + str(self.parentWidget.currentFeaturePK)
                sqlin += " ORDER BY id_pointtopo "
            else:
                sqlin += " ORDER BY id_pointtopo "


        return sqlin
    """

    """
    def getPkFromId(self, layername, inputid):
        return inputid





        if False:
            pk = None

            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                sql = "SELECT pk_pointtopo FROM Pointtopo_qgis "
                sql += "WHERE id_pointtopo = " + str(inputid)
                sql += " AND lpk_topographie = " + str(self.parentWidget.currentFeaturePK)
                #sql += self.dbase.dateVersionConstraintSQL()
                pk = self.dbase.query(sql)[0][0]

            return pk

    """

    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        pass

        if self.currentFeaturePK is None:
            #self.pushButton_savefeature.setEnabled(True)
            self.enablePropertiesButtons(True)
        else:
            # getlpkrevisionbeginfromparent
            sql = "SELECT lpk_revision_begin FROM Pointtopo_qgis WHERE pk_pointtopo = " + str(self.currentFeaturePK)
            result = self.dbase.query(sql)
            if len(result)>0:
                revbegin = result[0][0]
                if revbegin == self.dbase.maxrevision:
                    self.enablePropertiesButtons(True)
                else:
                    self.enablePropertiesButtons(False)
            else:
                self.enablePropertiesButtons(True)

    def enablePropertiesButtons(self, boolvalue):
        pass
        #self.pushButton_savefeature.setEnabled(boolvalue)
        #self.pushButton_addFeature.setEnabled(boolvalue)
        #self.pushButton_delFeature.setEnabled(boolvalue)
        #self.pushButton_savefeature.setEnabled(boolvalue)
        #self.groupBox_geom.setEnabled(boolvalue)


    def magicFunction(self):
        self.featureSelected()
        self.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_position.findText('Crete'))
        success = self.getGPSValues()
        if success:
            self.saveFeature()

    """
    def createParentFeature(self):

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Topographie':
                pktopo = self.parentWidget.currentFeaturePK
                pkpointtopo = self.currentFeaturePK

                sql = "UPDATE Pointtopo SET "
                sql += "lpk_topographie = " + str(pktopo)
                sql += ", id_pointtopo = " + str(pkpointtopo)
                sql += " WHERE pk_pointtopo = " + str(pkpointtopo) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()
    """


    def deleteParentFeature(self):
        return True


    def postSaveFeature(self, boolnewfeature):
        pass


    def getGPSValues(self):
        if self.gpsutil is not None:
            if self.gpsutil.currentpoint is None:
                self.mainifacewidget.errorMessage('GPS non connecte')
                return

            for i, fieldname in enumerate(self.gpswidget.keys()):
                try:
                    value = float(self.gpswidget[fieldname]['widget'].text())
                except ValueError:
                    value = None
                if value is not None:
                    self.formtoolwidgetconfdict[self.dbasetablename]['widgets'][fieldname].setValue(value)
                else:
                    self.formtoolwidgetconfdict[self.dbasetablename]['widgets'][fieldname].setValue(-1.0)

            self.mainifacewidget.qgiscanvas.createorresetRubberband(0)
            self.setTempGeometry([self.gpsutil.currentpoint],False)
            return True
        else:
            self.errorMessage('GPS non connecte')
            return False




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_pointtopo_tool_ui.ui')
        uic.loadUi(uipath, self)