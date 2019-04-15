# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView, QComboBox, QAbstractItemView,
                                 QTableWidgetItem, QApplication, QTableWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView, QComboBox, QAbstractItemView,
                                     QTableWidgetItem,QApplication,QTableWidget)

#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
#from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os
import io
import sys
if False:
    if sys.version_info.major == 2:
        from ...libs import pyqtgraph as pg
        from ...libs.pyqtgraph import exporters
    elif sys.version_info.major == 3:
        from ...libs import pyqtgraph as pg
        pg.setConfigOption('background', 'w')

if sys.version_info.major == 2:
    from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
elif sys.version_info.major == 3:
    from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx
import numpy as np
import shutil
import logging


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class CostTool(AbstractLamiaTool):

    DBASES = ['digue','base_digue']
    TOOLNAME = 'COUT'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(CostTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
        self.postInit()
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Synthese'
        self.NAME = 'Couts'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)

        self.iconpath = os.path.join(os.path.dirname(__file__), 'Lamia_cost_tool_icon.png')
        self.qtreewidgetfields = ['libelle']

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)
        self.multipleselection = True
        self.combotypeitems = ['Zone geographique','Troncon']


        if False:
            if self.dbase.dbasetype == 'spatialite':
                fielpathname = 'path_' + os.path.basename(self.dbase.spatialitefile).split('.')[0]
            elif self.dbase.dbasetype == 'postgis':
                fielpathname = 'path_' + str(self.dbase.pghost)+ '_' + str(self.dbase.pgdb) + '_' + str(self.dbase.pgschema)
            self.dbasetablename = os.path.join(os.path.dirname(__file__), '..', 'config', fielpathname + '.txt')
            #networkx var
            self.nxgraph = None
            self.ids = None
            self.indexnoeuds = None
            self.infralinfaces = None
            self.reverseinfralinfaces = None
            self.indexnoeuds = None
            # rubberband var
            self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,self.dbase.dbasetables['Infralineaire']['layer'].geometryType())
            self.rubberBand.setWidth(5)
            self.rubberBand.setColor(QtGui.QColor("magenta"))

            self.rubberbandtrack = qgis.gui.QgsVertexMarker(self.canvas)
            self.rubberbandtrack.setColor(QtGui.QColor(QtCore.Qt.red))
            self.rubberbandtrack.setIconSize(5)
            self.rubberbandtrack.setIconType(qgis.gui.QgsVertexMarker.ICON_BOX) # or ICON_CROSS, ICON_X
            self.rubberbandtrack.setPenWidth(3)
            # matplotlib var
            self.figuretype = plt.figure()
            self.axtype = self.figuretype.add_subplot(111)

            self.postOnActivation()



            # ****************************************************************************************
            # properties ui
            self.groupBox_geom.setParent(None)
            # self.groupBox_elements.setParent(None)

    def postInit(self):
        self.pathbpu = os.path.join(os.path.dirname(__file__), 'costtool', 'bordereau.csv')


    def initFieldUI(self):

        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()

            if True:
                self.combowdg = QComboBox()
                self.windowdialog.frame_4.layout().insertWidget(0, self.combowdg)
                self.combowdg.setVisible(False)



                self.userwdgfield.tableWidget.installEventFilter(self)

                self.userwdgfield.toolButton_calcul.clicked.connect(self.readBordereau)

                self.userwdgfield.toolButton_copier.clicked.connect(self.copier)
                self.userwdgfield.toolButton_selected.clicked.connect(self.goToSelectedId)

            if False:
                self.linkuserwdgfield = [self.userwdgfield.lineEdit_nom,
                                    self.userwdgfield.lineEdit_start,
                                    self.userwdgfield.lineEdit_end]

                self.linkuserwdgfield = {self.dbasetablename: [self.userwdgfield.lineEdit_nom,
                                                            self.userwdgfield.lineEdit_start,
                                                            self.userwdgfield.lineEdit_end]}

                self.userwdgfield.pushButton_pickstart.clicked.connect(self.getPickResult)
                self.userwdgfield.pushButton_pickend.clicked.connect(self.getPickResult)

                # plot
                if False:
                    self.plotWdg = pg.PlotWidget()
                    datavline = pg.InfiniteLine(0, angle=90, pen=pg.mkPen('r', width=1), name='cross_vertical')
                    datahline = pg.InfiniteLine(0, angle=0, pen=pg.mkPen('r', width=1), name='cross_horizontal')
                    self.plotWdg.addItem(datavline)
                    self.plotWdg.addItem(datahline)
                    self.userwdgfield.frame_chart.layout().addWidget(self.plotWdg)
                    self.userwdgfield.checkBox_track.stateChanged.connect(self.activateMouseTracking)
                    self.doTracking = True
                    self.showcursor = True

                    self.userwdgfield.comboBox_chart_theme.addItems(['Profil'])
                    self.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(self.computeGraph)
                if True:
                    self.figuretype = plt.figure()
                    self.axtype = self.figuretype.add_subplot(111)
                    self.mplfigure = FigureCanvas(self.figuretype)
                    self.userwdgfield.frame_chart.layout().addWidget(self.mplfigure)
                    self.toolbar = NavigationToolbar(self.mplfigure, self.userwdgfield.frame_chart)
                    self.userwdgfield.frame_chart.layout().addWidget(self.toolbar)

                    self.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(self.computeGraph)



    def postOnActivation(self):

        if True:
            self.disconnectIdsGui()
            self._clearLinkedTreeWidget()
            #self.userwdgfield.treeWidget_desordres.clear()

            # self.combowdg = QComboBox()
            self.combowdg.clear()
            self.combowdg.addItems(self.combotypeitems)
            #self.windowdialog.frame_4.layout().insertWidget(0,self.combowdg )
            self.combowdg.setVisible(True)
            self.combowdg.currentIndexChanged.connect(self.comboWidgetTypeChanged)
            self.combowdg.currentIndexChanged.emit(0)

            #
            # self.linkedtreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

            self.linkedtreewidget.itemSelectionChanged.connect(self.itemChanged)



            self.connectIdsGui()




    def readBordereau(self):
        debug = False
        if debug : logging.getLogger('Lamia').debug('Start')

        file = open(self.pathbpu, "r")
        lines = file.readlines()
        file.close()
        self.bordereau = {}
        self.bordereau['condition'] = None
        self.bordereau['price'] = None
        self.bordereau['prix'] =  []
        self.bordereau['fields'] = []
        linecourread = False
        for i, line in enumerate(lines):
            # print(linecourread, line)
            if i == 0:
                self.bordereau['sql'] = line.split(';')[0].strip()
                continue

            if not linecourread and line.split(';')[0] == '':
                continue
            elif not linecourread and line.split(';')[0] != '':
                linecourread = True
                linesplitted = line.split(';')
                for elem in linesplitted:
                    if elem.split(',')[0].strip() == 'Prix':
                        if len(elem.split(','))>1:
                            self.bordereau['prix'].append(elem.split(',')[1].strip())
                        else:
                            self.bordereau['prix'].append(None)
                    else:
                        self.bordereau['fields'].append(elem.strip())



                continue

            if linecourread:
                #self.bordereau['case'].append(line.split(';'))
                linesplitted = line.strip().split(';')
                lineprice = [float(val) if val != '' else None for val in linesplitted[0:len(self.bordereau['prix'])]]
                linecondition = linesplitted[len(self.bordereau['prix']):]

                #print(lineprice,linecondition )

                if self.bordereau['condition'] is None:
                    self.bordereau['condition'] = np.array([linecondition])
                    self.bordereau['price'] = np.array([lineprice])
                else:
                    self.bordereau['condition'] = np.append(self.bordereau['condition'],[linecondition], axis=0 )
                    self.bordereau['price'] = np.append(self.bordereau['price'], [lineprice], axis=0)

        if debug: logging.getLogger('Lamia').debug('self.bordereau')
        if debug: logging.getLogger('Lamia').debug('%s', str(self.bordereau))

        self.buildSQL()


    def buildSQL(self):
        debug = False
        if debug : logging.getLogger('Lamia').debug('Start')

        #zone geo selected
        #print([fet.attributes() for fet in self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()])
        idszonegeoselected = [str(feat['id_zonegeo']) for feat in self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()]
        if len(idszonegeoselected) == 0 :
            idszonegeoselected = None



        lenlinecondition = len(list(self.bordereau['condition']))
        #print('lenlinecondition',lenlinecondition)

        fields = ', '.join(self.bordereau['fields'])
        #print(fields)
        sqlfinal = self.bordereau['sql'].replace('*',fields )

        if idszonegeoselected is not None:
            sqlsplitted = self.dbase.splitSQLSelectFromWhereOrderby(sqlfinal)
            wheresql = 'id_zonegeo IN (' + ','.join(idszonegeoselected) + ')'
            if 'WHERE' in sqlsplitted.keys():
                sqlsplitted['WHERE'] += ' AND ' + wheresql
            else:
                sqlsplitted['WHERE'] = wheresql

            sqlfinal = self.dbase.rebuildSplittedQuery(sqlsplitted)

        if debug: logging.getLogger('Lamia').debug('sql : %s',sqlfinal )

        sqlfinal = self.dbase.updateQueryTableNow(sqlfinal)

        if debug: logging.getLogger('Lamia').debug('sql : %s', sqlfinal)

        restot = self.dbase.query(sqlfinal)


        self.priceCalculus(restot)


    def priceCalculus(self, restot):
        ressql=[]
        resultfinal=[]
        debug = False
        if debug : logging.getLogger('Lamia').debug('Start')

        for i, res in enumerate(restot):
            if False and debug and i>9:
                break

            restrunc = res[:-1]
            ressql.append(restrunc)
            force = None
            indexconditionline = None

            for j, linecondition in enumerate(self.bordereau['condition']):

                indexwherenull = np.where(linecondition=='')
                #print(indexwherenull)

                linesimplified = np.delete(linecondition, indexwherenull)
                ressimplified = np.delete(restrunc, indexwherenull)

                # if debug: logging.getLogger('Lamia').debug('lineres %s, linecond %s',linesimplified, ressimplified )

                #test if array equal
                arrayequal = False
                for k, tabelem in enumerate(linesimplified):
                    if ('<' in tabelem or '>' in tabelem) and ressimplified[k] is not None:
                        tempbool = eval(str(ressimplified[k]) + str(tabelem))
                        #print('eval', str(ressimplified[k]) + str(tabelem),tempbool)
                        if tempbool:
                            arrayequal = True
                        else:
                            arrayequal = False
                            break
                    else:
                        if ressimplified[k] == tabelem :
                            arrayequal = True
                        else:
                            arrayequal = False
                            break

                if arrayequal:
                    if force is None:
                        force = len(linesimplified)
                        indexconditionline = j
                    else:
                        if len(linesimplified) > force:
                            force = len(linesimplified)
                            indexconditionline = j



                if False:
                    if np.array_equal(linesimplified, ressimplified):
                        if force is None:
                            force = len(linesimplified)
                            indexconditionline = j
                        else:
                            if len(linesimplified)>force:
                                force = len(linesimplified)
                                indexconditionline = j

            #print('force',force,  indexconditionline)


            #price
            field = restrunc    #used in eval
            prices = self.bordereau['price'][indexconditionline]
            resultprices = []
            if indexconditionline is not None:
                if debug: logging.getLogger('Lamia').debug('line %s, cond %s', restrunc,self.bordereau['condition'][indexconditionline])

                for j, val in enumerate(self.bordereau['prix']):
                    if val is None:
                        resultprices.append(prices[j])
                    else:
                        stringtoeval = str(prices[j]) + val
                        # print('stringtoeval', stringtoeval)
                        try:
                            valeval = eval(stringtoeval)
                            #print('eval', valeval)
                            if valeval>0:
                                resultprices.append(valeval)
                            else:
                                resultprices.append(None)
                        except Exception as e:
                            #print('ex', e)
                            resultprices.append(None)
            else:
                if debug: logging.getLogger('Lamia').debug('line %s, cond %s', restrunc,'No condition')
                resultprices = [None]*len(self.bordereau['prix'])

            #finalprice
            finalprice = next(iter(item for item in resultprices[::-1] if item is not None),None)

            if debug: logging.getLogger('Lamia').debug('prices %s, finalprice %s', resultprices, finalprice)

            resultfinal.append(finalprice)

            if debug: logging.getLogger('Lamia').debug('resultfinal %s',str(resultfinal))

        self.writeResultsInTable(ressql, resultfinal)

    def writeResultsInTable(self,sqlresult, pricelist):

            self.userwdgfield.tableWidget.clear()
            columnlenght = len(self.bordereau['fields']) + 1
            self.userwdgfield.tableWidget.setColumnCount(columnlenght)
            header = self.bordereau['fields'] + ['Prix']
            self.userwdgfield.tableWidget.setHorizontalHeaderLabels(header)

            self.userwdgfield.tableWidget.setRowCount(0)

            for i, resfin in enumerate(sqlresult):
                lastrow = self.userwdgfield.tableWidget.rowCount()
                self.userwdgfield.tableWidget.insertRow(lastrow)

                for j, field in enumerate(self.bordereau['fields']):
                    tablename = None
                    fieldname = None
                    valuetoinsert=''
                    try:
                        tablename = field.split('.')[0].split('_')[0]
                        fieldname = field.split('.')[1]
                    except:
                        pass
                    if tablename is not None :
                        #print(tablename, fieldname, resfin[j])
                        if sys.version_info.major == 2:
                            if not isinstance(resfin[j], unicode):
                                valuetoinsert = str(self.dbase.getConstraintTextFromRawValue(tablename, fieldname, resfin[j]))
                            else:
                                valuetoinsert = self.dbase.getConstraintTextFromRawValue(tablename, fieldname, resfin[j])
                        else:
                            valuetoinsert = str( self.dbase.getConstraintTextFromRawValue(tablename, fieldname, resfin[j]))


                    else:
                        valuetoinsert = resfin[j]

                    self.userwdgfield.tableWidget.setItem(lastrow, j, QTableWidgetItem(valuetoinsert))

                #price
                self.userwdgfield.tableWidget.setItem(lastrow, columnlenght -1,  QTableWidgetItem(str(pricelist[i])))

    def eventFilter(self, source, event):


        if (event.type() == QtCore.QEvent.KeyPress and
                event.matches(QtGui.QKeySequence.Copy)):
            self.copier()
            return True
        #return True
        return super(CostTool, self).eventFilter(source, event)

    def copier(self, var=None):
        """copier la zone sélectionnée dans le clipboard
        """
        # emplacement sélectionné pour copier dans le clipboard

        texte = ""

        # copy header
        lenheader = self.userwdgfield.tableWidget.columnCount()
        for i in range(lenheader):
            texte += self.userwdgfield.tableWidget.horizontalHeaderItem(i).text() + "\t"
        texte = texte[:-1] + "\n"



        selected = self.userwdgfield.tableWidget.selectedRanges()

        beginrow=0
        endrow = 0
        begincolumn=0
        encolumn=0

        if len(selected)>0:
            beginrow = selected[0].topRow()
            endrow = selected[0].bottomRow() + 1
            begincolumn = selected[0].leftColumn()
            encolumn = selected[0].rightColumn() + 1
        else:
            beginrow = 0
            endrow = self.userwdgfield.tableWidget.rowCount()
            begincolumn = 0
            encolumn = self.userwdgfield.tableWidget.columnCount()




        # construction du texte à copier, ligne par ligne et colonne par colonne






        #for i in range(selected[0].topRow(), selected[0].bottomRow() + 1):
        for i in range(beginrow, endrow ):
            #for j in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
            for j in range(begincolumn, encolumn ):
                try:
                    texte += self.userwdgfield.tableWidget.item(i, j).text() + "\t"
                except AttributeError:
                    # quand une case n'a jamais été initialisée
                    texte += "\t"
            texte = texte[:-1] + "\n"  # le [:-1] élimine le '\t' en trop

        # enregistrement dans le clipboard
        QApplication.clipboard().setText(texte)


    def goToSelectedId(self):
        pass

    def postOnDesactivation(self):

        #self.combowdg.setParent(None)
        self.combowdg.setVisible(False)

        # self.linkedtreewidget.setSelectionMode(QAbstractItemView.SingleSelection)
        if False:
            try:
                self.userwdg.treeWidget_desordres.currentItemChanged.disconnect(self.showDesordres)
            except:
                pass

        try:
            self.linkedtreewidget.itemSelectionChanged.disconnect(self.itemChanged)
        except:
            pass



    def comboWidgetTypeChanged(self, comboindex ):
        if False:
            self.loadFeaturesinTreeWdg()
            self.disconnectIdsGui()



        if True:
            #print('comboWidgetTypeChanged', comboindex)
            type = self.combotypeitems[comboindex]
            # ['Zone geographique','Troncon']
            if type == 'Zone geographique':
                self.dbasetablename = 'Zonegeo'
                self.dbasetable = self.dbase.dbasetables['Zonegeo']
                if qgis.utils.iface is not None :
                    qgis.utils.iface.setActiveLayer(self.dbase.dbasetables['Zonegeo']['layerqgis'])


            elif type == 'Troncon':
                self.dbasetablename = 'Infralineaire'
                self.dbasetable = self.dbase.dbasetables['Infralineaire']
                if qgis.utils.iface is not None :
                    qgis.utils.iface.setActiveLayer(self.dbase.dbasetables['Infralineaire']['layerqgis'])



            self.loadFeaturesinTreeWdg()

            if False:

                self.disconnectIdsGui()
                self._clearLinkedTreeWidget()


                headerlist = list(self.qtreewidgetfields)
                headerlist.insert(0, 'ID')
                self.linkedtreewidget.setColumnCount(len(headerlist))
                self.linkedtreewidget.header().setVisible(True)
                self.linkedtreewidget.setHeaderItem(QTreeWidgetItem(headerlist))
                header = self.linkedtreewidget.header()
                lenheaderlist = len(headerlist)
                if sys.version_info.major == 2:
                    for i in range(lenheaderlist):
                        header.setResizeMode(i, QHeaderView.ResizeToContents)
                    header.setResizeMode(lenheaderlist-1, QHeaderView.Stretch)
                elif  sys.version_info.major == 3:
                    for i in range(lenheaderlist):
                        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(lenheaderlist-1, QHeaderView.Stretch)


                parentitem = self.linkedtreewidget.invisibleRootItem()

                if self.combowdg.currentText() == 'Troncon':
                    sql = "SELECT id_infralineaire "
                    if len(self.qtreewidgetfields) > 0:
                        sql += "," + ','.join(self.qtreewidgetfields)
                    sql += " FROM Infralineaire_now"

                elif self.combowdg.currentText() == 'Zone geographique':
                    sql = "SELECT id_zonegeo "
                    if len(self.qtreewidgetfields) > 0:
                        sql += "," + ','.join(self.qtreewidgetfields)
                    sql += " FROM zonegeo_qgis WHERE lpk_revision_end IS NULL"

                sql = self.dbase.updateQueryTableNow(sql)
                query = self.dbase.query(sql)
                ids = [list(row) for row in query]

                lenqtreewidg = len(self.qtreewidgetfields) + 1
                self.treefeatlist = [[id[0], QTreeWidgetItem([str(id[i]) for i in range(lenqtreewidg)])] for id in ids]
                parentitem.addChildren([elem[1] for elem in self.treefeatlist])



                # self.propertieswdgDESORDRE.reloadgraphtype()


                self.connectIdsGui()


    def postInitFeatureProperties(self, feat):
        pass


    def itemChanged(self,item1=None, item2=None):
        pass

        #print('itemChanged',item1, item2 )






class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_cost_tool.ui')
        uic.loadUi(uipath, self)

