        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()


#def amc(list_travaux, list_params_travaux, list_params_desordre, list_params_infra, list_poids):
def amc(list_travaux, list_params, list_poids):
    #Ici, list_params est une liste de noms de paramètres
    #list_poids est une liste de listes de tuples. Chaque paramètre a une liste de tuple (valeur, note) associées à chaque valeur possible
    #l'indice a prendre est le second élément du tuple dont le premier élément est la valeur pour le tronçon étudié au sein de la list_poids correpsondant au paramètre étudié
    list_travauxPonderes = []
    # On calcule une liste de travaux notés
    for travaux in list_travaux :
        note = 0
        i = 0

        #On récupère toutes les valeurs des paramètres avec une unique requête
        sql = "SELECT list_params FROM (((((Travaux FULL JOIN Observation ON Travaux.lk_observation = Observation.id_observation) "
        + "FULL JOIN Desordre ON Observation.lk_desordre = Desordre.id_desordre) FULL JOIN DescriptionSystem ON Desordre.lk_DescriptionSystem = DescriptionSystem.id_DescriptionSystem)"
        + " FULL JOIN Infralineaire ON DescriptionSystem.id_descriptionSystem= Infralineaire.id_descriptionSystem) FULL JOIN Noeud ON DescriptionSystem.id_descriptionSystem= Noeud.id_descriptionSystem)"
        query = self.dbase.query(sql)

        for param in query :
            for poids in list_poids[i]:
                if param==poids[0]:
                    note = note + poids[1]
                    break
            i+=1
        list_travauxPonderes = list_travauxPonderes + [travaux, note]

    return(list_travauxPonderes)

        """
        sql = "SELECT "
        for param in list_params_travaux:
            #On récupère la liste des valeurs pour les travaux en question
            sql += param + ", "
        sql = sql[:-2] + " FROM Travaux WHERE Travaux.id_travaux = " + str(travaux)
        query = self.dbase.query(sql)

        for param in query:
            #On calcule la somme pondérée avec les critères des travaux
            for poids in list_poids[i]:
                if param==poids[0]:
                    note = note + poids[1]
                    break
            i=i+1


        sql = "SELECT "
        for param in list_params_desordre:
            #On récupère la liste des valeurs pour le désordre associé
            sql += param + ", "
        sql = sql[:-2] + " FROM Desordre WHERE Desordre.lk_travaux = " + str(travaux)
        query = self.dbase.query(sql)

        for param in query:
            #On calcule la somme pondérée avec les critères des travaux
            for poids in list_poids[i]:
                if param==poids[0]:
                    note = note + poids[1]
                    break
            i=i+1






        for param in list_params_desordre:
            #On calcule la somme pondérée avec les critères du désordre
            for poids in list_poids[i]:
                if travaux.desordre.param==poids[0]:
                    note = note + poids[1]
            i=i+1
        for param in list_params_infra:
            #On calcule la somme pondérée avec les critères de l'infra
            for poids in list_poids[i]:
                if travaux.desordre.indra.param==poids[0]:
                    note = note + poids[1]
            i=i+1
        list_travauxPonderes = list_travauxPonderes + [travaux, note]

    #On trie la liste des travaux par note décroissante
    list_travauxPonderes.sort(key=lambda x: x[1], reverse=True)
"""

def getEcheance(list_travauxPonderes, seuils=[10,15,25,50], annees=[10,5,3,1]):
    res=[]
    for travaux in list_travauxPonderes:
        i=0
        for seuil in seuils:
            if travaux[1]<seuil:
                echeance = annees[i]
            else :
                echeance=annees[-1]*2
            i+=1
        res=res+[(travaux[0],travaux[1],echeance)]
        travaux[0].estimationecheance=echeance



def etablirStrat(list_travauxHierarchisee, budgets, scenario, nb_annees, report, seuil, degressif):
    list_years=[]
    year=0

    while year<nb_annees:


        if scenario == 1:
            #On fait des travaux en utilisant tout le budget
            for travaux in list_travauxHierarchisee:
                sql = "SELECT travaux.estimationcouts FROM Travaux WHERE Travaux.id_travaux="+str(travaux)
                query = self.dbase.query(sql)
                if query[0]<budgets[year]:
                    budgets[year]=budgets[year]-query[0]
                    list_years[year]=list_years[year]+[travaux]


        if scenario == 2:
            #On fait des travaux si la note est suppérieure au seuil
            for travaux in list_travauxHierarchisee:
                sql = "SELECT travaux.estimationcouts, travaux.urgence FROM Travaux WHERE Travaux.id_travaux="+str(travaux)
                query = self.dbase.query(sql)
                if travaux.query[1]>seuil:
                    budgets[year]=budgets[year]-query[0]
                    list_years[year]=list_years[year]+[travaux]



        if scenario == 3:
            #On fait des travaux si la note est suppérieure au seuil dégressif
            for travaux in list_travauxHierarchisee:
                sql = "SELECT travaux.estimationcouts, travaux.urgence FROM Travaux WHERE Travaux.id_travaux="+str(travaux)
                query = self.dbase.query(sql)
                if travaux.query[1]>seuil-year*degressif:
                    budgets[year]=budgets[year]-query[0]
                    list_years[year]=list_years[year]+[travaux]


        if scenario == 4:
            #On fait des travaux si la note est suppérieure au seuil et possible avec le budget
            for travaux in list_travauxHierarchisee:
                sql = "SELECT travaux.estimationcouts, travaux.urgence FROM Travaux WHERE Travaux.id_travaux="+str(travaux)
                query = self.dbase.query(sql)
                if travaux.query[1]>seuil and travaux.query[0]<budgets[year]:
                    budgets[year]=budgets[year]-query[0]
                    list_years[year]=list_years[year]+[travaux]



        if scenario == 5:
            #On fait des travaux si la note est suppérieure au seuil dégressif et possible avec le budget
            for travaux in list_travauxHierarchisee:
                sql = "SELECT travaux.estimationcouts, travaux.urgence FROM Travaux WHERE Travaux.id_travaux="+str(travaux)
                query = self.dbase.query(sql)
                if travaux.query[1]>seuil-year*degressif and travaux.query[0]<budgets[year]:
                    budgets[year]=budgets[year]-query[0]
                    list_years[year]=list_years[year]+[travaux]



        if report and year+1!=nb_annees:
            budgets[year+1]=budgets[year+1]+budgets[year]
        year=year+1

    return(list_years, budgets)




def getData(list_travaux, typeData):
    #On utilise les valeurs par défaut
    if typeData=='digues':
        list_params=[]
        list_poids=[]

    elif typeData=='eauPotable':
        list_params=['Materiau', 'TypeMateriau', 'AgeCanalisation','QualitéEau', 'TemperatureEau','OrigineCasse' ,'DensitéRepartition', 'CorrosivitéSolEtProtection', 'ImplantationCanalisation', 'Diamètre', 'Criticité', 'VariationP', 'AgeEau', 'TauxChlore']
        list_poids=[]

    elif typeData=='assainissement':
        list_params=[]
        list_poids=[]


return(list_travaux, list_params, list_poids)


def renouveau(list_poids_criteres, list_poids_sous_criteres):
    list_params=['materiau', 'anPoseSup', 'diametreNominal','qualiteEau', 'temperatureEau','origineCasse' ,'densiteRepartition','protection', 'corrosivitéSol', 'ImplantationCanalisation', 'criticite', 'variationP', 'ageEau', 'tauxChlore', 'id_infralineaire']
    res=[]

    #list_poids_criteres : Caractéristiques de la conduite, Caractéristiques de l'eau distribuée, Caractéristiques des casses, Environnement de la conduite, Vulnerabilite des réseaux, Fonctionnement des réseaux
    #list_poids_sous_criteres : Matériau, Age canalisation, Qualité eau distribuée (agressive), Température eau distribuée , Origine casse, Densité de réparation (nb/km/an), Corrosivité sol + protection contre la corrosion, Implantation canalisation, Diamètre, Criticité, Variation de pression, Age de l'eau, Taux de chlore

    test= True
    while test:
        test=False
        self.importobjetdialog.tableWidget.setRowCount(0)
        self.importobjetdialog.tableWidget.setColumnCount(2)
        for param in list_params:
            rowPosition = self.importobjetdialog.tableWidget.rowCount()
            self.importobjetdialog.tableWidget.insertRow(rowPosition)
            itemfield = QTableWidgetItem(param)
            itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.importobjetdialog.tableWidget.setItem(rowPosition, 0, itemfield)
            itemfield = QTableWidgetItem('')
            self.importobjetdialog.tableWidget.setItem(rowPosition, 1, itemfield)


        self.importobjetdialog.exec_()
        tableview = self.importobjetdialog.dialogIsFinished()
        if tableview is not None:
            result = []
            for row in range(self.importobjetdialog.tableWidget.rowCount()):
                if self.importobjetdialog.tableWidget.cellWidget(row, 1) is not None:
                    try:
                        result.append([self.importobjetdialog.tableWidget.item(row,0).text(),
                                       int(self.importobjetdialog.tableWidget.cellWidget(row, 1).currentText())])
                    except:
                        test=True
                        result.append([self.importobjetdialog.tableWidget.item(row,0).text(),
                                       int(self.importobjetdialog.tableWidget.cellWidget(row, 1).currentText())])
                else:
                    result.append([self.importobjetdialog.tableWidget.item(row,0).text(),
                                   self.importobjetdialog.tableWidget.item(row,1).text()])

    print(result)


    sql = "SELECT "+','.join(list_params)+" FROM Infralineaire"
    query = self.dbase.query(sql)

    for troncon in query:
        for i, item in enumerate(troncon):
            try:
                troncon[i]=int(item)
            except:
                troncon[i]=str(item)

        note = 0
        type_materiau = 0
        age = datetime.datetime.now()-datetime.datetime.strptime(troncon[1], '%Y-%m-%d')

        #MATERIAU

        if troncon[0]=="11":
            type_materiau = 2
            note_materiau = 4
        elif troncon[0]=="24" or troncon[0]=="25" or troncon[0]=="26" or troncon[0]=="27"  :
            type_materiau = 1
            note_materiau = 2
        elif troncon[0]=="16" or troncon[0]=="17" or troncon[0]=="18" :
            type_materiau = 1
            note_materiau = 2
        elif troncon[0]=="12":
            type_materiau = 2
            note_materiau = 10
        elif troncon[0]=="02":
            type_materiau = 0
            note_materiau = 10
        elif troncon[0]=="Composite":
            type_materiau = 0
            note_materiau = 4
        elif troncon[0]=="01":
            type_materiau = 2
            note_materiau = -10000
        elif troncon[0]=="07" or troncon[0]=="19":
            type_materiau = 2
            note_materiau = -10000
        elif troncon[0]=="08" or troncon[0]=="09" or troncon[0]=="10":
            type_materiau = 0
            note_materiau = 0
        elif troncon[0]=="14" :
            type_materiau = 0
            note_materiau = 0
        elif troncon[0]=="15":
            type_materiau = 0
            note_materiau = 0
        elif troncon[0]=="28":
            type_materiau = 2
            note_materiau = -10000
        elif troncon[0]=="20"or troncon[0]=="21" :
            type_materiau = 1
            note_materiau = 1
        elif troncon[0]=="22"or troncon[0]=="23" :
            type_materiau = 1
            note_materiau = 1
        elif troncon[0]=="13":
            type_materiau = 0
            note_materiau = -10000
        elif troncon[0]=="03" or troncon[0]=="04" or troncon[0]=="05" or troncon[0]=="06" :
            type_materiau = 0
            note_materiau = -10000
        elif troncon[0]=="00" or troncon[0]=="99":
            type_materiau = 0
            note_materiau = 0

        if type_materiau==0:
            #Sol
            note_sol=0
            #AGE
            if age<10:
                note_age =0
            elif age<20:
                note_age =2
            elif age<30:
                note_age =4
            elif age<40:
                note_age =6
            elif age<60:
                note_age =8
            else :
                note_age =10

            #DIAMETRE
            if troncon[2]<=100:
                note_diametre =6
            elif troncon[2]<=150:
                note_diametre =8

        elif type_materiau==1:
            #Sol
            note_sol=0
            #AGE
            if age<10:
                note_age = 2
            elif age<20:
                note_age =2
            elif age<30:
                note_age =2
            elif age<40:
                note_age =2
            elif age<60:
                note_age =2
            else :
                note_age =6

            #DIAMETRE
            if troncon[2]<=25:
                note_diametre =1
            elif troncon[2]<=40:
                note_diametre =2
            elif troncon[2]<=50:
                note_diametre =2
            elif troncon[2]<=63:
                note_diametre =3
            elif troncon[2]<=75:
                note_diametre =4
            elif troncon[2]<=90:
                note_diametre =4
            elif troncon[2]<=110:
                note_diametre =5
            elif troncon[2]<=125:
                note_diametre =6
            elif troncon[2]<=140:
                note_diametre =7
            elif troncon[2]<=160:
                note_diametre =8
            elif troncon[2]<=200:
                note_diametre =9
            elif troncon[2]<=225:
                note_diametre =10


        elif type_materiau==2:
            #Sol

            #Protection
            note_protection=troncon[7]

            #CorrosivitéSol
            if troncon[8] == '1':
                note_aggressivite_sol=2
                elif troncon[8]=='2':
                note_aggressivite_sol=1
                elif troncon[8]=='3':
                note_aggressivite_sol=1
                elif troncon[8]=='4':
                note_aggressivite_sol=1
                elif troncon[8]=='5':
                note_aggressivite_sol=0

            if note_protection==0:
                note_sol=10*note_aggressivite_sol
            else:
                note_sol=2*note_aggressivite_sol


            #AGE
            if age<10:
                note_age =1
            elif age<20:
                note_age =1
            elif age<30:
                note_age =2
            elif age<40:
                note_age =4
            elif age<60:
                note_age =7
            else :
                note_age =10

            #DIAMETRE
            if troncon[2]<=60:
                note_diametre =3
            elif troncon[2]<=80:
                note_diametre =4
            elif troncon[2]<=100:
                note_diametre =7
            elif troncon[2]<=125:
                note_diametre =8
            elif troncon[2]<=150:
                note_diametre =9
            elif troncon[2]<=200:
                note_diametre =10

        #QualitéEau
        if troncon[3]==0:
            note_qualite_eau=0
        elif troncon[3]==1:
            note_qualite_eau=5


        #TemperatureEau
        if troncon[4]<=10:
            note_temperature=1
        elif parma[4]<=25:
            note_temperature=2
        elif parma[4]<=30:
            note_temperature=3
        elif parma[4]<=35:
            note_temperature=7
        elif parma[4]<=100:
            note_temperature=10


        #OrigineCasse
        if troncon[5]=='01':
            note_casse=10
        elif troncon[5]=='02':
            note_casse=10
        elif troncon[5]=='03':
            note_casse=9
        elif troncon[5]=='04':
            note_casse=3
        elif troncon[5]=='05':
            note_casse=2
        elif troncon[5]=='06':
            note_casse=2
        elif troncon[5]=='07':
            note_casse=0
        elif troncon[5]=='08':
            note_casse=0
        elif troncon[5]=='09':
            note_casse=-10000
        elif troncon[5]=='10':
            note_casse=-10000
        elif troncon[5]=='11':
            note_casse=-10000
        elif troncon[5]=='12':
            note_casse=-10000



        #DensitéReparation
        if troncon[6] <=0:
            note_densite_reparation = 2
        elif troncon[6]<=1:
            note_densite_reparation=1
        elif troncon[6]<=3:
            note_densite_reparation=3
        elif troncon[6]<=4:
            note_densite_reparation=4
        elif troncon[6]<=8:
            note_densite_reparation=7
        elif troncon[6]<=1000:
            note_densite_reparation=10





        #ImplantationCanalisation
        if troncon[9] == '01':
            note_implantation=10
        elif troncon[9]=='02':
            note_implantation=10
        elif troncon[9]=='03':
            note_implantation=10
        elif troncon[9]=='04':
            note_implantation=10
        elif troncon[9]=='05':
            note_implantation=10
        elif troncon[9]=='06':
            note_implantation=10
        elif troncon[9]=='07':
            note_implantation=10
        elif troncon[9]=='08 ':
            note_implantation=10
        elif troncon[9]=='09':
            note_implantation=9
        elif troncon[9]=='10':
            note_implantation=8
        elif troncon[9]=='11':
            note_implantation=7
        elif troncon[9]=='12':
            note_implantation=7
        elif troncon[9]=='13':
            note_implantation=6
        elif troncon[9]=='14':
            note_implantation=6
        elif troncon[9]=='15':
            note_implantation=6
        elif troncon[9]=='16':
            note_implantation=5
        elif troncon[9]=='17':
            note_implantation=4
        elif troncon[9]=='18':
            note_implantation=2
        elif troncon[9]=='19':
            note_implantation=2
        elif troncon[9]=='00':
            note_implantation=0




        #Criticité
        if troncon[10] <=2:
            note_criticite=1
        elif troncon[10]<=4:
            note_criticite=2
        elif troncon[10]<=200:
            note_criticite=5
        elif troncon[10]<=5000:
            note_criticite=10


        #VariationP
        if troncon[11]<=5:
            note_pression=1
        elif troncon[11]<=10:
            note_pression = 2
        elif troncon[11]<=15:
            note_pression = 3
        elif troncon[11]<=20:
            note_pression = 4
        elif troncon[11]<=30:
            note_pression = 5
        elif troncon[11]<=50:
            note_pression = 7
        elif troncon[11]<=1000:
            note_pression = 10



        #AgeEau
        if troncon[12]==0:
            note_age_eau = 0
        elif troncon[12]<=12:
            note_age_eau=0
        elif troncon[12]<=24:
            note_age_eau=1
        elif troncon[12]<=36:
            note_age_eau=3
        elif troncon[12]<=48:
            note_age_eau=5
        elif troncon[12]<=72:
            note_age_eau=7
        elif troncon[12]<=10000:
            note_age_eau=10


        #TauxChlore
        if troncon[13]<=0.1:
            note_taux_chlore = 9
        elif troncon[13]<=0.2:
            note_taux_chlore = 2
        elif troncon[13]<=0.5:
            note_taux_chlore = 2
        elif troncon[13]<=1:
            note_taux_chlore = 3
        elif troncon[13]<=1000:
            note_taux_chlore = 6


        note = 6*(4*note_materiau+6*note_age)+2*(2*note_qualite_eau+2*note_temperature)+5*(4*note_casse+6*note_densite_reparation)
        note += 1*(3*note_sol+1*note_implantation+4*note_diametre)+1*2*note_criticite + 4*(6*note_pression+4*note_age_eau+3*note_taux_chlore)


        #note = list_poids_criteres[0]*(list_poids_sous_criteres[0]*note_materiau+list_poids_sous_criteres[1]*note_age)+list_poids_criteres[1]*(list_poids_sous_criteres[2]*note_qualite_eau+list_poids_sous_criteres[3]*note_temperature)+list_poids_criteres[2]*(list_poids_sous_criteres[4]*note_casse+list_poids_sous_criteres[5]*note_densite_reparation)
        #note += list_poids_criteres[3]*(list_poids_sous_criteres[6]*note_sol+list_poids_sous_criteres[7]*note_implantation+list_poids_sous_criteres[8]*note_diametre)+list_poids_criteres[4]*list_poids_sous_criteres[9]*note_criticite + list_poids_criteres[5]*(list_poids_sous_criteres[10]*note_pression+list_poids_sous_criteres[11]*note_age_eau+list_poids_sous_criteres[12]*note_taux_chlore)

        res+=[(troncon[14],note)]
    return(res)




def PCA(data, dims_rescaled_data=2, reduit):
    """
    returns: data transformed in 2 dims/columns + regenerated original data
    pass in: data as 2D NumPy array
    """
    import numpy as NP
    from scipy import linalg as LA
    m, n = data.shape
    # mean center the data
    if reduit:
        data -= data.mean(axis=0)
    # calculate the covariance matrix
    R = NP.cov(data, rowvar=False)
    # calculate eigenvectors & eigenvalues of the covariance matrix
    # use 'eigh' rather than 'eig' since R is symmetric,
    # the performance gain is substantial
    evals, evecs = LA.eigh(R)
    # sort eigenvalue in decreasing order
    idx = NP.argsort(evals)[::-1]
    evecs = evecs[:,idx]
    # sort eigenvectors according to same index
    evals = evals[idx]
    # select the first n eigenvectors (n is desired dimension
    # of rescaled data array, or dims_rescaled_data)
    evecs = evecs[:, :dims_rescaled_data]
    # carry out the transformation on the data using eigenvectors
    # and return the re-scaled data, eigenvalues, and eigenvectors
    return NP.dot(evecs.T, data.T).T, evals, evecs

def test_PCA(data, dims_rescaled_data=2):
    '''
    test by attempting to recover original data array from
    the eigenvectors of its covariance matrix & comparing that
    'recovered' array with the original data
    '''
    _ , _ , eigenvectors = PCA(data, dim_rescaled_data=2)
    data_recovered = NP.dot(eigenvectors, m).T
    data_recovered += data_recovered.mean(axis=0)
    assert NP.allclose(data, data_recovered)


def plot_pca(data):
    from matplotlib import pyplot as MPL
    clr1 =  '#2026B2'
    fig = MPL.figure()
    ax1 = fig.add_subplot(111)
    data_resc, data_orig = PCA(data)
    ax1.plot(data_resc[:, 0], data_resc[:, 1], '.', mfc=clr1, mec=clr1)
    MPL.show()


Liste modifs :



line 1996 : !!!!!!!!!! POSSIBLE : ALLER CHERCHER UN PARENT ET SE CENTRER SUR SA POSITION
        if feat.geometry() != None:
            point2 = self.dbase.xform.transform(feat.geometry().centroid().asPoint())
            self.canvas.setCenter(point2)
        else :
            pass

