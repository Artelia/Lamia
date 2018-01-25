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


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'desordresobsTool.ui'))



class desordresobsTool(AbstractInspectionDigueTool,FORM_CLASS):

    def __init__(self, dbase,dialog, linkedtreewidget, parent=None):

        super(desordresobsTool,self).__init__(dbase,dialog,linkedtreewidget,parent = parent)
        
        
        # signals
        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Desordres'
        self.NAME = 'Desordres_observations'
        self.sourcelayername = 'desordres_obs'
        
        #self.itemtempobs = None

        #self.iconpath = os.path.join(os.path.dirname(__file__),'..','icons','tools','Video_48x48.png' )
        
        from .InspectionDigue_photographies_tool import photographiesTool
        self.phototool =  photographiesTool(self.dbase, self.windowdialog, self.treeWidget_ph , parent = self)
        layout = self.frame_ph.layout()
        layout.addWidget(self.phototool)
        self.treeWidget_ph.itemClicked.connect(self.phototool.featureSelected)
        self.pushButton_add_ph.clicked.connect(self.phototool.addFeature)
        self.pushButton_del_ph.clicked.connect(self.phototool.deleteFeature)
        
        self.tools.append(self.phototool)
                    
        
    def onActivation(self):

        pass

    def onDesactivation(self):
        pass

            
            
        
    def showFeatureWidget(self,featureid = None):
        if featureid is not None:
            self.phototool.currentparentfeature =[self,self.currentFeature]
            self.phototool.loadFeaturesinTreeWdg()
        else:
            self.phototool.currentparentfeature = [self,None]
            self.phototool.loadFeaturesinTreeWdg()
            




        
        

        
        
        
        

        
