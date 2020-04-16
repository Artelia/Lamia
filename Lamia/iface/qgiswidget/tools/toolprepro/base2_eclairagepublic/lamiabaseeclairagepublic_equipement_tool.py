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
from collections import OrderedDict

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget)

from ..base2.lamiabase_equipement_tool import BaseEquipementTool
from .lamiabaseeclairagepublic_photo_tool import BaseEclairagePublicPhotoTool as BasePhotoTool
from .lamiabaseeclairagepublic_croquis_tool import BaseEclairagePublicCroquisTool as BaseCroquisTool
from .lamiabaseeclairagepublic_desordre_tool import BaseEclairagePublicDesordreTool





class BaseEclairagePublicEquipementTool(BaseEquipementTool):


    def __init__(self, **kwargs):
        super(BaseEclairagePublicEquipementTool, self).__init__(**kwargs)

    """
    def initTool(self):
        super(BaseEclairagePublicEquipementTool, self).initTool()
        self.visualmode = [1, 2]
    """

    def initMainToolWidget(self):
        # ****************************************************************************************
        #   userui Field
        if self.toolwidgetmain is None:
            # ****************************************************************************************
            # userui
            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {'Equipement' : {'linkfield' : 'id_equipement',
                                                            'widgets' : {
                                                                            'categorie': self.toolwidgetmain.comboBox_cat,

                                                                                # depart
                                                                            'dep_nom': self.toolwidgetmain.comboBox_dep_nom,
                                                                            'dep_foncall': self.toolwidgetmain.comboBox_dep_foncall,
                                                                            'dep_typprot': self.toolwidgetmain.comboBox_dep_typprot,
                                                                            'dep_calprot': self.toolwidgetmain.lineEdit_dep_calprot,
                                                                            'dep_diffdj': self.toolwidgetmain.lineEdit_dep_diffdj,
                                                                            'dep_neutsec': self.toolwidgetmain.comboBox_dep_neutsec,

                                                                            # foyer
                                                                            'fo_codlant': self.toolwidgetmain.lineEdit_fo_codlant,
                                                                            'fo_typelum': self.toolwidgetmain.comboBox_fo_typelum,
                                                                            'fo_marque': self.toolwidgetmain.lineEdit_fo_marque,
                                                                            'fo_ref': self.toolwidgetmain.lineEdit_fo_ref,
                                                                            'fo_classe': self.toolwidgetmain.comboBox_fo_classe,
                                                                            'fo_couleur': self.toolwidgetmain.lineEdit_fo_couleur,
                                                                            'fo_hautfeu': self.toolwidgetmain.doubleSpinBox_fo_hautfeu,
                                                                            'fo_typevas': self.toolwidgetmain.comboBox_fo_typevas,
                                                                            'fo_typapp': self.toolwidgetmain.comboBox_fo_typapp,
                                                                            'fo_famlamp': self.toolwidgetmain.comboBox_fo_famlamp,
                                                                            'fo_puilamp': self.toolwidgetmain.doubleSpinBox_fo_puilamp,


                                                                        }},
                                                'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {'commentaire': self.toolwidgetmain.textBrowser_comm}},
                                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                                    'widgets' : {  }}}


            self.toolwidgetmain.toolButton_fo_hautfeu.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_fo_hautfeu))
            self.toolwidgetmain.toolButton_fo_puilamp.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_fo_puilamp))



            self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)

            #self.toolwidgetmain.pushButton_getGPS.clicked.connect(self.getGPSValue)

            #self.allaccessfields = OrderedDict(self.dbasetable['fields']['acces'])


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self


            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)


            self.propertieswdgDesordre = BaseEclairagePublicDesordreTool(**self.instancekwargs)
            #self.propertieswdgDesordre.NAME = None
            #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            #self.propertieswdgDesordre.groupBox_elements.setParent(None)
            #self.propertieswdgDesordre.userwdgfield.stackedWidget.setParent(None)
            #self.propertieswdgDesordre.frame_editing.setParent(None)
            #self.toolwidgetmain.frame_desordre.layout().addWidget(self.propertieswdgDesordre)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)


    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):

        if (self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None
                and self.parentWidget.DBASETABLENAME == 'Noeud'):
            self.toolwidgetmain.comboBox_cat.setEnabled(False)

            typeparent = self.parentWidget.toolwidgetmain.comboBox_typenoeud.currentText()
            if typeparent == 'Armoire':
                self.toolwidgetmain.comboBox_cat.setCurrentIndex(2)
                # get geom
                #noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeaturePK)
                #neudfetgeom = noeudfet.geometry().asPoint()
                #self.createorresetRubberband(1)
                #self.setTempGeometry([neudfetgeom,neudfetgeom], False, False)

            elif typeparent == 'Support':
                self.toolwidgetmain.comboBox_cat.setCurrentIndex(1)
                # get geom
                #noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeaturePK)
                #neudfetgeom = noeudfet.geometry().asPoint()
                #self.createorresetRubberband(1)
                #self.setTempGeometry([neudfetgeom,neudfetgeom], False, False)
            geomtext = self.dbase.getValuesFromPk('Noeud',
                                            'ST_AsText(geom)',
                                            self.parentWidget.currentFeaturePK)
            fetgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
            self.mainifacewidget.qgiscanvas.createorresetRubberband(1)
            self.setTempGeometry([fetgeom,fetgeom], False, False)

        else:
            self.toolwidgetmain.comboBox_cat.setEnabled(True)




    def postSaveFeature(self, savedfeaturepk=None):
        # save a disorder on first creation
        #if self.savingnewfeature and not self.savingnewfeatureVersion:
        if self.currentFeaturePK is None:
            self.propertieswdgDesordre.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('Equipement_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)

            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
            qgsgeomfordesordre = qgsgeom
            self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)

            self.currentFeaturePK = savedfeaturepk
            self.propertieswdgDesordre.toolbarSave()
            pkdesordre = self.propertieswdgDesordre.currentFeaturePK
            sql = "UPDATE Desordre SET groupedesordre = 'EQP' WHERE pk_desordre = {}".format(pkdesordre)
            self.dbase.query(sql)
            
            """
            pkobjet = self.dbase.createNewObjet()
            lastiddesordre = self.dbase.getLastId('Desordre') + 1
            geomtext, iddessys = self.dbase.getValuesFromPk('Equipement_qgis',
                                                            ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                            self.currentFeaturePK)
            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                newgeom = qgis.core.QgsGeometry.fromPolyline([qgsgeom.asPoint(), qgsgeom.asPoint()])
                newgeomwkt = newgeom.exportToWkt()
            else:
                #newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPointXY(), qgsgeom.asPointXY()])
                #newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
                # print('geom',qgsgeom.asWkt() )
                if qgsgeom.type() == 0: #point
                    newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
                elif qgsgeom.type() == 1: #line
                    aspoint = qgsgeom.asPolyline()[0]
                    newgeom = qgis.core.QgsGeometry.fromPolylineXY([aspoint, aspoint])
                newgeomwkt = newgeom.asWkt()

            sql = self.dbase.createSetValueSentence(type='INSERT',
                                                    tablename='Desordre',
                                                    listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                    'lid_descriptionsystem', 'geom'],
                                                    listofrawvalues=[lastiddesordre, pkobjet, 'EQP',
                                                                        iddessys, newgeomwkt])
            self.dbase.query(sql)
            """




    def changeCategorie(self, intcat):
        if self.dbase.variante in [None, 'Lamia']:
            pagecount = self.toolwidget.stackedWidget.count()
            if intcat >= pagecount -1 :
                self.toolwidget.stackedWidget.setCurrentIndex(pagecount -1)
            else:
                self.toolwidget.stackedWidget.setCurrentIndex(intcat)






class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeclairagepublic_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)