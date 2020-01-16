import sys
if sys.version_info.major == 3 :
    from PyQt5 import QtGui, QtCore, QtWidgets
else:
    from PyQt4 import QtGui, QtCore
    from PyQt4 import QtGui  as  QtWidgets

import sys, os



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

vbox = QtWidgets.QVBoxLayout()
mainWidget.setLayout(vbox)
if False:
    ComboBox = CheckableComboBox()
    button = QtWidgets.QPushButton()

    vbox.addWidget(ComboBox)
    vbox.addWidget(button)

table = QtWidgets.QTableWidget()

table.setRowCount(1)
table.clear()
table.setColumnCount(4)
header = table.horizontalHeader()

item = QtWidgets.QTableWidgetItem('ozfneoizef i jefpe féeo jfpée fié fpée f')
item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
table.setItem(0, 0, item)

wdg = QtWidgets.QTextBrowser()
wdg.setMinimumHeight(30)
wdg.setMaximumHeight(50)
# wdg.setPreferedHeight(50)
# wdg.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
wdg.setReadOnly(False)
table.setCellWidget(0, 3, wdg)


#table.resizeColumnsToContents()
table.setHorizontalHeaderLabels(['popo', 'pupu'])
table.setWordWrap(True)
table.resizeRowsToContents()
table.setColumnWidth(0, 100)






vbox.addWidget(table)



dialog.show()
sys.exit(app.exec_())