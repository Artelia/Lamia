Explication de l'export 


************************** Les BAses ****************************************************************
tout d'abord, pou comprendre, il ne faut pas qu'il y ait de champs en double dans la requete

ensuite la requete est construite comme ca :

##with clause + selection des attributs + ##main clause

ainsi, avec le script suivant,

###main
FROM Photo_qgis

###with
WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL)

 ça fait:
 
 WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) + "SELECT (on verra apprès) " + FROM Photo_qgis
 
 
 si l'on selectionne des zonesgeo, ca rajoute :
  WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) + "SELECT (on verra apprès) " + FROM Photo_qgis + WHERE pk_zonegeo in (1,2,3)
 
************************** les colonnes selectionnees ****************************************************************
 il faut ensuite définir les champs qui seront mis dans la requetes (et qui seront au final dans le shapefile
 
************************** la version simple c'est ça :

###Photo
#nom              type               cst               valeur             as       
id_photoshp;         Int;                  ;               id_photo ;         photototo

on définit un nom arbitraire pour la séquence (ici ###Photo)
ensuite on défini pour la colonne à mettre dans le shapefile:
le nom qui sera mis dans le .shp
le type de variable du shp (Int, String ou Double)
la valeur dans la base de données : id_photo
en option, une valeur pour donner un nom à la variable ainsi utilisée, ici photototo

la requete finale devient:

WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) SELECT id_photo  FROM Photo_qgis

************************** la version plus compliquée c'est ça :

###Photo
##FROM Photo AS Phototemp WHERE Phototemp.pk_photo = Photo_qgis.pk_photo
#nom              type               cst               valeur             as       
id_photoshp;         Int;                  ;               id_photo ;         photototo

l'intérêt est que ca crée un requete où l'on ajoute les contraines de version et de date


la requete finale devient:

WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) 
SELECT (SELECT  id_photo FROM Photo AS Phototemp WHERE Phototemp.pk_photo = Photo_qgis.pk_photo (+contraines sur lpk_revision_begin et datetimemodification) ) AS photototo
FROM Photo_qgis


************************** astuces ****************************************************************

il faut rajouter 

###Zonegeo
## FROM Zonegeo_qgis WHERE ST_WITHIN(ST_MakeValid(Infralineaire_qgis.geom),ST_MakeValid(Zonegeo_qgis.geom))
pk_zonegeo;     Int;            ;        pk_zonegeo ;  pk_zonegeo
secteur;     String;            ;        libelle

adapté à la table pour que l'export se fase avec les zones geo selectionnées




Pour les tables de correspondances, les définir avec with et ne pas mettre lpk_revision_end ni lpk_revision_begin sinon la requete reconnait les champs en double et ca marche pas...



la valeur rentrée pour la colonne peut être une requete sql
###Infralineaire
##FROM Infralineaire_qgis AS Infralineairetemp WHERE  Infralineairetemp.pk_objet = Infralineaire_qgis.pk_objet
#nom              type               cst               valeur                                                                                                as       
photo;        String;                          ;        (SELECT file FROM Ressource WHERE Ressource.id_ressource = Infralineaire_qgis.lid_ressource_2)

ou 
#nom              type               cst               valeur                                                                                                as       
photo;        String;                          ;        CASE WHEN id_infralineaire IS NULL THEN 1 ELSE 0 END


