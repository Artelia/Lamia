Introduction
============

Ce document a pour but de donner les éléments de contexte du
développement de LAMIA, de détailler le fonctionnement du code et de
fournir suffisamment d’informations techniques pour permettre à toute
personne le souhaitant de rapidement commencer à développer de nouvelles
fonctionnalités.

Démarche générale, license
==========================

Nous cherchons à aider à la construction de base de données robustes et
cohérentes qui pourront vivre pendant des années et permettre le
développement d’une connaissance forte des infrastructures afin de
permettre le passage d’une approche de déconstruction/reconstruction à
une approche de gestion patrimoniale et de maintenance préventive.

Notre but final est de permettre une réduction des coûts de maintenance
des grandes infrastructures linéaires telles que les digues, les routes
ou encore les ponts, tout en en limitant drastiquement l’impact
écologique.

Nous cherchons à fournir à tous les secteurs public et privé un outil
simple d’utilisation pour la collecte, la maintenance et la vie d’une
donnée de grande qualité sur les infrastructures linéaires.

Le projet LAMIA est développé et maintenu par ARTELIA et diffusé sous
licence GNU GPL v3 (ou postérieure).

Tutoriel
========

Installation
------------

Prérequis : Librairies osgeo nécessaires
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LAMIA est un module complémentaire pour Qgis 2.18 et supérieures se
manifestant sous la forme d’un panneau supplémentaire dans
l’application.

Il s'agit donc dans un premier temps d'installer QGis 2.18.

-  Pour windows, nous vous recommendons l'installateur osgeo4w. Cette
   installateur permet également l'installation des libraiies
   compélmentaires à QGIs permettant le fonctionnement de Lamia.

-  Sous linux, une installation via apt-get est recommendée.

Pour installer LAMIA, les bibliothèques suivantes sont nécessaires :

-  pyqgis
-  Numpy
-  Matplotlib
-  Networkx
-  Xlrd (excel reader)
-  Pillow

Ces librairies sont installables à partir de l'installateur osgeo4w pour
windows.

Lancement de Lamia
~~~~~~~~~~~~~~~~~~

Si vous disposez de toutes ces bibliothèques et que le python que Qgis
utilise y a bien accès, il vous suffit d’ajouter LAMIA au dossier des
extensions Qgis pour pouvoir commencer à l’utiliser.

Vous pouvez aussi télécharger LAMIA directement depuis le dépôt des
extensions officielles Qgis.

La base de données
------------------

|image0|

L'organisation générale
~~~~~~~~~~~~~~~~~~~~~~~

Le schéma ci-dessus montre l'architecture générale de la base de
données. On retrouve quatre grands groupes de tables.

-  Les tables dédiées à la description du patrimoine (en bleu),
   comprenant les noeuds et les ronçons topologiques, ainsi que des
   éléments autres;
-  Les tables servant à poiner vers des ressources diverses (en violet)
   , telles des photos, des plans, des rapports....
-  Les tables de gestion, comme le intervenants ou les zones
   géograpiques (en blanc à gauche);
-  Les tables liées à l'état et aux interventions sur le réseau
   (désodre, observation, travaux,..).

La table Objet
~~~~~~~~~~~~~~

Lors de la création d'un élément dans un table quelconque, il est créé
un élément dans la table objet. Cet élément est renseigné avec une clé
primaire, une date de création, une date de version...

Developpement
=============

Fonctionnement général
----------------------

Le code repose principalement sur trois classes.

-  La classe «
   Lamia.dialog.InspectionDigue_windowwidget.InspectiondigueWindowWidget
   », qui est chargée au démarrage. Il s’agit du QDockWidget
   apparaissant au click sur l’icone Lamia dans l’interface QGis.
-  La classe « Lamia.main.DBaseParser.DBaseParser ». Il s’agit d’un
   QObject chargé de l’ensemble des intéractions avec la base de
   données.
-  La classe « Lamia.toolabstract. Lamia_abstract_tool.
   AbstractLamiaTool » qui est un widget abstrait dont héritent tous les
   widgets apparaissant sur l’écran « propriétés ».

L’activité lors de l’ouverture de la base de données est schématisée
ci-dessous :

|image1|

*InspectiondigueWindowWidget* est créé lors de l’ouverture de Lamia. Au
chargement/création de la base de données, la classe DBaseParser est
créée en variable *d’InspectiondigueWindowWidget* et cette classe se
charge de la création et de la lecture de la base de données.

Ensuite,\ *InspectiondigueWindowWidget.DBaseLoaded* charge l’ensemble
des widgets (tous héritant de AbstractLamiaTool) apparaissant dans
l’écran en bas à droite du *InspectiondigueWindowWidget*.

Ainsi, le code est structuré de la façon suivante :

================ ======================================================================================================================================================
Dossier          Contenu
+---dialog       Contient les fichiers sources des interfaces graphiques des boites de dialogues de LAMIA ainsi que les codes python pour les gérer.
                
                 Il contient notamment *InspectiondigueWindowWidget* .
+---main         Contient le main de LAMIA qui importe le DBaseParser et le DBaseParser qui initialise l'environnement LAMIA.
                
+---toolabstract Contient Lamia_abstract_tool.py qui est la classe abstraite dont héritent tous les widgets présents en bas à droite de *InspectiondigueWindowWidget* .
================ ======================================================================================================================================================

Les éléments propres à la création et à la manipulation de la base de
données sont ici :

================== ==========================================================================================================
Dossier            Contenu
+---DBASE          Dossier contenant tous les éléments nécessaires à la création des bases de données
\| +---BPU         Dossier contenant les bordereaux de prix permettant le chiffrage automatique des travaux
\| +---create      Dossier contenant tous les fichiers excel embarquant la description des tables ainsi que les nomenclatures
\| +---sqlite_base Dossier contenant la base SQLITE utilisée pour amorcée la création des bases de données
\| +---style       Contient les feuilles de styles utilisées pour l'affichage de l'interface LAMIA
\| \\---utils      Contient des ressources d'affichage
================== ==========================================================================================================

Tous les widgets apparaissant en bas à droite
d’\ *InspectiondigueWindowWidget* et héritant de AbstractLamiaTool sont
stockés ici :

==================== ========================================================================================================================
Dossier              Contenu
+---toolpostpro      Outils de post-production (synthèses, exports, rapports, …)
\| +---Base2         Outils génériques d'import, d'export, de synthèse, de gestion des paths, de génération des rapports, d'étude de coûts, …
\| +---[Type métier] Outils de post-traitement adaptés au métier.
\\---toolprepro      Interfaces graphiques et classes pythons permettant de manipuler la base de données
\| +---Base2         Outils génériques 
\| +---[Type métier] Outils d’alimentation de la base de données adaptés au métier.
==================== ========================================================================================================================

En plus de ces packages, les packages suivants sont également utilisés.

=============================== ==========================================================================================================
Dossier                         Contenu
+---config                      Stock les données récemment utilisées à conserver en mémoire comme l'adresse des dernières bases utilisées
+---gps                         Contient les outils de connexion et d'exploitation des GPS
+---html                        Contient des outils de mise en page (js, css, images, polices, …)
+---icons                       Contient les icones utilisés dans LAMIA
+---lamiautils                  Vide
+---libs                        Continent certaines librairies embarquées directement dans LAMIA, souvent parce qu'elles ont été modifiées
\| +---cloudant                 Librairie de connexion à une base NoSQL (lien avec SIRS Digues)
\| +---cloudant_2_10            Librairie de connexion à une base NoSQL (lien avec SIRS Digues)
\| +---pyqtgraph                Librairie de génération de graphiques
\| \\---xlrd                    Librairie de lecture de fichier Excel utilisée pour la création des bases de données
+---maptool                     Contient les éléments d'interaction avec la cartographie de Qgis
+---toolgeneral                 Contient des modules complémentaires pour LAMIA
\| +---LAMIA_to_SIRS            Permet de faire la passerelle depuis LAMIA vers SIRS Digues
\| +---LAMIA_to_SIRS_VCouch1_7  Permet de faire la passerelle depuis LAMIA vers SIRS Digues V1.7
\| +---SIRS_to_LAMIA            Permet de faire la passerelle depuis SIRS Digues vers LAMIA
\| \\---SIRS_to_LAMIA_VCouch1_7 Permet de faire la passerelle depuis SIRS Digues vers LAMIA
=============================== ==========================================================================================================

Cas pratique : création d’un nouveau module de post-traitement
--------------------------------------------------------------

Nous voulons créer un module de post-traitement pour le métier
« éclairage ».

Dans ce cas, il faut créer un fichier test_module.py dans le répertoire
lamia/toolpostpro/Base2_eclairage.

Ensuite, il convient de créer un widget avec QtDesigner et de
l’enregistrer sous 'test_module.ui' dans le même répertoire.

Ce fichier aura la structure minimale suivante :

.. code-block:: python

import os

from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool

from qgis.PyQt import uic

from qgis.PyQt.QtWidgets import (QWidget)

class CostTool(AbstractLamiaTool):

TOOLNAME = 'test_module'

def \__init__(self, dbase, dialog=None, linkedtreewidget=None,
gpsutil=None,parentwidget=None, parent=None):

super(CostTool, self).__init__(dbase, dialog, linkedtreewidget,
gpsutil,parentwidget, parent=parent)

def initTool(self):

#
\***************************************************************************************\*

# Main spec

self.CAT = 'Synthese'

self.NAME = 'Couts'

self.visualmode = [4]

self.groupBox_elements.setParent(None)

self.frame_editing.setParent(None)

def initFieldUI(self):

if self.userwdgfield is None:

self.userwdgfield = UserUI()

class UserUI(QWidget):

def \__init__(self, parent=None):

super(UserUI, self).__init__(parent=parent)

# self.setupUi(self)

uipath = os.path.join(os.path.dirname(__file__), 'test_module.ui')

uic.loadUi(uipath, self)

API
===

Class DBaseParser
-----------------

.. autoclass:: Lamia.main.DBaseParser.DBaseParser

:members:

.. :automethod:: Lamia.main.DBaseParser.DBaseParser.__init_\_

Class InspectionDigue_windowwidget
----------------------------------

.. automodule:: Lamia.dialog.InspectionDigue_windowwidget

:members:

:private-members:

Class Lamia_abstract_tool
-------------------------

.. automodule:: Lamia.toolabstract.Lamia_abstract_tool

:members:

.. |image0| image:: Pictures/10000000000006130000032E7295F17AD75EE661.jpg
   :width: 17cm
   :height: 8.899cm
.. |image1| image:: Pictures/100000000000035B0000022573534E11B79297C1.png
   :width: 13.996cm
   :height: 8.945cm
