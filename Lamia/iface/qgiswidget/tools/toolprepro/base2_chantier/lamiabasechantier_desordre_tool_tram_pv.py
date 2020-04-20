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

    tooltreewidgetSUBCAT = 'Proces verbal'

    def __init__(self, **kwargs):
        super(BaseChantierDesordreTool, self).__init__(**kwargs)


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
                                                            'widgets': {
                                                                        #'groupedesordre': self.toolwidgetmain.comboBox_groupedes,
                                                                        'detecteur': self.toolwidgetmain.comboBox_detecteur,
                                                                        'detecteur_com': self.toolwidgetmain.lineEdit_detecteur,

                                                                        }},
                                                'Objet': {'linkfield': 'id_objet',
                                                        'widgets': {}}}

            self.TABLEFILTERFIELD = {'groupedesordre' : 'PVE'}

            #self.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)
            #self.toolwidgetmain.comboBox_groupedes.setCurrentIndex(1)
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)

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
            
            #pv mise a dispo
            propertieswdgOBSERVATIONpv = BaseObservationTool(**self.instancekwargs)
            #propertieswdgOBSERVATIONpv.NAME = None
            #propertieswdgOBSERVATIONpv.setOBSTYPE('PVA', True)
            propertieswdgOBSERVATIONpv.tooltreewidgetSUBCAT = 'Mise a dispo'
            propertieswdgOBSERVATIONpv.TABLEFILTERFIELD = {'typeobservation': 'PVA' }
            # self.obsdict[wdgname].OBSTYPE = itemtype
            self.toolwidgetmain.stackedWidget.widget(1).layout().addWidget(propertieswdgOBSERVATIONpv)
            self.dbasechildwdgfield.append(propertieswdgOBSERVATIONpv)



        else:
            self.unloadWidgetinToolTree()
            self.loadWidgetinToolTree = lambda: None
            #self.toolTreeWidgetCurrentItemChanged = lambda: None


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
        """
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
        """






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
