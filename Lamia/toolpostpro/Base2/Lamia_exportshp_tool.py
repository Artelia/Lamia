# -*- coding: utf-8 -*-

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






import qgis
import os
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import sys, glob, inspect, logging, textwrap

try:
    from qgis.PyQt.QtGui import (QAction, QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QAction, QWidget)

from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
from ...lamiautils.abstractfilemanager import AbstractFileManager


class ExportShapefileTool(AbstractLamiaTool):

    TOOLNAME = 'exporttools'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(ExportShapefileTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)


    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Import/export'
        self.NAME = 'Export shp'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)

        self.iconpath = os.path.join(os.path.dirname(__file__), 'Lamia_exportshp_tool_icon.png')
        #self.qtreewidgetfields = ['libelle']

        # ****************************************************************************************
        # properties ui
        self.groupBox_elements.setParent(None)
        self.frame_editing.setParent(None)

        self.filemanager = ExportShpfileManager(self.windowdialog, self, '.txt')




        self.qfiledlg = self.windowdialog.qfiledlg

        self.confdatamain = os.path.join(os.path.dirname(inspect.getsourcefile(self.__class__)), self.TOOLNAME)
        self.confdataproject = os.path.join(self.dbase.dbaseressourcesdirectory, 'config',self.TOOLNAME)


    def initFieldUI(self):
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            self.userwdgfield.toolButton_filechooser.clicked.connect(self.chooseFile)

            self.userwdgfield.pushButton_export.clicked.connect(self.prepareData)

            self.userwdgfield.groupBox_filemanager.layout().addWidget(self.filemanager)



    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(self,
                                                   'InspectionDigue nouveau',
                                                   '',
                                                   'Shapefile (*.shp)')
        if reportfile:
            if isinstance(reportfile, tuple):    # qt5
                reportfile = reportfile[0]
            self.userwdgfield.lineEdit_nom.setText(reportfile)

    """
    def postInit(self):
        self.pathbpu = os.path.join(os.path.dirname(__file__), 'costtool', 'bordereau.csv')
    """

    def postOnActivation(self):
        #self.createfilesdir = os.path.join(os.path.dirname(__file__), 'exporttools')
        self.filemanager.reset()
        if False:
            self.userwdgfield.comboBox_type.clear()
            for workdir in [self.confdatamain, self.confdataproject]:
                for filename in glob.glob(os.path.join(workdir, '*.txt')):
                    basename = os.path.basename(filename).split('.')[0]
                    if basename != 'README':
                        #self.exportshapefiledialog.comboBox_type.addItems([basename])
                        if workdir == self.confdataproject:
                            basename = '*' + basename
                        self.userwdgfield.comboBox_type.addItems([basename])




    def prepareData(self):
        # print('prepareData', tabletype, shpfile)
        debug = False

        shpfile = self.userwdgfield.lineEdit_nom.text()


        #tabletype = self.userwdgfield.comboBox_type.currentText()
        tabletype = self.filemanager.getCurrentText()
        tabletypepath = self.filemanager.getCurrentPath()

        if False:
            if tabletype[0] == '*':
                tabletype = tabletype[1:]
                self.createfilesdir = self.confdataproject
            else:
                tabletype = tabletype
                self.createfilesdir = self.confdatamain



        self.pdffile = shpfile
        self.champs = self.readChamp(tabletypepath)


        self.fieldsforshp = self.buildQgsFields(self.champs)
        sql = self.buildSql(self.champs)
        if debug: logging.getLogger('Lamia').debug('sql %s', sql)



        query = self.dbase.query(sql)

        self.result = [list(row) for row in query]

        if debug: logging.getLogger('Lamia').debug('result %s', str(self.result))

        self.postprepareData(tabletype)

        if debug: logging.getLogger('Lamia').debug('result post : %s', str(self.result))

        if sys.version_info.major == 2:
            geomtype = qgis.core.QGis.WKBNoGeometry
        elif sys.version_info.major == 3:
            geomtype = qgis.core.QgsWkbTypes.NoGeometry

        for table in self.champs:
            if 'main' == table['table']:
                champmain = table['sql']


        for table in self.champs:
            if 'geom' in table['table']:
                sqlgeom = table['fields']['geom']['value']
                if 'ST_AsText(' in sqlgeom :
                    geomval = sqlgeom.split('ST_AsText(')[1][:-1]
                    print(geomval)
                else :
                    geomval = 'geom'

                #sql = 'SELECT ST_GeometryType(St_MakeValid(geom)) ' + champmain
                try:
                    sql = ' SELECT ST_GeometryType(St_MakeValid(' + geomval + ')) ' + champmain
                    sql = self.dbase.updateQueryTableNow(sql)
                    res = self.dbase.query(sql)[0][0]
                except TypeError:
                    sql = ' SELECT ST_GeometryType(' + geomval + ') ' + champmain
                    sql = self.dbase.updateQueryTableNow(sql)
                    res = self.dbase.query(sql)[0][0]
                # print('res',res)
                if sys.version_info.major == 2:
                    if res == 'LINESTRING':
                        geomtype = qgis.core.QGis.WKBLineString
                    elif res == 'POINT':
                        geomtype = qgis.core.QGis.WKBPoint
                elif sys.version_info.major == 3:
                    if res == 'LINESTRING':
                        geomtype = qgis.core.QgsWkbTypes.LineString
                    elif res == 'POINT':
                        geomtype = qgis.core.QgsWkbTypes.Point




        self.fillShapefile(shpfile,
                           geomtype,
                           self.fieldsforshp,
                           self.champs,
                           self.result)


    def readChamp(self,table):
        """

        :param table:
        :return: list : [           {'table' : tablename,
                                    {'sql' : lien sql
                                     {'fields' : ordereddic{... {fieldname : {type,
                                                                                cst,
                                                                                value}
                                                    ...]
        """

        debug = False

        #champs = OrderedDict()
        champs = []

        #filename = os.path.join(os.path.dirname(__file__), 'exporttools', table + '.txt')
        #self.createfilesdir = os.path.join(os.path.dirname(__file__), 'exporttools')
        #for filename in glob.glob(os.path.join(self.createfilesdir, '*.txt')):
        # print(self.createfilesdir, table + '.txt')
        # filename = os.path.join(self.createfilesdir, table + '.txt')
        filename = table

        if sys.version_info.major == 2:
            file = open(filename, 'r')
        elif sys.version_info.major == 3:
            file = open(filename, 'r',encoding="utf-8")
            #file = open(filename, 'rb')
        compt = 0
        actualtable = None
        for line in file:
            if len(line.strip()) == 0:
                continue


            if line[0:3] == '###':          # new field
                line = line[3:].strip()
                #linesplit = line.split(';')
                #fieldname = linesplit[0].strip()
                if debug: logging.getLogger("Lamia").debug('fieldname %s', line)
                actualtable = line
                #champs.append(actualtable)
                #champs[-1] =
                champs.append({})
                champs[-1]['table'] = actualtable
                champs[-1]['sql'] = None
                champs[-1]['fields'] = OrderedDict()

            elif line[0:2] == '##':         # parent field constraint name
                #self.dbasetables[tablename]['fields'][fieldname]['ParFldCst'] = line[2:].strip()
                #champs[actualtable]['sql'] = line[2:].strip()
                champs[-1]['sql'] = [ssline.strip() for ssline in line[2:].split(';')]

            elif line[0] == '#':            # comment - pass
                continue

            else:                           # field constraint
                if actualtable not in ['main','with']:
                    linesplit = line.split(';')


                    champs[-1]['fields'][linesplit[0].strip()] = {}

                    if linesplit[1].strip() != '':
                        champs[-1]['fields'][linesplit[0].strip()]['type'] = linesplit[1].strip()
                    else:
                        champs[-1]['fields'][linesplit[0].strip()]['type'] = None
                    if linesplit[2].strip() != '':
                        champs[-1]['fields'][linesplit[0].strip()]['cst'] = linesplit[2].strip()
                    else:
                        champs[-1]['fields'][linesplit[0].strip()]['cst'] = None
                    if linesplit[3].strip() != '':
                        champs[-1]['fields'][linesplit[0].strip()]['value'] = linesplit[3].strip()
                    else:
                        champs[-1]['fields'][linesplit[0].strip()]['value'] = None

                    if len(linesplit) == 5 and linesplit[4].strip() != '':
                        champs[-1]['fields'][linesplit[0].strip()]['as'] = linesplit[4].strip()
                    else:
                        champs[-1]['fields'][linesplit[0].strip()]['as'] = None


                else:
                    champs[-1]['sql'] = line.strip()

            compt += 1




        file.close()

        return champs




    def buildSql(self,champs):

        debug = False

        sql = ''


        for i, table in enumerate(champs):
            #if table != 'geom' and table != 'main' :
            if table['table']  in [ 'with']:
                sql += champs['with']


        sql += ' SELECT '

        #for table in champs.keys():
        for table in champs:
            if table['table'] not in ['main','with']:
                for i, name in enumerate(table['fields'].keys()):
                    attr = table['fields'][name]
                    if attr['value'] is None:
                        sql += 'NULL, '
                    else:
                        if table['sql'] is None:
                            sql += attr['value'] + ', '
                        else:
                            sql += "( SELECT "
                            sql += attr['value'] + ' '
                            sql += table['sql'][0]
                            #sql += " AND "
                            #sql += self.dbase.dateVersionConstraintSQL()
                            if False:
                                sql += ' AND  Objet.datecreation <= ' + "'" + self.dbase.workingdate + "'"
                                if self.dbase.dbasetype == 'postgis':
                                    sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                                    sql += 'THEN Objet.datedestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
                                elif self.dbase.dbasetype == 'spatialite':
                                    sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                                    sql += 'THEN Objet.datedestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END '
                            if len(table['sql'])>1:
                                sql += ' ' + table['sql'][1]
                            sql += '), '
                    if table['fields'][name]['as'] is not None :
                        sql = sql[:-2] + " AS " + table['fields'][name]['as'] + ", "


        sql = sql[:-2]

        #sql += ' FROM ' + champs.keys()[0]
        #sql +=  ' ' + champs['main']
        for i, table in enumerate(champs):
            #if table != 'geom' and table != 'main' :
            if table['table']  in [ 'main']:
                sql += ' ' + table['sql']
                champmain = table

        if debug: logging.getLogger("Lamia").debug('sql before now : %s ', sql)

        sql = self.dbase.updateQueryTableNow(sql)

        if debug : logging.getLogger("Lamia").debug('sql after  now : %s ',sql )


        # export by zonegeo
        boundinggeom = None
        if len(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()) >= 1:
            fetids = []
            currentfeats = self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()
            for fet in currentfeats:
                fetids.append(str(fet.id()))
            #print(currentfeat['id_zonegeo'])
            #fetid = currentfeat.id()
            # fetid = 21
            if False:
                sqltemp = "SELECT ST_AsText(ST_MakeValid(Zonegeo.geom)) FROM Zonegeo WHERE pk_zonegeo = " + str(fetid)
                query = self.dbase.query(sqltemp)
                result = [row[0] for row in query][0]
                boundinggeom = result

            if 'WHERE' in champmain['sql']:
                sql += " AND pk_zonegeo IN (" + ','.join(fetids) + ")"
            else:
                sql += " WHERE pk_zonegeo IN (" + ','.join(fetids) + ")"



        return sql



    def buildQgsFields(self, champs):
        fields = qgis.core.QgsFields()
        for i, table in enumerate(champs):
            #if table != 'geom' and table != 'main' :
            if table['table'] not in ['geom', 'main', 'with']:
                #print(i, champs[i])
                for j, name in enumerate(table['fields'].keys()):
                    if name in [field.name() for field in fields]:
                        self.windowdialog.errorMessage("ATTENTION Champ " + name + " deja utilise")

                    typefield = eval('QtCore.QVariant.' + table['fields'][name]['type'])
                    fields.append(qgis.core.QgsField(name, typefield))


        return fields



    def postprepareData(self,tabletype):
        pass


    def fillShapefile(self, filename, typegeom, fields, champs, result):

        debug = False

        if sys.version_info.major == 2:
            writer = qgis.core.QgsVectorFileWriter(filename,
                                                   'UTF-8',
                                                    fields,
                                                    typegeom,
                                                    # qgis.core.QGis.WKBPoint,
                                                    # qgis.core.QGis.WKBLineString,
                                                    self.dbase.qgiscrs)
        elif sys.version_info.major == 3:
            writer = qgis.core.QgsVectorFileWriter(filename,
                                                   'utf-8',
                                                    fields,
                                                    typegeom,
                                                    # qgis.core.QGis.WKBPoint,
                                                    # qgis.core.QGis.WKBLineString,
                                                    self.dbase.qgiscrs,
                                                   driverName="ESRI Shapefile")


        # print('*************')
        # print(len(fields.toList()))

        for row in result:
            if debug: logging.getLogger('Lamia').debug('res %s', str(row))
            feat = qgis.core.QgsFeature(fields)
            #qgis.core.QgsWkbTypes.NoGeometry
            if sys.version_info.major == 2:
                if typegeom != qgis.core.QGis.WKBNoGeometry :
                    if row[-1] is not None:
                        feat.setGeometry(qgis.core.QgsGeometry.fromWkt(row[-1]))
                        #print(row[10], feat.geometry())
                    else:
                        continue
            elif sys.version_info.major == 3:
                if typegeom != qgis.core.QgsWkbTypes.NoGeometry :
                    if row[-1] is not None:
                        feat.setGeometry(qgis.core.QgsGeometry.fromWkt(row[-1]))
                        #print(row[10], feat.geometry())
                    else:
                        continue
            # print(feat.geometry().exportToWkt())
            #feat.setAttributes(row)



            compteur = -1
            #for table in champs.keys():

            for table in champs:
                #if table != 'geom' and table != 'main' and 'postpro' not in table :
                if table['table'] not in['geom', 'main', 'with' ] and 'postpro' not in table['table']:
                    for i, name in enumerate(table['fields'].keys()):

                        compteur += 1
                        #print(row)
                        #print(table)
                        #print(compteur, table, champs[table]['fields'][name]['cst'], row[compteur])
                        if table['fields'][name]['cst'] is not None:
                            feat[compteur] = self.dbase.getConstraintTextFromRawValue(table['table'],
                                                                               table['fields'][name]['cst'],
                                                                               row[compteur])

                        else:
                            feat[compteur] = row[compteur]
                elif 'postpro' in table['table']  :

                    compteur += 1
                    feat[compteur] = row[compteur]

            if debug: logging.getLogger('Lamia').debug('fet %s -  %s', str(feat.id()), str(feat.attributes()))
            success = writer.addFeature(feat)

        del writer

        self.windowdialog.normalMessage('Export termine')



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_exportshp_tool.ui')
        uic.loadUi(uipath, self)


class ExportShpfileManager(AbstractFileManager):

    def __init__(self,  mainwindows=None, parentwdg=None, fileext=None):
        super(ExportShpfileManager, self).__init__(mainwindows, parentwdg, fileext)


    def new(self):

        if not os.path.exists(self.confdataproject):
            os.mkdir(self.confdataproject)

        if sys.version_info.major == 2:
            confpath, confext = self.qfiledialog.getSaveFileName(None, 'Choose the file', self.confdataproject,
                                                                     'txt (*.txt)', '')
        elif sys.version_info.major == 3:
            confpath , confext= self.qfiledialog.getSaveFileName(None, 'Choose the file', self.confdataproject,
                                                                     'txt (*.txt)', '')

        if confpath:
            conf_file = open(confpath, 'w', encoding="utf-8")
            conftxt =   """
                        # les lignes de commentaires commencent par #
                        
                        # la requete sql créée est formée ainsi :
                        #   SELECT [enumération des valeursql]
                        #   FROM [requete ecrite dans le ###main]
                        
                        # Le choix des champs à selectionner pour l'export se fait ainsi :
                        # ex :
                        # ###Noeud 
                        # #nom              ;type (Int, Double, String);  cst (nom du champ pour convertion trigamme); valeursql                    
                        # id_noeud;          Int;                      ;               id_noeud
                        
                        # avec :
                        # ###Noeud : nom de la table utilisée par convertir les trigrammes vers valeur texte
                        # nom : le nom du champ dans le shp
                        # type : le type dans le shp  : Int, Double, String
                        # champ de convertion : le nom du champ pour la convertion du trigramme vers du texte
                        # valeursql : la valeur (en sql) à prendre : peut etre un champ de la table, ou une requete sql
                        
                        # Pour choisir la géométrie considérée pour le shp 
                        # ###geom
                        # geom;         Int;               ;                  ST_AsText(Noeud_now.geom)
                        
                        # Enfin décrirer la requete FROM ..
                        # ###main 
                        # FROM Noeud_now
                        
                        # ici la requete utilisée pour la création du shp est 
                        # SELECT id_noeud FROM Noeud_now 
                        
                        # ex :

                        ###Noeud 
                        #nom              ;type     ;champ de convertion trigramme ? ; valeursql
                        id_noeud         ; Int      ;                                ; id_noeud
                        
                        ###geom
                        geom;         Int;               ;                  ST_AsText(Noeud_now.geom)
                        
                        ###main 
                        FROM Noeud_now
                        """
            conf_file.write(textwrap.dedent(conftxt))
            conf_file.close()

            self.reset()
            txttofind = self.projectcharacter + os.path.splitext(os.path.basename(confpath))[0]
            indexcombo = self.comboBox_files.findText(txttofind)
            self.comboBox_files.setCurrentIndex(indexcombo)

