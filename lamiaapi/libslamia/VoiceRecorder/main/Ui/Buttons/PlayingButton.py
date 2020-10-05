from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import Qt, QSize

class PlayingButton(QToolButton):

    def __init__(self, parent=None):
        super(PlayingButton, self).__init__(parent)        
        icon = QIcon()       
        icon.addPixmap(QPixmap(r"src\main\Views\play.svg"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap(r"src\main\Views\pause.svg"), QIcon.Normal, QIcon.On)
        self.setStyleSheet(open(r"src\main\Views\Blank_button.css").read())
        self.setIcon(icon)
        self.setIconSize(QSize(75, 75))
        self.setCheckable(True)        