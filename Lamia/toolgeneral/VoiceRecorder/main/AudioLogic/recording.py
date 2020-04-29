import numpy, time, uuid, re, logging
import scipy
class Recording(object):

    # See on regexr.com to understand what's going on under the hood
    _regex = r"(^(?:-?\w+)+-\w+)-(\w+)(\.\w+)$"

    def __init__(self, path, channel, dtype, extension_type='.raw', name=None):
        """A smplie recording object holding a set of information and really ahndy when using the stream output

            Parameters: 
                Path: The direct path to the recording audio file
                Channel: The number of channel on which the file should be recorded
                Dtype: The data type use to record the file (float32, int32, int16, int8, etc...) used by Numpy mainly
                Extension_type: The format of the audiofile (usually .wav)
                Name: The name of the audio file, by default it would be a string such as yyyy-mm-dd-hhmm-%id%-%dtype% where
                    id: is a randomly generate uuid unique id
                    dtype: is the file dtype
        """       
        self.path = path
        self.channel = channel
        self.dtype = dtype
        self.extension_type = extension_type    
        self.name = name
        if self.name is None : 
            self.name = str(time.strftime("%Y-%m-%dT%H%M%S")) + "-" + str(uuid.uuid1(uuid.getnode()))[:8] + "-" + self.dtype
        self.data = numpy.ndarray(shape=(1,2), dtype=self.dtype)
    
    @classmethod
    def create(cls, path, file):
        """Is a second init using only the file path and the name of the file to dertermine all the necessayr information, useful when reading inputted files but not when creating some        
        """
        match = re.search(Recording._regex, file)
        return cls(
            path = path + file, 
            channel = None,
            dtype= match.group(2),
            extension_type= match.group(3),
            name= match.group(1)
        )

    def add(self, chunk):
        """Add a chunk of data to the numpy array, used mainly to get the input from the stream callback, see ``recorder.getstream()``
        """        
        self.data = numpy.append(self.data, chunk, axis=0)

    def applyfft(self):
        logging.debug(self.data)
        self.data[:] = numpy.fft.rfft(self.data)

    def __call__(self):
        """Usefull to get the Recording data

            Return:
                NumpyArray: return a 2D numpy array of the record data
        """      
        return self.data