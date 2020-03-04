import logging, time, sys
from.Controller.Controller import Controller
from .Controller.Mediator import Mediator
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QAction
from PyQt5.QtCore import Qt

log = logging.getLogger("Lamia")

class MainWindow(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        log.debug("Init MainWindow")
        """Create a new main window on which appear the menu bar and the controler loaded widgets"""
        super(MainWindow, self).__init__(parent)        
        # CONTROLLER & MEDIATOR
        self._controller = Controller()
        self._mediator = Mediator.getinstance()
        # SETUP
        self._setup_mainwindow()
        self._mediator.emit("switch_widget","recorder")
        self._setup_menu()

    def _setup_mainwindow(self):        
        self.setWindowTitle('Voice recorder')
        self.setMinimumSize(200, 280)
        # LAYOUT
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignCenter)
        for widget in self._controller.widgets.values():
            self._layout.addWidget(widget)
        # CENTRAL WIDGET
        self._centralWidget = QWidget()
        self._centralWidget.setLayout(self._layout)
        self.setCentralWidget(self._centralWidget)

    def _setup_menu(self):
        # Add menu on the menu bar
        self._menubar = self.menuBar()
        self._recorder_menu = self._menubar.addMenu('Menu')            
        self._recorder_menu.addAction("Recorder").triggered.connect(lambda: self._controller.switch_widget("recorder")) 
        # self._recorder_menu.addAction("Player").triggered.connect(lambda: self._controller.switch_widget("player"))

    @staticmethod
    def run():
        """Main function."""
        # Create an instance of QApplication
        app = QApplication(sys.argv)
        # Show the main window
        view = MainWindow()
        view.show()
        # Execute the main loop
        sys.exit(app.exec_())

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    # Show the main window
    view = MainWindow().run()
    view.show()
    # Execute the main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)    
    main()
        