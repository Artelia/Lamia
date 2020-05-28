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


import os, pprint, sys
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
            self._initMainToolWidgetLamia()
                
        elif self.dbase.variante in ['Orange']:
            self._initMainToolWidgetOrange()
            
        #* common part
        self.formtoolwidgetconfdictmain['observation']['widgets'].update( {'ncbagreement': self.toolwidgetmain.comboBox_acceptation,
                                                                            'ncbtargetdate': self.toolwidgetmain.dateEdit_datecible,
                                                                            # 'ncb_observation': self.toolwidgetmain.textBrowser_ncbobs,

                                                                            'ncccheckstate': self.toolwidgetmain.comboBox_etatverif,
                                                                            # 'ncc_obs': self.toolwidgetmain.textBrowser_etatverif,
                                                                            # 'ncc_date': self.toolwidgetmain.dateEdit_etatverif,

                                                                            'ncdreservationremoval': self.toolwidgetmain.comboBox_leveres,
                                                                            # 'ncd_leveereservecom': self.toolwidgetmain.textBrowser_leveres,

                                                                            'ncecorrectiveaction': self.toolwidgetmain.comboBox_actioncorr,
                                                                            # 'nce_actioncorrcom': self.toolwidgetmain.textBrowser_actioncorr,

                                                                            # pva
                                                                            # 'pva_datetime': self.toolwidgetmain.dateTimeEdit_pva,
                                                                            # 'pva_commentaires': self.toolwidgetmain.textBrowser_pva,


                                                                            })
        self.formtoolwidgetconfdictmain['object']['widgets'].update({ 'comment': [self.toolwidgetmain.textBrowser_ncbobs,
                                                                                self.toolwidgetmain.textBrowser_etatverif,
                                                                                       self.toolwidgetmain.textBrowser_leveres,
                                                                                       self.toolwidgetmain.textBrowser_actioncorr,
                                                                                        self.toolwidgetmain.textBrowser_pva]
                                                                    })


        if 'observationcategory' in self.TABLEFILTERFIELD.keys():
            observationcategory = self.TABLEFILTERFIELD['observationcategory']
            for i in range(self.toolwidgetmain.stackedWidget_2.count()):
                # print(self.toolwidgetmain.stackedWidget_2.widget(i).objectName())
                if self.toolwidgetmain.stackedWidget_2.widget(i).objectName() == observationcategory:
                    #self.indexstackedpage = i
                    self.toolwidgetmain.stackedWidget_2.setCurrentIndex(i)
            
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

    def _initMainToolWidgetLamia(self):
        self.toolwidgetmain = UserUI()
        self.toolwidgetmain.stackedWidget_2.removeWidget(self.toolwidgetmain.stackedWidget_2.widget(0))
        self.ncawidget = NcaLamia(self.toolwidgetmain)
        self.toolwidgetmain.stackedWidget_2.insertWidget(0,self.ncawidget)
        self.toolwidgetmain.stackedWidget_2.widget(0).setObjectName('NCA')
        
        self.formtoolwidgetconfdictmain = {'observation' : {'linkfield' : 'id_observation',
                                                    'widgets' : {'datetimeobservation': self.toolwidgetmain.dateTimeEdit_datetimeobservation,
                                                        
                                                                'ncadescription': self.ncawidget.textBrowser_ncadescription,

                                                                'ncaquality':self.ncawidget.checkBox_ncathqualite  ,
                                                                'ncacivilworks':self.ncawidget.checkBox_ncathouvrage  ,
                                                                'ncasafety':self.ncawidget.checkBox_ncathsecurite  ,
                                                                'ncasystem':self.ncawidget.checkBox_ncathsystem  ,
                                                                'ncaenvironnemental':self.ncawidget.checkBox_ncathenvironnement  ,
                                                                'ncaregulatory':self.ncawidget.checkBox_ncathreglementaire  ,
                                                                # 'ncathcommentaire' : self.ncawidget.textBrowser_ncathcommentaire,
                                                                'gravity': self.ncawidget.comboBox_ncathcategorie,

                                                                'ncaprocessus': self.ncawidget.textBrowser_ncaprocessus,
                                                                'source': self.ncawidget.textBrowser_ncacause,
                                                            }},
                                'object' : {'linkfield' : 'object',
                                            'widgets' : {
                                                        'comment': self.ncawidget.textBrowser_ncathcommentaire,
                                            }}}

        self.tabWidget_page_formvisa = self.toolwidgetmain.tabWidget_formvisa.widget(1)

        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self
        self.lamiawidgets = []

        if 'observationcategory' in self.TABLEFILTERFIELD.keys():
            observationcategory = self.TABLEFILTERFIELD['observationcategory']
            #Signature
            if observationcategory in ['NCA', 'NCB', 'NCC', 'NCD']:
                signatureWidget = SignatureWidget(self, 'lid_actor_1', 'lid_resource_1', 'datetimesignature_1',
                                                        parentframe=self.toolwidgetmain.tabWidget_formvisa.widget(1))
                self.lamiawidgets.append(signatureWidget)
            else:
                self.toolwidgetmain.tabWidget_formvisa.removeTab(1)

            # Other
            if observationcategory == 'NCB':
                lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_actor_1',
                                                                parentframe = self.toolwidgetmain.frame_choisresp,
                                                                searchdbase='actor', searchfieldtoshow=['actorname','society'])
                self.lamiawidgets.append(lidchooser)
                # self.toolwidgetmain.tabWidget_formvisa.removeTab(1)
            # mise dispo
            elif observationcategory == 'PVA':
                #entreprise preneuse
                lidchooser = LidChooserWidget(parentwdg=self, 
                                                parentlidfield='lid_delivery_1',
                                                            parentframe = self.toolwidgetmain.frame_entpren_marche,
                                                            searchdbase='delivery', searchfieldtoshow=['name'])
                self.lamiawidgets.append(lidchooser)

                signatureWidgetPreneuse = SignatureWidget(self, 
                                                                'lid_actor_1', 
                                                                'lid_resource_1', 
                                                                'datetimesignature_1' ,
                                                                parentframe=self.toolwidgetmain.groupBox_entpren_sign)
                self.lamiawidgets.append(signatureWidgetPreneuse)

                #entreprise occupante
                lidchooser = LidChooserWidget(parentwdg=self, parentlidfield='lid_delivery_2',
                                                                parentframe = self.toolwidgetmain.frame_entocc_marche,
                                                                searchdbase='delivery', searchfieldtoshow=['name'])
                self.lamiawidgets.append(lidchooser)
                signatureWidgetOccupante = SignatureWidget(self, 'lid_actor_2', 'lid_resource_2', 'datetimesignature_2',
                                                                parentframe=self.toolwidgetmain.groupBox_entocc_sign)
                self.lamiawidgets.append(signatureWidgetOccupante)

                self.toolwidgetmain.tabWidget_formvisa.removeTab(1)

    def _initMainToolWidgetOrange(self):
        # userui
        self.toolwidgetmain = UserUI()
        self.toolwidgetmain.stackedWidget_2.removeWidget(self.toolwidgetmain.stackedWidget_2.widget(0))
        self.ncawidget = NcaOrange(self.toolwidgetmain)
        self.toolwidgetmain.stackedWidget_2.insertWidget(0,self.ncawidget)
        self.toolwidgetmain.stackedWidget_2.widget(0).setObjectName('NCA')

        self.formtoolwidgetconfdictmain = {'observation': {'linkfield': 'id_observation',
                                                        'widgets': {
                                                            'datetimeobservation': self.ncawidget.dateTimeEdit_datetimeobs,
                                                            'ncaweather': self.ncawidget.lineEdit_meteo,
                                                            # 'nca_mandataire': self.ncawidget.comboBox_mandataire,
                                                            'ncacontractorsonsite': self.ncawidget.lineEdit_etppres,

                                                            'ncaschedule': self.ncawidget.comboBox_planning,
                                                            'ncaschedulecomment': self.ncawidget.textBrowser_planningcom,

                                                            'ncaheadcountcontractor': self.ncawidget.spinBox_effectetp,
                                                            'ncaheadcountsubcontractor': self.ncawidget.spinBox_effectsstraitant,
                                                            'ncasitesupervisorpresence': self.ncawidget.checkBox_conduc,

                                                            'ncamachinesexcavator': self.ncawidget.checkBox_eng_pelle,
                                                            'ncamachinesloader': self.ncawidget.checkBox_eng_charg,
                                                            'ncamachinescompressor': self.ncawidget.checkBox_eng_compres,
                                                            'ncamachinestrencher': self.ncawidget.checkBox_eng_trancheuse,
                                                            'ncamachinesdumptruckmaterial': self.ncawidget.checkBox_eng_cam_mat,
                                                            'ncamachinesdumptruckexcavation': self.ncawidget.checkBox_eng_cam_deblais,
                                                            'ncamachinesvacuumtruck': self.ncawidget.checkBox_eng_cam_aspi,
                                                            'ncamachinessprayertruck': self.ncawidget.checkBox_eng_cam_repand,
                                                            'ncamachinesmixertruck': self.ncawidget.checkBox_eng_cam_malax,
                                                            'ncamachinescontainer': self.ncawidget.checkBox_eng_container,
                                                            'ncamachinesroller': self.ncawidget.checkBox_eng_compacteur,
                                                            'ncamachinesfinisher': self.ncawidget.checkBox_eng_finisseur,
                                                            'ncamachinesminiloader': self.ncawidget.checkBox_eng_minipelle,
                                                            'ncamachinesbuckettruck': self.ncawidget.checkBox_eng_nacelle,
                                                            'ncamachinesothers': self.ncawidget.checkBox_eng_autre,

                                                            'ncasafetystaff': self.ncawidget.comboBox_sec_personnel,
                                                            'ncasafetysiteprotected': self.ncawidget.comboBox_sec_protection,
                                                            'ncasafetyregulatorysheetshown': self.ncawidget.comboBox_sec_afficharrete,
                                                            'ncasafetyconstructionsigns': self.ncawidget.comboBox_sec_panneauxchant,
                                                            'ncasafetytraficsafety': self.ncawidget.comboBox_sec_circul,
                                                            'ncasafetylighting': self.ncawidget.comboBox_sec_eclairage,
                                                            'ncasafetywastedisposal': self.ncawidget.comboBox_sec_stockagedechet,
                                                            'ncasafetycleanness': self.ncawidget.comboBox_sec_proprete,
                                                            'ncasafetytrenchprotected': self.ncawidget.comboBox_sec_protectiontranchee,
                                                            'ncasafetytrenchshoring': self.ncawidget.comboBox_sec_blindage,
                                                            'ncasafetymarkingsstaking': self.ncawidget.comboBox_sec_reunionmarquage,
                                                            'ncasafetymarkingsmaintenance': self.ncawidget.comboBox_sec_entretienmarquage,
                                                            'ncasafetynetworkgatevalvesaccess': self.ncawidget.comboBox_sec_accesscoupure,
                                                            'ncasafetyworkataheight': self.ncawidget.comboBox_sec_travailhauteur,
                                                            'ncaregulatorygrievance': self.ncawidget.comboBox_sec_plaintes,
                                                            'ncaregulatorygrievancecomment': self.ncawidget.lineEdit_sec_plaintes_com,

                                                            }},
                                        'object': {'linkfield': 'id_object',
                                                'widgets': {}}}


        self.ncawidget.toolButton_effect_etp.clicked.connect(
            lambda: self.showNumPad(self.ncawidget.spinBox_effectetp))
        self.ncawidget.toolButton_effect_sstraitant.clicked.connect(
            lambda: self.showNumPad(self.ncawidget.spinBox_effectsstraitant))

        self.tabWidget_page_formvisa = self.toolwidgetmain.tabWidget_formvisa.widget(1)

        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self
        self.lamiawidgets = []

        if 'observationcategory' in self.TABLEFILTERFIELD.keys():
            observationcategory = self.TABLEFILTERFIELD['observationcategory']
            #NCA
            if observationcategory == 'NCA':
                self.tabWidget_multivisa = QTabWidget()
                self.tabWidget_page_formvisa.layout().addWidget(self.tabWidget_multivisa)
                self.tabWidget_multivisa.addTab(QWidget(), 'MOE')
                self.tabWidget_multivisa.addTab(QWidget(), 'Entreprise')


                # visa nca MOE
                self.signatureWidgetMOE = SignatureWidget(self, 'lid_actor_1', 'lid_resource_1', 'datetimesignature_1',
                                                        parentframe=self.tabWidget_multivisa.widget(0) )
                self.lamiawidgets.append(self.signatureWidgetMOE)

                # visa nca ETP
                self.signatureWidgetETP = SignatureWidget(self, 'lid_actor_2', 'lid_resource_2', 'datetimesignature_2',
                                                            parentframe=self.tabWidget_multivisa.widget(1)  )
                self.lamiawidgets.append(self.signatureWidgetETP)

                # sous fiche
                self.sousficheWidget = BaseConstructionsiteSubObservationTool(**self.instancekwargs)
                self.sousficheWidget.tooltreewidgetSUBCAT = 'Fiches\ndétaillées'
                self.dbasechildwdgfield.insert(0,self.sousficheWidget)


    def changeGroupe(self, comboindex):
        parentcombotext = self.parentWidget.toolwidgetmain.comboBox_groupedes.currentText()
        if parentcombotext == 'Non-conformité':
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
        elif parentcombotext == 'Procès-verbal':
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(5)


    def postSelectFeature(self):

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
        #update tab symbol
        obstype = self.dbase.getValuesFromPk(self.DBASETABLENAME,
                                              'observationcategory',
                                               featurepk )
        for lamiawidget in self.lamiawidgets:   #need to save before calling updateListSymbols
            lamiawidget.postSaveFeature(featurepk)
        if (obstype[0:2] == 'NC'):
            self.parentWidget.updateListSymbols()



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





