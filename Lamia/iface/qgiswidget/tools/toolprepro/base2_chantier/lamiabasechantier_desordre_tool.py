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

import os, inspect, datetime
from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget)

from ..base2.lamiabase_desordre_tool import BaseDesordreTool
from .lamiabasechantier_observation_tool import BaseChantierObservationTool as BaseObservationTool
from .lamiabasechantier_croquis_tool import BaseChantierCroquisTool as BaseCroquisTool
from .lamiabasechantier_photo_tool import BaseChantierPhotoTool as BasePhotoTool
from .lamiabasechantier_rapport_tool import BaseChantierRapportTool as BaseRapportTool
#from .lamiabasechantier_lidchooser import LidChooserWidget
from ..subwidgets.subwidget_lidchooser import LidChooserWidget



class BaseChantierDesordreTool(BaseDesordreTool):


    def __init__(self, **kwargs):
        super(BaseChantierDesordreTool, self).__init__(**kwargs)
        # nclist : [...[displayname, typeobservation,signing  ]...]
        self.nclist = [
                       # ['Généralités',None,False],
                        ['Description', 'NCA',True],
                       ['Proposition\navis', 'NCB',True],
                       ['Vérification', 'NCC',True],
                       ['Levée', 'NCD',True],
                       ['Recherche\ndes causes', 'NCE',False]
                    ]
        self.iconinterv1 = QtGui.QIcon(os.path.join(os.path.dirname(__file__),'interv1.png' ))
        self.iconinterv2 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'interv1.png'))
        self.iconinterv3 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'interv3.png'))

    """
    def initTool(self):
        super(BaseChantierDesordreTool, self).initTool()
        #self.NAME = 'Campagne de reconnaissance'
        #self.qtreewidgetfields = ['libelle']
        #self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
        self.NAME = 'Fiches'
        self.visualmode = [0,1]

        self.nclist = [['Généralités',None,False],
                        ['Description', 'NCA',True],
                       ['Proposition/avis', 'NCB',True],
                       ['Vérification', 'NCC',True],
                       ['Levée', 'NCD',True],
                       ['Recherche des causes', 'NCE',False]
                    ]





    """

    def initMainToolWidget(self):



        if self.dbase.variante in [None, 'Lamia']:

            self.toolwidgetmain = UserUI()

            self.formtoolwidgetconfdictmain = {'Desordre': {'linkfield': 'id_desordre',
                                                            'widgets': {'groupedesordre': self.toolwidgetmain.comboBox_groupedes,
                                                                        'detecteur': self.toolwidgetmain.comboBox_detecteur,
                                                                        'detecteur_com': self.toolwidgetmain.lineEdit_detecteur,

                                                                        }},
                                                'Objet': {'linkfield': 'id_objet',
                                                        'widgets': {}}}

            self.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)

            # non conformité
            #for elem in self.nclist:
            #    itemname = elem[0]
            #    self.toolwidgetmain.listWidget_nonconf.addItem(itemname)
            #self.toolwidgetmain.listWidget_nonconf.currentItemChanged.connect(self.itemChangedNonConformite)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            self.lamiawidgets = []
            
            ## nclist : [...[displayname, typeobservation,signing  ]...]
            #self.nclist = [['Généralités',None,False],

            for i, (displayname, typeobservation,signing) in enumerate(self.nclist):
                #print(i, displayname, typeobservation,signing)
                varname = 'self.propertieswdgOBSERVATION{}'.format(typeobservation)
                
                if False:
                    globals()[varname] =  BaseObservationTool(**self.instancekwargs)
                    globals()[varname].TABLEFILTERFIELD = {'typeobservation': typeobservation }
                    globals()[varname].tooltreewidgetSUBCAT = displayname
                    globals()[varname].initMainToolWidget()
                    #globals()[varname].toolwidgetmain.stackedWidget_2.setEnabled(True)
                    #globals()[varname].toolwidgetmain.stackedWidget_2.setCurrentIndex(i)
                    #globals()[varname].setOBSTYPE(typeobservation,signing)
                    self.dbasechildwdgfield.append(globals()[varname])
                if True:
                    temppropertieswdgOBSERVATION = BaseObservationTool(**self.instancekwargs)
                    temppropertieswdgOBSERVATION.TABLEFILTERFIELD = {'typeobservation': typeobservation }
                    temppropertieswdgOBSERVATION.tooltreewidgetSUBCAT = displayname
                    #temppropertieswdgOBSERVATION.initMainToolWidget()
                    #temppropertieswdgOBSERVATION.toolwidgetmain.stackedWidget_2.setCurrentIndex(i)
                    if False:
                        if signing:
                            pass
                            #temppropertieswdgOBSERVATION.toolwidgetmain.tabWidget_formvisa.insertTab(1, temppropertieswdgOBSERVATION.tabWidget_page_formvisa, 'Visa')
                        else:
                            temppropertieswdgOBSERVATION.toolwidgetmain.tabWidget_formvisa.removeTab(1)
                    #temppropertieswdgOBSERVATION
                    exec('self.propertieswdgOBSERVATION{} = temppropertieswdgOBSERVATION'.format(typeobservation))
                    exec('self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION{} )'.format(typeobservation))
                #self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION )
            #self.propertieswdgOBSERVATION = BaseObservationTool(**self.instancekwargs)
            ##self.propertieswdgOBSERVATION.NAME = None
            ##self.toolwidgetmain.stackedWidget_nonconf.widget(1).layout().addWidget(self.propertieswdgOBSERVATION )
            #self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION )

            propertieswdgChooseMarche = LidChooserWidget(parentwdg=self, parentlidfield='lid_marche',
                                                        parentframe = self.toolwidgetmain.frame_numarche,
                                                        searchdbase='Marche', searchfieldtoshow=['libelle'])
            self.lamiawidgets.append(propertieswdgChooseMarche)

            #pv mise a dispo
            propertieswdgOBSERVATIONpv = BaseObservationTool(**self.instancekwargs)
            #propertieswdgOBSERVATIONpv.NAME = None
            #propertieswdgOBSERVATIONpv.setOBSTYPE('PVA', True)
            propertieswdgOBSERVATIONpv.TABLEFILTERFIELD = {'typeobservation': 'PVA' }
            # self.obsdict[wdgname].OBSTYPE = itemtype
            self.toolwidgetmain.stackedWidget.widget(1).layout().addWidget(propertieswdgOBSERVATIONpv)
            self.dbasechildwdgfield.append(propertieswdgOBSERVATIONpv)



        elif self.dbase.variante in ['Orange']:
            self.toolwidgetmain = UserUI_Orange()

            self.formtoolwidgetconfdictmain = {'Desordre': {'linkfield': 'id_desordre',
                                                            'widgets': {'groupedesordre': self.toolwidgetmain.comboBox_groupedes,

                                                                        'commune': self.toolwidgetmain.lineEdit_commune,
                                                                        'rue': self.toolwidgetmain.lineEdit_rue,
                                                                        'za_sro': self.toolwidgetmain.comboBox_zasro,
                                                                        'datedebuttravaux': self.toolwidgetmain.dateEdit_debuttrav,
                                                                        'datefincontractuelle': self.toolwidgetmain.dateEdit_fintrav,

                                                                        }},
                                                'Objet': {'linkfield': 'id_objet',
                                                        'widgets': {}}}

            self.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)

            # non conformité
            #for elem in self.nclist:
            #    itemname = elem[0]
            #    self.toolwidgetmain.listWidget_nonconf.addItem(itemname)
            #self.toolwidgetmain.listWidget_nonconf.currentItemChanged.connect(self.itemChangedNonConformite)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            self.lamiawidgets = []

            """
            self.propertieswdgOBSERVATION = BaseObservationTool(**self.instancekwargs)
            #self.propertieswdgOBSERVATION.NAME = None
            #self.toolwidgetmain.stackedWidget_nonconf.widget(1).layout().addWidget(self.propertieswdgOBSERVATION)
            self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)
            """
            for i, (displayname, typeobservation,signing) in enumerate(self.nclist):
                temppropertieswdgOBSERVATION = BaseObservationTool(**self.instancekwargs)
                temppropertieswdgOBSERVATION.TABLEFILTERFIELD = {'typeobservation': typeobservation }
                temppropertieswdgOBSERVATION.tooltreewidgetSUBCAT = displayname
                #temppropertieswdgOBSERVATION.initMainToolWidget()
                exec('self.propertieswdgOBSERVATION{} = temppropertieswdgOBSERVATION'.format(typeobservation))
                exec('self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION{} )'.format(typeobservation))

            #propertieswdgChooseMarche = LidChooserWidget(parentwdg=self, parentlidfield='lid_marche',
            #                                            parentframe = self.toolwidgetmain.frame_numarche,
            #                                            searchdbase='Marche', searchfieldtoshow=['libelle'])
            #self.lamiawidgets.append(propertieswdgChooseMarche)




    def magicFunction(self):
        self.featureSelected()
        self.addGPSPoint()
        self.saveFeature()
        for wdgobservation in self.dbasechildwdgfield:
            if hasattr(wdgobservation, 'OBSTYPE') and wdgobservation.OBSTYPE == 'NCA':
                wdgobservation.featureSelected()
                wdgobservation.saveFeature()


    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super(BaseChantierDesordreTool, self).postSelectFeature()

        self.updateListSymbols()

        if self.currentFeaturePK is None:
            #self.toolwidgetmain.listWidget_nonconf.setCurrentRow(0)

            if self.dbase.variante in ['Orange']:
                datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d"))
                #self.initFeatureProperties(feat, self.DBASETABLENAME, 'datedebuttravaux', datecreation)
                #self.initFeatureProperties(feat, self.DBASETABLENAME, 'datefincontractuelle', datecreation)
                #datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                ##self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)
                self.formutils.applyResultDict({'datedebuttravaux' : datecreation},checkifinforgottenfield=False)
                self.formutils.applyResultDict({'datefincontractuelle' : datecreation},checkifinforgottenfield=False)




    def itemChangedNonConformite(self, itemcurrent, itemprevious):
        currentrow = self.toolwidgetmain.listWidget_nonconf.row(itemcurrent)
        if currentrow == 0:
            self.toolwidgetmain.stackedWidget_nonconf.setCurrentIndex(0)
        else:
            self.toolwidgetmain.stackedWidget_nonconf.setCurrentIndex(1)
            obstype = self.nclist[currentrow][1]
            signaturebool = self.nclist[currentrow][2]
            self.propertieswdgOBSERVATION.setOBSTYPE(obstype, signaturebool)

            self.currentFeatureChanged.emit()
            self.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_2.setCurrentIndex(currentrow -1)



    def updateListSymbols(self):
        #for i, elem in enumerate(self.nclist):
        for i, (itemname,typeobservation, fieldsign ) in enumerate(self.nclist):
            if fieldsign and self.currentFeaturePK is not None :
                exec('obswdg = self.propertieswdgOBSERVATION{} '.format(typeobservation),locals(),globals() )
                iddes = self.dbase.getValuesFromPk('Desordre', 'id_desordre', self.currentFeaturePK)
                signatureswdgs = [wdg for wdg in obswdg.lamiawidgets if wdg.__class__.__name__ == 'SignatureWidget']
                intervid=[]
                for sigwdg in signatureswdgs:
                    intervid.append(sigwdg.intervenantid)
                if len(intervid)>0:
                    obsname = obswdg.tooltreewidgetSUBCAT
                    goodtab = self.tabWidget.findChild(QWidget, obsname)
                    goodtabindex = self.tabWidget.indexOf(goodtab)
                    self.tabWidget.setTabIcon(goodtabindex,self.iconinterv1)

                    sql = "SELECT {} FROM Observation WHERE typeobservation = '{}' "\
                        " AND lid_desordre = {} ".format(', '.join(intervid),
                                                            typeobservation,
                                                            iddes)
                    res = self.dbase.query(sql)
                    if res :
                        test = [re for re in res[0] if self.dbase.utils.isAttributeNull(re)  ]
                        if len(test) == 0 :
                            self.tabWidget.setTabIcon(goodtabindex,self.iconinterv3)



            if False:
                if fieldsign and self.currentFeaturePK is not None :
                    iddes = self.dbase.getValuesFromPk('Desordre', 'id_desordre', self.currentFeaturePK)
                    sql = "SELECT lid_intervenant_1, lid_intervenant_2, lid_intervenant_3 FROM Observation WHERE typeobservation = '" + str(itemtype) + "'"
                    sql += " AND lid_desordre = " + str(iddes)
                    res = self.dbase.query(sql)
                    # print('**', sql, res)
                    if res is not None and len(res)>0 :
                        if not self.dbase.utils.isAttributeNull(res[0][0]) and not self.dbase.utils.isAttributeNull(res[0][2]):
                            self.toolwidgetmain.listWidget_nonconf.item(i).setIcon(self.iconinterv3)

                        elif not self.dbase.utils.isAttributeNull(res[0][0]):
                            self.toolwidgetmain.listWidget_nonconf.item(i).setIcon(self.iconinterv1)

                        else:
                            self.toolwidgetmain.listWidget_nonconf.item(i).setIcon(QtGui.QIcon())

                    else:
                        self.toolwidgetmain.listWidget_nonconf.item(i).setIcon(QtGui.QIcon())
                else:
                    self.toolwidgetmain.listWidget_nonconf.item(i).setIcon(QtGui.QIcon())




    def printWidget(self):

        #create finelname
        pdfdirectory = os.path.join(self.dbase.dbaseressourcesdirectory, 'Print')
        if not os.path.isdir(pdfdirectory):
            os.mkdir(pdfdirectory)

        currentid = self.dbase.getValuesFromPk('Desordre', 'id_desordre',self.currentFeaturePK  )

        date = str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

        filename = str(currentid) + '_desordre_' + date + '.pdf'

        pdffielname = os.path.join(pdfdirectory,filename )


        #choose phaseA report or phase C report
        sql = "SELECT typeobservation FROM  Observation_now WHERE Observation_now.lid_desordre = " + str(currentid)
        sql = self.dbase.updateQueryTableNow(sql)
        res = self.dbase.query(sql)

        if res is not None and len(res) > 0 and not self.dbase.utils.isAttributeNull(res[0][0]):
            if res[0][0] == 'PVA':
                reportype = 'procesverbalmiseadisposition'

            elif res[0][0][0:2] == 'NC':
                sql = "SELECT id_observation FROM Observation_now WHERE Observation_now.typeobservation = 'NCB'"
                sql += " AND Observation_now.lid_desordre = " + str(currentid)
                sql = self.dbase.updateQueryTableNow(sql)
                res = self.dbase.query(sql)
                if self.dbase.variante in [None, 'Lamia']:
                    if res is not None and len(res) > 0 and not self.dbase.utils.isAttributeNull(res[0][0]):
                        reportype = 'TRAMnonconformite'
                    else:
                        reportype = 'TRAMnonconformitephaseA'
                elif self.dbase.variante in ['Orange']:
                    print('*********ORANGEnonconformitephaseA')
                    reportype = 'ORANGEnonconformitephaseA'

        else:
            return

        #load rapport tool
        if not self.windowdialog.desktopuiloaded:
            self.windowdialog.loadUiDesktop()
        wdg = None
        for i, tool in enumerate(self.windowdialog.tools):
            # print(tool.__class__.__name__)
            if 'RapportTool' in tool.__class__.__name__:
                wdg = self.windowdialog.tools[i]
                break

        wdg.createconfData()
        impressionpdfworker = inspect.getmodule(wdg).printPDFBaseWorker(dbase=self.dbase,
                                                                         windowdialog=self.windowdialog,
                                                                         parentprintPDFworker=None,
                                                                         confData=wdg.confData,
                                                                         pdffile=pdffielname,
                                                                         reporttype=reportype,
                                                                          templatedir=wdg.confdatamain,
                                                                          #idlist={0: [currentid]},
                                                                         idlist={0: [self.currentFeaturePK]},
                                                                        )

        impressionpdfworker.work()



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantier_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUI_Orange(QWidget):
    def __init__(self, parent=None):
        super(UserUI_Orange, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantier_desordre_tool_orange_ui.ui')
        uic.loadUi(uipath, self)
