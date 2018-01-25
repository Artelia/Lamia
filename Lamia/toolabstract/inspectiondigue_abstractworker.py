# -*- coding: utf-8 -*-
from qgis.PyQt import QtXml, QtCore, QtGui


class AbstractWorker(QtCore.QObject):
    """Abstract worker, ihnerit from this and implement the work method"""

    # available signals to be used in the concrete worker
    finished = QtCore.pyqtSignal(object)
    error = QtCore.pyqtSignal(Exception)
    progress = QtCore.pyqtSignal(float)
    message = QtCore.pyqtSignal(str)
    toggle_show_progress = QtCore.pyqtSignal(bool)
    set_message = QtCore.pyqtSignal(str)
    toggle_show_cancel = QtCore.pyqtSignal(bool)

    # private signal, don't use in concrete workers this is automatically
    # emitted if the result is not None
    # successfully_finished = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QObject.__init__(self)
        self.killed = False

    def run(self):
        if False:
            result = self.work()
            self.finished.emit(result)


        if True:
            try:
                result = self.work()
                self.finished.emit(result)
            except Exception as e:
                # forward the exception upstream
                self.error.emit(e)
                self.finished.emit(None)

    def work(self):
        """ Reimplement this putting your calculation here
            available are:
                self.progress.emit(0-100)
                self.killed
            :returns a python object - use None if killed is true
        """

        raise NotImplementedError