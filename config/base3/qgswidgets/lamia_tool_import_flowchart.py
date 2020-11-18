# -*- coding: utf-8 -*-

"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """

import os, logging, sys, re
import numpy as np
import qgis, qgis.utils
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from qgis.PyQt.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QSplitter,
    QFrame,
    QGridLayout,
)

from Lamia.api.libs import pyqtgraph
from Lamia.api.libs.pyqtgraph.flowchart import Flowchart, Node
from Lamia.api.libs.pyqtgraph.flowchart.library.common import CtrlNode
from Lamia.api.libs.pyqtgraph.flowchart import library as fclib
from Lamia.api.libs.pyqtgraph.flowchart.library.Data import EvalNode
from Lamia.api.libs.pyqtgraph import configfile as configfile

from Lamia.api.libslamia.lamiaimport.lamiaimport import ImportCore

pyqtgraph.setConfigOption("background", "w")
pyqtgraph.setConfigOption("foreground", (0, 44, 83))
pyqtgraph.setConfigOptions(antialias=True)


class FlowChartWidget(QDialog):
    def __init__(self, dbase=None, messageinstance=None, mainifacewidget=None):
        super(FlowChartWidget, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)
        self.dbase = dbase
        self.qfiledlg = None
        if mainifacewidget:
            self.qfiledlg = mainifacewidget.qfiledlg
        self.messageinstance = messageinstance
        # self.importool = parentoolwdg
        self.importtool = ImportCore(
            dbaseparser=self.dbase, messageinstance=messageinstance
        )

        self.fromlayer = None
        self.lendatafromlayer = None

        self.library = fclib.LIBRARY.copy()  # start with the default node set
        self.library.nodeList = {}
        self.library.nodeTree = {}
        self.library.addNodeType(EvalNode, [()])
        self.library.addNodeType(AttributeReaderNode, [()])
        self.library.addNodeType(ConstantNode, [()])
        self.library.addNodeType(MultiplierNode, [()])
        self.terminalindict = {}
        self.fc = Flowchart(terminals=self.terminalindict)
        self.fc.setLibrary(self.library)

        self.initUI()

    def ___________________________initThings(self):
        pass

    def initUI(self):
        for butname in ["loadBtn", "saveBtn", "saveAsBtn", "reloadBtn", "showChartBtn"]:
            try:
                eval("self.fc.widget().ui." + butname + ".clicked.disconnect()")
            except:
                pass

        self.fc.widget().ui.showChartBtn.setVisible(False)
        self.fc.widget().ui.reloadBtn.setText("Import !!!")
        self.fc.widget().ui.reloadBtn.clicked.connect(self.runImport)
        self.fc.widget().ui.saveAsBtn.clicked.connect(self.fcSaveAs)
        self.fc.widget().ui.loadBtn.clicked.connect(self.fcLoad)

        wdg1lay = QVBoxLayout()
        wdgflowcontrol = self.fc.widget()
        wdg1lay.addWidget(wdgflowcontrol)
        self.flowqlabelmessage = QLabel(
            QtCore.QCoreApplication.translate("base3", "Status : /")
        )
        wdg1lay.addWidget(self.flowqlabelmessage)
        wdg1 = QFrame()
        wdg1.setLayout(wdg1lay)

        wdg2 = self.fc.widget().chartWidget
        wdg2.selDock.setVisible(False)
        splitwdg = QSplitter(QtCore.Qt.Horizontal)
        splitwdg.setStretchFactor(1, 10)

        splitwdg.addWidget(wdg1)
        splitwdg.addWidget(wdg2)
        self.layout().addWidget(splitwdg, 0, 0, 1, 1)

    def initFromandToLayers(self, fromqgslayer, tolayername):
        debug = True
        self.fromlayer = fromqgslayer
        self.tolayername = tolayername
        self.terminalindict = {}
        self.fc.clear()
        curoutput = dict(self.fc.inputNode.outputs())
        for outterm in curoutput:
            self.fc.inputNode.removeTerminal(outterm)
        curinput = dict(self.fc.outputNode.inputs())
        for interm in curinput:
            self.fc.outputNode.removeTerminal(interm)

        self.fc.setLibrary(self.library)
        # self.fc.removeNode(self.fc.outputNode)
        # self.fc.removeNode(self.fc.outputNode)

        fromfields = self._getFromFieldsfromQgsVectorLayer(fromqgslayer)
        tofields = self._getToFieldsFromLamiaTableName(tolayername)
        if debug:
            logging.getLogger("Lamia_unittest").debug("fromfields %s", str(fromfields))
        if debug:
            logging.getLogger("Lamia_unittest").debug("tofields %s", str(tofields))
        # get from valuues
        fromattributes = []
        for fet in fromqgslayer.getFeatures():
            fromattributes.append(np.array(fet.attributes()))
        fromattributesnp = np.array(fromattributes)
        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "npaatributes %s", str(fromattributesnp)
            )

        # initflowchart

        for field in tofields:
            self.terminalindict[field] = {"io": "out"}
        for field in fromfields:
            self.terminalindict[field] = {"io": "in"}
        for name, opts in self.terminalindict.items():
            self.fc.addTerminal(name, **opts)

        for i, field in enumerate(fromfields):
            if field != "":
                fieldstandard = field
                stringtoeval = (
                    "self.fc.setInput("
                    + fieldstandard
                    + "=list(fromattributesnp[:,"
                    + str(i)
                    + "]))"
                )
                eval(stringtoeval)

        self.fc.outputNode.graphicsItem().bounds = QtCore.QRectF(
            0, 0, 200, len(tofields) * 15
        )
        self.fc.outputNode.graphicsItem().updateTerminals()
        self.fc.outputNode.graphicsItem().update()

        self.fc.inputNode.graphicsItem().bounds = QtCore.QRectF(
            0, 0, 200, len(fromfields) * 15
        )
        self.fc.inputNode.graphicsItem().updateTerminals()
        self.fc.inputNode.graphicsItem().update()

        self.fc.sigChartChanged.connect(self.fcNodeAdded)

        if qgis.utils.iface is None:
            fNode = self.fc.createNode("AttributeReaderNode", pos=(0, 10))
            fNode2 = self.fc.createNode("AttributeReaderNode", pos=(0, 20))
            fNode3 = self.fc.createNode("PythonEval", pos=(0, 30))

    def _getToFieldsFromLamiaTableName(self, simpletablename):
        parentstable = [simpletablename] + self.dbase.getParentTable(simpletablename)
        result = []
        for tablename in parentstable:
            if tablename in self.dbase.dbasetables.keys():
                dbasetable = self.dbase.dbasetables[tablename]
                for field in dbasetable["fields"].keys():
                    if (
                        field[0:3] not in ["pk_", "id_"]
                        and field[0:4] not in ["lpk_", "lid_"]
                        and field not in ["datetimecreation", "datetimemodification"]
                    ):
                        result.append(tablename + "." + field)
        return result

    def _getFromFieldsfromQgsVectorLayer(self, qgslayer):
        currentlayerfields = qgslayer.fields()
        currentlayerfieldsname = [
            "_".join(field.name().split(" ")) for field in currentlayerfields
        ]
        self.lendatafromlayer = qgslayer.featureCount()
        return currentlayerfieldsname

    def ___________________________buttons(self):
        pass

    def fcSaveAs(self):
        if self.fc.widget().currentFileName is None:

            # startdir = os.path.join(
            #     self.dbase.dbaseressourcesdirectory, "config", "importtools"
            # )

            startdir = self.importtool.confdatadirproject

            conffile, fileext = self.qfiledlg.getSaveFileName(
                self, "Lamia - import conf", startdir, "flowfile (*.fc)"
            )

        else:
            conffile = self.fc.widget().currentFileName

        conffile = unicode(conffile)
        configfile.writeConfigFile(self.fc.saveState(), conffile)
        self.fc.sigFileSaved.emit(conffile)

    def fcLoad(self, fileName=None):
        if not fileName:
            # startdir = os.path.join(
            #     self.dbase.dbaseressourcesdirectory, "config", "importtools"
            # )
            startdir = self.importtool.confdatadirproject
            fileName, extension = self.qfiledlg.getOpenFileName(
                None, "Choose the file", startdir, "flowChart (*.fc)", ""
            )
        else:
            fileName = self.importtool.getConfFilePath(fileName)
        if fileName:
            try:
                fileName = unicode(fileName)
                state = configfile.readConfigFile(fileName)
                self.fc.setLibrary(self.library)
                self.fc.sigChartChanged.connect(self.fcNodeAdded)
                self._restoreState(state, clear=True)
                self.fc.viewBox.autoRange()
                # self.emit(QtCore.SIGNAL('fileLoaded'), fileName)
                self.fc.sigFileLoaded.emit(fileName)
            except Exception as e:
                print("err", e)

    def _restoreState(self, state, clear=False):
        # self.blockSignals(True)
        try:
            if clear:
                self.fc.clear()
            Node.restoreState(self.fc, state)
            nodes = state["nodes"]
            nodes.sort(key=lambda a: a["pos"][0])
            for n in nodes:
                if n["name"] in self.fc._nodes:
                    # self._nodes[n['name']].graphicsItem().moveBy(*n['pos'])
                    self.fc._nodes[n["name"]].restoreState(n["state"])
                    continue
                try:
                    node = self.fc.createNode(n["class"], name=n["name"])
                    node.restoreState(n["state"])
                except:
                    pass
                    # printExc("Error creating node %s: (continuing anyway)" % n['name'])
                # node.graphicsItem().moveBy(*n['pos'])

            self.fc.inputNode.restoreState(state.get("inputNode", {}))
            self.fc.outputNode.restoreState(state.get("outputNode", {}))

            # self.restoreTerminals(state['terminals'])
            connectionstoloadafter = []
            for n1, t1, n2, t2 in state["connects"]:
                if n1 in ["Output", "Input"] or n2 in ["Output", "Input"]:
                    self.fc.connectTerminals(
                        self.fc._nodes[n1][t1], self.fc._nodes[n2][t2]
                    )
                else:
                    connectionstoloadafter.append([n1, t1, n2, t2])

            for n1, t1, n2, t2 in connectionstoloadafter:
                try:
                    self.fc.connectTerminals(
                        self.fc._nodes[n1][t1], self.fc._nodes[n2][t2]
                    )
                except:
                    pass

        finally:
            pass
            # self.fc.blockSignals(False)

        self.fc.sigChartLoaded.emit()
        self.fc.outputChanged()
        self.fc.sigStateChanged.emit()
        # self.fc.sigOutputChanged.emit()

    def runImport(self):
        self.flowqlabelmessage.setText(
            QtCore.QCoreApplication.translate("base3", "Importing ...")
        )
        table_field_list, array = self._getDatasOfOutputTerminal()
        geoms = self._getReprojectedGeoms()

        self.importtool.importCleanedDatas(
            self.tolayername, table_field_list, array, geoms
        )
        self.flowqlabelmessage.setText(
            QtCore.QCoreApplication.translate("base3", "Imported")
        )

    def _getDatasOfOutputTerminal(self):
        outputflowchart = self.fc.output()
        totallinecount = self.lendatafromlayer

        # build datas
        table_field_list = []
        results = []
        for outputkey in outputflowchart.keys():
            table_field_list.append(outputkey)
            outputres = outputflowchart[outputkey]
            if outputres is not None:
                if isinstance(outputres, list) and len(outputres) == 1:
                    outputres = outputres * totallinecount
                elif isinstance(outputres, float) or isinstance(outputres, int):
                    outputres = [outputres] * totallinecount
            elif outputres is None:
                outputres = ["NULL"] * totallinecount

            if len(outputres) != totallinecount:
                self.flowqlabelmessage.setText(
                    QtCore.QCoreApplication.translate(
                        "base3", "Error message : issue with " + str(outputkey)
                    )
                )
                return
            results.append(outputres)

        results = np.array(results).T
        return table_field_list, results

    def _getReprojectedGeoms(self):
        dbaseqgiscrs = qgis.core.QgsCoordinateReferenceSystem()
        dbaseqgiscrs.createFromString("EPSG:" + str(self.dbase.crsnumber))
        self.xform = qgis.core.QgsCoordinateTransform(
            self.fromlayer.crs(), dbaseqgiscrs, qgis.core.QgsProject.instance()
        )
        geoms = []
        for layerfeat in self.fromlayer.getFeatures():
            featgeom = layerfeat.geometry()
            success = featgeom.transform(self.xform)
            featgeomwkt = featgeom.asWkt()
            geoms.append(featgeomwkt)
        return geoms

    def fcNodeAdded(self, flowchart, action, node):
        if node.nodeName == "AttributeReaderNode":
            node.setLayers(self.fromlayer)
            node.setDbase(self.dbase)
        elif node.nodeName == "MultiplierNode":
            node.setDbase(self.dbase)


class MultiplierNode(CtrlNode):
    nodeName = "MultiplierNode"
    uiTemplate = [
        ("coefficient", "spin", {"value": 1.0, "step": 1.0, "bounds": [0.0, None]}),
    ]

    def __init__(self, name):
        terminals = {
            "dataIn": dict(io="in"),  # each terminal needs at least a name and
            "dataOut": dict(io="out"),  # to specify whether it is input or output
        }  # other more advanced options are available
        # as well..
        CtrlNode.__init__(self, name, terminals=terminals)

    def process(self, display=True, **args):
        results = {}
        results["dataOut"] = None
        coef = self.ctrls["coefficient"].value()
        if args["dataIn"]:
            datain = [
                float(x) if not self.dbase.utils.isAttributeNull(x) else None
                for x in args["dataIn"]
            ]

            try:
                results["dataOut"] = (np.array(datain).astype(np.float) * coef).tolist()
            except Exception as e:
                print(e)
                pass
        return results

    def setDbase(self, dbase):
        self.dbase = dbase


class ConstantNode(CtrlNode):
    nodeName = "ConstantNode"
    uiTemplate = []

    def __init__(self, name):
        terminals = {
            # "dataIn": dict(io="in"),  # each terminal needs at least a name and
            "dataOut": dict(io="out"),  # to specify whether it is input or output
        }  # other more advanced options are available
        # as well..
        CtrlNode.__init__(self, name, terminals=terminals)

    def process(self, display=True, **args):
        results = {}
        results["dataOut"] = [1]
        return results

    def connected(self, localTerm, remoteTerm):
        self.update()


class AttributeReaderNode(CtrlNode):
    """Return the input data passed through an unsharp mask."""

    nodeName = "AttributeReaderNode"
    uiTemplate = []
    """
    uiTemplate = [
        ('sigma', 'spin', {'value': 1.0, 'step': 1.0, 'bounds': [0.0, None]}),
        ('strength', 'spin', {'value': 1.0, 'dec': True, 'step': 0.5, 'minStep': 0.01, 'bounds': [0.0, None]}),
    ]
    """

    def __init__(self, name):
        ## Define the input / output terminals available on this node
        # self.someQWidget = None
        terminals = {
            "dataIn": dict(io="in"),  # each terminal needs at least a name and
            "dataOut": dict(io="out"),  # to specify whether it is input or output
        }  # other more advanced options are available
        # as well..

        CtrlNode.__init__(self, name, terminals=terminals)
        self.stopconnect = False
        self.currentlayer = None
        self.currentlayerindex = None
        self.uniquevalues = None

    def process(self, display=True, **args):
        # CtrlNode has created self.ctrls, which is a dict containing {ctrlName: widget}
        debug = False
        results = {}

        if debug:
            logging.getLogger("Lamia").debug("***  process ***")
        if debug:
            logging.getLogger("Lamia").debug("nodename : %s", self.name())
        if debug:
            logging.getLogger("Lamia").debug("args : %s", str(args))
        if debug:
            logging.getLogger("Lamia").debug("inputs : %s", str(self.inputs().keys()))
        if debug:
            logging.getLogger("Lamia").debug("outputs : %s", str(self.outputs().keys()))

        if list(self.inputs().keys())[0] == "dataIn":

            if debug:
                logging.getLogger("Lamia").debug("dataIn type")
            for termname in self.outputs().keys():
                results[termname] = []
                if args["dataIn"] is not None:
                    for data in args["dataIn"]:
                        if data == termname:
                            results[termname].append(data)
                        else:
                            results[termname].append(None)

            # return results

        # elif list(self.outputs().keys())[0] == 'dataOut' and len(list(self.inputs().keys())) > 0:
        elif list(self.outputs().keys())[0] == "dataOut":
            if debug:
                logging.getLogger("Lamia").debug("dataOut type")
            results["dataOut"] = []
            datainput = {}
            leninput = None
            for termname in self.inputs().keys():
                if args[termname] is not None and args[termname] != {}:
                    if isinstance(args[termname], dict):
                        leninput = len(
                            args[termname][list(args[termname].keys())[0]]
                        )  # list(test_dict.keys())[0]
                        tempval = None
                        for k, v in args[termname].items():
                            if "ConstantNode" in k.node().name():
                                tempval = np.array(["lamiaconstant"])
                            elif tempval is None:
                                tempval = np.array(args[termname][k])
                                tempval = np.array(
                                    [x if x else "" for x in args[termname][k]]
                                )
                            else:
                                tempval = np.core.defchararray.add(
                                    tempval, [x if x else "" for x in args[termname][k]]
                                )

                        datainput[termname] = (
                            [x if x else None for x in tempval.tolist()]
                            if tempval is not None
                            else None
                        )

                    else:
                        leninput = len(args[termname])
                        datainput[termname] = args[termname]

            if leninput is not None:
                for i in range(leninput):
                    tempres = None
                    lamiaconstant = None
                    for termname in datainput.keys():
                        # if isinstance(datainput[termname], dict):
                        #     for k, v in datainput[termname].items():
                        #         if len(v) == 1 and v[0] == "lamiaconstant":
                        #             lamiaconstant = termname

                        #         elif v[i] is not None:
                        #             tempres = termname
                        #             break
                        if (
                            len(datainput[termname]) == 1
                            and datainput[termname][0] == "lamiaconstant"
                        ):
                            lamiaconstant = termname
                        elif datainput[termname][i] is not None:
                            # tempres = datainput[termname][i]
                            tempres = termname
                            break

                    if tempres is None and lamiaconstant is not None:
                        tempres = lamiaconstant

                    results["dataOut"].append(tempres)

        if debug:
            logging.getLogger("Lamia").debug("Results : %s", str(results))
        return results

        if False:
            print(self.someQWidget.comboBox_type.currentText())
            if self.someQWidget.comboBox_type.currentText() == "popo":
                output = [datai * 10 for datai in dataIn]
            elif self.someQWidget.comboBox_type.currentText() == "tet":
                output = [datai * 1000 for datai in dataIn]

            if False:
                sigma = self.ctrls["sigma"].value()
                strength = self.ctrls["strength"].value()
                output = dataIn - (strength * pg.gaussianFilter(dataIn, (sigma, sigma)))
        # return {'dataOut': output}

    def setLayers(self, currentlayer):
        self.currentlayer = currentlayer

    def setDbase(self, dbase):
        self.dbase = dbase

    def connected(self, localTerm, remoteTerm):
        debug = False

        if debug:
            logging.getLogger("Lamia").debug("***  connected ***")
        if debug:
            logging.getLogger("Lamia").debug(
                "%s, %s, %s", self.name(), str(localTerm), str(remoteTerm)
            )

        remotetermname = remoteTerm.node().name()
        # localtermname = remoteTerm.node().name()
        if remotetermname in ["Input", "Output"]:
            if not self.stopconnect:
                self.clearTerminals()
                self.stopconnect = True
            else:
                self.stopconnect = False
                self.update()
                return
        else:
            if debug:
                logging.getLogger("Lamia").debug("update")
            self.update()

        if remoteTerm.node().name() == "Output":
            if debug:
                logging.getLogger("Lamia").debug("connecttype : Output")
            self.clearTerminals()

            termname = remoteTerm.name()
            table, field = termname.split(".")
            fullcst = self.dbase.dbasetables[table]["fields"][field]["Cst"]
            values = [elem[0] for elem in fullcst]
            for value in values:
                self.addInput(name=str(value), multi=True)
            self.graphicsItem().bounds = QtCore.QRectF(0, 0, 200, len(values) * 15)
            self.graphicsItem().update()

            self.addOutput(name="dataOut")
            output = self.outputs()["dataOut"]
            output.connectTo(remoteTerm)
            # self.update()

        elif remoteTerm.node().name() == "Input":
            if debug:
                logging.getLogger("Lamia").debug("connecttype : Input")
            self.clearTerminals()
            termfieldname = remoteTerm.name()
            # uniquevalues
            self.uniquevalues = None
            for i, fieldname in enumerate(
                [field.name() for field in self.currentlayer.fields()]
            ):
                if fieldname == termfieldname:
                    self.uniquevalues = self.currentlayer.uniqueValues(i)
                    self.currentlayerindex = i
                    break
            if len(self.uniquevalues) < 20:
                for uniquevalue in self.uniquevalues:
                    # self.addOutput(name=str(uniquevalue), multi=True)
                    self.addOutput(name=str(uniquevalue))
                self.graphicsItem().bounds = QtCore.QRectF(
                    0, 0, 200, len(self.uniquevalues) * 15
                )
                self.graphicsItem().update()
                # fc.outputNode.graphicsItem().updateTerminals()
                # fc.outputNode.graphicsItem().update()
                # self.addOutput(name='test')
                # self.addOutput(name='test1')

            self.addInput(name="dataIn")

            input = self.inputs()["dataIn"]
            input.connectTo(remoteTerm)

            # self.update()

