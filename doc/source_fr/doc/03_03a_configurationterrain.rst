

Prise en main rapide - premiere utilisation "sur le terrain"
################################################################

.. warning::

    Il faut avoir au préalable lu la section précédente "première utisation au bureau "


Définition du répertoire de photo par défaut
==============================================

En cas d’utilisation de l’appareil photo de la tablette, il est possible de rapatrier automatiquement 
la dernière photo prise avec l’appareil photo. En revanche, il faut dire à Lamia où se situe 
le répertoire on sont stockées les photos.

Pour ce faire, dans la fenètre Lamia, aller dans Préférences/Répertoire Photo et choisir le 
répertoire où sont stockées les photos prises avec la tablette. Classiquement, elles sont dans
CePC\\Images\\Pellicule :

.. image:: /../_static/quickstart/fieldinvestigation_camera.png
    :width: 400px
    :align: center

.. image:: /../_static/quickstart/fieldinvestigation_camera_2.png
    :width: 400px
    :align: center


Ensuite, lors de l'utilisation du bouton "Baguette magique" dans la barre d'outil (à côté du +), et lorsque
vous êtes dans l'onglet "Photographie", Lamia créera automatiquement un nouvelle photo avec la dernière photo
prise. Si en plus vous êtes connecté au GPS (Cf. ci après), la photo se localisera automatiquement là où vous êtes.



Utilisation d’un GPS
==============================================

QGis et Lamia peuvent fonctionner avec un GPS. 

1. Je connecte le GPS de la tablette

Je vais dans le centre de notification Windows 10 et j'active le GPS ("Emplacement doit 
devenir bleu)

.. image:: /../_static/quickstart/GPS_01.png
    :width: 200px
    :align: center

1bis. Je connecte un GPS centimétrique

Il s'agit dans un premier temps de configurer le GPS pour qu'il envoit des données GPS de type 
"GGA" et "GST" (Pour ce faire, voir la doc fournisseur du GPS, se connecter en wifi à la 
configuration du GPS , cherche l'onglet de configuration des messages "NMEA" envoyés).

Aussi, le PS doit avoir le bluetooth activé et doit pouvoir envoyer ces informations par bluetooth.

Enfin, il s'agit de connecter la tablette au GPS via la connection bluetooth.


2. Je configure la hauteur de ma perche dans le cas de l'utilisation d'un GPS centimétrique.

Dans le menu Lamia, aller dans Préférences/Hauteur de perche et saisir la hauteur de la perche GPS.

3. Connecter QGis au GPS

Dans Qgis, aller dans le menu Vue/Panneau et cliquer sur information GPS. Un panneau apparaîtra permettant 
de connecter Qgis au GPS. Clicker sur connecter. Le petit rectangle grisé en haut à droite passe au 
vert lorsque la connection avec le GPS est établie.

.. image:: /../_static/quickstart/qs_11.png
    :width: 500px
    :align: center

4. Connecter Lamia à QGis.

Dans les menus Lamia, aller dans Préférences/se connecter au GPS pour connecter Lamia au Gps 
reconnu par Qgis.

Si le GPS est opérationnel, en bas de la fentre Lamia GPS connecté apparaît en vert. 

.. image:: /../_static/quickstart/qs_12.png
    :width: 500px
    :align: center

Il redevient rouge si Lamia perd le signal GPS.


Utilisation des fonctions GPS dans Lamia
==============================================

Saisie d'un point GPS ou rajout d'un point GPS à une ligne
---------------------------------------------------------------

Il suffira de cliquer sur le bouton suivant pour effectuer cette action :

.. image:: /../_static/quickstart/GPS_02.png
    :width: 500px
    :align: center

Ajouter une photo
==============================================

Quand le GPS est connecté, la prise de photo s'effectue selon le déroulé suivant :

1. Ouvrir l'appareil photo en cliquant sur l'icone suivante :

.. image:: /../_static/quickstart/camera1.png
    :width: 500px
    :align: center

2. Prendre la photo

 

3. Intégrer la photo à Lamia

Se rendre sur l'onglet photo de l'élément auquel on souhaite ratacher une photo et cliquer
sur l'icone baguette magique comme ci-dessous :

.. image:: /../_static/quickstart/camera2.png
    :width: 500px
    :align: center

Ce click a pour effet de :

- créer la nouvelle photo

- la localiser à l'emplacement GPS actuel

- Prendre la derniere photo prise

- Enregistrer la photo.
