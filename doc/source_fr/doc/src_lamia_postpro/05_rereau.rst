.. toctree::
    :maxdepth: 3

Utilisation du module Rereau
#####################################

Ce module permet d'appliquer la méthodologie Rereau à des ITVs.

On y accède via la barre de menu Lamia/ Interface / post-traitement  -- onglet 'Rer'eau'

.. image:: /../_static/postpro_rereau/presentation.png
    :width: 300px
    :align: center

Configuration des paramètres utilisés pour le calcul
***************************************

On peut changer les paramètres utilisés pour le calcul avec le menu déroulant. Les paramètres par défaut sont alpha = 2 et P = 5.

Le bouton 'NEW' permet d'ajouter une configuration au menu déroulant, définie par un alpha et un P.

Le bouton 'EDIT' permet de modifier les paramètres utilisés. On ne peut pas modifier les paramètres par défaut.

Le bouton 'DELETE' permet de supprimer une configuration. On ne peut pas supprimer la configuration par défaut.

Calculer les indicateurs Rereau et gérer les résultats
***************************************

En cliquant sur 'Compute' on lance le calcul des indicateurs.

Le menu déroulant 'Colour depends on :' permet de changer l'indicateur d'après lequel les couleurs des tronçons sont choisies. Les tronçons avec un score de 1 sont verts, 2 sont jaunes, 3 sont oranges, 4 sont rouges.

Le menu déroulant 'Select a result :' permet de choisir un résultat déjà calculer et de le charger (bouton 'Load') ou de le supprimer (bouton 'Delete result').
