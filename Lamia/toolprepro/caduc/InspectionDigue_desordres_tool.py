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


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'desordresTool.ui'))



class desordresTool(AbstractInspectionDigueTool,FORM_CLASS):

    def __init__(self, dbase,dialog, linkedtreewidget, parent=None):
        super(desordresTool,self).__init__(dbase,dialog,linkedtreewidget,parent = parent)
        
        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Desordres'
        self.NAME = 'Desordres'
        self.sourcelayername = 'desordres'

        from .InspectionDigue_desordres_obs_tool import desordresobsTool
        self.desordreobstool =  desordresobsTool(self.dbase, self.windowdialog,self.treeWidget_observation,parent = self)
        layout = self.frame_desordre_obs.layout()
        layout.addWidget(self.desordreobstool)
        self.treeWidget_observation.itemClicked.connect(self.desordreobstool.featureSelected)
        self.pushButton_add_obs.clicked.connect(self.desordreobstool.addFeature)
        self.pushButton__del_obs.clicked.connect(self.desordreobstool.deleteFeature)
        self.pickoptions = [[self.pushButton_Pick_elem,self.pushButton_show_link,self.comboBox_link_des, self.spinBox__link_des_id]]
        
        self.tools.append(self.desordreobstool)
                    
        
    def onActivation(self):
        pass

    def onDesactivation(self):
        pass


            
        
    def showFeatureWidget(self,featureid = None):
        if featureid is not None:
            self.desordreobstool.currentparentfeature =[self,self.currentFeature]
            self.desordreobstool.loadFeaturesinTreeWdg()
        else:
            self.desordreobstool.currentparentfeature = [self,None]
            self.desordreobstool.loadFeaturesinTreeWdg()

        

        
        

        
        
        
        

        
