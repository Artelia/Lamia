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
from .lamiabase_topographiedata_tool import BaseTopographiedataTool

"""
ne permettre de la renseigner qu en etant une classe fille de leve topo - sinon pas de datecreation
ca fout la merde....

"""


class BaseTopographieTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = 'Topographie'
    DBASETABLENAME = 'Topographie'
    LOADFIRST = True

    tooltreewidgetCAT = 'Ressources'
    tooltreewidgetSUBCAT = 'Topographie'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_topographie_tool_icon.png')

    PARENTJOIN = {'Marche' : {'colparent': 'id_marche',
                                'colthistable': 'lid_marche',
                                 'tctable': None,
                                 'tctablecolparent':None,
                                 'tctablecolthistable':None}
                 }

    def __init__(self, **kwargs):
        super(BaseTopographieTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Leves topographiques'
        self.dbasetablename = 'Topographie'
        # self.visualmode = [0, 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                           'idsource' : 'id_ressource',
                                       'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                       'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lk_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']}}
        # self.pickTable = None
        self.qtreewidgetfields = ['lpk_revision_begin']
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_topographie_tool_icon.png')

        # ****************************************************************************************
        #properties ui
    """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Topographie' : {'linkfield' : 'id_topographie',
                                                            'widgets' : {}},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {}},
                                            'Ressource' : {'linkfield' : 'id_ressource',
                                                        'widgets' : {'file': self.toolwidgetmain.lineEdit_file,
                                                                    'description': self.toolwidgetmain.lineEdit_nom,
                                                                    'datetimeressource': self.toolwidgetmain.dateTimeEdit_date}}}
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.choosePhoto)
        self.toolwidgetmain.pushButton_open.clicked.connect(self.openFile)
        self.toolwidgetmain.pushButton_ajoutpointGPS.clicked.connect(self.ajoutPointGPS)
        self.toolwidgetmain.pushButton_importer.clicked.connect(self.importer)

        typpointlist = [elem[0] for elem in self.dbase.dbasetables['Topographiedata']['fields']['typepointtopo']['Cst']]
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
        self.propertieswdgPOINTTOPO= BaseTopographiedataTool(**self.instancekwargs)
        self.propertieswdgPOINTTOPO.tooltreewidgetSUBCAT = 'Points topo'
        self.dbasechildwdgfield.append(self.propertieswdgPOINTTOPO)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postSaveFeature(self, savedfeaturepk=None):

        if self.currentFeaturePK is not None and self.currentFeaturePK != savedfeaturepk:   # new version of feature
            #fieldstoappend
            pointtopofields = list(self.dbase.dbasetables['Topographiedata']['fields'].keys())
            pointtopofields.remove('pk_topographiedata')
            indexpktopo = pointtopofields.index('lpk_topographie')
            pointtopofields.insert(-1, 'ST_AsText(geom)')

            sql = "SELECT " + ','.join(pointtopofields) + " FROM Topographiedata WHERE lpk_topographie = " + str(self.currentFeaturePK )
            results = self.dbase.query(sql)
            results = [list(res) for res in results]

            print(results)

            for i, res in enumerate(results):
                results[i][indexpktopo] = self.currentFeaturePK

            print(results)

            pointtopofields[pointtopofields.index('ST_AsText(geom)')] = 'geom'

            for res in results:

                sql = self.dbase.createSetValueSentence(type='INSERT',
                                                  tablename='Topographiedata',
                                                  listoffields=pointtopofields,
                                                  listofrawvalues=res)

                self.dbase.query(sql, docommit=False)

            self.dbase.commit()



    def openFile(self):
        filepath = self.completePathOfFile(self.userwdg.lineEdit_file.text())
        if filepath != '':
            os.startfile(filepath)

    def ajoutPointGPS(self):
        #self.propertieswdgPOINTTOPO.magicFunction()
        self.propertieswdgPOINTTOPO.featureSelected()
        #self.propertieswdgPOINTTOPO.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_position.findText('Crete'))
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
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)
            self.formutils.applyResultDict({'datetimeressource' : datecreation},checkifinforgottenfield=False)
        """
        if self.currentFeaturePK is None:
            # datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #self.initFeatureProperties(feat, 'Ressource', 'dateressource', datecreation)
            self.initFeatureProperties(feat, None, 'datetimeressource', datecreation)
        """

    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:


            # lastrevision = self.dbase.maxrevision
            datecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')

        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sql = "INSERT INTO Ressource (id_ressource, lpk_objet) "
        sql += "VALUES(" + str(lastressourceid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pkres = self.dbase.getLastRowId('Ressource')

        pktopo = self.currentFeaturePK
        lastidtopo = self.dbase.getLastId('Topographie') + 1
        sql = "UPDATE Topographie SET id_topographie = " + str(lastidtopo)  + ","
        sql += "lpk_ressource = " + str(pkres)
        sql += " WHERE pk_topographie = " + str(pktopo) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Marche':
                # print(self.parentWidget.currentFeature.attributes())
                currentparentlinkfield = self.parentWidget.currentFeature['id_marche']
                sql = "UPDATE Ressource SET lk_marche = " + str(currentparentlinkfield) + " WHERE id_ressource = " + str(pkres) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()
    """







class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_topographie_tool_ui.ui')
        uic.loadUi(uipath, self)

