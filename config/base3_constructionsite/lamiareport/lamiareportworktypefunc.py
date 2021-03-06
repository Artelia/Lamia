import os
import qgis, qgis.core
from Lamia.api.libslamia.constructionsitesubobservation.cssubobservationparser import (
    SubObservationParser,
)


def tableau_synth_sousfiches(self):

    atlasfeat = self.currentatlasfeat
    resfortable = []
    subobservationparser = SubObservationParser("orange")

    fieldsnames = ["Type fiche", "n°", "critère", "Commentaire"]

    # First get infos
    mainobsid = atlasfeat["id_observation"]
    sql = (
        " SELECT pk_observation, observationcategory FROM observation_now WHERE lid_observation = "
        + str(mainobsid)
    )
    sql = self.dbase.updateQueryTableNow(sql)
    resmainsql = self.dbase.query(sql)
    # print('**', resmainsql)
    if resmainsql is not None and len(resmainsql) > 0:
        # get sousobs widget
        # print(self.dbase.dbasetables['Desordre']['widget'])  propertieswdgOBSERVATION
        # sousobsdict = self.dbase.dbasetables['deficiency']['widget'][0].propertieswdgOBSERVATION.sousficheWidget.sousfichesdict
        # sousobsdict = self.mainifacewidget.toolwidgets['toolprepro']['deficiency'].propertieswdgOBSERVATIONNCA.sousficheWidget.sousfichesdict
        sousobsdict = subobservationparser.createDictionnary()
        dictfiche = None

        for pkobs, typefiche in resmainsql:
            resforcurrenttable = []

            # search fichedict

            if typefiche not in sousobsdict.keys():
                return ""
            else:
                dictfiche = sousobsdict[typefiche]
                typefichenom = typefiche + " " + dictfiche["name"]

            # for elem in sousobsdict.keys():
            #     if elem.split(' ')[0] == typefiche:
            #         typefichenom = elem
            #         dictfiche = sousobsdict[elem]
            #         break
            # if dictfiche is None:
            #     return ""

            usefullfichelist = []
            for datakey in dictfiche["datas"].keys():
                if dictfiche["datas"][datakey]["description"] is not None:
                    usefullfichelist.append(dictfiche["datas"][datakey])

            lentypefiche = len(usefullfichelist)
            # preparesql

            sql = (
                "SELECT "
                + ", ".join(["item_type_" + str(i) for i in range(1, lentypefiche + 1)])
                + " FROM Observation "
            )
            sql += " WHERE pk_observation = " + str(pkobs)
            res = self.dbase.query(sql)
            # print('**', res)
            for i, sousresult in enumerate(res[0]):
                if (
                    sousresult == 0
                    or dictfiche["datas"][list(dictfiche["datas"].keys())[i]]["type"]
                    is not None
                ):
                    typefichenom = typefichenom
                    typefichenumber = typefiche + "." + str(i + 1)
                    # print('**', i)
                    # print(dictfiche[i-1])
                    # typefichedescription = dictfiche[i][1]
                    typefichedescription = usefullfichelist[i]["description"]
                    # print(typefichedescription)
                    sqltemp = (
                        "SELECT item_obs_"
                        + str(i + 1)
                        + " FROM observation WHERE pk_observation = "
                        + str(pkobs)
                    )
                    restemp = self.dbase.query(sqltemp)[0][0]
                    typefichecommentaire = restemp

                    resforcurrenttable.append(
                        [
                            typefichenom,
                            typefichenumber,
                            typefichedescription,
                            typefichecommentaire,
                        ]
                    )

            if len(resforcurrenttable) == 0:
                resforcurrenttable = [[typefichenom, "/", "Aucune non conformité", ""]]

            resfortable += resforcurrenttable

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
             """

    html += """
                    <body>
                        <table>
                          <col width="130">
                          <col width="80">
            """

    # titre des colonnes
    html += """
           <thead> <!-- En-tête du tableau -->
               <tr>
           """
    for fieldname in fieldsnames:
        html += "<th>" + fieldname + "</th>"

    html += """
               </tr>
           </thead>
            """

    # lignes
    html += """
             <tbody> <!-- Corps du tableau -->
             """

    for line in resfortable:
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

    html += """
            </table>
             </body>
             </html>
             """

    # print(html)

    return html
