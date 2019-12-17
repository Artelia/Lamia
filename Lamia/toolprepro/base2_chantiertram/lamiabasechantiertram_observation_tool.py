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


# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QTabWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QTabWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_observation_tool import BaseObservationTool
#from ..base.lamiabase_photo_tool import BasePhotoTool
# from ..base.lamiabase_croquis_tool import BaseCroquisTool
# from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
#from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
#from .lamiabaseassainissement_croquis_tool import BaseAssainissementCroquisTool as BaseCroquisTool

from .lamiabasechantiertram_photo_tool import BaseChantierTramPhotoTool as BasePhotoTool
from .lamiabasechantiertram_croquis_tool import BaseChantierTramCroquisTool as BaseCroquisTool
from .lamiabasechantiertramintervenant_tool import BaseChantierTramIntervenantTool as BaseIntervenantTool
from .lamiabasechantiertram_rapport_tool import BaseChantierTramRapportTool as BaseRapportTool
from .lamiabasechantiertram_signature_tool import SignatureWidget
from .lamiabasechantiertram_lidchooser import LidChooserWidget

import os
import datetime


class BaseChantierTramObservationTool(BaseObservationTool):

    dbasetablename = 'Observation'
    OBSTYPE = None



    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseChantierTramObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        self.indexstackedpage = None






    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Observation' : {'linkfield' : 'id_observation',
                                             'widgets' : {'ncadescription': self.userwdgfield.textBrowser_ncadescription,

                                                            'ncathqualite':self.userwdgfield.checkBox_ncathqualite  ,
                                                            'ncathouvrage':self.userwdgfield.checkBox_ncathouvrage  ,
                                                            'ncathsecurite':self.userwdgfield.checkBox_ncathsecurite  ,
                                                            'ncathsystem':self.userwdgfield.checkBox_ncathsystem  ,
                                                            'ncathenvironnement':self.userwdgfield.checkBox_ncathenvironnement  ,
                                                            'ncathreglementaire':self.userwdgfield.checkBox_ncathreglementaire  ,
                                                          'ncathcommentaire' : self.userwdgfield.textBrowser_ncathcommentaire,
                                                          'ncathcategorie': self.userwdgfield.comboBox_ncathcategorie,

                                                          'ncaprocessus': self.userwdgfield.textBrowser_ncaprocessus,
                                                          'ncacause': self.userwdgfield.textBrowser_ncacause,

                                                          'ncb_accord': self.userwdgfield.comboBox_acceptation,
                                                          'ncb_datecible': self.userwdgfield.dateEdit_datecible,
                                                          'ncb_observation': self.userwdgfield.textBrowser_ncbobs,

                                                          'ncc_etatverif': self.userwdgfield.comboBox_etatverif,
                                                          'ncc_obs': self.userwdgfield.textBrowser_etatverif,
                                                          'ncc_date': self.userwdgfield.dateEdit_etatverif,

                                                          'ncd_leveereserve': self.userwdgfield.comboBox_leveres,
                                                          'ncd_leveereservecom': self.userwdgfield.textBrowser_leveres,

                                                          'nce_actioncorr': self.userwdgfield.comboBox_actioncorr,
                                                          'nce_actioncorrcom': self.userwdgfield.textBrowser_actioncorr,

                                                          # pva
                                                          'pva_datetime': self.userwdgfield.dateTimeEdit_pva,
                                                          'pva_commentaires': self.userwdgfield.textBrowser_pva,


                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}

            if self.parentWidget.dbasetablename == 'Desordre':
                self.parentWidget.userwdgfield.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)

            self.frame_editing.setVisible(False)

            # self.userwdgfield.tabWidget_formvisa.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")
            self.tabWidget_page_formvisa = self.userwdgfield.tabWidget_formvisa.widget(1)

            self.dbasechildwdgfield = []
            self.lamiawidgets = []

            #general
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgPHOTOGRAPHIE.NAME = None
            self.propertieswdgPHOTOGRAPHIE.CHECKGEOM = False
            self.propertieswdgPHOTOGRAPHIE.frame_editing.setVisible(False)
            # self.userwdgfield.tabWidget.widget(4).layout().addWidget(self.propertieswdgPHOTOGRAPHIE)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgCROQUIS.NAME = None
            # self.userwdgfield.tabWidget.widget(5).layout().addWidget(self.propertieswdgCROQUIS)
            # self.userwdgfield.toolox.widget(1).layout().addWidget(self.propertieswdgOBSERVATION2)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgRapport = BaseRapportTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgRapport.NAME = None
            self.propertieswdgRapport.CHECKGEOM = False
            self.propertieswdgRapport.frame_editing.setVisible(False)
            # self.userwdgfield.groupBox_NCB_PJ.layout().addWidget(self.propertieswdgRapport)
            self.dbasechildwdgfield.append(self.propertieswdgRapport)



            self.tabname_wdgtypedict = {'Photos': self.propertieswdgPHOTOGRAPHIE ,
                                        'Rapports': self.propertieswdgRapport ,
                                        'Proposition': self.propertieswdgRapport ,
                                        'Plans': self.propertieswdgCROQUIS}

            #NCA

            # def __init__(self, parentwdg=None, intervenantid=None, signatureid=None):
            self.signatureWidget = SignatureWidget(self, 'lid_intervenant_1', 'lid_ressource_1', 'datetimesignature_1' )
            #self.userwdgfield.tabWidget.widget(6).layout().addWidget(self.signatureWidget)
            self.userwdgfield.tabWidget_formvisa.widget(1).layout().addWidget(self.signatureWidget)
            self.lamiawidgets.append(self.signatureWidget)


            # NCB



            #self.signatureWidget2 = SignatureWidget(self, 'lid_intervenant_4', 'lid_ressource_4', 'datetimesignature_4' )
            #self.userwdgfield.tabWidget_avis.widget(1).layout().addWidget(self.signatureWidget2)
            if False:
                self.propertieswdgChooseResp = LidChooser(parentwdg=self, parentlidfield='lid_intervenant_4',
                                                            parentlabel=self.userwdgfield.label_ncbresponsable,
                                                            searchdbase='Intervenant', searchfieldtoshow=['nom','societe'])
                self.userwdgfield.frame_choisresp.layout().addWidget(self.propertieswdgChooseResp)

            lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_intervenant_4',
                                                            parentframe = self.userwdgfield.frame_choisresp,
                                                            searchdbase='Intervenant', searchfieldtoshow=['nom','societe'])
            self.lamiawidgets.append(lidchooser)

            # ncc
            #self.propertieswdgPHOTOGRAPHIE2 = BasePhotoTool(dbase=self.dbase, parentwidget=self)
            #self.propertieswdgPHOTOGRAPHIE2.NAME = None
            #self.userwdgfield.tabWidget_verif.widget(1).layout().addWidget(self.propertieswdgPHOTOGRAPHIE2)
            #self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE2)

            #self.signatureWidget3 = SignatureWidget(self, 'lid_intervenant_5', 'lid_ressource_5', 'datetimesignature_5' )
            #self.userwdgfield.tabWidget_verif.widget(2).layout().addWidget(self.signatureWidget3)

            # mise dispo
            if True:
                #self.propertieswdgRapport2 = BaseRapportTool(dbase=self.dbase, parentwidget=self)
                #self.propertieswdgRapport2.NAME = None
                #self.propertieswdgRapport2.CHECKGEOM = False
                #self.propertieswdgRapport2.frame_editing.setVisible(False)
                #self.userwdgfield.tabWidget_pvmisedispo.widget(4).layout().addWidget(self.propertieswdgRapport2)
                #self.dbasechildwdgfield.append(self.propertieswdgRapport2)

                #self.propertieswdgPHOTOGRAPHIE3 = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                #self.propertieswdgPHOTOGRAPHIE3.NAME = None
                #self.userwdgfield.tabWidget_pvmisedispo.widget(3).layout().addWidget(self.propertieswdgPHOTOGRAPHIE3)
                #self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE3)

                #entreprise preneuse
                lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_entpren_marche',
                                                            parentframe = self.userwdgfield.frame_entpren_marche,
                                                            searchdbase='Marche', searchfieldtoshow=['libelle'])
                self.lamiawidgets.append(lidchooser)


                self.signatureWidgetPreneuse = SignatureWidget(self, 'lid_entpren_intervenant',
                                                               'lid_ressource_entpren',
                                                               'lid_entpren_datetimesignature' )
                self.userwdgfield.groupBox_entpren_sign.layout().addWidget(self.signatureWidgetPreneuse)
                self.lamiawidgets.append(self.signatureWidgetPreneuse)

                #entreprise occupante
                lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_entocc_marche',
                                                                parentframe = self.userwdgfield.frame_entocc_marche,
                                                                searchdbase='Marche', searchfieldtoshow=['libelle'])
                self.lamiawidgets.append(lidchooser)

                self.signatureWidgetOccupante = SignatureWidget(self, 'lid_entocc_intervenant',
                                                               'lid_ressource_entocc',
                                                               'lid_entocc_datetimesignature' )
                self.userwdgfield.groupBox_entocc_sign.layout().addWidget(self.signatureWidgetOccupante)
                self.lamiawidgets.append(self.signatureWidgetOccupante)


    def changeGroupe(self, comboindex):
        parentcombotext = self.parentWidget.userwdgfield.comboBox_groupedes.currentText()
        if parentcombotext == 'Non-conformité':
            self.userwdgfield.stackedWidget_2.setCurrentIndex(0)
        elif parentcombotext == 'Procès-verbal':
            self.userwdgfield.stackedWidget_2.setCurrentIndex(5)



    def setOBSTYPE(self, obstype, boolsignature):
        if obstype is None:
            self.userwdgfield.tabWidget_formvisa.removeTab(1)
            return

        self.OBSTYPE = obstype

        if boolsignature:
            self.userwdgfield.tabWidget_formvisa.insertTab(1, self.tabWidget_page_formvisa, 'Visa')
        else:
            self.userwdgfield.tabWidget_formvisa.removeTab(1)

    def featureSelected(self, item=None, itemisid=False):
        super(BaseChantierTramObservationTool, self).featureSelected(item,itemisid)
        if item is None:
            self.saveFeature()


    def postSaveFeature(self, boolnewfeature):

        if self.currentFeaturePK is not None:
            sql = "UPDATE Observation SET typeobservation = '" + str(self.OBSTYPE) + "'"
            sql += " WHERE pk_observation = " + str(self.currentFeaturePK)
            self.dbase.query(sql)

        # self.signatureWidget.postSaveFeature(boolnewfeature)

        if self.OBSTYPE[0:2] == 'PV':
            pass
            # self.signatureWidgetOccupante.postSaveFeature(boolnewfeature)
            # self.signatureWidgetPreneuse.postSaveFeature(boolnewfeature)


        if (self.OBSTYPE[0:2] == 'NC'):
            self.parentWidget.updateListSymbols()


    def postloadIds(self,sqlin):
        sqlout = sqlin + " AND typeobservation = '" + str(self.OBSTYPE) + "'"
        return sqlout




    def postInitFeatureProperties(self, feat):
        super(BaseChantierTramObservationTool, self).postInitFeatureProperties(feat)

        # init signature and lidchooser
        if self.OBSTYPE is not None:
            pass
            # self.signatureWidget.postInitFeatureProperties(feat)

        # init date widget when feature creation
        if self.OBSTYPE is not None and self.currentFeaturePK is None:
            if self.OBSTYPE == 'NCB':
                valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d"))
                self.userwdgfield.dateEdit_datecible.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd'))
            elif self.OBSTYPE == 'NCC':
                valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d"))
                self.userwdgfield.dateEdit_etatverif.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd'))
            elif self.OBSTYPE == 'PVA':
                valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.userwdgfield.dateTimeEdit_pva.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd hh:mm:ss'))


        # check if good stackedwidget page
        if self.OBSTYPE is not None:
            # if self.indexstackedpage is None:
            for i in range(self.userwdgfield.stackedWidget_2.count()):
                # print(self.userwdgfield.stackedWidget_2.widget(i).objectName())
                if self.userwdgfield.stackedWidget_2.widget(i).objectName() == self.OBSTYPE:
                    self.indexstackedpage = i
                    break
            self.userwdgfield.stackedWidget_2.setCurrentIndex(self.indexstackedpage)

            # put photo and rapport the right place
            currentwdg = self.userwdgfield.stackedWidget_2.currentWidget().layout().itemAt(0).widget()
            if isinstance(currentwdg, QTabWidget):
                tabtext = [currentwdg.tabText(i) for i in range(currentwdg.count())]
                for tabname in self.tabname_wdgtypedict.keys():
                    if tabname in tabtext:
                        indextab = tabtext.index(tabname)
                        currentwdg.widget(indextab).layout().addWidget(self.tabname_wdgtypedict[tabname])




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantiertram_observation_tool_ui.ui')
        uic.loadUi(uipath, self)







