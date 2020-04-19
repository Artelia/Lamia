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
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
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
from .lamiabasechantiertram_lidchooser import LidChooser

import os
import datetime


class BaseChantierTramObservationTool(BaseObservationTool):

    OBSTYPE = None

    def __init__(self, **kwargs):
        super(BaseChantierTramObservationTool, self).__init__(**kwargs)
        self.indexstackedpage = None




    def initMainToolWidget(self):
        # ****************************************************************************************
        # userui Desktop
        if self.toolwidgetmain is None:
            # ****************************************************************************************
            # userui
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

            if self.parentWidget.DBASETABLENAME == 'Desordre':
                self.parentWidget.userwdgfield.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)

            self.frame_editing.setVisible(False)

            self.dbasechildwdgfield = []

            #NCA
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgPHOTOGRAPHIE.NAME = None
            self.toolwidgetmain.tabWidget.widget(4).layout().addWidget(self.propertieswdgPHOTOGRAPHIE)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgCROQUIS.NAME = None
            self.toolwidgetmain.tabWidget.widget(5).layout().addWidget(self.propertieswdgCROQUIS)
            # self.toolwidgetmain.toolox.widget(1).layout().addWidget(self.propertieswdgOBSERVATION2)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            # def __init__(self, parentwdg=None, intervenantid=None, signatureid=None):
            self.signatureWidget = SignatureWidget(self, 'lid_intervenant_1', 'lid_ressource_1', 'datetimesignature_1' )
            #self.toolwidgetmain.tabWidget.widget(6).layout().addWidget(self.signatureWidget)
            self.toolwidgetmain.tabWidget_formvisa.widget(1).layout().addWidget(self.signatureWidget)

            # NCB

            self.propertieswdgRapport = BaseRapportTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgRapport.NAME = None
            self.propertieswdgRapport.CHECKGEOM = False
            self.propertieswdgRapport.frame_editing.setVisible(False)
            self.toolwidgetmain.groupBox_NCB_PJ.layout().addWidget(self.propertieswdgRapport)
            self.dbasechildwdgfield.append(self.propertieswdgRapport)

            #self.signatureWidget2 = SignatureWidget(self, 'lid_intervenant_4', 'lid_ressource_4', 'datetimesignature_4' )
            #self.toolwidgetmain.tabWidget_avis.widget(1).layout().addWidget(self.signatureWidget2)

            self.propertieswdgChooseResp = LidChooser(parentwdg=self, parentlidfield='lid_intervenant_4',
                                                        parentlabel=self.toolwidgetmain.label_ncbresponsable,
                                                        searchdbase='Intervenant', searchfieldtoshow=['nom','societe'])
            self.toolwidgetmain.frame_choisresp.layout().addWidget(self.propertieswdgChooseResp)

            # ncc
            self.propertieswdgPHOTOGRAPHIE2 = BasePhotoTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgPHOTOGRAPHIE2.NAME = None
            self.toolwidgetmain.tabWidget_verif.widget(1).layout().addWidget(self.propertieswdgPHOTOGRAPHIE2)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE2)

            #self.signatureWidget3 = SignatureWidget(self, 'lid_intervenant_5', 'lid_ressource_5', 'datetimesignature_5' )
            #self.toolwidgetmain.tabWidget_verif.widget(2).layout().addWidget(self.signatureWidget3)

            # mise dispo
            if True:
                self.propertieswdgRapport2 = BaseRapportTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgRapport2.NAME = None
                self.propertieswdgRapport2.CHECKGEOM = False
                self.propertieswdgRapport2.frame_editing.setVisible(False)
                self.toolwidgetmain.tabWidget_pvmisedispo.widget(4).layout().addWidget(self.propertieswdgRapport2)
                self.dbasechildwdgfield.append(self.propertieswdgRapport2)

                self.propertieswdgPHOTOGRAPHIE3 = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgPHOTOGRAPHIE3.NAME = None
                self.toolwidgetmain.tabWidget_pvmisedispo.widget(3).layout().addWidget(self.propertieswdgPHOTOGRAPHIE3)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE3)

                #entreprise preneuse
                self.propertieswdgChoosePreneuseMarche = LidChooser(parentwdg=self, parentlidfield='lid_entpren_marche',
                                                            parentlabel=self.toolwidgetmain.label_entpren_marche,
                                                            searchdbase='Marche', searchfieldtoshow=['libelle'])
                self.toolwidgetmain.groupBox_entpren_marche.layout().addWidget(self.propertieswdgChoosePreneuseMarche)


                self.signatureWidgetPreneuse = SignatureWidget(self, 'lid_entpren_intervenant',
                                                               'lid_ressource_entpren',
                                                               'lid_entpren_datetimesignature' )
                self.toolwidgetmain.groupBox_entpren_sign.layout().addWidget(self.signatureWidgetPreneuse)

                #entreprise occupante
                self.propertieswdgChooseOccupanteMarche = LidChooser(parentwdg=self, parentlidfield='lid_entocc_marche',
                                                            parentlabel=self.toolwidgetmain.label_entocc_marche,
                                                            searchdbase='Marche', searchfieldtoshow=['libelle'])
                self.toolwidgetmain.groupBox_entocc_marche.layout().addWidget(self.propertieswdgChooseOccupanteMarche)


                self.signatureWidgetOccupante = SignatureWidget(self, 'lid_entocc_intervenant',
                                                               'lid_ressource_entocc',
                                                               'lid_entocc_datetimesignature' )
                self.toolwidgetmain.groupBox_entocc_sign.layout().addWidget(self.signatureWidgetOccupante)








    def changeGroupe(self, comboindex):
        parentcombotext = self.parentWidget.userwdgfield.comboBox_groupedes.currentText()
        if parentcombotext == 'Non-conformité':
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
        elif parentcombotext == 'Procès-verbal':
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(5)




    def setOBSTYPE(self, obstype, boolsignature):
        if obstype is None:
            self.toolwidgetmain.tabWidget_formvisa.removeTab(1)
            return

        self.OBSTYPE = obstype
        if False:
            obstypeindex = [elem[1] for elem in nclist].index(obstype)
            boolsignature = nclist[obstypeindex][2]
        if boolsignature  == False:
            self.toolwidgetmain.tabWidget_formvisa.removeTab(1)


    def postSaveFeature(self, boolnewfeature):

        if self.currentFeaturePK is not None:
            sql = "UPDATE Observation SET typeobservation = '" + str(self.OBSTYPE) + "'"
            sql += " WHERE pk_observation = " + str(self.currentFeaturePK)
            self.dbase.query(sql)

        self.signatureWidget.postSaveFeature(boolnewfeature)

        if self.OBSTYPE[0:2] == 'PV':
            self.signatureWidgetOccupante.postSaveFeature(boolnewfeature)
            self.signatureWidgetPreneuse.postSaveFeature(boolnewfeature)


        if (self.OBSTYPE[0:2] == 'NC'):
            self.parentWidget.updateListSymbols()


    def postloadIds(self,sqlin):
        sqlout = sqlin + " AND typeobservation = '" + str(self.OBSTYPE) + "'"
        return sqlout


    def postInitFeatureProperties(self, feat):
        super(BaseChantierTramObservationTool, self).postInitFeatureProperties(feat)

        if True:
            self.signatureWidget.postInitFeatureProperties(feat)

            if (self.OBSTYPE[0:2] == 'NC'):
                self.propertieswdgChooseResp.postInitFeatureProperties(feat)

            if self.OBSTYPE[0:2] == 'PV':
                self.signatureWidgetOccupante.postInitFeatureProperties(feat)
                self.signatureWidgetPreneuse.postInitFeatureProperties(feat)


                self.propertieswdgChooseOccupanteMarche.postInitFeatureProperties(feat)
                self.propertieswdgChoosePreneuseMarche.postInitFeatureProperties(feat)

        if self.currentFeaturePK is None:

            if self.OBSTYPE == 'NCB':
                valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d"))
                self.toolwidgetmain.dateEdit_datecible.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd'))
            elif self.OBSTYPE == 'NCC':
                valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d"))
                self.toolwidgetmain.dateEdit_etatverif.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd'))
            elif self.OBSTYPE == 'PVA':
                valuetoset = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.toolwidgetmain.dateTimeEdit_pva.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd hh:mm:ss'))


        #self.signatureWidget2.postInitFeatureProperties(feat)
        #self.signatureWidget3.postInitFeatureProperties(feat)


        if self.OBSTYPE is not None:
            if self.indexstackedpage is None:
                for i in range(self.toolwidgetmain.stackedWidget_2.count()):
                    # print(self.toolwidgetmain.stackedWidget_2.widget(i).objectName())
                    if self.toolwidgetmain.stackedWidget_2.widget(i).objectName() == self.OBSTYPE:
                        self.indexstackedpage = i

            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(self.indexstackedpage)





    """
    def postSaveFeature(self, boolnewfeature):
        #if self.currentFeaturePK is None and self.OBSTYPE in ['NCA']:   #new objet
            # def getValuesFromPk(self, dbasename, fields, pk):
            lastid = self.dbase.getLastId('Ressource') + 1
            
            sql = 'UPDATE Observation SET lid_ressource = ' + str(lastid)
            sql += ' WHERE pk_observation = ' + str(self.currentFeaturePK)
            
            
            #create signature and intervenant
            self.propertieswdgCROQUIS2.featureSelect_1 = ' + 

            self.propertieswdgCROQUIS2.saveFeature(ed()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Desordre':
                self.parentWidget.updateDateCampagne()
    """



"""
    def initTool(self):
        super(BaseParkingObservationTool, self).initTool()
        #self.NAME = 'Campagne de reconnaissance'
        #self.qtreewidgetfields = ['libelle']
        #self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
        self.NAME = 'Observation immat'
        self.visualmode = [0,1]


    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Observation'
        self.dbasetablename = 'Observation'
        #self.visualmode = [1, 2]
        self.visualmode = []
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Desordre' : {'tabletc' : None,
                                           'idsource' : 'lk_desordre',
                                       'idtcsource' : None,
                                           'iddest' : 'id_desordre',
                                       'idtcdest' : None,
                                           'desttable' : ['Desordre']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lk_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_observation_tool_icon.png')

        # ****************************************************************************************
        #properties ui
        pass
    



    def initMainToolWidget(self):
        # ****************************************************************************************
        # userui Desktop
        if self.toolwidgetmain is None:
            # ****************************************************************************************
            # userui
            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {'Observation' : {'linkfield' : 'id_observation',
                                             'widgets' : {'immatriculation' : self.toolwidgetmain.spinBox_immat,
                                                          'illicite' : self.toolwidgetmain.checkBox_illicite,
                                                         'datetimeobservation' : self.toolwidgetmain.dateTimeEdit,
                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}

            self.toolwidgetmain.toolButton_immat.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_immat))


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield=[]
            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)



    def postInitFeatureProperties(self, feat):

        if self.currentFeature is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, self.dbasetablename, 'datetimeobservation', datecreation)






    def showNumPad(self, finalwdg):
        # print('ok', finalwdg)

        self.windowdialog.numpaddialog.exec_()
        number = self.windowdialog.numpaddialog.dialogIsFinished()
        # print(number)
        if number:
            finalwdg.setValue(number)
            self.saveFeature()




"""

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantiertram_observation_tool_ui.ui')
        uic.loadUi(uipath, self)







