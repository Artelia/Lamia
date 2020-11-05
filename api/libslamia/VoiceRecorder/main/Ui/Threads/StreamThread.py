import time, logging
from ..Controller.Mediator import Mediator
from PyQt5.QtCore import QThread
from ...AudioLogic.audioFactory import AudioFactory

class StreamThread(QThread):    

    def __init__(self, parent=None):
        super(StreamThread, self).__init__(parent)
        logging.debug("THREAD: Thread been created")      
        self._player = AudioFactory.create("player")
        self.running = True
        self._stream = None        
        # MEDIATOR
        self._mediator = Mediator.getinstance()
        self._mediator.connect("stream_start", self.start_stream)
        self._mediator.connect("stream_stop", self.stop_stream)   

    def run(self):
        logging.debug("THREAD: start the stream")                   
        while self._stream.active:
            pass
        logging.debug("THREAD: stop the stream")
        self._mediator.emit("stream_stop")

    def set_stream(self, file_name):        
        self._stream = self._player.getstream(file_name)

    def start_stream(self):        
        logging.debug("THREAD: Got order to start the stream")
        if self._stream.active == False:            
            self._stream.start()    
            self.start()                   

    def stop_stream(self):
        logging.debug("THREAD: Got order to stop the stream")      
        self._stream.stop()