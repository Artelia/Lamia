import logging
from PyQt5.QtCore import QObject, pyqtSignal

log = logging.getLogger("AudioRecord")
class Mediator(QObject):

    stream_stop = pyqtSignal(name="stream_stop")
    stream_start = pyqtSignal(name="stream_start")
    switch_widget = pyqtSignal(str, name="switch_widget")

    _instance = None

    def __init__(self, parent=None):
        super(Mediator, self).__init__()
        if self._instance is not None:
            raise Exception("This class is a Singleton !")
        self._instance = self
        log.debug("Mediator initialized")
        
        self._signals = {
            "stream_stop": self.stream_stop,
            "stream_start": self.stream_start
        }

    @staticmethod
    def getinstance():        
        if(Mediator._instance is None):            
            Mediator._instance = Mediator()
        return Mediator._instance

    def emit(self, signal_name, *args):
        log.debug("SIGNAL: emit signal: " + signal_name + " - args: " + str(*args))
        self._signals[signal_name].emit(*args)

    def connect(self, signal_name, function):        
        self._signals[signal_name].connect(function)