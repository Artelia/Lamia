import logging, threading
from ..AudioLogic.deviceInterface import DeviceInterface
from ..AudioLogic.audioSystem import AudioSystem

class Player(DeviceInterface):          

    __instance = None

    #Need to put super(Recorder, self) for some reason, etiherwise it doens't really bring all the super class attributes
    def __init__(self):        
        super(Player, self).__init__()   
        self.loadsettings()
        self.event = threading.Event()     

    @staticmethod
    def getinstance():
        if Player.__instance is None:
            Player.__instance = Player()
        return Player.__instance

    def loadsettings(self):
        super().loadsettings()
        for it in self.configuration().devices:
            if it.type == "input":
                self().default.device = it.id
                self().default.channels = it.channels

    def play(self, file_name):
        """Play the given file using it's name, this fonction is supposely blocking
        """
        self.loadsettings()
        fs, data = self.audiosystem.read(file_name)        
        self().play(data= data, samplerate= fs)

    def getstream(self, file_name, callback=None):
        """Return a Stream, used to play the recording and still allow the user to stop the recording

            Return:
                Stream: An output Stream that can be stop and start and is more userfriendly

            Parameters:
                file_name: The name of the file (based on Recording naming fonction)
                callback: Allow to give a custom callback if needs is to            
        """
        self.loadsettings()        
        fs, data = self.audiosystem.read(file_name)
        
         # Default callback, can be modified to get the direct ouput or do some funky stuff with the stream
        if callback is None:
            def callback(output, frames, time, status):                
                currframe = self.i*frames
                if currframe < len(data):
                    high = currframe+frames
                    if high > len(data):
                        high = currframe+high-len(data)
                    low = currframe
                    output[:] = data[low:high]
                    self.i += 1                                                     
                else:
                    stream.stop()
                    self.i = 0

        self.i = 0        
        stream = self().OutputStream(callback=callback)
        return stream

