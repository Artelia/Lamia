# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_equipement_tool import BaseEquipementTool

# from ..base.lamiabase_photo_tool import BasePhotoTool
# from ..base.lamiabase_croquis_tool import BaseCroquisTool

from .lamiabaseeaupotable_photo_tool import BaseEaupotablePhotoTool as BasePhotoTool
from .lamiabaseeaupotable_croquis_tool import BaseEaupotableCroquisTool as BaseCroquisTool

import os
import datetime




class BaseEaupotableEquipementTool(BaseEquipementTool):

    LOADFIRST = True
    dbasetablename = 'Equipement'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseEaupotableEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Equipement'
        self.dbasetablename = 'Equipement'
        self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Equipement': {'tabletc': None,
                                           'idsource': 'lk_equipement',
                                           'idtcsource': None,
                                           'iddest': 'id_equipement',
                                           'idtcdest': None,
                                           'desttable': ['Equipement']}}
        # self.pickTable = None
        self.debug = False
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_equipement_tool_icon.svg')

        # ****************************************************************************************
        #properties ui
        pass
    """

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Equipement' : {'linkfield' : 'id_equipement',
                                             'widgets' : {
                                                            'type_equipement': self.userwdgfield.comboBox_cat,
                                                            'ss_type_equipement': self.userwdgfield.comboBox_soustype,
                                                            'acces': self.userwdgfield.comboBox_acces,
                                                            'diametre_entree': self.userwdgfield.doubleSpinBox_diam,
                                                            'diametre_sortie': self.userwdgfield.doubleSpinBox_diamsor,
                                                            'nature_reseau': self.userwdgfield.comboBox_nature_reseau,
                                                        'pres_echelon': self.userwdgfield.comboBox_echelon,
                                                            #ventouse
                                                             'altimetrie': self.userwdgfield.doubleSpinBox_altim,
                                                            #vanne
                                                          'localisation': [self.userwdgfield.comboBox_localisation,
                                                                           self.userwdgfield.comboBox_localisation2],
                                                         'accessibilite': [self.userwdgfield.comboBox_accessibilite,
                                                                           self.userwdgfield.comboBox_accessibilite2],
                                                        'manipulable': self.userwdgfield.comboBox_manipulable,
                                                           'position': self.userwdgfield.comboBox_position,
                                                 #vidange
                                                 'exutoire': self.userwdgfield.lineEdit_exutoire,
                                                 #reg pression
                                                 'consigne_aval': self.userwdgfield.doubleSpinBox_cons_av,
                                                 'consigne_amont': self.userwdgfield.doubleSpinBox_cons_am,

                                                 # hydrant
                                                 'id_cana_sig_sdis': self.userwdgfield.spinBox_idsdis,
                                                 'marque': [self.userwdgfield.lineEdit_marque,
                                                            self.userwdgfield.lineEdit_marque2],
                                                 'type': self.userwdgfield.lineEdit_type,
                                                 'conformite': self.userwdgfield.comboBox_conformite,

                                                 #compteur"
                                                 'dimensions': self.userwdgfield.doubleSpinBox_dimensions,
                                                 'tete_emettrice': self.userwdgfield.comboBox_tete_emettrice,
                                                 'numero': self.userwdgfield.spinBox_numero,
                                                 'equipable': self.userwdgfield.comboBox_equipable,
                                                 #'localisation': self.userwdgfield.comboBox_localisation2,
                                                 #'accessibilite': self.userwdgfield.comboBox_accessibilite2,
                                                 # 'marque': self.userwdgfield.lineEdit_marque2,
                                                 # 'type': self.userwdgfield.lineEdit_type2,
                                                 'entreprise': [self.userwdgfield.lineEdit_entreprise,
                                                                self.userwdgfield.lineEdit_entreprise2],
                                                 'telerelevage': [self.userwdgfield.comboBox_telerelevage,
                                                                  self.userwdgfield.comboBox_telerelevage2],
                                                 'organes_associes': self.userwdgfield.lineEdit_organes_associes,

                                                 #chloration
                                                 #'entreprise': self.userwdgfield.lineEdit_entreprise2,
                                                 #'telerelevage': self.userwdgfield.comboBox_telerelevage2,
                                                 # robinet de prise en charge
                                                 'collier': self.userwdgfield.comboBox_collier




                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire': self.userwdgfield.textBrowser_comm}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                      'widgets' : {  'enservice': self.userwdgfield.comboBox_enservice,
                                                                     'annee_fin_pose': self.userwdgfield.dateEdit_anneepose}}}


            self.userwdgfield.toolButton_diam.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_diam))
            self.userwdgfield.toolButton_diamsor.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_diamsor))

            self.userwdgfield.toolButton_altim.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_altim))

            self.userwdgfield.toolButton_cons_am.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_cons_am))
            self.userwdgfield.toolButton_cons_av.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_cons_av))



            self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            if False and self.parentWidget is None:
                self.pushButton_addFeature.setEnabled(False)




    def postInitFeatureProperties(self, feat):
        if feat is None and self.comboBox_featurelist.currentText() == self.newentrytext :
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
                if self.parentWidget.dbasetablename == 'Noeud':
                    # get geom
                    noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeaturePK)
                    if False:
                        if not self.dbase.revisionwork:
                            noeudfet = self.dbase.getLayerFeatureById('Noeud', self.parentWidget.currentFeature.id())
                        else:
                            noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeature.id())
                    neudfetgeom = noeudfet.geometry().asPoint()
                    self.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom,neudfetgeom],False)



    """
    def changeCategorie(self,intcat):
        self.userwdg.stackedWidget.setCurrentIndex(intcat)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):

        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid) + "," + str(lastrevision) + ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        # idobjet = self.dbase.getLastRowId('Objet')

        # sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, id_revisionbegin, id_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(lastrevision) + "," + str(lastobjetid) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        # idsys = self.dbase.getLastRowId('Descriptionsystem')

        pkequip = self.currentFeature.id()
        lastidequip = self.dbase.getLastId('Equipement') + 1

        sql = "UPDATE Equipement SET id_objet = " + str(lastobjetid) + ","
        sql += "id_descriptionsystem = " + str(lastdescriptionsystemid) + ","
        sql += "id_equipement = " + str(lastidequip) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_equipement = " + str(pkequip) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
            sql = "UPDATE Equipement SET lk_descriptionsystem = " + str(currentparentlinkfield)
            sql += " WHERE pk_equipement = " + str(pkequip)
            self.dbase.query(sql)
            self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):
        pass


    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']

        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True


    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)