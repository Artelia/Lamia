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

from ..base3.lamiabase_observation_tool import BaseObservationTool

from .lamiabase_cs_sketch_tool import BaseConstructionsiteSketchTool as BaseSketchTool
from .lamiabase_cs_camera_tool import BaseConstructionsiteCameraTool as BaseCameraTool
from .lamiabase_cs_report_tool import BaseConstructionsiteReportTool as BaseReportTool
from .lamiabase_cs_actor_tool import BaseConstructionsiteActorTool as BaseActorTool
#from ..subwidgets.lamiabasechantier_signature_tool import SignatureWidget
#from .lamiabasechantier_lidchooser import LidChooserWidget
from .lamiabase_cs_subobservation_tool import BaseConstructionsiteSubObservationTool

from ..subwidgets.subwidget_signature import SignatureWidget
from ..subwidgets.subwidget_lidchooser import LidChooserWidget



class BaseConstructionsiteObservationTool(BaseObservationTool):


    #OBSTYPE = None
    tooltreewidgetSUBCAT = None

    def __init__(self, **kwargs):
        super(BaseConstructionsiteObservationTool, self).__init__(**kwargs)
        self.indexstackedpage = None






    def initMainToolWidget(self):


        if self.dbase.variante in [None, 'Lamia']:

            self.toolwidgetmain = UserUI()
            self.toolwidgetmain.stackedWidget_2.removeWidget(self.toolwidgetmain.stackedWidget_2.widget(0))
            self.ncawidget = NcaLamia(self.toolwidgetmain)
            self.toolwidgetmain.stackedWidget_2.insertWidget(0,self.ncawidget)
            self.toolwidgetmain.stackedWidget_2.widget(0).setObjectName('NCA')
            
            self.formtoolwidgetconfdictmain = {'observation' : {'linkfield' : 'id_observation',
                                                        'widgets' : {'datetimeobservation': self.toolwidgetmain.dateTimeEdit_datetimeobservation,
                                                            
                                                                    'ncadescription': self.ncawidget.textBrowser_ncadescription,

                                                                    'ncathqualite':self.ncawidget.checkBox_ncathqualite  ,
                                                                    'ncathouvrage':self.ncawidget.checkBox_ncathouvrage  ,
                                                                    'ncathsecurite':self.ncawidget.checkBox_ncathsecurite  ,
                                                                    'ncathsystem':self.ncawidget.checkBox_ncathsystem  ,
                                                                    'ncathenvironnement':self.ncawidget.checkBox_ncathenvironnement  ,
                                                                    'ncathreglementaire':self.ncawidget.checkBox_ncathreglementaire  ,
                                                                    'ncathcommentaire' : self.ncawidget.textBrowser_ncathcommentaire,
                                                                    'ncathcategorie': self.ncawidget.comboBox_ncathcategorie,

                                                                    'ncaprocessus': self.ncawidget.textBrowser_ncaprocessus,
                                                                    'ncacause': self.ncawidget.textBrowser_ncacause,

                                                                    'ncb_accord': self.toolwidgetmain.comboBox_acceptation,
                                                                    'ncb_datecible': self.toolwidgetmain.dateEdit_datecible,
                                                                    'ncb_observation': self.toolwidgetmain.textBrowser_ncbobs,

                                                                    'ncc_etatverif': self.toolwidgetmain.comboBox_etatverif,
                                                                    'ncc_obs': self.toolwidgetmain.textBrowser_etatverif,
                                                                    # 'ncc_date': self.toolwidgetmain.dateEdit_etatverif,

                                                                    'ncd_leveereserve': self.toolwidgetmain.comboBox_leveres,
                                                                    'ncd_leveereservecom': self.toolwidgetmain.textBrowser_leveres,

                                                                    'nce_actioncorr': self.toolwidgetmain.comboBox_actioncorr,
                                                                    'nce_actioncorrcom': self.toolwidgetmain.textBrowser_actioncorr,

                                                                    # pva
                                                                    'pva_datetime': self.toolwidgetmain.dateTimeEdit_pva,
                                                                    'pva_commentaires': self.toolwidgetmain.textBrowser_pva,


                                                                    }},
                                        'object' : {'linkfield' : 'object',
                                                    'widgets' : {}}}




            self.tabWidget_page_formvisa = self.toolwidgetmain.tabWidget_formvisa.widget(1)



            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            self.lamiawidgets = []

            #general
            self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
            self.propertieswdgPHOTOGRAPHIE.NAME = None
            self.propertieswdgPHOTOGRAPHIE.CHECKGEOM = False
            #self.propertieswdgPHOTOGRAPHIE.frame_editing.setVisible(False)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
            self.propertieswdgCROQUIS.tooltreewidgetSUBCAT = 'Plans'
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgRapport = BaseReportTool(**self.instancekwargs)
            self.propertieswdgRapport.NAME = None
            # self.propertieswdgRapport.CHECKGEOM = False
            self.propertieswdgRapport.GEOMETRYSKIP = True
            #self.propertieswdgRapport.frame_editing.setVisible(False)
            self.dbasechildwdgfield.append(self.propertieswdgRapport)

            self.tabname_wdgtypedict = {'Photos': self.propertieswdgPHOTOGRAPHIE ,
                                        'Rapports': self.propertieswdgRapport ,
                                        'Proposition': self.propertieswdgRapport ,
                                        'Plans': self.propertieswdgCROQUIS}

            
            if 'observationcategory' in self.TABLEFILTERFIELD.keys():
                observationcategory = self.TABLEFILTERFIELD['observationcategory']
                for i in range(self.toolwidgetmain.stackedWidget_2.count()):
                    # print(self.toolwidgetmain.stackedWidget_2.widget(i).objectName())
                    if self.toolwidgetmain.stackedWidget_2.widget(i).objectName() == observationcategory:
                        #self.indexstackedpage = i
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(i)
                #NCA
                if observationcategory == 'NCA':
                    signatureWidget = SignatureWidget(self, 'lid_actor_1', 'lid_resource_1', 'datetimesignature_1',
                                                            parentframe=self.toolwidgetmain.tabWidget_formvisa.widget(1))
                    # self.toolwidgetmain.tabWidget_formvisa.widget(1).layout().addWidget(self.signatureWidget)
                    self.lamiawidgets.append(signatureWidget)
                # NCB
                elif observationcategory == 'NCB':
                    lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_actor_1',
                                                                    parentframe = self.toolwidgetmain.frame_choisresp,
                                                                    searchdbase='actor', searchfieldtoshow=['actorname','society'])
                    self.lamiawidgets.append(lidchooser)
                    self.toolwidgetmain.tabWidget_formvisa.removeTab(1)

                # mise dispo
                #if True:
                elif observationcategory == 'PVA':
                    #entreprise preneuse
                    # lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_entpren_marche',
                    #                                             parentframe = self.toolwidgetmain.frame_entpren_marche,
                    #                                             searchdbase='Marche', searchfieldtoshow=['libelle'])
                    lidchooser = LidChooserWidget(parentwdg=self, 
                                                    parentlidfield='lid_delivery_1',
                                                                parentframe = self.toolwidgetmain.frame_entpren_marche,
                                                                searchdbase='delivery', searchfieldtoshow=['name'])
                    self.lamiawidgets.append(lidchooser)


                    # self.signatureWidgetPreneuse = SignatureWidget(self, 'lid_actor_1',
                    #                                                 'lid_resource_1',
                    #                                                 'lid_entpren_datetimesignature' )
                    signatureWidgetPreneuse = SignatureWidget(self, 
                                                                    'lid_actor_1', 
                                                                    'lid_resource_1', 
                                                                    'datetimesignature_1' ,
                                                                    parentframe=self.toolwidgetmain.groupBox_entpren_sign)
                    # self.toolwidgetmain.groupBox_entpren_sign.layout().addWidget(self.signatureWidgetPreneuse)
                    self.lamiawidgets.append(signatureWidgetPreneuse)

                    #entreprise occupante
                    # lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_entocc_marche',
                    #                                                 parentframe = self.toolwidgetmain.frame_entocc_marche,
                    #                                                 searchdbase='Marche', searchfieldtoshow=['libelle'])
                    lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_delivery_2',
                                                                    parentframe = self.toolwidgetmain.frame_entocc_marche,
                                                                    searchdbase='delivery', searchfieldtoshow=['name'])
                    self.lamiawidgets.append(lidchooser)

                    # self.signatureWidgetOccupante = SignatureWidget(self, 'lid_entocc_intervenant',
                    #                                                 'lid_ressource_entocc',
                    #                                                 'lid_entocc_datetimesignature' )
                    signatureWidgetOccupante = SignatureWidget(self, 'lid_actor_2', 'lid_resource_2', 'datetimesignature_2',
                                                                    parentframe=self.toolwidgetmain.groupBox_entocc_sign)
                    
                    # self.toolwidgetmain.groupBox_entocc_sign.layout().addWidget(self.signatureWidgetOccupante)
                    self.lamiawidgets.append(signatureWidgetOccupante)

                    self.toolwidgetmain.tabWidget_formvisa.removeTab(1)
                
                else:
                    self.toolwidgetmain.tabWidget_formvisa.removeTab(1)

        elif self.dbase.variante in ['Orange']:
            # ****************************************************************************************
            # userui
            self.toolwidgetmain = UserUI_Orange()
            self.formtoolwidgetconfdictmain = {'observation': {'linkfield': 'id_observation',
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
                                                                # 'ncc_date': self.toolwidgetmain.dateEdit_etatverif,

                                                                'ncd_leveereserve': self.toolwidgetmain.comboBox_leveres,
                                                                'ncd_leveereservecom': self.toolwidgetmain.textBrowser_leveres,

                                                                'nce_actioncorr': self.toolwidgetmain.comboBox_actioncorr,
                                                                'nce_actioncorrcom': self.toolwidgetmain.textBrowser_actioncorr,

                                                                }},
                                            'object': {'linkfield': 'id_object',
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
            self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
            self.propertieswdgPHOTOGRAPHIE.NAME = None
            self.propertieswdgPHOTOGRAPHIE.CHECKGEOM = False
            #self.propertieswdgPHOTOGRAPHIE.frame_editing.setVisible(False)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
            self.propertieswdgCROQUIS.NAME = None
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgRapport = BaseReportTool(**self.instancekwargs)
            self.propertieswdgRapport.NAME = None
            self.propertieswdgRapport.CHECKGEOM = False
            #self.propertieswdgRapport.frame_editing.setVisible(False)
            self.dbasechildwdgfield.append(self.propertieswdgRapport)

            self.tabname_wdgtypedict = {'Photos': self.propertieswdgPHOTOGRAPHIE ,
                                        'Rapports': self.propertieswdgRapport ,
                                        'Proposition': self.propertieswdgRapport ,
                                        'Plans': self.propertieswdgCROQUIS}

            if 'observationcategory' in self.TABLEFILTERFIELD.keys():
                observationcategory = self.TABLEFILTERFIELD['observationcategory']
                for i in range(self.toolwidgetmain.stackedWidget_2.count()):
                    if self.toolwidgetmain.stackedWidget_2.widget(i).objectName() == observationcategory:
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(i)
                #NCA
                if observationcategory == 'NCA':
                    # visa nca MOE
                    self.signatureWidgetMOE = SignatureWidget(self, 'lid_actor_1', 'lid_resource_1', 'datetimesignature_1',
                                                            parentframe=self.toolwidgetmain.tabWidget_multivisa.widget(0) )
                    # self.toolwidgetmain.tabWidget_multivisa.widget(0).layout().addWidget(self.signatureWidgetMOE)
                    self.lamiawidgets.append(self.signatureWidgetMOE)

                    # visa nca ETP
                    self.signatureWidgetETP = SignatureWidget(self, 'lid_actor_2', 'lid_resource_2', 'datetimesignature_2',
                                                              parentframe=self.toolwidgetmain.tabWidget_multivisa.widget(1)  )
                    # self.toolwidgetmain.tabWidget_multivisa.widget(1).layout().addWidget(self.signatureWidgetETP)
                    self.lamiawidgets.append(self.signatureWidgetETP)

                    # sous fiche
                    self.sousficheWidget = BaseConstructionsiteSubObservationTool(**self.instancekwargs)
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



    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        # self._setVisaTabBehaviour()
        # print('postSelectFeature Obs', self.OBSTYPE, self.toolwidgetmain.stackedWidget_2.currentIndex()) 
        #super(BaseChantierObservationTool, self).postSelectFeature()
        if self.currentFeaturePK is None:

            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict({'datetimeobservation': datecreation}, checkifinforgottenfield=False)

            if 'observationcategory' in self.TABLEFILTERFIELD.keys() and self.currentFeaturePK is None:
                observationcategory = self.TABLEFILTERFIELD['observationcategory']
                valuedate = str(datetime.datetime.now().strftime("%Y-%m-%d"))
                valuedatetime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                if observationcategory == 'NCB':
                    self.toolwidgetmain.dateEdit_datecible.setDateTime(QtCore.QDateTime.fromString(valuedate, 'yyyy-MM-dd'))
                # elif observationcategory == 'NCC':
                #     self.toolwidgetmain.dateEdit_etatverif.setDateTime(QtCore.QDateTime.fromString(valuedate, 'yyyy-MM-dd'))
                elif observationcategory== 'PVA':
                    self.toolwidgetmain.dateTimeEdit_pva.setDateTime(QtCore.QDateTime.fromString(valuedatetime, 'yyyy-MM-dd hh:mm:ss'))


    def postSaveFeature(self, featurepk=None):
        obstype = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                              'observationcategory',
                                               featurepk )

        if (obstype[0:2] == 'NC'):
            self.parentWidget.updateListSymbols()






    # def postloadIds(self,sqlin):
    #     sqlout = sqlin + " AND typeobservation = '" + str(self.OBSTYPE) + "' AND lid_observation IS NULL"
    #     return sqlout






class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_cs_observation_tool_ui.ui')
        uic.loadUi(uipath, self)


class NcaLamia(QWidget):
    def __init__(self, parent=None):
        super(NcaLamia, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__),'ncawidget', 'lamiabase_cs_observation_nca_lamia.ui')
        uic.loadUi(uipath, self)

class NcaOrange(QWidget):
    def __init__(self, parent=None):
        super(NcaOrange, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__),'ncawidget', 'lamiabase_cs_observation_nca_orange.ui')
        uic.loadUi(uipath, self)





