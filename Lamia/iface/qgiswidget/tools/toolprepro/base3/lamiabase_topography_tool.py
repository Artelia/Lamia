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
import datetime

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget)

from ...lamia_abstractformtool import AbstractLamiaFormTool
from .lamiabase_topographydata_tool import BaseTopographydataTool

base3 = QtCore.QObject()



class BaseTopographyTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = 'topography'
    DBASETABLENAME = 'topography'
    LOADFIRST = True

    tooltreewidgetCAT =QtCore.QCoreApplication.translate('base3','Resources')
    tooltreewidgetSUBCAT =QtCore.QCoreApplication.translate('base3','Topography')
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_topography_tool_icon.png')

    PARENTJOIN = {'delivery' : {'colparent': 'id_delivery',
                                'colthistable': 'lid_delivery',
                                 'tctable': None,
                                 'tctablecolparent':None,
                                 'tctablecolthistable':None}
                 }

    def __init__(self, **kwargs):
        super(BaseTopographyTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'topography' : {'linkfield' : 'id_topography',
                                                            'widgets' : {}},
                                            'object' : {'linkfield' : 'id_object',
                                                        'widgets' : {}},
                                            'resource' : {'linkfield' : 'id_resource',
                                                        'widgets' : {'file': self.toolwidgetmain.lineEdit_file,
                                                                    'description': self.toolwidgetmain.lineEdit_nom,
                                                                    'datetimeresource': self.toolwidgetmain.dateTimeEdit_date}}}
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.choosePhoto)
        self.toolwidgetmain.pushButton_open.clicked.connect(self.openFile)
        self.toolwidgetmain.pushButton_ajoutpointGPS.clicked.connect(self.ajoutPointGPS)
        self.toolwidgetmain.pushButton_importer.clicked.connect(self.importer)

        typpointlist = [elem[0] for elem in self.dbase.dbasetables['topographydata']['fields']['topographydatatype']['Cst']]
        self.toolwidgetmain.comboBox_typepoints.addItems(typpointlist)


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


        # ****************************************************************************************
        # child widgets
        self.instancekwargs['parentwidget'] = self

        self.dbasechildwdgfield = []
        self.propertieswdgPOINTTOPO= BaseTopographydataTool(**self.instancekwargs)
        self.propertieswdgPOINTTOPO.tooltreewidgetSUBCAT =QtCore.QCoreApplication.translate('base3','Topographic point')
        self.dbasechildwdgfield.append(self.propertieswdgPOINTTOPO)



    def postSaveFeature(self, savedfeaturepk=None):

        if self.currentFeaturePK is not None and self.currentFeaturePK != savedfeaturepk:   # new version of feature
            #fieldstoappend
            pointtopofields = list(self.dbase.dbasetables['topographiedata']['fields'].keys())
            pointtopofields.remove('pk_topographydata')
            indexpktopo = pointtopofields.index('lpk_topography')
            pointtopofields.insert(-1, 'ST_AsText(geom)')

            sql = "SELECT " + ','.join(pointtopofields) + " FROM topographydata WHERE lpk_topography = " + str(self.currentFeaturePK )
            results = self.dbase.query(sql)
            results = [list(res) for res in results]

            for i, res in enumerate(results):
                results[i][indexpktopo] = self.currentFeaturePK

            pointtopofields[pointtopofields.index('ST_AsText(geom)')] = 'geom'

            for res in results:
                sql = self.dbase.createSetValueSentence(type='INSERT',
                                                  tablename='topographydata',
                                                  listoffields=pointtopofields,
                                                  listofrawvalues=res)

                self.dbase.query(sql, docommit=False)

            self.dbase.commit()



    def openFile(self):
        filepath = self.completePathOfFile(self.userwdg.lineEdit_file.text())
        if filepath != '':
            os.startfile(filepath)

    def ajoutPointGPS(self):
        self.propertieswdgPOINTTOPO.featureSelected()
        self.propertieswdgPOINTTOPO.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_typepoints.currentIndex())
        success = self.propertieswdgPOINTTOPO.getGPSValues()
        if success:
            self.propertieswdgPOINTTOPO.saveFeature()

    def importer(self):
        pass

    def choosePhoto(self):
        file, extension = self.mainifacewidget.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'All (*.*)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))


    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        if self.currentFeaturePK is None:   #first creation
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict({'datetimeresource' : datecreation},checkifinforgottenfield=False)



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_topography_tool_ui.ui')
        uic.loadUi(uipath, self)

