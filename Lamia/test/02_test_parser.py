import os
from Lamia.Lamia.main import DBaseParser
import sqlite3

parser = DBaseParser(None)
pathsqlite = os.path.normpath('C://000_testdigue//temp_VNF//test01.sqlite')
# parser.loadQgisVectorLayers(file=None, dbasetype='spatialite', host='localhost', port=None, dbname=None, schema=None, user=None, password=None)
parser.loadQgisVectorLayers(file=os.path.normpath( pathsqlite))


if False:
    sql = "SELECT * FROM Infralineaire"
    query = parser.query(sql)
    result = [row[0] for row in query]
    print(result)

    """
    sql = "INSERT INTO Infralineaire(description1) VALUES('test')"
    query = parser.query(sql)
    parser.commit()
    """

# test BLOB
if True:
    #write
    if False:
        pathfile = os.path.join(os.path.dirname(__file__),'..','DBASE','rapport','utils','logo.jpg')
        pathfile = "I://FLUVIAL//4352024_33_Conformite_digues_BM//4_Donnees//Photographies//05_10_2017//P1130152.JPG"
        with open(pathfile, 'rb') as f:
            ablob = f.read()
            sql = '''UPDATE Photo SET file = ?  WHERE id_photo = 1;'''
            args = [sqlite3.Binary(ablob)]
            query = parser.query(sql,args)

    #read
    if True:
        sql = '''SELECT file FROM Photo WHERE id_photo=7'''
        query = parser.query(sql)
        result = [row[0] for row in query][0]
        #print(result)

        with open('c://test1.jpg', 'wb') as f:
            f.write(result)


print('finished')
