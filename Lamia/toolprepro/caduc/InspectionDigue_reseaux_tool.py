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


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'reseauxTool.ui'))



class reseauxTool(AbstractInspectionDigueTool,FORM_CLASS):
    
    def __init__(self, dbase,dialog, linkedtreewidget , parent=None):
        #AbstractInspectionDigueTool.__init__(self,dbase,dialog)
        super(reseauxTool,self).__init__(dbase,dialog,linkedtreewidget,parent = parent)
        


        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Description'
        self.NAME = 'Reseaux'
        self.sourcelayername = 'reseaux'
        #self.iconpath = os.path.join(os.path.dirname(__file__),'..','icons','tools','Video_48x48.png' )
        
        from .InspectionDigue_reseaux_spe_tool import reseauxspeTool
        self.reseauxspetool =  reseauxspeTool(self.dbase, self.windowdialog, self.treeWidget_resspe , parent = self)
        layout = self.frame_resspe.layout()
        layout.addWidget(self.reseauxspetool)
        self.treeWidget_resspe.itemClicked.connect(self.reseauxspetool.featureSelected)
        self.pushButton_add_resspe.clicked.connect(self.reseauxspetool.addFeature)
        self.pushButton_del_resspe.clicked.connect(self.reseauxspetool.deleteFeature)

        #pickopt
        self.pickoptions = [[self.pushButton_Pick_view_2,self.pushButton_show_link_2,'troncons', self.spinBox_ID_2]]
        
        self.tools.append(self.reseauxspetool)
        
    def onActivation(self):
        pass

    def onDesactivation(self):
        pass
        
        
        
    def showFeatureWidget(self,featureid = None):
        if featureid is not None:
            self.reseauxspetool.currentparentfeature =  [self,self.currentFeature]
            self.reseauxspetool.loadFeaturesinTreeWdg()
        else:
            self.reseauxspetool.currentparentfeature = [self,None]
            self.reseauxspetool.loadFeaturesinTreeWdg()
        
        
        
        

        
        
        
        

        
