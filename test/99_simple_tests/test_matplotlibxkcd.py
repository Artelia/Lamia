import sys
import time
#from matplotlib import pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('agg')

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib import pyplot as plt


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)
        self.addToolBar(NavigationToolbar(static_canvas, self))

        if False:
            dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            layout.addWidget(dynamic_canvas)
            self.addToolBar(QtCore.Qt.BottomToolBarArea,
                            NavigationToolbar(dynamic_canvas, self))

        #self.ax = static_canvas.figure.subplots()

        plt.xkcd()

        fig = static_canvas.figure


        if True:
            plt.xkcd()
            ax0 = fig.add_subplot(2, 2, 1)
            ax0.plot(np.sin(np.linspace(0, 10)))
            plt.title('Whoo Hoo!!!')

        if True:

            plt.rcdefaults()
            ax1 = fig.add_subplot(2, 2, 2)
            ax1.spines['right'].set_color('none')
            ax1.spines['top'].set_color('none')
            plt.xticks([])
            plt.yticks([])
            ax1.set_ylim([-30, 10])

            data = np.ones(100)
            data[70:] -= np.arange(30)

            ax1.annotate(
                'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
                xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))
            ax1.plot(data)
            #ax.xlabel('time')
            #ax.ylabel('my overall health')

        if True:
            plt.xkcd()
            ax2 = fig.add_subplot(2, 2, 3)
            ax2.bar([-0.125, 1.0 - 0.125], [0, 100], 0.25)
            ax2.spines['right'].set_color('none')
            ax2.spines['top'].set_color('none')
            ax2.xaxis.set_ticks_position('bottom')
            ax2.set_xticks([0, 1])
            ax2.set_xlim([-0.5, 1.5])
            ax2.set_ylim([0, 110])
            ax2.set_xticklabels(['CONFIRMED BY\nEXPERIMENT', 'REFUTED BY\nEXPERIMENT'])
            plt.yticks([])

            plt.title("CLAIMS OF SUPERNATURAL POWERS")




if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()