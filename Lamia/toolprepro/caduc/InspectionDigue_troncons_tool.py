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

from ..maptool.mapTools import mapToolAddFeature, mapToolAddLine, mapToolCapture


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'tronconsTool.ui'))



class tronconsTool(AbstractInspectionDigueTool,FORM_CLASS):
    
    def __init__(self, dbase,dialog, linkedtreewidget , parent=None):
        #AbstractInspectionDigueTool.__init__(self,dbase,dialog)
        super(tronconsTool,self).__init__(dbase,dialog,linkedtreewidget,parent = parent)
        


        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Description'
        self.NAME = 'Troncons'
        self.sourcelayername = 'troncons'
        #self.iconpath = os.path.join(os.path.dirname(__file__),'..','icons','tools','Video_48x48.png' )

        
        
    def onActivation(self):
        pass

    def onDesactivation(self):
        pass
        
        
        
    def showFeatureWidget(self,featureid = None):
        pass
        
        
        
        
        

        
        
        
        

        
