from ...lamia_abstractformtool import AbstractLamiaFormTool
import os
import datetime
from qgis.PyQt.QtWidgets import (QWidget)
from qgis.PyQt import uic, QtCore


class BaseAssainissementTestTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'Infralineaire'
    LOADFIRST = True

    tooltreewidgetCAT = 'abba'
    tooltreewidgetSUBCAT = 'Test'

    def __init__(self,**kwargs):
        super(BaseAssainissementTestTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        if self.dbase.variante in [None, 'Lamia','2018_SNCF']:
            #if self.userwdgfield is None:
            self.toolwidgetmain = UserUIField()
            self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                        'widgets': { 'typeReseau': self.toolwidgetmain.comboBox_typeReseau,
                                                                    'branchement': self.toolwidgetmain.comboBox_branch,
                                                                    'modeCirculation': self.toolwidgetmain.comboBox_typeecoul,
                                                                    'formecanalisation': self.toolwidgetmain.comboBox_formecana,

                                                                    'materiau': self.toolwidgetmain.comboBox_materiau,
                                                                    #'anPoseInf': self.toolwidgetmain.dateEdit_anneepose,


                                                                    'diametreNominal': self.toolwidgetmain.doubleSpinBox_diametreNominal,
                                                                    'hauteur': self.toolwidgetmain.doubleSpinBox_haut,
                                                                    # 'largeur': self.toolwidgetmain.doubleSpinBox_larg,

                                                                    # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAmont,
                                                                    # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAval,
                                                                    'profamont': self.toolwidgetmain.doubleSpinBox_profamont,
                                                                    'profaval': self.toolwidgetmain.doubleSpinBox_profaval,
                                                                    'lid_descriptionsystem_1': self.toolwidgetmain.spinBox_lk_noeud1,
                                                                    'lid_descriptionsystem_2': self.toolwidgetmain.spinBox_lk_noeud2
                                                                    }},
                                        'Objet': {'linkfield': 'id_objet',
                                                'widgets': {'commentaire':self.toolwidgetmain.textBrowser_commentaire}},
                                        'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                            'widgets': {
                                                                'annee_debut_pose': self.toolwidgetmain.dateEdit_anneepose,

                                                            }}}


        elif self.dbase.variante in ['CD41']:

            # if self.userwdgfield is None:
            self.toolwidgetmain = UserUIField_2()

            self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                        'widgets': {
                                                            'typeReseau': self.toolwidgetmain.comboBox_typeReseau,
                                                            'branchement': self.toolwidgetmain.comboBox_branch,

                                                            'domaine': self.toolwidgetmain.comboBox_domaine,
                                                            'implantation': self.toolwidgetmain.comboBox_implant,
                                                            'modeCirculation': self.toolwidgetmain.comboBox_typeecoul,
                                                            'fonctionCannAss': self.toolwidgetmain.comboBox_fonction,





                                                            'materiau': self.toolwidgetmain.comboBox_materiau,
                                                            # 'anPoseInf': self.toolwidgetmain.dateEdit_anneepose,

                                                            'diametreNominal': self.toolwidgetmain.doubleSpinBox_diametreNominal,
                                                            'hauteur': self.toolwidgetmain.doubleSpinBox_haut,
                                                            # 'largeur': self.toolwidgetmain.doubleSpinBox_larg,

                                                            # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAmont,
                                                            # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAval,
                                                            'profamont': self.toolwidgetmain.doubleSpinBox_profamont,
                                                            'profaval': self.toolwidgetmain.doubleSpinBox_profaval,
                                                            'lid_descriptionsystem_1': self.toolwidgetmain.spinBox_lk_noeud1,
                                                            'lid_descriptionsystem_2': self.toolwidgetmain.spinBox_lk_noeud2
                                                            }},
                                        'Objet': {'linkfield': 'id_objet',
                                                'widgets': {
                                                    'commentaire': self.toolwidgetmain.textBrowser_commentaire}},
                                        'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                            'widgets': {
                                                                'annee_debut_pose': self.toolwidgetmain.dateEdit_anneepose,

                                                            }}}


    def initAdvancedToolWidget(self):
        pass

class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)


class UserUIField_2(QWidget):
    def __init__(self, parent=None):
        super(UserUIField_2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_infralineaire_tool_ui_CD41.ui')
        uic.loadUi(uipath, self)