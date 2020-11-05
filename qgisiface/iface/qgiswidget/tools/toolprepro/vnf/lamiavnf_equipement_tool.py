"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """


# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
"""
from .lamiadigue_photos_tool import PhotosTool
from .lamiadigue_croquis_tool import CroquisTool
"""

from .lamiavnf_ssequipementmain_tool  import EquipementMainTool
from .lamiavnf_photos_tool import PhotosTool
from .lamiavnf_croquis_tool import CroquisTool
from .lamiavnf_desordre_tool import DesordreTool

import os
import datetime



class EquipementTool(AbstractInspectionDigueTool):

    LOADFIRST = True
    dbasetablename = 'Equipement'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(EquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Equipement'
        self.dbasetablename = 'Equipement'
        # self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.visualmode = []
        # self.magicfunctionENABLED = True

        self.linkagespec = {'Infralineaire': {'tabletc': None,
                                           'idsource': 'lk_infralineaire',
                                           'idtcsource': None,
                                           'iddest': 'id_infralineaire',
                                           'idtcdest': None,
                                           'desttable': ['Infralineaire']}}

        # self.pickTable = None
        self.debug = False
        self.qtreewidgetfields = ['equipement', 'pk_debut','pk_fin']


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
            self.linkuserwdgfield = {'Equipement' : {'linkfield' : 'id_equipement',
                                             'widgets' : {'note_ief': self.userwdgfield.spinBox_note_ief,
                                                          'forcage_ree': self.userwdgfield.spinBox_forcage_ree,
                                                          'typepk' : self.userwdgfield.comboBox_typepk,
                                                          'pk_debut': self.userwdgfield.doubleSpinBox_pk_debut,
                                                          'pk_fin': self.userwdgfield.doubleSpinBox_pk_fin,
                                                          'pr_debut': self.userwdgfield.spinBox_pr_debut,
                                                          'pr_fin': self.userwdgfield.spinBox_pr_fin,
                                                          'abs_debut': self.userwdgfield.spinBox_abs_debut,
                                                          'abs_fin': self.userwdgfield.spinBox_abs_fin,
                                                          'is_modified': self.userwdgfield.comboBox_is_modified,
                                                          #'ouvrage': self.userwdgfield.spinBox_ouvrage,
                                                          'partie': self.userwdgfield.comboBox_partie,
                                                          'equipement': self.userwdgfield.comboBox_equipement

                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}
            #self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
            # self.pushButton_addPoint.setEnabled(False)
            # self.pushButton_addLine.setEnabled(False)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            if True:
                # self.propertieswdgSSEQUIPEMENT = EquipementMainToolInstance
                self.propertieswdgEquipement = EquipementMainTool(dbase=self.dbase, gpsutil=self.gpsutil,parentwidget=self)
                self.propertieswdgEquipement.NAME = None
                self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgEquipement)
                self.dbasechildwdgfield.append(self.propertieswdgEquipement)

            if True:
                self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.propertieswdgPHOTOGRAPHIE.NAME = None
                self.userwdgfield.tabWidget.widget(3).layout().addWidget(self.propertieswdgPHOTOGRAPHIE)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)







                self.propertieswdgDESORDRE = DesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.propertieswdgDESORDRE.NAME = None
                self.userwdgfield.tabWidget.widget(4).layout().addWidget(self.propertieswdgDESORDRE)
                self.dbasechildwdgfield.append(self.propertieswdgDESORDRE)


            self.userwdgfield.toolButton_pkdebut.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_pk_debut))
            self.userwdgfield.toolButton_pkfin.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_pk_fin))



            if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Infralineaire':
                self.pushButton_addFeature.setEnabled(True)
            else:
                self.pushButton_addFeature.setEnabled(False)




            """
            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            if self.parentWidget is None:
                #parentwdg = self.dbase.dbasetables['Equipement']['widget']
                self.propertieswdgEQUIPEMENT = EquipementTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

                try:
                    self.currentFeatureChanged.disconnect()
                except:
                    pass
                for childwdg in self.dbasechildwdgfield:
                    self.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)
            """

    """
    def changeCategorie(self,int):
        if 'Ponctuel' in self.userwdg.comboBox_cat.currentText():
            self.userwdg.stackedWidget.setCurrentIndex(1)
            self.pushButton_addPoint.setEnabled(True)
            self.pushButton_addLine.setEnabled(False)
        elif 'Lineaire' in self.userwdg.comboBox_cat.currentText():
            self.userwdg.stackedWidget.setCurrentIndex(0)
            self.pushButton_addPoint.setEnabled(False)
            self.pushButton_addLine.setEnabled(True)
        else:
            self.pushButton_addPoint.setEnabled(False)
            self.pushButton_addLine.setEnabled(False)
    """


    def postOnActivation(self):
        pass

        self.propertieswdgEquipement.postOnActivation()
        #self.propertieswdgSSEQUIPEMENT.postOnActivation()

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            self.userwdgfield.comboBox_partie.setEnabled(True)
            self.userwdgfield.comboBox_equipement.setEnabled(True)
        else:
            self.userwdgfield.comboBox_partie.setEnabled(False)
            self.userwdgfield.comboBox_equipement.setEnabled(False)



    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        # print(datecreation)
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idsys = self.dbase.getLastRowId('Descriptionsystem')

        idreseaulin = self.currentFeature.id()

        sql = "UPDATE Equipement SET id_objet = " + str(idobjet) + ",id_descriptionsystem = " + str(idsys) + " WHERE id_equipement = " + str(idreseaulin) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()

        # print('*********************************')
        #create options
        self.propertieswdgEquipement.disconnectIdsGui()

        typeequiptxt = self.userwdgfield.comboBox_equipement.currentText()
        typequiplist = [elem[0] for elem in self.dbase.dbasetables['Equipement']['fields']['equipement']['Cst']]
        # print('*********************************')
        # print(typeequiptxt)
        # print(typequiplist)
        typeequipindex = typequiplist.index(typeequiptxt)
        typeequip = int(self.dbase.dbasetables['Equipement']['fields']['equipement']['Cst'][typeequipindex][1])
        # print('typeequip', typeequip)
        #typeequip = self.dbase.dbasetables['Equipement']['fields']['equipement']['Cst'][typeequipindex][0]
        #print('typeequip', typeequip)
        #typeequip = self.userwdgfield.comboBox_equipement.currentIndex() + 1
        #print('typeequip', typeequip)
        for constraint in self.dbase.dbasetables['Propriete_option']['fields']['propriete']['Cst']:
            #field = self.dbase.dbasetables['Propriete_option']['fields']['propriete'][proprietekey]
            # print(typeequip, constraint[2])
            if typeequip in constraint[2]:
                # print(constraint)
                self.propertieswdgEquipement.propertieswdgPropriete.featureSelected(None)

                self.propertieswdgEquipement.propertieswdgPropriete.saveFeature(showsavemessage=False)
                sql = "UPDATE Propriete_option SET equipementpropriete = " + str(typeequip) + str(constraint[1]) + ", "
                sql += "propriete = " + str(constraint[1])
                sql += " WHERE id_propriete_option = " + str(self.propertieswdgEquipement.propertieswdgPropriete.currentFeature['id_propriete_option'])
                # print(sql)
                self.dbase.query(sql)
                #self.propertieswdgEquipement.propertieswdgPropriete.currentFeature['equipement'] = typeequip
                #self.propertieswdgEquipement.propertieswdgPropriete.currentFeature['propriete'] = constraint[1]
                #self.propertieswdgEquipement.propertieswdgPropriete.saveFeature()

        self.propertieswdgEquipement.connectIdsGui()



        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Infralineaire':
                currentparentlinkfield = self.parentWidget.currentFeature['id_infralineaire']
                sql = "UPDATE Equipement SET lk_infralineaire = " + str(currentparentlinkfield) + " WHERE id_equipement = " + str(idreseaulin)
                self.dbase.query(sql)
                self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):

        #update treewidget
        itemintree =  self.parentWidget.linkedtreewidget.findItems(self.dbasetablename, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 0)[0]
        print(itemintree.text(0))
        itemtochange = None
        for childitemindex in range(itemintree.childCount()):
            if itemintree.child(childitemindex).text(0) == str(self.currentFeature['id_equipement']):
                itemtochange = itemintree.child(childitemindex)

        for i, elem in enumerate(self.qtreewidgetfields):
            if   itemtochange is not None:
                txttemp = self.dbase.getConstraintTextFromRawValue('Equipement', elem, self.currentFeature[elem])
                itemtochange.setText(i+1, str(txttemp))

        #Ici faire les tests sur les pks et afficher un pop-up avant de supprimer l objet si ces pks n obeissent pas aux regles souhaitees

        correct=False

        pk_debut = float(self.userwdgfield.doubleSpinBox_pk_debut.text().replace(',', '.'))
        pk_fin = float(self.userwdgfield.doubleSpinBox_pk_fin.text().replace(',', '.'))
        type_pk = self.userwdgfield.comboBox_typepk.currentIndex()

        partie_type = self.userwdgfield.comboBox_partie.currentIndex()
        equipement_type = self.userwdgfield.comboBox_equipement.currentIndex()

        test_depassement = partie_type==2 or partie_type==3 or partie_type==4
        test_discontinuite = partie_type==2
        test_chevauchement = ((partie_type==2 or partie_type==3 or partie_type==4) and not (equipement_type==6 or equipement_type==7))

        print(pk_debut, pk_fin)
        print(self.parentWidget)
        print(self.parentWidget.currentFeature.attributes())

        ended = pk_fin != -1

        if self.parentWidget.currentFeature is not None :

            id_infralineaire = self.parentWidget.currentFeature['id_infralineaire']
            id_equipement = self.currentFeature.id()

            sql = "SELECT art_pk_debut, art_pk_fin FROM Infralineaire WHERE  id_infralineaire=" + str(id_infralineaire) + ";"
            query = self.dbase.query(sql)
            row=query[0]


            if row is not None :
                row = [row[0], row[1]]
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



                #absolu
                if type_pk == 0:
                    test_1=pk_debut>pk_fin and ended
                    test_2=pk_debut<row[0]
                    test_3=pk_fin>row[1] and ended
                    test_4= pk_debut>row[1]
                    test_5 = pk_fin<row[0] and ended



                #relatif croissant
                elif type_pk==1 :
                    test_1=pk_debut>pk_fin and ended
                    test_2=pk_debut<0
                    test_3=pk_fin>(row[1]-row[0]) and ended
                    test_4= pk_debut>(row[1]-row[0])
                    test_5 = pk_fin<0 and ended



                #relatif decroissant
                else:
                    test_1=pk_debut>pk_fin and ended
                    test_2=pk_debut<0
                    test_3=pk_fin>(row[1]-row[0]) and ended
                    test_4= pk_debut>(row[1]-row[0])
                    test_5=pk_fin<0 and ended



                if (test_1 or test_2 or test_3 or test_4 or test_5) and test_depassement:
                    correct=True
                    popup=QtGui.QMessageBox()
                    popup.setText('Les pks ne sont pas coherents avec ceux du bief et ont ete corriges en fonction. Pensez a verifier ces pks !')
                    popup.exec_()


                if correct:
                    if type_pk == 0:

                        if test_2:
                            sql = "UPDATE  Equipement SET pk_debut="+str(row[0])+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            self.dbase.commit()
                            pk_debut=row[0]

                        if test_3:
                            sql = "UPDATE  Equipement SET pk_fin="+str(row[1])+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            self.dbase.commit()
                            pk_fin = row[1]

                        if test_4:
                            sql = "UPDATE  Equipement SET pk_debut="+str(row[1])+", pk_fin = "+str(row[1])+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            self.dbase.commit()
                            pk_debut=row[1]
                            pk_fin=row[1]

                        if test_5:
                            sql = "UPDATE  Equipement SET pk_debut="+str(row[0])+",pk_fin="+str(row[0])+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            self.dbase.commit()
                            pk_debut = row[0]
                            pk_fin = row[0]

                        if pk_debut>pk_fin:
                            sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin)+", pk_fin="+str(pk_debut)+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            self.dbase.commit()
                            pk_transit=pk_debut
                            pk_debut=pk_fin
                            pk_fin = pk_transit

                    else :

                        if test_2:
                            sql = "UPDATE  Equipement SET pk_debut="+str(0)+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            self.dbase.commit()
                            pk_debut=0

                        if test_3:
                            sql = "UPDATE  Equipement SET pk_fin="+str(row[1]-row[0])+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            pk_fin=row[1]-row[0]

                        if test_4:
                            sql = "UPDATE  Equipement SET pk_debut="+str(row[1]-row[0])+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            self.dbase.commit()
                            pk_debut=row[1]-row[0]

                        if test_5:
                            sql = "UPDATE  Equipement SET pk_fin="+str(0)+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            self.dbase.commit()
                            pk_fin=0

                        if pk_debut>pk_fin:
                            sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin)+", pk_fin="+str(pk_debut)+" WHERE id_equipement=" + str(id_equipement) + ";"
                            query = self.dbase.query(sql)
                            self.dbase.commit()
                            pk_transit=pk_debut
                            pk_debut=pk_fin
                            pk_fin = pk_transit





                sql = "SELECT partie, equipement FROM Equipement WHERE  id_equipement=" + str(id_equipement) + ";"
                query = self.dbase.query(sql)
                row=query[0]

                partie= row[0]
                equipement = row[1]

                print(pk_debut, pk_fin)


                sql = "SELECT pk_debut, pk_fin, typepk FROM Equipement WHERE  lk_infralineaire='" + str(id_infralineaire) + "'AND equipement = '"+str(equipement)+"'AND partie = '"+str(partie)+"';"
                query = self.dbase.query(sql)
                modified = test_chevauchement
                message_needed=False
                while modified :
                    modified = False
                    for result in query :
                        if result is not None :

                            if result[0] is not None :
                                pk_debut_autre_equipement = float(result[0])
                            else:
                                pk_debut_autre_equipement=0

                            if result[1] is not None :
                                pk_fin_autre_equipement = float(result[1])
                                autre_equipement_ended=True
                            else :
                                pk_fin_autre_equipement=0
                                autre_equipement_ended=False

                            type_pk_autre_equipement = result[2]

                            if autre_equipement_ended and ended:

                                if type_pk_autre_equipement=='REC':
                                    pk_debut_autre_equipement= pk_debut_autre_equipement+pk_debut_bief
                                    pk_fin_autre_equipement = pk_fin_autre_equipement+pk_debut_bief

                                elif type_pk_autre_equipement=='RED':
                                    pk_debut_autre_equipement= pk_fin_bief-pk_fin_autre_equipement
                                    pk_fin_autre_equipement = pk_fin_bief-pk_debut_autre_equipement


                                if type_pk==1:
                                    pk_debut= pk_debut+pk_debut_bief
                                    pk_fin = pk_fin+pk_debut_bief

                                elif type_pk_autre_equipement==2:
                                    pk_debut= pk_fin_bief-pk_fin
                                    pk_fin = pk_fin_bief-pk_debut



                                if pk_debut<pk_debut_autre_equipement and pk_fin>pk_debut_autre_equipement:

                                    if type_pk_autre_equipement=='REC':
                                        sql = "UPDATE  Equipement SET pk_fin="+str(pk_debut_autre_equipement-pk_debut_bief)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                    elif type_pk_autre_equipement=='RED':
                                        sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_bief-pk_debut_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                    else :
                                        sql = "UPDATE  Equipement SET pk_fin="+str(pk_debut_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"


                                    message_needed=True
                                    modified = True
                                    query = self.dbase.query(sql)
                                    self.dbase.commit()
                                    pk_fin = pk_debut_autre_equipement




                                if pk_debut>pk_debut_autre_equipement and pk_fin<pk_fin_autre_equipement:

                                    if type_pk_autre_equipement=='REC':
                                        sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement-pk_debut_bief)+", pk_fin = "+str(pk_fin_autre_equipement-pk_debut_bief)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                    elif type_pk_autre_equipement=='RED':
                                        sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_bief-pk_debut_autre_equipement)+", pk_fin = "+str(pk_fin_bief-pk_debut_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                    else :
                                        sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement)+", pk_fin = "+str(pk_fin_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"


                                    message_needed=True
                                    modified = True
                                    query = self.dbase.query(sql)
                                    self.dbase.commit()
                                    pk_fin = pk_fin_autre_equipement
                                    pk_debut = pk_fin_autre_equipement




                                if pk_debut<pk_fin_autre_equipement and pk_fin>pk_fin_autre_equipement:

                                    if type_pk_autre_equipement=='REC':
                                        sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement-pk_debut_bief)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                    elif type_pk_autre_equipement=='RED':
                                        sql = "UPDATE  Equipement SET pk_fin="+str(pk_fin_bief-pk_fin_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                    else :
                                        sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"


                                    message_needed=True
                                    modified = True
                                    query = self.dbase.query(sql)
                                    self.dbase.commit()
                                    pk_debut = pk_fin_autre_equipement




                                if pk_debut<pk_debut_autre_equipement and pk_fin>pk_fin_autre_equipement:

                                    if type_pk_autre_equipement=='REC':
                                        sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement-pk_debut_bief)+", pk_fin = "+str(pk_fin_autre_equipement-pk_debut_bief)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                    elif type_pk_autre_equipement=='RED':
                                        sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_bief-pk_debut_autre_equipement)+", pk_fin = "+str(pk_fin_bief-pk_debut_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                    else :
                                        sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement)+", pk_fin = "+str(pk_fin_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"


                                    message_needed=True
                                    modified = True
                                    query = self.dbase.query(sql)
                                    self.dbase.commit()
                                    pk_fin = pk_fin_autre_equipement
                                    pk_debut = pk_fin_autre_equipement

                                if type_pk==1:
                                    pk_debut= pk_debut-pk_debut_bief
                                    pk_fin = pk_fin-pk_debut_bief

                                elif type_pk_autre_equipement==2:
                                    pk_debut= pk_fin_bief-pk_fin
                                    pk_fin = pk_fin_bief-pk_debut


                if message_needed:
                    popup=QtGui.QMessageBox()
                    popup.setText('Les pks saisis entrent en conflit avec ceux d un autre equipement du meme type et ont donc ete corriges en fonction. Pensez a verifier ces pks !')
                    popup.exec_()

        #self.updateTableParties()


                if test_discontinuite:
                    print(pk_debut, pk_fin)
                    sql = "SELECT pk_debut, pk_fin, typepk FROM Equipement WHERE  lk_infralineaire='" + str(id_infralineaire) + "'AND equipement = '"+str(equipement)+"'AND partie = '"+str(partie)+"';"
                    query = self.dbase.query(sql)
                    modified = True
                    message_needed=False
                    while modified :
                        modified = False
                        for result in query :
                            if result is not None :

                                if result[0] is not None :
                                    pk_debut_autre_equipement = float(result[0])
                                else:
                                    pk_debut_autre_equipement=0

                                if result[1] is not None :
                                    pk_fin_autre_equipement = float(result[1])
                                    autre_equipement_ended=True
                                else :
                                    pk_fin_autre_equipement=0
                                    autre_equipement_ended=False

                                if autre_equipement_ended and ended:

                                    if type_pk_autre_equipement=='REC':
                                        pk_debut_autre_equipement= pk_debut_autre_equipement+pk_debut_bief
                                        pk_fin_autre_equipement = pk_fin_autre_equipement+pk_debut_bief

                                    elif type_pk_autre_equipement=='RED':
                                        pk_debut_autre_equipement= pk_fin_bief-pk_fin_autre_equipement
                                        pk_fin_autre_equipement = pk_fin_bief-pk_debut_autre_equipement

                                    if type_pk==1:
                                        pk_debut= pk_debut+pk_debut_bief
                                        pk_fin = pk_fin+pk_debut_bief

                                    elif type_pk_autre_equipement==2:
                                        pk_debut= pk_fin_bief-pk_fin
                                        pk_fin = pk_fin_bief-pk_debut

                                        print(pk_debut, pk_fin, pk_debut_autre_equipement, pk_fin_autre_equipement)

                                    if pk_debut<pk_fin_autre_equipement and pk_fin<pk_fin_autre_equipement:

                                        if type_pk_autre_equipement=='REC':
                                            sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement-pk_debut_bief)+", pk_fin = "+str(pk_fin_autre_equipement-pk_debut_bief)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                        elif type_pk_autre_equipement=='RED':
                                            sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_bief-pk_debut_autre_equipement)+", pk_fin = "+str(pk_fin_bief-pk_debut_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                        else :
                                            sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement)+", pk_fin = "+str(pk_fin_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"


                                        message_needed=True
                                        modified = True
                                        query = self.dbase.query(sql)
                                        self.dbase.commit()
                                        pk_fin = pk_fin_autre_equipement
                                        pk_debut = pk_fin_autre_equipement


                                    if pk_debut<pk_fin_autre_equipement and pk_fin>pk_fin_autre_equipement:

                                        if type_pk_autre_equipement=='REC':
                                            sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement-pk_debut_bief)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                        elif type_pk_autre_equipement=='RED':
                                            sql = "UPDATE  Equipement SET pk_fin="+str(pk_fin_bief-pk_fin_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                        else :
                                            sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"


                                        message_needed=True
                                        modified = True
                                        query = self.dbase.query(sql)
                                        self.dbase.commit()
                                        pk_debut = pk_fin_autre_equipement

                                    if pk_debut>pk_fin_autre_equipement :

                                        if type_pk_autre_equipement=='REC':
                                            sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement-pk_debut_bief)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                        elif type_pk_autre_equipement=='RED':
                                            sql = "UPDATE  Equipement SET pk_fin="+str(pk_fin_bief-pk_fin_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"
                                        else :
                                            sql = "UPDATE  Equipement SET pk_debut="+str(pk_fin_autre_equipement)+" WHERE id_equipement=" + str(id_equipement) + ";"


                                        message_needed=True
                                        modified = True
                                        query = self.dbase.query(sql)
                                        self.dbase.commit()
                                        pk_debut = pk_fin_autre_equipement


                                    if type_pk==1:
                                        pk_debut= pk_debut-pk_debut_bief
                                        pk_fin = pk_fin-pk_debut_bief

                                    elif type_pk_autre_equipement==2:
                                        pk_debut= pk_fin_bief-pk_fin
                                        pk_fin = pk_fin_bief-pk_debut


                    if message_needed:
                        popup=QtGui.QMessageBox()
                        popup.setText('Les pks saisis ne resepctent pas la continuite des equiepements du meme type et ont donc ete corriges en fonction. Pensez a verifier ces pks !')
                        popup.exec_()


        pass


    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']

        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True



    """
    def postDeleteFeature(self):
        idobjet = self.currentFeature['IdObjet']
        datesuppr = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "UPDATE Objet SET datedestruction = '" + datesuppr + "'  WHERE id_objet = " + str(idobjet) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()
    """


    """
    def updateTableParties(self):
        #dic_parties : (num_ouvrage, partie) -> [[pk_debut, pk_fin], [pk_debut, pk_fin], [pk_debut, pk_fin], ...]


        dic_parties={}

        sql = "SELECT partie, ouvrage, pk_debut, pk_fin, typepk, lk_infralineaire FROM Equipement"
        equipements = self.dbase.query(sql)

        #Treat each equipement
        for equipement in equipements :
            partie = equipement[0]
            ouvrage = equipement[1]

            pk_debut = equipement[2]
            pk_fin = equipement[3]

            type_pk = equipement[4]

            #Get the real pk
            if type_pk != 'ABS':
                sql = lk_infralineaire

                sql = "SELECT art_pk_debut, art_pk_fin FROM Infralineaire WHERE id_infralineaire ="+str(equipement[5])
                pks_bief = self.dbase.query(sql)[0]


                if type_pk == 'REC':
                    pk_debut=pks_bief[0]+pk_debut
                    pk_fin=pks_bief[0]+pk_fin

                else :
                    pk_debut=pks_bief[1]-pk_fin
                    pk_fin=pks_bief[1]-pk_debut



            #Really analyse the equipement


            if (ouvrage, partie) in dic_parties :
                i=0
                for item in dic_parties[(ouvrage, partie)] :
                    if pk_debut<item[0] and pk_fin>item[0] :
                        dic_parties[(ouvrage, partie)][i][0]=pk_debut
                    if pk_debut<item[1] and pk_fin>item[1] :
                        dic_parties[(ouvrage, partie)][i][1]=pk_fin

                    i=i+1



            else :
                dic_parties[(ouvrage, partie)] = [[pk_debut, pk_fin]]



        pass
    """

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiavnf_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)
