# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
"""
"""
from qgis.PyQt.QtWidgets import (QWidget, QTreeWidgetItem, QMessageBox, QFileDialog, QTableWidget,
                                     QHeaderView, QComboBox, QSpinBox,QCheckBox, QPushButton, QDateEdit,QDateTimeEdit, QTextEdit,
                                     QDoubleSpinBox, QDialog, QVBoxLayout, QTreeWidget, QLineEdit, QCheckBox,
                                     QLabel, QMessageBox, QTextBrowser, QTableWidgetItem,QApplication,QToolButton, QAbstractItemView)
"""
from qgis.PyQt.QtWidgets import (QComboBox, QTextEdit,QLineEdit,  QSpinBox, QDoubleSpinBox,
                                 QDateEdit,QDateTimeEdit, QTextBrowser, QCheckBox, QLabel)
from qgis.PyQt import QtCore
import qgis, logging, datetime, os
import qgis.core

class FormToolUtils(QtCore.QObject):

    def __init__(self, formtoolwidget):
        super(FormToolUtils, self).__init__()
        self.formtoolwidget = formtoolwidget
        

    def ___________________actionsOnWidgetCreation(self):
        pass

    def initWidgetBehaviour(self):
        print('initWidgetBehaviour', self.formtoolwidget.DBASETABLENAME)
        templinkuserwgd = self.formtoolwidget.formtoolwidgetconfdict
        if templinkuserwgd is None:
            raise TypeError('formtoolwidgetconfdict of {} is None'.format(self.formtoolwidget.DBASETABLENAME))

        for tablename in templinkuserwgd:
            dbasetables = self.formtoolwidget.dbase.dbasetables

            if tablename in dbasetables.keys():
                dbasetable = dbasetables[tablename]
                for field in dbasetable['fields'].keys():
                    # for linkuserwdg in [self.linkuserwdg]:
                    for linkuserwdg in [templinkuserwgd]: 
                        if linkuserwdg is None or linkuserwdg.keys() is None:
                            continue

                        if (tablename in linkuserwdg.keys()
                                and field in linkuserwdg[tablename]['widgets'].keys()):
                            
                            wdgs = linkuserwdg[tablename]['widgets'][field]
                            print(wdgs)
                            if 'Cst' in dbasetable['fields'][field].keys():
                                # combox filling with constraints
                                if isinstance(wdgs, QComboBox) or (
                                        isinstance(wdgs, list) and isinstance(wdgs[0], QComboBox)):

                                    templist = [description[0] for description in
                                                dbasetable['fields'][field]['Cst']]
                                    if isinstance(wdgs, QComboBox):
                                        wdgs = [wdgs]
                                    for wdg in wdgs:
                                        wdg.clear()
                                        wdg.addItems(templist)
                                        print(wdg.objectName(), templist)

                            if 'ParFldCst' in dbasetable['fields'][field].keys():
                                nameparentfield = dbasetable['fields'][field]['ParFldCst']
                                # userwidget
                                if (tablename in linkuserwdg.keys() and 'widgets' in linkuserwdg[tablename].keys()
                                        and nameparentfield in linkuserwdg[tablename]['widgets'].keys()
                                        and isinstance(linkuserwdg[tablename]['widgets'][nameparentfield], QComboBox)):
                                    linkuserwdg[tablename]['widgets'][nameparentfield].currentIndexChanged.connect(self.comboparentValueChanged)

                            # multiple wdg for field management
                            if isinstance(wdgs, list):
                                if isinstance(wdgs[0], QComboBox):
                                    for wdg in wdgs:
                                        wdg.currentIndexChanged.connect(self.manageMultipleWidgetField)
                                elif isinstance(wdgs[0], QSpinBox) or isinstance(wdgs[0], QDoubleSpinBox):
                                    for wdg in wdgs:
                                        wdg.valueChanged.connect(self.manageMultipleWidgetField)

    def connectSubWidgetModifications(self):
        for table, tabledict in self.formtoolwidget.formtoolwidgetconfdict.items():
            for field, wdg in tabledict['widgets'].items():
                if isinstance(wdg, QTextEdit) or isinstance(wdg, QLineEdit):
                    wdg.textChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QSpinBox) or isinstance(wdg, QDoubleSpinBox):
                    wdg.valueChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QComboBox):
                    wdg.currentIndexChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QDateEdit):
                    wdg.dateChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QDateTimeEdit):
                    wdg.dateTimeChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QCheckBox):
                    wdg.stateChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QLabel):
                    pass



    def initWidgetUI(self, basewidget):
        """
        Called by changePropertiesWidget

        - Init combobox with default values

        - Init Parent/child combobox behaviour
        """

        if self.linkuserwdg:
            templinkuserwgd = {self.dbasetablename: None}
        else:
            templinkuserwgd = self.linkuserwdg


        for tablename in templinkuserwgd:
            if tablename in self.dbase.dbasetables.keys():
                dbasetable = self.dbase.dbasetables[tablename]
                for field in dbasetable['fields'].keys():
                    for linkuserwdg in [self.linkuserwdg]:
                        if linkuserwdg is None or linkuserwdg.keys() is None:
                            continue

                        if (tablename in linkuserwdg.keys()
                                and field in linkuserwdg[tablename]['widgets'].keys()):
                            wdgs = linkuserwdg[tablename]['widgets'][field]
                            if 'Cst' in dbasetable['fields'][field].keys():
                                # combox filling with constraints
                                if isinstance(wdgs, QComboBox) or (
                                        isinstance(wdgs, list) and isinstance(wdgs[0], QComboBox)):

                                    templist = [description[0] for description in
                                                dbasetable['fields'][field]['Cst']]
                                    if isinstance(wdgs, QComboBox):
                                        wdgs = [wdgs]
                                    for wdg in wdgs:
                                        wdg.clear()
                                        wdg.addItems(templist)

                            if 'ParFldCst' in dbasetable['fields'][field].keys():
                                nameparentfield = dbasetable['fields'][field]['ParFldCst']
                                # userwidget
                                if (tablename in linkuserwdg.keys() and 'widgets' in linkuserwdg[tablename].keys()
                                        and nameparentfield in linkuserwdg[tablename]['widgets'].keys()
                                        and isinstance(linkuserwdg[tablename]['widgets'][nameparentfield], QComboBox)):
                                    linkuserwdg[tablename]['widgets'][nameparentfield].currentIndexChanged.connect(self.comboparentValueChanged)

                            # multiple wdg for field management
                            if isinstance(wdgs, list):
                                if isinstance(wdgs[0], QComboBox):
                                    for wdg in wdgs:
                                        wdg.currentIndexChanged.connect(self.manageMultipleWidgetField)
                                elif isinstance(wdgs[0], QSpinBox) or isinstance(wdgs[0], QDoubleSpinBox):
                                    for wdg in wdgs:
                                        wdg.valueChanged.connect(self.manageMultipleWidgetField)


    def manageMultipleWidgetField(self):
        """
        Activated by widget.valueChanged or widget.currentIndexChanged signal

        Manage multiple combobox or spinbox linked to one table field
        """
        senderwdg = self.sender()

        #for tablename in self.linkuserwdg:
        for tablename in self.formtoolwidget.formtoolwidgetconfdict:
            #for fieldname in self.linkuserwdg[tablename]['widgets'].keys():
            for fieldname in self.formtoolwidget.formtoolwidgetconfdict[tablename]['widgets'].keys():
                # wdgs = self.linkuserwdg[tablename]['widgets'][fieldname]
                wdgs = self.formtoolwidget.formtoolwidgetconfdict[tablename]['widgets'][fieldname]
                if isinstance(wdgs, list) and senderwdg in wdgs:
                    if isinstance(senderwdg, QComboBox):
                        for wdg in wdgs:
                            if wdg != senderwdg:
                                try:
                                    wdg.currentIndexChanged.disconnect(self.manageMultipleWidgetField)
                                except:
                                    pass
                                wdg.setCurrentIndex(senderwdg.currentIndex())
                                wdg.currentIndexChanged.connect(self.manageMultipleWidgetField)
                        break
                    elif isinstance(senderwdg, QSpinBox) or isinstance(senderwdg, QDoubleSpinBox):
                        for wdg in wdgs:
                            if wdg != senderwdg:
                                try:
                                    wdg.valueChanged.disconnect(self.manageMultipleWidgetField)
                                except:
                                    pass
                                wdg.setValue(senderwdg.value())
                                wdg.valueChanged.connect(self.manageMultipleWidgetField)
                        break


    def comboparentValueChanged(self, index):
        """
        Activated by currentIndexChanged

        Manage paret/child combobox
        """

        debug = False
        if debug:
            senderwdg = self.sender()
            print('**', senderwdg.objectName())

        senderwdg = self.sender()
        if isinstance(senderwdg, QComboBox) and senderwdg.count() == 0:  # case triple descendant and parent not filled
            return

        #if self.groupBox_properties.layout().itemAt(0) is None:
        #    return

        parenttablename = None
        parentfieldname = None

        if (self.formtoolwidget.toolwidget == self.formtoolwidget.toolwidgetmain or 
                self.formtoolwidget.toolwidget == self.formtoolwidget.toolwidgetadvanced):
            comefromrawtable = False
            if self.formtoolwidget.formtoolwidgetconfdict is not None:
                for tablename, tabledict in self.formtoolwidget.formtoolwidgetconfdict.items():
                    for fieldname in tabledict['widgets'].keys():
                        if senderwdg == tabledict['widgets'][fieldname]:
                            parenttablename = tablename
                            parentfieldname = fieldname
                            break

        #if self.groupBox_properties.layout().itemAt(0).widget() == self.userwdg:
        #    comefromrawtable = False
        #    if self.linkuserwdg is not None:
        #        for tablename in self.linkuserwdg.keys():
        #            for fieldname in self.linkuserwdg[tablename]['widgets'].keys():
        #                if senderwdg == self.linkuserwdg[tablename]['widgets'][fieldname]:
        #                    parenttablename = tablename
        #                    parentfieldname = fieldname
        #                    break
        #
        #elif self.groupBox_properties.layout().itemAt(0).widget() == self.tableWidget:
        #    ind = self.tableWidget.indexAt(senderwdg.pos()).row()
        #    parenttablename, parentfieldname = self.tableWidget.item(ind, 0).text().split('.')
        #    comefromrawtable = True

        if parenttablename is None:
            return

        try:
            parentcstvalue = self.formtoolwidget.dbase.getConstraintRawValueFromText(parenttablename, parentfieldname,
                                                                      senderwdg.currentText())
        except Exception as e:
            logging.getLogger("Lamia_unittest").debug('error %s %s %s', e, parenttablename, parentfieldname)


        dbasetable = self.formtoolwidget.dbase.dbasetables[parenttablename]
        # get child index and combochild
        listparentcst = [dbasetable['fields'][field]['ParFldCst']
                         if 'ParFldCst' in dbasetable['fields'][field].keys() else None
                         for field in dbasetable['fields'].keys()]

        childfieldnames = [list(dbasetable['fields'].keys())[i] for i in range(len(listparentcst))
                           if parentfieldname == listparentcst[i]]

        if debug: print('**', listparentcst)
        if debug: print('***', childfieldnames)

        if comefromrawtable:
            listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
            for childfieldname in childfieldnames:
                if dbasetable['fields'][parentfieldname][
                    'PGtype'] == 'INT' and parentcstvalue != '' and parentcstvalue is not None:
                    parentcstvalue = int(parentcstvalue)
                listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if
                             parentcstvalue in value[2]]
                indexchildintable = listfieldname.index(parenttablename + '.' + childfieldname)
                combochild = self.tableWidget.cellWidget(indexchildintable, 1)
                combochild.clear()
                if len(listtoadd) > 0:
                    combochild.addItems(listtoadd)
        else:
            for childfieldname in childfieldnames:
                if dbasetable['fields'][parentfieldname]['PGtype'] == 'INT' and parentcstvalue != '' and parentcstvalue is not None:
                    parentcstvalue = int(parentcstvalue)


                listtoadd = [value[0] for value in dbasetable['fields'][childfieldname]['Cst'] if (value[2] is None or parentcstvalue in value[2])]

                if debug: print('****', listtoadd)
                wdgconfdict = self.formtoolwidget.formtoolwidgetconfdict
                if childfieldname in wdgconfdict[parenttablename]['widgets']:
                    combochild = wdgconfdict[parenttablename]['widgets'][childfieldname]
                    combochild.clear()
                    if len(listtoadd) > 0:
                        combochild.addItems(listtoadd)

    def ___________________actionsOnFeatureSelection(self):
        pass

    def getDictValuesForWidget(self, featurepk=None):
        columns = self.formtoolwidget.dbase.getColumns(self.formtoolwidget.DBASETABLENAME + '_qgis')
        if len(columns) == 0:   #table without qgis view ex : graphdata, pointtopo
            columns = self.formtoolwidget.dbase.getColumns(self.formtoolwidget.DBASETABLENAME)

        if not featurepk:
            values = [None] * len(columns)
        else:
            sql = "SELECT * FROM {} WHERE pk_{} = {}".format(self.formtoolwidget.DBASETABLENAME + '_qgis',
                                                            self.formtoolwidget.DBASETABLENAME.lower(),
                                                            featurepk)
            values = self.formtoolwidget.dbase.query(sql)[0]
        
        resdict = dict(zip(columns, values))
        return resdict

    def applyResultDict(self, resultdict, checkifinforgottenfield=True):
        
        if self.formtoolwidget.mainifacewidget.interfacemode in [0, 1]:
            for tablename, tabledict in self.formtoolwidget.formtoolwidgetconfdict.items():
                for field, fieldwdg in tabledict['widgets'].items():
                    if not field in resultdict.keys():
                        if checkifinforgottenfield:
                            logging.getLogger("Lamia_unittest").debug('%s : field %s-%s not found in dictconf : %s', self.formtoolwidget.DBASETABLENAME,
                                                                                                                tablename,
                                                                                                            field,
                                                                                                            resultdict.keys())
                        continue
                        # raise ValueError
                    self.setValueInWidget(fieldwdg, 
                                          resultdict[field], 
                                          tablename,
                                          field)




    def showImageinLabelWidget(self,wdg,savedfile):
        """
        Show the image file in the text widget
        Manage thumbnail image

        :param wdg: the text widget
        :param savedfile: the image file

        """
        filetoshow = self.formtoolwidget.dbase.completePathOfFile(savedfile)
        possiblethumbnail,ext = os.path.splitext(filetoshow)
        if os.path.isfile(possiblethumbnail + "_thumbnail.png"):
            filetoshow = possiblethumbnail + "_thumbnail.png"

        if os.path.isfile(filetoshow):
            wdg.clear()
            wdg.setPixmap(filetoshow)
        else:
            wdg.clear()
            wdg.setText('Image non trouvee')

    def ___________________actionsOnFeatureSave(self):
        pass

    def saveFeature(self, featurepk=None):
        #self.currentFeature, self.currentFeaturePK = self.manageFeatureCreationOrUpdate()

        dbasetablehasgeomfield = self.formtoolwidget.dbase.dbasetables[self.formtoolwidget.DBASETABLENAME].get('geom', None)
        geometryskip = False
        if hasattr(self.formtoolwidget, 'GEOMETRYSKIP') and self.formtoolwidget.GEOMETRYSKIP :
            geometryskip = True
        # print('dbasetablehasgeomfield',self.formtoolwidget.DBASETABLENAME, dbasetablehasgeomfield)
        if (dbasetablehasgeomfield is not None and featurepk is None 
                and self.formtoolwidget.tempgeometry is None
                and not geometryskip):     # assure taht a geometry is acquired on first creation
            self.formtoolwidget.mainifacewidget.connector.showErrorMessage('Geometry needed')
            return
        
        if hasattr(self.formtoolwidget, 'GEOMETRYSKIP') and self.formtoolwidget.GEOMETRYSKIP :
            pass

        savedfeaturepk = self.manageFeatureCreationOrUpdate(featurepk)

        if not geometryskip:
            self.setGeometryToFeature(savedfeaturepk)
        self.saveFeatureProperties(savedfeaturepk)
        self.saveTABLEFILTERFIELD(savedfeaturepk)
        self.formtoolwidget.postSaveFeature(savedfeaturepk)  #featurepk toknow if new or not
        for lidchooser in self.formtoolwidget.lamiawidgets:
            lidchooser.postSaveFeature(savedfeaturepk)
        self.saveRessourceFile(savedfeaturepk)
        self._saveParentWidgetRelation(savedfeaturepk)

        self.updateDateModification(savedfeaturepk)
        self._reinitAfterSaving()

        self.formtoolwidget.selectFeature(pk=savedfeaturepk)



    def manageFeatureCreationOrUpdate(self, featurepk=None):
        """
        Called by saveFeature - Manage versioning
        return pk of object
        """

        currentFeature = None
        dbase = self.formtoolwidget.mainifacewidget.dbase

        #if self.currentFeaturePK is not None :
        if featurepk is not None :
            if 'lpk_revision_begin' in dbase.getColumns(self.formtoolwidget.DBASETABLENAME + '_qgis'):
                featlastrevision = dbase.getValuesFromPk(self.formtoolwidget.DBASETABLENAME + '_qgis',
                                                        'lpk_revision_begin',
                                                            featurepk)

                if featlastrevision != dbase.maxrevision:   #new version feature
                    self.formtoolwidget.dbase.createNewFeatureVersion(self.formtoolwidget.DBASETABLENAME,
                                                                            featurepk)
                    pktoreturn= self.formtoolwidget.dbase.getLastPK(self.formtoolwidget.DBASETABLENAME)
                else:       #simple feature update
                    pktoreturn = featurepk
            else:
                pktoreturn = featurepk

        else:           # feature creation
            pktoreturn = self.formtoolwidget.dbase.createNewFeature(self.formtoolwidget.DBASETABLENAME)

        return pktoreturn


    def setGeometryToFeature(self, featurepk=None):

        """
        Methode pour assigner le self.tempgeometry au self.currenfeature
        cree le self.currenfeature si besoin

        """

        rawgeom = self.formtoolwidget.tempgeometry
        if rawgeom is None:         #geom no modified
            return

        processedgeom, success = self._convertGeomToProperGeom(rawgeom)

        # geometry conversion first
        """
        if (self.tempgeometry is not None and self.dbasetable['geom'] in ['POINT', 'LINESTRING', 'POLYGON']
                 and self.tempgeometry.isMultipart()):
            success = self.tempgeometry.convertToSingleType()
        elif (self.tempgeometry is not None and self.dbasetable['geom'] in ['MULTIPOLYGON']
                and not self.tempgeometry.isMultipart()):
            success = self.tempgeometry.convertToMultiType()

        if (self.dbasetable is not None and 'geom' in self.dbasetable.keys() and self.dbasetable['geom'] == 'LINESTRING'
            and self.tempgeometry is not None and self.tempgeometry.type() == 0): # case point in linestring layer
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.tempgeometry = qgis.core.QgsGeometry.fromPolyline([self.tempgeometry.asPoint(),
                                                                        self.tempgeometry.asPoint()])
            else:
                self.tempgeometry = qgis.core.QgsGeometry.fromPolylineXY([self.tempgeometry.asPoint(),
                                                                        self.tempgeometry.asPoint()])
        """
        #remove duplicate from linestring
        dbasetable = self.formtoolwidget.dbase.dbasetables[self.formtoolwidget.DBASETABLENAME]
        processedgeom = self._removeDuplicatesFromGeom(processedgeom)
        """
        if True:
            if self.tempgeometry is not None and self.dbasetable['geom'] in [ 'LINESTRING'] :
                if sys.version_info.major == 3:
                    geomaspoly  = self.tempgeometry.asPolyline()
                    geomfinal = [geomaspoly[0]]
                    if not self.dbase.areNodesEquals(geomaspoly[0], geomaspoly[-1]):
                        for index in range(len(geomaspoly) -1 ):
                            if not self.dbase.areNodesEquals(geomaspoly[index], geomaspoly[index +1] ):
                                geomfinal.append(geomaspoly[index +1])
                    self.tempgeometry = qgis.core.QgsGeometry.fromPolylineXY(geomfinal)

        """
        self._setGeometryToFeature(featurepk=featurepk,qgsgeom=processedgeom  )
        """
        if self.currentFeature is None:
            self.currentFeature = qgis.core.QgsFeature(self.dbasetable['layer'].fields())

            if self.tempgeometry is not None:
                self.currentFeature.setGeometry(self.tempgeometry)
                pass
            else:
                if ('geom' in self.dbasetable.keys()
                        and (self.frame_editing.isVisible() and self.groupBox_geom.isVisible() and self.groupBox_geom.parent() )
                        and ((hasattr(self,'CHECKGEOM') and self.CHECKGEOM == True) or not hasattr(self,'CHECKGEOM'))):
                    self.windowdialog.errorMessage('Pas de geometrie selectionnee !!')
                    self.currentFeature = None
                    self.canvas.freeze(False)
                    return False

            self.savingnewfeature = True
        else:
            if self.tempgeometry is not None:
                self.currentFeature.setGeometry(self.tempgeometry)
                pass
        """
        
        return True

    def _convertGeomToProperGeom(self, qgsgeom):
        dbasetable = self.formtoolwidget.dbase.dbasetables[self.formtoolwidget.DBASETABLENAME]
        success = False
        if (qgsgeom is not None and dbasetable['geom'] in ['POINT', 'LINESTRING', 'POLYGON']
                 and qgsgeom.isMultipart()):
            success = qgsgeom.convertToSingleType()
        elif (qgsgeom is not None and dbasetable['geom'] in ['MULTIPOLYGON']
                and not qgsgeom.isMultipart()):
            success = qgsgeom.convertToMultiType()

        if (dbasetable is not None and 'geom' in dbasetable.keys() and dbasetable['geom'] == 'LINESTRING'
                and qgsgeom is not None and qgsgeom.type() == 0): # case point in linestring layer
            qgsgeom = qgis.core.QgsGeometry.fromPolylineXY([qgsgeom.asPoint(),
                                                                    qgsgeom.asPoint()])
        return qgsgeom, success

    def _removeDuplicatesFromGeom(self,qgsgeom):
        dbasetable = self.formtoolwidget.dbase.dbasetables[self.formtoolwidget.DBASETABLENAME]

        if qgsgeom is not None and dbasetable['geom'] in [ 'LINESTRING'] :
            geomaspoly  = qgsgeom.asPolyline()
            geomfinal = [geomaspoly[0]]
            areNodesEqualsFct = self.formtoolwidget.dbase.utils.areNodesEquals
            if not areNodesEqualsFct(geomaspoly[0], geomaspoly[-1]):
                for index in range(len(geomaspoly) -1 ):
                    if not areNodesEqualsFct(geomaspoly[index], geomaspoly[index +1] ):
                        geomfinal.append(geomaspoly[index +1])
                qgsgeom = qgis.core.QgsGeometry.fromPolylineXY(geomfinal)
        return qgsgeom
    
    def _setGeometryToFeature(self,featurepk, qgsgeom):
        sqlqgsgeom = qgsgeom.asWkt()
        sql = "UPDATE {} SET geom=ST_GeomFromText('{}',{}) WHERE pk_{}={}".format(self.formtoolwidget.DBASETABLENAME,
                                                                        sqlqgsgeom,
                                                                        self.formtoolwidget.dbase.crsnumber,
                                                                        self.formtoolwidget.DBASETABLENAME.lower(),
                                                                        featurepk)
        self.formtoolwidget.dbase.query(sql)
    
    def updateDateModification(self, featurepk):
        if 'Objet' in self.formtoolwidget.dbase.getParentTable(self.formtoolwidget.DBASETABLENAME):
            pkobjet = self.formtoolwidget.dbase.getValuesFromPk(self.formtoolwidget.DBASETABLENAME.lower() + "_qgis ",
                                                                'pk_objet',
                                                                featurepk)

            datemodif = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "UPDATE Objet SET datetimemodification = '" + datemodif + "'  WHERE pk_objet = " + str(pkobjet)
            self.formtoolwidget.dbase.query(sql)

    def saveFeatureProperties(self, featurepk=None):
        """
        Method called by saveFeature

        Method for saving feature properties of the ui in the tables
        """

        debug = False

        if self.formtoolwidget.mainifacewidget.interfacemode in [0, 1]:
            if self.formtoolwidget.formtoolwidgetconfdict is None :
                return
            for tablename, tabledict in self.formtoolwidget.formtoolwidgetconfdict.items():
                if len(tabledict['widgets'].keys()) == 0:
                    continue
                # get field values
                result = []
                for fieldname, fieldwdg in tabledict['widgets'].items():
                    fieldvaluetosave = self.getValueFromWidget(fieldwdg,
                                                               tablename,
                                                                fieldname)
                    if fieldvaluetosave is not None:
                        result.append(fieldvaluetosave)
                    else:
                        result.append(None)

                # get tablepk
                tablepk = self.formtoolwidget.dbase.getValuesFromPk(self.formtoolwidget.DBASETABLENAME + '_qgis',
                                                                    'pk_' + tablename.lower(),
                                                                        featurepk)
                """
                sql = "SELECT pk_" + str(tablename).lower() + " FROM " + str(self.dbasetablename).lower() + "_qgis"
                sql += "  WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
                tablepk = self.dbase.query(sql)[0][0]
                """

                # update sql
                fieldnames = tabledict['widgets'].keys()
                sql = "UPDATE " + str(tablename).lower() + " SET "
                for i, field in enumerate(fieldnames):
                    if isinstance(result[i], str) or isinstance(result[i], unicode) :
                        if result[i] != '':
                            resultstring = result[i]
                            if "'" in resultstring:
                                resultstring = "''".join(resultstring.split("'"))
                            resulttemp = "'" + resultstring + "'"
                        else:
                            resulttemp = 'NULL'
                    elif result[i ] is None:
                        resulttemp = 'NULL'
                    else:
                        # print(type(result[i ]))
                        resulttemp = str(result[i ])

                    sql += str(field) + " = " + resulttemp + ','
                """
                for fieldname in self.formtoolwidget.TABLEFILTERFIELD.keys():
                    if fieldname in 
                if field in self.formtoolwidget.TABLEFILTERFIELD.keys():
                    value =  self.formtoolwidget.TABLEFILTERFIELD[field]
                    if isinstance(value, str):
                        value = "'" + value + "'"
                """
                sql = sql[:-1]  # remove last ,

                sql += " WHERE pk_" + str(tablename) + " = " + str(tablepk)
                self.formtoolwidget.dbase.query(sql)






        if False:
            self.dbasetable['layer'].startEditing()

            if self.windowdialog.interfacemode in [0, 1]:
                if self.linkuserwdg is not None:
                    for i, tablename in enumerate(self.linkuserwdg.keys()):
                        if debug: logging.getLogger("Lamia").debug('start : %s', tablename)
                        featpk = self.currentFeaturePK
                        fieldnames = self.linkuserwdg[tablename]['widgets'].keys()
                        if len(fieldnames) == 0:
                            continue
                        result = []
                        for fieldname in fieldnames:
                            fieldvaluetosave = self.getValueFromWidget(self.linkuserwdg[tablename]['widgets'][fieldname],
                                                                    tablename,
                                                                    fieldname)
                            if fieldvaluetosave is not None:
                                result.append(fieldvaluetosave)
                            else:
                                result.append(None)
                        #tablepk
                        sql = "SELECT pk_" + str(tablename).lower() + " FROM " + str(self.dbasetablename).lower() + "_qgis"
                        sql += "  WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
                        tablepk = self.dbase.query(sql)[0][0]

                        # update sql
                        sql = "UPDATE " + str(tablename).lower() + " SET "
                        for i, field in enumerate(fieldnames):
                            if isinstance(result[i], str) or isinstance(result[i], unicode) :
                                if result[i] != '':
                                    resultstring = result[i]
                                    if "'" in resultstring:
                                        resultstring = "''".join(resultstring.split("'"))
                                    resulttemp = "'" + resultstring + "'"
                                else:
                                    resulttemp = 'NULL'
                            elif result[i ] is None:
                                resulttemp = 'NULL'
                            else:
                                # print(type(result[i ]))
                                resulttemp = str(result[i ])

                            sql += str(field) + " = " + resulttemp + ','

                        sql = sql[:-1]  # remove last ,

                        sql += " WHERE pk_" + str(tablename) + " = " + str(tablepk)
                        self.dbase.query(sql)

                # lidchoosers
                for lidchooser in self.lamiawidgets:
                    lidchooser.saveProperties()



            if self.windowdialog.interfacemode == 2:
                if self.linkuserwdg is None:
                    templinkuserwgd = {self.dbasetablename: {'linkfield': 'ID','widgets': {}}}
                else:
                    templinkuserwgd = self.linkuserwdg

                listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]

                for i, tablename in enumerate(templinkuserwgd.keys()):
                    dbasetable = self.dbase.dbasetables[tablename]
                    result = []
                    for j, field in enumerate(dbasetable['fields'].keys()):
                        itemindex = listfieldname.index(tablename + '.' + field)
                        fieldvaluetosave = self.getValueFromWidget(self.tableWidget.cellWidget(itemindex, 1),
                                                                tablename,
                                                                field)
                        if fieldvaluetosave is not None:
                            result.append(fieldvaluetosave)
                        else:
                            result.append(None)

                    #tablepk
                    sql = "SELECT pk_" + str(tablename).lower() + " FROM " + str(self.dbasetablename).lower() + "_qgis"
                    sql += "  WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
                    tablepk = self.dbase.query(sql)[0][0]

                    # update sql
                    sql = "UPDATE " + str(tablename).lower() + " SET "
                    for i, field in enumerate(dbasetable['fields'].keys()):
                        if field[0:3] in ['pk_', 'id_'] or field[0:4] in ['lpk_']:
                            continue
                        if isinstance(result[i], str):
                            if result[i] != '':
                                resulttemp = "'" + result[i] + "'"
                            else:
                                resulttemp = 'NULL'
                        elif isinstance(result[i], unicode):
                            if result[i] != u'':
                                resulttemp = "'" + result[i] + "'"
                            else:
                                resulttemp = 'NULL'
                        elif result[i ] is None:
                            resulttemp = 'NULL'
                        else:
                            resulttemp = str(result[i])
                        sql += str(field) + " = " + resulttemp + ','

                    sql = sql[:-1]  # remove last ,
                    sql += " WHERE pk_" + str(tablename) + " = " + str(tablepk)
                    self.dbase.query(sql)

    def setValueInWidget(self, wdg, valuetoset, table, field):
        """
        Called by initFeatureProperties when iterating the fields

        :param wdg:         the widget to set a value to
        :param valuetoset:  the value
        :param table:       the table of the value
        :param field:       the field of the value
        """

        if isinstance(wdg, QTextEdit) or isinstance(wdg, QLineEdit):
            if valuetoset is not None:
                wdg.setText(valuetoset)
            else:
                wdg.setText('')
        elif isinstance(wdg, QSpinBox) or isinstance(wdg, QDoubleSpinBox):
            try:
                if valuetoset is not None:
                    wdg.setValue(valuetoset)
                else:
                    wdg.setValue(-1)
            except Exception as e:
                logging.getLogger("Lamia_unittest").debug('error %s %s %s %s', table,field , str(valuetoset), e)
        elif isinstance(wdg, QComboBox):
            try:
                if valuetoset is not None:
                    text = self.formtoolwidget.dbase.getConstraintTextFromRawValue(table, field, valuetoset)
                    index = wdg.findText(text)
                    wdg.setCurrentIndex(index)
                else:
                    wdg.setCurrentIndex(0)
            except Exception as e:
                    logging.getLogger("Lamia_unittest").debug('error %s %s %s',table,field ,  e)
        elif isinstance(wdg, QDateEdit):
            if valuetoset is not None:
                if isinstance(valuetoset, str) or isinstance(valuetoset, unicode):
                    wdg.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd'))

                elif isinstance(valuetoset, QtCore.QDate):
                    wdg.setDate(valuetoset)
            else:
                wdg.setSpecialValueText(" ")
                wdg.setDate(QtCore.QDate.fromString('0001-01-01', 'yyyy-MM-dd'))

        elif isinstance(wdg, QDateTimeEdit):
            if valuetoset is not None:
                if isinstance(valuetoset, str) or isinstance(valuetoset, unicode):
                    wdg.setDateTime(QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd hh:mm:ss'))

                elif isinstance(valuetoset, QtCore.QDate):
                    wdg.setDate(valuetoset)
                elif isinstance(valuetoset, datetime.datetime):
                    wdg.setDateTime(QtCore.QDateTime.fromString(str(valuetoset), 'yyyy-MM-dd hh:mm:ss'))
            else:
                wdg.setSpecialValueText(" ")
                wdg.setDate(QtCore.QDate.fromString('0001-01-01', 'yyyy-MM-dd'))

        elif isinstance(wdg, QCheckBox):
            if valuetoset is not None:
                if valuetoset:
                    wdg.setCheckState(2)
                else:
                    wdg.setCheckState(0)
            else:
                wdg.setCheckState(0)

        elif isinstance(wdg, QLabel):
            if valuetoset is not None:
                if 'Cst' in self.formtoolwidget.dbase.dbasetables[table]['fields'][field].keys():
                    wdg.setText(self.formtoolwidget.dbase.getConstraintTextFromRawValue(table, field, valuetoset))
                else:
                    wdg.setText(valuetoset)
            else:
                wdg.setText('')


    def getValueFromWidget(self, wdg, tablename, fieldname):
        """
        Method to obtain the savable value of a property widget

        :param wdg: the property widget
        :param tablename: the table name  linked with th widget
        :param fieldname: the field name  linked with th widget
        :return: The value of the widget, in good format for saving
        """

        fieldvaluetosave = None
        if ('Cst' in self.formtoolwidget.dbase.dbasetables[tablename]['fields'][fieldname].keys()
                and not isinstance(wdg, str)):
            try:
                if isinstance(wdg, list):
                    wdg = wdg[0]
                fieldvaluetosave = self.formtoolwidget.dbase.getConstraintRawValueFromText(tablename, fieldname, wdg.currentText())
            except Exception as e:
                print('error getValueFromWidget', tablename, fieldname, e)
            if fieldvaluetosave == '':
                fieldvaluetosave = None
        else:
            if isinstance(wdg, list):
                wdg = wdg[0]
            if isinstance(wdg, QSpinBox) and wdg.value() > -1:
                fieldvaluetosave = int(wdg.value() )
            elif isinstance(wdg, QDoubleSpinBox) and wdg.value() > -1:
                fieldvaluetosave = float(wdg.value())
            elif isinstance(wdg, QTextEdit) or isinstance(wdg, QTextBrowser):
                fieldvaluetosave = wdg.toPlainText()
            elif isinstance(wdg, QLineEdit):
                fieldvaluetosave = wdg.text()
            elif isinstance(wdg, QCheckBox) :
                value = wdg.checkState()
                if int(value):
                    fieldvaluetosave = 1
                else:
                    fieldvaluetosave = 0
            elif isinstance(wdg, QDateEdit) and wdg.findChild(QLineEdit).text() != ' ':
                fieldvaluetosave = wdg.date().toString('yyyy-MM-dd')
            elif isinstance(wdg, QDateTimeEdit) and wdg.findChild(QLineEdit).text() != ' ':
                fieldvaluetosave = wdg.dateTime().toString( 'yyyy-MM-dd hh:mm:ss')
            elif isinstance(wdg, str):
                fieldvaluetosave = wdg

        return fieldvaluetosave


    def saveRessourceFile(self,featurepk=None):
        """
        Called by saveFeature
        If ressource file is not in the dbase directory, save it in the dbase directory

        """
        # get date
        """
        sql = "SELECT datetimecreation FROM " + self.dbasetablename.lower() + "_qgis"
        sql += " WHERE pk_"+ self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
        query = self.dbase.query(sql)
        result = [row[0] for row in query]
        """
        if not 'Ressource' in self.formtoolwidget.dbase.getParentTable(self.formtoolwidget.DBASETABLENAME):
            return
            
        DBASETABLENAMElower = self.formtoolwidget.DBASETABLENAME.lower()
        result = self.formtoolwidget.dbase.getValuesFromPk(DBASETABLENAMElower + "_qgis",
                                                            'datetimecreation',
                                                            featurepk)

        if result is not None:
            datevalue = datetime.datetime.strptime(str(result), "%Y-%m-%d %H:%M:%S").date()
            if isinstance(datevalue, datetime.date):
                datevalue = datevalue.strftime('%Y-%m-%d')
        else:
            return

        date = ''.join(datevalue.split('-'))
        """
        sql = "SELECT pk_ressource, id_ressource, file FROM " + self.dbasetablename.lower() + "_qgis"
        sql += " WHERE pk_"+ self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
        query = self.dbase.query(sql)
        result = [row[0:3] for row in query]
        """
        result = self.formtoolwidget.dbase.getValuesFromPk(DBASETABLENAMElower + "_qgis",
                                                            ['pk_ressource', 'id_ressource', 'file'],
                                                            featurepk)
        if len(result) > 0:
            pkressource, idressource, file = result
        else:
            return

        dbaseressourcesdirectory = self.formtoolwidget.dbase.dbaseressourcesdirectory
        if file is not None and len(file) > 0:
            if file[0] == '.':
                file = os.path.join(dbaseressourcesdirectory,file)
            else:
                if os.path.isfile(file):
                    filename = os.path.basename(file)
                    filename = str(idressource) + '_' + filename
                    destinationdir = os.path.join(dbaseressourcesdirectory,self.formtoolwidget.DBASETABLENAME,date)
                    destinationfile = os.path.join(destinationdir, filename)

                    self.formtoolwidget.dbase.copyRessourceFile(fromfile= file,
                                                                tofile=destinationfile,
                                                                withthumbnail=0,
                                                                copywholedirforraster=False)


                    finalname = os.path.join('.',os.path.relpath(destinationfile, dbaseressourcesdirectory ))
                    sql = "UPDATE Ressource SET file = '" + finalname + "' WHERE pk_ressource = " +  str(pkressource) + ";"
                    query = self.formtoolwidget.dbase.query(sql)

                    #removing old file 
                    #if self.beforesavingFeature is not None:
                    if self.formtoolwidget.currentFeaturePK is not None:   #case updating existing feature
                        sql = "SELECT file FROM Ressource  WHERE pk_ressource = " + str(pkressource) + ";"
                        query = self.formtoolwidget.dbase.query(sql)
                        result = [row[0] for row in query]
                        oldfile = result[0]
                    else:
                        oldfile = ''

                    newfile = finalname

                    if os.path.isfile(self.formtoolwidget.dbase.completePathOfFile(oldfile)) and oldfile != newfile:
                        os.remove(self.formtoolwidget.dbase.completePathOfFile(oldfile))
                    else:
                        pass

    def _saveParentWidgetRelation(self,featurepk=None):

        debug = False
        if debug : self.formtoolwidget.dbase.printsql = True
        if self.formtoolwidget.currentFeaturePK == featurepk:   # relation is already saved
            return

        if hasattr(self.formtoolwidget, 'PARENTJOIN') and self.formtoolwidget.parentWidget is not None:
            parenttblname = self.formtoolwidget.parentWidget.DBASETABLENAME
            childtblname = self.formtoolwidget.DBASETABLENAME
            parentjoin = self.formtoolwidget.PARENTJOIN
            if parenttblname in self.formtoolwidget.PARENTJOIN.keys():
                joindict = self.formtoolwidget.PARENTJOIN[parenttblname]
                if joindict['tctable'] is None:
                    parentcolval = self.formtoolwidget.dbase.getValuesFromPk(parenttblname + '_qgis',
                                                                             joindict['colparent'],
                                                                             self.formtoolwidget.parentWidget.currentFeaturePK)
                    childparenttables = [childtblname] + self.formtoolwidget.dbase.getParentTable(childtblname)
                    for tablename in childparenttables:
                        dbasetable = self.formtoolwidget.dbase.dbasetables[tablename]
                        if joindict['colthistable'] in dbasetable['fields'].keys():
                            pktable = self.formtoolwidget.dbase.getValuesFromPk(tablename + '_qgis',
                                                                             'pk_' + tablename.lower(),
                                                                             featurepk)
                            sql = "UPDATE {} SET {} = {} WHERE pk_{} = {}".format(tablename,
                                                                                   joindict['colthistable'],
                                                                                    parentcolval,
                                                                                    tablename.lower(),
                                                                                    pktable)
                            self.formtoolwidget.dbase.query(sql)
                            break
                    
                else:
                    fieldtcthis = self.formtoolwidget.dbase.getValuesFromPk(childtblname + '_qgis',
                                                                             joindict['colthistable'],
                                                                             featurepk)
                    fieldtcparent = self.formtoolwidget.dbase.getValuesFromPk(parenttblname + '_qgis',
                                                                             joindict['colparent'],
                                                                             self.formtoolwidget.parentWidget.currentFeaturePK)
                    sql = "INSERT INTO {}(lpk_revision_begin,{},{}) "\
                          "VALUES({},{},{})".format(joindict['tctable'],
                                                     joindict['tctablecolparent'],
                                                     joindict['tctablecolthistable'],
                                                     self.formtoolwidget.dbase.maxrevision,
                                                     fieldtcparent,
                                                     fieldtcthis)
                    self.formtoolwidget.dbase.query(sql)
        if debug : self.formtoolwidget.dbase.printsql = False
        #self.dbase.commit()

    def saveTABLEFILTERFIELD(self, featurepk=None):
        if len(self.formtoolwidget.TABLEFILTERFIELD) > 0:
            parenttables = [self.formtoolwidget.DBASETABLENAME]
            parenttables += self.formtoolwidget.dbase.getParentTable(self.formtoolwidget.DBASETABLENAME)
            for tablename in parenttables:
                fields = self.formtoolwidget.dbase.dbasetables[tablename]['fields']
                tablepk = self.formtoolwidget.dbase.getValuesFromPk(self.formtoolwidget.DBASETABLENAME + '_qgis',
                                                    'pk_' + tablename.lower(),
                                                        featurepk)
                for fieldname, fieldvalue in self.formtoolwidget.TABLEFILTERFIELD.items():
                    if fieldname in fields:
                        if isinstance(fieldvalue, str):
                            fieldvalue = "'" + fieldvalue + "'"
                        sql = "UPDATE {} SET {} = {} WHERE pk_{} = {}".format(tablename,
                                                                               fieldname,
                                                                                fieldvalue,
                                                                                tablename.lower(),
                                                                                tablepk)
                        self.formtoolwidget.dbase.query(sql)


    def _reinitAfterSaving(self):
        #reinit
        layergeomtype = self.formtoolwidget.mainifacewidget.qgiscanvas.layers[self.formtoolwidget.DBASETABLENAME]['layer'].geometryType()
        self.formtoolwidget.mainifacewidget.qgiscanvas.createorresetRubberband(layergeomtype)
        self.formtoolwidget.tempgeometry = None
        self.formtoolwidget.mainifacewidget.qgiscanvas.layers[self.formtoolwidget.DBASETABLENAME]['layerqgis'].repaintRequested.emit()
        # self.mainifacewidget.qgiscanvas.canvas.refresh()

    def ___________________actionsOnDeletingFeature(self):
        pass

    def deleteFeature(self):

        tablestodel = [self.formtoolwidget.DBASETABLENAME]
        tablestodel += self.formtoolwidget.dbase.getParentTable(self.formtoolwidget.DBASETABLENAME)
        pkfields = ['pk_' + tablename.lower() for tablename in tablestodel]

        for tablename in tablestodel:
            pkvalues = self.formtoolwidget.dbase.getValuesFromPk(self.formtoolwidget.DBASETABLENAME + '_qgis',
                                                                pkfields,
                                                                self.formtoolwidget.currentFeaturePK)
        dictdelete=dict(zip(tablestodel, pkvalues))       # dict : {tablename : pkvalue}
        for tablename, pkvalue in dictdelete.items():
            sql = "DELETE FROM {} WHERE pk_{} = {}".format(tablename,
                                                            tablename.lower(),
                                                            str(pkvalue))
            self.formtoolwidget.dbase.query(sql)
        self.formtoolwidget.postDeleteFeature()



    def archiveFeature(self):
        pkobjet = self.formtoolwidget.dbase.getValuesFromPk(self.formtoolwidget.DBASETABLENAME + '_qgis',
                                                                'pk_objet',
                                                                self.formtoolwidget.currentFeaturePK)
        # idobjet = self.currentFeature['id_objet']
        #datesuppr = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sql = "UPDATE Objet SET datetimedestruction = '" + datesuppr + "'  WHERE pk_objet = " + str(pkobjet) + ";"
        self.formtoolwidget.dbase.query(sql)


    def ___________________utilsFunctions(self):
        pass

    def getQgsGeomFromPk(self,pk):
        wkt = self.formtoolwidget.dbase.getWktGeomFromPk(self.formtoolwidget.DBASETABLENAME, pk)
        geom = qgis.core.QgsGeometry.fromWkt(wkt)
        return geom

    if False:
        def initFeatureProperties(self, feat, inputtablename=None, fieldname=None, value=None):
            """
            Called by featureSelected
            Fill the fields in the widget

            :param feat: the selected  QgsFeature - if None it s a new feature
            :param inputtablename:  To init a specific table with specific field and a specific value
            :param fieldname:  specific field
            :param value:  specific value
            :return:
            """

            
            if feat is not None and feat.id() == 0:
                return

            if self.dbasetable is not None:
                if self.linkuserwdg is None:
                    templinkuserwgd = {self.dbasetablename: None}
                else:
                    templinkuserwgd = self.linkuserwdg

                if inputtablename is None:
                    tablestoiterate = self.dicttablefieldtoinit.keys()
                else:
                    tablestoiterate = [inputtablename]

                #Then get values
                for tablename in tablestoiterate:
                    dbasetable = self.dbase.dbasetables[tablename]
                    if len(self.dicttablefieldtoinit[tablename]) == 0 :
                        continue
                    if feat is not None:
                        if fieldname is None:
                            fieldstoiterate = self.dicttablefieldtoinit[tablename]
                        else:
                            fieldstoiterate = [fieldname]
                        sql = "SELECT " + ','.join(fieldstoiterate) + " FROM " + self.dbasetablename + "_qgis "
                        sql += " WHERE pk_" + self.dbasetablename.lower() + " = " + str(feat.id())
                        result = self.dbase.query(sql)[0]

                    else:
                        if fieldname is None:
                            fieldstoiterate = self.dicttablefieldtoinit[tablename]
                        else:
                            fieldstoiterate = [fieldname]

                    for i, field in enumerate(fieldstoiterate):
                        # raw table
                        if feat is not None and value is None:
                            valuetoset = result[i]
                        else:
                            valuetoset = value

                        if self.dbase.utils.isAttributeNull(valuetoset):
                            valuetoset = None

                        if self.windowdialog.interfacemode in [0, 1]:
                            if (tablename in templinkuserwgd.keys()
                                    and templinkuserwgd[tablename] is not None
                                    and 'widgets' in templinkuserwgd[tablename].keys()
                                    and field in  templinkuserwgd[tablename]['widgets'].keys()):
                                if isinstance(templinkuserwgd[tablename]['widgets'][field], list):
                                    self.setValueInWidget(templinkuserwgd[tablename]['widgets'][field][0], valuetoset, tablename, field)
                                else:
                                    self.setValueInWidget(templinkuserwgd[tablename]['widgets'][field], valuetoset, tablename,field)

                        if self.windowdialog.interfacemode == 2 :
                            listfieldname = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
                            itemindex = listfieldname.index(tablename + '.' + field)

                            if self.tableWidget.cellWidget(itemindex, 1) is not None:
                                self.setValueInWidget(self.tableWidget.cellWidget(itemindex, 1), valuetoset, tablename, field)
                            else:
                                if self.tableWidget.item(itemindex, 1) is not None:
                                    if valuetoset is None:
                                        self.tableWidget.item(itemindex, 1).setText('')
                                    else:
                                        self.tableWidget.item(itemindex, 1).setText(str(valuetoset))

            #lidchoosers
            for lidchooser in self.lamiawidgets:
                lidchooser.initProperties()

            # current prestation case:
            self.pushButton_savefeature.setEnabled(True)

            if feat is not None and self.linkagespec is not None and 'Marche' in self.linkagespec.keys()  and self.dbase.currentprestationid is not None:
                # search table with lk prestation
                if int(str(self.dbase.qgisversion_int)[0:3]) < 218:
                    isspatial = self.dbasetable['layerqgis'].geometryType() < 3
                else:
                    isspatial = self.dbasetable['layerqgis'].isSpatial()
                if isspatial:
                    # if self.dbasetable['layerview'].isSpatial():
                    # lk_presta = self.dbasetable['layerview'].getFeatures(qgis.core.QgsFeatureRequest(feat.id())).next()['lk_marche']
                    lk_presta = self.dbase.getLayerFeatureById(self.dbasetablename, feat.id())['lk_marche']
                else:
                    listfeat = list(self.dbasetable['layerqgis'].getFeatures())
                    featid = [fet.id() for fet in listfeat]
                    index = featid.index(feat.id())
                    lk_presta = listfeat[index]['lk_marche']

                if lk_presta != self.dbase.currentprestationid:
                    self.pushButton_savefeature.setEnabled(False)


