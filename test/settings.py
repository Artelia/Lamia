import socket
import  platform
import os, qgis


def initQGis():
    if platform.system() == 'Windows':
        qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
    elif platform.system() == 'Linux':
        qgis_path = '/usr'

    app = qgis.core.QgsApplication([], True)
    qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
    qgis.core.QgsApplication.initQgis()
    return app

def exitQGis():
    qgis.core.QgsApplication.exitQgis()


#* creation conf
CRS = 2154
#* DBase conf

DBTYPE = ['Base2_digue', 'Base2_assainissement', 'Base2_eaupotable', 'Base2_eclairagepublic',
         'Base2_chantier', 'Base2_tramway']
DBTYPE = ['base3_urbandrainage', 'base3_waterdistribution', 'base3_constructionsite',
         'base3_faunaflora']

DBTYPE = ['base3_levee']     
# VARIANTES = ['Lamia','Orange']

#* Connexion conf
#postgis
PGuser = 'pvr'
PGpassword = 'pvr'
PGbase = 'lamiaunittest'
if platform.system() == 'Windows':
    PGhost = 'localhost'
elif platform.system() == 'Linux':
    try:    #docker env in win host
        socket.gethostbyname('docker.for.win.localhost')
        PGhost = 'docker.for.win.localhost'
    except socket.error as e:   # else
        PGhost = 'localhost'
PGport = 5432

#* Test conf
SPATIALITE = True
POSTGIS = False

TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'testtempfiles')

#* test onparticularfile - uncomment to apply
if False:
    SLFILE = os.path.join(os.path.dirname(__file__), 'lamia_test','test01.sqlite')
    #SLFILE = os.path.join(os.path.dirname(__file__),'temp', 'c_creation', 'sl_Base2_digue_Lamia','test01.sqlite')
if False:
    PGhost = 'localhost'
    PGport = 5432
    PGbase = 'lamiaunittest'
    PGschema = 'lamia_base2_digue'
    PGuser = 'pvr'
    PGpassword = 'pvr'
    

    

