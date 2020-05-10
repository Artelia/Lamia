# -*- coding: utf-8 -*-
from qgis.PyQt import QtCore
from ...toolgeneral.VoiceRecorder.main.AudioLogic.audioFactory import AudioFactory
from ...toolgeneral.VoiceRecorder.main.Ui.Widgets.RecorderWidget import RecorderWidget
from ...toolgeneral.VoiceRecorder.main.Ui.Controller.Mediator import Mediator

import os, datetime, logging

log = logging.getLogger("Lamia")
class RecorderTool(RecorderWidget):

    def __init__(self, commentaire_id=None, parent=None):
        self.mediator = Mediator.getinstance()
        self.recorder = AudioFactory.create("recorder")        
        super(RecorderTool, self).__init__(self.recorder, self.mediator, parent)
        self.mediator.connect("stream_stop", self.saveAudiofile)
        self.parent = parent
        self.dbase = self.parent.dbase
        self.cursor = self.dbase.connSLITE.cursor()

    def saveAudiofile(self):
        self.postSaveFeature()
        # self.createParentFeature()

    def postSaveFeature(self, boolnewfeature=False):
        #Mettre les fichiers audio dans le tmp
        currentrecording = self.recorder.currentrecording
        pkressource = self.dbase.getValuesFromPk('Audio_qgis', 'pk_ressource', self.parent.currentFeaturePK)        

        querysql = """
        UPDATE Ressource 
        SET file = ? 
        WHERE pk_ressource = ?
        """
        queryvariables = (
            currentrecording.path + currentrecording.name + currentrecording.extension_type,
            pkressource
        )
        self.cursor.execute(querysql, queryvariables)
        self.dbase.connSLITE.commit()

    def createParentFeature(self):
        #Insertion dans la table des ressource de  du lien à l'objet
        #INSERT INTO Ressource (id_ressource, lpk_objet) VALUES( str(lastressourceid) , str(pkobjet))
        pkobjet = self.dbase.createNewObjet()
        lastressourceid = self.dbase.getLastId('Ressource') + 1        

        querysql = """ 
        INSERT INTO Ressource (id_ressource, lpk_objet)
        VALUES (?, ?)
        """
        queryvariables = (
            lastressourceid,
            pkobjet
        )
        self.cursor.execute(querysql, queryvariables)
        self.dbase.connSLITE.commit()

        pkressource = self.dbase.getLastRowId('Ressource')
        pkaudio = self.parent.currentFeaturePK
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
