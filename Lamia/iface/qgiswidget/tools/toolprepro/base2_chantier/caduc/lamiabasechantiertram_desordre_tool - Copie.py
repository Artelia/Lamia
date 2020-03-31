# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ..base2.lamiabase_desordre_tool import BaseDesordreTool
from .lamiabasechantiertram_observation_tool import BaseChantierTramObservationTool as BaseObservationTool
from .lamiabasechantiertram_croquis_tool import BaseChantierTramCroquisTool as BaseCroquisTool
from .lamiabasechantiertram_lidchooser import LidChooser
import os, inspect, datetime


class BaseChantierTramDesordreTool(BaseDesordreTool):
    LOADFIRST = True
    dbasetablename = 'Desordre'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseChantierTramDesordreTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget,
                                                              parent=parent)


    def initTool(self):
        super(BaseChantierTramDesordreTool, self).initTool()
        #self.NAME = 'Campagne de reconnaissance'
        #self.qtreewidgetfields = ['libelle']
        #self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
        #self.NAME = 'Observation immat'
        self.visualmode = [0,1]

        self.nclist = [['Généralités',None,False],
                        ['Description', 'NCA',True],
                       ['Proposition/avis', 'NCB',True],
                       ['Vérification', 'NCC',True],
                       ['Levée', 'NCD',True],
                       ['Recherche des causes', 'NCE',False]
                    ]



        self.iconinterv1 = QtGui.QIcon(os.path.join(os.path.dirname(__file__),'interv1.png' ))
        self.iconinterv2 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'interv1.png'))
        self.iconinterv3 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'interv3.png'))

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()

            self.linkuserwdgfield = {'Desordre': {'linkfield': 'id_desordre',
                                                  'widgets': {'groupedesordre': self.userwdgfield.comboBox_groupedes,
                                                              'detecteur': self.userwdgfield.comboBox_detecteur,
                                                              'detecteur_com': self.userwdgfield.lineEdit_detecteur,

                                                              }},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {}}}

            self.userwdgfield.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)

            # non conformité
            for elem in self.nclist:
                itemname = elem[0]
                self.userwdgfield.listWidget_nonconf.addItem(itemname)
            self.userwdgfield.listWidget_nonconf.currentItemChanged.connect(self.itemChangedNonConformite)
            

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            self.obsdict = {}
            for i, elem in enumerate(self.nclist):
                itemname = elem[0]
                itemtype = elem[1]
                itemboolsignature = elem[2]
                wdgname = 'self.propertieswdgOBSERVATION' + str(i)
                self.obsdict[wdgname] = None

                if itemtype is not None:
                    self.obsdict[wdgname] = BaseObservationTool(dbase=self.dbase, parentwidget=self)
                    self.obsdict[wdgname].NAME = None
                    self.obsdict[wdgname].setOBSTYPE(itemtype, itemboolsignature)
                    #self.obsdict[wdgname].OBSTYPE = itemtype
                    self.userwdgfield.stackedWidget_nonconf.widget(i).layout().addWidget(self.obsdict[wdgname])
                    self.dbasechildwdgfield.append(self.obsdict[wdgname])


            self.propertieswdgChooseMarche = LidChooser(parentwdg=self, parentlidfield='lid_marche',
                                                        parentlabel=self.userwdgfield.label_marche,
                                                        searchdbase='Marche', searchfieldtoshow=['libelle'])
            self.userwdgfield.frame_numarche.layout().addWidget(self.propertieswdgChooseMarche)

            #pv mise a dispo
            if True:
                propertieswdgOBSERVATIONpv = BaseObservationTool(dbase=self.dbase, parentwidget=self)
                propertieswdgOBSERVATIONpv.NAME = None
                propertieswdgOBSERVATIONpv.setOBSTYPE('PVA', True)
                # self.obsdict[wdgname].OBSTYPE = itemtype
                self.userwdgfield.stackedWidget.widget(1).layout().addWidget(propertieswdgOBSERVATIONpv)
                self.dbasechildwdgfield.append(propertieswdgOBSERVATIONpv)



    def magicFunction(self):
        self.featureSelected()
        self.addGPSPoint()
        self.saveFeature()
        for wdgobservation in self.dbasechildwdgfield:
            if hasattr(wdgobservation, 'OBSTYPE') and wdgobservation.OBSTYPE == 'NCA':
                wdgobservation.featureSelected()
                wdgobservation.saveFeature()


    def postInitFeatureProperties(self,feat):
        super(BaseChantierTramDesordreTool, self).postInitFeatureProperties(feat)
        self.propertieswdgChooseMarche.postInitFeatureProperties(feat)
        self.updateListSymbols()

        if self.currentFeaturePK is None:
            self.userwdgfield.listWidget_nonconf.setCurrentRow(0)




    def itemChangedNonConformite(self, itemcurrent, itemprevious):
        currentrow = self.userwdgfield.listWidget_nonconf.row(itemcurrent)
        self.userwdgfield.stackedWidget_nonconf.setCurrentIndex(currentrow)





    def updateListSymbols(self):
        for i, elem in enumerate(self.nclist):
            itemname = elem[0]
            itemtype = elem[1]
            # fieldsign = elem[2]
            if itemtype is not None and self.currentFeaturePK is not None :
                iddes = self.dbase.getValuesFromPk('Desordre', 'id_desordre', self.currentFeaturePK)
                sql = "SELECT lid_intervenant_1, lid_intervenant_2, lid_intervenant_3 FROM Observation WHERE typeobservation = '" + str(itemtype) + "'"
                sql += " AND lid_desordre = " + str(iddes)
                res = self.dbase.query(sql)
                # print('**', sql, res)
                if res is not None and len(res)>0 :
                    if not self.dbase.isAttributeNull(res[0][0]) and not self.dbase.isAttributeNull(res[0][2]):
                        self.userwdgfield.listWidget_nonconf.item(i).setIcon(self.iconinterv3)

                    elif not self.dbase.isAttributeNull(res[0][0]):
                        self.userwdgfield.listWidget_nonconf.item(i).setIcon(self.iconinterv1)

                    else:
                        self.userwdgfield.listWidget_nonconf.item(i).setIcon(QtGui.QIcon())

                else:
                    self.userwdgfield.listWidget_nonconf.item(i).setIcon(QtGui.QIcon())
            else:
                self.userwdgfield.listWidget_nonconf.item(i).setIcon(QtGui.QIcon())


    def printWidget(self):

        #create finelname
        pdfdirectory = os.path.join(self.dbase.dbaseressourcesdirectory, 'Print')
        if not os.path.isdir(pdfdirectory):
            os.mkdir(pdfdirectory)

        currentid = self.dbase.getValuesFromPk('Desordre', 'id_desordre',self.currentFeaturePK  )

        date = str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

        #filename = date + '_desordre_' + str(currentid) + '.pdf'
        filename = str(currentid) + '_desordre_' + date + '.pdf'

        pdffielname = os.path.join(pdfdirectory,filename )

        # print(pdffielname)

        #choose phaseA report or phase C report
        sql = "SELECT typeobservation FROM  Observation_now WHERE Observation_now.lid_desordre = " + str(currentid)
        sql = self.dbase.updateQueryTableNow(sql)
        res = self.dbase.query(sql)
        print('***', res)
        if res is not None and len(res) > 0 and not self.dbase.isAttributeNull(res[0][0]):
            if res[0][0] == 'PVA':
                reportype = 'procesverbalmiseadisposition'

            elif res[0][0][0:2] == 'NC':
                sql = "SELECT id_observation FROM Observation_now WHERE Observation_now.typeobservation = 'NCB'"
                sql += " AND Observation_now.lid_desordre = " + str(currentid)
                sql = self.dbase.updateQueryTableNow(sql)
                res = self.dbase.query(sql)

                if res is not None and len(res) > 0 and not self.dbase.isAttributeNull(res[0][0]):
                    reportype = 'nonconformite'
                else:
                    reportype = 'nonconformitephaseA'
        else:
            return

        #load rapport tool
        if not self.windowdialog.desktopuiloaded:
            self.windowdialog.loadUiDesktop()
        wdg = None
        for i, tool in enumerate(self.windowdialog.tools):
            print(tool.__class__.__name__)
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
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasechantiertram_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)

