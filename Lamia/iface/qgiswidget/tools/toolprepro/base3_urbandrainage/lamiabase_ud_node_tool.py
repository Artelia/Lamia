# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
import qgis
import sys, datetime
from collections import OrderedDict

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
from ..base3.lamiabase_node_tool import BaseNodeTool

# from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
# from .lamiabaseassainissement_croquis_tool import BaseAssainissementCroquisTool as BaseCroquisTool
# from .lamiabaseassainissement_desordre_tool import BaseAssainissementDesordreTool
# from .lamiabaseassainissement_equipement_tool import BaseAssainissementEquipementTool

from .lamiabase_ud_camera_tool import BaseUrbandrainageCameraTool
from .lamiabase_ud_sketch_tool import BaseUrbandrainageSketchTool
from .lamiabase_ud_deficiency_tool import BaseUrbandrainageDeficiencyTool
from .lamiabase_ud_equipment_tool import BaseUrbandrainageEquipmentTool



class BaseUrbandrainageNodeTool(BaseNodeTool):



    def __init__(self, **kwargs):
        super(BaseUrbandrainageNodeTool, self).__init__(**kwargs)



    def initMainToolWidget(self):

        if self.dbase.variante in [None, 'Lamia']:

            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {'node' : {'linkfield' : 'id_noeud',
                                                'widgets' : {
                                                            'sewertype': self.toolwidgetmain.comboBox_typeReseau,
                                                        'location' : self.toolwidgetmain.comboBox_environnement,
                                                            'nodetype': self.toolwidgetmain.comboBox_typeOuvrageAss,
                                                            'nodesubtype': self.toolwidgetmain.comboBox_soustype,
                                                        'manholecovershape': self.toolwidgetmain.comboBox_Formetampon,
                                                            'accessibility': self.toolwidgetmain.comboBox_accessibilite,

                                                        #regard
                                                        'presencesteps' : self.toolwidgetmain.comboBox_echelon,
                                                        'presencehandle': self.toolwidgetmain.comboBox_crosse,
                                                            'presencelowflowchannel': self.toolwidgetmain.comboBox_cunette,
                                                        'manholeshape': self.toolwidgetmain.comboBox_formeregard,
                                                        'manholematerial': self.toolwidgetmain.comboBox_regmat,

                                                        #branchement
                                                            'presencesiphoidpartition': self.toolwidgetmain.comboBox_cloisonsiphoide,
                                                            'presencelid': self.toolwidgetmain.comboBox_couvercle,
                                                        'lateralusercategory': self.toolwidgetmain.comboBox_typeusager,

                                                        #avaloir
                                                        'sedimenttrap': self.toolwidgetmain.comboBox_decant,

                                                        #PR
                                                        'psfence': self.toolwidgetmain.comboBox_cloture,
                                                        'pslocked': self.toolwidgetmain.comboBox_verouille,
                                                            'psh2streatment': self.toolwidgetmain.comboBox_h2s,

                                                        'pseleccabinet': self.toolwidgetmain.comboBox_posteelec,
                                                            'pseleccabinetlocked': self.toolwidgetmain.comboBox_armoire_verouille,
                                                        'psremotemonitoring': [self.toolwidgetmain.comboBox_telegestion,self.toolwidgetmain.comboBox_DSHalarme],
                                                        'psremotemonitoringcomment': self.toolwidgetmain.textBrowser_telegestioncom,
                                                        'pspumpswitchingcontroller': self.toolwidgetmain.comboBox_permut_pompes,

                                                        'psmaterial': [self.toolwidgetmain.comboBox_PRmateriau,self.toolwidgetmain.comboBox_DSH_materiau],
                                                        'psfallprotectiongratings': self.toolwidgetmain.comboBox_antichute,
                                                        'psinletscreen': self.toolwidgetmain.comboBox_panierdegrileur,

                                                            'pspumpswitchingcontrollertype': self.toolwidgetmain.comboBox_typeasservissement,
                                                            'psfloatnumber': self.toolwidgetmain.spinBox_poires,
                                                            'psoverflow': self.toolwidgetmain.comboBox_surverse,

                                                        'psguiderail': self.toolwidgetmain.comboBox_barrresguidage,
                                                        'pspumpliftingchain': self.toolwidgetmain.comboBox_pompe_relevage,
                                                            'pspumpnumber': self.toolwidgetmain.spinBox_pompes,

                                                        'pscheckvalve': self.toolwidgetmain.comboBox_vanne_clapet,
                                                        'psgatevalve': self.toolwidgetmain.comboBox_vanne_vanne,
                                                        'pspressureport': self.toolwidgetmain.comboBox_vanne_prisepression,

                                                        #DSH
                                                        # DSH materiau : self.toolwidgetmain_2.comboBox_DSH_materiau cf PR
                                                        #'DSHpresencealarme': self.toolwidgetmain_2.comboBox_DSHalarme,
                                                            'presencecontroller': self.toolwidgetmain.comboBox_automate,


                                                        # autre
                                                        'depthinvert': self.toolwidgetmain.doubleSpinBox_profradierouvrage,
                                                            'width': self.toolwidgetmain.doubleSpinBox_largeur,
                                                            'lenght': self.toolwidgetmain.doubleSpinBox_longueur,

                                                            'X': self.toolwidgetmain.doubleSpinBox_X,
                                                            'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                            'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                            'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                            'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                            'dZ': self.toolwidgetmain.doubleSpinBox_dZ,


                                                        }},
                                'object' : {'linkfield' : 'id_object',
                                            'widgets' : {'comment' : self.toolwidgetmain.textBrowser_commentaire}},
                                'descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                            'widgets' : {}}}

            self.toolwidgetmain.toolButton_longueur.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_longueur))
            self.toolwidgetmain.toolButton_largeur.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_largeur))
            self.toolwidgetmain.toolButton_calc.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profradierouvrage))
            self.toolwidgetmain.toolButton_poires.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_poires))
            self.toolwidgetmain.toolButton_pompes.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_pompes))

            self.toolwidgetmain.comboBox_typeOuvrageAss.currentIndexChanged.connect(self.fielduiTypeOhChanged)
            self.toolwidgetmain.pushButton_getGPS.clicked.connect(self.getGPSValue)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            self.propertieswdgPHOTOGRAPHIE = BaseUrbandrainageCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseUrbandrainageSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgDesordre = BaseUrbandrainageDeficiencyTool(**self.instancekwargs)
            self.propertieswdgDesordre.SKIP_LOADING_UI = True
            self.propertieswdgDesordre.initMainToolWidget()
            self.propertieswdgDesordre.formtoolwidgetconfdictmain['deficiency']['widgets']['deficiencycategory'] = 'NOD'
            #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            #self.propertieswdgDesordre.groupBox_elements.setParent(None)
            #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            #self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)

            self.propertieswdgEquipement = BaseUrbandrainageEquipmentTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgEquipement)


            self.gpswidget = {'x' : {'widget' : self.toolwidgetmain.label_X,
                                        'gga' : 'Xcrs'},
                                'y': {'widget': self.toolwidgetmain.label_Y,
                                    'gga': 'Ycrs'},
                                'zmngf': {'widget': self.toolwidgetmain.label_Z,
                                    'gga': 'zmNGF'},
                                'dx': {'widget': self.toolwidgetmain.label_dX,
                                    'gst': 'xprecision'},
                                'dy': {'widget': self.toolwidgetmain.label_dY,
                                    'gst': 'yprecision'},
                                'dz': {'widget': self.toolwidgetmain.label_dZ,
                                    'gst': 'zprecision'},
                                'zgps': {'widget': self.toolwidgetmain.label_zgps,
                                        'gga': 'elevation'},
                                'zwgs84': {'widget': self.toolwidgetmain.label_zwgs84,
                                        'gga': 'deltageoid'},
                                'raf09': {'widget': self.toolwidgetmain.label_raf09,
                                        'gga': 'RAF09'},
                                'hauteurperche': {'widget': self.toolwidgetmain.label_hautperche,
                                        'gga': 'hauteurperche'}
                                }

        elif self.dbase.variante in ['2018_SNCF']:

            self.toolwidgetmain = UserUI_2()
            self.formtoolwidgetconfdictmain = {'node': {'linkfield': 'id_node',
                                                    'widgets': {
                                                        'sewertype': self.toolwidgetmain.comboBox_typeReseau,
                                                        'location': self.toolwidgetmain.comboBox_environnement,
                                                        'nodetype': self.toolwidgetmain.comboBox_typeOuvrageAss,
                                                        'manholecovershape': self.toolwidgetmain.comboBox_Formetampon,
                                                        'accessibility': self.toolwidgetmain.comboBox_accessibilite,

                                                        # regard
                                                        'presencesteps': self.toolwidgetmain.comboBox_echelon,
                                                        'presencehandle': self.toolwidgetmain.comboBox_crosse,
                                                        # 'presencecunette': self.toolwidgetmain.comboBox_cunette,
                                                        'manholeshape': self.toolwidgetmain.comboBox_formeregard,
                                                        # 'formeregard': self.toolwidgetmain.comboBox_formeregard,



                                                        # branchement
                                                        # 'cloisonsiphoide': self.toolwidgetmain.comboBox_cloisonsiphoide,
                                                        # 'couvercle': self.toolwidgetmain.comboBox_couvercle,

                                                        # PR
                                                        # 'PRcloture': self.toolwidgetmain.comboBox_cloture,
                                                        # 'PRverouille': self.toolwidgetmain.comboBox_verouille,

                                                        'pseleccabinet': self.toolwidgetmain.comboBox_posteelec,
                                                        # 'PRarmoireelecverouillee': self.toolwidgetmain.comboBox_armoire_verouille,
                                                        'psremotemonitoring': [self.toolwidgetmain.comboBox_telegestion,
                                                                        self.toolwidgetmain.comboBox_DSHalarme],
                                                        'psremotemonitoringcomment': self.toolwidgetmain.textBrowser_telegestioncom,
                                                        # 'PRpermutautopompe': self.toolwidgetmain.comboBox_permut_pompes,

                                                        'psmaterial': [self.toolwidgetmain.comboBox_PRmateriau,
                                                                    self.toolwidgetmain.comboBox_DSH_materiau],
                                                        # 'PRgrilleantichute': self.toolwidgetmain.comboBox_antichute,
                                                        # 'PRpanierdegrilleur': self.toolwidgetmain.comboBox_panierdegrileur,
                                                        'pspumpswitchingcontrollertype': self.toolwidgetmain.comboBox_typeasservissement,
                                                        'psfloatnumber': self.toolwidgetmain.spinBox_poires,
                                                        'psoverflow': self.toolwidgetmain.comboBox_surverse,

                                                        # 'PRpompebarreguidage': self.toolwidgetmain.comboBox_barrresguidage,
                                                        # 'PRpompechainerelevage': self.toolwidgetmain.comboBox_pompe_relevage,
                                                        'PRnbrepompes': self.toolwidgetmain.spinBox_pompes,

                                                        # 'PRclapet': self.toolwidgetmain.comboBox_vanne_clapet,
                                                        # 'PRvannes': self.toolwidgetmain.comboBox_vanne_vanne,
                                                        # 'PRprisepression': self.toolwidgetmain.comboBox_vanne_prisepression,

                                                        # DSH
                                                        # DSH materiau : self.toolwidgetmain.comboBox_DSH_materiau cf PR
                                                        # 'DSHpresencealarme': self.toolwidgetmain.comboBox_DSHalarme,
                                                        'presencecontroller': self.toolwidgetmain.comboBox_automate,

                                                        # autre
                                                        'depthinvert': self.toolwidgetmain.doubleSpinBox_profradierouvrage,
                                                        'width': self.toolwidgetmain.doubleSpinBox_largeur,
                                                        'lenght': self.toolwidgetmain.doubleSpinBox_longueur,

                                                        'X': self.toolwidgetmain.doubleSpinBox_X,
                                                        'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                        'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                        'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                        'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                        'dZ': self.toolwidgetmain.doubleSpinBox_dZ,

                                                    }},
                                        'object': {'linkfield': 'id_object',
                                                    'widgets': {'name': self.toolwidgetmain.lineEdit_libelle,
                                                                'comment': self.toolwidgetmain.textBrowser_commentaire}},
                                        'descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                                'widgets': {}}}

            self.toolwidgetmain.toolButton_longueur.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_longueur))
            self.toolwidgetmain.toolButton_largeur.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_largeur))
            self.toolwidgetmain.toolButton_calc.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profradierouvrage))
            self.toolwidgetmain.toolButton_poires.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_poires))
            self.toolwidgetmain.toolButton_pompes.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_pompes))

            self.toolwidgetmain.comboBox_typeOuvrageAss.currentIndexChanged.connect(self.fieldui2TypeOhChanged)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            self.propertieswdgPHOTOGRAPHIE = BaseUrbandrainageCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
            self.propertieswdgCROQUIS = BaseUrbandrainageSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
            
            self.propertieswdgDesordre = BaseUrbandrainageDeficiencyTool(**self.instancekwargs)
            self.propertieswdgDesordre.initMainToolWidget()
            self.propertieswdgDesordre.formtoolwidgetconfdictmain['deficiency']['widgets']['deficiencycategory'] = 'NOD'
            #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            #self.propertieswdgDesordre.groupBox_elements.setParent(None)
            #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            #self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)

            self.propertieswdgEquipement = BaseUrbandrainageEquipmentTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgEquipement)
            
            self.gpswidget = {'x': {'widget': self.toolwidgetmain.label_X,
                                    'gga': 'Xcrs'},
                              'y': {'widget': self.toolwidgetmain.label_Y,
                                    'gga': 'Ycrs'},
                              'zmngf': {'widget': self.toolwidgetmain.label_Z,
                                        'gga': 'zmNGF'},
                              'dx': {'widget': self.toolwidgetmain.label_dX,
                                     'gst': 'xprecision'},
                              'dy': {'widget': self.toolwidgetmain.label_dY,
                                     'gst': 'yprecision'},
                              'dz': {'widget': self.toolwidgetmain.label_dZ,
                                     'gst': 'zprecision'},
                              'zgps': {'widget': self.toolwidgetmain.label_zgps,
                                       'gga': 'elevation'},
                              'zwgs84': {'widget': self.toolwidgetmain.label_zwgs84,
                                         'gga': 'deltageoid'},
                              'raf09': {'widget': self.toolwidgetmain.label_raf09,
                                        'gga': 'RAF09'},
                              'hauteurperche': {'widget': self.toolwidgetmain.label_hautperche,
                                                'gga': 'hauteurperche'}
                              }

            #self.dbase.dbasetables['node']['fields']['typeOuvrageAss']['Cst'] = self.modifiedtypeohassdict


        elif self.dbase.variante in ['CD41']:

            self.toolwidgetmain = UserUI_3()
            self.formtoolwidgetconfdictmain = {'node': {'linkfield': 'id_noeud',
                                                    'widgets': {
                                                        'domain': self.toolwidgetmain.comboBox_domaine,
                                                        'sewertype': self.toolwidgetmain.comboBox_typeReseau,
                                                        'location': self.toolwidgetmain.comboBox_environnement,
                                                        'nodetype': self.toolwidgetmain.comboBox_typeOuvrageAss,
                                                        'nodesubtype': self.toolwidgetmain.comboBox_soustype,


                                                        # regard
                                                        'accessibility': [self.toolwidgetmain.comboBox_accessibilite,
                                                                        self.toolwidgetmain.comboBox_accessibilite2],
                                                        'manholematerial': self.toolwidgetmain.comboBox_reg_materiau,
                                                            # diam_regard : longeur
                                                        'manholecovertype': self.toolwidgetmain.comboBox_typetampon,
                                                        'manholecoverdiameter': self.toolwidgetmain.doubleSpinBox_diamtampon,
                                                        'presencesteps': self.toolwidgetmain.comboBox_echelon,


                                                    # Equipement

                                                        #ouvrage de regul
                                                        'psremotemonitoring': self.toolwidgetmain.comboBox_telegestion_2,
                                                        'prof01': self.toolwidgetmain.comboBox_telegestion_2,


                                                        #PR
                                                        'psnominalcapacity': self.toolwidgetmain.doubleSpinBox_capanom,
                                                        'pspumpnumber': self.toolwidgetmain.spinBox_pompes2,
                                                        'psh2streatment': self.toolwidgetmain.comboBox_traithdeuxs,
                                                        'psoverflow': self.toolwidgetmain.comboBox_surverse2,

                                                        #avaloir
                                                        'sedimenttrap': self.toolwidgetmain.comboBox_decant,
                                                        #dimgrille : longeur


                                                        # autre
                                                        'depthinvert': self.toolwidgetmain.doubleSpinBox_profradierouvrage,
                                                        'width': self.toolwidgetmain.doubleSpinBox_largeur,
                                                        'lenght': self.toolwidgetmain.doubleSpinBox_longueur,

                                                        'X': self.toolwidgetmain.doubleSpinBox_X,
                                                        'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                        'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                        'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                        'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                        'dZ': self.toolwidgetmain.doubleSpinBox_dZ,

                                                    }},
                                        'object': {'linkfield': 'id_object',
                                                    'widgets': {
                                                                'comment': self.toolwidgetmain.textBrowser_commentaire
                                                            }},
                                        'descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                                'widgets': {}}}

            self.toolwidgetmain.toolButton_longueur.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_longueur))
            self.toolwidgetmain.toolButton_diamtampon.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diamtampon))
            self.toolwidgetmain.toolButton_profsurverse.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profsurverse))
            self.toolwidgetmain.toolButton_capanom.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_capanom))
            self.toolwidgetmain.toolButton_pompes2.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_pompes2))
            self.toolwidgetmain.toolButton_largeur.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_largeur))
            self.toolwidgetmain.toolButton_calc.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profradierouvrage))

            self.toolwidgetmain.comboBox_typeOuvrageAss.currentIndexChanged.connect(self.fieldui3TypeOhChanged)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            self.propertieswdgDesordre = BaseUrbandrainageDeficiencyTool(**self.instancekwargs)
            self.propertieswdgDesordre.initMainToolWidget()
            self.propertieswdgDesordre.formtoolwidgetconfdictmain['deficiency']['widgets']['deficiencycategory'] = 'NOD'
            #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            #self.propertieswdgDesordre.groupBox_elements.setParent(None)
            #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            #self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)
            self.propertieswdgPHOTOGRAPHIE = BaseUrbandrainageCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
            self.propertieswdgCROQUIS = BaseUrbandrainageSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)


            self.gpswidget = {'x': {'widget': self.toolwidgetmain.label_X,
                                    'gga': 'Xcrs'},
                              'y': {'widget': self.toolwidgetmain.label_Y,
                                    'gga': 'Ycrs'},
                              'zmngf': {'widget': self.toolwidgetmain.label_Z,
                                        'gga': 'zmNGF'},
                              'dx': {'widget': self.toolwidgetmain.label_dX,
                                     'gst': 'xprecision'},
                              'dy': {'widget': self.toolwidgetmain.label_dY,
                                     'gst': 'yprecision'},
                              'dz': {'widget': self.toolwidgetmain.label_dZ,
                                     'gst': 'zprecision'},
                              'zgps': {'widget': self.toolwidgetmain.label_zgps,
                                       'gga': 'elevation'},
                              'zwgs84': {'widget': self.toolwidgetmain.label_zwgs84,
                                         'gga': 'deltageoid'},
                              'raf09': {'widget': self.toolwidgetmain.label_raf09,
                                        'gga': 'RAF09'},
                              'hauteurperche': {'widget': self.toolwidgetmain.label_hautperche,
                                                'gga': 'hauteurperche'}}


    def fielduiTypeOhChanged(self, comboindex):
        #print(self.toolwidgetmain.comboBox_typeOuvrageAss.currentText())
        currenttext = self.toolwidgetmain.comboBox_typeOuvrageAss.currentText()

        if currenttext in ['Regard','Regard mixte EP EU']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
        elif currenttext in ['Branchement']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)
        elif currenttext in ['Poste de refoulement']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(2)
            """
            elif sys.version_info < (3, 0) and currenttext in ['Débourbeur/déshuileur'.decode('utf8')]:
                self.toolwidgetmain.stackedWidget.setCurrentIndex(3)
            elif sys.version_info > (3, 0) and currenttext in ['Débourbeur/déshuileur']:
                self.toolwidgetmain.stackedWidget.setCurrentIndex(3)
            """
        elif currenttext in ['Débourbeur/déshuileur']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(3)
        elif currenttext in ['Avaloir', 'Grille', 'Grille avaloir' ]:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(4)
        else:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(5)


        #self.propertieswdgDesordre.propertieswdgOBSERVATION2.updateObservationStackedWidget()
        self.propertieswdgDesordre.propertieswdgOBSERVATION.updateObservationStackedWidget()




    def fieldui2TypeOhChanged(self, comboindex):
        #print(self.toolwidgetmain_2.comboBox_typeOuvrageAss.currentText())
        currenttext = self.toolwidgetmain.comboBox_typeOuvrageAss.currentText()
        if currenttext in ['Regard','Avaloir', 'Grille']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
        elif currenttext in ['Poste de refoulement']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)
            """
            elif sys.version_info < (3, 0) and currenttext in ['Débourbeur/déshuileur'.decode('utf8')]:
                self.toolwidgetmain.stackedWidget.setCurrentIndex(2)
            elif sys.version_info > (3, 0) and currenttext in ['Débourbeur/déshuileur']:
                self.toolwidgetmain.stackedWidget.setCurrentIndex(2)
        """
        elif currenttext in [u'Débourbeur/déshuileur']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(2)
        else:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(3)

        #self.propertieswdgDesordre.propertieswdgOBSERVATION2.updateObservationStackedWidget()
        self.propertieswdgDesordre.propertieswdgOBSERVATION.updateObservationStackedWidget()


    def fieldui3TypeOhChanged(self, comboindex):
        #print(self.toolwidgetmain_2.comboBox_typeOuvrageAss.currentText())
        currenttext = self.toolwidgetmain.comboBox_typeOuvrageAss.currentText()
        if currenttext in ['Regard']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
        elif currenttext in ['']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)
        elif currenttext in [u'Ouvrage de régulation']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(2)
        elif currenttext in [u'Poste de refoulement']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(3)
        elif currenttext in [u'Avaloir']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(4)
        else:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(5)

        #self.propertieswdgDesordre.propertieswdgOBSERVATION2.updateObservationStackedWidget()
        self.propertieswdgDesordre.propertieswdgOBSERVATION.updateObservationStackedWidget()






    # def addGPSPoint(self):
    #     if self.gpsutil.currentpoint is None:
    #         self.windowdialog.errorMessage('GPS non connecte')
    #         return

    #     self.createorresetRubberband(0)

    #     layerpoint = self.gpsutil.currentpoint


    #     self.setTempGeometry([layerpoint],False)

    #     self.getGPSValue()



    def magicFunction(self):
        self.featureSelected()
        #self.lastPhoto()
        # self.addGPSPoint()
        self.toolbarGeomAddGPS()
        # self.saveFeature()
        self.toolbarSave()


    def getGPSValue(self):
        self.assignValue(self.toolwidgetmain.label_X, self.toolwidgetmain.doubleSpinBox_X)
        self.assignValue(self.toolwidgetmain.label_dX, self.toolwidgetmain.doubleSpinBox_dX)
        self.assignValue(self.toolwidgetmain.label_Y, self.toolwidgetmain.doubleSpinBox_Y)
        self.assignValue(self.toolwidgetmain.label_dY, self.toolwidgetmain.doubleSpinBox_dY)
        self.assignValue(self.toolwidgetmain.label_Z, self.toolwidgetmain.doubleSpinBox_Z)
        self.assignValue(self.toolwidgetmain.label_dZ, self.toolwidgetmain.doubleSpinBox_dZ)


    def assignValue(self,wdgfrom, wdgto):
        if self.isfloat(wdgfrom.text()):
            wdgto.setValue(float(wdgfrom.text()))

    def isfloat(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    # def postSaveFeature(self, boolnewfeature):
    def postSaveFeature(self, savedfeaturepk=None):
        self._createDeficiency(self.propertieswdgDesordre,savedfeaturepk)
        self._moveLinkedTopologicalEdge()

        if self.currentFeaturePK is not None and self.dbase.variante in ['2018_SNCF']:
            libelle=''
            sql = "SELECT nodetype,sewertype ,id_node  FROM Noeud WHERE pk_node = " + str(self.currentFeaturePK)
            typeouvrage, typereseau, idnoeud = self.dbase.query(sql)[0]
            if typeouvrage in ['60', '70', '71']:
                libelle += "R"
                if typereseau == 'PLU':
                    libelle += "P"
                elif typereseau == 'USE':
                    libelle += "V"
                elif typereseau == 'UNI':
                    libelle += "U"
                elif typereseau == 'IND':
                    libelle += "I"

            elif typeouvrage in ['10']:
                libelle += "POR"

            elif typeouvrage in ['22']:
                libelle += "FOS"
            elif typeouvrage in ['51']:
                libelle += "PUI"

            elif typeouvrage in ['21']:
                libelle += "DSH"

            else:
                libelle += "DIV"

            libelle += '_' + str(self.dbase.getValuesFromPk('node_qgis','id_node',self.currentFeaturePK ))

            pkobjet = self.dbase.getValuesFromPk('node_qgis','pk_object',self.currentFeaturePK )

            sql = "UPDATE object SET name = '" + libelle + "' WHERE pk_object = " + str(pkobjet)
            self.dbase.query(sql)
            self.toolwidgetmain.lineEdit_libelle.setText(libelle)



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_ud_node_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUI_2(QWidget):
    def __init__(self, parent=None):
        super(UserUI_2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_ud_node_tool_ui_2018SNCF.ui')
        uic.loadUi(uipath, self)

class UserUI_3(QWidget):
    def __init__(self, parent=None):
        super(UserUI_3, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_ud_node_noeud_tool_ui_CD41.ui')
        uic.loadUi(uipath, self)