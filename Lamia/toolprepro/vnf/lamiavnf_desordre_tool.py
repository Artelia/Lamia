# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_desordre_tool import AbstractDesordreTool
from .lamiavnf_photos_tool import PhotosTool
from .lamiavnf_observation_tool import ObservationTool
# from .lamiavnf_croquis_tool import CroquisTool
import os
import datetime
import qgis




class DesordreTool(AbstractDesordreTool):

    LOADFIRST = True
    dbasetablename = 'Desordre'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(DesordreTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)




    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Desordre'
        self.dbasetablename = 'Desordre'
        #self.visualmode = [1, 2]
        self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        self.magicfunctionENABLED = True

        self.linkagespec = {'Descriptionsystem' : {'tabletc' : None,
                                              'idsource' : 'lk_equipement',
                                            'idtcsource' : None,
                                           'iddest' : 'id_equipement',
                                           'idtcdest' : None,
                                           'desttable' : ['Equipement']}}


        self.pickTable = {'LkDesSys': {'TRONCON': 'IdSys'}}

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

            self.linkuserwdgfield = {'Desordre' : {'linkfield' : 'id_desordre',
                                             'widgets' : {
                                                        'equipement': self.userwdgfield.comboBox_equipement,
                                                         'desordre': self.userwdgfield.comboBox_des_cat,
                                                        'pk_debut': self.userwdgfield.doubleSpinBox_pkdebut,
                                                          'pk_fin': self.userwdgfield.doubleSpinBox_pkfin

                                                        }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}


            # ****************************************************************************************
            # child widgets

            if True:
                self.dbasechildwdgfield = []
                self.propertieswdgOBSERVATION = ObservationTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)


                self.propertieswdgOBSERVATION2 = ObservationTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgOBSERVATION2.NAME = None
                self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgOBSERVATION2)
                self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION2)

                self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self.propertieswdgOBSERVATION2)
                self.propertieswdgPHOTOGRAPHIE.NAME = None
                self.userwdgfield.tabWidget.widget(1).layout().addWidget(self.propertieswdgPHOTOGRAPHIE)

                """
                self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self.propertieswdgOBSERVATION2)
                self.propertieswdgCROQUIS.NAME = None
                self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgCROQUIS)
                """

                #self.propertieswdgOBSERVATION2.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE, self.propertieswdgCROQUIS]
                self.propertieswdgOBSERVATION2.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                try:
                    self.propertieswdgOBSERVATION2.currentFeatureChanged.disconnect()
                except:
                    pass
                for childwdg in self.propertieswdgOBSERVATION2.dbasechildwdgfield:
                    self.propertieswdgOBSERVATION2.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)

            if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Equipement':
                self.pushButton_addFeature.setEnabled(True)
            else:
                self.pushButton_addFeature.setEnabled(False)


                #self.dbasechildwdg = [self.propertieswdgOBSERVATION, self.propertieswdgOBSERVATION2]


    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass
    """
    def magicFunction(self):
        self.featureSelected()
        self.addGPSPoint()
        self.saveFeature()
        self.propertieswdgOBSERVATION2.featureSelected()
        self.propertieswdgOBSERVATION2.saveFeature()



    def postInitFeatureProperties(self, feat):
        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            typeequip = self.parentWidget.currentFeature['equipement']
            typequipindextab = [int(val[1]) for val in self.dbase.dbasetables['Equipement']['fields']['equipement']['Cst']]
            try:
                indexequip = typequipindextab.index(typeequip)
                self.userwdgfield.comboBox_equipement.setCurrentIndex(indexequip)
            except ValueError as e:
                print('postInitFeatureProperties', e)


    def createParentFeature(self):

        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        #print(datecreation)
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        iddesordre = self.currentFeature.id()

        sql = "UPDATE Desordre SET id_objet = " + str(idobjet) + " WHERE id_desordre = " + str(iddesordre) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        if  self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Equipement':
                idequip = self.parentWidget.currentFeature['id_equipement']
                typeequip =self.parentWidget.currentFeature['equipement']
                sql = "UPDATE Desordre SET lk_equipement = " + str(idequip)
                # sql += "equipement = " + str(typeequip)
                sql += " WHERE id_desordre= " + str(self.currentFeature['id_desordre']) + ";"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()

                self.propertieswdgOBSERVATION2.featureSelected(None)
                self.propertieswdgOBSERVATION2.saveFeature()




        if False:   #link nearest descriptionsystem... TODO

            #sql = "SELECT LkDesSys FROM DESORDRE WHERE ID = " + str(iddesordre)
            sql = "SELECT id_tcdescriptionsystem FROM Tcdesordredescriptionsystem WHERE id_tcdesordre = " + str(iddesordre)
            query = self.dbase.query(sql)
            ids = [row[0] for row in query]
            #print(ids)
            #if ids is None:
            if len(ids)==0:
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    geomaswkt = self.currentFeature.geometry().exportToWkt()
                else:
                    geomaswkt = self.currentFeature.geometry().asWkt()

                sql = "SELECT Infralineaire.id_descriptionsystem FROM Desordre "
                sql += "INNER JOIN Infralinemprise ON ST_WITHIN(ST_GeomFromText('" + geomaswkt + "'," + str(
                    self.dbase.crsnumber) + "),Infralinemprise.geom) "
                sql += " AND Desordre.id_desordre = " + str(iddesordre)
                sql += " INNER JOIN Infralineaire ON Infralineaire.id_infralineaire = Infralinemprise.lk_infralineaire"


                # print(sql)
                query = self.dbase.query(sql)
                ids = [row[0] for row in query]

                # print('result',ids)

                if len(ids)>0:
                    sql = "INSERT INTO Tcdesordredescriptionsystem(id_tcdescriptionsystem,id_tcdesordre) VALUES(" + str(ids[0]) + ", " + str(iddesordre) + ");"
                    #sql = "UPDATE DESORDRE SET LkDesSys = " + str(ids[0]) + " WHERE id = " + str(iddesordre) + ";"
                    query = self.dbase.query(sql)
                    self.dbase.commit()



                if False:
                    nearestindex = self.dbase.dbasetables['Infralineaire']['widget'].getNearestIdinBuffer(self.tempgeometry)
                    if nearestindex is not None:
                        feat = self.dbase.dbastables['Infralineaire']['layerqgis'].getFeatures(qgis.core.QgsFeatureRequest(nearestindex)).next()
                        idsys = feat['id_descriptionsystem']
                        sql = "INSERT INTO Tcdesordredescriptionsystem(id_tcdescriptionsystem,id_tcdesordre) VALUES(" + str(idsys) + ", " + str(iddesordre) + ");"
                        #sql = "UPDATE DESORDRE SET LkDesSys = " + str(ids[0]) + " WHERE id = " + str(iddesordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):
        #Ici faire les tests sur les pks et afficher un pop-up avant de supprimer l objet si ces pks n obeissent pas aux regles souhaitees

        correct=False

        pk_debut = float(self.userwdgfield.doubleSpinBox_pkdebut.text().replace(',', '.'))
        pk_fin = float(self.userwdgfield.doubleSpinBox_pkfin.text().replace(',', '.'))

        id_equipement = self.parentWidget.currentFeature['id_equipement']
        id_desordre = self.currentFeature['id_desordre']






        sql = "SELECT pk_debut, pk_fin, typepk FROM Equipement WHERE  id_equipement=" + str(id_equipement) + ";"
        query = self.dbase.query(sql)
        row=query[0]


        if row is not None :
            row = [row[0], row[1], row[2]]
            if row[0] is None :
                row[0]=0
            else :
                row[0]=float(row[0])
            if row[1] is None :
                row[1]=0
            else :
                row[1]=float(row[1])

            pk_debut_bief = float(row[0])
            pk_fin_bief = float(row[1])

            type_pk = row[2]

            #absolu
            if type_pk == 'ABS':
                test_1=pk_debut>pk_fin
                test_2=pk_debut<row[0]
                test_3=pk_fin>row[1]
                test_4= pk_debut>row[1]
                test_5 = pk_fin<row[0]



            #relatif croissant
            elif type_pk=='REC' :
                test_1=pk_debut>pk_fin
                test_2=pk_debut<0
                test_3=pk_fin>(row[1]-row[0])
                test_4= pk_debut>(row[1]-row[0])
                test_5 = pk_fin<0



            #relatif decroissant
            else:
                test_1=pk_debut>pk_fin
                test_2=pk_debut<0
                test_3=pk_fin>(row[1]-row[0])
                test_4= pk_debut>(row[1]-row[0])
                test_5=pk_fin<0



            if test_1 or test_2 or test_3 or test_4 or test_5:
                correct=True
                popup=QtGui.QMessageBox()
                popup.setText('Les pks ne sont pas coherents avec ceux du bief et ont ete corriges en fonction. Pensez a verifier ces pks !')
                popup.exec_()


            if correct:
                if type_pk == 'ABS':

                    if test_2:
                        sql = "UPDATE  Desordre SET pk_debut="+str(row[0])+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()
                        pk_debut=row[0]

                    if test_3:
                        sql = "UPDATE  Desordre SET pk_fin="+str(row[1])+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()
                        pk_fin = row[1]

                    if test_4:
                        sql = "UPDATE  Desordre SET pk_debut="+str(row[1])+", pk_fin = "+str(row[1])+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()
                        pk_debut=row[1]
                        pk_fin=row[1]

                    if test_5:
                        sql = "UPDATE  Desordre SET pk_debut="+str(row[0])+",pk_fin="+str(row[0])+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()
                        pk_debut = row[0]
                        pk_fin = row[0]

                    if pk_debut>pk_fin:
                        sql = "UPDATE  Desordre SET pk_debut="+str(pk_fin)+", pk_fin="+str(pk_debut)+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()
                        pk_transit=pk_debut
                        pk_debut=pk_fin
                        pk_fin = pk_transit

                else :

                    if test_2:
                        sql = "UPDATE  Desordre SET pk_debut="+str(0)+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()
                        pk_debut=0

                    if test_3:
                        sql = "UPDATE  Desordre SET pk_fin="+str(row[1]-row[0])+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        pk_fin=row[1]-row[0]

                    if test_4:
                        sql = "UPDATE  Desordre SET pk_debut="+str(row[1]-row[0])+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()
                        pk_debut=row[1]-row[0]

                    if test_5:
                        sql = "UPDATE  Desordre SET pk_fin="+str(0)+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()
                        pk_fin=0

                    if pk_debut>pk_fin:
                        sql = "UPDATE  Desordre SET pk_debut="+str(pk_fin)+", pk_fin="+str(pk_debut)+" WHERE id_desordre=" + str(id_desordre) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()
                        pk_transit=pk_debut
                        pk_debut=pk_fin
                        pk_fin = pk_transit



        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiavnf_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)


