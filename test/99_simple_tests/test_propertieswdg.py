import sys
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)

import sys, os
from qgis.PyQt import uic, QtCore, QtWidgets

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__),'..', '..', 'Lamia', 'dialog' , 'InspectionDigue_propertieswidget.ui')
        uic.loadUi(uipath, self)




# the basic main()
app = QtWidgets.QApplication(sys.argv)

wdg = UserUI()
wdg.show()

wdg.frame_editing.setParent(None)

sys.exit(app.exec_())



#
# dialog = QtWidgets.QMainWindow()
# mainWidget = QtWidgets.QWidget()
# dialog.setCentralWidget(mainWidget)
#
# vbox = QtWidgets.QVBoxLayout()
# mainWidget.setLayout(vbox)
#
# ComboBox = CheckableComboBox()
# button = QtWidgets.QPushButton()
#
# vbox.addWidget(ComboBox)
# vbox.addWidget(button)
#
#
# if True:
#     for i in range(6):
#         ComboBox.addItem("Combobox Item " + str(i))
#
#
# if False:
#
#     model = QtGui.QStandardItemModel()
#     ComboBox.setModel(model)
#
#     view = QtWidgets.QTreeView()
#     view.header().hide()
#     view.setRootIsDecorated(False)
#     ComboBox.setView(view)
#
#
#
#     button.clicked.connect(actionbuutton)
#     for i in range(6):
#         #ComboBox.addItem("Combobox Item " + str(i))
#         text_item = QtGui.QStandardItem('111')
#         text_item2 = QtGui.QStandardItem('111')
#         model.appendRow([text_item,text_item2 ])
#         # ComboBox.model().insertRow(-1,'popo')
#
#
# #ComboBox.setModelColumn(3)
#
#
# dialog.show()
# sys.exit(app.exec_())