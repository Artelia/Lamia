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
from qgis.PyQt.QtWidgets import (QWidget, QTabWidget)

from ..base2.lamiabase_observation_tool import BaseObservationTool

from .lamiabasechantier_photo_tool import BaseChantierPhotoTool as BasePhotoTool
from .lamiabasechantier_croquis_tool import BaseChantierCroquisTool as BaseCroquisTool
from .lamiabasechantier_intervenant_tool import BaseChantierIntervenantTool as BaseIntervenantTool
from .lamiabasechantier_rapport_tool import BaseChantierRapportTool as BaseRapportTool
#from ..subwidgets.lamiabasechantier_signature_tool import SignatureWidget
#from .lamiabasechantier_lidchooser import LidChooserWidget
from .lamiabasechantier_sousobservation_tool import BaseChantierSousObservationTool

from ..subwidgets.subwidget_signature import SignatureWidget
from ..subwidgets.subwidget_lidchooser import LidChooserWidget



class BaseChantierObservationTool(BaseObservationTool):


    #OBSTYPE = None
    tooltreewidgetSUBCAT = None

    def __init__(self, **kwargs):
        super(BaseChantierObservationTool, self).__init__(**kwargs)
        self.indexstackedpage = None






    def initMainToolWidget(self):

        if self.dbase.variante in [None, 'Lamia']:

            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {'Observation' : {'linkfield' : 'id_observation',
                                                        'widgets' : {'ncadescription': self.toolwidgetmain.textBrowser_ncadescription,

                                                                    'ncathqualite':self.toolwidgetmain.checkBox_ncathqualite  ,
                                                                    'ncathouvrage':self.toolwidgetmain.checkBox_ncathouvrage  ,
                                                                    'ncathsecurite':self.toolwidgetmain.checkBox_ncathsecurite  ,
                                                                    'ncathsystem':self.toolwidgetmain.checkBox_ncathsystem  ,
                                                                    'ncathenvironnement':self.toolwidgetmain.checkBox_ncathenvironnement  ,
                                                                    'ncathreglementaire':self.toolwidgetmain.checkBox_ncathreglementaire  ,
                                                                    'ncathcommentaire' : self.toolwidgetmain.textBrowser_ncathcommentaire,
                                                                    'ncathcategorie': self.toolwidgetmain.comboBox_ncathcategorie,

                                                                    'ncaprocessus': self.toolwidgetmain.textBrowser_ncaprocessus,
                                                                    'ncacause': self.toolwidgetmain.textBrowser_ncacause,

                                                                    'ncb_accord': self.toolwidgetmain.comboBox_acceptation,
                                                                    'ncb_datecible': self.toolwidgetmain.dateEdit_datecible,
                                                                    'ncb_observation': self.toolwidgetmain.textBrowser_ncbobs,

                                                                    'ncc_etatverif': self.toolwidgetmain.comboBox_etatverif,
                                                                    'ncc_obs': self.toolwidgetmain.textBrowser_etatverif,
                                                                    'ncc_date': self.toolwidgetmain.dateEdit_etatverif,

                                                                    'ncd_leveereserve': self.toolwidgetmain.comboBox_leveres,
                                                                    'ncd_leveereservecom': self.toolwidgetmain.textBrowser_leveres,

                                                                    'nce_actioncorr': self.toolwidgetmain.comboBox_actioncorr,
                                                                    'nce_actioncorrcom': self.toolwidgetmain.textBrowser_actioncorr,

                                                                    # pva
                                                                    'pva_datetime': self.toolwidgetmain.dateTimeEdit_pva,
                                                                    'pva_commentaires': self.toolwidgetmain.textBrowser_pva,


                                                                    }},
                                        'Objet' : {'linkfield' : 'id_objet',
                                                    'widgets' : {}}}

            #if self.parentWidget.DBASETABLENAME == 'Desordre':
            #    self.parentWidget.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)

            # self.frame_editing.setVisible(False)
            #self.frame_editing.setParent(None)

            self.tabWidget_page_formvisa = self.toolwidgetmain.tabWidget_formvisa.widget(1)

            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            self.lamiawidgets = []

            #general
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.propertieswdgPHOTOGRAPHIE.NAME = None
            self.propertieswdgPHOTOGRAPHIE.CHECKGEOM = False
            #self.propertieswdgPHOTOGRAPHIE.frame_editing.setVisible(False)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.propertieswdgCROQUIS.tooltreewidgetSUBCAT = 'Plans'
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgRapport = BaseRapportTool(**self.instancekwargs)
            self.propertieswdgRapport.NAME = None
            self.propertieswdgRapport.CHECKGEOM = False
            #self.propertieswdgRapport.frame_editing.setVisible(False)
            self.dbasechildwdgfield.append(self.propertieswdgRapport)

            self.tabname_wdgtypedict = {'Photos': self.propertieswdgPHOTOGRAPHIE ,
                                        'Rapports': self.propertieswdgRapport ,
                                        'Proposition': self.propertieswdgRapport ,
                                        'Plans': self.propertieswdgCROQUIS}

            
            if 'typeobservation' in self.TABLEFILTERFIELD.keys():
                typeobservation = self.TABLEFILTERFIELD['typeobservation']
                for i in range(self.toolwidgetmain.stackedWidget_2.count()):
                    # print(self.toolwidgetmain.stackedWidget_2.widget(i).objectName())
                    if self.toolwidgetmain.stackedWidget_2.widget(i).objectName() == typeobservation:
                        #self.indexstackedpage = i
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(i)
                #NCA
                if typeobservation == 'NCA':
                    self.signatureWidget = SignatureWidget(self, 'lid_intervenant_1', 'lid_ressource_1', 'datetimesignature_1' )
                    self.toolwidgetmain.tabWidget_formvisa.widget(1).layout().addWidget(self.signatureWidget)
                    self.lamiawidgets.append(self.signatureWidget)
                # NCB
                elif typeobservation == 'NCA':
                    lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_intervenant_4',
                                                                    parentframe = self.toolwidgetmain.frame_choisresp,
                                                                    searchdbase='Intervenant', searchfieldtoshow=['nom','societe'])
                    self.lamiawidgets.append(lidchooser)
                    self.toolwidgetmain.tabWidget_formvisa.removeTab(1)

                # mise dispo
                #if True:
                elif typeobservation == 'PVA':
                    #entreprise preneuse
                    lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_entpren_marche',
                                                                parentframe = self.toolwidgetmain.frame_entpren_marche,
                                                                searchdbase='Marche', searchfieldtoshow=['libelle'])
                    self.lamiawidgets.append(lidchooser)


                    self.signatureWidgetPreneuse = SignatureWidget(self, 'lid_entpren_intervenant',
                                                                    'lid_ressource_entpren',
                                                                    'lid_entpren_datetimesignature' )
                    self.toolwidgetmain.groupBox_entpren_sign.layout().addWidget(self.signatureWidgetPreneuse)
                    self.lamiawidgets.append(self.signatureWidgetPreneuse)

                    #entreprise occupante
                    lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_entocc_marche',
                                                                    parentframe = self.toolwidgetmain.frame_entocc_marche,
                                                                    searchdbase='Marche', searchfieldtoshow=['libelle'])
                    self.lamiawidgets.append(lidchooser)

                    self.signatureWidgetOccupante = SignatureWidget(self, 'lid_entocc_intervenant',
                                                                    'lid_ressource_entocc',
                                                                    'lid_entocc_datetimesignature' )
                    self.toolwidgetmain.groupBox_entocc_sign.layout().addWidget(self.signatureWidgetOccupante)
                    self.lamiawidgets.append(self.signatureWidgetOccupante)
                
                else:
                    self.toolwidgetmain.tabWidget_formvisa.removeTab(1)

        elif self.dbase.variante in ['Orange']:
            # ****************************************************************************************
            # userui
            self.toolwidgetmain = UserUI_Orange()
            self.formtoolwidgetconfdictmain = {'Observation': {'linkfield': 'id_observation',
                                                            'widgets': {
                                                                'datetimeobservation': self.toolwidgetmain.dateTimeEdit_datetimeobs,
                                                                'nca_meteo': self.toolwidgetmain.lineEdit_meteo,
                                                                'nca_mandataire': self.toolwidgetmain.comboBox_mandataire,
                                                                'nca_etp_presentes': self.toolwidgetmain.lineEdit_etppres,

                                                                'nca_planning': self.toolwidgetmain.comboBox_planning,
                                                                'nca_planning_com': self.toolwidgetmain.textBrowser_planningcom,

                                                                'nca_effectif_entreprise': self.toolwidgetmain.spinBox_effectetp,
                                                                'nca_effectif_sstraitant': self.toolwidgetmain.spinBox_effectsstraitant,
                                                                'nca_conducteurdetravaux': self.toolwidgetmain.checkBox_conduc,

                                                                'nca_engins_pelle': self.toolwidgetmain.checkBox_eng_pelle,
                                                                'nca_engins_chargeuse': self.toolwidgetmain.checkBox_eng_charg,
                                                                'nca_engins_compresseur': self.toolwidgetmain.checkBox_eng_compres,
                                                                'nca_engins_trancheuse': self.toolwidgetmain.checkBox_eng_trancheuse,
                                                                'nca_engins_camionsmat': self.toolwidgetmain.checkBox_eng_cam_mat,
                                                                'nca_engins_camiondeb': self.toolwidgetmain.checkBox_eng_cam_deblais,
                                                                'nca_engins_camionasp': self.toolwidgetmain.checkBox_eng_cam_aspi,
                                                                'nca_engins_camionrep': self.toolwidgetmain.checkBox_eng_cam_repand,
                                                                'nca_engins_camionmal': self.toolwidgetmain.checkBox_eng_cam_malax,
                                                                'nca_engins_container': self.toolwidgetmain.checkBox_eng_container,
                                                                'nca_engins_compacteur': self.toolwidgetmain.checkBox_eng_compacteur,
                                                                'nca_engins_finisseur': self.toolwidgetmain.checkBox_eng_finisseur,
                                                                'nca_engins_minipelle': self.toolwidgetmain.checkBox_eng_minipelle,
                                                                'nca_engins_nacelle': self.toolwidgetmain.checkBox_eng_nacelle,
                                                                'nca_engins_autres': self.toolwidgetmain.checkBox_eng_autre,

                                                                'nca_sec_personnel': self.toolwidgetmain.comboBox_sec_personnel,
                                                                'nca_sec_protection': self.toolwidgetmain.comboBox_sec_protection,
                                                                'nca_sec_afficharrete': self.toolwidgetmain.comboBox_sec_afficharrete,
                                                                'nca_sec_panneauxchant': self.toolwidgetmain.comboBox_sec_panneauxchant,
                                                                'nca_sec_circul': self.toolwidgetmain.comboBox_sec_circul,
                                                                'nca_sec_eclairage': self.toolwidgetmain.comboBox_sec_eclairage,
                                                                'nca_sec_stockagedechet': self.toolwidgetmain.comboBox_sec_stockagedechet,
                                                                'nca_sec_proprete': self.toolwidgetmain.comboBox_sec_proprete,
                                                                'nca_sec_protectiontranchee': self.toolwidgetmain.comboBox_sec_protectiontranchee,
                                                                'nca_sec_blindage': self.toolwidgetmain.comboBox_sec_blindage,
                                                                'nca_sec_reunionmarquage': self.toolwidgetmain.comboBox_sec_reunionmarquage,
                                                                'nca_sec_entretienmarquage': self.toolwidgetmain.comboBox_sec_entretienmarquage,
                                                                'nca_sec_accesscoupure': self.toolwidgetmain.comboBox_sec_accesscoupure,
                                                                'nca_sec_travailhauteur': self.toolwidgetmain.comboBox_sec_travailhauteur,
                                                                'nca_sec_plaintes': self.toolwidgetmain.comboBox_sec_plaintes,
                                                                'nca_sec_plaintes_com': self.toolwidgetmain.lineEdit_sec_plaintes_com,

                                                                'ncb_accord': self.toolwidgetmain.comboBox_acceptation,
                                                                'ncb_datecible': self.toolwidgetmain.dateEdit_datecible,
                                                                'ncb_observation': self.toolwidgetmain.textBrowser_ncbobs,

                                                                'ncc_etatverif': self.toolwidgetmain.comboBox_etatverif,
                                                                'ncc_obs': self.toolwidgetmain.textBrowser_etatverif,
                                                                'ncc_date': self.toolwidgetmain.dateEdit_etatverif,

                                                                'ncd_leveereserve': self.toolwidgetmain.comboBox_leveres,
                                                                'ncd_leveereservecom': self.toolwidgetmain.textBrowser_leveres,

                                                                'nce_actioncorr': self.toolwidgetmain.comboBox_actioncorr,
                                                                'nce_actioncorrcom': self.toolwidgetmain.textBrowser_actioncorr,

                                                                }},
                                            'Objet': {'linkfield': 'id_objet',
                                                    'widgets': {}}}

            #if self.parentWidget.DBASETABLENAME == 'Desordre':
            #    self.parentWidget.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)

            # self.frame_editing.setVisible(False)
            #self.frame_editing.setParent(None)

            self.toolwidgetmain.toolButton_effect_etp.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_effectetp))
            self.toolwidgetmain.toolButton_effect_sstraitant.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_effectsstraitant))

            self.tabWidget_page_formvisa = self.toolwidgetmain.tabWidget_formvisa.widget(1)
            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            self.lamiawidgets = []

            #general
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.propertieswdgPHOTOGRAPHIE.NAME = None
            self.propertieswdgPHOTOGRAPHIE.CHECKGEOM = False
            #self.propertieswdgPHOTOGRAPHIE.frame_editing.setVisible(False)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.propertieswdgCROQUIS.NAME = None
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgRapport = BaseRapportTool(**self.instancekwargs)
            self.propertieswdgRapport.NAME = None
            self.propertieswdgRapport.CHECKGEOM = False
            #self.propertieswdgRapport.frame_editing.setVisible(False)
            self.dbasechildwdgfield.append(self.propertieswdgRapport)

            self.tabname_wdgtypedict = {'Photos': self.propertieswdgPHOTOGRAPHIE ,
                                        'Rapports': self.propertieswdgRapport ,
                                        'Proposition': self.propertieswdgRapport ,
                                        'Plans': self.propertieswdgCROQUIS}

            if 'typeobservation' in self.TABLEFILTERFIELD.keys():
                typeobservation = self.TABLEFILTERFIELD['typeobservation']
                for i in range(self.toolwidgetmain.stackedWidget_2.count()):
                    # print(self.toolwidgetmain.stackedWidget_2.widget(i).objectName())
                    if self.toolwidgetmain.stackedWidget_2.widget(i).objectName() == typeobservation:
                        #self.indexstackedpage = i
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(i)
                #NCA
                if typeobservation == 'NCA':
                    #self.signatureWidget = SignatureWidget(self, 'lid_intervenant_1', 'lid_ressource_1', 'datetimesignature_1' )
                    #self.toolwidgetmain.tabWidget_formvisa.widget(1).layout().addWidget(self.signatureWidget)
                    #self.lamiawidgets.append(self.signatureWidget)
            
            
                    # visa nca MOE
                    self.signatureWidgetMOE = SignatureWidget(self, 'lid_intervenant_1', 'lid_ressource_1', 'datetimesignature_1' )
                    self.toolwidgetmain.tabWidget_multivisa.widget(0).layout().addWidget(self.signatureWidgetMOE)
                    self.lamiawidgets.append(self.signatureWidgetMOE)

                    # visa nca ETP
                    self.signatureWidgetETP = SignatureWidget(self, 'lid_intervenant_2', 'lid_ressource_2', 'datetimesignature_2')
                    self.toolwidgetmain.tabWidget_multivisa.widget(1).layout().addWidget(self.signatureWidgetETP)
                    self.lamiawidgets.append(self.signatureWidgetETP)

                    # sous fiche
                    self.sousficheWidget = BaseChantierSousObservationTool(**self.instancekwargs)
                    self.sousficheWidget.tooltreewidgetSUBCAT = 'Fiches\ndétaillées'
                    self.dbasechildwdgfield.insert(0,self.sousficheWidget)
                    #self.toolwidgetmain.tabWidget_nca.widget(1).layout().addWidget(self.sousficheWidget )




    def changeGroupe(self, comboindex):
        parentcombotext = self.parentWidget.toolwidgetmain.comboBox_groupedes.currentText()
        if parentcombotext == 'Non-conformité':
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
        elif parentcombotext == 'Procès-verbal':
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(5)


    """
    def setOBSTYPE(self, obstype, boolsignature):
        if obstype is None:
            self.toolwidgetmain.tabWidget_formvisa.removeTab(1)
            return

        self.OBSTYPE = obstype

        if boolsignature:
            self.toolwidgetmain.tabWidget_formvisa.insertTab(1, self.tabWidget_page_formvisa, 'Visa')
        else:
            self.toolwidgetmain.tabWidget_formvisa.removeTab(1)



    def featureSelected(self, item=None, itemisid=False):
        super(BaseChantierObservationTool, self).featureSelected(item,itemisid)
        if item is None:
            self.saveFeature()
    """

    def postSaveFeature(self, featurepk=None):
        obstype = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                              'typeobservation',
                                               featurepk )

        if (obstype[0:2] == 'NC'):
            self.parentWidget.updateListSymbols()


        if False:
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
        sqlout = sqlin + " AND typeobservation = '" + str(self.OBSTYPE) + "' AND lid_observation IS NULL"
        return sqlout




    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        pass
        # print('postSelectFeature Obs', self.OBSTYPE, self.toolwidgetmain.stackedWidget_2.currentIndex()) 
        #super(BaseChantierObservationTool, self).postSelectFeature()
        if False:
            # init signature and lidchooser
            if self.OBSTYPE is not None:
                pass
                # self.signatureWidget.postInitFeatureProperties(feat)

            # init date widget when feature creation
            if self.OBSTYPE is not None and self.currentFeaturePK is None:
                if self.OBSTYPE == 'NCB':
                    valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d"))
                    self.toolwidgetmain.dateEdit_datecible.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd'))
                elif self.OBSTYPE == 'NCC':
                    valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d"))
                    self.toolwidgetmain.dateEdit_etatverif.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd'))
                elif self.OBSTYPE == 'PVA':
                    valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    self.toolwidgetmain.dateTimeEdit_pva.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd hh:mm:ss'))

            if False:
                # check if good stackedwidget page
                if self.OBSTYPE is not None:
                    # if self.indexstackedpage is None:
                    for i in range(self.toolwidgetmain.stackedWidget_2.count()):
                        # print(self.toolwidgetmain.stackedWidget_2.widget(i).objectName())
                        if self.toolwidgetmain.stackedWidget_2.widget(i).objectName() == self.OBSTYPE:
                            self.indexstackedpage = i
                            break
                    self.toolwidgetmain.stackedWidget_2.setCurrentIndex(self.indexstackedpage)

                # put photo and rapport the right place
                if False:
                    currentwdg = self.toolwidgetmain.stackedWidget_2.currentWidget().layout().itemAt(0).widget()
                    if self.dbase.variante in ['Orange']:
                        try:
                            currentwdg = currentwdg.widget(0).layout().itemAt(0).widget()
                        except AttributeError as e:
                            pass
                    if isinstance(currentwdg, QTabWidget):
                        tabtext = [currentwdg.tabText(i) for i in range(currentwdg.count())]
                        for tabname in self.tabname_wdgtypedict.keys():
                            if tabname in tabtext:
                                indextab = tabtext.index(tabname)
                                currentwdg.widget(indextab).layout().addWidget(self.tabname_wdgtypedict[tabname])




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantier_observation_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUI_Orange(QWidget):
    def __init__(self, parent=None):
        super(UserUI_Orange, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantier_observation_tool_orange_ui.ui')
        uic.loadUi(uipath, self)






