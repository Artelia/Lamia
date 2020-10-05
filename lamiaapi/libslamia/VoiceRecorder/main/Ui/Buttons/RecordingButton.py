from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import Qt, QSize

class RecordingButton(QToolButton):

    def __init__(self, parent=None):
        super(RecordingButton, self).__init__(parent)        
        icon = QIcon()       
        icon.addPixmap(QPixmap(r"Lamia\toolgeneral\VoiceRecorder\main\Assets\recorder.svg"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap(r"Lamia\toolgeneral\VoiceRecorder\main\Assets\recorder_on.svg"), QIcon.Normal, QIcon.On)
        with open(r"Lamia\toolgeneral\VoiceRecorder\main\Assets\Blank_button.css") as stylesheet:            
            self.setStyleSheet(stylesheet.read())  
            self.setIcon(icon)
            self.setIconSize(QSize(90, 90))
            self.setCheckable(True)