.. toctree::
    :maxdepth: 3


Import d'inspections ITV (Valable uniquement pour Lamia assainissement)
###############################################################################

Utilisation du module
*****************************

.. image:: /../_static/ITV/NewITV.png
    :width: 400px
    :align: center

On accède à ce module allant dans "Interface / Bureau" et en selectionnant
l'onglet "ITV".

Il faut alors :

* créer une nouvelle campagne t'ITV (bouton +)

* Renseigner son nom et choisir les fichiers .csv associés à cette campagne (on peut choisir plusieurs fichiers)

.. image:: /../_static/ITV/itv_choose_files.png
    :width: 400px
    :align: center

* Enregistrer le formulaire ITV.


Exploitation des informations
*****************************

l'identifiant du regard de l'ITV doit correspondre au nom de regard de Lamia (champ "name" de la table "node_qgis").

Le boutton "Check if all nodes in Lamia" permet de savoir combien de noeuds de l'ITV sont retrouvées dans les noeuds rentrés dans Lamia.

Le boutton "View csv" permet de voir les données de l'ITV au format .csv (toutes les données de l'ITV sont présentées, pour cette fonction on n'a pas 
besoin d'avoir une correspondance entre les noms ITV et les noms Lamia).

Le boutton "View as Layer" permet de créerune couche QGis localisant les désordres recensés. Attention : il faut que les noeuds
amont et aval de l'ITV correspondent au champ "name" de la table "node" dans QGis.


