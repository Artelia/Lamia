import re, math
try :
    from qgis.PyQt import QtCore
    TRY_QT = True
except ImportError:
    TRY_QT = False


def updateQueryTableNow( sqlin, date=None):
    
    sqllist = re.split(' |,|\(|\)|\.|=', sqlin)
    withsql = ''
    alreadytables=[]
    for sqlword in sqllist:
        if '_now' in sqlword:
            tablename=sqlword.split('_now')[0]
            if tablename.lower() not in  alreadytables:
                alreadytables.append(tablename.lower())
                withsql +=  sqlword + " AS "
                withsql += " (SELECT * FROM " + tablename + "_qgis WHERE "
                withsql += self.dateVersionConstraintSQL(date)
                withsql += "), "

    withsql = withsql[0:-2]
    sqltemp1 = self.splitSQLSelectFromWhereOrderby(sqlin)
    sqlout = ''
    if 'WITH' in sqltemp1.keys():
        sqlout += 'WITH ' + sqltemp1['WITH']
        sqlout += ', ' + withsql
        sqlout += ' SELECT ' + sqltemp1['SELECT'] + ' FROM ' + sqltemp1['FROM']+ ' WHERE ' + sqltemp1['WHERE']
        if 'ORDER' in sqltemp1.keys():
            sqlout += ' ORDER BY ' + sqltemp1['ORDER']
        if 'GROUP' in sqltemp1.keys():
            sqlout += ' GROUP BY ' + sqltemp1['GROUP']

    elif withsql != '':
        sqlout += 'WITH ' + withsql + sqlin

    else:
        sqlout += sqlin
        
    return sqlout


def splitSQLSelectFromWhereOrderby(sqlin):
    sqltemp = sqlin.split(' ')
    indexparenthesis=0

    specwords = ['WITH', 'SELECT', 'FROM', 'WHERE', 'GROUP','ORDER','LIMIT']
    listres={}
    actualsqlword = None
    for sqlword in sqltemp:
        if '(' in sqlword or ')' in sqlword:
            indexparenthesis += sqlword.count('(')
            indexparenthesis += - sqlword.count(')')
            listres[actualsqlword] += ' ' + sqlword
        elif  sqlword.strip() in specwords and indexparenthesis == 0 :
            actualsqlword = sqlword.strip()
            listres[actualsqlword] = ''
        else:
            if actualsqlword:
                listres[actualsqlword] += ' ' + sqlword

    if 'GROUP' in listres.keys():
        listres['GROUP'] = ' '.join(listres['GROUP'].strip().split(' ')[1:])

    return listres

def rebuildSplittedQuery( sqlin):
    sqlout = ''
    if 'WITH' in sqlin.keys():
        sqlout += ' WITH ' + sqlin['WITH']
    if 'SELECT' in sqlin.keys():
        sqlout += ' SELECT ' + sqlin['SELECT']
    if 'FROM' in sqlin.keys():
        sqlout += ' FROM ' + sqlin['FROM']
    if 'WHERE' in sqlin.keys():
        sqlout += ' WHERE ' + sqlin['WHERE']
    if 'GROUP' in sqlin.keys():
        sqlout += ' GROUP BY ' + sqlin['GROUP']
    if 'ORDER' in sqlin.keys():
        sqlout += ' ORDER BY ' + sqlin['ORDER']
    if 'LIMIT' in sqlin.keys():
        sqlout += ' LIMIT ' + sqlin['LIMIT']
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

    if TRY_QT and isinstance(attr, QtCore.QVariant) and attr.isNull() :
        return True
    elif (isinstance(attr,bytes) or isinstance(attr,str)) and (attr == 'NULL' or attr == '' or attr == 'None') :
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
    dist = math.sqrt( (node2[0] - node1[0])**2 + (node2[1]-node1[1])**2 )
    if dist < 0.01:
        return True
    else:
        return False