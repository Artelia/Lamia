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
from qgis.PyQt.QtWidgets import (QWidget)

from ..base2.lamiabase_observation_tool import BaseObservationTool
from .lamiabasetramway_photo_tool import BaseTramwayPhotoTool as BasePhotoTool
from .lamiabasetramway_croquis_tool import BaseTramwayCroquisTool as BaseCroquisTool




class BaseTramwayObservationTool(BaseObservationTool):


    def __init__(self, **kwargs):
        super(BaseTramwayObservationTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Observation' : {'linkfield' : 'id_observation',
                                                        'widgets' : {'datetimeobservation' : self.toolwidgetmain.dateTimeEdit,
                                                                    'nombre' : self.toolwidgetmain.spinBox_nombre,
                                                                'gravite': self.toolwidgetmain.comboBox_urgence,
                                                                'evolution': self.toolwidgetmain.textEdit_evolution,
                                                                'typesuite': self.toolwidgetmain.comboBox_typesuite,
                                                                'commentairesuite': self.toolwidgetmain.textEdit_suite,


                                                                'presenceUO': self.toolwidgetmain.comboBox_presenceUO,
                                                                'presenceFatigue': self.toolwidgetmain.comboBox_presencefatigue,
                                                                    'precisionsFatigue': self.toolwidgetmain.lineEdit_precisionfatigue,
                                                                    'geoVoie': self.toolwidgetmain.comboBox_geovoie,
                                                                    'etatRechargement': self.toolwidgetmain.comboBox_etatrechargement,
                                                                    'precisionsRechargement': self.toolwidgetmain.lineEdit_precisionrechargement,
                                                                    'orniereporteuse': self.toolwidgetmain.comboBox_ornporteuse,

                                                                    'usure_V1GW1': self.toolwidgetmain.doubleSpinBox_V1GW1,
                                                                        'usure_V1GW2': self.toolwidgetmain.doubleSpinBox_V1GW2,
                                                                    'usure_V1GW3': self.toolwidgetmain.doubleSpinBox_V1GW3,
                                                                        'usure_V1GW4': self.toolwidgetmain.doubleSpinBox_V1GW4,
                                                                    'usure_V1DW1': self.toolwidgetmain.doubleSpinBox_V1DW1,
                                                                        'usure_V1DW2': self.toolwidgetmain.doubleSpinBox_V1DW2,
                                                                    'usure_V1DW3': self.toolwidgetmain.doubleSpinBox_V1DW3,
                                                                        'usure_V1DW4': self.toolwidgetmain.doubleSpinBox_V1DW4,
                                                                    'usure_V2GW1': self.toolwidgetmain.doubleSpinBox_V2GW1,
                                                                        'usure_V2GW2': self.toolwidgetmain.doubleSpinBox_V2GW2,
                                                                    'usure_V2GW3': self.toolwidgetmain.doubleSpinBox_V2GW3,
                                                                        'usure_V2GW4': self.toolwidgetmain.doubleSpinBox_V2GW4,
                                                                    'usure_V2DW1': self.toolwidgetmain.doubleSpinBox_V2DW1,
                                                                        'usure_V2DW2': self.toolwidgetmain.doubleSpinBox_V2DW2,
                                                                    'usure_V2DW3': self.toolwidgetmain.doubleSpinBox_V2DW3,
                                                                        'usure_V2DW4': self.toolwidgetmain.doubleSpinBox_V2DW4,




                                                                    'rev_fissurations': [self.toolwidgetmain.comboBox_rev_fissurations,
                                                                                        self.toolwidgetmain.comboBox_rev_fissurations2],
                                                                    'rev_degarnissage': self.toolwidgetmain.comboBox_rev_degarnissage,
                                                                    'rev_desafleurement': self.toolwidgetmain.comboBox_rev_desafleurement,
                                                                    'rev_affaissement': self.toolwidgetmain.comboBox_rev_affaissement,
                                                                    'rev_ornierage': self.toolwidgetmain.comboBox_rev_ornierage,
                                                                    'rev_disparitions': [self.toolwidgetmain.comboBox_rev_disparitions,
                                                                                        self.toolwidgetmain.comboBox_rev_disparitions2],

                                                                    'rev_deformations': self.toolwidgetmain.comboBox_rev_deformations,
                                                                    #'rev_fissurations': self.toolwidgetmain.comboBox_rev_fissurations,
                                                                    'rev_arrachement': self.toolwidgetmain.comboBox_rev_arrachement,
                                                                    'rev_remontees': self.toolwidgetmain.comboBox_rev_remontees,

                                                                    'rev_dessechement': self.toolwidgetmain.comboBox_rev_dessechement,
                                                                    'rev_vegetation': self.toolwidgetmain.comboBox_rev_vegetation,
                                                                    #'rev_disparitions': self.toolwidgetmain.comboBox_rev_disparitions,
                                                                    'rev_tonte': self.toolwidgetmain.comboBox_rev_tonte,

                                                                    'rev_tassement': self.toolwidgetmain.comboBox_rev_tassement,
                                                                    'rev_pollution': self.toolwidgetmain.comboBox_rev_pollution,

                                                                    'rev_decomposition': self.toolwidgetmain.comboBox_decompo,
                                                                    'rev_deformation': self.toolwidgetmain.comboBox_deform,


                                                                    'eqp_fissurationjoint': self.toolwidgetmain.comboBox_eqp_fissurationjoint,
                                                                    'eqp_degarnissage': self.toolwidgetmain.comboBox_eqp_degarnissage,
                                                                    'eqp_absencejoint': self.toolwidgetmain.comboBox_eqp_absencejoint,

                                                                    'eqp_fissurationgrille': self.toolwidgetmain.comboBox_eqp_fissurationgrille,
                                                                    'eqp_caniveaubouche': self.toolwidgetmain.comboBox_eqp_caniveaubouche,
                                                                    'eqp_desaffleurement': self.toolwidgetmain.comboBox_eqp_desaffleurement,
                                                                    'eqp_absenceass': self.toolwidgetmain.comboBox_eqp_absenceass,

                                                                    'eqp_heurtoir': self.toolwidgetmain.comboBox_heurtoir,
                                                                    'eqp_taquet': self.toolwidgetmain.comboBox_taquet,

                                                                    'eqp_graisseurvoie': self.toolwidgetmain.comboBox_graisseur,



                                                                    'etatEquipement': self.toolwidgetmain.comboBox_etatequip,

                                                                    'app_coteprotection': self.toolwidgetmain.comboBox_coteprotec,
                                                                    'app_coteprotectioncom': self.toolwidgetmain.lineEdit_coteprotec,
                                                                    'app_pointeaiguille': self.toolwidgetmain.comboBox_pointeaig,
                                                                    'app_pointeaiguillecom': self.toolwidgetmain.lineEdit_pointeaig,
                                                                    'app_talonaiguille': self.toolwidgetmain.comboBox_talonaig,
                                                                    'app_talonaiguillecom': self.toolwidgetmain.lineEdit_talonaig,
                                                                    'app_pointecoeur': self.toolwidgetmain.comboBox_pointecoeur,
                                                                    'app_pointecoeurcom': self.toolwidgetmain.lineEdit_pointecoeur,
                                                                    'app_pattelievre': self.toolwidgetmain.comboBox_pattelievre,
                                                                    'app_pattelievrecom': self.toolwidgetmain.lineEdit_pattelievre,
                                                                    'app_capotprotec': self.toolwidgetmain.comboBox_capotprotec,

                                                                    'app_zonetransition': self.toolwidgetmain.comboBox_zonetransit,
                                                                    'app_contrerail': self.toolwidgetmain.comboBox_contrerail,
                                                                    'app_ouverture': self.toolwidgetmain.comboBox_ouverture,






                                                                    'aspectlocalext': self.toolwidgetmain.lineEdit_aspectext,
                                                                    'aspectlocalint': self.toolwidgetmain.lineEdit_aspectint,
                                                                    'temperatureext': self.toolwidgetmain.spinBox_tempext,
                                                                    'presencerongeurs': self.toolwidgetmain.comboBox_presrongeurs,
                                                                    'presencerongeurscomm': self.toolwidgetmain.lineEdit_presrongeurs,
                                                                    'infiltrationeau': self.toolwidgetmain.lineEdit_infiltration,
                                                                    'incendieextincteurs': self.toolwidgetmain.comboBox_extincpres,
                                                                    'incendiecontroles': self.toolwidgetmain.comboBox_extinccontr,
                                                                    'incendietest': self.toolwidgetmain.comboBox_extincconclu,
                                                                    'presenceplans': self.toolwidgetmain.comboBox_presplan,
                                                                    'etatplancher': self.toolwidgetmain.comboBox_etatcan,
                                                                    'etatchemincables': self.toolwidgetmain.comboBox_etatchemins,

                                                                    'etateclairage': self.toolwidgetmain.comboBox_eclair,
                                                                    'etateclairagesecu': self.toolwidgetmain.comboBox_eclairsec,
                                                                    'etatprisecourant': self.toolwidgetmain.comboBox_prisecour,
                                                                    'etatpeintures': self.toolwidgetmain.comboBox_peinture,
                                                                    'etatidequipements': self.toolwidgetmain.comboBox_idequip,
                                                                    'etatbaretteterre': self.toolwidgetmain.comboBox_baretteterre,
                                                                    'etatappareilmesure': self.toolwidgetmain.comboBox_appmesure,
                                                                    'etatportesvoilee': self.toolwidgetmain.comboBox_portesvoile,
                                                                    'etatportesetat': self.toolwidgetmain.comboBox_porteetat,
                                                                    'etatpanopliesecupresent': self.toolwidgetmain.comboBox_panopsecupres,
                                                                    'etatpanopliesecuauxnormes': self.toolwidgetmain.comboBox_panopsecunomre,
                                                                    'etataffichagesynoptique': self.toolwidgetmain.comboBox_synopt,
                                                                    'etatverouillage': self.toolwidgetmain.comboBox_verouillage,
                                                                    'etatclesverouillage': self.toolwidgetmain.comboBox_verouillagecle,
                                                                    'etatchemincle': self.toolwidgetmain.comboBox_chemincle,

                                                                    'cellulesetat': self.toolwidgetmain.comboBox_celvisu,
                                                                    'cellulesid': self.toolwidgetmain.comboBox_celid,
                                                                    'foncvoyanttension': self.toolwidgetmain.comboBox_foncvoyanttension,
                                                                    'etataccessoiresposte': self.toolwidgetmain.comboBox_etataccessposte,
                                                                    'nombretypetransfo': self.toolwidgetmain.comboBox_typetransfo,
                                                                    'foncvoletembroch': self.toolwidgetmain.comboBox_embrochage,
                                                                    'etatverportescellules': self.toolwidgetmain.comboBox_verportescel,
                                                                    'etatcables': self.toolwidgetmain.comboBox_etatcables,
                                                                    'etatcleserure': self.toolwidgetmain.comboBox_etatcleserrure,
                                                                    'pressiongaz': self.toolwidgetmain.comboBox_presgaz,
                                                                    'voletsprotecpresence': self.toolwidgetmain.comboBox_voletsprotecpres,
                                                                    'voletsprotecetat': self.toolwidgetmain.comboBox_voletprotectetat,

                                                                    'etatvisueltab': self.toolwidgetmain.comboBox_etatvisueltab,
                                                                    'equipeid': self.toolwidgetmain.comboBox_equipeid,
                                                                    'poussiere': self.toolwidgetmain.comboBox_poussiere,
                                                                    'etatdisjonct': self.toolwidgetmain.comboBox_etatdisjonct,
                                                                    'etatisolants': self.toolwidgetmain.comboBox_etatisolants,
                                                                    'presencecle': self.toolwidgetmain.comboBox_presencecle,
                                                                    'suivivisuterre': self.toolwidgetmain.comboBox_suivivisuterre,
                                                                    'etatgainebt': self.toolwidgetmain.comboBox_etatgainebt,
                                                                    'fonctvoletembroch': self.toolwidgetmain.comboBox_fonctvoletembroch,
                                                                    'voletproteccontact': self.toolwidgetmain.comboBox_voletproteccontact,
                                                                    'positionintervdech': self.toolwidgetmain.comboBox_positionintervdech,

                                                                    'transfoetatgen': self.toolwidgetmain.comboBox_transfoetatgen,
                                                                    'transfoplaqueid': self.toolwidgetmain.comboBox_transfoplaqueid,
                                                                    'transfoverrou': self.toolwidgetmain.comboBox_transfoverrou,
                                                                    'transfoantivib': self.toolwidgetmain.comboBox_transfoantivib,
                                                                    'transfobacret': self.toolwidgetmain.comboBox_transfobacret,
                                                                    'transfobruitanorm': self.toolwidgetmain.comboBox_transfobruitanorm,
                                                                    'transforelaisprotec': self.toolwidgetmain.comboBox_transforelaisprotec,
                                                                    'transfoniveauhuile': self.toolwidgetmain.comboBox_transfoniveauhuile,
                                                                    'transfoetatcable': self.toolwidgetmain.comboBox_transfoetatcable,

                                                                    'btgenetat': self.toolwidgetmain.comboBox_btgenetat,
                                                                    'btgenhomogen': self.toolwidgetmain.comboBox_btgenhomogen,
                                                                    'btgenetatcablage': self.toolwidgetmain.comboBox_btgenetatcablage,
                                                                    'btgenfoncfreqelev': self.toolwidgetmain.comboBox_btgenfoncfreqelev,

                                                                    'btarmetatvis': self.toolwidgetmain.comboBox_btarmetatvis,
                                                                    'btarmsynop': self.toolwidgetmain.comboBox_btarmsynop,
                                                                    'btarmetatcabl': self.toolwidgetmain.comboBox_btarmetatcabl,

                                                                    'btondetatbat': self.toolwidgetmain.comboBox_btondetatbat,
                                                                    'btondetatconnex': self.toolwidgetmain.comboBox_btondetatconnex,
                                                                    'btondetatsupport': self.toolwidgetmain.comboBox_btondetatsupport,
                                                                    'btondaccessbat': self.toolwidgetmain.comboBox_btondaccessbat,
                                                                    'btondaspectond': self.toolwidgetmain.comboBox_btondaspectond,
                                                                    'btondoxydations': self.toolwidgetmain.comboBox_btondoxydations,
                                                                    'btondetatventil': self.toolwidgetmain.comboBox_btondetatventil,
                                                                    'btondetataffich': self.toolwidgetmain.comboBox_btondetataffich,
                                                                    'btonddocmateriel': self.toolwidgetmain.comboBox_btonddocmateriel

                                                                    }},
                                        'Objet' : {'linkfield' : 'id_objet',
                                                    'widgets' : {'commentaire': self.toolwidgetmain.textEdit_comm}}}

        self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre))

        self.toolwidgetmain.toolButton_V1GW1.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V1GW1))
        self.toolwidgetmain.toolButton_V1GW2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V1GW2))
        self.toolwidgetmain.toolButton_V1GW3.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V1GW3))
        self.toolwidgetmain.toolButton_V1GW4.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V1GW4))
        
        self.toolwidgetmain.toolButton_V1DW1.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V1DW1))
        self.toolwidgetmain.toolButton_V1DW2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V1DW2))
        self.toolwidgetmain.toolButton_V1DW3.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V1DW3))
        self.toolwidgetmain.toolButton_V1DW4.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V1DW4))

        self.toolwidgetmain.toolButton_V2GW1.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V2GW1))
        self.toolwidgetmain.toolButton_V2GW2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V2GW2))
        self.toolwidgetmain.toolButton_V2GW3.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V2GW3))
        self.toolwidgetmain.toolButton_V2GW4.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V2GW4))

        self.toolwidgetmain.toolButton_V2DW1.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V2DW1))
        self.toolwidgetmain.toolButton_V2DW2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V2DW2))
        self.toolwidgetmain.toolButton_V2DW3.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V2DW3))
        self.toolwidgetmain.toolButton_V2DW4.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_V2DW4))

        #self.groupBox_attributes.setParent(None)

        if self.parentWidget is not None :
            if self.parentWidget.parentWidget is not None :
                if self.parentWidget.parentWidget.DBASETABLENAME == 'Equipement':
                    equipementwdg = self.parentWidget.parentWidget
                    equipementwdg.toolwidgetmain.comboBox_souscat.currentIndexChanged.connect(self.Equipementchanged)

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield=[]
        self.instancekwargs['parentwidget'] = self
        #if self.parentWidget is not None:
        self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
        self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]

        self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    def Equipementchanged(self, combovalue):
        equipementwdgtxt = self.parentWidget.parentWidget.toolwidgetmain.comboBox_souscat.currentText()
        if equipementwdgtxt == u'Poste HT':
            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(0)
        elif equipementwdgtxt == u'Traction- tableau DC':
            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(1)
        elif equipementwdgtxt in [u'Traction - transformateur',u'Traction - transformateur aux']:
            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(2)
        elif equipementwdgtxt == u'Poste BT - général':
            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(3)
        elif equipementwdgtxt == u'Poste BT - armoire contrôle':
            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(4)
        elif equipementwdgtxt == u'Poste BT - onduleurs':
            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(5)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_observation_tool_ui.ui')
        uic.loadUi(uipath, self)