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
    """
    CAT = 'Description'
    NAME = 'test'
    """
    def __init__(self, dbase,dialog, parent=None):
        #AbstractInspectionDigueTool.__init__(self,dbase,dialog)
        super(desordresTool,self).__init__(dbase,dialog)
        
        
        # signals
        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Desordres'
        self.NAME = 'Desordres'
        self.sourcelayername = 'desordres'
        self.currentobsfeature = None
        
        self.itemtempobs = None
        #print('initTool', self.sourcelayername)
        #self.iconpath = os.path.join(os.path.dirname(__file__),'..','icons','tools','Video_48x48.png' )
        self.pushButton_add_obs.clicked.connect(self.addObservation)
        self.pushButton__del_obs.clicked.connect(self.delObservation)
        self.pushButton_saveobs.clicked.connect(self.saveObservation)

                    
        
    def onActivation(self):
        self.initCombobox(self.dbase.dbase_desordres_obs, self)

    def onDesactivation(self):
        try:
            self.treeWidget_observation.itemClicked.disconnect(self.obsSelected)
        except:
            pass
        
        
    def showFeatureWidget(self,featureid = None):
        #load observations layer_desordres_obs
        try:
            self.treeWidget_observation.itemClicked.disconnect(self.obsSelected)
        except:
            pass
        self.dbaseobsused = self.dbase.dbase_desordres_obs
        
        from .InspectionDigue_photographies_tool import photographiesTool
        self.phototool =  photographiesTool(self.dbase, self.windowdialog)
        layout=QtGui.QVBoxLayout()
        layout.addWidget(self.phototool)
        self.frame_ph.setLayout(layout)
        
        
        if featureid is not None:
            self.updateObservationTree(featureid)
        
            
            
    def updateObservationTree(self, featureid):
        try:
            self.treeWidget_observation.itemClicked.disconnect(self.obsSelected)
        except:
            pass
        #clear ElemtreeWidget
        for i in range(self.treeWidget_observation.invisibleRootItem().childCount()):
            self.treeWidget_observation.invisibleRootItem().removeChild(self.treeWidget_observation.invisibleRootItem().child(0))
    
        featlist = []
        request = qgis.core.QgsFeatureRequest( qgis.core.QgsExpression('DES_ID = '+str(featureid)) )
        for feat in self.dbase.layer_desordres_obs.getFeatures(request):
                featlist.append( feat.id()) 
        featlist.sort()
        self.treeWidget_observation.addTopLevelItems([ QtGui.QTreeWidgetItem([str(id)]) for id in featlist] )
        
        self.treeWidget_observation.itemClicked.connect(self.obsSelected)
                    
                    
        
    def obsSelected(self,item):
    
        try:
            self.treeWidget_observation.invisibleRootItem().removeChild(self.itemtempobs)
        except Exception as e:
            print(e)
    
        id = int(item.text(0))
        self.currentobsfeature =  self.dbase.layer_desordres_obs.getFeatures(qgis.core.QgsFeatureRequest(id)).next()
        
        self.initFeatureProperties(self.currentobsfeature, self.dbaseobsused, self)
        
        
    def addObservation(self):
        self.itemtempobs = QtGui.QTreeWidgetItem(['nouvelle entree'])
        self.treeWidget_observation.addTopLevelItems([ self.itemtempobs ] )
        self.treeWidget_observation.itemClicked.disconnect(self.obsSelected)
        self.treeWidget_observation.setCurrentItem(self.itemtempobs)
        self.treeWidget_observation.itemClicked.connect(self.obsSelected)
        self.initFeatureProperties(None, self.dbaseobsused, self)
        self.currentobsfeature = None
        
        
    def delObservation(self):
        feat = self.currentobsfeature
        layer =  self.dbase.layer_desordres_obs
        layer.startEditing()
        layer.deleteFeature(feat.id())
        layer.commitChanges()
        self.updateObservationTree(self.currentFeature.id())
        self.currentobsfeature = None
        
    def saveObservation(self):
        if self.currentobsfeature is None:
            self.currentobsfeature = qgis.core.QgsFeature(self.dbase.layer_desordres_obs.fields())
            print(self.currentobsfeature.id(), self.currentFeature.id())
            self.currentobsfeature.setAttribute('DES_ID', self.currentFeature.id())
            
        self.saveFeatureProperties(self.dbase.layer_desordres_obs,self.currentobsfeature,self.dbaseobsused, self)
        print('cur feat',self.currentFeature.id())
        self.updateObservationTree(self.currentFeature.id())
        self.currentobsfeature = None
        

        
        

        
        
        
        

        
