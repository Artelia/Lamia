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
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import numpy as np
import shutil
import io
import glob

from ..Base2.Lamia_exportshp_tool import ExportShapefileTool
from .Lamiadigue_rapport_tool import printPDFBaseWorker

# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class DigueExportShapefileTool(ExportShapefileTool):

    DBASES = ['digue','base_digue','base2_digue']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(DigueExportShapefileTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def postprepareData(self, tabletype):

        if tabletype == 'BM_Infralineaire':
            tempfield = []
            # donnees profil
            if False:
                tempfield.append(qgis.core.QgsField('Hauteur', QtCore.QVariant.Double))  # 0
                tempfield.append(qgis.core.QgsField('Larcrete', QtCore.QVariant.Double))
                # tempfield.append(qgis.core.QgsField('Larfranc', QtCore.QVariant.Double))
                tempfield.append(qgis.core.QgsField('typtater', QtCore.QVariant.String))
                tempfield.append(qgis.core.QgsField('typcrete', QtCore.QVariant.String))
                tempfield.append(qgis.core.QgsField('typtaeau', QtCore.QVariant.String))  # 5
                tempfield.append(qgis.core.QgsField('typauba', QtCore.QVariant.String))
                tempfield.append(qgis.core.QgsField('typberg', QtCore.QVariant.String))
                tempfield.append(qgis.core.QgsField('typpdber', QtCore.QVariant.String))
                # tempfield.append(qgis.core.QgsField('Desterre', QtCore.QVariant.String))
                # tempfield.append(qgis.core.QgsField('Descrete', QtCore.QVariant.String))         #10
                # tempfield.append(qgis.core.QgsField('Deseau', QtCore.QVariant.String))

                # self.fieldsforshp += tempfield
                # self.result[i][-1:-1] = [hauteurdigue, largcrete, typtater,typcrete,typtaeau,typeauba,typeberge,typepdberge,  Desterre, Descrete, Deseau  ]

                for i, field in enumerate(tempfield):
                    self.fieldsforshp.append(field)
                    if False:
                        self.champs['postpro' + str(i)] = None
                    # self.champs.append({})
                    self.champs.insert(-1, {})
                    self.champs[-2]['table'] = 'postpro' + str(i)
                    # champs += [[],[],[],[],[],[],[],[],[],[], []]
                # print('champs',champs)

                for i, row in enumerate(self.result):

                    hauteurdigue = None
                    largcrete = None
                    # largfrancbord = None
                    typtater = ''
                    typcrete = ''
                    typtaeau = ''
                    typeauba = ''
                    typeberge = ''
                    typepdberge = ''
                    # Desterre=''
                    # Descrete=''
                    # Deseau=''

                    sql = 'SELECT lid_ressource_4 FROM Infralineaire WHERE id_infralineaire = ' + str(row[0])
                    # print(sql)
                    query = self.dbase.query(sql)
                    # print('query',query)
                    lkprofil = query[0][0]

                    if lkprofil is not None:

                        sql = "SELECT pk_graphique, typegraphique FROM Graphique_qgis  WHERE id_ressource = " + str(
                            lkprofil)
                        query = self.dbase.query(sql)
                        resultrow = [row1 for row1 in query]
                        if len(resultrow) > 0 and resultrow[0][1] == 'PTR':
                            sql = "SELECT * FROM Graphiquedata WHERE lpk_graphique = " + str(resultrow[0][0])
                            sql += " ORDER BY id_graphiquedata"
                            query = self.dbase.query(sql)
                            resultrow2 = [list(row2[2:]) for row2 in query]
                            npresultrow = np.array(resultrow2)
                            # largeur crete
                            index = np.where(npresultrow[:, 5] == 'CRE')
                            largcrete = np.sum(npresultrow[:, 2][index])
                            # hauteur
                            minindexcrete = int(np.amin(index))
                            maxindexcrete = int(np.amax(index))
                            hauteurdigue = np.sum(npresultrow[0:minindexcrete, 3])

                            # francbord
                            """
                            index = np.where(npresultrow[:,5] == 'FRB')
                            largfrancbord = np.sum(npresultrow[:,2][index])
                            print(index,largfrancbord )
                            # print(hauteurdigue, largcrete, largfrancbord)
                            """
                            # description

                            listdescrtalusterre = ['dX;dZ;Partie;Type1;Type2']
                            listdescrcrete = ['dX;dZ;Partie;Type1;Type2']
                            listdescrtaluseau = ['dX;dZ;Partie;Type1;Type2']
                            for j, elem in enumerate(resultrow2):
                                # print(j,minindexcrete,maxindexcrete, self.dbase.getConstraintTextFromRawValue('Graphiquedata', 'index1', elem[5]),self.dbase.getConstraintTextFromRawValue('Graphiquedata', 'index3', elem[7]) )
                                if j < minindexcrete:
                                    # print('listdescrtalusterre')
                                    listdescrtalusterre += [';'.join([str(round(elem[2], 1)),
                                                                      str(round(elem[3], 1)),
                                                                      self.dbase.getConstraintTextFromRawValue(
                                                                          'Graphiquedata', 'index1', elem[5]),
                                                                      self.dbase.getConstraintTextFromRawValue(
                                                                          'Graphiquedata', 'index2', elem[6]),
                                                                      self.dbase.getConstraintTextFromRawValue(
                                                                          'Graphiquedata', 'index3', elem[7])])]
                                    if elem[5] in ['TAD', 'SOR', 'TAR']:
                                        if typtater == '':
                                            typtater = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                 self.dbase.getConstraintTextFromRawValue(
                                                                     'Graphiquedata', 'index3', elem[7])])
                                        else:
                                            typcurr = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                self.dbase.getConstraintTextFromRawValue(
                                                                    'Graphiquedata', 'index3', elem[7])])
                                            if typcurr != typtater:
                                                typtater = 'mixte'

                                elif j <= maxindexcrete and j >= minindexcrete:
                                    # print('listdescrcrete')
                                    listdescrcrete += [';'.join([str(round(elem[2], 1)),
                                                                 str(round(elem[3], 1)),
                                                                 self.dbase.getConstraintTextFromRawValue(
                                                                     'Graphiquedata', 'index1', elem[5]),
                                                                 self.dbase.getConstraintTextFromRawValue(
                                                                     'Graphiquedata', 'index2', elem[6]),
                                                                 self.dbase.getConstraintTextFromRawValue(
                                                                     'Graphiquedata', 'index3', elem[7])])]

                                    if typcrete == '':
                                        typcrete = ';'.join(
                                            [self.dbase.getConstraintTextFromRawValue('Graphiquedata', 'index2',
                                                                                      elem[6]),
                                             self.dbase.getConstraintTextFromRawValue('Graphiquedata', 'index3',
                                                                                      elem[7])])
                                    else:
                                        typcurr = ';'.join(
                                            [self.dbase.getConstraintTextFromRawValue('Graphiquedata', 'index2',
                                                                                      elem[6]),
                                             self.dbase.getConstraintTextFromRawValue('Graphiquedata', 'index3',
                                                                                      elem[7])])
                                        if typcurr != typcrete:
                                            typcrete = 'mixte'


                                elif j > maxindexcrete:
                                    # print('listdescrtaluseau')
                                    listdescrtaluseau += [';'.join([str(round(elem[2], 1)),
                                                                    str(round(elem[3], 1)),
                                                                    self.dbase.getConstraintTextFromRawValue(
                                                                        'Graphiquedata', 'index1', elem[5]),
                                                                    self.dbase.getConstraintTextFromRawValue(
                                                                        'Graphiquedata', 'index2', elem[6]),
                                                                    self.dbase.getConstraintTextFromRawValue(
                                                                        'Graphiquedata', 'index3', elem[7])])]

                                    if elem[5] in ['TAD', 'SOR', 'TAR']:
                                        if typtaeau == '':
                                            typtaeau = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                 self.dbase.getConstraintTextFromRawValue(
                                                                     'Graphiquedata', 'index3', elem[7])])
                                        else:
                                            typcurr = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                self.dbase.getConstraintTextFromRawValue(
                                                                    'Graphiquedata', 'index3', elem[7])])
                                            if typcurr != typtaeau:
                                                typtaeau = 'mixte'

                                    if elem[5] in ['FRB']:
                                        if typeauba == '':
                                            typeauba = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                 self.dbase.getConstraintTextFromRawValue(
                                                                     'Graphiquedata', 'index3', elem[7])])
                                        else:
                                            typcurr = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                self.dbase.getConstraintTextFromRawValue(
                                                                    'Graphiquedata', 'index3', elem[7])])
                                            if typcurr != typeauba:
                                                typeauba = 'mixte'

                                    if elem[5] in ['BER']:
                                        if typeberge == '':
                                            typeberge = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                  self.dbase.getConstraintTextFromRawValue(
                                                                      'Graphiquedata', 'index3', elem[7])])
                                        else:
                                            typcurr = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                self.dbase.getConstraintTextFromRawValue(
                                                                    'Graphiquedata', 'index3', elem[7])])
                                            if typcurr != typeberge:
                                                typeberge = 'mixte'

                                    if elem[5] in ['PDB']:
                                        if typepdberge == '':
                                            typepdberge = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                    self.dbase.getConstraintTextFromRawValue(
                                                                        'Graphiquedata', 'index3', elem[7])])
                                        else:
                                            typcurr = ';'.join([self.dbase.getConstraintTextFromRawValue(
                                                'Graphiquedata', 'index2', elem[6]),
                                                                self.dbase.getConstraintTextFromRawValue(
                                                                    'Graphiquedata', 'index3', elem[7])])
                                            if typcurr != typepdberge:
                                                typepdberge = 'mixte'

                            # description = '\n'.join(listdescr)
                            if False:
                                Desterre = '\n'.join(listdescrtalusterre)
                                Descrete = '\n'.join(listdescrcrete)
                                Deseau = '\n'.join(listdescrtaluseau)

                    self.result[i] = list(self.result[i])
                    self.result[i][-1:-1] = [hauteurdigue, largcrete, typtater, typcrete, typtaeau, typeauba, typeberge,
                                             typepdberge]

            # niveau protection surete
            if True:
                tempfield = []
                tempfield.append(qgis.core.QgsField('niv_pro_am', QtCore.QVariant.Double))
                tempfield.append(qgis.core.QgsField('niv_pro_av', QtCore.QVariant.Double))
                tempfield.append(qgis.core.QgsField('niv_sur_am', QtCore.QVariant.Double))
                tempfield.append(qgis.core.QgsField('niv_sur_av', QtCore.QVariant.Double))
                # champs += [[], [], [],[]]

                for i, field in enumerate(tempfield):
                    self.fieldsforshp.append(field)
                    # self.champs['postpro'+str(i)] = None
                    if False:
                        self.champs['postpro' + str(i)] = None
                    # self.champs.append({})
                    self.champs.insert(-1, {})
                    self.champs[-2]['table'] = 'postpro' + str(i)

                pathtool = None
                for i, tool in enumerate(self.windowdialog.tools):
                    if 'PathTool' in tool.__class__.__name__:
                        pathtool = self.windowdialog.tools[i]
                profiletraverstool = pathtool
                profiletraverstool.computeNXGraphForAll()

                for i, row in enumerate(self.result):
                    niv_pro_am = None
                    niv_pro_av = None
                    niv_sur_am = None
                    niv_sur_av = None

                    # currentgeom = self.currentFeature.geometry().asPolyline()
                    currentgeom = qgis.core.QgsGeometry.fromWkt(row[-1]).asPolyline()
                    profiletraverstool.computePath(list(currentgeom[0]), list(currentgeom[-1]))
                    datas = profiletraverstool.getGraphData()

                    for graphname in datas.keys():
                        if 'NIV' in graphname:
                            niv_pro_am = round(datas[graphname]['y'][0], 2)
                            niv_pro_av = round(datas[graphname]['y'][-1], 2)

                        if 'SUR' in graphname:
                            niv_sur_am = round(datas[graphname]['y'][0], 2)
                            niv_sur_av = round(datas[graphname]['y'][-1], 2)

                    # result[i] = list(result[i])[:-1] + [niv_pro_am, niv_pro_av, niv_sur_am, niv_sur_av] + list(result[i])[-1:]
                    # print([niv_pro_am, niv_pro_av, niv_sur_am, niv_sur_av])
                    # print(self.result[i][-1:-1])
                    self.result[i][-1:-1] = [niv_pro_am, niv_pro_av, niv_sur_am, niv_sur_av]

                profiletraverstool.rubberBand.reset(1)

            # export schema
            if True:
                # copy schema
                if False:
                    indexrapport = None

                    for i, menutool in enumerate(self.windowdialog.menutools):
                        if 'printPDFDigueWorker' in menutool.__class__.__name__:
                            indexrapport = i
                            break

                if False:
                    printer = None
                    for i, tool in enumerate(self.windowdialog.tools):
                        print(tool.__class__.__name__)
                        if 'printPDFBaseWorker' in tool.__class__.__name__:
                            print('ok')
                            printer = self.windowdialog.tools[i]
                            break
                printer = printPDFBaseWorker(dbase=self.dbase)
                exportrect = QtCore.QRect(0, 0, 200, 200)

                # create field
                tempfield = []
                tempfield.append(qgis.core.QgsField('schema', QtCore.QVariant.String))

                for i, field in enumerate(tempfield):
                    self.fieldsforshp.append(field)
                    self.champs.insert(-1, {})
                    self.champs[-2]['table'] = 'postpro' + str(i)

                if not os.path.exists(os.path.join(os.path.dirname(self.pdffile), 'schema')):
                    os.mkdir(os.path.join(os.path.dirname(self.pdffile), 'schema'))

                for i, row in enumerate(self.result):
                    #resfile = self.windowdialog.menutools[indexrapport].getImageFileOfProfileTravers(row[0], exportrect)
                    printer.currentatlasfeat = row[0]
                    printer.currentimageItem = QWidget()
                    printer.currentimageItem.setGeometry(exportrect)
                    resfile = printer.profiltravers()

                    if resfile is not None:
                        desfile = os.path.join(os.path.dirname(self.pdffile), 'schema',
                                               'schema_id' + str(row[0]) + '.png')
                        shutil.copyfile(resfile, desfile)

                        reldestfile = os.path.join('.', 'schema', 'schema_id' + str(row[0]) + '.png')
                        self.result[i][-1:-1] = [reldestfile]
                    else:
                        self.result[i][-1:-1] = [None]





