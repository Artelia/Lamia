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
     Implementation of QgsPluginLayer class, used to show selafin res
     
    Versions :
    Impl
    0.0 : debut

 ***************************************************************************/
"""

#unicode behaviour
from __future__ import unicode_literals

#from PyQt4 import uic, QtGui
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QDialog, QTableWidgetItem, QMessageBox, QComboBox
except:
    from qgis.PyQt.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QComboBox

import os
import qgis.gui


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'InspectionDigue_linkage.ui'))

class LinkageDialog(QDialog, FORM_CLASS):

    def __init__(self, widget, parent=None):
        """Constructor."""
        super(LinkageDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.finished.connect(self.dialogIsFinished)
        self.widget = widget

        self.comboBox_linktype.addItems(self.widget.linkagespec.keys())
        """
        self.currenttype = self.comboBox_linktype.currentText()
        self.populateTable()
        """
        self.comboBox_linktype.currentIndexChanged.connect(self.typeChanged)
        self.comboBox_linktype.currentIndexChanged.emit(0)




        self.pushButton_add.clicked.connect(self.addrow)
        self.pushButton_remove.clicked.connect(self.removerow)

        self.pushButton_resetfromgeom.clicked.connect(self.resetFromGeometry)

        self.pushButton_save.clicked.connect(self.save)



    def typeChanged(self,comboindex):
        self.currenttype = self.comboBox_linktype.currentText()
        self.currentlinkage = self.widget.linkagespec[self.currenttype]
        if self.currentlinkage['tabletc'] is not None:
            self.frame_actions.setEnabled(True)
            self.dbasetc = self.widget.dbase.dbasetables[self.currentlinkage['tabletc']]
        else:
            self.frame_actions.setEnabled(False)
            self.dbasetc = self.widget.dbase.dbasetables[self.currenttype]

        self.populateTable()

    def populateTable(self):
        self.headerlist = []

        if self.currentlinkage['tabletc'] is not None:

            for fieldname in self.dbasetc['fields']:
                if fieldname == self.currentlinkage['idtcsource'] or fieldname == 'pk_' + self.currenttype.lower() :
                    continue
                else:
                    self.headerlist.append(fieldname)
        else:
            self.headerlist.append(self.currentlinkage['idsource'])


        self.tableWidget.setColumnCount(len(self.headerlist))
        self.tableWidget.setHorizontalHeaderLabels(self.headerlist)
        self.tableWidget.setRowCount(0)

        # print(self.headerlist)

        if self.widget.currentFeature is not None:
            if self.currentlinkage['tabletc'] is not None:
                sql = "SELECT pk_" + self.currenttype.lower()  +"," + ",".join(self.headerlist) + " FROM " + self.currentlinkage['tabletc']
                sql += " WHERE " + self.currentlinkage['idtcsource'] + " = " + str(self.widget.currentFeature[self.currentlinkage['idsource']])
                query = self.widget.dbase.query(sql)
                ids = [row[0:len(self.headerlist)+1] for row in query]
                # print('populate',ids)

                #self.tableWidget.setRowCount(len(ids) )

                #layertc = self.widget.dbase.dbasetables[linkagetemp['tabletc']]['layer']
                if len(ids)>0:
                    for i in range((len(ids) )):
                        #index = self.tableWidget.rowCount()
                        #currentfeature = layer.getFeatures(qgis.core.QgsFeatureRequest(ids[i][0])).next()
                        self.addrow()
                        for j in range(self.tableWidget.columnCount()):
                            fieldname = self.headerlist[j]
                            #print('populate',i,j,fieldname)
                            if 'Cst' in self.dbasetc['fields'][fieldname].keys():
                                if ids[i][j + 1] is None:
                                    valuetoset = ''
                                else:
                                    valuetoset = ids[i][j + 1]
                                txt = self.widget.dbase.getConstraintTextFromRawValue(self.currenttype,fieldname,valuetoset)
                                self.tableWidget.cellWidget(i, j).setCurrentIndex(self.tableWidget.cellWidget(i, j).findText(txt))
                            else:
                                self.tableWidget.setItem(i, j, QTableWidgetItem( str(ids[i][j+1])  ))
                                #self.tableWidget.item(i, j).setText( str(ids[i][j+1])   )
                        self.tableWidget.setCurrentCell(i, 0)
            else:
                #sql = "SELECT id_" + self.currenttype.lower()  +"," + ",".join(self.headerlist) + " FROM " + self.currentlinkage['tabletc']
                #sql += " WHERE " + self.currentlinkage['idtcsource'] + " = " + str(self.widget.currentFeature[self.currentlinkage['idsource']])

                #bug qgis
                #curfeatview = self.widget.dbasetable['layerview'].getFeatures(qgis.core.QgsFeatureRequest(self.widget.currentFeature.id())).next()
                """
                if self.widget.dbasetable['layerqgis'].isSpatial():
                    curfeatviewidsource = self.widget.dbasetable['layerqgis'].getFeatures(qgis.core.QgsFeatureRequest(self.widget.currentFeature.id())).next()[self.currentlinkage['idsource']]
                    sql = "SELECT " +self.currentlinkage['idsource'] + "FROM
                else:
                """
                #sql = "SELECT lk_prestation FROM Ressource WHERE Ressource.id_ressource = " + str(feat['id_ressource'])
                #sql = "SELECT " +self.currentlinkage['idsource'] + " FROM " +self.widget.dbasetablename + "_view  "
                sql = "SELECT " + self.currentlinkage['idsource'] + " FROM " + self.widget.dbasetablename
                sql += " WHERE pk_" + self.widget.dbasetablename  + " = " + str(self.widget.currentFeature.id())
                query = self.widget.dbase.query(sql)


                if False:
                    curfeatviewidsource = [row[0] for row in query][0]
                    if curfeatviewidsource is None:
                        curfeatviewidsource = 'NULL'

                    sql = "SELECT " + self.currentlinkage['iddest'] + " FROM " + self.currenttype
                    sql += " WHERE " + self.currentlinkage['iddest'] + " = " + str(curfeatviewidsource)
                    query = self.widget.dbase.query(sql)


                if len(query)>0:
                    ids = [row[0] for row in query]
                    self.addrow()
                    if len(ids)> 0 and not self.widget.dbase.isAttributeNull(ids[0]):
                        self.tableWidget.setItem(0,0,QTableWidgetItem( str(ids[0])))
                    else :
                        self.tableWidget.setItem(0,0,QTableWidgetItem( ''))


    def resetFromGeometry(self):

        quit_msg = "Les changements seront immeddiats. voulez vous continuer ?"
        reply = QMessageBox.question(self, 'Message',
                                           quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.widget.initLinkageFromGeometry(self.currenttype)
            self.tableWidget.setRowCount(0)
            self.populateTable()




    def addrow(self):
        introw = self.tableWidget.currentRow()
        self.tableWidget.insertRow(introw+1)
        self.configureRow(introw+1)


    def configureRow(self,row):
        for i, fieldname in enumerate(self.headerlist):
            if fieldname in self.dbasetc['fields'].keys() and 'Cst' in self.dbasetc['fields'][fieldname].keys():  # case tc
                combo = QComboBox()
                #print(self.dbasetc['fields'][fieldname]['Cst'])
                namelist = [elem[0] for elem in self.dbasetc['fields'][fieldname]['Cst']]
                combo.addItems(namelist)
                self.tableWidget.setCellWidget(row, i, combo)


        
    def removerow(self):
        introw = self.tableWidget.currentRow()
        self.tableWidget.removeRow(introw)
        if  introw != 0 and  introw != (self.tableWidget.rowCount()):
            self.tableWidget.setItem(introw, 1, QTableWidgetItem(self.tableWidget.item(introw-1,2)))
        
        
    def checkUpperLower(self, row,column):
        try:
            self.tableWidget.cellChanged.disconnect(self.checkUpperLower)
        except Exception as e:
            pass
        if column == 1:
            self.tableWidget.setItem(row-1, 2, QTableWidgetItem(self.tableWidget.item(row,column)))
        elif column == 2:
            self.tableWidget.setItem(row+1, 1, QTableWidgetItem(self.tableWidget.item(row,column)))
        
        self.tableWidget.cellChanged.connect(self.checkUpperLower)
        
        
    def PickObject(self):
        sender = self.sender()

            
    def dialogIsFinished(self):
        """
        return level list
        return color array like this : [stop in 0 < stop > 1 ,r,g,b,alpha]
        """
        pass
        if False:
            print(self.tableWidget.rowCount())
            #ids = [int(self.tableWidget.item(i,0).text()) for i in range(self.tableWidget.rowCount())]
            if (self.result() == 1):
                #colors, levels = self.returnColorsLevels()
                return self.currenttype, ids
            else:
                return None,None
            


    def save(self):
        # *************************
        # save Linkage
        #for type in self.linkageids.keys():
        #linkagetemp = self.currentlinkage
        #first delete existing


        if self.currentlinkage['tabletc'] is not None:
            sql = "DELETE FROM " + self.currentlinkage['tabletc']  + " WHERE  " + self.currentlinkage['idtcsource'] + " =  " + str(self.widget.currentFeature[self.currentlinkage['idsource']]) + ";"
            #sql = "INSERT INTO " + self.currentlinkage['tabletc'] + " (" + self.currentlinkage['idtcsource'] + "," +  self.currentlinkage['idtcdest'] + ") "
            #sql += "VALUES(" + str(self.currentFeature[self.currentlinkage['idsource']]) + "," + str(id) + " );"
            # print(sql)
            query = self.widget.dbase.query(sql)
            self.widget.dbase.commit()



            #then add
            #for id in self.linkageids[type]:
            for row in range(self.tableWidget.rowCount()):
                if False:
                    sql = "INSERT INTO " + self.currentlinkage['tabletc'] + " (" + self.currentlinkage['idtcsource'] + "," +  self.currentlinkage['idtcdest'] + ") "
                    sql += "VALUES(" + str(self.currentFeature[self.currentlinkage['idsource']]) + "," + str(id) + " );"

                rowvalues = []
                for column in range(self.tableWidget.columnCount()):
                    if self.tableWidget.cellWidget(row,column) is not None:
                        wdg = self.tableWidget.cellWidget(row,column)
                        if isinstance(wdg, QComboBox):
                            #rowvalues.append("'" + self.widget._getConstraintRawValueFromText(self.currenttype,self.headerlist[column], wdg.currentText()) + "'")
                            rowvalues.append("'" + self.widget.dbase.getConstraintRawValueFromText(self.currenttype,
                                                                                              self.headerlist[column],
                                                                                              wdg.currentText()) + "'")
                    elif self.tableWidget.item(row,column) is not None:
                        if self.tableWidget.item(row,column).text() in ['', 'None']:
                            valuetoset = 'NULL'
                        else:
                            valuetoset = self.tableWidget.item(row,column).text()
                        rowvalues.append(valuetoset )
                    else:
                        rowvalues.append('NULL')

                sql = "INSERT INTO " + self.currentlinkage['tabletc'] + " (" + self.currentlinkage['idtcsource'] + "," +  ",".join(self.headerlist) + ") "
                sql += "VALUES(" + str(self.widget.currentFeature[self.currentlinkage['idsource']]) + "," + ",".join(rowvalues) + " );"
                # print(sql)
                query = self.widget.dbase.query(sql)
                self.widget.dbase.commit()
        else:
            #search table
            actiontable = None
            for key in self.widget.linkuserwdg.keys():
                if self.currentlinkage['idsource'] in self.widget.dbase.dbasetables[key]['fields'].keys():
                    actiontable = key
                    break
            if actiontable is not None:
                if self.tableWidget.item(0,0).text() == '':
                    valuetoset = 'NULL'
                else:
                    valuetoset = self.tableWidget.item(0,0).text()
                sql = "UPDATE " + actiontable + " SET " + self.currentlinkage['idsource'] + " = " + valuetoset
                sql += " WHERE " + actiontable + "." + self.widget.linkuserwdg[actiontable]['linkfield']
                sql += " = " + str(self.widget.currentFeature[self.widget.linkuserwdg[actiontable]['linkfield']])
                print(sql)
                query = self.widget.dbase.query(sql)
                self.widget.dbase.commit()




