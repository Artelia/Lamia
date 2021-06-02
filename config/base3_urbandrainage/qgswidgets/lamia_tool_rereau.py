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

import os
import io
import sys
import json

import qgis
from qgis.PyQt import uic, QtGui, QtCore
from qgis.PyQt.QtWidgets import (
    QWidget,
    QLabel,
    QFrame,
    QTreeWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QTableWidgetItem,
    QDialog,
)

import Lamia

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool
from Lamia.api.libslamia.lamiaITVimport.lamiaITVimport import ITVImportCore
from Lamia.qgisiface.iface.qgiswidget.tools.general_subwidgets.abstractfilemanager import (
    AbstractFileManager,
)
import numpy as np
import shutil, platform, subprocess
import logging

from Lamia.api.libslamia.lamiaITVimport.exfiltration_indicators import all_exfiltration_indicators
from Lamia.api.libslamia.lamiaITVimport.infiltration_indicators import all_infiltration_indicators
from Lamia.api.libslamia.lamiaITVimport.ensablement_indicators import all_ensablement_indicators
# from Lamia.api.libslamia.lamiaITVimport.effondrement_indicators import all_effondrement_indicators
# from Lamia.api.libslamia.lamiaITVimport.bouchage_indicators import all_bouchage_indicators
from Lamia.api.libslamia.lamiaITVimport.red_cap_hydraulique_indicators import all_red_cap_hydraulique_indicators


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

# class PathTool(AbstractInspectionDigueTool):
class RereauTool(AbstractLamiaTool):

    # DBASES = ["digue", "base_digue"]
    # TOOLNAME = "Networktool"

    POSTPROTOOLNAME = ITVImportCore.POSTPROTOOLNAME

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Analytics")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Rer'eau")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_tool_network_icon.png"
    )
    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(RereauTool, self).__init__(**kwargs)

        self.itvcore = ITVImportCore(
            dbaseparser=self.dbase, messageinstance=self.mainifacewidget.connector
        )

        self.filemanager = RereaufileManager(self.mainifacewidget, self.itvcore)

        result_folder = os.path.join(self.dbase.dbaseressourcesdirectory + '/result_computation')
        if not os.path.exists(result_folder):
            os.makedirs(result_folder)

    def _check_combobox_indicator(self, other_layer=None, name_itv="ITV"):
        """
        change color of edge based on indicator value
        """

        qgislayer = self.mainifacewidget.qgiscanvas.layers['edge']['layerqgis']

        if other_layer != None:
            
            other_layer.startEditing()
            for field in other_layer.fields():
                if 'etat' in field.name():
                    idx = other_layer.fields().indexFromName(field.name())
                    split_word = 'etat'
                    new_name = split_word + field.name().partition(split_word)[2]
                    other_layer.renameAttribute(idx, new_name)
                elif 'note' in field.name():
                    idx = other_layer.fields().indexFromName(field.name())
                    split_word = 'note'
                    new_name = split_word + field.name().partition(split_word)[2]
                    other_layer.renameAttribute(idx, new_name)
            other_layer.commitChanges()
            
            with open(os.path.join(self.filemanager.toolclass.confdatadirproject, self.filemanager.getCurrentText())) as json_file:
                config = json.load(json_file)
            result_folder = os.path.join(self.dbase.dbaseressourcesdirectory, 'result_computation')
            date = QtCore.QDate().currentDate().toString('yyyy/MM/dd') # date forme us
            date = date.replace(u"/", u"")
            heure = QtCore.QTime().currentTime().toString('hh:mm:ss') # heure:minutes:secondes
            heure = heure.replace(u":", u"")
            writer = qgis.core.QgsVectorFileWriter.writeAsVectorFormat(other_layer, os.path.join(result_folder, name_itv), "utf-8", qgis.core.QgsCoordinateReferenceSystem(), "CSV")
            for join in qgislayer.vectorJoins():
                qgislayer.removeJoin(join.joinLayerId())
            # join between itv result table and qgis edge layer
            joinObject = qgis.core.QgsVectorLayerJoinInfo()
            joinObject.setJoinFieldName("id_edge")
            joinObject.setTargetFieldName("id_edge")
            joinObject.setJoinLayerId(other_layer.id())
            joinObject.setUsingMemoryCache(True)
            joinObject.setPrefix("")
            joinObject.setJoinLayer(other_layer)

            self.mainifacewidget.qgiscanvas.layers['edge']['layerqgis'].addJoin(joinObject)
            qgis.core.QgsProject.instance().addMapLayer(other_layer)

            self.toolwidgetmain.comboBox_result.clear()
            result_list = [f for f in os.listdir(result_folder) if os.path.isfile(os.path.join(result_folder, f))]
            self.toolwidgetmain.comboBox_result.addItems(result_list)
            
            qgislayer.startEditing()
            for field in qgislayer.fields():
                if 'etat' in field.name():
                    idx = qgislayer.fields().indexFromName(field.name())
                    split_word = 'etat'
                    new_name = split_word + field.name().partition(split_word)[2]
                    qgislayer.renameAttribute(idx, new_name)
                elif 'note' in field.name():
                    idx = qgislayer.fields().indexFromName(field.name())
                    split_word = 'note'
                    new_name = split_word + field.name().partition(split_word)[2]
                    qgislayer.renameAttribute(idx, new_name)
            qgislayer.commitChanges()
        
        self.indicator_changed()

    def initMainToolWidget(self):

        # userui

        self.toolwidgetmain = UserUI()

        self.toolwidgetmain.groupBox_filemanager.layout().addWidget(self.filemanager)
        self.choosertreewidget = self.mainifacewidget.toolwidgets[
            "itv"
        ].choosertreewidget

        self.toolwidgetmain.pushButton_analysis.clicked.connect(self.computeRereau)

        indicator_list = []
        for indicator in all_exfiltration_indicators.keys():
            indicator_list.append(indicator)
        for indicator in all_infiltration_indicators.keys():
            indicator_list.append(indicator)
        for indicator in all_ensablement_indicators.keys():
            indicator_list.append(indicator)
        for indicator in all_red_cap_hydraulique_indicators.keys():
            indicator_list.append(indicator)
        # fill comboBox with available indicator
        self.toolwidgetmain.comboBox_indicator.addItems(indicator_list)

        result_folder = self.dbase.dbaseressourcesdirectory + '/result_computation'
        result_list = [f for f in os.listdir(result_folder) if os.path.isfile(os.path.join(result_folder, f))]
        self.toolwidgetmain.comboBox_result.addItems(result_list)

        self.toolwidgetmain.comboBox_indicator.currentIndexChanged.connect(self.indicator_changed)

        self.toolwidgetmain.pushButton_delete.clicked.connect(self.delete_result)
        
        self.toolwidgetmain.pushButton_load.clicked.connect(self.load_result)

        if len(result_list) == 0:
            boolenabled = False
        else:
            boolenabled = True

        self.toolwidgetmain.pushButton_delete.setEnabled(boolenabled)
        self.toolwidgetmain.pushButton_load.setEnabled(boolenabled)

    def computeRereau(self):
        """
        compute indicators from ITV and edges
        """
        with open(os.path.join(self.filemanager.toolclass.confdatadirproject, self.filemanager.getCurrentText())) as json_file:
            config = json.load(json_file)

        result_folder = os.path.join(self.dbase.dbaseressourcesdirectory, 'result_computation')
        date = QtCore.QDate().currentDate().toString('yyyy/MM/dd') # date forme us
        date = date.replace(u"/", u"")
        heure = QtCore.QTime().currentTime().toString('hh:mm:ss') # heure:minutes:secondes
        heure = heure.replace(u":", u"")

        # itv path
        pks = self.choosertreewidget.getSelectedPks()
        resfiles = []
        name_itv = ""
        for itvpk in pks:
            name_itv = name_itv + self.dbase.lamiaorm["itv"].read(itvpk)["name"]
            tempfiles = self.dbase.lamiaorm["itv"].read(itvpk)["file"].split(";")
            tempfiles = [self.dbase.completePathOfFile(fl.strip()) for fl in tempfiles]
            resfiles += tempfiles
        name_itv = name_itv + "_a_" + str(config["alpha"]) + "_P_" + str(config["P"]) + "_" + date +"_"+ heure + ".csv"
        temp_layer = self.itvcore.computeIndicators(resfiles, alpha=config["alpha"], P=config["P"], itv_name=name_itv)
        layer = self.itvcore.getQgsLayer(resfiles)
        project = qgis.core.QgsProject.instance()
        root = project.layerTreeRoot()
        project.addMapLayer(layer, True)

        layer_to_write = self._check_combobox_indicator(temp_layer, name_itv)

        result_folder = self.dbase.dbaseressourcesdirectory + '/result_computation'
        result_list = [f for f in os.listdir(result_folder) if os.path.isfile(os.path.join(result_folder, f))]
        self.toolwidgetmain.comboBox_result.clear()
        self.toolwidgetmain.comboBox_result.addItems(result_list)

        if len(result_list) == 0:
            boolenabled = False
        else:
            boolenabled = True

        self.toolwidgetmain.pushButton_delete.setEnabled(boolenabled)
        self.toolwidgetmain.pushButton_load.setEnabled(boolenabled)

    def postToolTreeWidgetCurrentItemChanged(self):
        self.filemanager.reset()
    
    def delete_result(self):
        """
        delete result
        """
        result_folder = self.dbase.dbaseressourcesdirectory + '/result_computation'
        currentxt = self.toolwidgetmain.comboBox_result.currentText()
        currentfilepath = os.path.join(result_folder, currentxt)

        os.remove(currentfilepath)

        self.toolwidgetmain.comboBox_result.clear()
        result_list = [f for f in os.listdir(result_folder) if os.path.isfile(os.path.join(result_folder, f))]
        self.toolwidgetmain.comboBox_result.clear()
        self.toolwidgetmain.comboBox_result.addItems(result_list)

        currentfilepath = os.path.join(result_folder, currentxt)
        if len(result_list) == 0:
            boolenabled = False
        else:
            boolenabled = True

        self.toolwidgetmain.pushButton_delete.setEnabled(boolenabled)
        self.toolwidgetmain.pushButton_load.setEnabled(boolenabled)

    def load_result(self):
        """
        load result file
        """
        result_folder = self.dbase.dbaseressourcesdirectory + '/result_computation'
        currentxt = self.toolwidgetmain.comboBox_result.currentText()
        currentfilepath = os.path.join(result_folder, currentxt)

        qgsproject = qgis.core.QgsProject.instance()

        layers = qgsproject.mapLayers()
        # print( [lay.name() for lay in layers] )
        print(layers)


        layerswithname = qgsproject.mapLayersByName(currentxt[:-5])
        print(layerswithname)
        if len(layerswithname) > 0:
            print('found')
            vlayer = layerswithname[0]
        else :
            vlayer = qgis.core.QgsVectorLayer(currentfilepath, currentxt[:-5], "ogr")
            
        if not vlayer.isValid():
            print("Layer failed to load!")
        else:
            # rename vlayer score and result
            vlayer.startEditing()
            for field in vlayer.fields():
                if 'etat' in field.name():
                    idx = vlayer.fields().indexFromName(field.name())
                    split_word = 'etat'
                    new_name = split_word + field.name().partition(split_word)[2]
                    vlayer.renameAttribute(idx, new_name)
                elif 'note' in field.name():
                    idx = vlayer.fields().indexFromName(field.name())
                    split_word = 'note'
                    new_name = split_word + field.name().partition(split_word)[2]
                    vlayer.renameAttribute(idx, new_name)
            vlayer.commitChanges()
            qgis.core.QgsProject.instance().addMapLayer(vlayer)
            qgislayer = self.mainifacewidget.qgiscanvas.layers['edge']['layerqgis']

            for join in qgislayer.vectorJoins():
                qgislayer.removeJoin(join.joinLayerId())
            # join between itv result table and qgis edge layer
            joinObject = qgis.core.QgsVectorLayerJoinInfo()
            joinObject.setJoinFieldName("id_edge")
            joinObject.setTargetFieldName("id_edge")
            joinObject.setJoinLayerId(vlayer.id())
            joinObject.setUsingMemoryCache(True)
            joinObject.setPrefix("")
            joinObject.setJoinLayer(vlayer)

            self.mainifacewidget.qgiscanvas.layers['edge']['layerqgis'].addJoin(joinObject)

            qgislayer.startEditing()
            for field in qgislayer.fields():
                if 'etat' in field.name():
                    idx = qgislayer.fields().indexFromName(field.name())
                    split_word = 'etat'
                    new_name = split_word + field.name().partition(split_word)[2]
                    qgislayer.renameAttribute(idx, new_name)
                elif 'note' in field.name():
                    idx = qgislayer.fields().indexFromName(field.name())
                    split_word = 'note'
                    new_name = split_word + field.name().partition(split_word)[2]
                    qgislayer.renameAttribute(idx, new_name)
            qgislayer.commitChanges()

            self.indicator_changed()
    
    def indicator_changed(self):
        path_file = os.path.join(os.path.dirname(Lamia.__file__), "config/base3_urbandrainage/lamiaITVimport/" + self.toolwidgetmain.comboBox_indicator.currentText() + "_style.qml")
        layer_to_change = self.mainifacewidget.qgiscanvas.layers['edge']['layerqgis']
        try:
            layer_to_change.loadNamedStyle(path_file)
        except:
            print("change style failed")
        self.mainifacewidget.qgiscanvas.layers["edge"]['layerqgis'].triggerRepaint()

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_rereau_ui.ui")
        uic.loadUi(uipath, self)


class RereaufileManager(AbstractFileManager):

    def __init__(self, mainwindows=None, toolclass=None):
        super(RereaufileManager, self).__init__(mainwindows, toolclass)
        self.reset()

    def new(self):
        """
        add a new configuration
        """
        self.popupwidget = Config_Manager(parent=self)
        self.popupwidget.exec_()
        alpha, P = self.popupwidget.dialogIsFinished()
        config = {"alpha": alpha, "P": P}
        if alpha is not None and P is not None and "alpha_%.2f_P_%.2f.json" % (alpha, P) not in [self.comboBox_files.itemText(i) for i in range(self.comboBox_files.count())]:
            file_name = os.path.join(self.toolclass.confdatadirproject, "alpha_%.2f_P_%.2f.json" % (alpha, P))
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=4)
            self.reset()

    def edit(self):
        """
        edit configuration file
        """
        with open(os.path.join(self.toolclass.confdatadirproject, self.getCurrentText())) as json_file:
            config = json.load(json_file)
        self.popupwidget = Config_Manager(parent=self)
        self.popupwidget.doubleSpinBox_alpha.setValue(config["alpha"])
        self.popupwidget.doubleSpinBox_P.setValue(config["P"])
        self.popupwidget.exec_()
        alpha, P = self.popupwidget.dialogIsFinished()
        if alpha is not None and P is not None and "alpha_%.2f_P_%.2f.json" % (alpha, P) not in [self.comboBox_files.itemText(i) for i in range(self.comboBox_files.count())]:
            self.delete()
            config = {"alpha":alpha, "P":P}
            if alpha is not None and P is not None and "alpha_%.2f_P_%.2f.json" % (alpha, P) not in [self.comboBox_files.itemText(i) for i in range(self.comboBox_files.count())]:
                config = {"alpha":alpha, "P":P}
                file_name = os.path.join(self.toolclass.confdatadirproject, "alpha_%.2f_P_%.2f.json" % (alpha, P))
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(config, f, ensure_ascii=False, indent=4)
                self.reset()

    def reset(self):
        """
        reset comboBox_files, used to select configuration
        """
        self.toolclass.getNamePathFiles()
        self.comboBox_files.clear()
        config = {"alpha":2, "P":5}
        file_name = os.path.join(self.toolclass.confdatadirproject, "alpha_2.00_P_5.00.json")
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
        for file in os.listdir(self.toolclass.confdatadirproject):
            if file.endswith(".json"):
                self.comboBox_files.addItems([file])
                self.comboChanged()

    def delete(self):
        """
        delete active configuration
        """
        currentxt = self.getCurrentText()
        if "alpha_2.00_P_5.00.json" not in currentxt:
            currentfilepath = os.path.join(self.toolclass.confdatadirproject, currentxt)
            
            os.remove(currentfilepath)
            self.reset()

    def comboChanged(self):
        """
        enable or desanable EDIT and DELETE button
        """
        if self.comboBox_files.count() > 1 and "alpha_2.00_P_5.00.json" not in self.getCurrentText():
            boolenabled = True
        else:
            boolenabled = False

        self.toolButton_edit.setEnabled(boolenabled)
        self.toolButton_delete.setEnabled(boolenabled)


class Config_Manager(QDialog):
    """
    open a popup to define alpha and P
    """
    def __init__(self, parent=None):
        super(Config_Manager, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_popup_rereau_ui.ui")

        uic.loadUi(uipath, self)

        self.finished.connect(self.dialogIsFinished)

    def dialogIsFinished(self):
        """
        return (None, None) if canceled,
        return (alpha, P) if validated.
        """

        if self.result() == QDialog.Accepted:
            return (
                self.doubleSpinBox_alpha.value(),
                self.doubleSpinBox_P.value(),
            )
        else:
            return (None, None)
