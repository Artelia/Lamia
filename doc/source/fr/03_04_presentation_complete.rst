

Présentation Complète
##################################


Le menu
*********

.. image:: /_static/completepresentation/menu.png
    :width: 300px
    :align: center

Le menu fichier:
=====================

Nouvelle base de données
-----------------------------

Permet de créer une nouvelle base de données, l'utilisation est vue dans la prise en main rapide

Charger une base de données
-----------------------------

Charger la base de données voulue

Import/export
-----------------------------

Permet de transferer une base de données en local (sur l'ordinateur ou la tablette), de travailler sur cette
base de données en local, et ensuite de reverser les modifications sur la base de données "mère".

* Créer une copie locale

Après avoir ouvert la base de données "mère", cette fonction permet de créer une copie locale pour travailler dessus
hors connexion

* Reverser la base de données dans la base de données mère

Ceci permet de transférer les modifications faites sur la copie locale de la base mère (la base "enfant") vers
la base mère.

* Rajouter une DB à la DB actuelle

Permet d'ajouter une base de données de même type à la base de données ouverte.


Interface :
===============

Ce menu permet de changer d'interface. Trois modes sont actuellement disponibles :

* L'interface "terrain"

Cette interface est épurée et est destinée à l'utilisation par tablette lors des campagnes de terrain.

* L'interface "bureau"

L'interface bureau permet d'accéder à l'ensemble des tables et champs de Lamia.

* L'interface "Post-traitement"

Cette interface permet d'accéder à l'ensemble des modules de post-traitement (Cf. description et utilisation
Dans le paragraphe dédié).

Préférences :
===============

Répertoire des photos
-----------------------------

Le fait de configurer ici le répertoire où sont stockées les photos prises à l'aide de la tablette permet
d'utiliser l'outil "Baguette magique" lors de l'utilisation de la table photo. En effet, la baguette magique
ira automatiquement chercher la dernière photo prise avec la tablette.

Fonctions GPS
-----------------------------

* Se connecter au GPS Qgis

Cette fonction permet, une fois que le gps de qgis est opérationnel (Cf. prise en main rapide) de coupler
Lamia avec le GPS. La barre GPS apparait alors verte en bas de la fenêtre Lamia :

.. image:: /_static/quickstart/qs_12.png
    :width: 500px
    :align: center

* Hauteur de la perche GPS

Permet de rentrer la hauteur de la perche GPs dans le cas d'un GPS centimétrique avec relevé
de l'altimétrie.


Aide :
===============

Aide
--------

Permet d'acceder à la présente aide

Tables et champs
----------------------

Permet de visualiser l'ensemble des tables et champs de la base de données en cours
d'utilisation


La barre d'outils:
*********************

Edition d'objet
===================

.. image:: /_static/completepresentation/toolbar_objectediting.png
    :width: 200px
    :align: center

1. Creation d'objet

Permet la création d'un nouvel objet

2. "Baguette magique"

Permet la création de fonctions de raccourcis - souvent la création automatique de l'objet
à l'endroit de la position GPS lors de la campagne de terrain.

3. Annuler les modifications

4. Supprimer l'objet

5. SAuvegarder l'objet en cours d'édition.




Edition de geometrie
=======================

.. image:: /_static/completepresentation/toolbar_geomediting.png
    :width: 200px
    :align: center

1. Saisie d'un nouveau point

2. Saisie d'une nouvelle ligne

3. Saisie d'un nouveau Polygone

4. Rajout d'un point à une polyligne

5. Rajout d'un point depuis la position GPS.

Cette fonction nécessite que le GPS de Lamia soit connecté.


Edition de couche vecteur
=========================

.. image:: /_static/completepresentation/toolbar_layerediting.png
    :width: 150px
    :align: center

1. Ouvrir la couche vecteur de l'objet en cours d'édition

Ceci permet notamment  pour les lignes et les polylignes d'acceder aux fonctions d'édition
de géomtrie avancées de QGis.

2. Quitter les modifications sans sauvegarder.

3. Enregistrer les modifications.



Outils
===================

Cette barre permet d'acceder à divers outils, tels l'impression.