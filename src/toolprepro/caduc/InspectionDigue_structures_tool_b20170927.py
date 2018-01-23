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
import operator

from ..maptool.mapTools import mapToolAddFeature, mapToolAddLine, mapToolCapture


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'structuresTool.ui'))



class structuresTool(AbstractInspectionDigueTool,FORM_CLASS):

    def __init__(self, dbase,dialog, linkedtreewidget, parent=None):

        super(structuresTool,self).__init__(dbase,dialog,linkedtreewidget,parent = parent)
        
        
        # signals
        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Description'
        self.NAME = 'Structures'
        self.sourcelayername = 'structures'
        self.dbtablename = 'TRONCON'
        
        #self.itemtempobs = None

        #self.iconpath = os.path.join(os.path.dirname(__file__),'..','icons','tools','Video_48x48.png' )

        """
        #paint
        self.paintwidg = Example(self.dbase,self)
        layout = self.frame_coupe.layout()
        layout.addWidget(self.paintwidg)
        
        #structureelemnt
        from .InspectionDigue_structures_elements_tool import structuresElementsTool
        self.structureselementstool =  structuresElementsTool(self.dbase, self.windowdialog, self.treeWidget_elem , parent = self)
        layout = self.frame_elem.layout()
        layout.addWidget(self.structureselementstool)
        self.treeWidget_elem.itemClicked.connect(self.structureselementstool.featureSelected)
        self.pushButton_add_elem.clicked.connect(self.structureselementstool.addFeature)
        self.pushButton_del_elem.clicked.connect(self.structureselementstool.deleteFeature)

        self.treeWidget_elem.currentItemChanged.connect(self.paintwidg.repaint)
        self.pushButton_addlevee.clicked.connect(self.addLevee)

        
        #photo
        from .InspectionDigue_photographies_tool import photographiesTool
        self.phototool =  photographiesTool(self.dbase, self.windowdialog, self.treeWidget_ph , parent = self)
        layout = self.frame_ph.layout()
        layout.addWidget(self.phototool)
        self.treeWidget_ph.itemClicked.connect(self.phototool.featureSelected)
        self.pushButton_add_ph.clicked.connect(self.phototool.addFeature)
        self.pushButton_del_ph.clicked.connect(self.phototool.deleteFeature)
        """

        
        #pickopt
        self.pickoptions = [[self.pushButton_Pick_view,self.pushButton_show_link,'troncons', self.spinBox_ID]]

        """
        # tools
        self.tools.append(self.structureselementstool)
        self.tools.append(self.phototool)
        """

    def addLevee(self):
        if self.structureselementstool.currentparentfeature is not None and self.structureselementstool.currentparentfeature[1] is not None:

            elemstoadd = [{'cote' : 'TERRE',
                           'position' : 'Talus digue'},
                          {'cote': 'CRETE',
                           'position': 'Crete'},
                          {'cote': 'EAU',
                           'position': 'Talus digue'}
                          ]
            for elemtoadd in elemstoadd:
                self.structureselementstool.featureSelected()
                # coteindex = self.structureselementstool.dbaseused['combobox'][self.structureselementstool.dbaseused['champs'].index('COTE')]
                index = self.structureselementstool.comboBox_elem_cote.findText(elemtoadd['cote'], QtCore.Qt.MatchFixedString)
                self.structureselementstool.comboBox_elem_cote.setCurrentIndex(index)
                #positionindex = self.structureselementstool.dbaseused['combobox'][self.structureselementstool.dbaseused['champs'].index('POSITION')]
                index = self.structureselementstool.comboBox_elem_position.findText(elemtoadd['position'], QtCore.Qt.MatchFixedString)
                self.structureselementstool.comboBox_elem_position.setCurrentIndex(index)
                index = self.structureselementstool.comboBox_nature.findText('Partie revetue', QtCore.Qt.MatchFixedString)
                self.structureselementstool.comboBox_nature.setCurrentIndex(index)
                index = self.structureselementstool.comboBox_materiaux.findText('revetement vegetalise', QtCore.Qt.MatchFixedString)
                self.structureselementstool.comboBox_materiaux.setCurrentIndex(index)
                self.structureselementstool.saveFeature()

        
    def onActivation(self):



        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        data1 = ['row1','row2','row3','row4']
        data2 = ['1','2.0','3.00000001','3.9999999']
        combo_box_options = ["Option 1","Option 2","Option 3"]
        
        item1 = QtGui.QTableWidgetItem(data1[0])
        self.tableWidget.setItem(0,0,item1)
        
        combo = QtGui.QComboBox()
        combo.addItems(combo_box_options)
        self.tableWidget.setCellWidget(3,1,combo)
        
        txtb = QtGui.QTextEdit()
        txtb.setText('plplpl')
        txtb.setEnabled(True)
        #combo.addItems(combo_box_options)
        self.tableWidget.setCellWidget(0,1,txtb)
        self.tableWidget.setRowHeight(0,60)
        
        txtd = QtGui.QDateEdit()
        #combo.addItems(combo_box_options)
        self.tableWidget.setCellWidget(1,1,txtd)
        
        txts = QtGui.QSpinBox()
        #combo.addItems(combo_box_options)
        self.tableWidget.setCellWidget(2,1,txts)
        
        txtp = QtGui.QPushButton()
        #combo.addItems(combo_box_options)
        self.tableWidget.setCellWidget(2,2,txtp)
        txtp.clicked.connect(self.testpvr)
        
        txtc = QtGui.QCheckBox()
        #combo.addItems(combo_box_options)
        self.tableWidget.setCellWidget(2,3,txtc)
        
        

    def onDesactivation(self):
        pass

    def testpvr(self):
        print('okok')
            
        
    def showFeatureWidget(self,featureid = None):
        if False:
            if featureid is not None:
                self.structureselementstool.currentparentfeature = [self,self.currentFeature]
                self.structureselementstool.loadFeaturesinTreeWdg()
                #self.paintwidg.elemid = self.structureselementstool.treefeatlist
                self.paintwidg.repaint()
                self.phototool.currentparentfeature = [self,self.currentFeature]
                self.phototool.loadFeaturesinTreeWdg()
            else:
                self.structureselementstool.currentparentfeature = [self,None]
                self.structureselementstool.loadFeaturesinTreeWdg()
                self.paintwidg.repaint()
                self.phototool.currentparentfeature = [self,None]
                self.phototool.loadFeaturesinTreeWdg()
        pass




class Example(QtGui.QWidget):
    def __init__(self,dbase,parentwdg):
        super(Example, self).__init__()
        self.elemid=None
        self.dbase = dbase
        self.parentwdg = parentwdg
        #self.layer = self.dbase.layer_structures_elements


        self.elementcoords = {'CRE' : '0,10,20,10',
                              'FRB' : '70,80,90,80',
                              'BER' : '90,80,100,100',
                              'SOR' : '40,50,50,50',
                              'TAR' : '50,50,70,80',
                              'TAD' : '20, 10, 70, 80',
                              'TADR' : '20, 10, 40, 50',
                              'RVH' : '0,1,8,1',
                              'REV2' : '8,1,8,10'}



    def paintEvent(self, event):
        #print(self.elemid)
        self.layer = self.dbase.layer_structures_elements
        size = self.size()

        self.elemid = self.parentwdg.structureselementstool.treefeatlist
        #request = qgis.core.QgsFeatureRequest().setFilterFids(self.elemid)
        #request = qgis.core.QgsFeatureRequest([elem[0] for elem in self.elemid])
        request = qgis.core.QgsFeatureRequest().setFilterFids([elem[0] for elem in self.elemid])
        elems=[]
        for feat in self.layer.getFeatures(request):
            if False:
                if feat['COTE']=='TER':
                    elemsTER.append(feat['POSITION'])
                elif feat['COTE']=='RIV':
                    elemsRIV.append(feat['POSITION'])
                elif feat['COTE']=='CRE':
                    elemcre.append(1)
            elems.append([feat['COTE'],feat['POSITION'],feat['NATURE'],feat.id()])

        cote = [ele[0] for ele in elems]
        position = [ele[1] for ele in elems]

        qp = QtGui.QPainter()
        qp.begin(self)
        
        elems2 = [[temp[0],temp[1]] for temp in elems]
        elems3 = [[temp[0], temp[1], temp[2]] for temp in elems]


        #talus:
        cotes = ['RIV','TER']
        for cote in cotes:
            if [cote,'SOR'] in elems2 or [cote,'TAR'] in elems2:
                if [cote,'SOR'] in elems2 :
                    eval("self.drawLine(qp, " + self.elementcoords['SOR'] + ", elems[elems2.index([cote,'SOR'])])")
                if [cote,'TAR'] in elems2:
                    eval("self.drawLine(qp, " + self.elementcoords['TAR'] + ", elems[elems2.index([cote,'TAR'])])")
                if [cote,'TAD'] in elems2:
                    #self.drawLine(qp,  40, 50, 50, 50, ele)
                    eval("self.drawLine(qp, " + self.elementcoords['TADR'] + ", elems[elems2.index([cote,'TAD'])])")
            else:
                if [cote,'TAD'] in elems2:
                    #self.drawLine(qp,  40, 50, 50, 50, ele)
                    eval("self.drawLine(qp, " + self.elementcoords['TAD'] + ", elems[elems2.index([cote,'TAD'])])")

        if ['RIV','FRB'] in elems2 :
            eval("self.drawLine(qp, " + self.elementcoords['FRB'] + ", elems[elems2.index(['RIV','FRB'])])")

        if ['RIV','BER'] in elems2 :
            eval("self.drawLine(qp, " + self.elementcoords['BER'] + ", elems[elems2.index(['RIV','BER'])])")

        if ['CRE','CRE'] in elems2:
            eval("self.drawLine(qp, " + self.elementcoords['CRE'] + ", elems[elems2.index(['CRE','CRE'])])")
            if ['CRE','CRE','RVH']  in elems3:
                eval("self.drawLine(qp, " + self.elementcoords['RVH'] + ", elems[elems3.index(['CRE','CRE','RVH'] )])")
                eval("self.drawLine(qp, " + self.elementcoords['REV2'] + ", elems[elems3.index(['CRE','CRE','RVH'] )])")


        qp.end()





    def drawText2(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, 'popo')

    def drawLine(self,qp,x1,y1,x2,y2,elem = None):
        try:
            if int(elem[3]) == int(self.parentwdg.treeWidget_elem.currentItem().text(0)):
                pen = QtGui.QPen( QtGui.QColor(168, 34, 3))
                pen.setWidth(4)
                qp.setPen(QtGui.QPen( QtGui.QColor(168, 34, 3)))
            else:
                pen = QtGui.QPen(QtGui.QColor(9, 34, 3))
                pen.setWidth(1)
        except AttributeError as e:
            pen = QtGui.QPen(QtGui.QColor(9, 34, 3))
        except ValueError as e:
            pen = QtGui.QPen(QtGui.QColor(9, 34, 3))

        qp.setPen(pen)

        h = self.size().height()
        larg = self.size().width()
        if elem[0] == 'TER':
            #qp.drawLine(larg/2 - larg*x1/2/100 , y1*h, larg*(100 - x2)/2 , y2*h)
            qp.drawLine(larg*(1.-x1/100.)/2. , y1 * h/100., larg*(1.-x2/100.)/2., y2 * h/100.)
        elif elem[0] == 'RIV':
            qp.drawLine(larg * (1. + x1 / 100.) / 2., y1 * h/100., larg * (1. + x2 / 100.) / 2., y2 * h/100.)
        elif elem[0] == 'CRE' :
            qp.drawLine(larg * (1. - x1 / 100.) / 2., y1 * h / 100., larg * (1. - x2 / 100.) / 2., y2 * h / 100.)
            qp.drawLine(larg * (1. + x1 / 100.) / 2., y1 * h / 100., larg * (1. + x2 / 100.) / 2., y2 * h / 100.)

        else:
            qp.drawLine(larg * x1/100., y1 * h/100., larg * x2/100., y2 * h/100.)

        
    def mousePressEvent(self, event):

        h = float(self.size().height())
        larg = float(self.size().width())
        x = (event.pos().x()*100./larg - 50.) * 2.
        y = event.pos().y()*100./h

        resultstruct = []
        for struccoor in self.elementcoords.keys():
            x1,y1,x2,y2 = eval(self.elementcoords[struccoor] )
            if abs(x)>x1 and abs(x)<x2:
                resultstruct.append(struccoor)

        if x>0:
            cote = 'RIV'
        else:
            cote = 'TER'
        if 'CRE' in resultstruct:
            cote = 'CRE'

        result = []
        for elem in self.elemid:
            feature = self.layer.getFeatures(qgis.core.QgsFeatureRequest(elem[0])).next()
            #print(resultstruct,feature['POSITION'], feature['NATURE'] ,  feature['COTE'])
            if (feature['POSITION'] in resultstruct or   feature['NATURE'] in resultstruct  )and feature['COTE'] == cote:
                result.append([elem,feature['POSITION'],feature['NATURE']])

        elem = None
        if len(result) == 1:
            elem = result[0][0]
        else:
            positions = [temp[1] for temp in result]
            natures = [temp[2] for temp in result]
            if 'TAD' in positions:
                if 'SOR' in positions:
                    elem = result[positions.index('SOR')][0]
                elif 'TAR' in positions:
                    elem = result[positions.index('TAR')][0]
                else :
                    elem = result[positions.index('TAD')][0]
            elif 'CRE' in positions:
                if 'RVH' in resultstruct and 'RVH' in natures:
                    elem = result[natures.index('RVH')][0]
                else:
                    elem = result[positions.index('CRE')][0]
        if elem is not None:
            self.parentwdg.treeWidget_elem.setCurrentItem(elem[1])
            self.parentwdg.treeWidget_elem.itemClicked.emit(elem[1], 1)