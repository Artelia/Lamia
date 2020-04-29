import sounddevice
from abc import abstractmethod
from ..Configuration.configuration import Configuration
from ..AudioLogic.audioSystem import AudioSystem

class DeviceInterface:

    _instance = None

    def __init__(self):      
        """ Init method shouldn't be directly use for classe instantiation
        """
        self.configuration = Configuration.getinstance()
        self.audiosystem = AudioSystem.getinstance()        
        
        if self._instance is not None:
            raise Exception("This class is a Singleton !")
        self._instance = self      

    def __call__(self):
        return sounddevice  

    @staticmethod
    @abstractmethod
    def getinstance():
        """Get and instance of the class, init one if it's not already done, should be only access point to the class

            Return:
                Cls: Return a classe intance if the classe already been instantiate
        """
        pass

    @abstractmethod
    def loadsettings(self):
        """Load the settings given by the configuration class
        """
        sounddevice.default.dtype = self.configuration().dtype
        sounddevice.default.samplerate = self.configuration().frequence