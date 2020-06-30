import math


def getGraphSpec():
    """Define graph conf :
    dict {...graphsubtype:{...,'colname where is saved the value': 'colname displayed in widget',...}
          }

    :return: configuration dictionnary
    :rtype: dict
    """


    graphdict = {'SIM': {
                            'graphnum1':'X',
                            'graphnum2':'Y',

                        },
                'PTR': {'graphnum1':'X',
                        'graphnum2':'Y',
                        'graphchar1': 'Position',
                        'graphchar2':'Nature',
                        'graphchar3':'Materiau',
                        'graphchar4':'Cote',
                    },      
                }      
    

    return graphdict

    """
    self.graphspec = {'SIM': {'x': [],
                                'y':[],
                            },
                        'RAD': {'var': [],
                                'value':[],
                            },
                        'PTR': {'x': [],
                                'y':[],
                                'Position': ['/',
                                            'Crete',
                                            'Talus digue',
                                            'Sommet risberme',
                                            'Talus risberme',
                                            'Talus risberme - pied',
                                            'Pied de digue',
                                            'Franc-bord',
                                            'Berge',
                                            'Pied de berge',
                                            'Hors digue',
                                            'Plusieurs parties',
                                            'Indefini'],
                                'Nature': ['/',
                                        'Abscence de revetement',
                                        'Dispositif fusible',
                                        'Enrochement',
                                        'Fondation meuble',
                                        'Fondation rocheuse',
                                        'Contre fosse(cote terre)',
                                        'Gabion',
                                        'Indefini',
                                        'Mur de soutenement',
                                        'Ouvrage parafouille',
                                        'Palplanche',
                                        'Paroi etanche',
                                        'Perre',
                                        'Pieux',
                                        'Remblais',
                                        'Ouvrage de revanche',
                                        'Revetement',
                                        'Seuil, deversoir',
                                        'Zone de dissipation',
                                        'Zone urbanisee'],
                                'Materiau': ['/',
                                            'Acier',
                                            'Bentonite-ciment',
                                            'Beton',
                                            'Bois',
                                            'Concasse 0/80',
                                            'Dechet carriere 0/400',
                                            'Enrobe',
                                            'Fraisat recycle',
                                            'Galets 0/100',
                                            'Geotextile',
                                            'Geomembrane',
                                            'Graviers 0/33',
                                            'Grillage',
                                            'Indefini',
                                            'Limons',
                                            'Limons et sables',
                                            'Moellons',
                                            'Lit naturel du fosse',
                                            'Paves',
                                            'Plaques beton joitives',
                                            'Panneaux JK',
                                            'Pierres maconnees',
                                            'Pierres seches',
                                            'Remblais',
                                            'Roches appareilles',
                                            'Roches betonnees',
                                            'Roches deversee',
                                            'Sables',
                                            'Schistes 0/100',
                                            'Silts',
                                            'Terre vegetale',
                                            'Tuyau drain',
                                            'Tout venant brut',
                                            'Vegetalise enherbe',
                                            'Vegetalise arbustif',
                                            'Vegetalise boise'],
                                'Cote': ['/',
                                        'Eau',
                                        'Terre',
                                        'Crête'],
                            },      
                        }       
    """



def SIM(mplfigure,pdgraphdata):
    axtype = mplfigure.add_subplot(111, polar=False, label='plotgraph')
    try:
        pdgraphdata.plot(kind='line', x=0, y=1, ax=axtype)
        axtype.grid()
    except (TypeError,IndexError) as e:
        print('grapherror', e)


def PTR(mplfigure,pdgraphdata):

        # self.figuretype = plt.figure()
        # self.axtype = self.figuretype.add_subplot(111)
        axtype = mplfigure.add_subplot(111, polar=False, label='ptrgraph')

        Xgraph = [0.0]
        Zgraph = [0.0]
        typepartie = []

        # print(pdgraphdata)

        for i in range(len(pdgraphdata)):
            try:
                Xgraph.append(Xgraph[-1] + float(pdgraphdata['X'][i]))
                Zgraph.append(Zgraph[-1] + float(pdgraphdata['Y'][i]))
                typepartie.append(pdgraphdata['Nature'][i] + ' - ' + pdgraphdata['Materiau'][i])
            except (ValueError, KeyError) as e:
                return

        label = []
        for i in range(len(Xgraph)-1):
            typep = typepartie[i]
            graphcolor = 'black'
            graphlinestyle = '-'
            graphlinewidth = 3.0
            if 'Vegetalise enherbe' in typep:
                graphcolor = 'lightgreen'
            elif 'Vegetalise arbustif' in typep:
                graphcolor = 'seagreen'
            elif 'Vegetalise boise' in typep:
                graphcolor = 'darkgreen'
            elif 'Gabion' in typep:
                graphcolor = 'gray'
                graphlinestyle = '-'
                graphlinewidth = 5.
            elif 'Gravier 0/33' in typep:
                graphcolor = 'darkgray'
                graphlinestyle = '--'
            elif 'Enrobe' in typep:
                graphcolor = 'black'
                graphlinewidth = 4.
            elif 'Beton' in typep:
                graphcolor = 'gray'
            elif 'Pierre maconnees' in typep:
                graphcolor = 'gray'
                graphlinestyle = '--'
            elif 'Roches appareillees' in typep:
                graphcolor = 'gray'
                graphlinestyle = '-.'
            elif 'Abscence de revetement' in typep:
                graphcolor = 'saddlebrown'

            if typep not in label:
                label.append(typep)
            else:
                typep = None

            axtype.plot([Xgraph[i],Xgraph[i+1]], [Zgraph[i], Zgraph[i+1]], label=typep, color=graphcolor,
                                linewidth=graphlinewidth, linestyle=graphlinestyle)

        legend = axtype.legend(bbox_to_anchor=(0., 1.), loc="lower left", bbox_transform=mplfigure.transFigure, prop={'size': 8})
        axtype.annotate('TERRE', xy=(0.05, 1.05), xycoords='axes fraction',horizontalalignment='left')
        axtype.annotate('EAU', xy=(0.95, 1.05), xycoords='axes fraction',horizontalalignment='right')

        #plt.ylabel('Z (m)', fontsize=8)
        axtype.set_ylabel('Z (m)', fontsize=8)
