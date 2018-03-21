# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_raster_tool import AbstractRasterTool
import os
import datetime



class RasterTool(AbstractRasterTool):

    LOADFIRST = True
    dbasetablename = 'Rasters'
    
    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(RasterTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

"""
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Fonds de plan'
        self.dbasetablename = 'Rasters'
        self.visualmode = [1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Rasters' : {'linkfield' : 'id_rasters',
                                             'widgets' : {
                                            'typeraster' : self.userwdgfield.comboBox_type}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {'file': self.userwdgfield.lineEdit_file,
                                                     'dateressource': self.userwdgfield.dateEdit}}}
            self.userwdgfield.pushButton_chooseph.clicked.connect(self.chooseFile)
            self.userwdgfield.pushButton_loadraster.clicked.connect(self.loadRaster)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def loadRaster(self,feat = None):
        if feat is None or  isinstance(feat,bool):
            if self.currentFeature is not None:
                sql = "SELECT file FROM Ressource WHERE id_ressource = " + str(self.currentFeature['id_ressource'])
                query = self.dbase.query(sql)
                filetemp = [row[0] for row in query][0]
                file = self.dbase.completePathOfFile(filetemp)
            else:
                return
        else:
            #file = self.dbase.completePathOfFile(feat['file'])
            sql = "SELECT file FROM Ressource WHERE id_ressource = " + str(self.currentFeature['id_ressource'])
            query = self.dbase.query(sql)
            filetemp = [row[0] for row in query][0]
            file = self.dbase.completePathOfFile(filetemp)

        basename = os.path.basename(file).split('.')[0]
        rlayer = qgis.core.QgsRasterLayer(file, basename)
        qgis.core.QgsMapLayerRegistry.instance().addMapLayer(rlayer, True)

    def chooseFile(self):
        file, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'All (*.*)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Date', datecreation)


    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        sql = "INSERT INTO Ressource (id_objet) VALUES(" + str(idobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idres = self.dbase.getLastRowId('Ressource')

        idraster = self.currentFeature.id()

        sql = "UPDATE Rasters SET id_objet = " + str(idobjet) + ",id_ressource = " + str(idres) + " WHERE id_rasters = " + str(idraster) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

    def postSaveFeature(self, boolnewfeature):
        pass






class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamia_raster_tool_ui.ui')
        uic.loadUi(uipath, self)
"""