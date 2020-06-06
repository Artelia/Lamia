La base de données
####


.. image:: ./rawimages/database/lamia_database.png
    :width: 400px
    :align: center

L'organisation générale
=====================================

Le schéma ci-dessus montre l'architecture générale de la base de données. On retrouve quatre grands groupes de tables. 

*   Les tables dédiées à la description du patrimoine (en bleu), comprenant les noeuds et les ronçons topologiques, ainsi que des éléments autres;
*   Les tables servant à poiner vers des ressources diverses (en violet) , telles des photos, des plans, des rapports....
*   Les tables de gestion, comme le intervenants ou les zones géograpiques (en blanc à gauche);
*   Les tables liées à l'état et aux interventions sur le réseau (désodre, observation, travaux,..).


La table Objet
=====================================

Lors de la création d'un élément dans un table quelconque, il est créé un élément dans la table objet. Cet élément est renseigné avec une clé primaire, une date de création, une date de version...
