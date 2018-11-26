Explication de l'export 


************************** Les Bases ****************************************************************
Tout d'abord, pour comprendre, il ne faut pas qu'il y ait de champs en double dans la requete


ensuite la requete est construite comme ca :

##with clause + selection des attributs + ##main clause

ainsi, avec le script suivant,

"
###main
FROM Photo_qgis

###with
WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL)

"
 ça fait:
 
 "
 
 WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) + "SELECT (on verra apprès) " + FROM Photo_qgis
 
 "
 
 
 si l'on selectionne des zonesgeo, ca rajoute :
  WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) 
  SELECT (on verra apprès)  
  FROM Photo_qgis  WHERE pk_zonegeo in (1,2,3)
 
 
 Enfin, si l'on utilise le mot cle _now a la fin d'une table ca rajoute les contraintes de date et version
 ex :
 "
 
###main
FROM Photo_now

###with
WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL)

"
 
 devient :
   WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) ,
   Photo_now as (SELECT * FROM Photo_qgis WHERE + contraintes date et version )
  SELECT (on verra apprès)  
  FROM Photo_now  WHERE pk_zonegeo in (1,2,3)
 
 
************************** les colonnes selectionnees ****************************************************************
 il faut ensuite définir les champs qui seront mis dans la requetes (et qui seront au final dans le shapefile
 
************************** la version simple c'est ça :

###Photo
#nom              type               cst               valeur             as       
id_photoshp;         Int;                  ;               id_photo ;         photototo

on définit un nom qui sera utilisé pour retrouver la valeur non formatée pour la séquence (ici ###Photo)
ensuite on défini pour la colonne à mettre dans le shapefile:
le nom de la colonne qui sera utilisé dans le .shp
le type de variable du shp (Int, String ou Double)
si la valeur cst n'est pas nulle, c'est utilisé pour retrouver la valeu non formatée du champ (INF deviendra Infralineaire p.Ex)
la valeur de la colonne dans la base de données : id_photo
en option, une valeur pour donner un nom à la variable ainsi utilisée, ici photototo

la requete finale devient:

WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) 
SELECT id_photo  as photototo
FROM Photo_qgis



************************** la version plus compliquée c'est ça :

###Photo
##FROM Photo_now  WHERE Photo_now.id_ressource = Infralineaire.lid_ressource_1
#nom              type               cst               valeur             as       
id_photoshp;         Int;                  ;               id_photo ;         photototo

l'intérêt est que ca crée un requete où l'on ajoute les contraines de version et de date


la requete finale devient:

WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) ,
Photo_now as (SELECT * FROM Photo_qgis WHERE + contraintes date et version )
SELECT (SELECT  id_photo FROM Photo_now  WHERE Photo_now.id_ressource = Infralineaire.lid_ressource_1) AS photototo
FROM Photo_now


************************** astuces ****************************************************************

il faut rajouter 

###Zonegeo
## FROM Zonegeo_now WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom),ST_MakeValid(Zonegeo_now.geom))
pk_zonegeo;     Int;            ;        pk_zonegeo ;  pk_zonegeo
secteur;     String;            ;        libelle

adapté à la table pour que l'export se fasse avec les zones geo selectionnées




Pour les tables de correspondances, les définir avec with et ne pas mettre lpk_revision_end ni lpk_revision_begin sinon la requete reconnait les champs en double et ca marche pas...



la valeur rentrée pour la colonne peut être une requete sql
###Infralineaire
##FROM Infralineaire_qgis AS Infralineairetemp WHERE  Infralineairetemp.pk_objet = Infralineaire_qgis.pk_objet
#nom              type               cst               valeur                                                                                                as       
photo;        String;                          ;        (SELECT file FROM Ressource WHERE Ressource.id_ressource = Infralineaire_qgis.lid_ressource_2)

ou 
#nom              type               cst               valeur                                                                                                as       
photo;        String;                          ;        CASE WHEN id_infralineaire IS NULL THEN 1 ELSE 0 END


