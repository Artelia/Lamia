import logging, time
from ..AudioLogic.deviceInterface import DeviceInterface
from ..AudioLogic.audioSystem import AudioSystem
from ..AudioLogic.recording import Recording

class Recorder(DeviceInterface):          

    __instance = None    

    #Need to put super(Recorder, self) for some reason, etiherwise it doens't really bring all the super class attributes
    def __init__(self):
        super(Recorder, self).__init__()
        self.loadsettings()
        self.currentrecording = None

    @staticmethod
    def getinstance():
        if Recorder.__instance is None:
            Recorder.__instance = Recorder()
        return Recorder.__instance

    def loadsettings(self):
        """Load the settings in the configuration file
        """        
        super().loadsettings()        
        for it in self.configuration().devices:
            if it.type == "output":
                self().default.device = it.id
                self().default.channels = it.channels
    
    def createrecording(self, recording_name=None):
        """Create a recording for the usage of the stream
        """
        return Recording(
            path=self.configuration().soundfiles_dir,
            channel=self().default.channels,
            dtype=self.configuration().dtype,
            extension_type=self.configuration().extension_type,
            name=recording_name
        )

    def record(self):
        """Record an audio file for the time set in the fonciguation file, nothing more, nothing less (not pratical)
        if you want a non-determine duration, use .getstream()

            Example:
                'recorder.record()'
        """
        self.loadsettings()
        self.currentrecording = self.createrecording()
        data = self().rec(int(self.configuration().duration * self.configuration().frequence))
        self.currentrecording.add(data)
        self.audiosystem.write(self.currentrecording)

    def getstream(self, recording_name=None):
        """Return a stream on which is written the audio input, the basic callback and final callback wrote 
        the output final in the directory defined in the configuration

            Parameters:
                recording_name: the name of the ouput file for the recording

            Return:
                Stream: A stream object which implement the basic streaming method
                Recording: an object which is the representaiton of the in going recording

            Example:
                'stream, recording = recorder.getstream()
                stream.start()
                time.sleep(10)
                stream.stop()
                log.info(recording.path + recording.name)
                '
        """      
        self.loadsettings()   
        self.currentrecording = self.createrecording(recording_name)                   
        # Default callback used heavily by the stream        
        def recording_callback(input, frames, time, status):
            self.currentrecording.add(input)


        # Default finish callback        
        def finished_callback() :
            self.currentrecording.applyfft()
            self.audiosystem.write(self.currentrecording)
                
        return self().InputStream(samplerate=self.configuration().frequence, callback=recording_callback, finished_callback=finished_callback), self.currentrecording

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    recorder = Recorder.getinstance()       

    t = 5

    stream, recording = recorder.getstream()
    stream.start()
    time.sleep(t)   
    stream.stop()
