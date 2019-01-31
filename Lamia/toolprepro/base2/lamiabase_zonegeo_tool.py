# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QGroupBox,QGridLayout,QLabel,QTableWidgetItem)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QGroupBox,QGridLayout,QLabel,QTableWidgetItem)

#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os
import datetime



class BaseZonegeoTool(AbstractLamiaTool):

    LOADFIRST = False
    dbasetablename = 'Zonegeo'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Gestion'
        self.NAME = 'Zone geographique'
        self.dbasetablename = 'Zonegeo'
        self.visualmode = [ 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetzonegeo' : {'tabletc' : 'Tcobjetzonegeo',
                                              'idsource' : 'id_zonegeo',
                                            'idtcsource' : 'id_tczonegeo',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire']}}
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_zonegeo_tool_icon.svg')
        self.qtreewidgetfields = ['libelle']
        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Zonegeo' : {'linkfield' : 'id_zonegeo',
                                             'widgets' : {
                                                          'typezonegeo':self.userwdgfield.comboBox_type
                                                        }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {
                                                        'libelle' : self.userwdgfield.lineEdit_nom
                                                        }}}

            # rem : il sera affiné le select avec le champ datetimecreation trouvé dans la requete
            # il faut que zone geo soit présent dans la requete
            self.stats = [['Infralineaire lineaire',
                           ''' SELECT SUM(ST_Length(ST_MakeValid(Infralineaire_qgis.geom))) 
                                FROM Infralineaire_qgis, Zonegeo 
                                WHERE ST_WITHIN(ST_MakeValid(Infralineaire_qgis.geom), ST_MakeValid(Zonegeo.geom)) ''']
                           ]

            self.userwdgfield.tableWidget_stats.setRowCount(0)
            self.userwdgfield.tableWidget_stats.setColumnCount(2)
            self.userwdgfield.tableWidget_stats.horizontalHeader().setStretchLastSection(True)
            for i, stat in enumerate(self.stats):
                rowPosition = self.userwdgfield.tableWidget_stats.rowCount()
                self.userwdgfield.tableWidget_stats.insertRow(rowPosition)
                itemfield = QTableWidgetItem(stat[0])
                itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.userwdgfield.tableWidget_stats.setItem(rowPosition, 0, itemfield)



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postInitFeatureProperties(self, feat):

        if feat is not None:

            #stat fill
            for i, stat in enumerate(self.stats) :

                featpk = self.currentFeaturePK
                sql = stat[1]
                if sql != '':
                    sql += ' AND Zonegeo.pk_zonegeo = ' + str(featpk) + ' AND '
                    sql += self.dbase.dateVersionConstraintSQL()
                    """
                    sql += ' AND  Objet.datetimecreation <= ' + "'" + self.dbase.workingdate + "'"
                    if self.dbase.dbasetype == 'postgis':
                        sql += ' AND CASE WHEN Objet.datetimedestruction IS NOT NULL  '
                        sql += 'THEN Objet.datetimedestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
                    elif self.dbase.dbasetype == 'spatialite':
                        sql += ' AND CASE WHEN Objet.datetimedestruction IS NOT NULL  '
                        sql += 'THEN Objet.datetimedestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END '
                    """

                    query = self.dbase.query(sql)
                    #print(query)
                    result = query[0][0]

                    itemresult = QTableWidgetItem(str(result))
                    itemresult.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.userwdgfield.tableWidget_stats.setItem(i, 1, itemresult)




    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:


            # lastrevision = self.dbase.maxrevision
            # datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid) + "," + str(self.dbase.maxrevision) + ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')

        """
        # sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pksys = self.dbase.getLastRowId('Descriptionsystem')
        """

        # idnoeud = self.currentFeature.id()
        pkzonegeo = self.currentFeaturePK
        lastidzonegeo = self.dbase.getLastId('Zonegeo') + 1
        sql = "UPDATE Zonegeo SET id_zonegeo = " + str(lastidzonegeo) + ","
        sql += "lpk_objet = " + str(pkobjet)
        sql += " WHERE pk_zonegeo = " + str(pkzonegeo) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()




    def postSaveFeature(self, boolnewfeature):
        pass


    def deleteParentFeature(self):


        sql = "SELECT pk_objet FROM Zonegeo_qgis WHERE pk_zonegeo = " + str(self.currentFeaturePK)
        pkobjet = self.dbase.query(sql)[0][0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()


        return True


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_zonegeo_tool_ui.ui')
        uic.loadUi(uipath, self)