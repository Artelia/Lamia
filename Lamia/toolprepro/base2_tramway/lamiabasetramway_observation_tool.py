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

from .lamiabasetramway_photo_tool import BaseTramwayPhotoTool as BasePhotoTool
from .lamiabasetramway_croquis_tool import BaseTramwayCroquisTool as BaseCroquisTool

import os
import datetime


class BaseTramwayObservationTool(BaseObservationTool):

    dbasetablename = 'Observation'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseTramwayObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Observation' : {'linkfield' : 'id_observation',
                                             'widgets' : {'datetimeobservation' : self.userwdgfield.dateTimeEdit,
                                                          'nombre' : self.userwdgfield.spinBox_nombre,
                                                        'gravite': self.userwdgfield.comboBox_urgence,
                                                        'evolution': self.userwdgfield.textEdit_evolution,
                                                        'typesuite': self.userwdgfield.comboBox_typesuite,
                                                        'commentairesuite': self.userwdgfield.textEdit_suite,


                                                        'presenceUO': self.userwdgfield.comboBox_presenceUO,
                                                        'presenceFatigue': self.userwdgfield.comboBox_presencefatigue,
                                                         'precisionsFatigue': self.userwdgfield.lineEdit_precisionfatigue,
                                                          'geoVoie': self.userwdgfield.comboBox_geovoie,
                                                          'etatRechargement': self.userwdgfield.comboBox_etatrechargement,
                                                          'precisionsRechargement': self.userwdgfield.lineEdit_precisionrechargement,
                                                          'orniereporteuse': self.userwdgfield.comboBox_ornporteuse,

                                                          'usure_V1GW1': self.userwdgfield.doubleSpinBox_V1GW1,
                                                              'usure_V1GW2': self.userwdgfield.doubleSpinBox_V1GW2,
                                                          'usure_V1GW3': self.userwdgfield.doubleSpinBox_V1GW3,
                                                              'usure_V1GW4': self.userwdgfield.doubleSpinBox_V1GW4,
                                                          'usure_V1DW1': self.userwdgfield.doubleSpinBox_V1DW1,
                                                             'usure_V1DW2': self.userwdgfield.doubleSpinBox_V1DW2,
                                                          'usure_V1DW3': self.userwdgfield.doubleSpinBox_V1DW3,
                                                              'usure_V1DW4': self.userwdgfield.doubleSpinBox_V1DW4,
                                                          'usure_V2GW1': self.userwdgfield.doubleSpinBox_V2GW1,
                                                              'usure_V2GW2': self.userwdgfield.doubleSpinBox_V2GW2,
                                                          'usure_V2GW3': self.userwdgfield.doubleSpinBox_V2GW3,
                                                              'usure_V2GW4': self.userwdgfield.doubleSpinBox_V2GW4,
                                                          'usure_V2DW1': self.userwdgfield.doubleSpinBox_V2DW1,
                                                              'usure_V2DW2': self.userwdgfield.doubleSpinBox_V2DW2,
                                                          'usure_V2DW3': self.userwdgfield.doubleSpinBox_V2DW3,
                                                              'usure_V2DW4': self.userwdgfield.doubleSpinBox_V2DW4,




                                                          'rev_fissurations': [self.userwdgfield.comboBox_rev_fissurations,
                                                                               self.userwdgfield.comboBox_rev_fissurations2],
                                                          'rev_degarnissage': self.userwdgfield.comboBox_rev_degarnissage,
                                                          'rev_desafleurement': self.userwdgfield.comboBox_rev_desafleurement,
                                                          'rev_affaissement': self.userwdgfield.comboBox_rev_affaissement,
                                                          'rev_ornierage': self.userwdgfield.comboBox_rev_ornierage,
                                                          'rev_disparitions': [self.userwdgfield.comboBox_rev_disparitions,
                                                                               self.userwdgfield.comboBox_rev_disparitions2],

                                                          'rev_deformations': self.userwdgfield.comboBox_rev_deformations,
                                                          #'rev_fissurations': self.userwdgfield.comboBox_rev_fissurations,
                                                          'rev_arrachement': self.userwdgfield.comboBox_rev_arrachement,
                                                          'rev_remontees': self.userwdgfield.comboBox_rev_remontees,

                                                          'rev_dessechement': self.userwdgfield.comboBox_rev_dessechement,
                                                          'rev_vegetation': self.userwdgfield.comboBox_rev_vegetation,
                                                          #'rev_disparitions': self.userwdgfield.comboBox_rev_disparitions,
                                                          'rev_tonte': self.userwdgfield.comboBox_rev_tonte,

                                                          'rev_tassement': self.userwdgfield.comboBox_rev_tassement,
                                                          'rev_pollution': self.userwdgfield.comboBox_rev_pollution,

                                                          'rev_decomposition': self.userwdgfield.comboBox_decompo,
                                                          'rev_deformation': self.userwdgfield.comboBox_deform,


                                                          'eqp_fissurationjoint': self.userwdgfield.comboBox_eqp_fissurationjoint,
                                                          'eqp_degarnissage': self.userwdgfield.comboBox_eqp_degarnissage,
                                                          'eqp_absencejoint': self.userwdgfield.comboBox_eqp_absencejoint,

                                                          'eqp_fissurationgrille': self.userwdgfield.comboBox_eqp_fissurationgrille,
                                                          'eqp_caniveaubouche': self.userwdgfield.comboBox_eqp_caniveaubouche,
                                                          'eqp_desaffleurement': self.userwdgfield.comboBox_eqp_desaffleurement,
                                                          'eqp_absenceass': self.userwdgfield.comboBox_eqp_absenceass,

                                                          'eqp_heurtoir': self.userwdgfield.comboBox_heurtoir,
                                                          'eqp_taquet': self.userwdgfield.comboBox_taquet,

                                                          'eqp_graisseurvoie': self.userwdgfield.comboBox_graisseur,



                                                          'etatEquipement': self.userwdgfield.comboBox_etatequip,

                                                          'app_coteprotection': self.userwdgfield.comboBox_coteprotec,
                                                          'app_coteprotectioncom': self.userwdgfield.lineEdit_coteprotec,
                                                          'app_pointeaiguille': self.userwdgfield.comboBox_pointeaig,
                                                          'app_pointeaiguillecom': self.userwdgfield.lineEdit_pointeaig,
                                                          'app_talonaiguille': self.userwdgfield.comboBox_talonaig,
                                                          'app_talonaiguillecom': self.userwdgfield.lineEdit_talonaig,
                                                          'app_pointecoeur': self.userwdgfield.comboBox_pointecoeur,
                                                          'app_pointecoeurcom': self.userwdgfield.lineEdit_pointecoeur,
                                                          'app_pattelievre': self.userwdgfield.comboBox_pattelievre,
                                                          'app_pattelievrecom': self.userwdgfield.lineEdit_pattelievre,
                                                          'app_capotprotec': self.userwdgfield.comboBox_capotprotec,

                                                          'app_zonetransition': self.userwdgfield.comboBox_zonetransit,
                                                          'app_contrerail': self.userwdgfield.comboBox_contrerail,
                                                          'app_ouverture': self.userwdgfield.comboBox_ouverture,






                                                          'aspectlocalext': self.userwdgfield.lineEdit_aspectext,
                                                          'aspectlocalint': self.userwdgfield.lineEdit_aspectint,
                                                          'temperatureext': self.userwdgfield.spinBox_tempext,
                                                          'presencerongeurs': self.userwdgfield.comboBox_presrongeurs,
                                                          'presencerongeurscomm': self.userwdgfield.lineEdit_presrongeurs,
                                                          'infiltrationeau': self.userwdgfield.lineEdit_infiltration,
                                                          'incendieextincteurs': self.userwdgfield.comboBox_extincpres,
                                                          'incendiecontroles': self.userwdgfield.comboBox_extinccontr,
                                                          'incendietest': self.userwdgfield.comboBox_extincconclu,
                                                          'presenceplans': self.userwdgfield.comboBox_presplan,
                                                          'etatplancher': self.userwdgfield.comboBox_etatcan,
                                                          'etatchemincables': self.userwdgfield.comboBox_etatchemins,

                                                          'etateclairage': self.userwdgfield.comboBox_eclair,
                                                          'etateclairagesecu': self.userwdgfield.comboBox_eclairsec,
                                                          'etatprisecourant': self.userwdgfield.comboBox_prisecour,
                                                          'etatpeintures': self.userwdgfield.comboBox_peinture,
                                                          'etatidequipements': self.userwdgfield.comboBox_idequip,
                                                          'etatbaretteterre': self.userwdgfield.comboBox_baretteterre,
                                                          'etatappareilmesure': self.userwdgfield.comboBox_appmesure,
                                                          'etatportesvoilee': self.userwdgfield.comboBox_portesvoile,
                                                          'etatportesetat': self.userwdgfield.comboBox_porteetat,
                                                          'etatpanopliesecupresent': self.userwdgfield.comboBox_panopsecupres,
                                                          'etatpanopliesecuauxnormes': self.userwdgfield.comboBox_panopsecunomre,
                                                          'etataffichagesynoptique': self.userwdgfield.comboBox_synopt,
                                                          'etatverouillage': self.userwdgfield.comboBox_verouillage,
                                                          'etatclesverouillage': self.userwdgfield.comboBox_verouillagecle,
                                                          'etatchemincle': self.userwdgfield.comboBox_chemincle,

                                                          'cellulesetat': self.userwdgfield.comboBox_celvisu,
                                                          'cellulesid': self.userwdgfield.comboBox_celid,
                                                          'foncvoyanttension': self.userwdgfield.comboBox_foncvoyanttension,
                                                          'etataccessoiresposte': self.userwdgfield.comboBox_etataccessposte,
                                                          'nombretypetransfo': self.userwdgfield.comboBox_typetransfo,
                                                          'foncvoletembroch': self.userwdgfield.comboBox_embrochage,
                                                          'etatverportescellules': self.userwdgfield.comboBox_verportescel,
                                                          'etatcables': self.userwdgfield.comboBox_etatcables,
                                                          'etatcleserure': self.userwdgfield.comboBox_etatcleserrure,
                                                          'pressiongaz': self.userwdgfield.comboBox_presgaz,
                                                          'voletsprotecpresence': self.userwdgfield.comboBox_voletsprotecpres,
                                                          'voletsprotecetat': self.userwdgfield.comboBox_voletprotectetat,

                                                          'etatvisueltab': self.userwdgfield.comboBox_etatvisueltab,
                                                          'equipeid': self.userwdgfield.comboBox_equipeid,
                                                          'poussiere': self.userwdgfield.comboBox_poussiere,
                                                          'etatdisjonct': self.userwdgfield.comboBox_etatdisjonct,
                                                          'etatisolants': self.userwdgfield.comboBox_etatisolants,
                                                          'presencecle': self.userwdgfield.comboBox_presencecle,
                                                          'suivivisuterre': self.userwdgfield.comboBox_suivivisuterre,
                                                          'etatgainebt': self.userwdgfield.comboBox_etatgainebt,
                                                          'fonctvoletembroch': self.userwdgfield.comboBox_fonctvoletembroch,
                                                          'voletproteccontact': self.userwdgfield.comboBox_voletproteccontact,
                                                          'positionintervdech': self.userwdgfield.comboBox_positionintervdech,

                                                          'transfoetatgen': self.userwdgfield.comboBox_transfoetatgen,
                                                          'transfoplaqueid': self.userwdgfield.comboBox_transfoplaqueid,
                                                          'transfoverrou': self.userwdgfield.comboBox_transfoverrou,
                                                          'transfoantivib': self.userwdgfield.comboBox_transfoantivib,
                                                          'transfobacret': self.userwdgfield.comboBox_transfobacret,
                                                          'transfobruitanorm': self.userwdgfield.comboBox_transfobruitanorm,
                                                          'transforelaisprotec': self.userwdgfield.comboBox_transforelaisprotec,
                                                          'transfoniveauhuile': self.userwdgfield.comboBox_transfoniveauhuile,
                                                          'transfoetatcable': self.userwdgfield.comboBox_transfoetatcable,

                                                          'btgenetat': self.userwdgfield.comboBox_btgenetat,
                                                          'btgenhomogen': self.userwdgfield.comboBox_btgenhomogen,
                                                          'btgenetatcablage': self.userwdgfield.comboBox_btgenetatcablage,
                                                          'btgenfoncfreqelev': self.userwdgfield.comboBox_btgenfoncfreqelev,

                                                          'btarmetatvis': self.userwdgfield.comboBox_btarmetatvis,
                                                          'btarmsynop': self.userwdgfield.comboBox_btarmsynop,
                                                          'btarmetatcabl': self.userwdgfield.comboBox_btarmetatcabl,

                                                          'btondetatbat': self.userwdgfield.comboBox_btondetatbat,
                                                          'btondetatconnex': self.userwdgfield.comboBox_btondetatconnex,
                                                          'btondetatsupport': self.userwdgfield.comboBox_btondetatsupport,
                                                          'btondaccessbat': self.userwdgfield.comboBox_btondaccessbat,
                                                          'btondaspectond': self.userwdgfield.comboBox_btondaspectond,
                                                          'btondoxydations': self.userwdgfield.comboBox_btondoxydations,
                                                          'btondetatventil': self.userwdgfield.comboBox_btondetatventil,
                                                          'btondetataffich': self.userwdgfield.comboBox_btondetataffich,
                                                          'btonddocmateriel': self.userwdgfield.comboBox_btonddocmateriel

                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire': self.userwdgfield.textEdit_comm}}}

            self.userwdgfield.toolButton_calc_nb.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nombre))

            self.userwdgfield.toolButton_V1GW1.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V1GW1))
            self.userwdgfield.toolButton_V1GW2.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V1GW2))
            self.userwdgfield.toolButton_V1GW3.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V1GW3))
            self.userwdgfield.toolButton_V1GW4.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V1GW4))
            
            self.userwdgfield.toolButton_V1DW1.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V1DW1))
            self.userwdgfield.toolButton_V1DW2.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V1DW2))
            self.userwdgfield.toolButton_V1DW3.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V1DW3))
            self.userwdgfield.toolButton_V1DW4.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V1DW4))

            self.userwdgfield.toolButton_V2GW1.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V2GW1))
            self.userwdgfield.toolButton_V2GW2.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V2GW2))
            self.userwdgfield.toolButton_V2GW3.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V2GW3))
            self.userwdgfield.toolButton_V2GW4.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V2GW4))

            self.userwdgfield.toolButton_V2DW1.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V2DW1))
            self.userwdgfield.toolButton_V2DW2.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V2DW2))
            self.userwdgfield.toolButton_V2DW3.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V2DW3))
            self.userwdgfield.toolButton_V2DW4.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_V2DW4))

            self.groupBox_attributes.setParent(None)

            if self.parentWidget is not None :
                if self.parentWidget.parentWidget is not None :
                    if self.parentWidget.parentWidget.dbasetablename == 'Equipement':
                        equipementwdg = self.parentWidget.parentWidget
                        equipementwdg.userwdgfield.comboBox_souscat.currentIndexChanged.connect(self.Equipementchanged)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield=[]
            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]

                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    def Equipementchanged(self, combovalue):
        equipementwdgtxt = self.parentWidget.parentWidget.userwdgfield.comboBox_souscat.currentText()
        if equipementwdgtxt == u'Poste HT':
            self.userwdgfield.stackedWidget_3.setCurrentIndex(0)
        elif equipementwdgtxt == u'Traction- tableau DC':
            self.userwdgfield.stackedWidget_3.setCurrentIndex(1)
        elif equipementwdgtxt in [u'Traction - transformateur',u'Traction - transformateur aux']:
            self.userwdgfield.stackedWidget_3.setCurrentIndex(2)
        elif equipementwdgtxt == u'Poste BT - général':
            self.userwdgfield.stackedWidget_3.setCurrentIndex(3)
        elif equipementwdgtxt == u'Poste BT - armoire contrôle':
            self.userwdgfield.stackedWidget_3.setCurrentIndex(4)
        elif equipementwdgtxt == u'Poste BT - onduleurs':
            self.userwdgfield.stackedWidget_3.setCurrentIndex(5)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_observation_tool_ui.ui')
        uic.loadUi(uipath, self)