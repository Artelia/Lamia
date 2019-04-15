# -*- coding: utf-8 -*-
"""
This example demonstrates a very basic use of flowcharts: filter data,
displaying both the input and output of the filter. The behavior of
the filter can be reprogrammed by the user.

Basic steps are:
  - create a flowchart and two plots
  - input noisy data to the flowchart
  - flowchart connects data to the first plot, where it is displayed
  - add a gaussian filter to lowpass the data, then display it in the second plot.
"""
# import initExample ## Add path to library (just for examples; you do not need this)


from Lamia.Lamia.libs.pyqtgraph.flowchart import Flowchart, Terminal, Node
#from Lamia.Lamia.libs.pyqtgraph.Qt import QtGui, QtCore
import Lamia.Lamia.libs.pyqtgraph as pg
import numpy as np
import Lamia.Lamia.libs.pyqtgraph.metaarray as metaarray
import Lamia.Lamia.libs.pyqtgraph.flowchart.library as fclib
from Lamia.Lamia.libs.pyqtgraph.flowchart.library.common import CtrlNode
import os, qgis, qgis.core
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict

try:
    from qgis.PyQt.QtGui import (QInputDialog,QTableWidgetItem,QComboBox,QAction,QProgressBar,QApplication,QWidget,QToolButton,
                                 QDialog, QGridLayout, QMainWindow)
except ImportError:
    from qgis.PyQt.QtWidgets import (QInputDialog,QTableWidgetItem,QComboBox,QAction,QProgressBar,QApplication,QWidget,QToolButton,
                                     QDialog, QGridLayout,QMainWindow)

if False:
    app = QtGui.QApplication([])
else:
    app = qgis.core.QgsApplication([], True)
    qgis_path = "C://Program Files//OSGeo4W64//apps//qgis-ltr"
    qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
    qgis.core.QgsApplication.initQgis()

## Create main window with grid layout
win = QMainWindow()
win.setWindowTitle('pyqtgraph example: Flowchart')
cw = QWidget()
win.setCentralWidget(cw)
layout = QGridLayout()
cw.setLayout(layout)





if True:
    layerpath = os.path.join(os.path.dirname(__file__),'importtool', 'testshape.shp')
    print(layerpath)
    currentlayer = qgis.core.QgsVectorLayer(layerpath, 'test', 'ogr')
    print(currentlayer.isValid())
    data = [fet[0] for fet in currentlayer.getFeatures()]
    print('values', data)
    #fc.setInput(dataIn=data)

## Create flowchart, define input/output terminals
if True:
    terminalindict = OrderedDict()
    fieldnames = [field.name()for field in currentlayer.fields()]
    for field in fieldnames:
        terminalindict[field] = {'io': 'in'}
    terminalindict['Output'] =  {'io': 'out'}
    fc = Flowchart(terminals=terminalindict)
    fc.inputNode.graphicsItem().bounds = QtCore.QRectF(0, 0, 100, len(fieldnames)*15)
    fc.inputNode.graphicsItem().update()

    fc.widget().ui.loadBtn.clicked.disconnect()
    fc.widget().ui.saveBtn.clicked.disconnect()
    fc.widget().ui.saveAsBtn.clicked.disconnect()

    fc.widget().ui.saveBtn.clicked.connect(saveAs)


def saveAs():
    pass


#fNode.graphicsItem().updateTerminals()
#fc.inputNode.graphicsItem().bounds = QtCore.QRectF(0, 0, 100, 300)

if False:
    fc = Flowchart()
    inputnode = Node('Input', terminals={
            'dataIn': {'io': 'in', 'multi': True},
            'datain2':{'io': 'in'}})
    fc.addNode(inputnode,'Input',pos=(0, 0) )



wdg = fc.widget()

#wdg = fc.chartGraphicsItem()
wdg1 = fc.widget().chartWidget
wdg1.selDock.setVisible(False)


## Add flowchart control panel to the main window
layout.addWidget(wdg, 0, 0, 2, 1)
layout.addWidget(wdg1, 1, 1, 1, 2)

if False:
    ## Add two plot widgets
    pw1 = pg.PlotWidget()
    pw2 = pg.PlotWidget()
    layout.addWidget(pw1, 0, 1)
    layout.addWidget(pw2, 1, 1)

win.show()

if True:
    layerpath = os.path.join(os.path.dirname(__file__),'importtool', 'testshape.shp')
    print(layerpath)
    currentlayer = qgis.core.QgsVectorLayer(layerpath, 'test', 'ogr')
    print(currentlayer.isValid())
    data = [fet[0] for fet in currentlayer.getFeatures()]
    print('values', data)
    #fc.setInput(dataIn=data)


else:
    ## generate signal data to pass through the flowchart
    data = np.random.normal(size=1000)
    data[200:300] += 1
    data += np.sin(np.linspace(0, 100, 1000))
    data = metaarray.MetaArray(data, info=[{'name': 'Time', 'values': np.linspace(0, 1.0, len(data))}, {}])

    ## Feed data into the input terminal of the flowchart
    fc.setInput(dataIn=data)



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_exportshp_tool.ui')
        uic.loadUi(uipath, self)

        self.comboBox_type.addItems(['tet','popo'])


class TestNode(CtrlNode):
    """Return the input data passed through an unsharp mask."""
    nodeName = "TestNode"

    uiTemplate = [
        ('sigma', 'spin', {'value': 1.0, 'step': 1.0, 'bounds': [0.0, None]}),
        ('strength', 'spin', {'value': 1.0, 'dec': True, 'step': 0.5, 'minStep': 0.01, 'bounds': [0.0, None]}),
    ]

    def __init__(self, name):
        ## Define the input / output terminals available on this node
        #self.someQWidget = None
        terminals = {
            'dataIn': dict(io='in'),  # each terminal needs at least a name and
            'dataOut': dict(io='out'),  # to specify whether it is input or output
        }  # other more advanced options are available
        # as well..

        CtrlNode.__init__(self, name, terminals=terminals)
        self.stopconnect = False
        self.currentlayer = None
        self.currentlayerindex = None
        self.uniquevalues = None
        #self.connected.connect(self.connectionChanged)

    def process(self,  display=True ,**args):
        # CtrlNode has created self.ctrls, which is a dict containing {ctrlName: widget}
        print('*********** process', self.name())
        print(args)
        output = [1]
        if False:
            print(self.someQWidget.comboBox_type.currentText() )
            if self.someQWidget.comboBox_type.currentText() == 'popo':
                output = [datai*10 for datai in dataIn]
            elif self.someQWidget.comboBox_type.currentText() == 'tet':
                output = [datai*1000 for datai in dataIn]

            if False:
                sigma = self.ctrls['sigma'].value()
                strength = self.ctrls['strength'].value()
                output = dataIn - (strength * pg.gaussianFilter(dataIn, (sigma, sigma)))
        return {'dataOut': output}

    def ctrlWidget(self):  # this method is optional
        self.someQWidget = UserUI()
        self.someQWidget.comboBox_type.currentIndexChanged.connect(self.update)
        return self.someQWidget

    def setLayers(self, currentlayer):
        self.currentlayer = currentlayer

    def connected(self,localTerm, remoteTerm ):
        print('******* connected',localTerm, remoteTerm )
        print(self.name(), self.inputValues())

        remotetermname = remoteTerm.node().name()
        if remotetermname in  ['Input', 'Output']:
            if not self.stopconnect:
                self.clearTerminals()
                self.stopconnect = True
            else:
                self.stopconnect = False
                return
        else:
            #self.process(self.inputValues())
            #print('inputval', self.name(), self.inputValues())
            self.update()
            #self.sigOutputChanged.emit(self)

        if remoteTerm.node().name() == 'Output':
            self.clearTerminals()
            self.addInput(name='test')
            self.addInput(name='test1')
            self.addOutput(name='dataOut')

            output = self.outputs()['dataOut']
            output.connectTo(remoteTerm)

        elif remoteTerm.node().name() == 'Input':
            self.clearTerminals()
            termfieldname = remoteTerm.name()
            #uniquevalues
            self.uniquevalues=None
            for i, fieldname in enumerate([field.name() for field in self.currentlayer.fields()]):
                if fieldname == termfieldname:
                    self.uniquevalues = self.currentlayer.uniqueValues(i)
                    self.currentlayerindex = i
                    break
            if len(self.uniquevalues)<20:
                for uniquevalue in self.uniquevalues:
                    self.addOutput(name=str(uniquevalue))
                self.graphicsItem().bounds = QtCore.QRectF(0, 0, 200, len(self.uniquevalues) * 15)
                #fc.outputNode.graphicsItem().updateTerminals()
                #fc.outputNode.graphicsItem().update()
                #self.addOutput(name='test')
                #self.addOutput(name='test1')

            self.addInput(name='dataIn')

            output = self.inputs()['dataIn']
            output.connectTo(remoteTerm)


            if False:
                if remoteTerm.node().name() == 'Output':
                    print('remote term Output')
                    terms = dict(self.inputs())
                    for key in terms:
                        print('disconnect and close',key)
                        terms[key].disconnectAll()
                        self.removeTerminal(terms[key])
                        #terms[key].close()
                    #self._inputs = OrderedDict()
                    self.update()
                    self.addInput(name='test')
                    self.addInput(name='test1')
                    self.update()
                    terms = dict(self.outputs())
                    for key in terms.keys():
                        if terms[key].isConnected():
                            #terms[key].disconnectAll()
                            print('rename', key)
                            terms[key].rename('dataOut')
                        else:
                            print('disconnect and close', key)
                            terms[key].disconnectAll()
                            self.removeTerminal(terms[key])
                            #terms[key].close()
                    self.update()

                elif remoteTerm.node().name() == 'Input':
                    print('remote term Input')
                    terms = dict(self.outputs())
                    for key in terms:
                        print('disconnect and close', key)
                        terms[key].disconnectAll()
                        self.removeTerminal(terms[key])
                        #terms[key].close()
                    self.update()
                    #self._outputs = OrderedDict()

                    self.addOutput(name='test')
                    self.addOutput(name='test1')
                    self.update()
                    terms = dict(self.inputs())
                    for key in terms.keys():
                        if terms[key].isConnected():
                            print('rename', key)
                            #terms[key].disconnectAll()
                            terms[key].rename('dataIn')
                        else:
                            print('disconnect and close', key)
                            terms[key].disconnectAll()
                            self.removeTerminal(terms[key])
                            #terms[key].close()
                    self.update()




if True:
    library = fclib.LIBRARY.copy()  # start with the default node set

    library.addNodeType(TestNode, [('Image',),
                                          ('Submenu_test', 'submenu2', 'submenu3')])
    fc.setLibrary(library)

    fNode = fc.createNode('TestNode', pos=(0, 10))
    fNode.setLayers(currentlayer)
    #fNode.clearTerminals()



if False:
    pass
    fc.connectTerminals(fc['dataIn'], fNode['dataIn'])



if False:
    ## populate the flowchart with a basic set of processing nodes.
    ## (usually we let the user do this)
    plotList = {'Top Plot': pw1, 'Bottom Plot': pw2}

    pw1Node = fc.createNode('PlotWidget', pos=(0, -150))
    pw1Node.setPlotList(plotList)
    pw1Node.setPlot(pw1)

    pw2Node = fc.createNode('PlotWidget', pos=(150, -150))
    pw2Node.setPlot(pw2)
    pw2Node.setPlotList(plotList)

    fNode = fc.createNode('GaussianFilter', pos=(0, 0))
    fNode.ctrls['sigma'].setValue(5)
    fc.connectTerminals(fc['dataIn'], fNode['In'])
    fc.connectTerminals(fc['dataIn'], pw1Node['In'])
    fc.connectTerminals(fNode['Out'], pw2Node['In'])
    fc.connectTerminals(fNode['Out'], fc['dataOut'])

if False:
    output = fc.output()
    print(output)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()


