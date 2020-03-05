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

from qgis.PyQt import QtCore
from ...toolgeneral.VoiceRecorder.main.AudioLogic.audioFactory import AudioFactory
from ...toolgeneral.VoiceRecorder.main.Ui.Widgets.RecorderWidget import RecorderWidget
from ...toolgeneral.VoiceRecorder.main.Ui.Controller.Mediator import Mediator

import os, datetime, logging

log = logging.getLogger("Lamia")
class RecorderTool(RecorderWidget):

    def __init__(self, dbase, commentaire_id=None):
        self.dbase = dbase        
        self.mediator = Mediator.getinstance()
        self.recorder = AudioFactory.create("recorder")
        super(RecorderTool, self).__init__(self.recorder, self.mediator)
        self.mediator.connect("stream_stop", self.saveProperties)       
        
    def initProperties(self):
        pass

    def saveProperties(self):
        log.debug("Pas encore implémenté")
        # self.postSaveFeature()
        # self.createParentFeature()

    def postSaveFeature(self, boolnewfeature=False):
        #Mettre les fichiers audio dans le tmp
        currentrecording = self.recorder.currentrecording
        pkressource = self.dbase.getValuesFromPk('Audio_qgis', 'pk_ressource', self.dbase.currentFeaturePK)
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
