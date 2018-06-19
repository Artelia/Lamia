# coding=utf-8
from __future__ import unicode_literals
# from PyQt4 import uic, QtGui
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QDialog, QFileDialog
except:
    from qgis.PyQt.QtWidgets import QDialog, QFileDialog

import os

from queryFranceDigue import *
from queryLamia import *
import json

#faculatitaif
import sys
reload(sys)
sys.setdefaultencoding('utf-8')




def import_sirs():
    import_sirsDialog=ImportSirsDialog()
    import_sirsDialog.exec_()
    user, pwd, ip, port, nom_sirs, path_LAMIA = import_sirsDialog.dialogIsFinished()
    print(user, pwd, ip, port, nom_sirs, path_LAMIA)

    #user = "r.beckprotoy"
    #pwd = "CouchDb"
    #ip = "10.3.38.37"
    #port = "5984"
    #nom_sirs='valence_romans_agglo'
    #path_lamia = '../../DB/test_valence.sqlite'

    FDtL = FranceDiguetoLamia(user,pwd,ip,port,nom_sirs,path_LAMIA)
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
        self.lineEdit_nom_LAMIA.setText('c:\\base_LAMIA.sqlite')
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
            self.lineEdit_nom_LAMIA.setText(reportfile)

    def dialogIsFinished(self):
        return self.lineEdit_user.text(), self.lineEdit_password.text(), self.lineEdit_adresse.text(), self.lineEdit_port.text(), self.lineEdit_nom.text(), self.lineEdit_nom_LAMIA.text()


class FranceDiguetoLamia():

    def __init__(self, user, pwd, ip, port, nom_sirs, path_lamia):
        self.configPATH =  os.path.join(os.path.dirname(__file__), 'jsonConfig/config.json')
        self.bridgePATH =  os.path.join(os.path.dirname(__file__), 'jsonConfig/bridge.json')
        self.convertisseurPATH = os.path.join(os.path.dirname(__file__), 'jsonConfig/convertisseur.json')
        #user = "r.beckprotoy"
        #pwd = "CouchDb"
        #ip = "10.3.38.37"
        #port = "5984"
        #nom_sirs='valence_romans_agglo'
        #path_lamia = '../../DB/test_valence.sqlite'
        self.queryFD = queryFranceDigue(user, pwd, ip, port, nom_sirs)
        self.queryL = queryLamia(path_lamia)


    """
    Insert all the data taken from the CouchDb insert into the Sqlite database
    rtype : none
    """
    def insertInLamia(self):
        config = json.load(open(self.configPATH, 'r'))

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
            if 'query_couch' in config[nom_lm]:
                print(config[nom_lm]['query_couch'])
                for doc in self.queryFD.customQuery(config[nom_lm]['query_couch'],['_id','@class']):
                    print('test',doc)
                    id_fd = doc['_id']

                    #Cas ou le métaObjet est constiutés sur un seul document (Desersordre, Indralineaire)
                    if not id_fd in checkList and not 'list' in config[nom_lm]:
                        metaObj = self.makeMetaObjet(nom_lm, id_fd)
                        id_lm = self.queryL.insertion(nom_lm, metaObj)
                        nom_fd = doc['@class'][19:]

                        self.insertInConvertisseur(convertisseur, id_fd, id_lm, nom_fd, nom_lm)
                        newElem = True

                    #Cas où le metaObjet est constitués sur une liste contentnat les information (Observations, Photos)
                    elif 'list' in config[nom_lm]:
                        arrMetaObjet = self.makeMetaObjet(nom_lm, id_fd)
                        for metaObj in arrMetaObjet:
                            id_lm = self.queryL.insertion(nom_lm, {nom_lm :arrMetaObjet[metaObj]} )
                            nom_fd = doc['@class'][19:]

                            self.insertInConvertisseur(convertisseur, id_fd, id_lm, nom_fd, nom_lm)
                        newElem = True
        if newElem:
            open('output.txt','a').write('--- START ---\n')

            self.setDependencies()
            #Block d'écriture et de fermeture des connexions aux bases
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
        convertisseur = json.load(open(self.convertisseurPATH,'r'))
        bridge = json.load(open(self.bridgePATH, 'r'))

        for obj in bridge:

            for i in range(0, len(bridge[obj])):
                path = bridge[obj][i]['path']
                fld_lm_src = bridge[obj][i]['source']
                tab_lm_dest = bridge[obj][i]['table']

                for it in convertisseur:
                    if obj == it['sql']['type']:

                        id_lm_src = it['sql']['id']
                        id_fd_src = it['couch']['id']

                        doc = self.queryFD.getDocument(id_fd_src)
                        id_fd_dest = self.queryFD.seekIn(doc, path.split(' '))

                        id_lm_dest = self.getObj('couch id', id_fd_dest, convertisseur)['sql']['id']

                        if 'destination' in bridge[obj][i]:
                            fld_lm_dest = bridge[obj][i]['destination']
                            id_lm_dest = self.queryL.selectId(tab_lm_dest, fld_lm_dest, 'id_'+tab_lm_dest, id_lm_dest)

                        self.queryL.updateDependencies(obj, fld_lm_src, 'id_'+obj, id_lm_dest, id_lm_src)

    def resetConvertisseur(self):
        open(self.convertisseurPATH, 'w').write('[]')


