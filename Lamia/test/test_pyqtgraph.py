import qgis
from qgis.networkanalysis import *
from qgis.PyQt import QtGui, uic, QtCore, QtXml

# https://docs.qgis.org/2.18/en/docs/pyqgis_developer_cookbook/network_analysis.html

from InspectionDigueV2.src.libs import pyqtgraph as pg
from InspectionDigueV2.src.libs.pyqtgraph import exporters

app = QtGui.QApplication([])
plotWdg = pg.PlotWidget()

#plotWdg.show()


plotWdg.resize(500,200)
plotWdg.setVisible(True)
#QtGui.QApplication.processEvents()
#plotWdg.setWidth(500)
#plotWdg.repaint()
#plotWdg.setVisible(True)

plotWdg.plot([1,2],[2,2])

pitems = plotWdg.getPlotItem().listDataItems()
print(pitems)



plotWdg2 = pg.PlotWidget()
plotWdg2.resize(500,200)
pitems = plotWdg.getPlotItem().listDataItems()
for item in pitems:
    plotWdg2.addItem(item)




if True:
    exporter = exporters.ImageExporter(plotWdg2.scene())
    plotWdg2.setVisible(True)
    QtGui.QApplication.processEvents()
    exporter.export('C://test.jpg')

    plotWdg2.resize(500,500)
    plotWdg2.setVisible(True)
    QtGui.QApplication.processEvents()

    exporter = exporters.ImageExporter(plotWdg2.scene())
    exporter.export('C://test1.jpg')

# print(plotWdg.scene())
#app.exec_()


print('end')

