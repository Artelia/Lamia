Structure de la base de données
===============================


Nommage des fichiers
~~~~~~~~~~~~~~~~~~~~

Le modèle pour la création de la base de données est dans le répertoire Lamia\\DBASE\\create\\{nom_du_metier}

Dans ce répertoire se trouvent les fichiers textes contenant les informations nécessaires à la création de la base de données et à la définition des valeurs contraintes. 

Ces fichiers textes sont nommés comme suit :

{numero}_{nom_de_la_table_créée) avec :

* numero : l'ordre de création de la table en question. L'ordre compte car des champs avec des clés étrangères sont créés à l'occasion. Il faut alors que la table liée existe déjà.
* nom_de_la_table_créée : c'est le nom que prendra la table dans la base de données.

Contenu du fichier
~~~~~~~~~~~~~~~~~~~

En tête
+++++++

L'en tête peut contenir les lignes suivantes :

#DJAN 
    requete sql pour créer la vue utilisée sous Django
#QGIS
    requete sql pour créer la vue qui alimente la table affichée sous qgis. Doit contenir les colonnes  datecreation,  datedestruction, revisionbegin et revisionend.
    Qgis effectue une requete sur cette view pour afficher les bons elements en fonction de la date et du numero de version.
    
#SHOW
    Prends la valeur YES ou NO . Charge la table dans qgis ou non.
    
#EXPO 
    requete sql qui créé une view.

Corps du fichier
++++++++++++++++
    
Ensuite vient la création des colonnes à proprement parler. Le mise en forme est celle ci :

Example::

    ### Nom_du_champ;TypePostGis;TypeSpatialite ;Option

Avec:

Nom_du_champ
    le nom du champ. Voir le paragraphe suivant pour les conventions de nommage.
    
TypePostGis
     VARCHAR(255), INT
     
TypeSpatialite
    TEXT, INTEGER

Option
    Utilisée pour sépcifier une relation par clé étrangère. Mettre le nom de la table puis le nom de la colonne entre parenthèse :
    exemple :
    Descriptionsystem(id_descriptionsystem)
    
    
Valeurs contraintes
~~~~~~~~~~~~~~~~~~~

Il es possble d'indiquer les valeurs que peut prendre la colonne. Rajouter alors en dessous de la déclaration de la colonne /
(###nom_colonne) des lignes avec un couple {valeur affichée; valeur stockée dans la table}

Example::

    ###cote;                VARCHAR(255);            TEXT
    /;
    Eau;RIV
    Terre;TER
    Etang;ETG

De même, si une deuxième colonne a des valeurs contraines par les valeurs d'une premère colonne, préciser la colonne  associée avec ##colonne_associée puis indiquer un trio {valeur affichée; valeur stockée dans la table; valeur qui peut prendre la colonne mère}

Example::

    ###position;           VARCHAR(255);            TEXT
    ##cote
    /;                                 ;            ['','RIV','TER','DEU','MER','CRE','IND']
    Crete;                          CRE ;           ['CRE']
    Talus digue;                     TAD ;          ['RIV','TER','DEU','MER','ETG']

    
Commentaires
~~~~~~~~~~~~

Un commentaire peut être insérer avec # en tête de ligne
    
    
Convention de nommage utilisées
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Colonne avec clé étrangère
++++++++++++++++++++++++++

Une convention de nommage est utilisée pour les colonnes associées à des clés étrangères. 

Trois mots clés sont alors  utilisés pour le nom des colonnes: ``pk``, ``id_`` et ``lk_``. A la suite doit être indiqué le nom de la table (en minuscule) associée à cette colonne . 
Si plusieurs colonnes ont une clé étrangère renvoyant vers une même table, les appeler lk_nomtable1, lk_nomtable2 ...

La différence entre ``id_`` et ``lk_`` est que ``id_`` est lié à les tables parentes (c'est à dire créées en même temps que la ligne  de la table), alors que ``lk_`` est utilisé pour des jointures ultérieures.

Colonne avec date
+++++++++++++++++

Appeler le champ date.....

Colonne de géométrie
++++++++++++++++++++

Toujours l'appeler "geom"


structure commune à tous les métiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Indépendemment des métiers, une structure commune est à utiliser et se trouve dans Lamia\\DBASE\\create\\Base

Pour créer une nouvelle base, créer un repertore dans Lamia\\DBASE\\create qui s'appelle Base_{nom du metier}



