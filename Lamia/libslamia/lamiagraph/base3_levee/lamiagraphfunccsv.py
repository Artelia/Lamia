
def getGraphSpec():
    """Define graph conf :
    dict {...graphsubtype:{...,'colname in csv file': 'list of constraints',...}
          }

    :return: configuration dictionnary
    :rtype: dict
    """

    graphdict =    {'SIM': {
                            'X': [],
                            'Y': [],
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
