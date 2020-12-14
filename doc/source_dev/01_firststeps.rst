.. toctree::
    :maxdepth: 2

Warming up with Lamia API
#################################

Define QGIS path settings
*********************************

Adapt the paths in Lamia/utils/qgisconfig.txt to match your qgis install

.. code-block:: 

    OSGEOPATH=C:\OSGeo4W64
    QGISPATH=C:\OSGeo4W64\apps\qgis
    #QGISPATH=/usr/....
    QGISPATHLINUX=/usr/lib


Creating and loading a new DBASE 
***************************************

.. code-block:: python

    from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

    # getting the dbaseparser
    sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()

    SLFILE = r"c:\test.sqlite"

    #creating a DBASE
    sqlitedbase.createDBase(
        crs=2154,                           # the epsg code
        worktype='base3_levee',             # the dbase type
        dbaseressourcesdirectory=None,      # the dir where resources are saved, None for default
        variante=variante,                  # the Dbase variant 
        slfile=SLFILE,                      # spatialite file path to be created
    )

    #loading DBASE
    sqlitedbase.loadDBase(slfile=SLFILE)

    # **************
    # querying the dbase

    # pure sql
    res = sqlitedbase.query("SELECT * FROM edge")

    # lamiaorm

    # create a new edge line, and returns the pk of new element
    newpk = sqlitedbase.lamiaorm['edge'].create()               

    # read columns of line with pk = 9
    res = sqlitedbase.lamiaorm['edge'].read(pk=9)                            

    # read values from table edge where pk_edge = 9 and field1 = 'bob'
    res = sqlitedbase.lamiaorm['edge']["pk_edge = 9 and field1 = 'bob'"]      

    # update field1 and field2 column of table edge line with pk=9
    sqlitedbase.lamiaorm['edge'].update(9,{'field1': 'pop', 'field2': 987}) 

    # delete line with pk = 9 from edge table
    sqlitedbase.lamiaorm['edge'].delete(pk=9)



Display the lamia gui outside qgis
***************************************

.. code-block:: python  

    #first be sure the parent directory of Lamia is in sys.path
    # sys.path.append('/.../')

    from Lamia.qgisiface.iface.qgsconnector.ifaceloggingconnector import LoggingConnector
    from Lamia.test.test_utils import *

    # init qgis
    app = initQGis()

    # load and apply translations
    translator = loadLocale()

    # get lamia guis : the maingui, the canvas and the lamia dockwidget
    mainwin, canvas, lamiawidget = getDisplayWidget()

    # set a connector for outputs
    lamiawidget.connector = LoggingConnector()

    # load a spatialite project
    SLFILE = "/usr/src/Lamia/testfiles/test/test.sqlite"
    lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    # display the gui
    mainwin.exec_()

    # finally exit qgis
    exitQGis()

    
Get a particular form of  Lamia ouside qgis gui
******************************************************

.. code-block:: python  

    [...]
    lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    # get the form - the key used is PREPROTOOLNAME or POSTPROTOOLNAME variable of the form class
    wdg = lamiawidget.toolwidgets["lamiamca"]
    # Tells the gui to activate this form
    wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)
    # Make actions with the form
    wdg.doSomething()

    [...]



Play with API in Lamia.lamialibs
*************************************

.. code-block:: python  

    from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

    from Lamia.test.test_utils import *
    from Lamia.api.lamialibs.testlib import TestLib

    # only if API uses qgis 
    app = initQGis()

    # getting the dbaseparser and load test dbase
    sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
    SLFILE = r"c:\test.sqlite"
    lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    # active the lib and execute functions (for exemple)
    newlib = TestLib(sqlitedbase)
    newlib.doSomething()



