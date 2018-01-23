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

from __future__ import unicode_literals
#from PyQt4 import uic, QtCore, QtGui
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QWidget, QTreeWidgetItem,QMessageBox
except:
    from qgis.PyQt.QtWidgets import QWidget, QTreeWidgetItem;QMessageBox
import os
import qgis
from ..maptool.mapTools import mapToolAddFeature, mapToolAddLine, mapToolCapture

import datetime


class AbstractInspectionDigueTool(QWidget):
    
    saveFeatureSignal = QtCore.pyqtSignal()
    
    def __init__(self, dbase,dialog, linkedtreewidget = None , parent=None):
        """!
        Abstract class for working on table
        @param dbase : The dbase class linked
        @param dialog : the main dialog widget
        @param linkedtreewidget  : the treewidget it interacts with
        @param parent : the parent widget (TODO : the same as dialog)
        """

        super(AbstractInspectionDigueTool, self).__init__(parent)

        #***************************************************************
        # ******************   Variables def ****************************
        # ***************************************************************


        #***** Data base var
        ## the dbaseparser
        self.dbase = dbase
        ## the current widget feature selected in self.linkedtreewidget
        self.currentFeature = None
        ## the current feature selected when widget is linked withh a parent feature
        self.currentparentfeature = None

        # ***** Ui var
        ## Name used for rool tree in main qtreewidget
        self.CAT = None
        ## Name used for child tree in main qtreewidget
        self.NAME = None
        ## Main window widget
        self.windowdialog = dialog
        ## MaintreeWidget qtreewidgetitem
        self.qtreewidgetitem = None
        ## the qtreewidget within the features are displayed
        self.linkedtreewidget = linkedtreewidget

        # ***** QGis var
        ## qgis map canvas
        self.canvas = self.windowdialog.canvas
        ##layer shown in cnvas or not
        self.layerdisplayed = False


        self.mtool = None                                 #the capture map tool


        self.widgetindex = None                         # current widget index
        self.iconpath = None
        


        self.layers = None                              # the layers linked with the widget
        self.sourcelayername = None                     #the name of sourcelayer (troncons...
        self.dbaseused = None                           # the dbase spec for sourcelayer
        self.windowsonlyfeature = 0                     #show only mapcanvs inise feature in linkedtreewidget
        self.mtool = None                               #the capture tool
        self.actuallayerindex  = None                   #for layer with two geoemtry type (point,line), the actual layer index referrint to dbused['type']
        self.rubberBand = None                          #the rubberband for new geometry
        self.tempgeometry  = None                       #the geoemtryr captured
        self.itemtemp = QTreeWidgetItem(['nouvelle entree'])    #used for add new feature


        self.pointEmitter = qgis.gui.QgsMapToolEmitPoint(self.canvas)   # maptoolused for picking
        self.pickoptions = None                         #for picker : used to connect the button  pick ,the button  show, and the combobox where the result is displayer ex : [[self.pushButton_Pick_elem,self.pushButton_show_link,self.comboBox_link_des, self.spinBox__link_des_id]]
        self.picklayername = None                       #the layername withon we want to pick
        self.pickspinbox = None                         #the spin box where is displayed the id of the picked feature
        self.tools = []                                 #the tools inside the actual tool

        #load tools - must be kept in thos order
        self.initTool()
        #specific var
        if self.dbaseused is None and self.sourcelayername is not None:
            exec("self.dbaseused = self.dbase.dbase_"+self.sourcelayername)     #sourcelayername defined after initTool
            #self.initCombobox(self.dbaseused, self)

            # signal connections
            self.windowdialog.dbase.dBaseLoaded.connect(self.DBaseLoaded)
            if False:
                self.pushButton_saveFeature.clicked.connect(self.saveFeature)
                if self.pickoptions  is not None:
                    for elem in self.pickoptions:
                        elem[0].clicked.connect(self.pickFeature)
                        elem[1].clicked.connect(self.showLinkedFeature)
                for elem in self.dbaseused['type']:
                    try:
                        eval("self.pushButton_"+elem+".clicked.connect(self.addgeom)" )
                    except Exception as e:
                        pass

        
    def initTool(self):
        """
        Load widget and icons and init things
        must contain :
            self.setupUi(self)
            self.iconpath = '...path to icon...'
        """
        pass
        
        
    def onActivation(self):
        pass
        
    def onDesactivation(self):
        pass
        
    def showFeatureWidget(self,featureid=None):
        pass
        
    
    
    def loadWidget(self):
        """!
        Called on the widget creation in windowsdialog
        DO:
        load the widget in the main stacked widget
        call onActivationRaw when qtreewidgetitem is clicked in MaintreeWidget
        """
        # add qtreewidget item in MaintreeWidget
        arb=[self.CAT,self.NAME]
        self.qtreewidgetitem = QTreeWidgetItem()
        self.qtreewidgetitem.setText(0,arb[-1])
        self.qtreewidgetitem.setFlags(self.qtreewidgetitem.flags() | QtCore.Qt.ItemIsUserCheckable)
        self.qtreewidgetitem.setCheckState(0, QtCore.Qt.Unchecked)
        if self.iconpath != None:
            self.qtreewidgetitem.setIcon(0,QtGui.QIcon(self.iconpath))
        wdgitem = None
        root = self.windowdialog.MaintreeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            if item.text(0) == arb[0]:
                wdgitem = item
                break
        if wdgitem is None:
            wdgitem = QTreeWidgetItem()
            wdgitem.setText(0,arb[0]) 
            self.windowdialog.MaintreeWidget.addTopLevelItems([wdgitem])
        wdgitem.addChild(self.qtreewidgetitem )
        wdgitem.setExpanded(True)

        # add widget of inherited class
        self.windowdialog.stackedWidgetTool.addWidget(self)
        self.widgetindex = self.windowdialog.stackedWidgetTool.indexOf(self)
        
        #connect signals of inherited widget
        self.windowdialog.MaintreeWidget.itemClicked.connect(self.onActivationRaw)

                
                
    def DBaseLoaded(self):
        """!
        update layers when a dbase is loaded - activated on dbase qsignal
        TODO : to remove....
        """
        if False:
            self.layers = []
            if len(self.dbaseused['type'] )>0:
                for type in self.dbaseused['type'] :
                    exec("self.layers.append( self.dbase.layer_"+self.sourcelayername+'_'+type+')' )
            else:
                exec("self.layers.append( self.dbase.layer_"+self.sourcelayername+')' )
        pass


    def loadFeaturesinTreeWdg(self):
        """!
        load features in self.linkedtreewidget
        called whenever the list need to be reinitialized (ex : click in maintreewidget,...)
        """
        #clear treewidget
        if True:
            for i in range(self.linkedtreewidget.invisibleRootItem().childCount()):
                self.linkedtreewidget.invisibleRootItem().removeChild(self.linkedtreewidget.invisibleRootItem().child(0))
        else:   
            self.linkedtreewidget.clear()   #not used it deletes the qtreewidget....
        
        #selection of particular feature to load (if parentfeature, or window only mode)
        if self.currentparentfeature is None:
            if self.windowsonlyfeature   == 2 :
                xform = qgis.core.QgsCoordinateTransform(self.canvas.mapSettings().destinationCrs(), self.layers[0].crs() )
                request = qgis.core.QgsFeatureRequest().setFilterRect(xform.transform( qgis.utils.iface.mapCanvas().extent()) )
            else:
                request = qgis.core.QgsFeatureRequest()
        else:
            if self.currentparentfeature[1] is not None:
                expr=''
                for link in self.dbaseused['linkfield']:
                    if link[0] is None :
                        if link[1] == self.currentparentfeature[0].sourcelayername:
                            expr = '"' + link[2]  + '" = ' + str(self.currentparentfeature[1].id())
                    else:
                        parentname = [temp[1] for temp in link[1]]
                        if self.currentparentfeature[0].sourcelayername in parentname:
                            trigram = self.dbase.dbase_tables[[elem[1] for elem in self.dbase.dbase_tables].index(self.currentparentfeature[0].sourcelayername)][0]
                            expr = '"' + link[2] + '" = ' + str(self.currentparentfeature[1].id()) + ' AND "' + link[0]+'" = ' + "'" + trigram + "'"

                if len(expr)>0:
                    exec ("request = qgis.core.QgsFeatureRequest(qgis.core.QgsExpression(expr))")
                else:
                    request = qgis.core.QgsFeatureRequest()
            else:
                #request = qgis.core.QgsFeatureRequest()
                self.setEnabled(False)
                return



        #filling tre widget
        featlist = []
        if self.layers is not None:
            for layer in self.layers :
                for feat in layer.getFeatures(request):
                    if len(self.dbaseused['type'] )>0:
                        if not isinstance( feat.geometry(), QtCore.QPyNullVariant) and not feat.geometry() is None:
                            featlist.append( feat.id()) 
                    else:
                        if not isinstance( feat.geometry(), QtCore.QPyNullVariant) :
                            featlist.append( feat.id()) 
            featlist.sort()
            self.treefeatlist = [ [id,QTreeWidgetItem([str(id)])] for id in featlist]
            self.linkedtreewidget.addTopLevelItems([elem[1] for elem in self.treefeatlist ])

            if len(featlist)>0:
                self.linkedtreewidget.itemClicked.emit(self.treefeatlist[0][1],1)
            else:
                self.initFeatureProperties(None, self.dbaseused, self)
                if self.currentparentfeature is not None:
                    self.showFeatureWidget()
                self.setEnabled(False)
                for tool in self.tools:
                    tool.setEnabled(False)
                    
                
        
    def onDesactivationRaw(self):
        #reinit
        self.currentFeature = None
        if self.rubberBand is not None:
            self.rubberBand.reset(0)
        self.rubberBand = None
        
        #disconnection
        try:
            self.linkedtreewidget.itemClicked.disconnect(self.featureSelected)
        except:
            pass
        try:
            qgis.utils.iface.mapCanvas().extentsChanged.disconnect(self.loadFeaturesinTreeWdg)
        except:
            pass
        try:
            self.windowdialog.checkBox_onlyvisible.stateChanged.disconnect(self.loadFeaturesinTreeWdg)
        except:
            pass
        try:
            self.pushButton_saveFeature.disconnect(self.saveFeature)
        except:
            pass

        
    def onActivationRaw(self, param1, param2 = None):
        """
        Mangage the activation of tool when tool's icon is clicked on main tree widget
        Do:
        display tool widget
        load features in ElemtreeWidget
        connect ElemtreeWidget click to featureSelected
        TODO : display or not the layer
        """
        if isinstance(param1, QTreeWidgetItem):    #signal from treeWidget_utils
            if param1 == self.qtreewidgetitem:
                #manage display
                if self.layerdisplayed:
                    qgis.utils.iface.setActiveLayer(self.dbase.dbasetables[self.dbtablename]['layer'])
                if self.qtreewidgetitem.checkState(0) == 2 and self.layerdisplayed == False :
                    #qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbase.dbasetables[self.dbtablename]['layer'],True)
                    #qgis.utils.iface.legendInterface().setLayerVisible(self.dbase.dbasetables[self.dbtablename]['layer'], True)
                    self.dbase.dbasetables[self.dbtablename]['layer'].setOpacity(1.0)
                    print('active')
                    self.layerdisplayed = True
                elif self.qtreewidgetitem.checkState(0) == 0 and self.layerdisplayed == True :
                    #qgis.core.QgsMapLayerRegistry.instance().removeMapLayer (self.dbase.dbasetables[self.dbtablename]['layer'])
                    #qgis.utils.iface.legendInterface().setLayerVisible(self.dbase.dbasetables[self.dbtablename]['layer'], False)
                    self.dbase.dbasetables[self.dbtablename]['layer'].setOpacity(0.0)
                    print('unactive')
                    self.layerdisplayed = False


                self.windowdialog.stackedWidgetTool.setCurrentWidget(self)
                if self.dbaseused is not None:
                    #self.windowdialog.checkBox_onlyvisible.setCheckState(self.windowsonlyfeature)
                    #self.windowdialog.checkBox_onlyvisible.stateChanged.connect(self.CheckBoxOnlyvisibleChecked)
                    self.loadFeaturesinTreeWdg()    #after self.layer and self.dbaseused are not None
                    # connection
                    self.linkedtreewidget.itemClicked.connect(self.featureSelected)
                    #inherited class call
                    self.initFeatureProperties(None, self.dbaseused, self)
                    try:
                        self.tabWidget_main.setCurrentIndex(0)
                    except:
                        pass
                    self.setEnabled(False)
                self.onActivation()
            else:
                self.onDesactivationRaw()
                #inherited class call
                self.onDesactivation()
        
    def CheckBoxOnlyvisibleChecked(self,state):
        self.windowsonlyfeature = self.windowdialog.checkBox_onlyvisible.checkState()
        if self.windowsonlyfeature == 2:
            qgis.utils.iface.mapCanvas().extentsChanged.connect(self.loadFeaturesinTreeWdg)
        else:
            try:
                qgis.utils.iface.mapCanvas().extentsChanged.disconnect(self.loadFeaturesinTreeWdg)
            except:
                pass
        self.loadFeaturesinTreeWdg()

    if False:
            
        def featureSelected(self,item=None):
            """
            item : if none, add new feature else show properties of id selected
            """
            # init things
            #remove selection in case no parent layer
            if self.currentparentfeature is None:
                for layer in self.dbase.layers:
                    layer.removeSelection()
            #remove nouvelle entree item
            try:
                self.linkedtreewidget.invisibleRootItem().removeChild(self.itemtemp)
            except Exception as e:
                print(e)

            if not self.isEnabled():
                self.setEnabled(True)

            id = None
            self.currentFeature = None

            if item is not None:
                id = int(item.text(0))
                for i, layer in enumerate(self.layers):
                    self.currentFeature = layer.getFeatures(qgis.core.QgsFeatureRequest(id)).next()
                    if len(self.dbaseused['type'] )>0:
                        if not isinstance( self.currentFeature.geometry(), QtCore.QPyNullVariant) and not self.currentFeature.geometry() is None:
                            self.actuallayerindex = i
                            break
                    else:
                        if not isinstance( self.currentFeature.geometry(), QtCore.QPyNullVariant) :
                            self.actuallayerindex = i
                            break
            else:
                self.itemtemp = QTreeWidgetItem(['nouvelle entree'])
                self.linkedtreewidget.addTopLevelItems([ self.itemtemp ] )
                self.linkedtreewidget.itemClicked.disconnect(self.featureSelected)
                self.linkedtreewidget.setCurrentItem(self.itemtemp)
                self.linkedtreewidget.itemClicked.connect(self.featureSelected)
                self.actuallayerindex = None

                for tool in self.tools:
                    tool.setEnabled(False)

                try:
                    self.tabWidget_main.setCurrentIndex(0)
                except:
                    pass

            self.updateCaptureButton(self.currentFeature)

            if self.actuallayerindex is not None:
                if self.rubberBand is not None:
                    self.rubberBand.reset(self.layers[self.actuallayerindex].geometryType())
                self.tempgeometry = None
                if item is not None and self.currentparentfeature is None:
                    self.layers[self.actuallayerindex].setSelectedFeatures( [self.currentFeature.id()] )
            else:
                if self.rubberBand is not None:
                    self.rubberBand.reset(self.layers[0].geometryType())

            self.initFeatureProperties(self.currentFeature, self.dbaseused, self)

            self.showFeatureWidget(id)



        def saveFeature(self):
            if self.actuallayerindex is None:   #case no geometry has been captured - non spatial layer
                if len(self.dbaseused['type']) > 0:
                   layerwithnogeometry = False
                else:
                    layerwithnogeometry = True
                self.actuallayerindex = 0

            else:
                layerwithnogeometry = False

            if self.currentFeature is None:
                self.currentFeature = qgis.core.QgsFeature(self.layers[self.actuallayerindex].fields())
                if self.tempgeometry is not None  :
                    self.currentFeature.setGeometry(self.tempgeometry)
                else:
                    if not layerwithnogeometry:
                        qgis.utils.iface.messageBar().pushMessage("InspectionDigue", 'Pas de geometrie selectionnee !!', level=qgis.gui.QgsMessageBar.WARNING, duration=3)
                        self.currentFeature = None
                        return
                selectlastitemintree = True
            else:
                if self.tempgeometry is not None  :
                    self.currentFeature.setGeometry(self.tempgeometry)
                selectlastitemintree = False

            self.saveFeatureProperties(self.layers[self.actuallayerindex],self.currentFeature,self.dbaseused, self)

            if qgis.utils.iface is not None:
                qgis.utils.iface.messageBar().pushMessage("InspectionDigue", 'Sauvegarde effectuee', level=qgis.gui.QgsMessageBar.SUCCESS, duration=3)

            if self.rubberBand is not None:
                self.rubberBand.reset(self.layers[self.actuallayerindex].geometryType())
            self.tempgeometry = None

            if True and selectlastitemintree:
                self.loadFeaturesinTreeWdg()
                self.linkedtreewidget.setCurrentItem(self.treefeatlist[-1][1])
                self.featureSelected(self.treefeatlist[-1][1])



        def addgeom(self):

            source = self.sender()
            if 'point' in source.objectName():
                type = 0
                typename = 'point'
            elif 'line' in source.objectName():
                type = 1
                typename = 'line'
            elif 'polygon' in source.objectName():
                type = 2
                typename = 'polygon'

            self.actuallayerindex = self.dbaseused['type'].index(typename)

            # rubberband things
            if self.rubberBand is not None:
                self.rubberBand.reset(self.layers[self.actuallayerindex].geometryType())
            else:
                self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,
                                                         self.layers[self.actuallayerindex].geometryType())
            self.rubberBand.setWidth(5)
            self.rubberBand.setColor(QtGui.QColor("magenta"))


            try:
                if type == qgis.core.QgsWkbTypes.PointGeometry :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint
                elif type == qgis.core.QgsWkbTypes.LineGeometry  :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CaptureLine
                elif type == qgis.core.QgsWkbTypes.PolygonGeometry   :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CapturePolygon
                else:
                    return
            except:
                if type == qgis.core.QGis.Point :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint
                elif type == qgis.core.QGis.Line  :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CaptureLine
                elif type == qgis.core.QGis.Polygon   :
                    mode = qgis.gui.QgsMapToolAdvancedDigitizing.CapturePolygon
                else:
                    return

            self.mtool = mapToolCapture( self.canvas, qgis.utils.iface.cadDockWidget(), mode , self.layers[self.actuallayerindex] )
            self.canvas.setMapTool(self.mtool)
            self.mtool.stopCapture.connect(self.setTempGeometry)
            self.mtool.startCapturing()

        def setTempGeometry(self,points):

            #crs thiings things
            xform = qgis.core.QgsCoordinateTransform( self.canvas.mapSettings().destinationCrs(),self.layers[self.actuallayerindex].crs() )
            points2=[]
            for point in points:
                points2.append(xform.transform(point))


            if len(points) == 1 or self.mtool.mode() == qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint  :
                geometryformap = qgis.core.QgsGeometry.fromPoint(points[0])
                geometryforlayer = qgis.core.QgsGeometry.fromPoint(points2[0])
            elif self.mtool.mode() == qgis.gui.QgsMapToolAdvancedDigitizing.CaptureLine:
                geometryformap = qgis.core.QgsGeometry.fromMultiPolyline([points])
                geometryforlayer = qgis.core.QgsGeometry.fromMultiPolyline([points2])
            elif self.mtool.mode() == qgis.gui.QgsMapToolAdvancedDigitizing.CapturePolygon :
                geometryformap = qgis.core.QgsGeometry.fromPolygon([points])
                geometryforlayer = qgis.core.QgsGeometry.fromPolygon([points2])


            self.rubberBand.addGeometry(geometryformap, None)
            self.rubberBand.show()
            self.tempgeometry = geometryforlayer


        def updateCaptureButton(self,currentfeature=None):
            if currentfeature is not None:
                for i, elem in enumerate( self.dbaseused['type'] ):
                    if i == self.actuallayerindex :
                        eval("self.pushButton_"+elem+".setEnabled(True)" )
                    else:
                        eval("self.pushButton_"+elem+".setEnabled(False)" )
            else:
                for i, elem in enumerate( self.dbaseused['type'] ):
                    eval("self.pushButton_"+elem+".setEnabled(True)" )


        def initCombobox(self,dbasetouse, widgettouse):
            for i, elem in enumerate( dbasetouse['champs']):
                if dbasetouse['QtWidget'][i] is not None:
                    if 'comboBox' in dbasetouse['QtWidget'][i]  :
                        if dbasetouse['comboboxparent'][i] is None:
                            eval("widgettouse."+dbasetouse['QtWidget'][i]+".clear()")
                            list = [elem[1] for elem in dbasetouse['combobox'][i]]
                            #list.insert(0,'')
                            eval("self."+dbasetouse['QtWidget'][i]+".addItems(list)")
                        else:
                            eval("self." +  dbasetouse['comboboxparent'][i]+ ".currentIndexChanged.connect(self.updateCombo)")
                            eval("self." +  dbasetouse['comboboxparent'][i]+ ".currentIndexChanged.emit(0)")

        def updateCombo(self):

            source = self.sender()
            #print('update',source.objectName())
            for i, comboparent in enumerate(self.dbaseused['comboboxparent']):
                if source.objectName() == comboparent:
                    list = []
                    exec("combochild = self." + self.dbaseused['QtWidget'][i])
                    parentindex = self.dbaseused['QtWidget'].index(source.objectName())
                    parentnamelist = [elem[1] for elem in self.dbaseused['combobox'][parentindex]]
                    parentnameindex = parentnamelist.index(source.currentText())
                    parentvalue = self.dbaseused['combobox'][parentindex][parentnameindex][0]
                    combochild.clear()
                    for elem in self.dbaseused['combobox'][i]:
                        if len(elem)> 2 and parentvalue in elem[2] :
                            list.append(elem[1])
                    combochild.addItems(list)




        def initFeatureProperties(self,feat, dbasetouse, widgettouse):

            forcedfields = self.getParentInitProperties(self)
            forcedfieldsfield = [elem[0] for elem in forcedfields]

            for i, elem in enumerate( dbasetouse['champs']):
                if dbasetouse['QtWidget'][i] is not None:
                    if elem in forcedfieldsfield:
                        forcedvalue = forcedfields[forcedfieldsfield.index(elem)][1]
                    else:
                        forcedvalue = None

                    if feat is not None and forcedvalue is not None and feat[elem] != forcedvalue:
                        qgis.utils.iface.messageBar().pushMessage("InspectionDigue", 'Attention valeur incoherente champ ' + elem, level=qgis.gui.QgsMessageBar.WARNING, duration=3)

                    try:
                        if 'lineEdit' in dbasetouse['QtWidget'][i]  :
                            if feat is not None and feat[elem] is not None and not isinstance(feat[elem], QtCore.QPyNullVariant):
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setText( feat[elem] )" )
                            elif feat is None and forcedvalue is not None:
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setText( forcedvalue )" )
                            else:
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setText( '' )" )

                        elif 'comboBox' in dbasetouse['QtWidget'][i]  :
                            if feat is not None and feat[elem] is not None and not isinstance(feat[elem], QtCore.QPyNullVariant):
                                listraw = [val[0] for val in dbasetouse['combobox'][i]]
                                index = listraw.index(feat[elem])
                                text = dbasetouse['combobox'][i][index][1]
                                exec("count = widgettouse." + dbasetouse['QtWidget'][i]+".count()")
                                for j in range( count):
                                    exec("textcombo =  widgettouse." + dbasetouse['QtWidget'][i]+".itemText(" + str(j) + ")" )
                                    if textcombo == text:
                                        eval("widgettouse."+dbasetouse['QtWidget'][i]+".setCurrentIndex("+str(j)+")" )
                                        break
                            elif feat is None and forcedvalue is not None:
                                listraw = [val[0] for val in dbasetouse['combobox'][i]]
                                forcedvalue = listraw.index(forcedvalue)
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setCurrentIndex (forcedvalue)" )
                            else:
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setCurrentIndex (0)" )

                        elif 'textBrowser' in dbasetouse['QtWidget'][i]  :
                            if feat is not None and feat[elem] is not None and not isinstance(feat[elem], QtCore.QPyNullVariant):
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setText( feat[elem] )" )
                            elif feat is None and forcedvalue is not None:
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setText( forcedvalue )" )
                            else:
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setText( '' )" )

                        elif 'dateEdit' in dbasetouse['QtWidget'][i]  :
                            if feat is not None and feat[elem] is not None and not isinstance(feat[elem], QtCore.QPyNullVariant):
                                #datelist = [int(dat) for dat in feat[elem].split('-')]
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setDate(QtCore.QDate.fromString(feat[elem], 'yyyy-MM-dd' ))" )
                            elif feat is None and forcedvalue is not None:
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setDate(QtCore.QDate.fromString(str(forcedvalue), 'yyyy-MM-dd' )  )" )
                            else:
                                #datelist = [int(dat) for dat in str(datetime.date.today()).split('-')]
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setDate(QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd' )  )" )

                        elif 'spinBox' in dbasetouse['QtWidget'][i] or 'doubleSpinBox' in dbasetouse['QtWidget'][i]  :
                            if feat is not None and feat[elem] is not None and not isinstance(feat[elem], QtCore.QPyNullVariant):
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setValue(feat[elem])" )
                            elif feat is None and forcedvalue is not None:
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setValue(forcedvalue)" )
                            else:
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setValue(-1)" )


                        elif 'checkBox' in dbasetouse['QtWidget'][i]  :
                            if feat is not None and feat[elem] is not None and not isinstance(feat[elem], QtCore.QPyNullVariant):
                                if int(feat[elem]):
                                    eval("widgettouse."+dbasetouse['QtWidget'][i]+".setCheckState(2)" )
                                else:
                                    eval("widgettouse."+dbasetouse['QtWidget'][i]+".setCheckState(0)" )
                            elif feat is None and forcedvalue is not None:
                                if int(forcedvalue):
                                    eval("widgettouse."+dbasetouse['QtWidget'][i]+".setCheckState(2)" )
                                else:
                                    eval("widgettouse."+dbasetouse['QtWidget'][i]+".setCheckState(0)" )
                            else:
                                eval("widgettouse."+dbasetouse['QtWidget'][i]+".setCheckState (0)" )

                    except Exception as e:
                        print('initFeatureProperties',e)


        def getParentInitProperties(self,wdg):

            forcedfields=[[None,None]]
            #catch linked fields
            if wdg.currentparentfeature is not None:
                if wdg.currentparentfeature[1] is not None:
                    for link in wdg.dbaseused['linkfield']:
                        if link[0] is None:
                            if link[1] == wdg.currentparentfeature[0].sourcelayername:
                                forcedfields.append([link[2],wdg.currentparentfeature[1].id()])
                            elif link[1] in [elem[1] for elem in wdg.currentparentfeature[0].dbaseused['linkfield'] ]:
                                linkfieldparent = wdg.currentparentfeature[0].dbaseused['linkfield']
                                champparentindex = [elem[1] for elem in linkfieldparent].index(link[1])
                                nomchamp = linkfieldparent[champparentindex][2]
                                try:
                                    forcedfields.append([link[2], wdg.currentparentfeature[1][nomchamp]])
                                except KeyError as e:
                                    if qgis.utils.iface is not None:
                                        qgis.utils.iface.messageBar().pushMessage("InspectionDigue", "Champ force " + nomchamp + " non trouve",  level=qgis.gui.QgsMessageBar.WARNING, duration=3)
                                    else:
                                        print("Champ force " + nomchamp + " non trouve")



                        else:
                            parentname = [temp[1] for temp in link[1]]
                            if wdg.currentparentfeature[0].sourcelayername in parentname:
                                trigram = wdg.dbase.dbase_tables[ [elem[1] for elem in wdg.dbase.dbase_tables].index( wdg.currentparentfeature[0].sourcelayername)][0]
                                forcedfields.append([link[2], wdg.currentparentfeature[1].id()])
                                forcedfields.append([link[0], trigram])
                                break
            return forcedfields


        def saveFeatureProperties(self,layer,feat,dbasetouse, widgettouse):
            with qgis.core.edit(layer):
                for i, elem in enumerate( dbasetouse['champs']):
                    if dbasetouse['QtWidget'][i] is not None:
                        value = None
                        if 'lineEdit' in dbasetouse['QtWidget'][i] :
                                exec("value = self."+dbasetouse['QtWidget'][i]+".text()" )
                        elif 'comboBox' in dbasetouse['QtWidget'][i] :
                                exec("text = self." + dbasetouse['QtWidget'][i]+".currentText()")
                                textlist = [temp[1] for temp in dbasetouse['combobox'][i]]
                                index = textlist.index(text)
                                value = dbasetouse['combobox'][i][index][0]
                        elif 'textBrowser' in dbasetouse['QtWidget'][i]  :
                            exec("value = self."+dbasetouse['QtWidget'][i]+".toPlainText()" )

                        elif 'spinBox' in dbasetouse['QtWidget'][i] :
                            exec("value = int(self."+dbasetouse['QtWidget'][i]+".value())" )

                        elif 'doubleSpinBox' in dbasetouse['QtWidget'][i]:
                            exec("value = float(self."+dbasetouse['QtWidget'][i]+".value())" )

                        elif 'dateEdit' in dbasetouse['QtWidget'][i]  :
                            exec("value = self."+dbasetouse['QtWidget'][i]+".date().toString('yyyy-MM-dd') " )

                        elif 'checkBox' in dbasetouse['QtWidget'][i]  :
                            exec("value = self."+dbasetouse['QtWidget'][i]+".checkState() " )
                            if int(value):
                                value = 1
                            else:
                                value = 0

                        if value is not None:
                            try:
                                feat.setAttribute (elem, value)
                            except KeyError  as e :
                                if qgis.utils.iface is not None:
                                    qgis.utils.iface.messageBar().pushMessage("InspectionDigue", 'Champ ' + elem + ' non trouve ', level=qgis.gui.QgsMessageBar.WARNING, duration=3)
                                else:
                                    print('Champ ' + elem + ' non trouve ')

                if feat.id() == 0:    #new feature
                    layer.addFeature(feat)

                layer.updateFeature(feat)


        def addFeature(self):

            if self.currentparentfeature is not None:
                if self.currentparentfeature[1] is not None:
                    self.featureSelected()
                else:
                    qgis.utils.iface.messageBar().pushMessage("InspectionDigue", "Enregistrer l'element parent d'abord ", level=qgis.gui.QgsMessageBar.WARNING, duration=3)
            else:
                self.featureSelected()




        def deleteFeature(self):
            reply = QMessageBox.question(None, 'Inspectiondigue','Etes vous sur de vouloir supprimer l element', QMessageBox.Yes, QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                with qgis.core.edit(self.layers[self.actuallayerindex]):
                    self.layers[self.actuallayerindex].deleteFeature(self.currentFeature.id())

                self.loadFeaturesinTreeWdg()

        def zoomToFeature(self):

            #self.canvas.zoomToFeatureIds(self.layers[self.actuallayerindex], [self.currentFeature.id()] )
            xform = qgis.core.QgsCoordinateTransform(self.layers[self.actuallayerindex].crs(), self.canvas.mapSettings().destinationCrs())
            point2 = xform.transform(self.currentFeature.geometry().centroid().asPoint())
            self.canvas.setCenter(point2)
            self.canvas.refresh()


        def pickFeature(self):

            source = self.sender()
            for elem in self.pickoptions:
                if source == elem[0]:
                    if isinstance(elem[2],str):
                        self.picklayername = elem[2]
                    else:
                        self.picklayername = elem[2].currentText()

                    self.pickspinbox = elem[3]


            self.pointEmitter.canvasClicked .connect(self.selectPickedFeature)
            self.canvas.setMapTool( self.pointEmitter )

        def selectPickedFeature(self, point, button):

            layername = self.picklayername

            layer, nearestid = self.getNearestId(point, layername)
            layer.setSelectedFeatures([nearestid])
            self.pickspinbox.setValue(nearestid)

            self.canvas.unsetMapTool( self.pointEmitter )
            try:
                self.pointEmitter.canvasClicked .disconnect(self.selectPickedFeature)
            except:
                pass
            self.picklayername = None
            self.pickspinbox = None

        def showLinkedFeature(self):

            source = self.sender()

            for elem in self.pickoptions:
                if source == elem[1]:
                    if isinstance(elem[2],str):
                        self.picklayername = elem[2]
                    else:
                        self.picklayername = elem[2].currentText()

                    self.pickspinbox = elem[3]

            layername = self.picklayername
            if layername is not None :
                exec("layerdbase = self.dbase.dbase_" + layername )
                if len(layerdbase['type']) > 0:
                    for type in layerdbase['type']:
                        try:
                            layerrealname =  'layer_' + layername + '_' + type
                            exec("layer = self.dbase." + layerrealname)
                            id = self.pickspinbox.value()
                            layer.setSelectedFeatures([layer.getFeatures(qgis.core.QgsFeatureRequest(id)).next().id()])
                        except:
                            pass
            self.picklayername = None
            self.pickspinbox = None

        def getNearestId(self,canvaspoint, layername):
            exec("layerdbase = self.dbase.dbase_" + layername )
            nearestid=[]
            if len(layerdbase['type']) > 0:
                for type in layerdbase['type']:
                    try:
                        layerrealname =  'layer_' + layername + '_' + type
                        exec("layer = self.dbase." + layerrealname)
                        #width = self.canvas.mapUnitsPerPixel() * 2
                        point2 = self.pointEmitter.toLayerCoordinates(layer, canvaspoint)
                        point2geom = qgis.core.QgsGeometry.fromPoint(point2)
                        spIndex = qgis.core.QgsSpatialIndex(layer.getFeatures())
                        layernearestid = spIndex.nearestNeighbor(point2,1)
                        for nid in layernearestid:
                            nearestid.append( [layer,point2geom,nid ])
                    except:
                        pass

            if len(nearestid)>1:
                distance = None
                nearestindex = None
                for i, elem in enumerate(nearestid):
                    feat = elem[0].getFeatures(qgis.core.QgsFeatureRequest(elem[2])).next()
                    dist = feat.geometry().distance( elem[1])
                    if distance is None:
                        distance = dist
                        nearestindex = i
                    elif dist < distance:
                        distance = dist
                        nearestindex = i
            else:
                nearestindex = 0
            return nearestid[nearestindex][0], nearestid[nearestindex][2]


        def copyFeature(self):
            if True:
                self.tempgeometry = self.currentFeature.geometry()
                self.currentFeature = None
                self.saveFeature()


            else:
                if True:
                    self.layers[self.actuallayerindex].featureAdded.connect(self.featureAdded)
                    with qgis.core.edit(self.layers[self.actuallayerindex]):
                        feature = qgis.core.QgsFeature(self.currentFeature)
                        print('feat',feature.id() )
                        feature['ID'] = None
                        print('feat', feature.id())
                        print(self.featureaddedid)
                        success = self.layers[self.actuallayerindex].addFeature(feature)
                        print(success)
                        print(self.featureaddedid)
                        self.layers[self.actuallayerindex].updateFeature(feature)
                        print(self.featureaddedid)

                        feat = self.layers[self.actuallayerindex].getFeatures(qgis.core.QgsFeatureRequest(feature.id())).next()
                        #feat = self.layers[self.actuallayerindex].getFeature(feature.id())
                        print('fet',feat.id())
                    self.layers[self.actuallayerindex].featureAdded.disconnect(self.featureAdded)
                    print(self.featureaddedid)
                    self.layers[self.actuallayerindex].reload()
                    print(self.layers[self.actuallayerindex].allFeatureIds())
                    print('feat', feature.id())
                    print('fet', feat.id())
                    feat = self.layers[self.actuallayerindex].getFeatures(qgis.core.QgsFeatureRequest(feat.id())).next()
                    print('fet', feat.id())

                    self.loadFeaturesinTreeWdg()
                    self.linkedtreewidget.itemClicked.emit(self.treefeatlist[-1][1], 1)
                else:
                    self.layers[self.actuallayerindex].startEditing()
                    feature = qgis.core.QgsFeature(self.currentFeature)
                    print(feature.id())
                    feature['ID'] = None
                    self.layers[self.actuallayerindex].addFeature(feature)
                    self.layers[self.actuallayerindex].updateFeature(feature)
                    print(feature.id())
                    print(feature['ID'])
                    self.loadFeaturesinTreeWdg()
                    self.layers[self.actuallayerindex].commitChanges()
                    print(feature.id())
                    print(feature['ID'])

        def featureAdded(self,id):
            self.featureaddedid = id