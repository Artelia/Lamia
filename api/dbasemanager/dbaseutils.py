import re
import math
import datetime

try:
    from qgis.PyQt import QtCore

    TRY_QT = True
except ImportError:
    TRY_QT = False


def splitSQLSelectFromWhereOrderby(sqlin):
    sqltemp = sqlin.split(" ")
    indexparenthesis = 0

    specwords = ["WITH", "SELECT", "FROM", "WHERE", "GROUP", "ORDER", "LIMIT"]
    listres = {}
    actualsqlword = None
    for sqlword in sqltemp:
        if "(" in sqlword or ")" in sqlword:
            indexparenthesis += sqlword.count("(")
            indexparenthesis += -sqlword.count(")")
            listres[actualsqlword] += " " + sqlword
        elif sqlword.strip() in specwords and indexparenthesis == 0:
            actualsqlword = sqlword.strip()
            listres[actualsqlword] = ""
        else:
            if actualsqlword:
                listres[actualsqlword] += " " + sqlword

    if "GROUP" in listres.keys():
        listres["GROUP"] = " ".join(listres["GROUP"].strip().split(" ")[1:])

    return listres


def rebuildSplittedQuery(sqlin):
    sqlout = ""
    if "WITH" in sqlin.keys():
        sqlout += " WITH " + sqlin["WITH"]
    if "SELECT" in sqlin.keys():
        sqlout += " SELECT " + sqlin["SELECT"]
    if "FROM" in sqlin.keys():
        sqlout += " FROM " + sqlin["FROM"]
    if "WHERE" in sqlin.keys():
        sqlout += " WHERE " + sqlin["WHERE"]
    if "GROUP" in sqlin.keys():
        sqlout += " GROUP BY " + sqlin["GROUP"]
    if "ORDER" in sqlin.keys():
        sqlout += " ORDER  " + sqlin["ORDER"]
    if "LIMIT" in sqlin.keys():
        sqlout += " LIMIT " + sqlin["LIMIT"]
    return sqlout


def isAttributeNull(attr):
    """
    Vérifie si un qgisfeature attribute est NULL - piégeux car le NULL peu prendre plusieurs formes
    :param attr: get an qgisfeature attribute
    :return: True if NULL, else False
    """

    """
    if int(str(self.qgisversion_int)[0:3]) < 220 and isinstance(attr, QtCore.QPyNullVariant):
        return True
    elif int(str(self.qgisversion_int)[0:3]) > 220 and isinstance(attr, QtCore.QVariant) and attr.isNull():
        return True
    """

    if TRY_QT and isinstance(attr, QtCore.QVariant) and attr.isNull():
        return True
    elif (isinstance(attr, bytes) or isinstance(attr, str)) and (
        attr == "NULL" or attr == "" or attr == "None"
    ):
        return True
    elif attr is None:
        return True
    else:
        return False


def areNodesEquals(node1, node2):
    """
    Fonction pour examiner l'égalité géographique de deux points.
    Nécessaire car parfois les arrondis des coordonnées géographiques font que deux points égaux ont une
    différence de qques micromètres
    :param node1: point1 (list 2x1)
    :param node2: point2 (list 2x1)
    :return: Boolean, en fonction de l'égalité geographique des points
    """
    dist = math.sqrt((node2[0] - node1[0]) ** 2 + (node2[1] - node1[1]) ** 2)
    if dist < 0.01:
        return True
    else:
        return False


def getCurrentDateTime():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
