# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os
import datetime

from .lamiabase_pointtopo_tool import BasePointtopoTool

"""
ne permettre de la renseigner qu en etant une classe fille de leve topo - sinon pas de datecreation
ca fout la merde....

"""


class BaseTopographieTool(AbstractLamiaTool):

    LOADFIRST = True
    dbasetablename = 'Topographie'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseTopographieTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Leves topographiques'
        self.dbasetablename = 'Topographie'
        # self.visualmode = [0, 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                           'idsource' : 'id_ressource',
                                       'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                       'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lk_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']}}
        # self.pickTable = None
        self.qtreewidgetfields = ['lpk_revision_begin']
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_topographie_tool_icon.png')

        # ****************************************************************************************
        #properties ui

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Topographie' : {'linkfield' : 'id_topographie',
                                             'widgets' : {}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {'file': self.userwdgfield.lineEdit_file,
                                                        'description': self.userwdgfield.lineEdit_nom,
                                                        'dateressource': self.userwdgfield.dateEdit_date}}}
            self.userwdgfield.pushButton_chooseph.clicked.connect(self.choosePhoto)
            self.userwdgfield.pushButton_open.clicked.connect(self.openFile)
            self.userwdgfield.pushButton_ajoutpointGPS.clicked.connect(self.ajoutPointGPS)
            self.userwdgfield.pushButton_importer.clicked.connect(self.importer)

            typpointlist = [elem[0] for elem in self.dbase.dbasetables['Pointtopo']['fields']['typepointtopo']['Cst']]
            self.userwdgfield.comboBox_typepoints.addItems(typpointlist)


            self.gpswidget = {'x' : {'widget' : self.userwdgfield.label_X,
                                     'gga' : 'Xcrs'},
                              'y': {'widget': self.userwdgfield.label_Y,
                                    'gga': 'Ycrs'},
                              'zmngf': {'widget': self.userwdgfield.label_Z,
                                    'gga': 'zmNGF'},
                              'dx': {'widget': self.userwdgfield.label_dX,
                                    'gst': 'xprecision'},
                              'dy': {'widget': self.userwdgfield.label_dY,
                                    'gst': 'yprecision'},
                              'dz': {'widget': self.userwdgfield.label_dZ,
                                    'gst': 'zprecision'},
                              'zgps': {'widget': self.userwdgfield.label_zgps,
                                     'gga': 'elevation'},
                              'zwgs84': {'widget': self.userwdgfield.label_zwgs84,
                                       'gga': 'deltageoid'},
                              'raf09': {'widget': self.userwdgfield.label_raf09,
                                       'gga': 'RAF09'},
                              'hauteurperche': {'widget': self.userwdgfield.label_hautperche,
                                        'gga': 'hauteurperche'}
                              }


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.propertieswdgPOINTTOPO= BasePointtopoTool(dbase=self.dbase,gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPOINTTOPO)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postSaveFeature(self, boolnewfeature):

        if self.savingnewfeatureVersion:

            #fieldstoappend
            pointtopofields = self.dbase.dbasetables['Pointtopo']['fields'].keys()
            pointtopofields.remove('pk_pointtopo')
            indexpktopo = pointtopofields.index('lpk_topographie')
            pointtopofields.insert(-1, 'ST_AsText(geom)')

            sql = "SELECT " + ','.join(pointtopofields) + " FROM Pointtopo WHERE lpk_topographie = " + str(self.beforesavingFeaturePK)
            results = self.dbase.query(sql)
            results = [list(res) for res in results]

            print(results)

            for i, res in enumerate(results):
                results[i][indexpktopo] = self.currentFeaturePK

            print(results)

            pointtopofields[pointtopofields.index('ST_AsText(geom)')] = 'geom'

            for res in results:

                sql = self.dbase.createSetValueSentence(type='INSERT',
                                                  tablename='Pointtopo',
                                                  listoffields=pointtopofields,
                                                  listofrawvalues=res)

                self.dbase.query(sql, docommit=False)

            self.dbase.commit()



    def openFile(self):
        filepath = self.completePathOfFile(self.userwdg.lineEdit_file.text())
        if filepath != '':
            os.startfile(filepath)

    def ajoutPointGPS(self):
        #self.propertieswdgPOINTTOPO.magicFunction()
        self.propertieswdgPOINTTOPO.featureSelected()
        #self.propertieswdgPOINTTOPO.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_position.findText('Crete'))
        self.propertieswdgPOINTTOPO.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_typepoints.currentIndex())
        success = self.propertieswdgPOINTTOPO.getGPSValues()
        if success:
            self.propertieswdgPOINTTOPO.saveFeature()

    def importer(self):
        pass

    def choosePhoto(self):
        file, extension = self.windowdialog.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'All (*.*)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            #self.initFeatureProperties(feat, 'Ressource', 'dateressource', datecreation)
            self.initFeatureProperties(feat, None, 'dateressource', datecreation)



    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:


            # lastrevision = self.dbase.maxrevision
            datecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')

        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sql = "INSERT INTO Ressource (id_ressource, lpk_objet) "
        sql += "VALUES(" + str(lastressourceid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pkres = self.dbase.getLastRowId('Ressource')

        pktopo = self.currentFeaturePK
        lastidtopo = self.dbase.getLastId('Topographie') + 1
        sql = "UPDATE Topographie SET id_topographie = " + str(lastidtopo)  + ","
        sql += "lpk_ressource = " + str(pkres)
        sql += " WHERE pk_topographie = " + str(pktopo) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Marche':
                # print(self.parentWidget.currentFeature.attributes())
                currentparentlinkfield = self.parentWidget.currentFeature['id_marche']
                sql = "UPDATE Ressource SET lk_marche = " + str(currentparentlinkfield) + " WHERE id_ressource = " + str(pkres) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()








class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_topographie_tool_ui.ui')
        uic.loadUi(uipath, self)

