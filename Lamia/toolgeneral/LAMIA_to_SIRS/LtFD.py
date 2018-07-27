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
import re
import qgis

import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')
elif sys.version_info.major == 3:
    import importlib
    importlib.reload(sys)

import time

def export_sirs(self):
    export_sirsDialog=ExportSirsDialog()
    export_sirsDialog.exec_()
    user, pwd, ip, port, nom_sirs, path_LAMIA, user_LAMIA, password_LAMIA, adresse_LAMIA, port_LAMIA, nom_LAMIA, srid, type_spatialite, type_postgis = export_sirsDialog.dialogIsFinished()
    print(user, pwd, ip, port, nom_sirs, path_LAMIA, user_LAMIA, password_LAMIA, adresse_LAMIA, port_LAMIA, nom_LAMIA, srid, type_spatialite, type_postgis)

    #user = "r.beckprotoy"
    #pwd = "CouchDb"
    #ip = "10.3.38.37"
    #port = "5984"
    #nom_sirs='valence_romans_agglo'
    #path_lamia = '../../DB/test_valence.sqlite'


    queryFD = queryFranceDigue(user, pwd, ip, port, nom_sirs)
    queryL = queryLamia(path_LAMIA, srid , user_LAMIA, password_LAMIA, adresse_LAMIA, port_LAMIA, nom_LAMIA, type_spatialite, type_postgis)
    LtFD = LamiatoFranceDigue(queryFD, queryL)
    LtFD.insertInFranceDigue()


class ExportSirsDialog(QDialog):
    def __init__(self, parent=None):

        super(ExportSirsDialog, self).__init__(parent)
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


    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(self,
                                                   'Base LAMIA',
                                                   '',
                                                   'Sqlite (*.sqlite)')
        if reportfile:
            if isinstance(reportfile, tuple):    # qt5
                reportfile = reportfile[0]
            self.lineEdit_path_LAMIA.setText(reportfile)




class LamiatoFranceDigue():

    def __init__(self, queryFD, queryL):
        self.queryFD = queryFD
        self.queryL = queryL
        self.count = 0

        self.templatePATH = path = os.path.join(os.path.dirname(__file__), 'jsonConfig/templates.json')
        self.bridgePATH = path = os.path.join(os.path.dirname(__file__), 'jsonConfig/bridge.json')
        self.convertisseurPATH = os.path.join(os.path.dirname(__file__), 'jsonConfig/convertisseur.json')

    """Insere la donnees recupere depuis Lamia vers FranceDigue"""
    def insertInFranceDigue(self):
        documents = json.load(open(self.templatePATH,'r'))['Document']
        self.resetConvertisseur()

        try:
            convertisseur = json.load(open(self.convertisseurPATH, 'r'))
            self.resetConvertisseur()
        except ValueError:
            self.resetConvertisseur()
            convertisseur = json.load(open(self.convertisseurPATH, 'r'))

        if len(convertisseur) > 0:
            print('Purge de la base CouchDb')


            #self.resetCouchDb()
            self.resetConvertisseur()


            sys.exit()

        template = {}
        checkList = []

        newElem = False
        for i in range(0, len(convertisseur)):
            checkList.append(convertisseur[i]['sql']['id'])

        i = 0
        # start_time = time.time()
        for obj in documents:
            print('obj :',obj)

            template[obj['couch']['type']] = self.makeTemplate(obj['couch']['fields'], obj['sql']['fields'])
            print('template :',template[obj['couch']['type']])

            for metaObj in self.queryL.createMetaObjet(obj['couch']['type'], template, obj['sql']['query']):
                print('metaobjet :', metaObj)
                self.count = 0
                if not metaObj['id'] in checkList :
                    print('metabobjet id :', metaObj['id'])
                    self.setSecondaryDependencies(metaObj['id'], metaObj)

                    id_fd =  self.queryFD.addDocument(metaObj[obj['couch']['type']])['_id']
                    nom_fd = obj['couch']['type']
                    id_lm = metaObj['id']
                    nom_lm = obj['sql']['type']

                    self.insertInConvertisseur(id_fd, id_lm, nom_fd, nom_lm)
                    i += 1
                    newElem = True
                    continue
            #reset du template après creations des n metaObjet
            template = {}


        open('output.txt','a').write('--- START ---\n')
        if newElem:
            print('done :'+str(i)+' elements treated')
            print("threating dependencies")
            self.setPrimaryDependencies()
        else:
            print('done : no elements treadted')
        open('output.txt','a').write('--- STOP ---\n')


        #Add the observations and their pictures
        self.updateDesordreObservationsAndPictures()




        self.queryFD.disconnect()

    """
    Writing a new object in the convertion json file
    :param convertisseur: file/dict - the current converter file
    :param id_fd: string - the France digue id
    :param id_lm: int - the Lamia id
    :param nom_fd: string - object type
    :param nom_lm: string - object type
    """
    def insertInConvertisseur(self, id_fd, id_lm, nom_fd, nom_lm):
        convertisseur = json.load(open(self.convertisseurPATH, 'r'))
        tmp = {'couch': {'id': id_fd, 'type': nom_fd}, 'sql': {'id': id_lm, 'type': nom_lm}}
        convertisseur.append(tmp)
        open(self.convertisseurPATH,'w').write(json.dumps(convertisseur))


    """
    Creer un patron d'un metaObjet via recursivite + differenciation en fonction du type donne dans le json
    :param type: list ou dict - string
    :param fieldsCouch: list of string
    :param fieldsSql: list of string
    :rtype: dict of dict and/or list
    """
    def makeTemplate(self, fieldsCouch, fieldsSql):
        subDocuments = json.load(open(self.templatePATH,'r'))['SubDocument']

        ret = {}

        listIndexSubDoc = self.getListIndexSubDoc(fieldsSql)
        listIndexList = self.getListIndexList(fieldsSql)
        listIndexDict = self.getListIndexDict(fieldsSql)

        for idx in listIndexList:
            ret[fieldsCouch[idx]] = self.makeList(fieldsSql[idx])

        for idx in listIndexDict:
            ret[fieldsCouch[idx]] = self.makeTemplate(fieldsSql[idx].keys(), fieldsSql[idx].values())

        for idx in listIndexSubDoc:
            subDoc = subDocuments[fieldsSql[idx][5:]]
            ret[fieldsSql[idx]] = self.makeTemplate(subDoc['couch']['fields'], subDoc['sql']['fields'])

        if len(fieldsCouch) != len(fieldsSql):
            raise LookupError('Error on : '+fieldsSql[0]+'\nNumber of key '+str(len(fieldsCouch))+'\nNumber of values '+str(len(fieldsSql)))

        for i in range(0, len(fieldsCouch)):
            if i not in listIndexSubDoc and i not in listIndexList and i not in listIndexDict:
                if isinstance(fieldsSql[i], unicode) and 'fld:' in fieldsSql[i]:
                    ret[fieldsCouch[i]] = 'fld: '+str(self.count)
                    self.count += 1
                else:
                    ret[fieldsCouch[i]] = fieldsSql[i]
        return ret

    def makeList(self, fieldsSql):
        subDocuments = json.load(open(self.templatePATH,'r'))['SubDocument']
        listIndexSubDoc = self.getListIndexSubDoc(fieldsSql)
        ret = []

        for idx in listIndexSubDoc:
            subDoc = subDocuments[fieldsSql[idx][5:]]
            ret.append(self.makeTemplate(subDoc['couch']['fields'], subDoc['sql']['fields']))

        for i in range(0, len(fieldsSql)):
            if i not in listIndexSubDoc:
                ret.append(fieldsSql[i])

        return ret

    """
    recupere les index des objets tague comme sous-objet
    :param obj: list of string/int/bool
    :rtype: list of int
    """
    def getListIndexSubDoc(self, fieldsSql):
        ret = []
        for i in range(0, len(fieldsSql)):
            if isinstance(fieldsSql[i], unicode) and re.match('^(sub:)', fieldsSql[i]):
                ret.append(i)
        return ret

    def setSecondaryDependencies(self, id_parent, obj):
        subDocuments = json.load(open(self.templatePATH, 'r'))['SubDocument']
        print('subDoc :',subDocuments)


        listIndexDict = self.getListIndexDict(obj)
        listIndexList = self.getListIndexList(obj)

        for idx in listIndexDict:
            self.setSecondaryDependencies(id_parent, obj[idx])

        for idx in listIndexList:
            self.setSecondaryDependencies(id_parent, obj[idx])



        if isinstance(obj, list):
            for i in range(0, len(obj)):
                if isinstance(obj[i], unicode) and 'crt:' in obj[i]:
                    template = {}
                    tmp = subDocuments[obj[i][5:]]
                    template[obj[i][5:]] = self.makeTemplate(tmp['couch']['fields'], tmp['sql']['fields'])
                    self.count = 0
                    for subMetaObjet in self.queryL.createMetaObjet(obj[i][5:], template, tmp['sql']['query'].format(id_search = id_parent)):
                        #Inscription du sous-Objet dans le convertisseur, afin de le supprimer en cas de purge
                        obj[i] = self.queryFD.addDocument(subMetaObjet[tmp['couch']['type']])['_id']
                        nom_fd = tmp['couch']['type']
                        id_lm = id_parent
                        nom_lm = tmp['sql']['type']
                        self.insertInConvertisseur(obj[i], id_lm, nom_fd, nom_lm)

        if isinstance(obj, dict):
            for it in obj:
                print('dict :',obj)
                if isinstance(obj[it], unicode) and 'crt:' in obj[it]:
                    template = {}
                    tmp = subDocuments[obj[it][5:]]
                    template[obj[it][5:]] = self.makeTemplate(tmp['couch']['fields'], tmp['sql']['fields'])
                    self.count = 0
                    for subMetaObjet in self.queryL.createMetaObjet(obj[it][5:], template, tmp['sql']['query'].format(id_search = id_parent)):
                        #Inscription du sous-Objet dans le convertisseur, afin de le supprimer en cas de purge
                        obj[it] = self.queryFD.addDocument(subMetaObjet[tmp['couch']['type']])['_id']
                        nom_fd = tmp['couch']['type']
                        id_lm = id_parent
                        nom_lm = tmp['sql']['type']
                        self.insertInConvertisseur(obj[it], id_lm, nom_fd, nom_lm)

    """Retourne la liste des index|cles menant vers un dict"""
    def getListIndexDict(self, obj):
        ret = []
        if isinstance(obj, list):
            for i in range(0, len(obj)):
                if isinstance(obj[i], dict):
                    ret.append(i)

        if isinstance(obj, dict):
            for it in obj:
                if isinstance(obj[it], dict):
                    ret.append(it)
        return ret

    """Retourne la liste des index|cles menant vers une list"""
    def getListIndexList(self, obj):
        ret = []
        if isinstance(obj, list):
            for i in range(0, len(obj)):
                if isinstance(obj[i], list):
                    ret.append(i)

        if isinstance(obj, dict):
            for it in obj:
                if isinstance(obj[it], list):
                    ret.append(it)
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
    def getObj(self, path, id_search, tab_search, obj):
        for it in obj:
            if id_search == it[path]['id'] and tab_search == it[path]['type']:
                return it

    """
    Injecte les dependences de cles etrangères dans la CouchDb
    """
    def setPrimaryDependencies(self):
        convertisseur = json.load(open(self.convertisseurPATH, 'r'))
        bridge = json.load(open(self.bridgePATH, 'r'))
        #Recuperation d'un des objets du modèle
        for obj in bridge:
            print(obj+': ')
            #recuperaiton des info contenu dans cet objet
            for i in range(0, len(bridge[obj])):
                path = bridge[obj][i]['path']
                if 'bypass' not in bridge[obj][i]:
                    fld_lm_src = bridge[obj][i]['source']
                    fld_lm_dest = bridge[obj][i]['destination']
                    tab_lm_dest = bridge[obj][i]['table']

                #iteration des objet contenu dans le convertisseur
                for it in convertisseur:

                    if it['couch']['type'] == obj:

                        id_fd_src = it['couch']['id']
                        id_lm_src = it['sql']['id']
                        tab_lm_src = it['sql']['type']

                        #Si l'on cree l'objet de toute pièce
                        if 'bypass' in bridge[obj][i]:
                            for id_fd_dest in self.queryFD.customQuery(bridge[obj][i]['bypass'], ['_id']):
                                if len(id_fd_dest) > 0:
                                    print('bypass: '+str(id_fd_src)+'-->'+str(path)+'-->'+str(id_fd_dest['_id']))
                                    self.queryFD.updateDocument(id_fd_src, path, id_fd_dest['_id'])
                                    continue
                                print('bypass: '+str(id_fd_src)+'-->'+str(path)+'-->'+str(None))
                                self.queryFD.updateDocument(id_fd_src, path, None)
                                continue
                            continue

                        #Recuperation en utilisant l'id
                        id_lm_dest = self.queryL.selectId(tab_lm_dest, tab_lm_src, fld_lm_dest, fld_lm_src, id_lm_src)

                        #Recuperation en utilisant le plus proche voisin
                        if id_lm_dest is None:
                            id_lm_dest = self.queryL.selectClosestGeom(tab_lm_dest, tab_lm_src, fld_lm_dest, fld_lm_src, id_lm_src)

                        if id_lm_dest is not None:
                            id_fd_dest = self.getObj('sql', id_lm_dest, tab_lm_dest, convertisseur)['couch']['id']
                            print('update: '+str(id_fd_src)+'-->'+str(path)+'-->'+str(id_fd_dest))
                            self.queryFD.updateDocument(id_fd_src, path, id_fd_dest)
                        else:
                            print('update: '+str(id_fd_src)+'-->'+str(path)+'-->'+str(None))
                            self.queryFD.updateDocument(id_fd_src, path, None)

    """Reset la CouhcDb"""
    def resetCouchDb(self):
        convertisseur = json.load(open(self.convertisseurPATH, 'r'))
        for i in range(0, len(convertisseur)):
            print(convertisseur[i]['couch']['id'])
            self.queryFD.deleteDocument(convertisseur[i]['couch']['id'])
        self.resetConvertisseur()

    """Reset le convertisseur pour faire une nouvelle insertion dans la couchDb"""
    def resetConvertisseur(self):
        open(self.convertisseurPATH, 'w').write('[]')


    def updateDesordreObservationsAndPictures(self):

        print("Upload Observations .................................................................")
        query = "SELECT id_observation, id_objet, lk_desordre, dateobservation, source, gravite, nombre FROM Observation "
        cursor_obs=self.queryL.SLITEcursor.execute(query)
        convertisseur = json.load(open(self.convertisseurPATH, 'r'))

        while True:
            list_obs = cursor_obs.fetchmany(1000)

            if not list_obs:
                break

            for obs in list_obs :
                id_observation = obs[0]
                id_objet=obs[1]
                lk_desordre=obs[2]
                dateobservation=obs[3]
                source=obs[4]
                gravite=obs[5]
                nombre=obs[6]
                print(obs)

                #Recupere le desordre couch associe avec lk_desordre et le convertisseur
                for item in convertisseur :
                    print('convertisseur',item['couch']['type']==item['sql']['type'], item['sql']['type']=='Desordre')
                    if item['couch']['type']=='Desordre' and item['sql']['type']=='Desordre' and item['sql']['id']==lk_desordre :
                        desordre = self.queryFD.getDocument(item['couch']['id'])

                        #cree la liste des observations si elle n'existe pas pour ce desordre dans couch avec un if not "observations" in keys()
                        if not 'observations' in desordre.keys():
                            desordre['observations']=[]

                        #cree la nouvelle observation sous forme de dic et db.save({'key': 'value'})
                        #Pour cela, commence par traiter les champs de observation
                        new_observation = {}
                        new_observation['@class']='fr.sirs.core.model.Observation'
                        new_observation['valid']='true'
                        new_observation['nombreDesordres']=nombre
                        if gravite is not None and not gravite == -1 and not gravite =='NULL'  :
                            new_observation['urgenceId']='RefUrgence:'+str(gravite)
                        else :
                            new_observation['urgenceId']='RefUrgence:0'
                        new_observation['date']=str(dateobservation)


                        new_observation['photos']=[]

                        query = "SELECT id_tcressource FROM Tcobjetressource WHERE id_tcobjet="+str(id_objet)

                        cursor_ressources=self.queryL.SLITEcursor.execute(query)

                        while True:
                            list_ressources = cursor_ressources.fetchmany(1000)

                            if not list_ressources:
                                break

                            for id_ressource in list_ressources :
                                query = "SELECT o.libelle, r.file  FROM Ressource r, Objet o WHERE o.id_objet = r.id_objet AND r.id_ressource = "+str(id_ressource[0])
                                print(query)
                                cursor_photo=self.queryL.SLITEcursor.execute(query)
                                photo_lamia = cursor_photo.fetchone()
                                if photo_lamia:
                                    print(photo_lamia)

                                    new_photo ={}

                                    new_photo["@class"]= "fr.sirs.core.model.Photo"
                                    new_photo["borne_debut_aval"]= False
                                    new_photo["borne_debut_distance"]= 0
                                    new_photo["prDebut"]= 0
                                    new_photo["borne_fin_aval"]= False
                                    new_photo["borne_fin_distance"]= 0
                                    new_photo["prFin"]=0
                                    new_photo["valid"]= True
                                    new_photo["longitudeMin"]= 0
                                    new_photo["longitudeMax"]= 0
                                    new_photo["latitudeMin"]=0
                                    new_photo["latitudeMax"]= 0
                                    new_photo["geometryMode"]= "LINEAR"
                                    new_photo["designation"]=photo_lamia[0]
                                    new_photo["chemin"]=self.traitement_path_photo(photo_lamia[1])

                                    photo_sirs = self.queryFD.addDocument(new_photo)

                                    new_observation['photos']+=[photo_sirs]

                        observation = self.queryFD.addDocument(new_observation)

                        desordre['observations']+=[observation]
                        print("MAJ :", desordre)
                        #desordre.save()


                    #puis recupere la liste des photos associees à cette observation et les ressources et objets associes
                    #creer la liste des photos et y injecter les photos une a une
                    #Ajouter les photos une a une a la base pour récupérer leur id
                    #Reinjecter cet id dans l observation
                    #ajouter l observation contenant les photos a la base
                    #recuperer l id
                    #completer l observation et l ajouter au desordre

        convertisseur = json.load(open(self.convertisseurPATH, 'r'))
        print("Upload Desordres geometry  .................................................................")

        for item in convertisseur :
            print('convertisseur',item['couch']['type'], item['sql']['type'])
            if item['couch']['type']=='Desordre' and item['sql']['type']=='Desordre' :
                desordre_sirs = self.queryFD.getDocument(item['couch']['id'])
                query = "SELECT ST_AsText(geom), lk_descriptionsystem FROM Desordre WHERE id_desordre = "+str(item['sql']['id'])
                print(query)
                cursor_des=self.queryL.SLITEcursor.execute(query)
                res = cursor_des.fetchone()
                print(res)
                geom=str(res[0])
                lk_description_system = res[1]
                print('desordre_sirs :',desordre_sirs)

                #Process geometry
                if not geom == 'None' :


                    desordre_sirs["geometry"] = geom
                    desordre_sirs['geometryMode'] = 'LINEAR'

                    #type_geom = 0 if point, else linear and =1
                    if 'POINT' in geom :
                        type_geom=0
                    elif 'LINE' in geom :
                        type_geom = 1


                    #Get the part inside the () : list of points
                    geom = geom.split('(')
                    geom = geom[1].split(')')
                    geom=geom[0]

                    #Then get the list of those points
                    if type_geom==0:
                        point_lat = geom.split(' ')[1]
                        point_lon = geom.split(' ')[0]
                        if point_lat[0]==' ':
                            point_lat = point_lat[1:]
                        if point_lat[-1]==' ':
                            point_lat = point_lat[:-1]
                        if point_lon[0]==' ':
                            point_lon = point_lon[1:]
                        if point_lon[-1]==' ':
                            point_lon = point_lon[:-1]


                        lat=[float(point_lat)]
                        lon=[float(point_lon)]
                        list_bornes_desordres=[qgis.core.QgsPoint(lon[0], lat[0])]

                    else :
                        lat=[]
                        lon=[]
                        list_bornes_desordres=[]

                        for point in geom.split(','):
                            if point[0]==' ':
                                point = point[1:]
                            if point[-1]==' ':
                                point = point[:-1]
                            print('point :',point)
                            lat+=[float(point.split(' ')[1])]
                            lon+=[float(point.split(' ')[0])]
                            list_bornes_desordres+=[qgis.core.QgsPoint(lon[-1], lat[-1])]

                    print("1:",lat,lon, list_bornes_desordres)



                    #Get the linear attached to the desordre and the rest of the data injected with it

                    query = "SELECT ST_AsText(geom) FROM Infralineaire WHERE id_descriptionsystem = "+str(lk_description_system)
                    cursor_des=self.queryL.SLITEcursor.execute(query)
                    res = cursor_des.fetchone()[0]
                    geom_troncon_lamia=res[0]

                    id_troncondigue= desordre_sirs['foreignParentId']
                    print('id_troncondigue :',id_troncondigue)


                    #Get the list of points in the referentiel system
                    troncon_FD = self.queryFD.getDocument(desordre_sirs['foreignParentId'])
                    sysrepdefaut = self.queryFD.getDocument(troncon_FD['systemeRepDefautId'])
                    list_bornes_sys_rep = sysrepdefaut['systemeReperageBornes']

                    print('list_bornes :', list_bornes_sys_rep)

                    bornes_sys_rep=[]
                    for id_borne in list_bornes_sys_rep:
                        bornes_sys_rep += [self.queryFD.getDocument(id_borne['borneId'])['geometry']]

                    #process the bornes to get qgis points
                    bornes_points_sys_rep = []
                    for borne in bornes_sys_rep :
                        res = borne.split('(')[1]
                        res = res.split(')')[0]
                        res = qgis.core.QgsPoint(float(res.split(' ')[0]), float(res.split(' ')[1]))
                        bornes_points_sys_rep +=[res]


                    print("2:",troncon_FD,bornes_points_sys_rep)





                    #Process the data
                    if not geom_troncon_lamia == 'None' and id_troncondigue is not None :
                        #Create the begining and ending points of the desordre geometry
                        point_debut=qgis.core.QgsPoint(lon[0],lat[0])
                        point_fin=qgis.core.QgsPoint(lon[-1],lat[-1])




                        #Get the projection of the desordre on the linear

                        print("qgis 1 :",qgis.core.QgsGeometry.fromPolyline(bornes_points_sys_rep).asPolyline())
                        print("qgis 2 :",qgis.core.QgsGeometry.fromPoint(point_debut).asPoint())
                        print("qgis 3 :",qgis.core.QgsGeometry.fromPoint(point_debut).asPoint())
                        projection_beginning = qgis.core.QgsGeometry.fromPolyline(bornes_points_sys_rep).nearestPoint(qgis.core.QgsGeometry.fromPoint(point_debut)).asPoint()
                        desordre_sirs['positionDebut']= "POINT("+str(projection_beginning.x())+" "+str(projection_beginning.y())+")"


                        projection_end = qgis.core.QgsGeometry.fromPolyline(bornes_points_sys_rep).nearestPoint(qgis.core.QgsGeometry.fromPoint(point_fin)).asPoint()
                        desordre_sirs['positionFin']=  "POINT("+str(projection_end.x())+" "+str(projection_end.y())+")"


                        print("5:",desordre_sirs['positionFin'],desordre_sirs['positionDebut'])





                        #Get the closest bornes to the projection and the pos and distance to it

                        k=0
                        index = 0
                        distance = projection_beginning.distance(bornes_points_sys_rep[0])
                        borne_proche = bornes_points_sys_rep[0]
                        for borne_ref in bornes_points_sys_rep :
                            if distance > projection_beginning.distance(borne_ref) :
                                borne_proche = borne_ref
                                distance = projection_beginning.distance(borne_ref)
                                index=k

                            k=k+1


                        desordre_sirs['borneDebutId']= list_bornes_sys_rep[index]['borneId']
                        desordre_sirs['borne_debut_aval']=False
                        desordre_sirs['borne_debut_distance']= projection_beginning.distance(borne_proche)

                        print("6:",list_bornes_sys_rep[index],projection_beginning.distance(borne_proche))




                        k=0
                        index = 0
                        distance = projection_end.distance(bornes_points_sys_rep[0])
                        borne_proche = bornes_points_sys_rep[0]
                        for borne_ref in bornes_points_sys_rep :
                            if distance >= projection_end.distance(borne_ref) :
                                borne_proche = borne_ref
                                distance = projection_end.distance(borne_ref)
                                index=k

                            k=k+1

                        desordre_sirs['borneFinId']= list_bornes_sys_rep[index]['borneId']
                        desordre_sirs['borne_fin_aval']=False
                        desordre_sirs['borne_fin_distance']= projection_end.distance(borne_proche)


                        desordre_sirs['SystemRepId']= troncon_FD['systemeRepDefautId']
                        print("7:",list_bornes_sys_rep[index]['borneId'],projection_end.distance(borne_proche))


                    else :
                        #We just take the begining and the end of the bief

                        desordre_sirs['borneDebutId']= bornes_geom[0]
                        desordre_sirs['borneFinId']= bornes_geom[-1]
                        desordre_sirs['borne_debut_aval']=False
                        desordre_sirs['borne_fin_aval']=False
                        desordre_sirs['borne_debut_distance']= 0
                        desordre_sirs['borne_fin_distance']= 0
                        desordre_sirs['positionDebut']= self.queryFD.getDocument(desordre_sirs['borneDebutId'])['geometry']
                        desordre_sirs['positionFin']= self.queryFD.getDocument(desordre_sirs['borneFinId'])['geometry']
                        desordre_sirs['SystemRepId']= troncon_FD['systemeRepDefautId']


                    print(desordre_sirs)
                    print(desordre_sirs['geometry'])
                    desordre_sirs.save()

        return

    #Update the path to the new ressource folder
    def traitement_path_photo(self, chemin):
        return chemin