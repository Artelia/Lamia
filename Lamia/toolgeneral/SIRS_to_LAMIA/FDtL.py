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


# coding=utf-8
from __future__ import unicode_literals
# from PyQt4 import uic, QtGui
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QDialog, QFileDialog
except:
    from qgis.PyQt.QtWidgets import QDialog, QFileDialog

import os

from .queryFranceDigue import *
from .queryLamia import *
import json

#faculatitaif
import sys

if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')
elif sys.version_info.major == 3:
    import importlib
    importlib.reload(sys)

def import_sirs():
    import_sirsDialog=ImportSirsDialog()
    import_sirsDialog.exec_()
    user, pwd, ip, port, nom_sirs, path_LAMIA, user_LAMIA, password_LAMIA, adresse_LAMIA, port_LAMIA, nom_LAMIA, srid, type_spatialite, type_postgis  = import_sirsDialog.dialogIsFinished()

    print(user, pwd, ip, port, nom_sirs, path_LAMIA, user_LAMIA, password_LAMIA, adresse_LAMIA, port_LAMIA, nom_LAMIA, srid, type_spatialite, type_postgis)

    #user = "r.beckprotoy"
    #pwd = "CouchDb"
    #ip = "10.3.38.37"
    #port = "5984"
    #nom_sirs='valence_romans_agglo'
    #path_lamia = '../../DB/test_valence.sqlite'

    FDtL = FranceDiguetoLamia(user, pwd, ip, port, nom_sirs, path_LAMIA, user_LAMIA, password_LAMIA, adresse_LAMIA, port_LAMIA, nom_LAMIA, srid, type_spatialite, type_postgis)
    FDtL.insertInLamia()



class ImportSirsDialog(QDialog):
    def __init__(self, parent=None):

        super(ImportSirsDialog, self).__init__(parent)
        #self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), 'PasserelleSIRS_connexion.ui')
        uic.loadUi(path, self)
        self.qfiledlg = QFileDialog()
        self.qfiledlg.setFileMode(QFileDialog.ExistingFile)
        self.qfiledlg.setOption(QFileDialog.DontConfirmOverwrite)
        self.lineEdit_path_LAMIA.setText('c:\\base_LAMIA.sqlite')
        self.checkBox_spatialite.setChecked(True)
        self.pushButton_filechoose.setEnabled(True)
        self.lineEdit_path_LAMIA.setEnabled(True)
        self.lineEdit_user_LAMIA.setEnabled(False)
        self.lineEdit_password_LAMIA.setEnabled(False)
        self.lineEdit_adresse_LAMIA.setEnabled(False)
        self.lineEdit_port_LAMIA.setEnabled(False)
        self.lineEdit_nom_LAMIA.setEnabled(False)
        self.checkBox_spatialite.stateChanged.connect(self.changeStateSpatialite)
        self.checkBox_postgis.stateChanged.connect(self.changeStatePostgis)
        self.pushButton_filechoose.clicked.connect(self.chooseFile)
        self.finished.connect(self.dialogIsFinished)

    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(self,
                                                   'Base LAMIA',
                                                   '',
                                                   'Sqlite (*.sqlite)')
        if reportfile:
            if isinstance(reportfile, tuple):    # qt5
                reportfile = reportfile[0]
            self.lineEdit_path_LAMIA.setText(reportfile)

    def dialogIsFinished(self):
        return self.lineEdit_user.text(), self.lineEdit_password.text(), self.lineEdit_adresse.text(), self.lineEdit_port.text(), self.lineEdit_nom.text(), self.lineEdit_path_LAMIA.text(), self.lineEdit_user_LAMIA.text(), self.lineEdit_password_LAMIA.text(), self.lineEdit_adresse_LAMIA.text(), self.lineEdit_port_LAMIA.text(), self.lineEdit_nom_LAMIA.text(), self.lineEdit_SRID.text(), self.checkBox_spatialite.isChecked(), self.checkBox_postgis.isChecked()


    def changeStatePostgis(self):
        if self.checkBox_spatialite.isChecked() and self.checkBox_postgis.isChecked():
            self.checkBox_spatialite.setCheckState(False)
            self.pushButton_filechoose.setEnabled(False)
            self.lineEdit_path_LAMIA.setEnabled(False)
            self.lineEdit_user_LAMIA.setEnabled(True)
            self.lineEdit_password_LAMIA.setEnabled(True)
            self.lineEdit_adresse_LAMIA.setEnabled(True)
            self.lineEdit_port_LAMIA.setEnabled(True)
            self.lineEdit_nom_LAMIA.setEnabled(True)
        if not self.checkBox_spatialite.isChecked() and not self.checkBox_postgis.isChecked():
            self.checkBox_spatialite.setChecked(True)
            self.pushButton_filechoose.setEnabled(True)
            self.lineEdit_path_LAMIA.setEnabled(True)
            self.lineEdit_user_LAMIA.setEnabled(False)
            self.lineEdit_password_LAMIA.setEnabled(False)
            self.lineEdit_adresse_LAMIA.setEnabled(False)
            self.lineEdit_port_LAMIA.setEnabled(False)
            self.lineEdit_nom_LAMIA.setEnabled(False)

        return


    def changeStateSpatialite(self):
        if self.checkBox_spatialite.isChecked() and self.checkBox_postgis.isChecked():
            self.checkBox_postgis.setCheckState(False)
            self.pushButton_filechoose.setEnabled(True)
            self.lineEdit_path_LAMIA.setEnabled(True)
            self.lineEdit_user_LAMIA.setEnabled(False)
            self.lineEdit_password_LAMIA.setEnabled(False)
            self.lineEdit_adresse_LAMIA.setEnabled(False)
            self.lineEdit_port_LAMIA.setEnabled(False)
            self.lineEdit_nom_LAMIA.setEnabled(False)
        if not self.checkBox_spatialite.isChecked() and not self.checkBox_postgis.isChecked():
            self.checkBox_postgis.setChecked(True)
            self.pushButton_filechoose.setEnabled(False)
            self.lineEdit_path_LAMIA.setEnabled(False)
            self.lineEdit_user_LAMIA.setEnabled(True)
            self.lineEdit_password_LAMIA.setEnabled(True)
            self.lineEdit_adresse_LAMIA.setEnabled(True)
            self.lineEdit_port_LAMIA.setEnabled(True)
            self.lineEdit_nom_LAMIA.setEnabled(True)
        return


class FranceDiguetoLamia():

    def __init__(self, user, pwd, ip, port, nom_sirs, path_LAMIA, user_LAMIA, password_LAMIA, adresse_LAMIA, port_LAMIA, nom_LAMIA, srid, type_spatialite, type_postgis):
        self.configPATH =  os.path.join(os.path.dirname(__file__), 'jsonConfig/config.json')
        self.bridgePATH =  os.path.join(os.path.dirname(__file__), 'jsonConfig/bridge.json')
        self.convertisseurPATH = os.path.join(os.path.dirname(__file__), 'jsonConfig/convertisseur.json')
        #user = "r.beckprotoy"
        #pwd = "CouchDb"
        #ip = "10.3.38.37"
        #port = "5984"
        #nom_sirs='valence_romans_agglo'
        #path_lamia = '../../DB/test_valence.sqlite'
        self.typedb = type_spatialite
        self.srid=srid
        self.queryFD= queryFranceDigue(user, pwd, ip, port, nom_sirs)
        self.queryL = queryLamia(path_LAMIA, srid , user_LAMIA, password_LAMIA, adresse_LAMIA, port_LAMIA, nom_LAMIA, type_spatialite, type_postgis)


    """
    Insert all the data taken from the CouchDb insert into the Sqlite database
    rtype : none
    """
    def insertInLamia(self):
        config = json.load(open(self.configPATH, 'r'))
        self.resetConvertisseur()

        try:
            convertisseur = json.load(open(self.convertisseurPATH, 'r'))
        except ValueError:
            self.resetConvertisseur()
            convertisseur = json.load(open(self.convertisseurPATH, 'r'))

        if len(convertisseur) > 0:
            self.resetConvertisseur()

        newElem = False

        checkList = self.getListObj('couch id', convertisseur)

        for nom_lm in config:
            print("Import de la couche : ", nom_lm)
            if 'query_couch' in config[nom_lm]:
                print(config[nom_lm]['query_couch'])
                for doc in self.queryFD.customQuery(config[nom_lm]['query_couch'],['_id','@class']):
                    print("import des donnees de l objet ou d'un sous objet de l objet :",doc)
                    id_fd = doc['_id']

                    #Cas ou le métaObjet est constiutés sur un seul document (Desersordre, Infralineaire)
                    if not id_fd in checkList and not 'list' in config[nom_lm]:
                        metaObj = self.makeMetaObjet(nom_lm, id_fd)
                        id_lm = self.queryL.insertion(nom_lm, metaObj)
                        nom_fd = doc['@class'][19:]

                        self.insertInConvertisseur(convertisseur, id_fd, id_lm, nom_fd, nom_lm)
                        newElem = True

                    #Cas où le metaObjet est constitués sur une liste contentnat les information (Observations, Photos)
                    elif 'list' in config[nom_lm]:
                        if config[nom_lm]['list'] in self.queryFD.getDocument(id_fd).keys() :
                            arrMetaObjet = self.makeMetaObjet(nom_lm, id_fd)
                            for metaObj in arrMetaObjet:
                                id_lm = self.queryL.insertion(nom_lm, {nom_lm :arrMetaObjet[metaObj]} )
                                nom_fd = doc['@class'][19:]

                                self.insertInConvertisseur(convertisseur, id_fd, id_lm, nom_fd, nom_lm)
                            newElem = True

        if newElem:
            open('output.txt','a').write('--- START ---\n')
            self.queryL.commit()

            #Add version begin and id
            self.setKeys()
            self.queryL.commit()

            #Correct the link between objects and DescriptionSystem
            self.updateDescriptionSystem()

            #Correct the geometry of the table desordres
            self.updateGeomDesordres()

            self.setDependencies()
            #Block d'écriture et de fermeture des connexions aux bases

            #Gestion des photos
            self.importPhotos()


            self.queryL.commit()


            self.setKeysPhotos()
            self.queryL.commit()



            self.queryFD.disconnect()
            self.queryL.disconnect()

            open('output.txt','a').write('--- END ---\n')

    """
    Writing a new object in the convertion json file
    :param convertisseur: file/dict - the current converter file
    :param id_fd: string - the France digue id
    :param id_lm: int - the Lamia id
    :param nom_fd: string - object type
    :param nom_lm: string - object type
    """
    def insertInConvertisseur(self, convertisseur, id_fd, id_lm, nom_fd, nom_lm, alpha = []):
        tmp = {'couch': {'id': id_fd, 'type': nom_fd}, 'sql': {'id': id_lm, 'type': nom_lm}}
        convertisseur.append(tmp)
        open(os.path.join(os.path.dirname(__file__), 'jsonConfig/convertisseur.json'),'w').write(json.dumps(convertisseur))

    """
    Entry point of the recurcive loop for creating a metaObjet
    :param type: string
    :param id: string
    """
    def makeMetaObjet(self, nom_lm, id):
        print("make metaobjet :", nom_lm, id)
        ret = {}
        config = json.load(open(self.configPATH, 'r'))[nom_lm]
        fields = config['fields']
        if 'list' in config:
            indication = config['list']
            for i in range(0, len(self.queryFD.getDocument(id)[indication])):
                for j in range(0, len(fields)):
                    if not re.match('[A-Z]\w+', fields[j]):
                        fields[j] = indication+' '+str(i)+' '+fields[j]
                ret[nom_lm+str(i)] = self.queryFD.getDocFields(id,fields)
        else:
            ret[nom_lm] = self.queryFD.getDocFields(id, fields)
        return ret

    """
    Get all the value pointed by the path, contain in obj
    :param path: string
    :param obj: dict
    """
    def getListObj(self, path, obj):
        path = path.split(' ')
        ret = []
        for it in obj:
            ret.append(it[path[0]][path[1]])
        return ret

    """
    Get one value using the id_search and the path
    :param path: string
    :param id_search: int || string
    :param obj: dict
    """
    def getObj(self, path, id_search, obj):
        path = path.split(' ')
        for it in obj:
            if id_search == it[path[0]][path[1]]:
                return it

    """
    Set all the dependencies using mutliples json files (convertisseur, bridge)
    :param newElem: dict
    """
    def setDependencies(self):
        #Ici on rattache tous les ojets à ceux auxquels ils ne sont pas liés par un heritage direct, par exemple les dersordres aux infralineaires
        convertisseur = json.load(open(self.convertisseurPATH,'r'))
        bridge = json.load(open(self.bridgePATH, 'r'))

        for obj in bridge:
            #Le bridge est constitue ainsi
            #Le nom de chaque dico est celui de la table qu on veut rattacher (par ex desordre)
            #le champ source donne le nom du champ de la clef etrangere dans la table qu on veut rattacher (ici lid_descriptionsystem qui est dans la table desordre)
            #Le champ destination donne le nom de la clef dans la table a laquelle on veut se rattacher (ici lpk_descriptionsystem dans la table Infralineaire qui renvoie a l element de la table descriptionsystem)
            #Le champ table donne la table a laquelle on veut rattacher l objet (ici infralineaire)
            print('obj',obj)

            for i in range(0, len(bridge[obj])):
                print(i)
                path = bridge[obj][i]['path']
                fld_lm_src = bridge[obj][i]['source']
                tab_lm_dest = bridge[obj][i]['table']

                for it in convertisseur:
                    print('it:',it)
                    if obj == it['sql']['type']:
                        id_lm_src = it['sql']['id']
                        id_fd_src = it['couch']['id']

                        doc = self.queryFD.getDocument(id_fd_src)
                        print(path.split(' '))
                        id_fd_dest = self.queryFD.seekIn(doc, path.split(' '))

                        print('id',id_fd_dest)

                        id_lm_dest = self.getObj('couch id', id_fd_dest, convertisseur)['sql']['id']

                        if 'destination' in bridge[obj][i]:
                            fld_lm_dest = bridge[obj][i]['destination']
                            id_lm_dest = self.queryL.selectId(tab_lm_dest, fld_lm_dest, 'id_'+tab_lm_dest, id_lm_dest)

                        self.queryL.updateDependencies(obj, fld_lm_src, 'id_'+obj, id_lm_dest, id_lm_src)


    def resetConvertisseur(self):
        open(self.convertisseurPATH, 'w').write('[]')

    """
    Import les photos de FD
    Va parcourir tous les désordres, leurs observations et leurs photos
    Crée la ressource
    Crée la photo
    Assigne les FK
    """

    def importPhotos(self):
        convertisseur = json.load(open(self.convertisseurPATH, 'r'))

        for desordre in self.queryFD.customQuery( { "@class": "fr.sirs.core.model.Desordre"},['_id','@class']):

            id_desordre= desordre['_id']
            print("traitement des photos du desordre : ", desordre['_id'], "........................................................")

            if 'observations' in self.queryFD.getDocument(id_desordre).keys() :
                for observation in desordre['observations']:
                    print("traitement des photos de l'observation : ", desordre['_id'], observation['id'])
                    if 'photos' in observation.keys():
                        for photo in observation['photos']:
                            print("traitement de la photo : ", photo['id'])


                            #Creation de l'objet
                            print("insertion de l objet")
                            query_to_run = "INSERT INTO Objet (datetimemodification, datetimecreation, libelle) VALUES ("
                            query_to_run=query_to_run+"'"+str(observation['date'])+"', "
                            query_to_run=query_to_run+"'"+str(observation['date'])+"', "
                            query_to_run=query_to_run+"'"+str(photo['designation'])+"') "

                            if self.typedb:
                                self.queryL.SLITEcursor.execute(query_to_run)

                                try:
                                    fetch = self.queryL.SLITEcursor.lastrowid
                                except TypeError:
                                    fetch = 0

                            else:
                                try :
                                    query_to_run = query_to_run+ "RETURNING id_objet"
                                    self.queryL.SLITEcursor.execute(query_to_run)
                                    fetch = self.SLITEcursor.fetchone()[0]
                                except :
                                    print("erreur !", query_to_run)
                                    self.queryL.SLITEcursor.execute(query_to_run)
                                    fetch = 0
                            id_objet_insere = fetch


                            #Creation de la Ressource
                            print("insertion de la ressource")
                            query_to_run = "INSERT INTO Ressource (lpk_objet, description, dateressource, file) VALUES ("
                            query_to_run=query_to_run+"'"+str(id_objet_insere)+"', "
                            query_to_run=query_to_run+"'"+str(photo['designation'])+"', "
                            query_to_run=query_to_run+"'"+str(observation['date'])+"', "
                            query_to_run=query_to_run+"'"+self.traitementCheminPhoto(str(photo['chemin']))+"') "

                            if self.typedb:
                                self.queryL.SLITEcursor.execute(query_to_run)

                                try:
                                    fetch = self.queryL.SLITEcursor.lastrowid
                                except TypeError:
                                    fetch = 0

                            else:
                                try :
                                    query_to_run = query_to_run+ "RETURNING id_ressource"
                                    self.queryL.SLITEcursor.execute(query_to_run)
                                    fetch = self.queryL.SLITEcursor.fetchone()[0]
                                except :
                                    print("erreur !", query_to_run)
                                    self.queryL.SLITEcursor.execute(query_to_run)
                                    fetch = 0
                            id_ressource_inseree = fetch





                            #Insertion dans la Tc
                            print("insertion dans la tc")
                            query_to_run = "INSERT INTO Tcobjetressource (lid_ressource, lid_objet) VALUES ("
                            query_to_run=query_to_run+"'"+str(id_ressource_inseree)+"', "
                            query_to_run=query_to_run+"'"+str(self.fetchObservationConvertisseur(observation['id']))+"') "

                            self.queryL.SLITEcursor.execute(query_to_run)




                            #Creation de la photo
                            print("insertion de la photo")
                            query_to_run = "INSERT INTO Photo (lpk_ressource, geom, typephoto) VALUES ("
                            query_to_run=query_to_run+"'"+str(id_ressource_inseree)+"', "
                            query_to_run=query_to_run+"ST_GeomFromText('POINT("+str(photo['longitudeMin'])+' '+str(photo['latitudeMin'])+")',"+str(self.srid)+"), "
                            query_to_run=query_to_run+"'PHO')"
                            print(query_to_run)
                            self.queryL.SLITEcursor.execute(query_to_run)



        return

    #Modification du chemin pour relocaliser les photos au bon endroit sur le serveur de destination
    def traitementCheminPhoto(self, chemin):
        return chemin

    def fetchObservationConvertisseur(self, id_observation):
        print(id_observation)
        query = "SELECT lpk_objet FROM Observation WHERE source='"+str(id_observation)+"'"

        if self.typedb:
            fetch = self.queryL.SLITEcursor.execute(query).fetchone()[0]

        else:
            self.queryL.SLITEcursor.execute(query)
            fetch = self.queryL.SLITEcursor.fetchone()[0]
        print("id_objet de l observation : ",fetch)
        return fetch


    #Add the id_objet field to the Infralineaires items
    def updateDescriptionSystem(self):
        """
        print("Update DescriptionSystem .................................................................")
        query = "SELECT id_descriptionsystem FROM Descriptionsystem WHERE lpk_objet IS NULL"
        cursor_id_dessys=self.queryL.SLITEcursor.execute(query)

        while True:
            list_id_dessys = cursor_id_dessys.fetchmany(1000)

            if not list_id_dessys:
                break

            for id_dessys_item in list_id_dessys:
                print(id_dessys_item)
                id_dessys = id_dessys_item[0]

                try :
                    query = "SELECT id_objet FROM Noeud WHERE id_descriptionsystem = '"+str(id_dessys)+"'"
                    list_id_noeud=self.queryL.SLITEcursor.execute(query)
                    id_objet_res = list_id_noeud.fetchone()[0]
                    print("noeud", id_objet_res)

                except :
                    query = "SELECT id_objet FROM Infralineaire WHERE id_descriptionsystem = '"+str(id_dessys)+"'"
                    list_id_infra=self.queryL.SLITEcursor.execute(query)
                    id_objet_res = list_id_infra.fetchone()[0]
                    print("infralineaire", id_objet_res)

                query = "UPDATE Descriptionsystem SET id_objet=" + str(id_objet_res)+" WHERE id_descriptionsystem = "+str(id_dessys)
                print(query)
                self.queryL.SLITEcursor.execute(query)

        """
        return

    def updateGeomDesordres(self):

        convertisseur = json.load(open(self.convertisseurPATH,'r'))

        for obj in convertisseur:
            if obj['couch']['type']==obj['sql']['type'] and obj['sql']['type']=="Desordre":

                desordre_couch=self.queryFD.getDocument(obj['couch']['id'])



                if 'borneDebutId' in desordre_couch.keys() and 'borneFinId' in desordre_couch.keys() :

                    geom_borneMin = self.queryFD.getDocument(desordre_couch['borneDebutId'])
                    geom_bornMax = self.queryFD.getDocument(desordre_couch['borneFinId'])

                    latitudeMin = str(geom_borneMin['geometry'][geom_borneMin['geometry'].find('(')+1:geom_borneMin['geometry'].find(' ')])
                    latitudeMax = str(geom_borneMin['geometry'][geom_borneMin['geometry'].find(' ')+1:geom_borneMin['geometry'].find(')')])
                    longitudeMin =str(geom_bornMax['geometry'][geom_bornMax['geometry'].find('(')+1:geom_bornMax['geometry'].find(' ')])
                    longitudeMax =str(geom_bornMax['geometry'][geom_bornMax['geometry'].find(' ')+1:geom_bornMax['geometry'].find(')')])


                else:

                    latitudeMin = str(desordre_couch['latitudeMin'])
                    latitudeMax = str(desordre_couch['longitudeMin'])
                    longitudeMin = str(desordre_couch['latitudeMax'])
                    longitudeMax = str(desordre_couch['longitudeMax'])



                query = "UPDATE Desordre SET geom=ST_GeomFromText('LINESTRING("
                query = query + longitudeMin +' '
                query = query + latitudeMin +', '
                query = query + longitudeMax +' '
                query = query + latitudeMax
                query = query + ")', "+ str(self.srid)+")"
                query = query + " WHERE id_desordre="+str(obj['sql']['id'])

                if 'geometry' in desordre_couch.keys():
                    if desordre_couch['geometry']!="":
                        query = "UPDATE Desordre SET geom=ST_GeomFromText('"
                        query = query + desordre_couch['geometry']
                        query = query + "', "+ str(self.srid)+")"
                        query = query + " WHERE id_desordre="+str(obj['sql']['id'])

                print(query)
                self.queryL.SLITEcursor.execute(query)


        return

    def setKeys(self):


        for table in ['Objet', 'Desordre', 'Infralineaire', 'Equipement', 'Noeud', 'Descriptionsystem', 'Observation'] :
            query = "UPDATE "+table+" SET id_"+table+"= pk_"+table
            print(query)
            self.queryL.SLITEcursor.execute(query)

        query = "UPDATE Objet SET lpk_revision_begin='1'"
        print(query)
        self.queryL.SLITEcursor.execute(query)

    def setKeysPhotos(self):

        for table in ['Photo', 'Ressource', 'Objet'] :
            query = "UPDATE "+table+" SET id_"+table+"= pk_"+table
            print(query)
            self.queryL.SLITEcursor.execute(query)

        query = "UPDATE Objet SET lpk_revision_begin='1'"
        print(query)
        self.queryL.SLITEcursor.execute(query)

        table = 'Tcobjetressource'
        query = "UPDATE "+table+" SET lpk_revision_begin = '1'"
        self.queryL.SLITEcursor.execute(query)