import os, math
import numpy as np
import qgis, qgis.core



def tableau_infralin(self):
    atlasfeat = self.currentatlasfeat

    # id diam materiau prof  natureeffluent commentaire
    iddessys = atlasfeat['id_descriptionsystem']
    # fields = ['id_infralineaire', 'lid_descriptionsystem_2', 'Round(diametreNominal*1000)', 'profaval', 'materiau',
    #           'typeReseau', 'commentaire']
    fields = ['id_edge', 'lid_descriptionsystem_2', 'Round(nominaldiameter*1000)', 'depthdown', 'material',
              'networktype', 'comment']

    fieldsnames = ['Identifiant', 'Regard amont <br> ou aval', 'diamètre', 'profondeur', 'materiau',
                   'Type de réseau', 'commentaire']

    tabfinal = []
    sql = "SELECT  " + ','.join(fields)
    sql += " FROM edge_now WHERE lid_descriptionsystem_2 = " + str(iddessys)
    sql = self.dbase.updateQueryTableNow(sql)

    query = self.dbase.query(sql)
    for res in query:
        tabfinal.append([])
        for i, field in enumerate(fields):
            tabfinal[-1].append(self.dbase.getConstraintTextFromRawValue('edge', field, res[i]))
        if self.dbase.utils.isAttributeNull(tabfinal[-1][fields.index('depthdown')]) and not self.dbase.utils.isAttributeNull(
                atlasfeat['depthinvert']):
            tabfinal[-1][fields.index('depthdown')] = atlasfeat['depthinvert']

        sql = "SELECT node_now.name FROM node_now "
        sql += " INNER JOIN edge_now ON  edge_now.lid_descriptionsystem_1 = node_now.id_descriptionsystem "
        sql += " WHERE edge_now.id_edge = " + str(res[0])
        sql = self.dbase.updateQueryTableNow(sql)
        result = self.dbase.query(sql)

        if result is not None and len(result) > 0:
            libelle = result[0][0]
            if self.dbase.utils.isAttributeNull(libelle):
                tabfinal[-1][1] = '?'
            else:
                tabfinal[-1][1] = libelle
        else:
            tabfinal[-1][1] = '?'

    # fields = ['id_infralineaire', 'lid_descriptionsystem_2', 'Round(diametreNominal*1000)', 'profamont', 'materiau',
    #           'typeReseau', 'commentaire']
    fields = ['id_edge', 'lid_descriptionsystem_2', 'Round(nominaldiameter*1000)', 'depthup', 'material',
              'networktype', 'comment']


    sql = "SELECT  " + ','.join(fields)
    sql += " FROM edge_now WHERE lid_descriptionsystem_1 = " + str(iddessys)
    sql = self.dbase.updateQueryTableNow(sql)

    query = self.dbase.query(sql)
    for res in query:
        tabfinal.append([])
        for i, field in enumerate(fields):
            tabfinal[-1].append(self.dbase.getConstraintTextFromRawValue('edge', field, res[i]))
        if self.dbase.utils.isAttributeNull(tabfinal[-1][fields.index('depthup')]) and not self.dbase.utils.isAttributeNull(
                atlasfeat['depthinvert']):
            tabfinal[-1][fields.index('depthup')] = atlasfeat['depthinvert']

        sql = "SELECT node_now.name FROM node_now "
        sql += " INNER JOIN edge_now ON  edge_now.lid_descriptionsystem_2 = node_now.id_descriptionsystem "
        sql += " WHERE edge_now.id_edge = " + str(res[0])
        sql = self.dbase.updateQueryTableNow(sql)
        result = self.dbase.query(sql)
        if result is not None and len(result) > 0:
            libelle = result[0][0]
            if self.dbase.utils.isAttributeNull(libelle):
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
    for fieldname in fieldsnames:
        html += "<th>" + (fieldname) + "</th>"

    html += """
               </tr>
           </thead>
            """
    # lignes
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

def schema_node(self):

    debug = False
    atlasfeat = self.currentatlasfeat
    noeudorientenord = True

    if debug: logging.getLogger("Lamia").debug('started')
    # result : [ ..[id troncon, angle]...]
    resultlinesout = []
    resultlinesin = []
    initialangle = 0

    iddessys = atlasfeat['id_descriptionsystem']

    sql = "SELECT pk_edge, id_edge FROM edge_now "
    sql += "WHERE lid_descriptionsystem_1 = " + str(iddessys)
    sql = self.dbase.updateQueryTableNow(sql)

    res = self.dbase.query(sql)
    compt = -1
    for pk, id in res:  # amont
        compt += 1
        # fetinfra = self.dbase.getLayerFeatureByPk('edge', pk)
        # fetgeom = qgis.core.QgsGeometry(fetinfra.geometry())
        fetgeom = self.qgiscanvas.getQgsGeomFromPk(self.dbase, 'edge', pk)
        data = np.array([list(elem) for elem in fetgeom.asPolyline()])

        lastlinepoly = uniqueSortedDatas(data)
        # print(data)
        # print(lastlinepoly)
        if len(lastlinepoly) >= 2:
            lastlinevector = lastlinepoly[1] - lastlinepoly[0]
            # print('lastlinevector',lastlinevector)
            angle = py_ang(lastlinevector, np.array([1, 0]))

            if not noeudorientenord and compt == 0:
                initialangle = angle
            resultlinesout.append([id, angle - initialangle])
        else :
            self.errorMessage('schema error - pk infra : ' + str(fetinfra.id()) + ' - polyline trop courte...')

    sql = "SELECT pk_edge, id_edge FROM edge WHERE lid_descriptionsystem_2 = "
    sql += str(iddessys)
    res = self.dbase.query(sql)
    for pk, id in res:  # aval
        # fetinfra = self.dbase.getLayerFeatureByPk('edge', pk)
        # fetgeom = qgis.core.QgsGeometry(fetinfra.geometry())
        fetgeom = self.qgiscanvas.getQgsGeomFromPk(self.dbase, 'edge', pk)
        # lastlinepoly = np.array(fetgeom.asPolyline()[:-2])
        # lastlinepoly = np.unique(np.array(fetgeom.asPolyline()), axis=0)
        data = np.array([list(elem) for elem in fetgeom.asPolyline()])
        if False:
            # Perform lex sort and get sorted data
            sorted_idx = np.lexsort(data.T)
            sorted_data = data[sorted_idx, :]
            # Get unique row mask
            row_mask = np.append([True], np.any(np.diff(sorted_data, axis=0), 1))
            # Get unique rows
            lastlinepoly = sorted_data[row_mask]
        lastlinepoly = uniqueSortedDatas(data)
        # print(data)
        # print(lastlinepoly)
        if len(lastlinepoly)>=2:
            lastlinevector = lastlinepoly[-2] - lastlinepoly[-1]
            # print('lastlinevector', lastlinevector)
            angle = py_ang(lastlinevector, np.array([1, 0]))
            resultlinesin.append([id, angle - initialangle])
        else :
            self.errorMessage('schema error - pk infra : ' + str( fetinfra.id()) +  ' - polyline trop courte...')


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
        html += ' transform= "rotate(' + str(-angle) + ',100,100 ) "'
        html += ' stroke= "black"/> '

        translatex = math.cos(-angle / 180 * math.pi) * 90
        translatey = math.sin(-angle / 180 * math.pi) * 90
        html += '<text  x="100" y="100" transform="translate(' + str(translatex) + ', ' + str(translatey) + ')" '
        html += 'style="text-anchor: middle" dy="6px" font-size="12px" >' + str(id) + '</text>'

    for id, angle in resultlinesin:
        html += '<use xlink:href="#arrowint"  '
        html += ' transform= "rotate(' + str(-angle) + ',100,100 ) "'
        html += ' stroke= "black"/> '

        translatex = math.cos(-angle / 180 * math.pi) * 90
        translatey = math.sin(-angle / 180 * math.pi) * 90
        html += '<text  x="100" y="100" transform="translate(' + str(translatex) + ', ' + str(translatey) + ')" '
        html += 'style="text-anchor: middle" dy="6px" font-size="12px" >' + str(id) + '</text>'

    html += """
             </svg>
             </body>
             </html>
             """

    return html

def uniqueSortedDatas(datas):
    result = []

    for data in datas:
        if not list(data) in result:
            result.append(list(data))
    return np.array(result)

def py_ang(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'    """
    ang1 = np.arctan2(*v1[::-1])
    ang2 = np.arctan2(*v2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))