# -*- coding: utf-8 -*-
import os
import json
import uuid
import shutil
from datetime import datetime
import requests, urllib3

from qgis.core import QgsGeometry

from Lamia.api.libs.cloudant.client import Cloudant
from Lamia.api.libs.cloudant.error import CloudantException
from Lamia.api.libs.cloudant.result import Result, ResultByKey, QueryResult
from Lamia.api.libs.cloudant.query import Query

# from Lamia.main.DBaseParser import DBaseParser

"""
try:
    from pyspatialite import dbapi2 as db
    from pyspatialite.dbapi2 import *
except ImportError:
    import sqlite3
    from sqlite3 import *

    print("spatialite not enabled")
"""

user = "geouser"
pwd = "geopw"
ip = "127.0.0.1"
port = "5984"
nom_sirs = "test_lamia"
nom_sirs_exp = "test"
nom_sirs_img = "M://FR//ECH//841_RER//MISSIONS//8411754_74_SM3A VTA_PRD//03_donnees//02_client//Donnees_photos_SM3A_2019_01"
nom_sql = "C://Users//Aurelien.perrin//Documents//DONNEES//Lamia//Lamia//bdd//export_sirs_v2.sqlite"

# parsertemp = DBaseParser(None)

"""
Recherche une valeur dans une base CouchDB
:param db: BDD CouchDB
:param limit: Nombre d'enregistrements sur lesquels effectuer la recherche
:param val: valeur à rechercher
"""


class SirsConverter:
    def __init__(self, dbaseparser):
        self.parsertemp = dbaseparser
        self.sirsconnectiondict = {
            "user": None,
            "password": None,
            "ip": None,
            "port": None,
            "dbname": None,
        }

        self.client = None
        self.my_db = None

    def find_val(self, db=None, limit=1000000, val=None):
        if not db:
            self.client, self.my_db = self.getSirsConnection()

        """
        if not db:
            client = Cloudant(user, pwd, url="http://" + ip + ":" + port)
            client.connect()
            my_db = client[nom_sirs]
        else:
            my_db = db
        """

        result_collection = Result(self.my_db.all_docs, include_docs=True)
        i = 0
        for r in result_collection:
            i += 1
            if "doc" in r.keys():
                for k in r["doc"].keys():
                    if r["doc"][k] == val:
                        print(r["doc"])
            if i == limit:
                break

        if not db:
            # self.client.disconnect()
            self.disconnectSirs()

    """
    Retourne toutes les clés existantes d'une base CouchDB
    :param db: BDD CouchDB
    :param limit: Nombre d'enregistrements sur lesquels effectuer la recherche
    :return: liste contenant toutes les clés de la BDD
    """

    # not used
    def lst_keys(self, db=None, limit=1000000):

        if not db:
            self.client, self.my_db = self.getSirsConnection()

        """
        if not db:
            client = Cloudant(user, pwd, url="http://" + ip + ":" + port)
            client.connect()
            my_db = client[nom_sirs]
        else:
            my_db = db
        """

        lst_keys = []

        result_collection = Result(self.my_db.all_docs, include_docs=True)
        i = 0
        for r in result_collection:
            i += 1
            if "doc" in r.keys():
                for k in r["doc"].keys():
                    if k not in lst_keys:
                        lst_keys.append(k)
                        print(k)
            if i == limit:
                break

        if not db:
            # self.client.disconnect()
            self.disconnectSirs()

        return lst_keys

    """
    Retourne toutes les classes existantes d'une base CouchDB
    :param db: BDD CouchDB
    :param limit: Nombre d'enregistrements sur lesquels effectuer la recherche
    :return: liste contenant toutes les classes de la BDD
    """
    # not used
    def lst_class(self, db=None, limit=1000000):

        if not db:
            self.client, self.my_db = self.getSirsConnection()

        """
        if not db:
            client = Cloudant(user, pwd, url="http://" + ip + ":" + port)
            client.connect()
            my_db = client[nom_sirs]
        else:
            my_db = db
        """

        lst_class = []

        result_collection = Result(self.my_db.all_docs, include_docs=True)
        i = 0
        for r in result_collection:
            i += 1
            if "doc" in r.keys():
                if "@class" in r["doc"].keys():
                    if r["doc"]["@class"] not in lst_class:
                        lst_class.append(r["doc"]["@class"])
            if i == limit:
                break

        if not db:
            # self.client.disconnect()
            self.disconnectSirs()

        return lst_class

    """
    Recherche toutes les valeurs possibles pour une classe donnée
    :param db: BDD CouchDB
    :param clas: Liste des classes sur lesquelles effectuer la recherche
    :param limit: Nombre d'enregistrements sur lesquels effectuer la recherche
    """
    # not used
    def lst_val_class(self, db=None, clas=[], limit=1000000):

        if not db:
            self.client, self.my_db = self.getSirsConnection()

        """
        if not db:
            client = Cloudant(user, pwd, url="http://" + ip + ":" + port)
            client.connect()
            my_db = client[nom_sirs]
        else:
            my_db = db
        """

        for c in clas:
            print(c)
            print("------------------------------------")
            query_collection = Query(
                self.my_db, selector={"@class": "fr.sirs.core.model.{}".format(c)}
            )
            for doc in query_collection(limit=limit, skip=0)["docs"]:
                print("{}|{}".format(doc["libelle"], doc["_id"]))
            print("------------------------------------")
            print("------------------------------------")

    """
    Recherche toutes les clés possibles pour une classe donnée
    :param db: BDD CouchDB
    :param clas: Liste des classes sur lesquelles effectuer la recherche
    :param limit: Nombre d'enregistrements sur lesquels effectuer la recherche
    """
    # not used
    def lst_key_class(self, db=None, clas=[], limit=1000000):

        if not db:
            self.client, self.my_db = self.getSirsConnection()

        """
        if not db:
            client = Cloudant(user, pwd, url="http://" + ip + ":" + port)
            client.connect()
            my_db = client[nom_sirs]
        else:
            my_db = db
        """

        for c in clas:
            print(c)
            print("------------------------------------")
            query_collection = Query(
                self.my_db, selector={"@class": "fr.sirs.core.model.{}".format(c)}
            )
            for doc in query_collection(limit=limit, skip=0)["docs"]:
                for k in doc.keys():
                    if k not in lst_keys:
                        lst_keys.append(k)
                        print(k)
            print("------------------------------------")
            print("------------------------------------")

    """
    Recherche toutes les clés possibles pour une "sous-classe"
    :param db: BDD CouchDB
    :param clas: Liste des classes et sous-classes sur lesquelles effectuer la recherche
    :param limit: Nombre d'enregistrements sur lesquels effectuer la recherche
    """
    # not used
    def lst_key_ss_class(self, db=None, clas=[], limit=1000000):

        if not db:
            self.client, self.my_db = self.getSirsConnection()

        """
        if not db:
            client = Cloudant(user, pwd, url="http://" + ip + ":" + port)
            client.connect()
            my_db = client[nom_sirs]
        else:
            my_db = db
        """

        for c in clas:
            lst_keys = []
            print(c)
            print("------------------------------------")
            query_collection = Query(
                self.my_db, selector={"@class": "fr.sirs.core.model.{}".format(c[0])}
            )
            for doc in query_collection(limit=limit, skip=0)["docs"]:
                if c[1] in doc.keys():
                    lst_ss_doc = doc[c[1]]
                    for ss_doc in lst_ss_doc:
                        for k in ss_doc.keys():
                            if k not in lst_keys:
                                lst_keys.append(k)
                                print(k)
            print("------------------------------------")
            print("------------------------------------")

    """
    Recherche toutes les clés possibles pour une "sous-sous-classe"
    :param db: BDD CouchDB
    :param clas: Liste des classes, sous-classes et sous-sous-classes sur lesquelles effectuer la recherche
    :param limit: Nombre d'enregistrements sur lesquels effectuer la recherche
    """
    # not used
    def lst_key_ss_ss_class(self, db=None, clas=[], limit=1000000):

        if not db:
            self.client, self.my_db = self.getSirsConnection()

        """
        if not db:
            client = Cloudant(user, pwd, url="http://" + ip + ":" + port)
            client.connect()
            my_db = client[nom_sirs]
        else:
            my_db = db
        """

        for c in clas:
            lst_keys = []
            print("------------------------------------")
            query_collection = Query(
                self.my_db, selector={"@class": "fr.sirs.core.model.{}".format(c[0])}
            )
            for doc in query_collection(limit=limit, skip=0)["docs"]:
                if c[1] in doc.keys():
                    lst_ss_doc = doc[c[1]]
                    for ss_doc in lst_ss_doc:
                        if c[2] in ss_doc.keys():
                            lst_ss_ss_doc = ss_doc[c[2]]
                            for ss_ss_doc in lst_ss_ss_doc:
                                for k in ss_ss_doc.keys():
                                    if k not in lst_keys:
                                        lst_keys.append(k)
                                        print(k)
            print("------------------------------------")
            print("------------------------------------")

    """
    Construction de la requête SQL permettant l'enregistrement d'un document
    :param doc: Document CouchDB à traiter
    :param param: Paramètres définis dans le fichier JSON de configuration, pour la classe à laquelle appartient l'objet
    :param vars: Dico de variables relatives au document courant, renseignées au cours du traitement
    :param dico_id: Dico de correspondance entre les identifiants SIRS et LAMIA
    :return: Champs à insérer dans la requête, Valeurs à insérer dans la requête, Lien vers image si existant
    """

    def analyse_param(self, doc, param, vars, dico_id):
        txt_fld = ""
        txt_val = ""
        img = None
        for p in param:
            val = None
            if (
                "var" in p.keys()
            ):  # Si il s'agit d'une variable générée par le programme, on cherche sa valeur dans le dico
                if p["var"] in vars.keys():
                    val = vars[p["var"]]
            if (
                "sirs" in p.keys()
            ):  # Si il s'agit d'une valeur contenue dans la BDD SIRS, on cherche sa valeur dans le document
                if p["sirs"] in doc.keys():
                    if (
                        "dico_id" in p.keys()
                    ):  # Si il s'agit d'un identifiant, on cherche sa correspondance dans le dico
                        if isinstance(doc[p["sirs"]], list):
                            id_tmp = doc[p["sirs"]][0]
                        else:
                            id_tmp = doc[p["sirs"]]
                        if id_tmp in dico_id.keys():
                            if p["dico_id"] in dico_id[id_tmp].keys():
                                val = dico_id[id_tmp][p["dico_id"]]
                    else:  # Sinon, on récupère directement la valeur
                        val = doc[p["sirs"]]
            if (
                "value" in p.keys()
            ):  # Si il s'agit d'une valeur fixée, on récupère celle ci dans les paramètres
                val = p["value"]

            if val is not None:  # Formatage des valeurs en fonction du type renseigné
                if p["type"] == "str":
                    val = '"{}"'.format(str(val).replace('"', '""'))
                if p["type"] == "img":
                    img = val
                    val = '".\media\{}"'.format(str(val).replace('"', '""'))
                if p["type"] == "date":
                    if len(val) == 19:
                        val = '"{}"'.format(str(val).replace('"', '""'))
                    elif len(val) == 10:
                        val = '"{} 00:00:00"'.format(str(val).replace('"', '""'))
                elif p["type"] == "geomL":
                    val = 'GeomFromText("{}", {})'.format(val, 2154)
                elif p["type"] == "geomP":
                    if val[0:7] == "POINT (":
                        val = 'GeomFromText("{}", {})'.format(val, 2154)
                    if val[0:12] == "LINESTRING (":
                        coord = val.split("(")[1].split(")")[0]
                        lst_coord = coord.split(", ")
                        val = 'GeomFromText("POINT ({})", {})'.format(
                            lst_coord[(len(lst_coord) - 1) // 2], 2154
                        )
                txt_fld = "{}{}, ".format(txt_fld, p["lamia"])
                txt_val = "{}{}, ".format(txt_val, val)

        return txt_fld[:-2], txt_val[:-2], img

    """
    Execution de la requête SQL permettant l'enregistrement d'un document
    :param doc: Document CouchDB à traiter
    :param rs: Curseur pointant vers la BDD SQLIte
    :param tab: Table dans laquelle insérer le document
    :param param: Paramètres définis dans le fichier JSON de configuration, pour la classe à laquelle appartient l'objet
    :param vars: Dico de variables relatives au document courant, renseignées au cours du traitement
    :param dico_id: Dico de correspondance entre les identifiants SIRS et LAMIA
    :param rep_res_lamia: Répertoire où sont enregistrées les ressources LAMIA
    :return: Identifiant de l'objet créé
    """

    def lamia_insert(self, doc, rs, tab, param, vars, dico_id, rep_res_lamia=None):
        tf, tv, img = self.analyse_param(doc, param, vars, dico_id)
        sql = "INSERT INTO {} ({}) VALUES ({})".format(tab, tf, tv)
        rs.execute(sql)
        last_id = rs.lastrowid
        if img:
            img_sirs = os.path.join(nom_sirs_img, img)
            img_lamia = os.path.join(
                os.path.dirname(nom_sql), rep_res_lamia, "media", img
            )
            self.parsertemp.copyRessourceFile(img_sirs, img_lamia, withthumbnail=1)
        return last_id

    """
    Traitement des observations contenues dans un document
    :param obs: Observation CouchDB à traiter
    :param rs: Curseur pointant vers la BDD SQLIte
    :param param_obs: Paramètres définis dans le fichier JSON de configuration, pour la classe à laquelle appartient l'objet
    :param vars: Dico de variables relatives au document courant, renseignées au cours du traitement
    :param dico_id: Dico de correspondance entre les identifiants SIRS et LAMIA
    """

    def import_obs(self, obs, rs, param_obs, vars, dico_id):
        vars["$id_sirs_cur_obs"] = obs[param_obs["id"]]
        dico_id[vars["$id_sirs_cur_obs"]] = {}
        if param_obs["create_obj"]:
            vars["$id_obj_cur_obs"] = self.lamia_insert(
                obs, rs, "object", param_obs["create_obj"], vars, dico_id
            )
            dico_id[vars["$id_sirs_cur_obs"]]["id_obj"] = vars["$id_obj_cur_obs"]
        if param_obs["insert_lamia"]:
            vars["$id_elem_cur_obs"] = self.lamia_insert(
                obs,
                rs,
                param_obs["insert_lamia"]["tab"],
                param_obs["insert_lamia"]["fld"],
                vars,
                dico_id,
            )
            dico_id[vars["$id_sirs_cur_obs"]]["id_elem"] = vars["$id_elem_cur_obs"]

    """
    Traitement des photos contenues dans un document
    :param pho: Photo CouchDB à traiter
    :param rs: Curseur pointant vers la BDD SQLIte
    :param param_pho: Paramètres définis dans le fichier JSON de configuration, pour la classe à laquelle appartient l'objet
    :param vars: Dico de variables relatives au document courant, renseignées au cours du traitement
    :param dico_id: Dico de correspondance entre les identifiants SIRS et LAMIA
    :param rep_res_lamia: Répertoire où sont enregistrées les ressources LAMIA
    """

    def import_pho(self, pho, rs, param_pho, vars, dico_id, rep_res_lamia):
        vars["$id_sirs_cur_pho"] = pho[param_pho["id"]]
        dico_id[vars["$id_sirs_cur_pho"]] = {}
        if param_pho["create_obj"]:
            vars["$id_obj_cur_pho"] = self.lamia_insert(
                pho, rs, "object", param_pho["create_obj"], vars, dico_id
            )
            dico_id[vars["$id_sirs_cur_pho"]]["id_obj"] = vars["$id_obj_cur_pho"]
        if param_pho["create_res"]:
            vars["$id_res_cur_pho"] = self.lamia_insert(
                pho,
                rs,
                "resource",
                param_pho["create_res"],
                vars,
                dico_id,
                rep_res_lamia,
            )
            dico_id[vars["$id_sirs_cur_pho"]]["id_res"] = vars["$id_res_cur_pho"]
        if param_pho["create_obj_res"]:
            self.lamia_insert(
                pho, rs, "tcobjectresource", param_pho["create_obj_res"], vars, dico_id
            )
        if param_pho["insert_lamia"]:
            vars["$id_elem_cur_pho"] = self.lamia_insert(
                pho,
                rs,
                param_pho["insert_lamia"]["tab"],
                param_pho["insert_lamia"]["fld"],
                vars,
                dico_id,
            )
            dico_id[vars["$id_sirs_cur_pho"]]["id_elem"] = vars["$id_elem_cur_pho"]

    """
    Import d'une BDD SIRS vers Lamia
    :param only_valid: Import seulement des documents validés si True
    """

    def getSirsConnection(self):
        """Return Cloudant instances for connection
        need self.sirsconnectiondict to be defined

        :return: cloudant client and database
        """

        url = (
            "http://"
            + self.sirsconnectiondict["ip"]
            + ":"
            + self.sirsconnectiondict["port"]
        )

        client = Cloudant(
            self.sirsconnectiondict["user"],
            self.sirsconnectiondict["password"],
            url=url,
        )

        try:
            client.connect()
        except requests.exceptions.InvalidURL:
            return None, "Invalid url" + url
        except urllib3.exceptions.NewConnectionError:
            return None, "getaddrinfo failed"
        except requests.exceptions.ConnectionError:
            return None, "ConnectionError with url : " + url
        except urllib3.exceptions.MaxRetryError:
            return None, "Max retries exceeded with url : " + url

        my_db = client[self.sirsconnectiondict["dbname"]]

        return client, my_db

    def disconnectSirs(self):
        """Disconnect cloudant client
        """
        if self.client:
            self.client.disconnect()
            self.client = None
            self.my_db = None

    def import_sirs(self, only_valid=True):
        # Ouverture du fichier de config
        config_path = os.path.join(os.path.dirname(__file__), "config_apn.json")
        config = json.load(open(config_path, "r"))

        # Connexion à la base SQLIte
        """
        bdd_sql = sqlite3.connect(nom_sql)
        bdd_sql.enable_load_extension(True)
        bdd_sql.load_extension("mod_spatialite")
        """

        bdd_sql = self.parsertemp.connSLITE
        rs = bdd_sql.cursor()

        # rs.execute("SELECT repertoireressources FROM Basedonnees")
        # row = rs.fetchone()
        # rep_res_lamia = row[0]

        rep_res_lamia = self.parsertemp.dbaseressourcesdirectory

        # Connexion à la base CouchDB
        """
        client = Cloudant(user, pwd, url="http://" + ip + ":" + port)
        client.connect()
        my_db = client[nom_sirs]
        """

        self.client, self.my_db = self.getSirsConnection()

        if self.client is None:
            print("Failed to connect")
            return

        """
        # Réinitialisation de la base SQLite
        tabs = [
            "object",
            "descriptionsystem",
            "edge",
            "equipment",
            "deficiency",
            "observation",
            "resource",
            "media",
            "tcobjectresource",
        ]
        for t in tabs:
            rs.execute("DELETE FROM {}".format(t))
            rs.execute('DELETE FROM sqlite_sequence WHERE name = "{}"'.format(t))
        """
        # Récupération des paramètres relatifs aux observation et aux photos
        param_obs = config["ss_table"]["observations"]
        param_pho = config["ss_table"]["photos"]

        dico_id = {}

        # Pour chacune des classes à importer
        for nm_class, param in config["import_table"].items():
            # Construction d'un "selecteur" permettant de filtrer la BDD SIRS
            selector = {"@class": "fr.sirs.core.model.{}".format(nm_class)}
            if only_valid:
                selector["valid"] = True

            # Requête récupérant les documents de la BDD SIRS pour la classe courante
            query_collection = Query(self.my_db, selector=selector)

            # Pour chacun des documents récupérés
            for doc in query_collection(limit=1000000, skip=0)["docs"]:
                vars = dict()
                vars["$id_sirs"] = doc[param["id"]]
                dico_id[vars["$id_sirs"]] = {}
                if param[
                    "create_obj"
                ]:  # Créé un enregistrement dans la table Objet si nécessaire
                    vars["$id_obj"] = self.lamia_insert(
                        doc, rs, "object", param["create_obj"], vars, dico_id
                    )
                    dico_id[vars["$id_sirs"]]["id_obj"] = vars["$id_obj"]
                if param[
                    "create_des"
                ]:  # Créé un enregistrement dans la table descriptionsystem si nécessaire
                    vars["$id_des"] = self.lamia_insert(
                        doc, rs, "descriptionsystem", param["create_des"], vars, dico_id
                    )
                    dico_id[vars["$id_sirs"]]["id_des"] = vars["$id_des"]
                if param[
                    "insert_lamia"
                ]:  # Créé un enregistrement dans la table propre à la classe courante
                    vars["$id_elem"] = self.lamia_insert(
                        doc,
                        rs,
                        param["insert_lamia"]["tab"],
                        param["insert_lamia"]["fld"],
                        vars,
                        dico_id,
                    )
                    dico_id[vars["$id_sirs"]]["id_elem"] = vars["$id_elem"]
                if (
                    "observations" in doc.keys()
                ):  # Traitement des observations liées au document courant
                    lst_obs = doc["observations"]
                    for obs in lst_obs:
                        if param["import_obs"]:
                            self.import_obs(obs, rs, param_obs, vars, dico_id)
                        if "photos" in obs.keys():
                            lst_pho = obs["photos"]
                            for pho in lst_pho:
                                if param["import_pho"]:
                                    self.import_pho(
                                        pho, rs, param_pho, vars, dico_id, rep_res_lamia
                                    )
                if (
                    "photos" in doc.keys()
                ):  # Traitement des photos liées au document courant
                    lst_pho = doc["photos"]
                    for pho in lst_pho:
                        if param["import_pho"]:
                            self.import_pho(
                                pho, rs, param_pho, vars, dico_id, rep_res_lamia
                            )

        # MAJ de la BDD Lamia
        for table in [
            "object",
            "descriptionsystem",
            "edge",
            "equipment",
            "deficiency",
            "observation",
            "resource",
            "media",
        ]:
            rs.execute(
                "UPDATE {t} SET id_{f} = pk_{f}".format(t=table, f=table.lower())
            )
        bdd_sql.commit()

        rs.execute("SELECT UpdateLayerStatistics()")
        bdd_sql.commit()

        # Deconnexions des 2 BDD
        # bdd_sql.close()
        # self.client.disconnect()
        self.disconnectSirs()

    """
    Export d'une BDD LAMIA vers SIRS
    """

    def export_lamia(self, export_img=True):
        # Ouverture du fichier de config
        config_path = os.path.join(os.path.dirname(__file__), "config_apn.json")
        config = json.load(open(config_path, "r"))

        # Connexion à la base SQLIte
        """
        bdd_sql = sqlite3.connect(nom_sql)
        bdd_sql.enable_load_extension(True)
        bdd_sql.load_extension("mod_spatialite")
        rs = bdd_sql.cursor()
        """
        bdd_sql = self.parsertemp.connSLITE
        rs = bdd_sql.cursor()

        """
        rs.execute("SELECT repertoireressources FROM Basedonnees")
        row = rs.fetchone()
        rep_res_lamia = row[0]
        """

        rep_res_lamia = self.parsertemp.dbaseressourcesdirectory

        # Connexion à la base CouchDB
        """
        client = Cloudant(user, pwd, url="http://" + ip + ":" + port)
        client.connect()
        my_db = client[nom_sirs_exp]
        """

        self.client, self.my_db = self.getSirsConnection()

        if self.client is None:
            print("Failed to connect")
            return

        # Récupération des paramètres relatifs aux observation et aux photos
        param_obs = config["ss_table"]["observations"]
        param_pho = config["ss_table"]["photos"]

        # Pour test, à supprimer par la suite (permet de considérer comme non traités les objets précédemment exportés, afin de les exporter à nouveau)
        rs.execute(
            "UPDATE object SET importid = Null, importtable = Null WHERE importid = 1"
        )
        bdd_sql.commit()

        # Création d'un dictionnaire de correspondance entre les IDs Lamia & les IDs SIRS (pour les tronçons)
        dico_infra = dict()
        sql = "SELECT pk_edge, importtable FROM edge_qgis"
        rows = self.parsertemp.query(sql)
        """
        rs.execute(
            "SELECT pk_edge, importtable FROM (object INNER JOIN descriptionsystem ON object.pk_object = descriptionsystem.lpk_object) "
            "INNER JOIN edge ON descriptionsystem.pk_descriptionsystem = edge.lpk_descriptionsystem"
        )
        rows = rs.fetchall()
        """
        for row in rows:
            dico_infra[row[0]] = row[1]

        # Création d'un dictionnaire rattachant chaque équipement/désordre à un tronçon
        dico_lnk_obj_infra = dict()
        rs.execute(
            "SELECT object.pk_object as id_des, edge.pk_edge as id_infra, MIN(ST_Distance(deficiency.geom, edge.geom)) as dist "
            "FROM deficiency INNER JOIN object ON deficiency.lpk_object = object.pk_object, edge WHERE object.importtable is Null GROUP BY id_des"
        )
        rows = rs.fetchall()
        rs.execute(
            "SELECT object.pk_object as id_equip, edge.pk_edge as id_infra, MIN(ST_Distance(equipment.geom, edge.geom)) as dist "
            "FROM (equipment INNER JOIN descriptionsystem ON equipment.lpk_descriptionsystem = descriptionsystem.pk_descriptionsystem) "
            "INNER JOIN object ON descriptionsystem.lpk_object = object.pk_object, edge WHERE object.importtable is Null GROUP BY id_equip"
        )
        rows.extend(rs.fetchall())
        for row in rows:
            dico_lnk_obj_infra[row[0]] = row[1]

        # Création de l'utilisateur qui servira pour l'export
        id_usr = "{}".format(uuid.uuid4().hex)
        usr = dict()
        usr["@class"] = "fr.sirs.core.model.Utilisateur"
        usr["_id"] = id_usr
        usr["designation"] = "ARTELIA {}".format(
            datetime.now().strftime("%Y%m%d%H%M%S")
        )
        usr["valid"] = True
        self.my_db.create_document(usr)

        # Pour chacune des classes à exporter
        class_to_import = config["import_table"].copy()
        class_to_import["Observation"] = param_obs
        for nm_class, param in class_to_import.items():
            if param["export"]["obj"]:
                l = []
                # Récupération des paramètres nécessaires à l'export pour chaque classe
                sql_txt, fld_sirs, fld_type, is_geom = self.create_qry_export(
                    nm_class, param
                )
                rs.execute(sql_txt)
                rows = rs.fetchall()
                for row in rows:
                    # Récupération des données pour chaque enregistrement
                    rec = dict()
                    rec["@class"] = "fr.sirs.core.model.{}".format(nm_class)
                    rec[param["id"]] = "{}".format(uuid.uuid4().hex)
                    rec["valid"] = True
                    rec["author"] = id_usr
                    for c, val in enumerate(row):
                        if val not in [None, ""]:
                            if fld_type[c] == "date":
                                rec[fld_sirs[c]] = val[0:10]
                            elif fld_type[c] == "img":
                                rec[fld_sirs[c]] = val.replace(".\\media\\", "")
                            else:
                                rec[fld_sirs[c]] = val
                    # Traitement de la géométrie
                    if is_geom:
                        self.init_geom(rec)
                        rec["linearId"] = "{}".format(
                            dico_infra[dico_lnk_obj_infra[rec["#id_lamia_obj"]]]
                        )
                        rec["foreignParentId"] = "{}".format(
                            dico_infra[dico_lnk_obj_infra[rec["#id_lamia_obj"]]]
                        )
                        (
                            rec["geometry"],
                            rec["positionDebut"],
                            rec["positionFin"],
                        ) = self.create_sirs_geom(
                            bdd_sql,
                            nm_class,
                            rec["#id_lamia"],
                            dico_lnk_obj_infra[rec["#id_lamia_obj"]],
                        )
                    l.append(rec)
                    # Mise à jour de l'enregistrement dans Lamia, renseignement de l'ID SIRS créé
                    rs.execute(
                        "UPDATE object SET importid = 1, importtable = '{s}' WHERE pk_object = {l}".format(
                            s=rec[param["id"]], l=rec["#id_lamia_obj"]
                        )
                    )

                # Export des données dans SIRS
                for data in l:
                    if nm_class == "Observation":
                        id_desordre = data["#id_desordre"]

                    self.clean_data(data)

                    if nm_class == "Observation":
                        doc_desordre = self.my_db[id_desordre]
                        if "observations" in doc_desordre.keys():
                            doc_desordre["observations"].append(data)
                        else:
                            doc_desordre["observations"] = [data]
                        doc_desordre.save()
                    else:
                        self.my_db.create_document(data)

        # Export des photos (différentes classes en fonction du type d'objet auquel la photo est rattachée)
        for nm_class in ["PhotoTroncon", "PhotoEquip", "PhotoObs"]:
            param = param_pho
            if param["export"]["obj"]:
                l = []
                # Récupération des paramètres nécessaires à l'export pour chaque classe
                sql_txt, fld_sirs, fld_type, is_geom = self.create_qry_export(
                    nm_class, param
                )
                rs.execute(sql_txt)
                rows = rs.fetchall()
                for row in rows:
                    # Récupération des données pour chaque enregistrement
                    rec = dict()
                    rec["@class"] = "fr.sirs.core.model.Photo"
                    rec[param["id"]] = "{}".format(uuid.uuid4().hex)
                    rec["valid"] = True
                    rec["author"] = id_usr
                    for c, val in enumerate(row):
                        if val not in [None, ""]:
                            if fld_type[c] == "date":
                                rec[fld_sirs[c]] = val[0:10]
                            elif fld_type[c] == "img":
                                rec[fld_sirs[c]] = val.replace(".\\media\\", "")
                            else:
                                rec[fld_sirs[c]] = val
                    # Traitement de la géométrie
                    if is_geom:
                        self.init_geom(rec)
                        if nm_class == "PhotoTroncon":
                            tronc_sirs = rec["#id_troncon"]
                            tronc_lamia = rec["#id_lamia_troncon"]
                        elif nm_class == "PhotoEquip":
                            tronc_sirs = "{}".format(
                                dico_infra[dico_lnk_obj_infra[rec["#id_lamia_equip"]]]
                            )
                            tronc_lamia = dico_lnk_obj_infra[rec["#id_lamia_equip"]]
                        elif nm_class == "PhotoObs":
                            tronc_sirs = "{}".format(
                                dico_infra[dico_lnk_obj_infra[rec["#id_lamia_des"]]]
                            )
                            tronc_lamia = dico_lnk_obj_infra[rec["#id_lamia_des"]]
                        rec["linearId"] = tronc_sirs
                        rec["foreignParentId"] = tronc_sirs
                        (
                            rec["geometry"],
                            rec["positionDebut"],
                            rec["positionFin"],
                        ) = self.create_sirs_geom(
                            bdd_sql, nm_class, rec["#id_lamia"], tronc_lamia
                        )
                    l.append(rec)
                    # Mise à jour de l'enregistrement dans Lamia, renseignement de l'ID SIRS créé
                    rs.execute(
                        "UPDATE object SET importid = 1, importtable = '{s}' WHERE pk_object = {l}".format(
                            s=rec[param["id"]], l=rec["#id_lamia_obj"]
                        )
                    )
                # Export des données dans SIRS
                for data in l:
                    if nm_class == "PhotoTroncon":
                        id_objet = data["#id_troncon"]
                        id_obs = None
                    elif nm_class == "PhotoEquip":
                        id_objet = data["#id_equip"]
                        id_obs = None
                    elif nm_class == "PhotoObs":
                        id_objet = data["#id_des"]
                        id_obs = data["#id_obs"]

                    self.clean_data(data)

                    doc = self.my_db[id_objet]
                    if id_obs:
                        for d in doc["observations"]:
                            if d["id"] == id_obs:
                                res = d
                                break
                    else:
                        res = doc

                    if "photos" in res.keys():
                        res["photos"].append(data)
                    else:
                        res["photos"] = [data]
                    doc.save()

                    # Copie du fichier photo dans le répertoire SIRS
                    if export_img:
                        img_lamia = os.path.join(
                            os.path.dirname(nom_sql),
                            rep_res_lamia,
                            "media",
                            data["chemin"],
                        )
                        img_sirs = os.path.join(nom_sirs_img, data["chemin"])
                        destinationdir = os.path.dirname(img_sirs)
                        if os.path.exists(img_lamia):
                            if not os.path.exists(destinationdir):
                                os.makedirs(destinationdir)
                            shutil.copy(img_lamia, img_sirs)

        bdd_sql.commit()

        # Deconnexions des 2 BDD
        # bdd_sql.close()
        # self.client.disconnect()
        self.disconnectSirs()

    """
    Nettoyage des données avant leur export dans SIRS
    :param data: Données à nettoyer
    """

    def clean_data(self, data):
        # Suppression des champs non utiles dans SIRS
        l_key_del = []
        for key in data.keys():
            if key[0] == "#":
                l_key_del.append(key)

        for key_del in l_key_del:
            del data[key_del]

    """
    Initialisation des paramètres communs liés à la géométrie des objets
    :param rec: Enregistrement à initialiser
    """

    def init_geom(self, rec):
        rec["borne_debut_aval"] = False
        rec["borne_debut_distance"] = 0
        rec["prDebut"] = 0
        rec["borne_fin_aval"] = False
        rec["borne_fin_distance"] = 0
        rec["prFin"] = 0
        rec["geometryMode"] = "LINEAR"  #'COORD'

    """
    Création de la géométrie au format SIRS avec les outils QGIS
    :param bdd: BDD Lamia
    :param nm_class: Classe de l'objet dont la géométrie est à créer
    :param id_obj: Identifiant de l'objet dont la géométrie est à créer
    :param id_infra: Identifiant du tronçon auquel est rattaché l'objet
    :return: Géométrie au format SIRS, Premier noeud de la géométrie, Dernier noeud de la géométrie
    """

    def create_sirs_geom(self, bdd, nm_class, id_obj, id_infra):
        dst_min, dst_max, param_min, param_max = None, None, None, None
        if nm_class == "Desordre":
            table = "deficiency"
            fld = "pk_deficiency"
        elif nm_class[0:5] == "Photo":
            table = "media"
            fld = "pk_media"
        else:
            table = "equipment"
            fld = "pk_equipment"

        # Récupération de la géométrie du tronçon
        rs = bdd.cursor()
        rs.execute("SELECT ASTEXT(geom) FROM edge WHERE pk_edge = {}".format(id_infra))
        row = rs.fetchone()
        geom_infra = QgsGeometry.fromWkt(row[0])
        long_infra = geom_infra.length()
        poly_infra = geom_infra.asPolyline()

        # Récupération de la géométrie de l'objet à projeter
        rs.execute(
            "SELECT ASTEXT(geom), ST_GeometryType(geom) FROM {t} WHERE {f} = {i}".format(
                t=table, f=fld, i=id_obj
            )
        )
        row = rs.fetchone()
        geom_equip = QgsGeometry.fromWkt(row[0])
        type_geom_equip = row[1]
        rs.close()

        # Récupération des noeuds de l'objet à projeter
        if type_geom_equip == "LINESTRING":
            lst_pts = geom_equip.asPolyline()
        elif type_geom_equip == "POINT":
            lst_pts = [geom_equip.asPoint()]

        # Recherche des extrémités de l'objet projeté
        for pt in lst_pts:
            p = QgsGeometry.fromPointXY(pt)
            dst_tmp = geom_infra.lineLocatePoint(p)
            if (dst_min is None) or (dst_tmp < dst_min):
                (
                    sqdist,
                    projpoint,
                    aftervertex,
                    leftOf,
                ) = geom_infra.closestSegmentWithContext(pt)
                param_min = {"pt_prj": projpoint, "vrtx": aftervertex}
                dst_min = dst_tmp
            if (dst_max is None) or (dst_tmp > dst_max):
                (
                    sqdist,
                    projpoint,
                    aftervertex,
                    leftOf,
                ) = geom_infra.closestSegmentWithContext(pt)
                param_max = {"pt_prj": projpoint, "vrtx": aftervertex}
                dst_max = dst_tmp

        # Création de l'objet projeté
        if dst_max < long_infra:
            poly_infra = poly_infra[: param_max["vrtx"]]
            poly_infra.append(param_max["pt_prj"])
        if dst_min > 0.0:
            poly_infra = poly_infra[param_min["vrtx"] :]
            poly_infra.insert(0, param_min["pt_prj"])

        pline_txt = QgsGeometry.fromPolylineXY(poly_infra).asWkt()
        ptdeb_txt = QgsGeometry.fromPointXY(poly_infra[0]).asWkt()
        ptfin_txt = QgsGeometry.fromPointXY(poly_infra[-1]).asWkt()

        return pline_txt, ptdeb_txt, ptfin_txt

    # def extractPoints( geom ):
    #     multi_geom = qgis.core.QgsGeometry()
    #     temp_geom = []
    #     if geom.type() == 0: # it's a point
    #         if geom.isMultipart():
    #             temp_geom = geom.asMultiPoint()
    #         else:
    #             temp_geom.append(geom.asPoint())
    #     elif geom.type() == 1: # it's a line
    #         if geom.isMultipart():
    #             multi_geom = geom.asMultiPolyline() #multi_geog is a multiline
    #             for i in multi_geom: #i is a line
    #                 temp_geom.extend( i )
    #         else:
    #             temp_geom = geom.asPolyline()
    #     elif geom.type() == 2: # it's a polygon
    #         if geom.isMultipart():
    #             multi_geom = geom.asMultiPolygon() #multi_geom is a multipolygon
    #             for i in multi_geom: #i is a polygon
    #                 for j in i: #j is a line
    #                     temp_geom.extend( j )
    #         else:
    #             multi_geom = geom.asPolygon() #multi_geom is a polygon
    #             for i in multi_geom: #i is a line
    #                 temp_geom.extend( i )
    #     return temp_geom

    """
    Création de la géométrie au format SIRS en SQL
    :param bdd: BDD Lamia
    :param nm_class: Classe de l'objet dont la géométrie est à créer
    :param id_obj: Identifiant de l'objet dont la géométrie est à créer
    :param id_infra: Identifiant du tronçon auquel est rattaché l'objet
    :return: Géométrie au format SIRS, Premier noeud de la géométrie, Dernier noeud de la géométrie
    """

    def create_sirs_geom_by_sql(self, bdd, nm_class, id_obj, id_infra):
        if nm_class == "Desordre":
            table = "deficiency"
            fld = "pk_deficiency"
        elif nm_class[0:5] == "Photo":
            table = "media"
            fld = "pk_media"
        else:
            table = "equipment"
            fld = "pk_equipment"

        rs = bdd.cursor()
        rs.execute(
            "SELECT "
            "CASE GeometryType(proj_geom) "
            "WHEN 'POINT' THEN ASTEXT(MakeLine(proj_geom, proj_geom)) "
            "WHEN 'LINESTRING' THEN ASTEXT(proj_geom) "
            "END geom_final, "
            "CASE GeometryType(proj_geom) "
            "WHEN 'POINT' THEN ASTEXT(proj_geom) "
            "WHEN 'LINESTRING' THEN AsTEXT(StartPoint(proj_geom)) "
            "END pos_deb, "
            "CASE GeometryType(proj_geom) "
            "WHEN 'POINT' THEN ASTEXT(proj_geom) "
            "WHEN 'LINESTRING' THEN AsTEXT(EndPoint(proj_geom)) "
            "END pos_fin "
            "FROM "
            "(SELECT {f}, "
            "CASE GeometryType({t}.geom) "
            "WHEN 'POINT' THEN (SELECT ClosestPoint(edge.geom, {t}.geom)) "
            "WHEN 'LINESTRING' THEN "
            "CASE StartPoint({t}.geom) "
            "WHEN EndPoint({t}.geom) THEN (SELECT ClosestPoint(edge.geom, StartPoint({t}.geom))) "
            "ELSE (SELECT Line_Substring(edge.geom, "
            "(SELECT Line_Locate_Point(edge.geom, StartPoint({t}.geom))), "
            "(SELECT Line_Locate_Point(edge.geom, EndPoint({t}.geom))))) "
            "END END proj_geom "
            "FROM {t}, edge "
            "WHERE {t}.{f} = {o} AND edge.pk_edge = {i})".format(
                t=table, f=fld, o=id_obj, i=id_infra
            )
        )
        row = rs.fetchone()
        rs.close
        return row[0], row[1], row[2]

    """
    Création de la requête permettant de récupérer les infos nécessaires à l'export vers SIRS, pour une classe donnée
    :param nm_class: Classe à traiter
    :param param: Paramètres de la classe à traiter, issus du fichier de config
    :return: Requête SQL à executer, Champs SIRS associés, Format des valeurs récupérées, Indique si une géométrie est à créer
    """

    def create_qry_export(self, nm_class, param):
        is_geom = False

        # Initialisation de la requête en fonction de la classe de l'objet
        if nm_class == "Observation":
            fld_sirs = ["#id_lamia_obj", "#id_desordre"]
            fld_type = ["int", "str"]
            sql_txt = "SELECT object.pk_object, obj_des.importtable"
        elif nm_class == "Desordre":
            fld_sirs = ["#id_lamia_obj", "#id_lamia"]
            fld_type = ["int", "int"]
            sql_txt = "SELECT object.pk_object, deficiency.pk_deficiency"
        elif nm_class == "PhotoTroncon":
            fld_sirs = [
                "#id_lamia_obj",
                "#id_lamia",
                "#id_lamia_troncon",
                "#id_troncon",
            ]
            fld_type = ["int", "int", "int", "str"]
            sql_txt = "SELECT object.pk_object, media.pk_media, tronc.pk_object, tronc.importtable"
        elif nm_class == "PhotoEquip":
            fld_sirs = ["#id_lamia_obj", "#id_lamia", "#id_lamia_equip", "#id_equip"]
            fld_type = ["int", "int", "int", "str"]
            sql_txt = "SELECT object.pk_object, media.pk_media, equip.pk_object, equip.importtable"
        elif nm_class == "PhotoObs":
            fld_sirs = [
                "#id_lamia_obj",
                "#id_lamia",
                "#id_lamia_des",
                "#id_des",
                "#id_obs",
            ]
            fld_type = ["int", "int", "int", "str", "str"]
            sql_txt = "SELECT object.pk_object, media.pk_media, des.pk_object, des.importtable, obs.importtable"
        else:
            fld_sirs = ["#id_lamia_obj", "#id_lamia"]
            fld_type = ["int", "int"]
            sql_txt = "SELECT object.pk_object, equipment.pk_equipment"

        # Récupération des valeurs contenues dans la table Objet
        if param["create_obj"]:
            for param_fld in param["create_obj"]:
                if param_fld["lamia"] == "geom":
                    is_geom = True
                if self.recup_fld(param_fld):
                    sql_txt = "{s}, object.{f}".format(s=sql_txt, f=param_fld["lamia"])
                    fld_sirs.append(param_fld["sirs"])
                    fld_type.append(param_fld["type"])

        # Récupération des valeurs contenues dans la table resource
        if param["create_res"]:
            for param_fld in param["create_res"]:
                if param_fld["lamia"] == "geom":
                    is_geom = True
                if self.recup_fld(param_fld):
                    sql_txt = "{s}, resource.{f}".format(
                        s=sql_txt, f=param_fld["lamia"]
                    )
                    fld_sirs.append(param_fld["sirs"])
                    fld_type.append(param_fld["type"])

        # Récupération des valeurs contenues dans la table associée à chaque classe
        if param["insert_lamia"]:
            for param_fld in param["insert_lamia"]["fld"]:
                if param_fld["lamia"] == "geom":
                    is_geom = True
                if self.recup_fld(param_fld):
                    sql_txt = "{s}, {t}.{f}".format(
                        s=sql_txt, t=param["insert_lamia"]["tab"], f=param_fld["lamia"]
                    )
                    fld_sirs.append(param_fld["sirs"])
                    fld_type.append(param_fld["type"])

        # Création du "FROM" de la requête en fonction de la classe de l'objet
        if nm_class == "Desordre":
            sql_txt = "{s} FROM object INNER JOIN {t} ON object.pk_object = {t}.lpk_object".format(
                s=sql_txt, t=param["insert_lamia"]["tab"]
            )
        elif nm_class == "Observation":
            sql_txt = (
                "{s} FROM ((deficiency INNER JOIN {t} ON deficiency.pk_deficiency = {t}.lid_deficiency) "
                "INNER JOIN object ON {t}.lpk_object = object.pk_object) "
                "INNER JOIN object as obj_des ON deficiency.lpk_object = obj_des.pk_object".format(
                    s=sql_txt, t=param["insert_lamia"]["tab"]
                )
            )
        elif nm_class == "PhotoTroncon":
            sql_txt = (
                "{s} FROM(((((media INNER JOIN resource ON media.lpk_resource = resource.pk_resource) "
                "INNER JOIN tcobjectresource ON resource.id_resource = tcobjectresource.lid_resource) "
                "INNER JOIN object as tronc ON tcobjectresource.lid_object = tronc.id_object) "
                "INNER JOIN object ON resource.lpk_object = object.pk_object) "
                "INNER JOIN descriptionsystem ON tronc.pk_object = descriptionsystem.lpk_object) "
                "INNER JOIN edge ON descriptionsystem.pk_descriptionsystem = edge.lpk_descriptionsystem".format(
                    s=sql_txt
                )
            )
        elif nm_class == "PhotoEquip":
            sql_txt = (
                "{s} FROM(((((media INNER JOIN resource ON media.lpk_resource = resource.pk_resource) "
                "INNER JOIN tcobjectresource ON resource.id_resource = tcobjectresource.lid_resource) "
                "INNER JOIN object as equip ON tcobjectresource.lid_object = equip.id_object) "
                "INNER JOIN object ON resource.lpk_object = object.pk_object) "
                "INNER JOIN descriptionsystem ON equip.pk_object = descriptionsystem.lpk_object) "
                "INNER JOIN equipment ON descriptionsystem.pk_descriptionsystem = equipment.lpk_descriptionsystem".format(
                    s=sql_txt
                )
            )
        elif nm_class == "PhotoObs":
            sql_txt = (
                "{s} FROM (((((((media INNER JOIN resource ON media.lpk_resource = resource.pk_resource) "
                "INNER JOIN tcobjectresource ON resource.id_resource = tcobjectresource.lid_resource) "
                "INNER JOIN object as obs ON tcobjectresource.lid_object = obs.id_object) "
                "INNER JOIN object ON resource.lpk_object = object.pk_object) "
                "INNER JOIN Observation ON obs.pk_object = Observation.lpk_object) "
                "INNER JOIN deficiency ON deficiency.id_deficiency = Observation.lid_deficiency)"
                "INNER JOIN object as des ON deficiency.lpk_object = des.id_object)".format(
                    s=sql_txt
                )
            )
        else:
            sql_txt = (
                "{s} FROM (descriptionsystem INNER JOIN {t} ON descriptionsystem.pk_descriptionsystem = {t}.lpk_descriptionsystem) "
                "INNER JOIN object ON descriptionsystem.lpk_object = object.pk_object".format(
                    s=sql_txt, t=param["insert_lamia"]["tab"]
                )
            )

        # Création de la clause "WHERE" de la requête
        sql_txt = "{s} WHERE object.importtable is Null".format(s=sql_txt)
        if "where" in param["export"].keys():
            sql_txt = "{s} AND {w}".format(s=sql_txt, w=param["export"]["where"])

        return sql_txt, fld_sirs, fld_type, is_geom

    """
    Détermine si le champ Lamia doit être récupéré pour l'export vers SIRS
    :param param_fld: Paramètres liés au champ, issus du fichier de config
    :return: True si le champ doit être récupéré, False sinon 
    """

    def recup_fld(self, param_fld):
        recup = False
        if "sirs" in param_fld.keys():
            if "exp" in param_fld.keys():
                if param_fld["exp"]:
                    recup = True
            else:
                recup = True
        return recup


# import_sirs()
# export_lamia(export_img=False)
