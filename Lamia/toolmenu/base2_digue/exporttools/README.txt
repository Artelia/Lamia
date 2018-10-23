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

 �a fait:
 
 WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) + "SELECT (on verra appr�s) " + FROM Photo_qgis
 
 
 si l'on selectionne des zonesgeo, ca rajoute :
  WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) + "SELECT (on verra appr�s) " + FROM Photo_qgis + WHERE pk_zonegeo in (1,2,3)
 
************************** les colonnes selectionnees ****************************************************************
 il faut ensuite d�finir les champs qui seront mis dans la requetes (et qui seront au final dans le shapefile
 
************************** la version simple c'est �a :

###Photo
#nom              type               cst               valeur             as       
id_photoshp;         Int;                  ;               id_photo ;         photototo

on d�finit un nom arbitraire pour la s�quence (ici ###Photo)
ensuite on d�fini pour la colonne � mettre dans le shapefile:
le nom qui sera mis dans le .shp
le type de variable du shp (Int, String ou Double)
la valeur dans la base de donn�es : id_photo
en option, une valeur pour donner un nom � la variable ainsi utilis�e, ici photototo

la requete finale devient:

WITH Tcobjetressourcetemp AS ( SELECT lid_ressource, lid_objet FROM Tcobjetressource WHERE lpk_revision_end IS NULL) SELECT id_photo  FROM Photo_qgis

************************** la version plus compliqu�e c'est �a :

###Photo
##FROM Photo AS Phototemp WHERE Phototemp.pk_photo = Photo_qgis.pk_photo
#nom              type               cst               valeur             as       
id_photoshp;         Int;                  ;               id_photo ;         photototo

l'int�r�t est que ca cr�e un requete o� l'on ajoute les contraines de version et de date


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

adapt� � la table pour que l'export se fase avec les zones geo selectionn�es




Pour les tables de correspondances, les d�finir avec with et ne pas mettre lpk_revision_end ni lpk_revision_begin sinon la requete reconnait les champs en double et ca marche pas...



la valeur rentr�e pour la colonne peut �tre une requete sql
###Infralineaire
##FROM Infralineaire_qgis AS Infralineairetemp WHERE  Infralineairetemp.pk_objet = Infralineaire_qgis.pk_objet
#nom              type               cst               valeur                                                                                                as       
photo;        String;                          ;        (SELECT file FROM Ressource WHERE Ressource.id_ressource = Infralineaire_qgis.lid_ressource_2)

ou 
#nom              type               cst               valeur                                                                                                as       
photo;        String;                          ;        CASE WHEN id_infralineaire IS NULL THEN 1 ELSE 0 END


