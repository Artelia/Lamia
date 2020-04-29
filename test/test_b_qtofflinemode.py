import unittest, os, logging, sys, shutil, logging, time, glob, json, datetime
from pprint import pprint
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), '..'))
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)


import qgis, qgis.core
from qgis.PyQt.QtWidgets import  (QApplication)
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow)


from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.iface.qgsconnector.ifaceqgisconnector import QgisConnector


from settings import *

X_BEGIN = 400000.0
Y_BEGIN = 6000000.0

class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests."""
        #TESTDIR = os.path.join(os.path.dirname(__file__), 'temp')
        self.connector = QgisConnector()

        self.offlinetdir = os.path.join(TESTDIR, 'offlinemodedbase')
        if not os.path.isdir(self.offlinetdir):
            os.mkdir(self.offlinetdir)

        self.filephoto = os.path.join(os.path.dirname(__file__), 'datas','logo_artelia.jpg' )


    def test_a_testoffline(self):
        self._createWin()
        self._createMainWin()

        if SPATIALITE:
            #* create parent db
            logging.getLogger("Lamia_unittest").debug('Create parentDB ')
            offlinepath = os.path.join(self.offlinetdir,'parentdb','parenttestoffline.sqlite')
            childofflinepath = os.path.join(self.offlinetdir,'childdb','childtestoffline.sqlite')

            if True:
                if not os.path.isdir(os.path.dirname(offlinepath)):
                    os.mkdir(os.path.dirname(offlinepath))
                sqlitedbase = DBaseParserFactory('spatialite').getDbaseParser()
                sqlitedbase.createDBase(crs=CRS, 
                                        worktype='Base2_digue', 
                                        dbaseressourcesdirectory=None, 
                                        variante='Lamia',
                                        slfile=offlinepath)
                sqlitedbase.disconnect()

                self.wind.loadDBase(dbtype='Spatialite', slfile=offlinepath)
                self.createInitialFeatures()
                # self.showandstop()
                

                #* pull child db
                logging.getLogger("Lamia_unittest").debug('pull child db ')
                
                if not os.path.isdir(os.path.dirname(childofflinepath)):
                    os.mkdir(os.path.dirname(childofflinepath))
                self.wind.pullDBase(exportfilepath=childofflinepath)


                #* make changes in child db
                logging.getLogger("Lamia_unittest").debug('Make changes in child db - %s', self.wind.dbase.getDBName())
                self.makeChangesinChildDB()
                # self.showandstop()

                #*make changes in parent db
                logging.getLogger("Lamia_unittest").debug('modifiy parentdb')
                self.wind.loadDBase(dbtype='Spatialite', slfile=offlinepath)
                self.makechangesinParentDB()
                # self.showandstop()

            if True:
                copyfile = os.path.join(os.path.dirname(offlinepath),'parenttestoffline_backup.sqlite')
                shutil.copy(offlinepath, copyfile)
                # shutil.copy(copyfile, offlinepath)
                #* push child
                logging.getLogger("Lamia_unittest").debug('push child')
                self.wind.loadDBase(dbtype='Spatialite', slfile=childofflinepath)

                self.wind.dbase.dbaseofflinemanager.__class__.RESOLVECONFLICTTYPE = 'auto'
                self.wind.dbase.dbaseofflinemanager.__class__.RESOLVECONFLICTCHOICE = 'import'
                # print(self.wind.dbase.dbaseofflinemanager.__class__.RESOLVECONFLICTTYPE)
                # print(self.wind.dbase.dbaseofflinemanager.RESOLVECONFLICTTYPE)
                self.wind.pushDBase()

            if True:
                #* finaly open parentdb
                #conflict must be id 4, 5, 6, 8, 9, 11
                #visual result if imported table choosen :
                #pk     1   2   3   4   5   6   7   8   9   10  11  12
                #place  0   2   1   1   1   1   del del del del 2   1
                #photo  1   12  13  1   123 1   /   /   /   /   2   3
                #visual result if main table choosen :
                #pk     1   2   3   4   5   6   7   8   9   10  11  12
                #place  0   2   1   del 2   del del 2   2   del 2   1
                #photo  1   12  13  1   123 /   /   1   1   /   2   3

                logging.getLogger("Lamia_unittest").debug('openparentdb')
                self.wind.loadDBase(dbtype='Spatialite', slfile=offlinepath)
                # self.showandstop()

    def showandstop(self):
        self.mainwin.exec_()
        exitQGis()
        sys.exit()

    """
    cases: (datet : datetravail)
    MAin                                             Import
    case n° datem       revbegin    revend          datem       revbegin    revend      Action                              Action on import                    Action if main retained
    0       /                                       >datet      2                       new item
    1       <datet      11                          <datet      1                       nothing modified                    /                                   /
    2       >datet      11                          <datet      1                       only main modified - ok             /                                   /
    3       <datet      11                          >datet      1           2           only import modified ok             close lastrev and create new rev    /
                                                    >datet      2
    4       suppr                                   >datet      1           2           conflict                            add new rev with same id            close new rev
                                                    >datet      2
    9       >datet      11                          >datet      1           2           conflit                             close lastrev                       unclose lastrev
    7       suppr                                   >datet      1           2           ok : deleted on main and import     /                                   /
    5       >datet      11          12              >datet      1           2           conflict                            rewrite main new rev                rewrite new rev with main
            >datet      12                          >datet      2
    6       >datet      11          12              >datet      1           2           conflict                            add new rev                         close new rev
                                                    >datet      2
    
    8       >datet      11          12              >datet      1           2           conflict                            close lastrev                      write new rev with main
            >datet      12
 
    10      >datet      11          12              >datet      1           2           ok : deleted on main and import     /                                   /
    11      >datet      11          12              >datet      1           2           conlit                              add new rev                         /  close las rev
                                                    >datet      2

    :param dbaseparserfrom:
    :param conflictobjetid:
    :return:
    """            

    def createInitialFeatures(self):
        # creatin infralin
        name='Troncon'
        wdg = self.wind.toolwidgets['toolprepro'][name][0]
        
        for i in range(10):
            wdg.widgetClicked()
            # self.wind.toolbarNew()
            wdg.selectFeature()
            wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 0),qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 1)])
            # self.wind.toolbarSave()
            wdg.toolbarSave()
            wdgphoto = wdg.propertieswdgPHOTOGRAPHIE
            wdgphoto.widgetClicked()
            wdgphoto.selectFeature()
            wdgphoto.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + i,Y_BEGIN + 4)])
            wdgphoto.formutils.applyResultDict({'file':self.filephoto},checkifinforgottenfield=False)
            wdgphoto.toolbarSave()




    def makechangesinParentDB(self):
        name='Troncon'
        wdg = self.wind.toolwidgets['toolprepro'][name][0]
        wdgphoto = wdg.propertieswdgPHOTOGRAPHIE

        wdg.widgetClicked()
        #* case 0 :create new
        pk=11
        wdg.selectFeature()
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 3)])
        wdg.toolbarSave()
        wdgphoto.widgetClicked()
        wdgphoto.selectFeature()
        wdgphoto.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN  + pk - 1,Y_BEGIN + 5)])
        wdgphoto.formutils.applyResultDict({'file':self.filephoto},checkifinforgottenfield=False)
        wdgphoto.toolbarSave()
        #* case 1 : noting modif
        #* case 2 : only main updated
        pk=2
        wdg.selectFeature(pk=pk)
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 3)])
        wdg.toolbarSave()
        wdgphoto.widgetClicked()
        wdgphoto.selectFeature()
        wdgphoto.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN  + pk - 1,Y_BEGIN + 5)])
        wdgphoto.formutils.applyResultDict({'file':self.filephoto},checkifinforgottenfield=False)
        wdgphoto.toolbarSave()
        #* case 3 : offline updated

        #case4 : suppr in main and updated in offline
        pk=4
        wdg.selectFeature(pk=pk)
        wdg.formutils.deleteFeature()
        #case 9 : modifed in main and deleted in offline
        pk=9
        wdg.selectFeature(pk=pk)
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 3)])
        wdg.toolbarSave()
        #case7 : deleted in main and offline
        pk=7
        wdg.selectFeature(pk=pk)
        wdg.formutils.deleteFeature()

        #new version
        datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sql = "INSERT INTO Revision(datetimerevision, commentaire)  "
        sql += " VALUES('" + datecreation + "','travail horsligne')"
        self.wind.dbase.query(sql)
        self.wind.dbase.maxrevision = self.wind.dbase.getLastPK('Revision')
        self.wind.dbase.currentrevision = self.wind.dbase.maxrevision

        #case5: updated in main and offline
        pk=5
        wdg.selectFeature(pk=pk)
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 3)])
        wdg.toolbarSave()
        wdgphoto.widgetClicked()
        wdgphoto.selectFeature()
        wdgphoto.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN  + pk - 1,Y_BEGIN + 5)])
        wdgphoto.formutils.applyResultDict({'file':self.filephoto},checkifinforgottenfield=False)
        wdgphoto.toolbarSave()
        #case6:archive in main and updated in offline
        pk=6
        wdg.selectFeature(pk=pk)
        wdg.formutils.archiveFeature()

        #case 8 : deleted in offline and updated in main
        pk=8
        wdg.selectFeature(pk=pk)
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 3)])
        wdg.toolbarSave()
        #case10 : deleted in main and offline
        pk=10
        wdg.selectFeature(pk=pk)
        wdg.formutils.archiveFeature()


    def makeChangesinChildDB(self):
        name='Troncon'
        wdg = self.wind.toolwidgets['toolprepro'][name][0]
        wdgphoto = wdg.propertieswdgPHOTOGRAPHIE

        wdg.widgetClicked()
        #* case 0 :create new
        pk = 12
        wdg.selectFeature()
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 1),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2)])
        wdg.toolbarSave()
        wdgphoto.widgetClicked()
        wdgphoto.selectFeature()
        wdgphoto.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 6)])
        wdgphoto.formutils.applyResultDict({'file':self.filephoto},checkifinforgottenfield=False)
        wdgphoto.toolbarSave()
        #* case 1 : noting modif
        #* case 2 : only main updated
        #* case 3 : offline updated
        pk=3
        wdg.selectFeature(pk=pk)
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 1),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2)])
        wdg.toolbarSave()
        wdgphoto.widgetClicked()
        wdgphoto.selectFeature()
        wdgphoto.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN  + pk - 1,Y_BEGIN + 6)])
        wdgphoto.formutils.applyResultDict({'file':self.filephoto},checkifinforgottenfield=False)
        wdgphoto.toolbarSave()
        #case4 : suppr in main and updated in offline
        pk=4
        wdg.selectFeature(pk=pk)
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 1),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2)])
        wdg.toolbarSave()
        #case 9 : modifed in main and deleted in offline
        pk=9
        wdg.selectFeature(pk=pk)
        wdg.formutils.archiveFeature()
        #case5: updated in main and offline
        pk=5
        wdg.selectFeature(pk=pk)
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 1),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2)])
        wdg.toolbarSave()
        wdgphoto.widgetClicked()
        wdgphoto.selectFeature()
        wdgphoto.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN  + pk - 1,Y_BEGIN + 6)])
        wdgphoto.formutils.applyResultDict({'file':self.filephoto},checkifinforgottenfield=False)
        wdgphoto.toolbarSave()
        #case6:archive in main and updated in offline
        pk=6
        wdg.selectFeature(pk=pk)
        wdg.setTempGeometry([qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 1),qgis.core.QgsPointXY(X_BEGIN + pk - 1,Y_BEGIN + 2)])
        wdg.toolbarSave()
        #case7 : deleted in main and offline
        pk=7
        wdg.selectFeature(pk=pk)
        wdg.formutils.archiveFeature()
        #case 8 : deleted in offline and updated in main
        pk=8
        wdg.selectFeature(pk=pk)
        wdg.formutils.archiveFeature()

        #case10 : deleted in main and offline
        pk=10
        wdg.selectFeature(pk=pk)
        wdg.formutils.archiveFeature()


    def _createMainWin(self):
        self.mainwin = UserUI()
        self.mainwin.frame.layout().addWidget(self.canvas)
        self.mainwin.frame_2.layout().addWidget(self.wind)
        self.mainwin.setParent(None)
        self.mainwin.resize(QtCore.QSize(1000,800))

    def _createWin(self):
        self.canvas = qgis.gui.QgsMapCanvas()
        self.canvas.enableAntiAliasing(True)
        canvascrs = qgis.core.QgsCoordinateReferenceSystem()
        canvascrs.createFromString('EPSG:2154')
        self.canvas.setDestinationCrs(canvascrs)

        self.wind = LamiaWindowWidget()
        self.wind.qgiscanvas.setCanvas(self.canvas)

        stylesheet = """
                    QMainWindow{
                                background-color: rgba(0, 55, 90,80);
                                }
                    """
        stylesheet = ''
        self.wind.setStyleSheet(stylesheet)
        self.wind.setParent(None)
        self.dbase = self.wind.dbase
        self.mainwin = None


class UserUI(QDialog):

    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'qtdialog', 'mainwindows.ui')
        uic.loadUi(uipath, self)

def main():
    app = initQGis()
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s',
                        datefmt="%H:%M:%S")
    logging.getLogger( "Lamia_unittest" ).setLevel( logging.DEBUG )
    logging.getLogger( "Lamiaoffline" ).setLevel( logging.DEBUG )
    unittest.main()
    exitQGis()
    sys.exit()

if __name__ == "__main__":
    main()




