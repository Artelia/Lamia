# -*- coding: utf-8 -*-

"""
/***************************************************************************
 PostTelemac
                                 A QGIS plugin
 Post Traitment or Telemac
                              -------------------
        begin                : 2015-07-07
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Artelia
        email                : patrice.Verchere@arteliagroup.com
 ***************************************************************************/
 
 ***************************************************************************/
 get Image class
 Generate a Qimage from selafin file to be displayed in map canvas 
 with tht draw method of posttelemacpluginlayer
 
Versions :
0.0 : debut

 ***************************************************************************/
"""


from qgis.PyQt import uic, QtCore, QtGui
from .InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import qgis
import os
import glob
import datetime

from ..maptool.mapTools import mapToolAddFeature, mapToolAddLine, mapToolCapture


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'structureselementsTool.ui'))



class structuresElementsTool(AbstractInspectionDigueTool,FORM_CLASS):

    def __init__(self, dbase,dialog, linkedtreewidget, parent=None):
        super(structuresElementsTool,self).__init__(dbase,dialog,linkedtreewidget,parent = parent)

        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Description'
        self.NAME = 'Elements de structure'
        self.sourcelayername = 'structures_elements'
        #self.iconpath = os.path.join(os.path.dirname(__file__),'..','icons','tools','Video_48x48.png' )
        self.pickoptions = [[self.pushButton_Pick_view,self.pushButton_show_link,'structures', self.spinBox_link_struc_id]]
        self.doubleSpinBox_larg.valueChanged.connect(self.updateFruit)
        self.doubleSpinBox_haut.valueChanged.connect(self.updateFruit)
        
        

        
        
        
    def onActivation(self):
        print('activ')


    def onDesactivation(self):
        pass


        
    def showFeatureWidget(self,featureid = None):
        pass

        
    def updateFruit(self,value):
        if self.doubleSpinBox_haut.value()>0:
            fruit = float(self.doubleSpinBox_larg.value()) / float(self.doubleSpinBox_haut.value())
            self.doubleSpinBox_fruit.setValue(fruit)
        else:
            self.doubleSpinBox_fruit.setValue(-1.0)
        
        

        
        
        
        

        
