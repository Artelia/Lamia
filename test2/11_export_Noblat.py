# -*- coding: utf-8 -*-

import os
import sys
import qgis
import qgis.gui
import qgis.utils
import shutil
import pprint
from shutil import copyfile

from Lamia.Lamia.main.DBaseParser import DBaseParser

try:
    qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
except AttributeError:  # qgis 3
    qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT
# print(qgisversion_int)

if int(str(qgisversion_int)[0:3]) < 220:
    qgis_path = "C://OSGeo4W64//apps//qgis218"
    qgis_path = "C://Program Files//OSGeo4W64//apps//qgis-ltr"
else:
    qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
    # os.environ["QT_QPA_PLATFORM"] = "offscreen"

app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()


# sourcepath = "C://000_testdigue//0_caroline2//sqlitein"
# exportpath = 'C://000_testdigue//0_caroline2//res'

sourcepath = "M://FR//BOR//VT//URBAIN//4352240_87_NOBLAT_EtudeAEP_EU_EP//5_Etude//01_SIG//SIG ASS NOBLAT//NOBLAT SIG ASS ARTELIA//Sqlite a transformer"
exportpath = "M://FR//BOR//VT//URBAIN//4352240_87_NOBLAT_EtudeAEP_EU_EP//5_Etude//01_SIG//SIG ASS NOBLAT//NOBLAT SIG ASS ARTELIA//Shape final"
exportpath = "M://FR//BOR//VT//URBAIN//4352240_87_NOBLAT_EtudeAEP_EU_EP//5_Etude//01_SIG//SIG ASS NOBLAT//NOBLAT SIG ASS ARTELIA//shapefinal2"

def ExportOldLamiaNode(fileoldlamia):

    pathfrom = fileoldlamia
    dbaseparserfrom = DBaseParser(None)
    dbaseparserfrom.loadQgisVectorLayers(pathfrom)

    pathvlayer = 'C://000_testdigue//0_caroline2//fichiersource//REGARDS_ASS.shp'
    # pathvlayer = 'C://000_testdigue//0_caroline2//fichiersource//Regard GEOREF.shp'

    # [(0, 'ART_ID_ART'), (1, 'ART_NB_ARR'), (2, 'ART_PROF_A'), (3, 'ART_DEPOTS'), (4, 'ART_ACCESS'), (5, 'ART_OBSERV'), (6, 'ART_PHOTOS'), (7, 'ART_TRAVAU'), (8, 'ART_PRIORI'), (9, 'Topo_X'), (10, 'Topo_Y'), (11, 'ART_NB_BRT'), (12, 'COMMUNE'), (13, 'INSEE'), (14, 'DATEMAJ'), (15, 'SYSTCOLLEC'), (16, 'SOURCEMAJ'), (17, 'FE_CHUTE2'), (18, 'FE_CHUTE3'), (19, 'NB_ANO_REU'), (20, 'ART_PHOTO2'), (21, 'ANOM_EU1'), (22, 'ANOM_EU2'), (23, 'Topo_Z_TN'), (24, 'CHUTE_REU'), (25, 'FE_CHUTE1'), (26, 'Heure1_REU'), (27, 'Heure2_REU'), (28, 'Heure3_REU'), (29, 'PRO_FE_REU'), (30, 'ES_REU'), (31, 'Tete_REU'), (32, 'Sec_REU'), (33, 'Topo_Xp'), (34, 'Topo_Yp'), (35, 'Topo_Zp'), (36, 'TYP_POINTS'), (37, 'TYP_OUV_EP'), (38, 'PROF_BRT'), (39, 'REGARD_PE'), (40, 'REGARD_NV'), (41, 'COTE_TN'), (42, 'COTE_FE_BR'), (43, 'DEPOTS_BRT'), (44, 'ANOM_BRT1'), (45, 'ANOM_BRT2'), (46, 'ACCES_BRT'), (47, 'OBSERV_BRT'), (48, 'CLOISO_BRT'), (49, 'PRO_OUV_EP'), (50, 'COT_TN_OUV'), (51, 'COT_FE_OUV'), (52, 'DEPOTS_OUV'), (53, 'ANOM_OUV1'), (54, 'ANOM_OUV2'), (55, 'ACCES_OUV'), (56, 'OBSERV_OUV'), (57, 'TYP_OUV_SP'), (58, 'OBS_OUVSP'), (59, 'TYP_RESEAU')]


    # ['ART_ID_ART', 'ART_NB_ARR', 'ART_PROF_A', 'ART_DEPOTS', 'ART_ACCESS', 'ART_OBSERV', 'ART_PHOTOS', 'ART_TRAVAU', 'ART_PRIORI', 'Topo_X', 'Topo_Y', 'ART_NB_BRT', 'COMMUNE', 'INSEE', 'DATEMAJ', 'SYSTCOLLEC', 'SOURCEMAJ', 'FE_CHUTE2', 'FE_CHUTE3', 'NB_ANO_REU', 'ART_PHOTO2', 'ANOM_EU1', 'ANOM_EU2', 'Topo_Z_TN', 'CHUTE_REU', 'FE_CHUTE1', 'Heure1_REU', 'Heure2_REU', 'Heure3_REU', 'PRO_FE_REU', 'ES_REU', 'Tete_REU', 'Sec_REU', 'Topo_Xp', 'Topo_Yp', 'Topo_Zp', 'TYP_POINTS', 'TYP_OUV_EP', 'PROF_BRT', 'REGARD_PE', 'REGARD_NV', 'COTE_TN', 'COTE_FE_BR', 'DEPOTS_BRT', 'ANOM_BRT1', 'ANOM_BRT2', 'ACCES_BRT', 'OBSERV_BRT', 'CLOISO_BRT', 'PRO_OUV_EP', 'COT_TN_OUV', 'COT_FE_OUV', 'DEPOTS_OUV', 'ANOM_OUV1', 'ANOM_OUV2', 'ACCES_OUV', 'OBSERV_OUV', 'TYP_OUV_SP', 'OBS_OUVSP', 'TYP_RESEAU']

    # ['ART_ID_ART', 'ART_NB_ARR', 'ART_PROF_A',
    # 'ART_DEPOTS', 'ART_ACCESS',
    # 'ART_OBSERV', 'ART_PHOTOS',
    # 'ART_TRAVAU', 'ART_PRIORI',
    # 'Topo_X', 'Topo_Y',
    # 'ART_NB_BRT', 'COMMUNE', 'INSEE',
    # 'DATEMAJ',
    # 'SYSTCOLLEC', 'SOURCEMAJ',
    # 'FE_CHUTE2',
    # 'FE_CHUTE3',
    # 'NB_ANO_REU', 'ART_PHOTO2',
    # 'ANOM_EU1', 'ANOM_EU2',
    # 'Topo_Z_TN',
    # 'CHUTE_REU',
    # 'FE_CHUTE1', 'Heure1_REU', 'Heure2_REU', 'Heure3_REU',
    # 'PRO_FE_REU',
    # 'ES_REU',
    # 'Tete_REU',
    # 'Sec_REU',
    # 'Topo_Xp', 'Topo_Yp', 'Topo_Zp',
    # 'TYP_POINTS',
    # 'TYP_OUV_EP',
    # 'PROF_BRT',
    # 'REGARD_PE', 'REGARD_NV',
    # 'COTE_TN', 'COTE_FE_BR',
    # 'DEPOTS_BRT',
    # 'ANOM_BRT1', 'ANOM_BRT2',
    # 'ACCES_BRT',
    # 'OBSERV_BRT',
    # 'CLOISO_BRT',
    # 'PRO_OUV_EP',
    # 'COT_TN_OUV', 'COT_FE_OUV',
    # 'DEPOTS_OUV',
    # 'ANOM_OUV1', 'ANOM_OUV2',
    # 'ACCES_OUV', 'OBSERV_OUV',
    # 'TYP_OUV_SP', 'OBS_OUVSP', 'TYP_RESEAU']


    if True:
        sql = "SELECT Noeud_qgis.id_descriptionsystem, ST_AsText(Noeud_qgis.geom), "
        #       'ART_ID_ART',
        sql += "id_noeud,   "

        # 'ART_NB_ARR',
        if False:
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') THEN COUNT(id_infralineaire) END ,"
        if True:
            sql += """
                    CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') THEN
                    ( SELECT COUNT(temp1.id_infralineaire) FROM Infralineaire_qgis as temp1 
                    WHERE ST_Intersects(ST_EndPoint(temp1.geom), ST_Buffer(Noeud_qgis.geom,0.01) ))
                    END ,
                    """
        # 'ART_PROF_A'
        sql += " CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') THEN profradierouvrage END ,"
        #       'ART_DEPOTS',
        sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') AND Noeud_qgis.accessibilite IN ('OUV') THEN 
                    CASE WHEN depots = 0 THEN 'Aucun'
                    WHEN depots = 1 THEN 'Léger'
                    WHEN depots = 2 THEN 'Moyen' 
                    WHEN depots = 3 THEN 'Fort' 
                    ELSE 'Aucun' 
                     END
                 END,
        """

        #       'ART_ACCESS'
        sql += """
            CASE WHEN Noeud_qgis.typeOuvrageAss IN ('60','62') THEN 
                CASE WHEN accessibilite IN ('OUV') THEN 'ouvrable'
                WHEN accessibilite IN ('SVO')  THEN 'sous voirie' 
                WHEN accessibilite IN ('NVU')  THEN 'non vu'
                ELSE 'non ouvrable' 
                END
            END,
        """



        #       # 'ART_OBSERV',                  'ART_PHOTOS',
        sql += " CASE WHEN Noeud_qgis.typeOuvrageAss IN ('60','62') THEN  Observation_qgis.commentaires END, Ressource_qgis.numphoto , "
        #       # 'ART_TRAVAU', 'ART_PRIORI',
        sql += " 'Aucun' ,      NULL, "
        #       'Topo_X',                       'Topo_Y',
        sql += " round(ST_X(Noeud_qgis.geom),2), round(ST_Y(Noeud_qgis.geom),2), "
        #       'ART_NB_BRT',
        sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss IN ('60','62') THEN
                    (WITH temp1 AS (SELECT temp1.profaval FROM Infralineaire_qgis as temp1 WHERE temp1.lk_descriptionsystem2  = Noeud_qgis.id_descriptionsystem AND 
                    temp1.branchement = 1 )
                    SELECT COUNT(*) FROM temp1 )
                END,
                """

        # 'COMMUNE', 'INSEE',
        sql += " NULL,          NULL, "


        #           'DATEMAJ',
        sql += " CASE WHEN Observation_qgis.dateobservation IS NOT NULL THEN Observation_qgis.dateobservation  "
        sql += "ELSE ( WITH temp1 as ( SELECT * FROM Observation_qgis as temp2  WHERE   temp2.dateobservation IS NOT NULL )  SELECT MAX(temp1.dateobservation) FROM temp1 WHERE temp1.lk_desordre <= Desordre_qgis.id_desordre   )"
        sql += " END, "
        #       'SYSTCOLLEC', 'SOURCEMAJ',
        sql += "Zonegeo_qgis.libelle, 'ARTELIA',  "
        #       'FE_CHUTE2',  en fait prof
        sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') THEN 
                    (SELECT temp1.profaval FROM Infralineaire_qgis as temp1 WHERE temp1.profaval is NOT NULL AND temp1.lk_descriptionsystem2  = Noeud_qgis.id_descriptionsystem LIMIT 1 OFFSET 1)
                END,
                """
         #       'FE_CHUTE3', en fait prof
        sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') THEN 
                    (SELECT temp1.profaval FROM Infralineaire_qgis as temp1 WHERE  temp1.profaval is NOT NULL AND temp1.lk_descriptionsystem2  = Noeud_qgis.id_descriptionsystem LIMIT 1 OFFSET 2)
                END,
                """
        # 'NB_ANO_REU',
        sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') AND Noeud_qgis.accessibilite IN ('OUV') THEN 
                    ((CASE WHEN Observation_qgis.ECPPdepuisbranchement IS NULL THEN 0 ELSE 1 END)
                    + (CASE WHEN Observation_qgis.gcdegrade IS NULL THEN 0 ELSE 1 END)
                    + (CASE WHEN Observation_qgis.infiltration IS NULL THEN 0 ELSE 1 END)
                    + (CASE WHEN Observation_qgis.intrusionracine IS NULL THEN 0 ELSE 1 END)
                    + (CASE WHEN Observation_qgis.miseencharge IS NULL THEN 0 ELSE 1 END)
                    + (CASE WHEN Observation_qgis.tamponendommage IS NULL THEN 0 ELSE 1 END)) 
                END ,
                """

        # 'ART_PHOTO2',
        sql += " Ressource_qgis.file ,"

        #       # 'ANOM_EU1',
        sql += """
        CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') AND Noeud_qgis.accessibilite IN ('OUV') THEN 
            ( WITH temp1(test) AS 
            ( VALUES ( CASE WHEN Observation_qgis.ECPPdepuisbranchement IS NOT NULL THEN 'Eaux claires parasites' END), 
                    ( CASE WHEN Observation_qgis.gcdegrade IS NOT NULL THEN 'Génie civil dégradé' END), 
                    ( CASE WHEN Observation_qgis.infiltration IS NOT NULL THEN 'Infiltration' END), 
                    ( CASE WHEN Observation_qgis.intrusionracine IS NOT NULL THEN 'Intrusion racine' END), 
                    ( CASE WHEN Observation_qgis.miseencharge IS NOT NULL THEN 'Mise en charge' END), 
                    ( CASE WHEN Observation_qgis.tamponendommage IS NOT NULL THEN 'Tampon endommagé'  END))
            SELECT   test  FROM temp1 WHERE test is NOT NULL LIMIT 1 OFFSET 0 ) 
        END ,
        """
        #  'ANOM_EU2',
        sql += """
        CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') AND Noeud_qgis.accessibilite IN ('OUV') THEN 
            ( WITH temp1(test) AS 
            ( VALUES ( CASE WHEN Observation_qgis.ECPPdepuisbranchement IS NOT NULL THEN 'Eaux claires parasites' END), 
                    ( CASE WHEN Observation_qgis.gcdegrade IS NOT NULL THEN 'Génie civil dégradé' END), 
                    ( CASE WHEN Observation_qgis.infiltration IS NOT NULL THEN 'Infiltration' END), 
                    ( CASE WHEN Observation_qgis.intrusionracine IS NOT NULL THEN 'Intrusion racine' END), 
                    ( CASE WHEN Observation_qgis.miseencharge IS NOT NULL THEN 'Mise en charge' END), 
                    ( CASE WHEN Observation_qgis.tamponendommage IS NOT NULL THEN 'Tampon endommagé'  END))
            SELECT   test  FROM temp1 WHERE test is NOT NULL LIMIT 1 OFFSET 1 ) 
        END,
        
        """


        #       # 'Topo_Z_TN',
        sql += "Round(Noeud_qgis.Z,2) - 2.0,"

        #       'CHUTE_REU',
        sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') AND Noeud_qgis.accessibilite IN ('OUV')  THEN 
                    CASE WHEN (SELECT temp1.profaval FROM Infralineaire_qgis as temp1 WHERE  temp1.profaval is NOT NULL AND  temp1.lk_descriptionsystem2  = Noeud_qgis.id_descriptionsystem LIMIT 1 OFFSET 0)
                    IS NOT NULL THEN 'oui' 
                    ELSE (CASE WHEN Noeud_qgis.accessibilite = 'SVO' THEN NULL ELSE 'non'  END )
                    END 
                END,
                """
        #       'FE_CHUTE1', en fait prof
        sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') THEN 
                    (SELECT temp1.profaval FROM Infralineaire_qgis as temp1 WHERE  temp1.profaval is NOT NULL AND  temp1.lk_descriptionsystem2  = Noeud_qgis.id_descriptionsystem LIMIT 1 OFFSET 0)
                END,
                """
        #     Position horaire chute 1, 2 et 3
        sql += " NULL, NULL, NULL,  "
        # 'PRO_FE_REU',
        sql += "CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') THEN  Noeud_qgis.Z -2.0 - Noeud_qgis.profradierouvrage END,  "
        # 'ES_REU',
        sql += """ 
                CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') AND Noeud_qgis.accessibilite IN ('OUV') THEN 
                    CASE WHEN Observation_qgis.miseencharge IS NULL   THEN 'non' ELSE 'oui' END 
                END,
        """
        # 'Tete_REU',
        sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') AND Noeud_qgis.accessibilite IN ('OUV') THEN 
                    CASE WHEN (SELECT temp1.pk_infralineaire FROM Infralineaire_qgis as temp1 WHERE temp1.lk_descriptionsystem2  = Noeud_qgis.id_descriptionsystem) IS NULL THEN 'oui' ELSE 'non' 
                    END
                END,
                """
        # 'Sec_REU',
        sql += """ 
                CASE WHEN Noeud_qgis.typeOuvrageAss IN('60','62') AND Noeud_qgis.accessibilite IN ('OUV') THEN 
                    CASE WHEN Observation_qgis.ECPPdepuisbranchement IS NULL   THEN 'non' ELSE 'oui' END 
                END,
        """
        # 'Topo_Xp', 'Topo_Yp', 'Topo_Zp',
        sql += 'round(Noeud_qgis.dX,2),round(Noeud_qgis.dY,2), round(Noeud_qgis.dZ,2), '
        # # 'TYP_POINTS',
        sql += """
                CASE 
                WHEN Noeud_qgis.typeOuvrageAss = '60' THEN 'Regard'
                WHEN Noeud_qgis.typeOuvrageAss = '62' THEN 'Regard'
                WHEN Noeud_qgis.typeOuvrageAss = '61' THEN 'Branchement'
                WHEN Noeud_qgis.typeOuvrageAss in ('10','20','30','40') THEN 'Ouvrage spécial'
                 ELSE 'Ouvrage EP'
                 END ,
        """

        # # 'TYP_OUV_EP',
        sql += """
                CASE
                WHEN Noeud_qgis.typeOuvrageAss = '72' THEN 'Grille avaloir'
                WHEN Noeud_qgis.typeOuvrageAss = '71' THEN 'Grille'
                WHEN Noeud_qgis.typeOuvrageAss = '70' THEN 'Avaloir'
                WHEN Noeud_qgis.typeOuvrageAss = '10' THEN 'Poste de refoulement' 
                WHEN Noeud_qgis.typeOuvrageAss = '73' THEN 'Tête de buse'
                WHEN Noeud_qgis.typeOuvrageAss = '00' THEN 'Autre'
                 END ,
        
        """

        # 'PROF_BRT',
        sql += " CASE WHEN Noeud_qgis.typeOuvrageAss = '61' THEN Noeud_qgis.profradierouvrage END, "
        # 'REGARD_PE', 'REGARD_NV',
        sql += "NULL, CASE WHEN  Noeud_qgis.accessibilite = 'OUN' THEN 'oui' ELSE 'non' END, "
        # 'COTE_TN', 'COTE_FE_BR',
        sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss = '61' THEN
                    round(Noeud_qgis.Z,2) - 2.0 
                END,
                CASE WHEN Noeud_qgis.typeOuvrageAss = '61' THEN
                    round(Noeud_qgis.Z - Noeud_qgis.profradierouvrage - 2.0 ,2) 
                END,
                
            """

        # 'DEPOTS_BRT',
        sql += " CASE WHEN Noeud_qgis.typeOuvrageAss = '61' THEN "
        sql +=  "  (CASE WHEN depots = 0 THEN 'Aucun' "
        sql += " WHEN depots = 1 THEN 'Léger'  "
        sql += " WHEN depots = 2 THEN 'Moyen'  "
        sql += " WHEN depots = 3 THEN 'Fort'  "
        sql += " ELSE 'Aucun'  "
        sql += " END )"
        sql +=  " END, "

        # 'ANOM_BRT1', 'ANOM_BRT2',
        if True:
            sql += """
            CASE WHEN Noeud_qgis.typeOuvrageAss = '61' THEN 
                ( WITH temp1(test) AS 
                ( VALUES ( CASE WHEN Observation_qgis.ECPPdepuisbranchement IS NOT NULL THEN 'Eaux claires parasites' END), 
                        ( CASE WHEN Observation_qgis.gcdegrade IS NOT NULL THEN 'Génie civil dégradé' END), 
                        ( CASE WHEN Observation_qgis.infiltration IS NOT NULL THEN 'Infiltration' END), 
                        ( CASE WHEN Observation_qgis.intrusionracine IS NOT NULL THEN 'Intrusion racine' END), 
                        ( CASE WHEN Observation_qgis.miseencharge IS NOT NULL THEN 'Mise en charge' END), 
                        ( CASE WHEN Observation_qgis.tamponendommage IS NOT NULL THEN 'Tampon endommagé'  END))
                SELECT   test  FROM temp1 WHERE test is NOT NULL LIMIT 1 OFFSET 0 ) 
            END ,
    
            """

            sql += """
            CASE WHEN Noeud_qgis.typeOuvrageAss = '61' THEN 
                ( WITH temp1(test) AS 
                ( VALUES ( CASE WHEN Observation_qgis.ECPPdepuisbranchement IS NOT NULL THEN 'Eaux claires parasites' END), 
                        ( CASE WHEN Observation_qgis.gcdegrade IS NOT NULL THEN 'Génie civil dégradé' END), 
                        ( CASE WHEN Observation_qgis.infiltration IS NOT NULL THEN 'Infiltration' END), 
                        ( CASE WHEN Observation_qgis.intrusionracine IS NOT NULL THEN 'Intrusion racine' END), 
                        ( CASE WHEN Observation_qgis.miseencharge IS NOT NULL THEN 'Mise en charge' END), 
                        ( CASE WHEN Observation_qgis.tamponendommage IS NOT NULL THEN 'Tampon endommagé'  END))
                SELECT   test  FROM temp1 WHERE test is NOT NULL LIMIT 1 OFFSET 1 ) 
            END ,
        
            """


        # 'ACCES_BRT',
        if True:
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss = '61' THEN "
            sql += "(CASE WHEN Noeud_qgis.accessibilite = 'OUV' THEN 'ouvrable' ELSE 'non ouvrable' END)"
            sql += " END, "
            # 'OBSERV_BRT',
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss = '61' THEN Observation_qgis.commentaires  END,"
            # 'CLOISO_BRT',
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss = '61'  THEN "
            sql += " (CASE WHEN Noeud_qgis.cloisonsiphoide = 0 THEN 'non' ElSE 'oui' END) "
            sql += " END, "

            # 'PRO_OUV_EP'
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss NOT IN ('60', '61', '62', '40')  THEN "
            sql += " Noeud_qgis.profradierouvrage "
            sql += " END, "

            # 'COT_TN_OUV' en fait prof , 'COT_FE_OUV' en fait null,
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss NOT IN ('60', '61','62', '40')  THEN "
            sql += " Noeud_qgis.Z -2.0 "
            sql += " END, "
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss NOT IN ('60', '61','62', '40')  THEN "
            sql += " Noeud_qgis.Z - 2.0 - Noeud_qgis.profradierouvrage"
            sql += " END, "

        if True:
            # 'DEPOTS_OUV',
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss NOT IN ('60', '61','62', '40')  THEN "
            sql += "  (CASE WHEN depots = 0 THEN 'Aucun' "
            sql += " WHEN depots = 1 THEN 'Léger'  "
            sql += " WHEN depots = 2 THEN 'Moyen'  "
            sql += " WHEN depots = 3 THEN 'Fort'  "
            sql += " ELSE 'Aucun'  "
            sql += " END )"
            sql += " END, "
            # 'ANOM_OUV1', 'ANOM_OUV2',
            if True:
                sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss NOT IN ('60', '61','62', '40') THEN 
                    ( WITH temp1(test) AS 
                    ( VALUES ( CASE WHEN Observation_qgis.ECPPdepuisbranchement IS NOT NULL THEN 'Eaux claires parasites' END), 
                            ( CASE WHEN Observation_qgis.gcdegrade IS NOT NULL THEN 'Génie civil dégradé' END), 
                            ( CASE WHEN Observation_qgis.infiltration IS NOT NULL THEN 'Infiltration' END), 
                            ( CASE WHEN Observation_qgis.intrusionracine IS NOT NULL THEN 'Intrusion racine' END), 
                            ( CASE WHEN Observation_qgis.miseencharge IS NOT NULL THEN 'Mise en charge' END), 
                            ( CASE WHEN Observation_qgis.tamponendommage IS NOT NULL THEN 'Tampon endommagé'  END))
                    SELECT   test  FROM temp1 WHERE test is NOT NULL LIMIT 1 OFFSET 0 ) 
                END ,
    
                """

                sql += """
                CASE WHEN Noeud_qgis.typeOuvrageAss NOT IN ('60', '61','62', '40') THEN 
                    ( WITH temp1(test) AS 
                    ( VALUES ( CASE WHEN Observation_qgis.ECPPdepuisbranchement IS NOT NULL THEN 'Eaux claires parasites' END), 
                            ( CASE WHEN Observation_qgis.gcdegrade IS NOT NULL THEN 'Génie civil dégradé' END), 
                            ( CASE WHEN Observation_qgis.infiltration IS NOT NULL THEN 'Infiltration' END), 
                            ( CASE WHEN Observation_qgis.intrusionracine IS NOT NULL THEN 'Intrusion racine' END), 
                            ( CASE WHEN Observation_qgis.miseencharge IS NOT NULL THEN 'Mise en charge' END), 
                            ( CASE WHEN Observation_qgis.tamponendommage IS NOT NULL THEN 'Tampon endommagé'  END))
                    SELECT   test  FROM temp1 WHERE test is NOT NULL LIMIT 1 OFFSET 1 ) 
                END ,
    
                """


            # # 'ACCES_OUV',
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss NOT IN ('60', '61','62', '40')  THEN "
            sql += " (CASE WHEN  Noeud_qgis.accessibilite = 'OUV' THEN 'ouvrable' ELSE 'non ouvrable' END )  "
            sql += " END, "
            # 'OBSERV_OUV',
            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss NOT IN ('60', '61', '62','40')  THEN "
            sql += " Observation_qgis.commentaires  || (SELECT Objet.commentaire FROM Objet WHERE Objet.id_objet = Noeud_qgis.id_objet)"
            sql += " END, "

            # 'TYP_OUV_SP', 'OBS_OUVSP', 'TYP_RESEAU']
            sql += """ CASE WHEN Noeud_qgis.typeOuvrageAss IN (10,20,30,40)  THEN (
                            CASE WHEN Noeud_qgis.typeOuvrageAss = 10 THEN 'Poste de refoulement' 
                                 WHEN Noeud_qgis.typeOuvrageAss = 20 THEN "Station d'épuration" 
                                 WHEN Noeud_qgis.typeOuvrageAss = 30 THEN 'Bassin de stockage' 
                                 WHEN Noeud_qgis.typeOuvrageAss = 40 THEN 'Deversoir d orage' END )
                        END,
            """


            sql += " CASE WHEN Noeud_qgis.typeOuvrageAss IN (10,20,30,40) THEN "
            sql += " Observation_qgis.commentaires  ||  (SELECT Objet.commentaire FROM Objet WHERE Objet.id_objet = Noeud_qgis.id_objet)"
            sql += " END, "
            # 'TYP_RESEAU']
            sql += "CASE  "
            sql += " WHEN Noeud_qgis.typeReseau =  'PLU' THEN 'Eaux pluviales' "
            sql += " WHEN Noeud_qgis.typeReseau =  'USE' THEN 'Eaux usées' "
            sql += " WHEN Noeud_qgis.typeReseau =  'UNI' THEN 'Unitaire' "
            sql += " END "





        sql += " FROM Noeud_qgis , Zonegeo_qgis  "
        sql += " LEFT JOIN Infralineaire_qgis  ON Infralineaire_qgis.lk_descriptionsystem2  = Noeud_qgis.id_descriptionsystem"
        sql += " LEFT JOIN Desordre_qgis ON Desordre_qgis.lk_descriptionsystem = Noeud_qgis.id_descriptionsystem "
        sql += " LEFT JOIN Observation_qgis ON Observation_qgis.lk_desordre = Desordre_qgis.id_desordre "
        sql += " LEFT JOIN Tcobjetressource ON Noeud_qgis.id_objet = Tcobjetressource.id_tcobjet "
        sql += " LEFT JOIN Ressource_qgis ON Ressource_qgis.id_ressource = Tcobjetressource.id_tcressource "
        sql += " WHERE ST_WITHIN(Noeud_qgis.geom, Zonegeo_qgis.geom) "
        sql += ' GROUP BY Noeud_qgis.id_descriptionsystem'

        reschp01 = dbaseparserfrom.query(sql)

        pprint.pprint(reschp01[0:10])

    if True:
        fileraw, ext = os.path.splitext(pathvlayer)
        basename = os.path.basename(fileraw)
        sqlitebasename = os.path.basename(pathfrom).split('.')[0]



        fileto = os.path.join(os.path.normpath(exportpath), basename+'_' + sqlitebasename + '.shp')
        print(fileto)

    if True:

        for ext in ['.shp', '.dbf', '.qpj', '.prj', '.shx']:
            try:
                os.remove(os.path.join(exportpath, basename+'_' + sqlitebasename +ext))
            except :
                pass
            copyfile(fileraw + ext, os.path.join(exportpath, basename+'_' + sqlitebasename +ext))

    if True:

        #fileto = os.path.join('C://', '000_testdigue', '0_caroline2', 'res', 'REGARDS_ASS.shp')
        print(fileto)
        vlayerto = qgis.core.QgsVectorLayer(fileto, "toto", "ogr")
        print(vlayerto.isValid())
        vlayerto.startEditing()

        featurelist=[]
        for i, elem in enumerate(reschp01):
            feat = qgis.core.QgsFeature(vlayerto.fields())
            if i==0:
                print([(k, f.name()) for k, f in enumerate(feat.fields())])
                print([(k, type(elem[k])) for k, f in enumerate(feat.fields())])
            #geom
            geom = qgis.core.QgsGeometry.fromWkt(elem[1])
            feat.setGeometry(geom)
            featurelist.append(feat)

            for j, sselem in enumerate(elem[2:]):
                if False and isinstance(sselem, float):
                    sselem = float(round(sselem,2))
                feat[j] = sselem

        success = vlayerto.addFeatures(featurelist)
        print(success)

        vlayerto.commitChanges()


def ExportOldLamiaLine(fileoldlamia):

    pathfrom = fileoldlamia
    dbaseparserfrom = DBaseParser(None)
    dbaseparserfrom.loadQgisVectorLayers(pathfrom)

    pathvlayer = 'C://000_testdigue//0_caroline2//fichiersource//RESEAUX_ASS.shp'


    #[(0, 'TYP_RESEAU'), (1, 'TYP_ECOUL'), (2, 'FORME_CANA'), (3, 'DIAMETRE'), (4, 'MATERIAUX'), (5, 'HAUTEUR'), (6, 'LARGEUR'), (7, 'ANNEEPOSE'), (8, 'OBSERVATIO')]
    #[(0, 'TYP_RESEAU'), (1, 'TYP_ECOUL'), (2, 'FORME_CANA'), (3, 'DIAMETRE'), (4, 'MATERIAUX'), (5, 'HAUTEUR'), (6, 'LARGEUR'), (7, 'ANNEEPOSE'), (8, 'OBSERVATIO')]

    sql = "SELECT "

    sql = "SELECT Infralineaire_qgis.id_descriptionsystem, ST_AsText(Infralineaire_qgis.geom), "
    # [(0, 'TYP_RESEAU'),
    sql += """
            CASE WHEN typeReseau = 'PLU' THEN 'Eaux pluviales'
            WHEN typeReseau = 'USE' THEN 'Eaux usées' 
            WHEN typeReseau = 'UNI' THEN 'Unitaire'
            END,
            
            """
    #(1, 'TYP_ECOUL'),
    sql += """
            CASE WHEN modeCirculation = 1 THEN 'Gravitaire'
            WHEN modeCirculation = 2 THEN 'Refoulement' 
            WHEN modeCirculation = 3 THEN 'Sous-vide'
            END,

            """
    # 2, 'FORME_CANA'),
    sql += """
            CASE WHEN formecanalisation = 'CIR' THEN 'Circulaire'
            WHEN formecanalisation = 'AQU' THEN 'Aqueduc' 
            WHEN formecanalisation = 'OVO' THEN 'Ovoide'
            WHEN formecanalisation = 'FOS' THEN 'Fossé enherbé'
            WHEN formecanalisation = 'FOB' THEN 'Fossé béton'
            END,

            """
    #(3, 'DIAMETRE'),
    sql += "diametreNominal * 1000 ,"
    # (4, 'MATERIAUX'),
    sql += """
            CASE WHEN materiau = '03' THEN 'Béton armé tole'
            WHEN materiau = '04' THEN 'Béton armé' 
            WHEN materiau = '06' THEN 'Béton non armé'
            WHEN materiau = '18' THEN 'PEHD lisse'
            WHEN materiau = '26' THEN 'PVC U annele'
            WHEN materiau = '27' THEN 'PVC U lisse'
            WHEN materiau = '28' THEN 'Tole galvanisee'
            ELSE (CASE WHEN formecanalisation = 'FOS' THEN NULL ELSE 'Indéterminé' END)
            END,

            """
    #(5, 'HAUTEUR'), (6, 'LARGEUR'), (7, 'ANNEEPOSE'),
    sql += "NULL, NULL, NULL,  "
    # Observation
    sql += """
            CASE WHEN branchement = 0 THEN 'Réseau principal'
            WHEN branchement = '1' THEN 'Réseau de branchement' 

            END

            """

    #sql += "ST_Length(Infralineaire_qgis.geom) "

    sql += " FROM Infralineaire_qgis"

    reschp01 = dbaseparserfrom.query(sql)

    pprint.pprint(reschp01[0:10])

    if True:
        fileraw, ext = os.path.splitext(pathvlayer)
        basename = os.path.basename(fileraw)
        sqlitebasename = os.path.basename(pathfrom).split('.')[0]



        fileto = os.path.join(exportpath, basename+'_' + sqlitebasename + '.shp')
        print(fileto)

    if True:

        for ext in ['.shp', '.dbf', '.qpj', '.prj', '.shx']:
            try:
                os.remove(os.path.join(exportpath, basename+'_' + sqlitebasename +ext))
            except :
                pass
            copyfile(fileraw + ext, os.path.join(exportpath, basename+'_' + sqlitebasename +ext))

    if True:

        print(fileto)
        vlayerto = qgis.core.QgsVectorLayer(fileto, "toto", "ogr")
        print(vlayerto.isValid())
        vlayerto.startEditing()

        featurelist=[]
        for i, elem in enumerate(reschp01):
            feat = qgis.core.QgsFeature(vlayerto.fields())
            if i==0:
                print([(k, f.name()) for k, f in enumerate(feat.fields())])
                print([(k, type(elem[k])) for k, f in enumerate(feat.fields())])
            #geom
            geom = qgis.core.QgsGeometry.fromWkt(elem[1])
            feat.setGeometry(geom)
            featurelist.append(feat)

            for j, sselem in enumerate(elem[2:]):
                if False and isinstance(sselem, float):
                    sselem = float(round(sselem,2))
                feat[j] = sselem

        success = vlayerto.addFeatures(featurelist)
        print(success)

        vlayerto.commitChanges()



print('start')

onlyfiles = [f for f in os.listdir(sourcepath) if os.path.isfile(os.path.join(sourcepath, f))]
print(onlyfiles)
for sqlfile in onlyfiles:
    ExportOldLamiaNode(os.path.join(sourcepath, sqlfile))
    ExportOldLamiaLine(os.path.join(sourcepath, sqlfile))

print('ok')