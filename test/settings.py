import socket
import platform
import os, sys, qgis, qgis.core

# fr en
LOCALE = "fr"
# * creation conf
CRS = 2154
# * DBase conf

DBTYPE = [
    "Base2_digue",
    "Base2_assainissement",
    "Base2_eaupotable",
    "Base2_eclairagepublic",
    "Base2_chantier",
    "Base2_tramway",
]
DBTYPE = [
    # "base3_urbandrainage",
    # "base3_waterdistribution",
    # "base3_constructionsite",
    # "base3_faunaflora",
    "base3_levee",
]


# VARIANTES = ['Lamia','Orange']

# * Connexion conf
# postgis
PGuser = "pvr"
PGpassword = "pvr"
PGbase = "lamiaunittest"
if platform.system() == "Windows":
    PGhost = "localhost"
elif platform.system() == "Linux":
    try:  # docker env in win host
        socket.gethostbyname("docker.for.win.localhost")
        PGhost = "docker.for.win.localhost"
    except socket.error as e:  # else
        PGhost = "localhost"
PGport = 5432

# * Test conf
SPATIALITE = True
POSTGIS = False

TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), "testtempfiles")

# * test onparticularfile - uncomment to apply
if False:
    SLFILE = os.path.join(os.path.dirname(__file__), "lamia_test", "test01.sqlite")
    # SLFILE = os.path.join(os.path.dirname(__file__),'temp', 'c_creation', 'sl_Base2_digue_Lamia','test01.sqlite')
if False:
    PGhost = "localhost"
    PGport = 5432
    PGbase = "lamiaunittest"
    PGschema = "lamia_base2_digue"
    PGuser = "pvr"
    PGpassword = "pvr"
