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


import datetime, os

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget)

from ...lamia_abstractformtool import AbstractLamiaFormTool
from .lamiabase_rapport_tool import BaseRapportTool
from .lamiabase_photo_tool import BasePhotoTool
from .lamiabase_topographie_tool import BaseTopographieTool



class BaseMarcheTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'Marche'
    LOADFIRST = False

    tooltreewidgetCAT = 'Gestion'
    tooltreewidgetSUBCAT = 'Marche'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_marche_tool_icon.png')
    
    """
    tempparentjoin = {}
    linkdict = {'colparent': 'id_objet',
                'colthistable': 'id_intervenant',
                    'tctable': 'Tcobjetintervenant',
                    'tctablecolparent':'lid_objet',
                    'tctablecolthistable':'lid_intervenant'}
    for tablename in ['Intervenant']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin
    """

    def __init__(self, **kwargs):
        super(BaseMarcheTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Gestion'
        self.NAME = 'Marche'
        self.dbasetablename = 'Marche'
        # self.visualmode = [0, 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_objet',
                                            'idtcsource' : 'id_tcobjet',
                                           'iddest' : 'id_intervenant',
                                           'idtcdest' : 'id_tcintervenant',
                                           'desttable' : ['Intervenant']}
                                            }
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_marche_tool_icon.png')

        # ****************************************************************************************
        #properties ui
        pass
    """


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Marche' : {'linkfield' : 'id_marche',
                                            'widgets' : {
                                                        'datemarche' : self.toolwidgetmain.dateEdit_date,
                                                        'numero_marche': self.toolwidgetmain.lineEdit_nummarche,
                                            }},
                            'Objet' : {'linkfield' : 'id_objet',
                                        'widgets' : {'libelle': self.toolwidgetmain.lineEdit_nom}}}
        self.toolwidgetmain.pushButton_currentPrestation.clicked.connect(self.defineCurrentPrestation)
        #self.toolwidgetmain.pushButton_defineinter.clicked.connect(self.manageLinkage)

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        self.propertieswdgRAPPORT = BaseRapportTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgRAPPORT)

        self.propertieswdgPHOTO = BasePhotoTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTO)

        self.propertieswdgTOPOGRAPHIE = BaseTopographieTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgTOPOGRAPHIE)



    def defineCurrentPrestation(self):
        self.windowdialog.currentprestationlabel.setText('Prestation : ' + str(self.currentFeature.id()) + " - " +str(self.currentFeature['nommarche'] ))
        self.dbase.currentprestationid = self.currentFeature.id()


    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass
    """

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        if self.currentFeaturePK is None:
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            #self.initFeatureProperties(feat, self.dbasetablename, 'datemarche', datecreation)
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict({'datemarche' : datecreation},checkifinforgottenfield=False)

        else:
            try:
                idobjet = self.dbase.getValuesFromPk(self.DBASETABLENAME + '_qgis', 
                                                    'id_objet',
                                                    self.currentFeaturePK)
                sql = "SELECT Tcobjetintervenant.fonction, Intervenant.nom,Intervenant.societe  FROM Tcobjetintervenant "
                sql += " INNER JOIN Intervenant ON Tcobjetintervenant.lid_intervenant = Intervenant.id_intervenant "
                #sql += "WHERE id_tcobjet = " + str(self.currentFeature['id_objet'])
                sql += "WHERE lid_objet = " + str(idobjet)
                query = self.dbase.query(sql)

                result = "\n".join([str(row) for row in query])
                self.toolwidgetmain.textBrowser_intervenants.clear()
                self.toolwidgetmain.textBrowser_intervenants.append(result)
            except KeyError as e:
                print('postInitFeatureProperties', e)

    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:


            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid) + "," + str(self.dbase.maxrevision) + ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')



        pkmarche= self.currentFeaturePK
        lastidmarche = self.dbase.getLastId('Marche') + 1


        sql = "UPDATE Marche SET id_marche = " + str(lastidmarche) + ","
        sql += "lpk_objet = " + str(pkobjet)
        sql += " WHERE pk_marche = " + str(pkmarche) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()
    """





    def postSaveFeature(self, boolnewfeature):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_marche_tool_ui.ui')
        uic.loadUi(uipath, self)