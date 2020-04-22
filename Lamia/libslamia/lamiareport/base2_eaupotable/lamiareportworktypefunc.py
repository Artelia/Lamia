import os
import qgis, qgis.core


def tableau_organeregard(self):
    atlasfeat = self.currentatlasfeat

    # id diam materiau prof  natureeffluent commentaire
    iddessys = atlasfeat['id_descriptionsystem']
    fields = ['id_equipement', 'categorie', 'ss_type_equipement', 'nature_reseau']
    fieldsnames = ['Identifiant', 'Type', 'Sous-type', 'Réseau']



    tabfinal = []
    sql = "SELECT  " + ','.join(fields)
    sql += " FROM Equipement_now WHERE lid_descriptionsystem_1 = " + str(iddessys)
    sql = self.dbase.updateQueryTableNow(sql)

    query = self.dbase.query(sql)
    for res in query:
        tabfinal.append([])
        for i, field in enumerate(fields):
            tabfinal[-1].append(self.dbase.getConstraintTextFromRawValue('Equipement', field, res[i]))



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
            if sys.version_info.major == 2:
                if isinstance(res,unicode):
                    html += "<td>" + res + "</td>"
                else:
                    html += "<td>" + str(res) + "</td>"
            elif sys.version_info.major == 3:
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
