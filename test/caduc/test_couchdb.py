# -*- coding: utf-8 -*-
#
#

import couchdb

#couch = couchdb.Server('http://geouser:pwd@127.0.0.1:5984/')

couch = couchdb.Server('http://geouser:geopw@127.0.0.1:5984/')

print(couch.config())

db = couch['test1']

print(db.info())
if False:
    for docid in db.view('_all_docs'):
        print('docid', docid)
        id = docid['id']
        print(id)
        doc = db[id]
        print('doc', doc)


map_fun = '''function(doc) {
            if (doc.type == 'Person')
            emit(doc.name, null);
            }'''

print('start')

map_fun = '''function(doc) {
            if (doc.prDebut )
            emit(doc.name, null);
            }'''

map_fun = '''function(doc) {
            if (doc.author) 
            emit([doc.type, doc.author], doc.name);
            }'''

map_fun = '''function(doc) {
            if (doc.author) 
            emit([doc.type, doc.@class], doc.name);
            }'''

for row in db.query(map_fun):
    print(row.key)
    autid = row.key[1]
    print(db[autid])




print('end')

