from qgis.PyQt import uic, QtCore, QtWidgets

def tr(msg):
    # base3 = QtCore.QObject()
    # return base3.tr('Lamia',msg)
    return QtWidgets.QApplication.translate('Lamia',msg)