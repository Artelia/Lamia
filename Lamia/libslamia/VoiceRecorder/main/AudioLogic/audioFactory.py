from ..AudioLogic.player import Player
from ..AudioLogic.recorder import Recorder
from ..AudioLogic.audioSystem import AudioSystem

class AudioFactory():

    @staticmethod
    def create(type):
        if type=="recorder":
            return Recorder.getinstance()
        if type=="player":
            return Player.getinstance()
        if type=="system":
            return AudioSystem.getinstance()