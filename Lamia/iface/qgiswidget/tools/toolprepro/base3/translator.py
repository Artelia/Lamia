from qgis.PyQt import uic, QtCore, QtWidgets

class Translator(QtCore.QObject):
    def __init__(self):
        super().__init__()

    def translate(self,msg):
        # return self.tr(msg)
        return QtCore.QCoreApplication.translate('lamia', '%s'%(msg),None)


def tr(msg):
    # tranlsat = Translator()
    base3 = QtCore.QObject()
    return QtCore.QCoreApplication.translate('base3','Lamia',msg)
    # return tranlsat.translate(msg)
    # return QtCore.QT_TRANSLATE_NOOP('Lamia', msg)
    # return QtCore.QCoreApplication.translate('popo', msg, None)