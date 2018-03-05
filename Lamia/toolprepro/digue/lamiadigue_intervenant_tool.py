# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QInputDialog)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QInputDialog)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import datetime



class IntervenantTool(AbstractInspectionDigueTool):

    LOADFIRST = False
    dbasetablename = 'Intervenant'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(IntervenantTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Gestion'
        self.NAME = 'Intervenants'
        self.dbasetablename = 'Intervenant'
        self.visualmode = [1, 2]
        # self.PointEnabled = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_intervenant',
                                            'idtcsource' : 'id_tcintervenant',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire','Prestation']}
                                            }
        # self.pickTable = None
        # ****************************************************************************************
        #properties ui
        pass

    def initDesktopUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgdesktop is None:
            # ****************************************************************************************
            # userui
            self.userwdgdesktop = UserUI()

            self.linkuserwdgdesktop = {'Intervenant': {'linkfield': 'id_intervenant',
                                                  'widgets': {'nom' : self.userwdgdesktop.lineEdit_nom,
                                                              'societe': self.userwdgdesktop.lineEdit_societe,
                                                              'adresse': self.userwdgdesktop.lineEdit_adresse,
                                                              'fax': self.userwdgdesktop.lineEdit_mail,
                                                              'tel': self.userwdgdesktop.lineEdit_tel,}},
                                'Objet': {'linkfield': 'id_objet',
                                          'widgets': {}}}




    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()

        idobjet = self.dbase.getLastRowId('Objet')

        idintervenant = self.currentFeature.id()

        sql = "UPDATE Intervenant SET id_objet = " + str(idobjet) + " WHERE id_intervenant = " + str(idintervenant) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Marche':
                items = [elem[0] for elem in self.dbasetable['fields']['fonction']['Cst']]
                item, ok = QInputDialog.getItem(self, "Choisir la fonction",
                                                "Choisir la fonction", items, 0, False)
                print(item,ok)
                if ok:
                    fonctionvalue = self.dbase.getConstraintRawValueFromText(self.tablename,'fonction',item)
                    currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                    sql = "INSERT INTO Tcobjetintervenant(id_tcintervenant, id_tcobjet,fonction) VALUES( " + str(idintervenant + "," + currentparentlinkfield + "," + fonctionvalue + ");")
                    #sql = "UPDATE OBSERVATION SET LkDesordre = " + str(currentparentlinkfield) + " WHERE id = " + str(idobservation) + ";"
                    query = self.dbase.query(sql)
                    self.dbase.commit()

    def postSaveFeature(self, boolnewfeature):
        pass

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'IntervenantToolUser.ui')
        uic.loadUi(uipath, self)