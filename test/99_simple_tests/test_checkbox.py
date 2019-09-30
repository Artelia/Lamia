import sys
if sys.version_info.major == 3 :
    from PyQt5 import QtGui, QtCore, QtWidgets
else:
    from PyQt4 import QtGui, QtCore
    from PyQt4 import QtGui  as  QtWidgets

import sys, os


def actionbuutton():
    print('ko')
    print(ComboBox)
    for index in range(ComboBox.count()):
        print(ComboBox.itemText(index), ComboBox.model().item(index).checkState())



# subclass
class CheckableComboBox(QtWidgets.QComboBox):
    # once there is a checkState set, it is rendered
    # here we assume default Unchecked



    def addItem(self, item):
        super(CheckableComboBox, self).addItem(item)
        item = self.model().item(self.count()-1,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)

    """
    def itemChecked(self, index):
        print('checked')
        item = self.model().item(i,0)
        return item.checkState() == QtCore.Qt.Checked
    """


# the basic main()
app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QMainWindow()
mainWidget = QtWidgets.QWidget()
dialog.setCentralWidget(mainWidget)
ComboBox = CheckableComboBox(mainWidget)
button = QtGui.QPushButton(mainWidget)
button.clicked.connect(actionbuutton)
for i in range(6):
    ComboBox.addItem("Combobox Item " + str(i))

dialog.show()
sys.exit(app.exec_())