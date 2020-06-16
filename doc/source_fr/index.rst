.. toctree::
    :hidden:
    :caption: Documentation utilisateur en français
    :maxdepth: 4

    doc/00_index


.. comment contents:: :local:


Le projet Lamia
==============================

.. raw:: html

    <div style="display: flex;flex-direction: column;">
        <div style="display: flex;flex-direction: row;">
            <p style="flex: 3 ">
            Dans le cadre de sa transformation digitale et afin d’améliorer sa qualité de service, 
            Artelia a mis au point une solution numérique globale destinée à la gestion patrimoniale 
            d’infrastructures linéaires : le projet LAMIA. <br> 
            Les types d'infrastructures actuellement prises en compte par Lamia sont :
            </p>
            <div data-aos="fade-left" style="flex: 1 ;margin: 20px;">
                <img height="300" src="_static/presentation/logoArtelia.png">
            </div>
        </div>
        <div style="display: flex;flex-direction: row;">
            <p style="flex: 3 ">
            Gestion patrimoniale des <b>réseaux d'assainissement</b> urbains
            </p>
            <div data-aos="fade-left" style="flex: 1 ;margin: 20px;">
                <img height="75px" src="_static/presentation/assainissement.png">
            </div>
        </div>

        <div style="display: flex;flex-direction: row;">
            <p style="flex: 3 ">
            Gestion patrimoniale des <b>réseaux d'eau potable</b>
            </p>
            <div data-aos="fade-left" style="flex: 1 ;margin: 20px;">
                <img height="75px" src="_static/presentation/waterdistribution.jpg">
            </div>
        </div>

        <div style="display: flex;flex-direction: row;">
            <p style="flex: 3 ">
            Gestion patrimoniale des <b>digues</b> de protection contre les inondations
            </p>
            <div data-aos="fade-left" style="flex: 1 ;margin: 20px;">
                <img height="75px" src="_static/presentation/levee.png">
            </div>
        </div>
        <div style="display: flex;flex-direction: row;">
            <p style="flex: 3 ">
            Relevés de terrain <b>faune/flore</b>
            </p>
            <div data-aos="fade-left" style="flex: 1 ;margin: 20px;">
                <img height="75px" src="_static/presentation/faunaflora.png">
            </div>
        </div>
        <div style="display: flex;flex-direction: row;">
            <p style="flex: 3 ">
            Le suivi de <b>chantier</b>
            </p>
            <div data-aos="fade-left" style="flex: 1 ;margin: 20px;">
                <img height="75px" src="_static/presentation/constructionsite.png">
            </div>
        </div>
    </div>

Le projet Lamia est constitué de deux composantes : 

.. raw:: html

    <div style="display: flex;flex-direction: column;">
        <div style="display: flex;flex-direction: row;">
            <p style="flex: 2 ">
            
            la base de données géographique (PostGis, Spatialite)
            <br>La base de données de LAMIA est structurée de façon à 
            s’adapter à toute infrastructure linéaire. 
            <br>Les thèmes traités par cette base de données sont :
            <br> •	La description du patrimoine (caractéristiques géométriques, fonctionnelles…) ;
            <br> •	Les ressources au sens large que l’on peut associer à ce patrimoine 
            (photographies, rapports, relevés de terrain…) ;
            <br> •	Les éléments de gestion (annuaire des prestataires et usagers, zones de gestion, etc…) ;
            <br> •	Les éléments relatifs au suivi de l’état du patrimoine.

            <div data-aos="fade-left" data-aos-duration="3000" data-aos-anchor-placement="center-bottom" 
                    style="flex: 1 ;margin: 20px;">
                <img height="75px" src="_static/presentation/database.png">
            </div>
        </div>

        <div style="display: flex;flex-direction: row;">
            <p style="flex: 2 ">
            les outils d’accès et de consultation de cette base de données (QGis, Web)
            </p>
            <div data-aos="fade-left"  data-aos-duration="3000"  data-aos-anchor-placement="center-bottom" 
                    style="flex: 1 ;margin: 20px;">
                <img height="75px" src="_static/presentation/qgisiface.png">
            </div>
        </div>
    </div>



L’ensemble de ces briques sont développées en open-source.




Objectif du projet
=============================

Nous cherchons à aider à la construction de base de données robustes et cohérentes 
qui pourront vivre pendant des années et permettre le développement d’une connaissance 
forte des infrastructures afin de permettre le passage d’une approche de 
déconstruction/reconstruction à une approche de gestion patrimoniale et de 
maintenance préventive. 

Notre but final est de permettre une réduction des coûts de maintenance 
des grandes infrastructures linéaires telles que les digues, les routes ou encore 
les ponts, tout en en limitant drastiquement l’impact écologique. 

Nous cherchons à fournir à tous les secteurs public et privé un outil simple 
d’utilisation pour la collecte, la maintenance et la vie d’une donnée de grande qualité 
sur les infrastructures linéaires. 






Fonctionnalités
==============================

Acquisition et exploitation de données terrain
----------------------------------------------------------------

.. raw:: html

    <div style="display: flex;flex-direction: row;">
        <p style="flex: 2 ">
        L’interface sous QGis, associé à un GPS (tablette ou spécifique) permet la saisie 
        géoréférencée des éléments observés sur site.
        L’interface de saisie a été élaborée en étroite collaboration 
        avec les agents de terrain pour en faire un outil accepté.
        </p>
        <div data-aos="flip-down"  data-aos-duration="1000" data-aos-anchor-placement="center-bottom" 
                style="flex: 1 ;margin: 20px;">
                <img height="75px" src="_static/presentation/dataacquisition.png">
        </div>
    </div>

Import et export de la donnée
----------------------------------------------------------------

.. raw:: html

    <div style="display: flex;flex-direction: row;">
        <p style="flex: 2 ">
        Lamia permet d'importer les données de source variée de façon ergonomique, et permet 
        également l'export vers des formats variés (shapefile, rapports au format pdf, ...)
        </p>
        <div data-aos="flip-down"  data-aos-duration="1000" data-aos-anchor-placement="center-bottom"  
                style="flex: 1 ;margin: 20px;">
                <img height="75px" src="_static/presentation/importexport.png">
        </div>
    </div>

Gestion patrimoniale
----------------------------------------------------------------

.. raw:: html

    <div style="display: flex;flex-direction: row;">
        <p style="flex: 2 ">
        Lamia possède des modules d’import permettant 
        l’intégration de tout type de base de données des fournisseurs.
        Le module d’Analyse Multi-Critère (AMC) permet ensuite d’exploiter 
        ces données pour réaliser une priorisation des travaux à réaliser.
        </p>
        <div data-aos="flip-down"  data-aos-duration="1000" data-aos-anchor-placement="center-bottom"  
                style="flex: 1 ;margin: 20px;">
            <p>Todo</p>
        </div>
    </div>


Suivi de chantier
----------------------------------------------------------------

.. raw:: html

    <div style="display: flex;flex-direction: row;">
        <p style="flex: 2 ">
        Lamia permet le suivi de chantier avec un process de traçabilité 
        des non conformités :
        Description, proposition de l’entreprise, accord du MOE, 
        vérification sur site et levée de réserve.
        </p>
        <div data-aos="flip-down"  data-aos-duration="1000" data-aos-anchor-placement="center-bottom"  
                style="flex: 1 ;margin: 20px;">
            <img height="200px" src="_static/presentation/chantier.png">
        </div>
    </div>

… votre usage !
----------------------------------------------------------------

.. raw:: html

    <div style="display: flex;flex-direction: row;">
        <p style="flex: 2 ">
        Lamia est suffisamment généraliste pour s’adapter à tout usage associé à la gestion 
        d’infrastructure linéaire. Exprimez-nous vos besoins et nous étudierons l’intégration 
        de nouveaux usages dans LAMIA !
        </p>
        <div data-aos="flip-down"  data-aos-duration="1000" data-aos-anchor-placement="center-bottom" 
                style="flex: 1 ;margin: 20px;">
            <img height="200px" src="_static/presentation/usersatisfaction.png">
        </div>
    </div>



Open Source
==============================

Le projet LAMIA est développé et maintenu par ARTELIA et diffusé sous licence GNU GPL v3 
(ou postérieure). 

.. comment header
.. 1 : ####
.. 2 : ****
.. 3 : ====
.. 4 : ----

