# coding=utf-8
from ...libs.cloudant import Cloudant
from ...libs.cloudant import query

#from cloudant import Cloudant
#from cloudant.query import Query
import json
import re

class queryFranceDigue():

    """
    All the entry arguments are in form of strings
    :param user: String
    :param pwd: String
    :param ip: String
    :param port: String
    :param selectDB: String
    """
    def __init__(self, user, pwd, ip, port, selectDb):
        self.client = Cloudant(user, pwd, url='http://' + ip + ':' + port)
        self.client.connect()
        self.setSelectedDB(selectDb)

    """
    get the current client
    :rtype: cloudant.client.Cloudant
    """
    def getClient(self):
        return self.client

    """
    get the current selected database
    :rtype: String
    """
    def getSelectedDB(self):
        return self.selectDb

    """
    Set the current database
    :param selectDB: String
    """
    def setSelectedDB(self, selectDB):
        if selectDB not in self.client.all_dbs():
            raise ValueError("The database you searching '"+selectDB+"' isn't here")
        self.selectDb = selectDB
        self.keySet = self.getPossibleKeys()

    """
    Get all the possible keys in a select dataBase
    :rtype: list of String
    """
    def getPossibleKeys(self):
        keys = []
        for doc in self.client[self.selectDb]:
            for key in doc:
                if key not in keys:
                    keys.append(key)
        return keys

    """
    Get all possible values for a certain key
    :param key: String
    :rtype: list of String
    """
    def getPossibleValues(self, key):
        if key not in self.keySet:
            raise ValueError('error the key: ' + key + ' isn\'t in the keyset')
        values = []
        for doc in self.client[self.selectDb]:
            if key in doc and doc[key] not in values:
                values.append(doc[key])
        return values

    """
    Get all the document with a specific Key
    :param key: String
    :rtype: list of cloudant.document.Document
    """
    def getDocWithKey(self, key):
        documents = []
        for doc in self.client[self.selectDb]:
            if key in doc:
                documents.append(doc)
        return documents

    """
    Make a custom query using a Json, and if a fields is given return the selected one,
    otherwise it's return all the possible fields
    :param json: Json
    :param fields: list fo string
    :rtype: an iterable object
    """
    def customQuery(self, json, fields=None):
        if fields == None:
            fields = self.getPossibleKeys()
        query = Query(self.client[self.selectDb], selector=json, fields=fields)
        return query.result

    """
    Get the document with the specified id, and return the values of the fields given in entry
    :param id: string
    :param fields: list of string
    :rtype: dict of String
    """
    def getDocFields(self, id, fields):
        ret = {}
        doc = self.getDocument(id)
        for fld in fields:
            if ' ' in fld:
                ret[fld] = self.seekIn(doc, fld.split(' '))
            else:
                ret[fld] = self.seekIn(doc, [fld])
        return ret

    """
    Really big function thath allow to navigate easily trought this god damn CouchDb databse full, of list of dict by giving a path in entry
    obj - the current obj to explore
    path - wich index to enter
    """
    def seekIn(self, obj, path):
        search = path[0]

        #Si le path est compose d'un noeud, une redirection vers un autre objet a creer
        if path[0][0].isupper() and len(path) == 1:
            fields = json.load(open('jsonConfig/fields.json'))
            path = path[0]
            ret = self.getDocFields(obj['_id'], fields[path])
            return ret

        #Si l'obj a explorer est de type list on peux donc iterer sur des int
        if isinstance(obj, list):
            search = int(path[0])

            for i in range(0, len(obj)):

                #Si l'index actuel est egal a celui recheche, mais qu'il est de type dict ou une list, alors on rentre dedans
                if i == search and (isinstance(obj[i], dict) or isinstance(obj[i], list)) :
                    return self.seekIn(obj[i], path[1:])

                #Si l'index actuel est egal a celui recheche, mais que le path n'est pas fini, alors il s'agit d'une redirection
                elif i == search and len(path) > 1:
                    return self.jumpTo(obj[i], path[1:])

                #Si l'index actuel est egal a celui recheche, mais que le path est finis alors il s'agit de notre element cible
                elif i == search and len(path) == 1 :
                    return obj[i]
            else:
                print('None at list')
                return None

        #Si l'obj a explorer est de type dict, on peux donc iterer sur des string
        if isinstance(obj, dict):

            for elem in obj:

                #Si l'element actuel est egal, mais qu'il est de type dict ou une list, alors on rentre dedans
                if elem == search and (isinstance(obj[elem], dict) or isinstance(obj[elem], list)) :
                    return self.seekIn(obj[elem], path[1:])

                #Si l'element actuel est egal a celui recherche, mais que le path n'est pas fini, alors il s'agit d'une redirection
                elif elem == search and len(path) > 1 :
                    return self.jumpTo(obj[elem], path[1:])

                #Si l'element actuel est egal a celui recherche, mais que le path est finis alors il s'agit de notre element cible
                elif elem == search and len(path) == 1 :
                    return obj[elem]
        else:
            print('none at dict')
            return None

    """
    Allow redirection from one document to another
    target - string of the id of the tergeted document
    path - the path to follow afterwards
    """
    def jumpTo(self, target, path):
        #Test si la cible est bien un id, ou une reference
        if isinstance(target, unicode) and re.match('(\d|[a-z]){5,30}', target) or 'Ref' in target:
            doc = self.getDocument(target)
            ret = self.seekIn(doc, path)
            return ret
        else:
            print('not matching: '+str(target))
            return None

    """
    Return a specific element as a cloudant.document type,
    wich then can be manipulate with update and delete function from Cloudant module
    :rtype: cloudant.document.Document
    """
    def getDocument(self, id):
        ret = self.client[self.selectDb][id]
        return ret

    def addDocument(self, data):
        return self.client[self.selectDb].create_document(data)

    """
    Allow to edit an attribut of a document
    :param id: String
    :param key: String
    :param value: String
    """
    def updateDocument(self, id, path, value):
        doc = self.getDocument(id)
        #On split le path comme d'hab
        path = path.split(' ')
        #On convertit les éventuels Char: 0,1,2... en vrai INT
        for i in range(0 , len(path)):
            if path[i].isnumeric():
                path[i] = int(path[i])
        #Triviale mais rapide, peut-être amélioré en reprendnat le code de seekIn() on modifie la valeur pointé par le path
        if len(path) == 1:
            doc[path[0]] = value
        if len(path) == 2:
            doc[path[0]][path[1]] = value
        if len(path) == 3:
            doc[path[0]][path[1]][path[2]] = value
        #save() permet de modifier la version distante de la CouchDb
        doc.save()

    """
    Allow to delete a document using his primary key
    :param id: String
    """
    def deleteDocument(self, id):
        self.getDocument(id).delete()

    """
    Disconnect the client from the database
    """
    def disconnect(self):
        self.client.disconnect()

def main():
    print("Class name : QueryFranceDigue\npurpose: make NoSql query to the FrancDigue database")

if __name__ == '__main__':
    main()
