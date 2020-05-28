import math


def getGraphSpec():
    """Define graph conf :
    dict {...graphsubtype:{...,'colname where is saved the value': 'colname displayed in widget',...}
          }

    :return: configuration dictionnary
    :rtype: dict
    """


    graphdict =    {'SIM': {
                            'graphnum1':'X',
                            'graphnum2':'Y',

                        },
                    'SAS': {
                            'graphnum1': 'Cadre de vie',
                            'graphnum2': 'Investissement',
                            'graphnum3': 'Biodiversité',
                            'graphnum4': 'Exploitation',
                            'graphnum5': 'Traitement',
                            'graphnum6': 'Lutte contre les ilots de chaleur',
                            'graphnum7': 'Récréatif',
                            'graphnum9': 'Protection',
                            'graphnum10': 'Facteur de charge',
                            'graphnum11': 'Autre',
                        },
    }
    

    return graphdict



def SIM(mplfigure,pdgraphdata):
    axtype = mplfigure.add_subplot(111, polar=False, label='plotgraph')
    try:
        pdgraphdata.plot(kind='line', x=0, y=1, ax=axtype)
        axtype.grid()
    except (TypeError,IndexError) as e:
        print('grapherror', e)



def SAS(mplfigure,pdgraphdata):
    print('rad')
    # https://jingwen-z.github.io/data-viz-with-matplotlib-series8-radar-chart/


    axtype = mplfigure.add_subplot(111, polar=True, label='radgraph')

    if not pdgraphdata.columns.values.tolist():
        return
    
    datas = pdgraphdata.loc[0,:].values.tolist()
    # print('*',datas, datas[:1])
    datas = datas + datas[:1]    #to close graph

    categories = pdgraphdata.columns
    # print(categories)

    # values += values[:1] # repeat the first value to close the circular graph
    angles = [n / float(len(categories)) * 2 * math.pi for n in range(len(categories))]
    angles += angles[:1]

    # fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8),
    #                     subplot_kw=dict(polar=True))

    # plt.xticks(angles[:-1], categories, color='grey', size=12)
    axtype.set_xticks(angles[:-1])
    axtype.set_xticklabels(categories)

    # setxticksvalues
    maxdatasvalue = max(datas)
    if maxdatasvalue == 0:
        return
    log10value = int(math.log10(maxdatasvalue))
    step = 10**log10value
    maxstep = 10**log10value * (int(maxdatasvalue/step) + 1)
    # print(step, maxstep)
    valuerange = range(step, maxstep, step)
    valuerangestr = [str(elem) for elem in valuerange]
    # print(valuerange,valuerangestr )

    axtype.set_yticks(valuerange)
    axtype.set_yticklabels(valuerangestr)

    # plt.yticks(np.arange(1, 6), ['1', '2', '3', '4', '5'],
    #         color='grey', size=12)
    # plt.yticks(valuerange, valuerangestr,
    #         color='grey', size=12)
    # plt.ylim(0, 5)
    axtype.set_rlabel_position(30)
    
    axtype.plot(angles, datas, linewidth=1, linestyle='solid')
    axtype.fill(angles, datas, 'skyblue', alpha=0.4)
