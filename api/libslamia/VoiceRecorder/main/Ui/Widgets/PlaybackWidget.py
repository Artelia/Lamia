import logging
from ..Buttons.PlayingButton import PlayingButton
from ..Threads.StreamThread import StreamThread
from ..Controller.Mediator import Mediator
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMessageBox
from PyQt5.QtCore import QSize, QThread

class PlaybackWidget(QWidget):

    def __init__(self):        
        logging.debug("Playback widget init")       
        super(PlaybackWidget, self).__init__()        
        self._currstream = None   
        # SETUP
        self._setup_playingbutton()
        self._setup_layout()
        # THREAD & MEDIATOR   
        self._streamthread = StreamThread()
        self._mediator = Mediator.getinstance()
        self._mediator.connect("stream_stop", self._stop)  
        # DIALOG BOX
        self.err_message = QMessageBox()
        self.err_message.setIcon(QMessageBox.Critical)
        self.err_message.setText("Error no files as been selected")
        self.err_message.setInformativeText('Please select a file')
        self.err_message.setWindowTitle("Error")

    def _setup_layout(self):
        self._layout = QHBoxLayout()
        self._layout.addWidget(self._playingbutton)     
        self.setLayout(self._layout)

    def _setup_playingbutton(self):
        self._playingbutton = PlayingButton()
        self._playingbutton.clicked.connect(self.play)   

    def set_currfile(self, file_name):
        logging.debug("PLAYBACK: File selected: " + file_name)
        self._currstream =  file_name      
        self._streamthread.set_stream(file_name)        

    def play(self):
        if self._currstream is not None:
            if self._playingbutton.isChecked():                                     
                self._mediator.emit("stream_start")
            else:            
                self._mediator.emit("stream_stop")
        else:
            self._playingbutton.setChecked(False)
            self.err_message.exec_()

    def _stop(self):
        logging.debug("PLAYBACK_WIDGET: Got order to pause button")             
        self._playingbutton.setChecked(False)