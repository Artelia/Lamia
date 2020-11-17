import logging
from ...AudioLogic.audioFactory import AudioFactory
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget
from PyQt5.QtCore import QSize
from ..Widgets.PlaybackWidget import PlaybackWidget

class PlayerWidget(QWidget):

    def __init__(self):        
        logging.debug("Player init")       
        super(PlayerWidget, self).__init__()
        self._system = AudioFactory.create("system")           
        # SETUP
        self._setup_recordinglist()
        self._setup_playbackwidget()
        self._setup_layout()

    def _setup_layout(self):
        self._layout = QVBoxLayout()
        self._layout.addWidget(self._recordinglist) 
        self._layout.addWidget(self._playbackwidget)
        self.setLayout(self._layout)           

    def _setup_recordinglist(self):
        self._recordinglist = QListWidget()
        self._reloadrecordinglist()
        self._recordinglist.itemClicked.connect(self.selectfile)

    def _setup_playbackwidget(self):
        self._playbackwidget = PlaybackWidget()
    
    def selectfile(self):
        self._playbackwidget.set_currfile(self._recordinglist.currentItem().text())

    def show(self):        
        self._reloadrecordinglist()      
        super().show()

    def _reloadrecordinglist(self):
        self._system.setsoundfiles()
        self._recordinglist.clear()
        for key in self._system.soundfiles:
            self._recordinglist.addItem(key)

        