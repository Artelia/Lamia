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
from ..base2.lamiabase_noeud_tool import BaseNoeudTool

from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
from .lamiabaseassainissement_croquis_tool import BaseAssainissementCroquisTool as BaseCroquisTool
from .lamiabaseassainissement_desordre_tool import BaseAssainissementDesordreTool
from .lamiabaseassainissement_equipement_tool import BaseAssainissementEquipementTool




class BaseAssainissementNoeudTool(BaseNoeudTool):

    DBASETABLENAME = 'Noeud'
    LOADFIRST = True

    tooltreewidgetCAT = 'Description'
    tooltreewidgetSUBCAT = 'Noeud'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__),'..','base2', 'lamiabase_noeud_tool_icon.svg')


    def __init__(self, **kwargs):
        super(BaseAssainissementNoeudTool, self).__init__(**kwargs)
        #self.instancekwargs = kwargs

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Noeud'
        self.dbasetablename = 'Noeud'
        self.visualmode = [0, 1, 2]
        self.PointENABLED = True
        # self.LineENABLED = False
        # self.PolygonENABLED = True
        self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__),'..','base2', 'lamiabase_noeud_tool_icon.svg')
        self.linkedgeom = [['Equipement', 'lid_descriptionsystem_1'],['Desordre', 'lid_descriptionsystem']]

        # ****************************************************************************************
        #properties ui
        pass
    """


    def initMainToolWidget(self):

        if self.dbase.variante in [None, 'Lamia']:

            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {'Noeud' : {'linkfield' : 'id_noeud',
                                                'widgets' : {
                                                            'typeReseau': self.toolwidgetmain.comboBox_typeReseau,
                                                        'environnement' : self.toolwidgetmain.comboBox_environnement,
                                                            'typeOuvrageAss': self.toolwidgetmain.comboBox_typeOuvrageAss,
                                                            'soustypeOuvrageAss': self.toolwidgetmain.comboBox_soustype,
                                                        'tampon_forme': self.toolwidgetmain.comboBox_Formetampon,
                                                            'accessibilite': self.toolwidgetmain.comboBox_accessibilite,

                                                        #regard
                                                        'presenceechelon' : self.toolwidgetmain.comboBox_echelon,
                                                        'presencecrosse': self.toolwidgetmain.comboBox_crosse,
                                                            'presencecunette': self.toolwidgetmain.comboBox_cunette,
                                                        'regard_forme': self.toolwidgetmain.comboBox_formeregard,
                                                        'regard_materiau': self.toolwidgetmain.comboBox_regmat,

                                                        #branchement
                                                            'cloisonsiphoide': self.toolwidgetmain.comboBox_cloisonsiphoide,
                                                            'couvercle': self.toolwidgetmain.comboBox_couvercle,
                                                        'type_usager': self.toolwidgetmain.comboBox_typeusager,

                                                        #avaloir
                                                        'decantation': self.toolwidgetmain.comboBox_decant,

                                                        #PR
                                                        'PRcloture': self.toolwidgetmain.comboBox_cloture,
                                                        'PRverouille': self.toolwidgetmain.comboBox_verouille,
                                                            'PRtraitHdeuxs': self.toolwidgetmain.comboBox_h2s,

                                                        'PRarmoireelec': self.toolwidgetmain.comboBox_posteelec,
                                                            'PRarmoireelecverouillee': self.toolwidgetmain.comboBox_armoire_verouille,
                                                        'PRtelegestion': [self.toolwidgetmain.comboBox_telegestion,self.toolwidgetmain.comboBox_DSHalarme],
                                                        'PRtelegestioncommentaire': self.toolwidgetmain.textBrowser_telegestioncom,
                                                        'PRpermutautopompe': self.toolwidgetmain.comboBox_permut_pompes,

                                                        'PRmateriau': [self.toolwidgetmain.comboBox_PRmateriau,self.toolwidgetmain.comboBox_DSH_materiau],
                                                        'PRgrilleantichute': self.toolwidgetmain.comboBox_antichute,
                                                        'PRpanierdegrilleur': self.toolwidgetmain.comboBox_panierdegrileur,

                                                            'PRtypeasservissementpompe': self.toolwidgetmain.comboBox_typeasservissement,
                                                            'PRnbrepoires': self.toolwidgetmain.spinBox_poires,
                                                            'PRsurverse': self.toolwidgetmain.comboBox_surverse,

                                                        'PRpompebarreguidage': self.toolwidgetmain.comboBox_barrresguidage,
                                                        'PRpompechainerelevage': self.toolwidgetmain.comboBox_pompe_relevage,
                                                            'PRnbrepompes': self.toolwidgetmain.spinBox_pompes,

                                                        'PRclapet': self.toolwidgetmain.comboBox_vanne_clapet,
                                                        'PRvannes': self.toolwidgetmain.comboBox_vanne_vanne,
                                                        'PRprisepression': self.toolwidgetmain.comboBox_vanne_prisepression,

                                                        #DSH
                                                        # DSH materiau : self.toolwidgetmain_2.comboBox_DSH_materiau cf PR
                                                        #'DSHpresencealarme': self.toolwidgetmain_2.comboBox_DSHalarme,
                                                            'presenceautomate': self.toolwidgetmain.comboBox_automate,


                                                        # autre
                                                        'profradierouvrage': self.toolwidgetmain.doubleSpinBox_profradierouvrage,
                                                            'largeur': self.toolwidgetmain.doubleSpinBox_largeur,
                                                            'longueur': self.toolwidgetmain.doubleSpinBox_longueur,

                                                            'X': self.toolwidgetmain.doubleSpinBox_X,
                                                            'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                            'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                            'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                            'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                            'dZ': self.toolwidgetmain.doubleSpinBox_dZ,


                                                        }},
                                'Objet' : {'linkfield' : 'id_objet',
                                            'widgets' : {'commentaire' : self.toolwidgetmain.textBrowser_commentaire}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
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
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgDesordre = BaseAssainissementDesordreTool(**self.instancekwargs)
            self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            self.propertieswdgDesordre.groupBox_elements.setParent(None)
            self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)

            self.propertieswdgEquipement = BaseAssainissementEquipementTool(**self.instancekwargs)
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
            self.formtoolwidgetconfdictmain = {'Noeud': {'linkfield': 'id_noeud',
                                                    'widgets': {
                                                        'typeReseau': self.toolwidgetmain.comboBox_typeReseau,
                                                        'environnement': self.toolwidgetmain.comboBox_environnement,
                                                        'typeOuvrageAss': self.toolwidgetmain.comboBox_typeOuvrageAss,
                                                        'tampon_forme': self.toolwidgetmain.comboBox_Formetampon,
                                                        'accessibilite': self.toolwidgetmain.comboBox_accessibilite,

                                                        # regard
                                                        'presenceechelon': self.toolwidgetmain.comboBox_echelon,
                                                        'presencecrosse': self.toolwidgetmain.comboBox_crosse,
                                                        # 'presencecunette': self.toolwidgetmain.comboBox_cunette,
                                                        'regard_forme': self.toolwidgetmain.comboBox_formeregard,
                                                        # 'formeregard': self.toolwidgetmain.comboBox_formeregard,



                                                        # branchement
                                                        # 'cloisonsiphoide': self.toolwidgetmain.comboBox_cloisonsiphoide,
                                                        # 'couvercle': self.toolwidgetmain.comboBox_couvercle,

                                                        # PR
                                                        # 'PRcloture': self.toolwidgetmain.comboBox_cloture,
                                                        # 'PRverouille': self.toolwidgetmain.comboBox_verouille,

                                                        'PRarmoireelec': self.toolwidgetmain.comboBox_posteelec,
                                                        # 'PRarmoireelecverouillee': self.toolwidgetmain.comboBox_armoire_verouille,
                                                        'PRtelegestion': [self.toolwidgetmain.comboBox_telegestion,
                                                                        self.toolwidgetmain.comboBox_DSHalarme],
                                                        'PRtelegestioncommentaire': self.toolwidgetmain.textBrowser_telegestioncom,
                                                        # 'PRpermutautopompe': self.toolwidgetmain.comboBox_permut_pompes,

                                                        'PRmateriau': [self.toolwidgetmain.comboBox_PRmateriau,
                                                                    self.toolwidgetmain.comboBox_DSH_materiau],
                                                        # 'PRgrilleantichute': self.toolwidgetmain.comboBox_antichute,
                                                        # 'PRpanierdegrilleur': self.toolwidgetmain.comboBox_panierdegrileur,
                                                        'PRtypeasservissementpompe': self.toolwidgetmain.comboBox_typeasservissement,
                                                        'PRnbrepoires': self.toolwidgetmain.spinBox_poires,
                                                        'PRsurverse': self.toolwidgetmain.comboBox_surverse,

                                                        # 'PRpompebarreguidage': self.toolwidgetmain.comboBox_barrresguidage,
                                                        # 'PRpompechainerelevage': self.toolwidgetmain.comboBox_pompe_relevage,
                                                        'PRnbrepompes': self.toolwidgetmain.spinBox_pompes,

                                                        # 'PRclapet': self.toolwidgetmain.comboBox_vanne_clapet,
                                                        # 'PRvannes': self.toolwidgetmain.comboBox_vanne_vanne,
                                                        # 'PRprisepression': self.toolwidgetmain.comboBox_vanne_prisepression,

                                                        # DSH
                                                        # DSH materiau : self.toolwidgetmain.comboBox_DSH_materiau cf PR
                                                        # 'DSHpresencealarme': self.toolwidgetmain.comboBox_DSHalarme,
                                                        'presenceautomate': self.toolwidgetmain.comboBox_automate,

                                                        # autre
                                                        'profradierouvrage': self.toolwidgetmain.doubleSpinBox_profradierouvrage,
                                                        'largeur': self.toolwidgetmain.doubleSpinBox_largeur,
                                                        'longueur': self.toolwidgetmain.doubleSpinBox_longueur,

                                                        'X': self.toolwidgetmain.doubleSpinBox_X,
                                                        'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                        'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                        'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                        'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                        'dZ': self.toolwidgetmain.doubleSpinBox_dZ,

                                                    }},
                                        'Objet': {'linkfield': 'id_objet',
                                                    'widgets': {'libelle': self.toolwidgetmain.lineEdit_libelle,
                                                                'commentaire': self.toolwidgetmain.textBrowser_commentaire}},
                                        'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
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
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgDesordre = BaseAssainissementDesordreTool(**self.instancekwargs)
            #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            #self.propertieswdgDesordre.groupBox_elements.setParent(None)
            #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            #self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)

            self.propertieswdgEquipement = BaseAssainissementEquipementTool(**self.instancekwargs)
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

            #self.dbase.dbasetables['Noeud']['fields']['typeOuvrageAss']['Cst'] = self.modifiedtypeohassdict


        elif self.dbase.variante in ['CD41']:

            self.toolwidgetmain = UserUI_3()
            self.formtoolwidgetconfdictmain = {'Noeud': {'linkfield': 'id_noeud',
                                                    'widgets': {
                                                        'domaine': self.toolwidgetmain.comboBox_domaine,
                                                        'typeReseau': self.toolwidgetmain.comboBox_typeReseau,
                                                        'environnement': self.toolwidgetmain.comboBox_environnement,
                                                        'typeOuvrageAss': self.toolwidgetmain.comboBox_typeOuvrageAss,
                                                        'soustypeOuvrageAss': self.toolwidgetmain.comboBox_soustype,


                                                        # regard
                                                        'accessibilite': [self.toolwidgetmain.comboBox_accessibilite,
                                                                        self.toolwidgetmain.comboBox_accessibilite2],
                                                        'regard_materiau': self.toolwidgetmain.comboBox_reg_materiau,
                                                            # diam_regard : longeur
                                                        'tampon_type': self.toolwidgetmain.comboBox_typetampon,
                                                        'tampon_diam': self.toolwidgetmain.doubleSpinBox_diamtampon,
                                                        'presenceechelon': self.toolwidgetmain.comboBox_echelon,


                                                    # Equipement

                                                        #ouvrage de regul
                                                        'PRtelegestion': self.toolwidgetmain.comboBox_telegestion_2,
                                                        'prof01': self.toolwidgetmain.comboBox_telegestion_2,


                                                        #PR
                                                        'Prcapacitenominale': self.toolwidgetmain.doubleSpinBox_capanom,
                                                        'PRnbrepompes': self.toolwidgetmain.spinBox_pompes2,
                                                        'PRtraitHdeuxs': self.toolwidgetmain.comboBox_traithdeuxs,
                                                        'PRsurverse': self.toolwidgetmain.comboBox_surverse2,

                                                        #avaloir
                                                        'decantation': self.toolwidgetmain.comboBox_decant,
                                                        #dimgrille : longeur


                                                        # autre
                                                        'profradierouvrage': self.toolwidgetmain.doubleSpinBox_profradierouvrage,
                                                        'largeur': self.toolwidgetmain.doubleSpinBox_largeur,
                                                        'longueur': self.toolwidgetmain.doubleSpinBox_longueur,

                                                        'X': self.toolwidgetmain.doubleSpinBox_X,
                                                        'dX': self.toolwidgetmain.doubleSpinBox_dX,
                                                        'Y': self.toolwidgetmain.doubleSpinBox_Y,
                                                        'dY': self.toolwidgetmain.doubleSpinBox_dY,
                                                        'Z': self.toolwidgetmain.doubleSpinBox_Z,
                                                        'dZ': self.toolwidgetmain.doubleSpinBox_dZ,

                                                    }},
                                        'Objet': {'linkfield': 'id_objet',
                                                    'widgets': {
                                                                'commentaire': self.toolwidgetmain.textBrowser_commentaire
                                                            }},
                                        'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
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
            self.propertieswdgDesordre = BaseAssainissementDesordreTool(**self.instancekwargs)
            self.propertieswdgDesordre.initMainToolWidget()
            #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            #self.propertieswdgDesordre.groupBox_elements.setParent(None)
            #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            #self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)

            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
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






    def addGPSPoint(self):
        if self.gpsutil.currentpoint is None:
            self.windowdialog.errorMessage('GPS non connecte')
            return

        self.createorresetRubberband(0)

        layerpoint = self.gpsutil.currentpoint


        self.setTempGeometry([layerpoint],False)

        self.getGPSValue()



    def magicFunction(self):
        self.featureSelected()
        #self.lastPhoto()
        self.addGPSPoint()
        self.saveFeature()


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
        print('**********', 'postSaveFeature', self.currentFeaturePK)
        if self.currentFeaturePK is None :  #very new equip, not newversion
            self.propertieswdgDesordre.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('Noeud_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)
            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
            qgsgeomfordesordre = [qgsgeom,qgsgeom]
            self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)
            self.propertieswdgDesordre.parentWidget.currentFeaturePK = savedfeaturepk
            self.propertieswdgDesordre.toolbarSave()
            pkdesordre = self.propertieswdgDesordre.currentFeaturePK
            sql = "UPDATE Desordre SET groupedesordre = 'NOD' WHERE pk_desordre = {}".format(pkdesordre)
            print(sql)
            self.dbase.query(sql)


        #adapt linked infralin geoemtry
        if self.currentFeaturePK is not None:
            nodeiddessys = self.dbase.getValuesFromPk('Noeud_qgis',['id_descriptionsystem'],self.currentFeaturePK )
            # nodegeom = self.currentFeature.geometry().asPoint()
            nodegeom = self.formutils.getQgsGeomFromPk(self.currentFeaturePK).asPoint()

            # iterate on lid_descriptionsystem_1 and lid_descriptionsystem_2
            valuetoiterate = [1, 2]
            for indexnode in valuetoiterate:
                #sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_qgis "
                #sql += "WHERE lid_descriptionsystem_" + str(indexnode ) + " = " + str(nodeiddessys)
                #sql += " AND "
                #sql += self.dbase.dateVersionConstraintSQL()
                sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_now "\
                      "WHERE lid_descriptionsystem_{} = {} ".format(str(indexnode ),
                                                                    str(nodeiddessys))
                sql = self.dbase.sqlNow(sql)
                result = self.dbase.query(sql)
                if indexnode == 1 :
                    indexgeom = 0
                elif indexnode == 2:
                    indexgeom = -1

                for fetpk, fetid in result:
                    infrafet = self.dbase.getLayerFeatureByPk('Infralineaire', fetpk)
                    infrafetgeom = infrafet.geometry().asPolyline()

                    if not self.dbase.areNodesEquals(infrafetgeom[indexgeom], nodegeom):
                        self.dbase.createNewLineVersion('Infralineaire', fetpk)
                        fetpk = self.dbase.getLayerFeatureById('Infralineaire', fetid).id()
                        infrafetgeom[indexgeom] = nodegeom
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            newgeom = qgis.core.QgsGeometry.fromPolyline(infrafetgeom)
                        else:
                            newgeom = qgis.core.QgsGeometry.fromPolylineXY(infrafetgeom)
                        dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
                        dbasetablelayer.startEditing()
                        success = dbasetablelayer.changeGeometry(fetpk, newgeom)
                        dbasetablelayer.commitChanges()
                        # move branchement
                        self.moveBranchement(fetpk, newgeom)


        #self.dbase.dbasetables['Infralineaire']['layerqgis'].triggerRepaint()
        self.mainifacewidget.qgiscanvas.layers['Infralineaire']['layerqgis'].triggerRepaint()
        
        #if self.savingnewfeature and not self.savingnewfeatureVersion:



        """
        if self.currentFeaturePK != savedfeaturepk: # save a disorder on first creation
            pkobjet = self.dbase.createNewObjet()
            # lastiddesordre = self.dbase.getLastId('Desordre') + 1
            lastiddesordre = self.dbase.getmaxColumnValue('Desordre', 'id_desordre') + 1
            geomtext, iddessys = self.dbase.getValuesFromPk('Noeud_qgis',
                                                            ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                            savedfeaturepk)
            qgsgeom = self.tempgeometry
            #qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext)
            newgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(), qgsgeom.asPoint()])
            newgeomwkt = newgeom.asWkt()

            sql = self.dbase.createSetValueSentence(type='INSERT',
                                                    tablename='Desordre',
                                                    listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                'lid_descriptionsystem', 'geom'],
                                                    listofrawvalues=[lastiddesordre, pkobjet, 'NOD',
                                                                    iddessys, newgeomwkt])
            self.dbase.query(sql)
        """
        if self.currentFeaturePK is not None:
            #if  hasattr(self, 'userwdgfield_2') and self.userwdg == self.toolwidgetmain_2:
            if self.dbase.variante in ['2018_SNCF'] :
                libelle=''
                sql = "SELECT typeOuvrageAss,typeReseau ,id_noeud  FROM Noeud WHERE pk_noeud = " + str(self.currentFeaturePK)
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

                libelle += '_' + str(self.dbase.getValuesFromPk('Noeud_qgis','id_noeud',self.currentFeaturePK ))

                pkobjet = self.dbase.getValuesFromPk('Noeud_qgis','pk_objet',self.currentFeaturePK )

                sql = "UPDATE Objet SET libelle = '" + libelle + "' WHERE pk_objet = " + str(pkobjet)
                self.dbase.query(sql)
                self.toolwidgetmain.lineEdit_libelle.setText(libelle)




    def moveBranchement(self, pkinfralin, newgeom):

        fetiddessys = self.dbase.getValuesFromPk('Infralineaire_qgis', 'id_descriptionsystem', pkinfralin)
        dbasetablelayer = self.dbase.dbasetables['Infralineaire']['layer']
        print('moveBranchement1', pkinfralin, fetiddessys)
        # sql = "SELECT id_infralineaire FROM Infralineaire WHERE lk_descriptionsystem2 = " + str(infrafet['id_descriptionsystem'])
        #sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_qgis WHERE lid_descriptionsystem_2 = " + str( fetiddessys)
        #sql += " AND "
        #sql += self.dbase.dateVersionConstraintSQL()
        sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_now "\
              " WHERE lid_descriptionsystem_2 = {} ".format( str(fetiddessys))
        sql = self.dbase.sqlNow(sql)
        # query = self.dbase.query(sql)
        # result2 = [row[0] for row in query]
        result2 = self.dbase.query(sql)
        # for fetid2 in result2:
        for fetpk2, fetid2 in result2:
            print('moveBranchement2',fetpk2,fetid2 )
            # infrafet = self.dbase.getLayerFeatureById('Infralineaire', fetid2)
            self.dbase.createNewLineVersion('Infralineaire', fetpk2)
            fetpk2 = self.dbase.getLayerFeatureById('Infralineaire', fetid2).id()
            infrafet = self.dbase.getLayerFeatureByPk('Infralineaire', fetpk2)
            if sys.version_info.major == 2:
                infrafetpoint1 = qgis.core.QgsGeometry().fromPoint(infrafet.geometry().asPolyline()[0])
            elif sys.version_info.major == 3:
                infrafetpoint1 = qgis.core.QgsGeometry().fromPointXY(infrafet.geometry().asPolyline()[0])
            # newgeom2 = newgeom.shortestLine(infrafetpoint1)
            newgeom2 = infrafetpoint1.shortestLine(newgeom)
            dbasetablelayer.startEditing()
            success = dbasetablelayer.changeGeometry(fetpk2, newgeom2)
            dbasetablelayer.commitChanges()


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUI_2(QWidget):
    def __init__(self, parent=None):
        super(UserUI_2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_noeud_tool_ui_2018SNCF.ui')
        uic.loadUi(uipath, self)

class UserUI_3(QWidget):
    def __init__(self, parent=None):
        super(UserUI_3, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_noeud_tool_ui_CD41.ui')
        uic.loadUi(uipath, self)