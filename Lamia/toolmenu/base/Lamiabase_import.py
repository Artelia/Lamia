# -*- coding: utf-8 -*-

import qgis
import os
#from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal

from .importtools.InspectionDigue_Import import ImportObjetDialog

try:
    from qgis.PyQt.QtGui import (QInputDialog,QTableWidgetItem,QComboBox)
except ImportError:
    from qgis.PyQt.QtWidgets import (QInputDialog,QTableWidgetItem,QComboBox)


class importShapefileBaseWorker(object):

    #def __init__(self, dbase, importtable, results):
    def __init__(self, dbase=None, windowdialog=None):
        #AbstractWorker.__init__(self)
        self.dbase = dbase
        #self.importtable = importtable
        #self.results = results
        self.windowdialog = windowdialog

        self.importobjetdialog = ImportObjetDialog()

        lauchaction = QtGui.QAction(QtGui.QIcon(), 'Import',self.windowdialog.menuPreferences)
        lauchaction.triggered.connect(self.launchDialog)
        self.windowdialog.menuOutils.addAction(lauchaction)


        self.postInit()




    def postInit(self):
        pass


    def launchDialog(self):

        items = ("Points topo", "Infralineaire")
        item, ok = QInputDialog.getItem(None, "select input dialog",
                                        "list of languages", items, 0, False)
        if ok and item:
            if self.dbase.qgsiface is not None:
                # if not self.dbase.standalone:
                currentlayer = self.dbase.qgsiface.activeLayer()
                currentlayerfields = currentlayer.fields()
                currentlayerfieldsname = [''] + [field.name() for field in currentlayerfields]
                # combofield = QComboBox([''] + currentlayerfieldsname)
            else:  # debug outside qgis
                currentlayerfieldsname = ['', 'ALTINGF', 'typ']

            if item == "Points topo":
                print('ok')
                templinkuserwgd = self.dbase.dbasetables['Topographie']['widget'][0].propertieswdgPOINTTOPO.linkuserwdg
            if item == "Infralineaire":
                templinkuserwgd = self.dbase.dbasetables['Infralineaire']['widget'][0].linkuserwdg
            if item == "Desordre":
                templinkuserwgd = self.dbase.dbasetables['Desordre']['widget'][0].linkuserwdg
            if item == "Observation":
                templinkuserwgd = self.dbase.dbasetables['Observation']['widget'][0].linkuserwdg
            if item == "Noeud":
                templinkuserwgd = self.dbase.dbasetables['Noeud']['widget'][0].linkuserwdg
            if item == "Equipement":
                templinkuserwgd = self.dbase.dbasetables['Equipement']['widget'][0].linkuserwdg
            if item == "Travaux":
                templinkuserwgd = self.dbase.dbasetables['Travaux']['widget'][0].linkuserwdg
            if item == "Environnement":
                templinkuserwgd = self.dbase.dbasetables['Environnement']['widget'][0].linkuserwdg

            self.importobjetdialog.tableWidget.setRowCount(0)
            self.importobjetdialog.tableWidget.setColumnCount(2)
            for tablename in templinkuserwgd:
                if tablename in self.dbase.dbasetables.keys():
                    dbasetable = self.dbase.dbasetables[tablename]
                    for field in dbasetable['fields'].keys():
                        # print(field)
                        rowPosition = self.importobjetdialog.tableWidget.rowCount()
                        self.importobjetdialog.tableWidget.insertRow(rowPosition)
                        itemfield = QTableWidgetItem(tablename + '.' + field)
                        itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.importobjetdialog.tableWidget.setItem(rowPosition, 0, itemfield)
                        # item.setFlags()
                        if field[0:2] != 'id' and field[0:2] != 'pk' :
                            combofield = QComboBox()
                            combofield.addItems(currentlayerfieldsname)
                            self.importobjetdialog.tableWidget.setCellWidget(rowPosition, 1, combofield)
                        else:
                            itemfield = QTableWidgetItem('')
                            self.importobjetdialog.tableWidget.setItem(rowPosition, 1, itemfield)

            self.importobjetdialog.exec_()
            tableview = self.importobjetdialog.dialogIsFinished()
            if tableview is not None:
                result = []
                for row in range(self.importobjetdialog.tableWidget.rowCount()):
                    if self.importobjetdialog.tableWidget.cellWidget(row, 1) is not None:
                        result.append([self.importobjetdialog.tableWidget.item(row, 0).text(),
                                       self.importobjetdialog.tableWidget.cellWidget(row, 1).currentText()])
                    else:
                        result.append([self.importobjetdialog.tableWidget.item(row, 0).text(),
                                       self.importobjetdialog.tableWidget.item(row, 1).text()])
                print(result)

                if False:
                    self.worker = ImportObjectWorker(self.dbase, item, result)
                    self.worker.finished.connect(self.exportPDFFinished)
                    self.worker.error.connect(self.printError)
                    self.worker.message.connect(self.printMessage)
                    self.worker.run()
                if True:
                    self.work(result)


    def work(self,linktable):
        self.results = linktable

        #print(self.importtable)

        tablestemp = [result[0].split('.')[0] for result in self.results]
        tables = list(set(tablestemp))
        # print(tables)

        print(self.results)

        tablefield = [result[0] for result in self.results]
        values = [result[1] for result in self.results]

        if self.dbase.qgsiface is not None:
            layer = self.dbase.qgsiface.activeLayer()
        else:
            layer = qgis.core.QgsVectorLayer('C://001_travail_BM//testtopo//toposijalag1.shp', 'test', "ogr")

        layerfromfieldsname = [field.name() for field in layer.fields()]
        print('layerfromfieldsname',layerfromfieldsname)
        xform = qgis.core.QgsCoordinateTransform(layer.crs(), self.dbase.qgiscrs)
        if len(layer.selectedFeatures()) == 0:
            feats  = layer.getFeatures()
        else:
            feats = layer.selectedFeatures()



        if self.importtable == 'Points topo':
            table = 'Pointtopo'
            fielddestination=['typepointtopo', 'x', 'y', 'zgps', 'zwgs84', 'raf09', 'zmngf', 'precision', 'dx', 'dy', 'dz', 'hauteurperche',
                    'id_topographie','geom']


            linktable = {}
            for i, result in enumerate(self.results):
                for j, field in enumerate(fielddestination):
                    if table + '.' + field in result:
                        linktable[j] = i

            # print(linktable)




            for layerfeat in feats:
                sql = "INSERT INTO Pointtopo (" + ', '.join(fielddestination) + ") "
                sql += "VALUES("
                featvalues = []
                for i, field in enumerate(fielddestination):
                    # print('values',field,featvalues)
                    if field == 'geom':
                        featgeom = layerfeat.geometry()
                        success = featgeom.transform(xform)
                        featgeomwkt = featgeom.exportToWkt()

                        geomsql = "ST_GeomFromText('"
                        geomsql += featgeomwkt
                        geomsql += "', " + str(self.dbase.crsnumber) + ")"
                        featvalues.append(geomsql)
                    else:
                        valuefieldtemp = values[linktable[i]]
                        # print(valuefieldtemp, layerfromfieldsname)
                        if valuefieldtemp == '':
                            featvalues.append('NULL')
                        else:


                            if valuefieldtemp in layerfromfieldsname:
                                valuefieldtemp = layerfeat[valuefieldtemp]
                                # print(valuefieldtemp)
                                if valuefieldtemp is None:
                                    featvalues.append('NULL')
                                else:
                                    # print(type(valuefieldtemp))
                                    if isinstance(valuefieldtemp, unicode):
                                        featvalues.append("'" + str(valuefieldtemp) + "'")
                                    else:
                                        featvalues.append(str(valuefieldtemp))
                            else:
                                featvalues.append(str(valuefieldtemp))


                sql += ', '.join(featvalues)
                sql += ");"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()




        if self.importtable == 'Infralineaires':
            table = 'Infralineaire'
            fielddestination=['description1', 'description2', 'importancestrat', 'etatfonct', 'datederniereobs', 'qualitegeoloc', 'parametres', 'listeparametres', 'datecreation', 'datemodification', 'datedestruction', 'commentaire', 'libelle', 'geom']


            linktable = {}
            for i, result in enumerate(self.results):
                for j, field in enumerate(fielddestination):
                    if 'Infralineaire.' + field in result or 'Objet.'+ field in result or 'Descriptionsystem.' + field in result :
                        linktable[j] = i

            # print(linktable)




            for layerfeat in feats:
                sql = "INSERT INTO Objet (datecreation, datemodification, datedestruction, commentaire, libelle) VALUES ('"
                featvalues = []
                for i, field in enumerate(fielddestination):
                    if field in ['datecreation', 'datemodification', 'datedestruction', 'commentaire', 'libelle']:
                        valuefieldtemp = values[linktable[i]]
                        # print(valuefieldtemp, layerfromfieldsname)
                        if valuefieldtemp == '':
                            featvalues.append('NULL')
                        else:


                            if valuefieldtemp in layerfromfieldsname:
                                valuefieldtemp = layerfeat[valuefieldtemp]
                                # print(valuefieldtemp)
                                if valuefieldtemp is None:
                                    featvalues.append('NULL')
                                else:
                                    # print(type(valuefieldtemp))
                                    if isinstance(valuefieldtemp, unicode):
                                        featvalues.append("'" + str(valuefieldtemp) + "'")
                                    else:
                                        featvalues.append(str(valuefieldtemp))
                            else:
                                featvalues.append(str(valuefieldtemp))


                sql += ', '.join(featvalues)
                sql += ") RETURNING id_objet;"
                # print(sql)
                id_objet = self.dbase.query(sql)
                self.dbase.commit()



            for layerfeat in feats:
                sql = "INSERT INTO Descriptionsystem (id_objet, importancestrat, etatfonct, datederniereobs, qualitegeoloc, parametres, listeparametres) VALUES ('"
                sql += str(id_objet)+', '
                featvalues = []
                for i, field in enumerate(fielddestination):
                    if field in ['importancestrat', 'etatfonct', 'datederniereobs', 'qualitegeoloc', 'parametres', 'listeparametres']:
                        valuefieldtemp = values[linktable[i]]
                        # print(valuefieldtemp, layerfromfieldsname)
                        if valuefieldtemp == '':
                            featvalues.append('NULL')
                        else:


                            if valuefieldtemp in layerfromfieldsname:
                                valuefieldtemp = layerfeat[valuefieldtemp]
                                # print(valuefieldtemp)
                                if valuefieldtemp is None:
                                    featvalues.append('NULL')
                                else:
                                    # print(type(valuefieldtemp))
                                    if isinstance(valuefieldtemp, unicode):
                                        featvalues.append("'" + str(valuefieldtemp) + "'")
                                    else:
                                        featvalues.append(str(valuefieldtemp))
                            else:
                                featvalues.append(str(valuefieldtemp))


                sql += ', '.join(featvalues)
                sql += ") RETURNING id_descriptionsystem;"
                # print(sql)
                id_descriptionsystem = self.dbase.query(sql)
                self.dbase.commit()




                sql = "INSERT INTO Infralineaires (id_objet, id_descriptionsystem, description1, description2, geom) "
                sql += "VALUES("+str(id_objet)+', '+str(id_descriptionsystem)+', '
                featvalues = []
                for i, field in enumerate(fielddestination):
                    # print('values',field,featvalues)
                    if field == 'geom':
                        featgeom = layerfeat.geometry()
                        success = featgeom.transform(xform)
                        featgeomwkt = featgeom.exportToWkt()

                        geomsql = "ST_GeomFromText('"
                        geomsql += featgeomwkt
                        geomsql += "', " + str(self.dbase.crsnumber) + ")"
                        featvalues.append(geomsql)
                    else:
                        if field in ['description1', 'description2']:
                            valuefieldtemp = values[linktable[i]]
                            # print(valuefieldtemp, layerfromfieldsname)
                            if valuefieldtemp == '':
                                featvalues.append('NULL')
                            else:


                                if valuefieldtemp in layerfromfieldsname:
                                    valuefieldtemp = layerfeat[valuefieldtemp]
                                    # print(valuefieldtemp)
                                    if valuefieldtemp is None:
                                        featvalues.append('NULL')
                                    else:
                                        # print(type(valuefieldtemp))
                                        if isinstance(valuefieldtemp, unicode):
                                            featvalues.append("'" + str(valuefieldtemp) + "'")
                                        else:
                                            featvalues.append(str(valuefieldtemp))
                                else:
                                    featvalues.append(str(valuefieldtemp))


                sql += ', '.join(featvalues)
                sql += ");"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()








