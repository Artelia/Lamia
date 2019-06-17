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


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import qgis
import os
import logging

# from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal
import numpy as np
import glob
import math

#from .tools.Lamia_exportshpdialog import ExportShapefileDialog
from ..base2.Lamiabase_rapport import printPDFBaseWorker

#class exportShapefileWorker(AbstractWorker):


class printPDFAssainissementWorker(printPDFBaseWorker):


    def __init__(self, dbase=None, windowdialog=None, reporttype=None, pdffile=None):
        # AbstractWorker.__init__(self)

        super(printPDFAssainissementWorker, self).__init__(dbase, windowdialog)

    def postInit(self):
        """
        Appelé à la fin de l'init
        permet pour les classes filles de préciser le self.createfilesdir
        """
        self.createfilesdir = os.path.join(os.path.dirname(__file__), 'rapporttools')
        """
        for filename in glob.glob(os.path.join(self.createfilesdir, '*.txt')):
            basename = os.path.basename(filename).split('.')[0]
            #self.exportshapefiledialog.comboBox_type.addItems([basename])
            self.printrapportdialog.comboBox_type.addItems([basename])
        """

    def processImages(self,newComposition,atlas,atlasfeat):
        if True:
            #for imageitemname in reportdic['images'].keys():
            for imageitemname in self.atlasconfData['images'].keys():
                # get imageitem
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    imageitem = newComposition.getComposerItemById(imageitemname)
                else:
                    imageitem = newComposition.itemById(imageitemname)
                    # composeritem = newComposition.itemByUuid(compitemuuid)
                    #imageitem.__class__ = qgis.core.QgsLayoutItemPicture

                # print(imageitem, reportdic['images'][imageitemname])
                imagefile = None

                if os.path.isfile(self.atlasconfData['images'][imageitemname]):
                    imagefile = self.atlasconfData['images'][imageitemname]

                elif True and self.atlasconfData['images'][imageitemname] == 'profile':
                    #try:
                    imagefile = self.getImageFileOfProfile(atlas.currentGeometry(self.dbase.qgiscrs), imageitem)
                    #except Exception as e:
                    #    print(e)

                elif True and self.atlasconfData['images'][imageitemname] == 'profiltravers':
                    # imagefile = self.getImageFileOfProfileTravers(reportdic, currentfeature, imageitem)
                    imagefile = self.getImageFileOfProfileTravers(atlasfeat, imageitem)


                elif 'photo' in self.atlasconfData['images'][imageitemname]:
                    table = self.atlasconfData['images'][imageitemname].split('.')[0]
                    photoid = int(self.atlasconfData['images'][imageitemname].split('.')[1][5:])
                    imagefile = self.getNumberedPhoto(atlasfeat, table, photoid)

                elif 'ressource' in self.atlasconfData['images'][imageitemname]:
                    table = self.atlasconfData['images'][imageitemname].split('.')[0]
                    ressourcenum = int(self.atlasconfData['images'][imageitemname].split('.')[1][9:])
                    #imagefile = self.getPhoto(reportdic, currentfeature)
                    imagefile = self.getNumberedRessource(atlasfeat, table, ressourcenum)

                elif self.atlasconfData['images'][imageitemname] == 'logo':
                    imagefile = os.path.join(os.path.dirname(__file__), '..','..', 'DBASE', 'rapport', 'utils', 'logo.jpg')

                elif self.atlasconfData['images'][imageitemname] == 'schema_noeud':
                    htmltotal = self.getHtmlForSchemaNoeud(atlasfeat)

                elif self.atlasconfData['images'][imageitemname] == 'tableau_infralin':
                    htmltotal = self.getHtmlForInfralinConnected(atlasfeat)


                # print('imageitem', imageitem.__class__, type(imageitem), isinstance(imageitem, qgis.core.QgsComposerFrame))

                if imageitem is not None:
                    # print('ok',imagefile )
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        if isinstance(imageitem, qgis.core.QgsComposerPicture):
                            imageitem.setPicturePath(imagefile)
                            imageitem.updateItem()
                        elif isinstance(imageitem, qgis.core.QgsComposerFrame):
                            # print(htmltotal)
                            imageitem.multiFrame().setContentMode(1)
                            imageitem.multiFrame().setHtml(htmltotal)
                            imageitem.multiFrame().loadHtml()
                    else:
                        if isinstance(imageitem, qgis.core.QgsLayoutItemPicture):
                            imageitem.setPicturePath(imagefile)
                            imageitem.refreshPicture()
                        if isinstance(imageitem, qgis.core.QgsLayoutFrame):
                            imageitem.multiFrame().setContentMode(1)
                            imageitem.multiFrame().setHtml(htmltotal)
                            imageitem.multiFrame().loadHtml()


    def getHtmlForInfralinConnected(self, atlasfeat):
        #id diam materiau prof  natureeffluent commentaire
        iddessys = atlasfeat['id_descriptionsystem']
        fields = ['id_infralineaire', 'lid_descriptionsystem_2', 'Round(diametreNominal*1000)', 'profaval', 'materiau', 'typeReseau', 'commentaire']
        fieldsnames=['Identifiant', 'Regard amont <br> ou aval',      'diamètre',      'profondeur', 'materiau', 'Type de réseau', 'commentaire']

        tabfinal=[]
        sql = "SELECT  " + ','.join(fields)
        sql += " FROM Infralineaire_now WHERE lid_descriptionsystem_2 = " + str(iddessys)
        sql = self.dbase.updateQueryTableNow(sql)

        query = self.dbase.query(sql)
        for res in query:
            tabfinal.append([])
            for i, field in enumerate(fields):
                tabfinal[-1].append(self.dbase.getConstraintTextFromRawValue('Infralineaire',field,res[i]))
            if self.dbase.isAttributeNull(tabfinal[-1][fields.index('profaval')]) and not self.dbase.isAttributeNull(atlasfeat['profradierouvrage']):
                tabfinal[-1][fields.index('profaval')]  = atlasfeat['profradierouvrage']

            sql = "SELECT Noeud_now.Libelle FROM Noeud_now "
            sql += " INNER JOIN Infralineaire_now ON  Infralineaire_now.lid_descriptionsystem_1 = Noeud_now.id_descriptionsystem "
            sql += " WHERE Infralineaire_now.id_infralineaire = " + str(res[0])
            sql = self.dbase.updateQueryTableNow(sql)
            result = self.dbase.query(sql)
            if result is not None:
                libelle = result[0][0]
                if self.dbase.isAttributeNull(libelle):
                    tabfinal[-1][1] = '?'
                else:
                    tabfinal[-1][1] = libelle
            else:
                tabfinal[-1][1] = '?'

        fields = ['id_infralineaire', 'lid_descriptionsystem_2', 'Round(diametreNominal*1000)', 'profamont', 'materiau', 'typeReseau', 'commentaire']

        sql = "SELECT  " + ','.join(fields)
        sql += " FROM Infralineaire_now WHERE lid_descriptionsystem_1 = " + str(iddessys)
        sql = self.dbase.updateQueryTableNow(sql)

        query = self.dbase.query(sql)
        for res in query:
            tabfinal.append([])
            for i, field in enumerate(fields):
                tabfinal[-1].append(self.dbase.getConstraintTextFromRawValue('Infralineaire',field,res[i]))
            if self.dbase.isAttributeNull(tabfinal[-1][fields.index('profamont')]) and not self.dbase.isAttributeNull(atlasfeat['profradierouvrage']):
                tabfinal[-1][fields.index('profamont')] = atlasfeat['profradierouvrage']

            sql = "SELECT Noeud_now.Libelle FROM Noeud_now "
            sql += " INNER JOIN Infralineaire_now ON  Infralineaire_now.lid_descriptionsystem_2 = Noeud_now.id_descriptionsystem "
            sql += " WHERE Infralineaire_now.id_infralineaire = " + str(res[0])
            sql = self.dbase.updateQueryTableNow(sql)
            result = self.dbase.query(sql)
            if result is not None:
                libelle = result[0][0]
                if self.dbase.isAttributeNull(libelle):
                    tabfinal[-1][1] = '?'
                else:
                    tabfinal[-1][1] = libelle
            else:
                tabfinal[-1][1] = '?'


        # diamtre to integer
        for res in tabfinal:
            if isinstance(res[2], float):
                res[2] = int(res[2])


        # Mise en page
        html = """
                <!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset="utf-8" />
                             <meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1"> 
                            <title>Titre</title>   
                            <style>
                                table
                                {
                                 width: 100%;
                                    border-collapse: collapse;
                                }
                                th:nth-child(1){
                                     width:50px;
                                }
                                td, th /* Mettre une bordure sur les td ET les th */
                                {
                                    border: 1px solid black;
                                font-family: Arial,  Times, serif;
                                }
                                
                                th
                                {
                                font-family: Arial;
                                font-size : 12pt;
                                }

                                td
                                {
                                font-family: Arial;
                                font-size : 10pt;
                                }
                                
                            </style>
                        </head>
                    <body>
                """

        html += """
                <body>
                    <table>
               """


        # titre des colonnes
        html += """
               <thead> <!-- En-tête du tableau -->
                   <tr>
               """
        for fieldname in fieldsnames :
            html += "<th>" + fieldname + "</th>"

        html += """
                   </tr>
               </thead>
                """
        #lignes
        html += """
                <tbody> <!-- Corps du tableau -->
                """

        for line in tabfinal:
            html += """
                    <tr>
                    """
            for res in line:
                html += "<td>" + str(res) + "</td>"

            html += """
                    </tr>
                    """
        html += """
                </tbody>
                """


        # Fin
        html += """
                        </table>
                    </body>
                </html>
                """


        return html




    def getHtmlForSchemaNoeud(self,  atlasfeat):

        debug = False

        if debug : logging.getLogger("Lamia").debug('started')
        # result : [ ..[id troncon, angle]...]
        resultlinesout=[]
        resultlinesin = []
        initialangle = 0

        iddessys = atlasfeat['id_descriptionsystem']


        sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire_now "
        sql +=  "WHERE lid_descriptionsystem_1 = " + str(iddessys)
        sql = self.dbase.updateQueryTableNow(sql)

        res = self.dbase.query(sql)
        compt = -1
        for pk, id in res:  #amont
            compt += 1
            fetinfra = self.dbase.getLayerFeatureByPk('Infralineaire', pk)
            fetgeom = qgis.core.QgsGeometry(fetinfra.geometry())
            data = np.array([list(elem) for elem in fetgeom.asPolyline()])

            lastlinepoly = self.uniqueSortedDatas(data)
            # print(data)
            # print(lastlinepoly)
            lastlinevector = lastlinepoly[1] - lastlinepoly[0]
            #print('lastlinevector',lastlinevector)
            angle = self.py_ang(lastlinevector, np.array([1, 0]))

            if compt == 0:
                initialangle = angle
            resultlinesout.append([id, angle - initialangle])

        sql = "SELECT pk_infralineaire, id_infralineaire FROM Infralineaire WHERE lid_descriptionsystem_2 = "
        sql += str(iddessys)
        res = self.dbase.query(sql)
        for pk, id in res:  #aval
            fetinfra = self.dbase.getLayerFeatureByPk('Infralineaire', pk)
            fetgeom = qgis.core.QgsGeometry(fetinfra.geometry())
            #lastlinepoly = np.array(fetgeom.asPolyline()[:-2])
            #lastlinepoly = np.unique(np.array(fetgeom.asPolyline()), axis=0)
            data = np.array([list(elem) for elem in fetgeom.asPolyline()])
            if False:
                # Perform lex sort and get sorted data
                sorted_idx = np.lexsort(data.T)
                sorted_data = data[sorted_idx, :]
                # Get unique row mask
                row_mask = np.append([True], np.any(np.diff(sorted_data, axis=0), 1))
                # Get unique rows
                lastlinepoly = sorted_data[row_mask]
            lastlinepoly = self.uniqueSortedDatas(data)
            # print(data)
            # print(lastlinepoly)
            lastlinevector = lastlinepoly[-2] - lastlinepoly[-1]
            # print('lastlinevector', lastlinevector)
            angle = self.py_ang(lastlinevector, np.array([1, 0]))
            resultlinesin.append([id, angle - initialangle])


        if debug: logging.getLogger("Lamia").debug('resultlinesout : %s', str(resultlinesout))
        if debug: logging.getLogger("Lamia").debug('resultlinesin : %s', str(resultlinesin))




        html = """
                <!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset="utf-8" />
                            <title>Titre</title>   
                            <style>
                    
                            </style>
                            </head>
                    
                        <body>
                """


        html += """
                <svg width="200px" height="200px" viewBox="0 0 200 200">
                  <!-- center of rotation -->
                  <circle cx="100" cy="100" r="30" stroke="black" stroke-width="2" fill="none"/>
                  <rect id="def-rect" width="200" height="200" x="0" y="0" stroke="black" stroke-width="2" fill="none"/>
               """

        html += """
                <defs>
                  <g id="arrowout"  style="stroke: black;">
                    <line x1="150" y1="100" x2="180" y2="100"/>
                    <polygon points="185 100, 180 95, 180 105"/>
                  </g>
                  <g id="arrowint"  style="stroke: black;">
                    <line x1="150" y1="100" x2="180" y2="100"/>
                    <polygon points="145 100, 150 95, 150 105"/>
                  </g>
                  <text id="textdf" x="100" y="100" font-size="8" >I love SVG!</text>
                  </defs>
        """

        for id, angle in resultlinesout:
            html += '<use xlink:href="#arrowout"  '
            html += ' transform= "rotate(' + str(-angle) +',100,100 ) "'
            html += ' stroke= "black"/> '

            translatex = math.cos(-angle/180*math.pi) * 90
            translatey = math.sin(-angle / 180 * math.pi) * 90
            html += '<text  x="100" y="100" transform="translate(' + str(translatex) + ', ' + str(translatey) + ')" '
            html += 'style="text-anchor: middle" dy="6px" font-size="12px" >' + str(id) + '</text>'

        for id, angle in resultlinesin:
            html += '<use xlink:href="#arrowint"  '
            html += ' transform= "rotate(' + str(-angle) +',100,100 ) "'
            html += ' stroke= "black"/> '

            translatex = math.cos(-angle/180*math.pi) * 90
            translatey = math.sin(-angle / 180 * math.pi) * 90
            html += '<text  x="100" y="100" transform="translate(' + str(translatex) + ', ' + str(translatey) + ')" '
            html += 'style="text-anchor: middle" dy="6px" font-size="12px" >' + str(id) + '</text>'

        html +=  """
                 </svg>
                 </body>
                 </html>
                 """

        return html
        
    def uniqueSortedDatas(self, datas):
        result=[]

        for data in datas:
            if not list(data) in result:
                result.append(list(data))
        return np.array(result)



    def py_ang(self, v1, v2):
        """ Returns the angle in radians between vectors 'v1' and 'v2'    """
        ang1 = np.arctan2(*v1[::-1])
        ang2 = np.arctan2(*v2[::-1])
        return np.rad2deg((ang1 - ang2) % (2 * np.pi))


