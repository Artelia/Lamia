import os
from Lamia.Lamia.main import DBaseParser

parser = DBaseParser(None)
# parser.loadQgisVectorLayers(file=None, dbasetype='spatialite', host='localhost', port=None, dbname=None, schema=None, user=None, password=None)
parser.loadQgisVectorLayers(file=os.path.normpath( 'C://000_testdigue//temp//test01.sqlite'))

sql = "SELECT * FROM Infralineaire"
query = parser.query(sql)
result = [row[0] for row in query]
print(result)


sql = "INSERT INTO Infralineaire(description1) VALUES('test')"
query = parser.query(sql)
parser.commit()
