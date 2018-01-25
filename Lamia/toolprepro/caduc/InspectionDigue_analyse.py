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
import collections
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QWidget, QTreeWidgetItem, QLabel
except:
    from qgis.PyQt.QtWidgets import QWidget, QTreeWidgetItem,QLabel

from ..maptool.mapTools import mapToolAddFeature, mapToolAddLine, mapToolCapture

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'analysedesordresTool.ui'))


class AnalyseDesordresTool(AbstractInspectionDigueTool, FORM_CLASS):

    def __init__(self, dbase,dialog , linkedtreewidget, parent=None):

        super(AnalyseDesordresTool,self).__init__(dbase,dialog,linkedtreewidget,parent = parent)

    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Analyse'
        self.NAME = 'Troncons'
        #self.layersdes=[self.dbase.layer_desordres_point,self.dbase.layer_desordres_line]
        self.windowdialog.dbase.dBaseLoaded.connect(self.DBaseLoaded)

        self.figuretype = plt.figure(0)
        self.canvastype = FigureCanvas(self.figuretype)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.canvastype)
        self.frame_type.setLayout(layout)
        self.axtype = self.figuretype.add_subplot(111)

        self.figureposition = plt.figure(1)
        self.canvasposition = FigureCanvas(self.figureposition)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.canvasposition)
        self.frame_position.setLayout(layout)
        self.axposition = self.figureposition.add_subplot(111)

        self.figureurgence= plt.figure(2)
        self.canvasurgence = FigureCanvas(self.figureurgence)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.canvasurgence)
        self.frame_urgence.setLayout(layout)
        self.axurgence = self.figureurgence.add_subplot(111)





    def onDesactivation(self):
        self.reinitWidget()
        try:
            self.linkedtreewidget.itemClicked.disconnect(self.showProperties)
        except:
            pass
        try:
            self.treeWidget_desordres.currentItemChanged .disconnect(self.showDesordres)
        except:
            pass

    def DBaseLoaded(self):
        self.layers = [self.dbase.layer_desordres_point,self.dbase.layer_desordres_line]


    def onActivation(self):
        for i in range(self.linkedtreewidget.invisibleRootItem().childCount()):
            self.linkedtreewidget.invisibleRootItem().removeChild(self.linkedtreewidget.invisibleRootItem().child(0))
        self.reinitWidget()
        featlist = []

        for feat in self.dbase.layer_troncons_line.getFeatures():
                    featlist.append( feat.id())
        featlist.sort()
        self.treefeatlist = [ [id,QTreeWidgetItem([str(id)])] for id in featlist]
        self.linkedtreewidget.addTopLevelItems([elem[1] for elem in self.treefeatlist ])

        if len(featlist)>0:
            self.linkedtreewidget.itemClicked.emit(self.treefeatlist[0][1],1)
        if False:
                self.initFeatureProperties(None, self.dbaseused, self)
                if self.currentparentfeature is not None:
                    self.showFeatureWidget()
                self.setEnabled(False)
                for tool in self.tools:
                    tool.setEnabled(False)

        self.linkedtreewidget.itemClicked.connect(self.showTronconsDesordres)
        #self.linkedtreewidget.itemClicked.connect(self.getSyntheticResults)

        self.treeWidget_desordres.currentItemChanged .connect(self.showDesordres)

    def showTronconsDesordres(self,item):

        for i in range(self.treeWidget_desordres.invisibleRootItem().childCount()):
            self.treeWidget_desordres.invisibleRootItem().removeChild(self.treeWidget_desordres.invisibleRootItem().child(0))


        root = self.treeWidget_desordres.invisibleRootItem()
        troncon_id = int(item.text(0))
        self.desordrelist = []
        for feat in self.dbase.layer_desordres_point.getFeatures():
            if feat['LK_TYPE'] == 'STR':
                featchild = self.dbase.layer_structures_line.getFeatures(qgis.core.QgsFeatureRequest(feat['LK_ID'])).next()
                if featchild['DIG_ID'] == troncon_id:
                    if feat.geometry() is None:
                        geomtype = 'line'
                    else:
                        geomtype = 'point'
                    self.desordrelist.append(['STR', feat.id() , featchild,geomtype])

            elif feat['LK_TYPE'] == 'RES':
                featchild = self.dbase.layer_reseaux_line.getFeatures(qgis.core.QgsFeatureRequest(feat['LK_ID'])).next()
                if featchild['LK_TR'] == troncon_id:
                    if feat.geometry() is None:
                        geomtype = 'line'
                    else:
                        geomtype = 'point'
                    self.desordrelist.append(['RES', feat.id() , featchild,geomtype])

            elif feat['LK_TYPE'] == 'RSP':
                featchild = self.dbase.layer_reseaux_spe_point.getFeatures(qgis.core.QgsFeatureRequest(feat['LK_ID'])).next()
                if featchild['TR_ID'] == troncon_id:
                    geomtype = 'point'
                    self.desordrelist.append(['RSP', feat.id() , featchild,geomtype])



        self.treeWidget_desordres.addTopLevelItems( [QTreeWidgetItem(root,[str(elem[1]), elem[0]]) for elem in self.desordrelist] )
        self.treeWidget_desordres.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.treeWidget_desordres.header().setStretchLastSection(False)

        self.getSyntheticResults()


    def showDesordres(self,item):


        self.reinitWidget()

        if item is None:
            return
        desordreid = int(item.text(0))
        typegeom = self.desordrelist[[elem[1] for elem in self.desordrelist].index(desordreid)][3]
        exec("currentlayer = self.dbase.layer_desordres_"+typegeom )
        desordrefeat = currentlayer.getFeatures(qgis.core.QgsFeatureRequest(desordreid)).next()

        self.showFeature(currentlayer,desordrefeat )


        self.label_cote.setText(     self.getDescription('desordres',desordrefeat,'COTE')  )
        self.label_position.setText(self.getDescription('desordres',desordrefeat,'POSITION') )
        self.label_type.setText(self.getDescription('desordres',desordrefeat,'TYPE_DES'))



        self.label_elem_assoc.setText( self.getDescription('desordres',desordrefeat,'LK_TYPE') )

        request = qgis.core.QgsFeatureRequest(qgis.core.QgsExpression('"DES_ID" = ' + str(desordreid)))
        finalobsfeat = None
        date = None
        for feat in self.dbase.layer_desordres_obs.getFeatures(request):
            if date is None:
                date = feat['DATE']
                finalobsfeat = feat
            else:
                if feat['DATE']>date:
                    date = feat['DATE']
                    finalobsfeat = feat

        if finalobsfeat is not None:
            self.label_date.setText(finalobsfeat['DATE'])
            #self.label_urgence.setText(str(finalobsfeat['URGENCE']))
            self.label_urgence.setText(self.getDescription('desordres_obs', finalobsfeat, 'URGENCE'))
            self.textBrowser_evol.setText(finalobsfeat['EVOLUTION'])
            self.textBrowser_com.setText(finalobsfeat['COMMENTAIR'])
            self.textBrowser_suite.setText(finalobsfeat['SUITE'])

            expr = '"LK_TYPE" = ' + "'" + 'OBS' + "' AND " + '"LK_ID" = '  + str(finalobsfeat.id())
            request = qgis.core.QgsFeatureRequest(qgis.core.QgsExpression(expr))
            for feat in self.dbase.layer_photographies_point.getFeatures(request):
                filetotreat = feat['CHEMIN_FIC']

                if filetotreat[0] == '.':
                    filetoeval = '"' + os.path.dirname(self.dbase.dbasefile) + '","' + '","'.join( filetotreat.split('\\')) + '"'
                    file = eval("os.path.join(" + filetoeval + ")")
                else:
                    file = os.path.normpath(filetotreat)

                label = QLabel()
                self.tabWidget_photos.addTab(label, os.path.basename(file))

                myPixmap = QtGui.QPixmap(os.path.normpath(file))
                pixsize = myPixmap.size()
                myScaledPixmapH = myPixmap.scaledToHeight(label.size().height())
                myScaledPixmapW = myPixmap.scaledToWidth(label.size().width())
                if myScaledPixmapH.size().height() < myScaledPixmapW.size().height():
                    label.setPixmap(myScaledPixmapH)
                else:
                    label.setPixmap(myScaledPixmapW)

    def reinitWidget(self):
        for tab in range(self.tabWidget_photos.count()):
            self.tabWidget_photos.removeTab(0)
        if self.layers is not None:
            for layerdes in self.layers:
                layerdes.removeSelection()

        self.label_cote.setText('/')
        self.label_position.setText('/')
        self.label_type.setText('/')
        self.label_elem_assoc.setText('/')
        self.label_date.setText('/')
        self.label_urgence.setText('/')

        self.textBrowser_evol.setText('/')
        self.textBrowser_com.setText('/')
        self.textBrowser_suite.setText('/')


    def getSyntheticResults(self,item=None):
        type = []
        positions=[]
        urgence = []

        #root = self.treeWidget_desordres.invisibleRootItem()
        #for i in range(root.childCount()):

        for elem in  self.desordrelist:

            #item = root.child(i)
            #desordreid = int(item.text(0))
            desordreid = elem[1]
            desordrefeat = self.layers[0].getFeatures(qgis.core.QgsFeatureRequest(desordreid)).next()
            type.append(desordrefeat['TYPE_DES'])
            positions.append(desordrefeat['COTE'] + '/' + desordrefeat['POSITION'])
            request = qgis.core.QgsFeatureRequest(qgis.core.QgsExpression('"DES_ID" = ' + str(desordreid)))
            finalobsfeat = None
            date = None
            for feat in self.dbase.layer_desordres_obs.getFeatures(request):
                if date is None:
                    date = feat['DATE']
                    finalobsfeat = feat
                else:
                    if feat['DATE']>date:
                        date = feat['DATE']
                        finalobsfeat = feat

            if finalobsfeat is not None:
                urgence.append(finalobsfeat['URGENCE'])



        countertype = collections.Counter(type)
        counterpositions = collections.Counter(positions)
        counterurgence = collections.Counter(urgence)

        self.textBrowser_type.setText(str(countertype))
        self.textBrowser_position.setText(str(counterpositions))
        self.textBrowser_urgence.setText(str(counterurgence))

        self.axtype.clear()
        labels = countertype.keys()
        sizes = countertype.values()
        explode = [0.05]*len(labels)
        if True:
            self.axtype.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        else:
            patches, texts = self.axtype.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
            self.axtype.legend(patches, labels, loc="best")
        self.axtype.axis('equal')
        self.axtype.set_title('Type de desordre')
        self.figuretype.canvas.draw()

        self.axposition.clear()
        labels = counterpositions.keys()
        sizes = counterpositions.values()
        explode = [0.05]*len(labels)
        if True:
            self.axposition.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        else:
            patches, texts = self.axposition.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
            self.axposition.legend(patches, labels, loc="best")
        self.axposition.axis('equal')
        self.axposition.set_title('Position des desordres')
        self.figureposition.canvas.draw()

        self.axurgence.clear()
        labels = counterurgence.keys()
        sizes = counterurgence.values()
        explode = [0.05]*len(labels)
        if True:
            self.axurgence.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        else:
            patches, texts = self.axurgence.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
            self.axurgence.legend(patches, labels, loc="best")
        self.axurgence.axis('equal')
        self.axurgence.set_title('Urgence des desordres')
        self.figureurgence.canvas.draw()



    def getDescription(self,table,feature,field):
        #self.getDescription('desordres', desordrefeat, 'COTE')
        exec("dbase = self.dbase.dbase_" + table)
        index = dbase['champs'].index(field)
        combovalues = dbase['combobox'][index]
        featurevalue = feature[field]
        for values in combovalues:
            if featurevalue == values[0]:
                return values[1]
        return 'Valeur non trouvee'

    def showFeature(self,layer,feature):
        self.canvas.refresh()
        #self.canvas.zoomToFeatureIds(self.layers[self.actuallayerindex], [self.currentFeature.id()] )
        xform = qgis.core.QgsCoordinateTransform(layer.crs(), self.canvas.mapSettings().destinationCrs())
        point2 = xform.transform(feature.geometry().centroid().asPoint())
        self.canvas.setCenter(point2)
        self.canvas.refresh()
        layer.setSelectedFeatures([feature.id()])