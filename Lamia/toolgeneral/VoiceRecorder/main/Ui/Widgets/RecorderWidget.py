import logging
from ...AudioLogic.audioFactory import AudioFactory
from ..Buttons.RecordingButton import RecordingButton
from ..Controller.Mediator import Mediator
from qgis.PyQt.QtWidgets import QWidget, QHBoxLayout
from qgis.PyQt.QtCore import QSize

log = logging.getLogger("AudioRecord")
class RecorderWidget(QWidget):

    def __init__(self, recorder, mediator, parent=None):        
        super(RecorderWidget, self).__init__(parent)
        log.debug("Recorder initialized")
        self._recorder = recorder
        # SETUP        
        self._setup_recordingButton()
        self._setup_layout()
        #Mediator
        self._mediator = mediator

    def _setup_layout(self):
        self._layout = QHBoxLayout()
        self._layout.addWidget(self._recordingButton)
        self.setLayout(self._layout)

    def _setup_recordingButton(self):
        self._recordingButton = RecordingButton()
        self._recordingButton.clicked.connect(self.record)        

    def _start_recording(self):
        log.debug("Start recording")
        self.stream, _ = self._recorder.getstream()
        self._mediator.emit("stream_start")
        self.stream.start()

    def _stop_recording(self):
        log.debug("Stop recording")
        self.stream.stop()
        self._mediator.emit("stream_stop")    

    def record(self):        
        if self._recordingButton.isChecked():             
            self._start_recording()
        else:
            self._stop_recording()
            