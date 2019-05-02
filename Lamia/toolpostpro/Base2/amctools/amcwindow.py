from qgis.PyQt import uic, QtCore, QtGui
import os, sys
import qgis.core
import logging

try:
    from qgis.PyQt.QtGui import (QWidget,QDialog,QMainWindow,QApplication,QTreeWidgetItem,
                                 QMenu,QToolButton,QSpinBox,QDoubleSpinBox,QHeaderView,QLineEdit,
                                 QTextBrowser,QTreeWidgetItemIterator)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow,QApplication,QTreeWidgetItem,
                                     QMenu,QToolButton,QSpinBox,QDoubleSpinBox,QHeaderView,QLineEdit,
                                     QTextBrowser,QTreeWidgetItemIterator)



#class AMCWindow(QMainWindow):QDialog
class AMCWindow(QDialog):

    def __init__(self, parent=None, dbase=None):
        super(AMCWindow, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'amcwindow1.ui')
        uic.loadUi(uipath, self)
        self.dbase = dbase


        # treewidget
        self.treeWidget.setColumnCount(4)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.openMenu)

        self.maintreewdgitem = QTreeWidgetItem(self.treeWidget.invisibleRootItem(),['note'])

        headerlist = ['criteres', 'sql SELECT','bareme', 'ponderation']
        self.treeWidget.setHeaderItem(QTreeWidgetItem(headerlist))

        self.treeWidget.header().setStretchLastSection(False)
        self.treeWidget.header().resizeSection(1,200)
        self.treeWidget.header().resizeSection(2, 100)
        self.treeWidget.header().resizeSection(3, 100)
        self.treeWidget.header().setResizeMode(0, QHeaderView.Stretch)

        self.treeWidget.itemDoubleClicked.connect(self.itemdoubleclicked)
        self.treeWidget.itemChanged.connect(self.treeitemChanged)

        #qmenu
        self.menu = QMenu()
        self.menu.addAction(self.tr("Add critere"))
        # menu.addAction(self.tr("Rename critere"))
        self.menu.addAction(self.tr("Remove critere"))
        self.menu.triggered.connect(self.menuaction)

        self.toolButton_testsql.clicked.connect(self.testSQL)

        self.menuitem = None
        self.itemnameediting = None

        if self.dbase.qgsiface is None:
            self.menuitem = self.maintreewdgitem
            actions = self.menu.actions()
            wdgitem = self.menuaction(actions[0])

            self.lineEdit_sqlfinal.setText("FROM #lamia.noeud INNER JOIN #lamia.descriptionsystem ON descriptionsystem.pk_descriptionsystem = noeud.lpk_descriptionsystem")

            brows = self.treeWidget.itemWidget(wdgitem,1)
            brows.setText("pk_noeud")

            if True:
                actions = self.menu.actions()
                wdgitem = self.menuaction(actions[0])
                brows = self.treeWidget.itemWidget(wdgitem,1)
                brows.setText("pk_descriptionsystem")



    def treeitemChanged(self,itemchanged, column):
        self.treeWidget.closePersistentEditor(self.itemnameediting, 0)
        self.itemnameediting = None

    def itemdoubleclicked(self,itemclicked):
        print(itemclicked.text(0))
        if itemclicked == self.maintreewdgitem:
            return
        self.itemnameediting = itemclicked
        self.treeWidget.openPersistentEditor(itemclicked, 0)

    def openMenu(self,position):
        self.menuitem = self.treeWidget.currentItem()
        self.menu.exec_(self.treeWidget.viewport().mapToGlobal(position))



    def menuaction(self,actionname):
        print('ok',actionname)
        if actionname.text() == self.tr("Add critere"):
            lineedit = QLineEdit()
            #self.treeWidget.setItemWidget(qtreewidgetitm, 1, qbutton)
            qtreewidgetitm = QTreeWidgetItem(self.menuitem,['nouveau critere'])
            #qtreewidgetitm.setFlags(QtCore.Qt.ItemIsEditable)

            #lineedit = QLineEdit()
            #self.treeWidget.setItemWidget(qtreewidgetitm, 0, lineedit)

            qtextbrower = QTextBrowser()
            qtextbrower.setMaximumHeight(50)
            qtextbrower.setReadOnly(False)
            self.treeWidget.setItemWidget(qtreewidgetitm, 1, qtextbrower)

            qbutton = QToolButton()
            self.treeWidget.setItemWidget(qtreewidgetitm,2,qbutton)
            qbutton.setProperty('widgetitem', qtreewidgetitm)
            qbutton.clicked.connect(self.baremebuttonpressed)

            spinbox = QDoubleSpinBox()
            self.treeWidget.setItemWidget(qtreewidgetitm, 3, spinbox)
            self.menuitem.setExpanded(True)

            return qtreewidgetitm

            #self.treeWidget.resizeColumnToContents(0)

        elif actionname.text() == self.tr("Remove critere"):
            self.menuitem.parent().removeChild(self.menuitem)



    def baremebuttonpressed(self,clickbool):

        wdgitem = self.sender().property('widgetitem')
        print(wdgitem.text(0))



    def testSQL(self):
        print('testSQL')

        sql={}
        sql['final']=''
        sql['critere']=[]

        sql['final'] = self.lineEdit_sqlfinal.text()

        iterator = QTreeWidgetItemIterator(self.treeWidget, QTreeWidgetItemIterator.All)
        while iterator.value():
                item = iterator.value()
                itemwdg = self.treeWidget.itemWidget(item,1)
                if isinstance(itemwdg, QTextBrowser):
                    sql['critere'].append( itemwdg.toPlainText() )
                iterator+=1

        #print(sql)
        self.createVLayer(sql)

    def createVLayer(self,sqlsict):
        debug = True

        self.textBrowser_res.clear()

        if debug: logging.getLogger("Lamia").debug('sqlsict %s', str(sqlsict))

        layers={}
        sqlfinal='SELECT '

        for sql in sqlsict['critere']:
            layersql, sentencesql = self.analyseRawSQL(sql)
            for vlayername, vlayersql in layersql:
                if not vlayername in layers.keys():
                    layers[vlayername] = vlayersql
            sqlfinal += sentencesql + ', '
        sqlfinal = sqlfinal[:-2]

        layersql, sentencesql = self.analyseRawSQL(sqlsict['final'])
        for vlayername, vlayersql in layersql:
            if not vlayername in layers.keys():
                layers[vlayername] = vlayersql

        sqlfinal += sentencesql
        sqlfinal = self.dbase.updateQueryTableNow(sqlfinal)
        #sqlfinal += sqlsict['final']

        if debug: logging.getLogger("Lamia").debug('********************* ')
        if debug: logging.getLogger("Lamia").debug('layers %s', str(layers))
        if debug: logging.getLogger("Lamia").debug('sqlfinal %s', str(sqlfinal))

        #scriptvl = '?' + str(QtCore.QUrl.toPercentEncoding('&'.join([layers[key] for key in layers.keys()])))
        scriptvl = '?' + '&'.join([layers[key] for key in layers.keys()])
        if sys.version_info.major == 2:
            scriptvl += "&query=" + str(QtCore.QUrl.toPercentEncoding(sqlfinal))
        elif sys.version_info.major == 3:
            scriptvl += '&query=' + QtCore.QUrl.toPercentEncoding(sqlfinal).data().decode('utf-8')
        #scriptvl += "&query=" + QtCore.QUrl.toPercentEncoding(sqlfinal)

        if debug: logging.getLogger("Lamia").debug('scriptvl %s', str(scriptvl))

        vlayer = qgis.core.QgsVectorLayer(scriptvl, "vlayer", "virtual")
        self.textBrowser_res.append(str(vlayer.isValid()))
        #print('vlayer', vlayer.isValid())

        for fet in vlayer.getFeatures():
            #print(fet.attributes())
            self.textBrowser_res.append(str(fet.attributes()))



    def analyseRawSQL(self,sql):
        layersql, sentencesql = [], ''


        if '#' in sql:
            sqlssplitspace = sql.split(' ')
            for sqlsplitspace in sqlssplitspace:
                if '#' in sqlsplitspace:

                    tabletype, tablename = sqlsplitspace.split('.')
                    if tabletype == '#lamia':
                        if '_now' in tablename:
                            rawtablename = '_'.join(tablename.split('_')[:-1])
                            tablenamevlayer = '_'.join(tablename.split('_')[:-1]) + '_qgis'
                        elif '_qgis' in tablename:
                            rawtablename = '_'.join(tablename.split('_')[:-1])
                            tablenamevlayer = '_'.join(tablename.split('_')[:-1]) + '_qgis'
                        else:
                            rawtablename = tablename
                            tablenamevlayer = tablename


                        vlayerlayer = "layer=spatialite:"
                        print(self.dbase.spatialitefile)
                        print(os.path.normpath(self.dbase.spatialitefile))

                        print('rawtablename',rawtablename,tablenamevlayer)


                        if sys.version_info.major == 2:
                            if self.dbase.isTableSpatial(rawtablename):
                                vlayerlayer += str(QtCore.QUrl.toPercentEncoding("dbname='" + self.dbase.spatialitefile
                                                                                 + "' key ='pk_" + rawtablename.lower() +"' "
                                                                                 + 'table="' + tablenamevlayer.lower() + '"'
                                                                                 + ' (geom) sql='))
                            else:
                                vlayerlayer += str(QtCore.QUrl.toPercentEncoding("dbname='" + self.dbase.spatialitefile
                                                                                 + "' key ='pk_" + rawtablename.lower() +"' "
                                                                                 + 'table="' + tablenamevlayer.lower() + '"'
                                                                                 + ' () sql='))
                        elif sys.version_info.major == 3:
                            if self.dbase.isTableSpatial(rawtablename):
                                vlayerlayer += QtCore.QUrl.toPercentEncoding("dbname='" + self.dbase.spatialitefile
                                                                                 + "' key ='pk_" + rawtablename.lower() +"' "
                                                                                 + 'table="' + tablenamevlayer.lower() + '"'
                                                                                 + ' (geom) sql=').data().decode('utf-8')
                            else:
                                vlayerlayer += QtCore.QUrl.toPercentEncoding("dbname='" + self.dbase.spatialitefile
                                                                                 + "' key ='pk_" + rawtablename.lower() +"' "
                                                                                 + 'table="' + tablenamevlayer.lower() + '"'
                                                                                 + ' () sql=').data().decode('utf-8')



                        if False:
                            vlayerlayer += ("dbname='" + self.dbase.spatialitefile + "' "
                                             + "key='pk_" + rawtablename.lower() +"' "
                                             + 'table="' + tablenamevlayer.lower() + '"'
                                             + ' (geom) sql=')
                        vlayerlayer += ":" + str(tablenamevlayer.lower()) + ":UTF8"

                        layersql.append([tablenamevlayer, vlayerlayer])
                        sentencesql += ' ' + tablename


                else:
                    sentencesql += ' ' + sqlsplitspace
                    continue
        else:
            sentencesql = sql

        return layersql, sentencesql


