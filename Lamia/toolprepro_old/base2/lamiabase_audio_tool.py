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




from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QVBoxLayout)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QVBoxLayout)
from qgis.PyQt.QtCore import Qt
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os, logging
import datetime
import glob

from ...toolgeneral.VoiceRecorder.main.AudioLogic.audioFactory import AudioFactory
from ...toolgeneral.VoiceRecorder.main.Ui.Widgets.RecorderWidget import RecorderWidget
from ...toolgeneral.VoiceRecorder.main.Ui.Controller.Mediator import Mediator

import sys

log = logging.getLogger("Lamia")
class BaseAudioTool(AbstractLamiaTool):    
    LOADFIRST = False
    dbasetablename = 'Audio'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseAudioTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
        self.parentwidget = parentwidget
        log.debug(self.parentwidget)

    def initTool(self):      
        # ****************************************************************************************
        # Main spec
        log.debug("init audio tool")
        self.CAT = 'Ressources'
        self.NAME = 'Audio'
        self.dbasetablename = 'Audio'
        self.visualmode = [ 1, 2]        
        self.linkgespec = {            
            'Tcobjetressource' : {
                'tabletc' : 'Tcobjetressource',
                'idsource' : 'lpk_ressource',
                'idtcsource' : 'lid_ressource',
                'iddest' : 'id_objet',
                'idtcdest' : 'lid_objet',
                'desttable' : [
                    'Infralineaire',
                    'Observation',
                    'Equipement',
                    'Noeud',
                    'Profil'
                ]
            } 
        }
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_photo_tool_icon.svg')        

        # ****************************************************************************************
        #properties ui        

        # ****************************************************************************************
        # userui
        # self.dbase.dbaseressourcesdirectory

    def initFieldUI(self):        
        if self.userwdgfield is None:
            log.debug("init field UI")            
            self.recorder = AudioFactory.create("recorder")                             
            self.mediator = Mediator.getinstance()
            self.mediator.connect("stream_stop", self.saveFeature)            
            self.userwdgfield = UserUI(RecorderWidget(self.recorder, self.mediator))            

            self.linkuserwdgfield = { 
                "Audio":{ 
                    "linkfield":"id_photo",
                    "widgets":{ 

                    }
                },
                "Objet":{ 
                    "linkfield":"id_objet",
                    "widgets":{ 

                    }
                },
                "Ressource":{ 
                    "linkfield":"id_ressource",
                    "widgets":{ 

                    }
                }
            }

    def postInitFeatureProperties(self, feat):
        pass


    def postSaveFeature(self, boolnewfeature):
        #Mettre les fichiers audio dans le tmp
        currentrecording = self.recorder.currentrecording
        pkressource = self.dbase.getValuesFromPk('Audio_qgis', 'pk_ressource', self.currentFeaturePK)
        sqlquery = (
            "UPDATE Ressource "
            "SET file = '{0}' "
            "WHERE pk_ressource = {1}"
        ).format(
            currentrecording.path + currentrecording.name + currentrecording.extension_type,
            pkressource
        )

        self.dbase.query(sqlquery)
        self.dbase.commit()
    
    def createParentFeature(self):
        #Insertion dans la table des ressource de  du lien à l'objet
        #INSERT INTO Ressource (id_ressource, lpk_objet) VALUES( str(lastressourceid) , str(pkobjet))
        pkobjet = self.dbase.createNewObjet()
        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sqlquery = (
            "INSERT INTO Ressource (id_ressource, lpk_objet) "
            "VALUES ( {0}, {1})"
        ).format(
            lastressourceid,
            pkobjet
        )        
        self.dbase.query(sqlquery)
        self.dbase.commit()

        pkressource = self.dbase.getLastRowId('Ressource')
        pkaudio = self.currentFeaturePK
        lastidaudio = self.dbase.getLastId('Audio') + 1
        
        # Liaison de l'objet (ici de l'audio) à l'entrée précédente de la table ressource
        # UPDATE Audio SET id_audio = str(lastidaudio) ,lpk_ressource = str(pkres) WHERE pk_audio = str(pkaudio)
        sqlquery = (
            "UPDATE Audio SET id_audio = {0}, lpk_ressource = {1} "
            "WHERE pk_audio = {2}"
        ).format(
            lastidaudio,
            pkressource,
            pkaudio
        )        
        self.dbase.query(sqlquery)
        self.dbase.commit()

        # Ajout de de l'id du widget parent dans la table audio, pour faire le lier entre les fichier wav et les champs de text
        log.debug(self.parentwidget)

class UserUI(QWidget):

    def __init__(self, widget, parent=None):
        super(UserUI, self).__init__(parent=parent)
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignCenter)
        self._layout.addWidget(widget)
        self.setLayout(self._layout)        

