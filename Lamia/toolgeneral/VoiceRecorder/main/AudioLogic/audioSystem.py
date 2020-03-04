import os, logging
from scipy.io.wavfile import read,write
from ..Configuration.configuration import Configuration
from ..AudioLogic.recording import Recording

class AudioSystem():

    __instance = None

    #Implementing Singleton pattern
    def __init__(self):
        self.configuration = Configuration.getinstance()
        self.setsoundfiles()

        if self.__instance is not None:
            raise Exception("This class is a Singleton !")
        self.__instance = self  

    @staticmethod
    def getinstance():
        if AudioSystem.__instance is None:
            AudioSystem.__instance = AudioSystem()
        return AudioSystem.__instance
    
    def write(self, recording):
        filepath = recording.path + recording.name + recording.extension_type        
        write(filepath, int(self.configuration().frequence), recording())    

    def read(self, file_name):
        """Return the data and frame sampling from the readed file

            Return:
                Tuple: a tupe composed of the form (fs, data) fs been the sampling frame and data the actual numpy array of data

            Parameters:
                
        """        
        return read(self.soundfiles[file_name].path)

    def setsoundfiles(self):
        """Setter for the soundfiles, it's make a call to scanfiles() to make sure the recent files been added        
        """
        self.soundfiles = self.scanfiles()

    def scanfiles(self):
        """Scan for file based on the configuraiton set extenstion type and the give diretory

            Return:
                Dict: A dictionnary of Recording, using the Recording name as key
        """        
        record = None
        soundfiles = {}
        for file in os.listdir(self.configuration().soundfiles_dir):
            if file.endswith(self.configuration().extension_type):
                record = Recording.create(self.configuration().soundfiles_dir, file)                
                soundfiles[record.name] = record
        return soundfiles   