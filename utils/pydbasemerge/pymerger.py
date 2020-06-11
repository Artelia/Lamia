import os, sys
lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), '..','..')
sys.path.append(lamiapath)

from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
# from Lamia.iface.qgsconnector.ifaceqgisconnector import QgisConnector

def merger():

    #Ass part
    if True:
        sourcefile = os.path.join(os.path.dirname(__file__),'c_merge_ass','GPMB Bacalan.sqlite')
        sqlitedbasesource = DBaseParserFactory('spatialite').getDbaseParser()
        sqlitedbasesource.loadDBase(dbtype='Spatialite', slfile=sourcefile)


        mergedir = os.path.join(os.path.dirname(__file__),'b_result')
        mergefiles = [
                    os.path.join(mergedir, r'BASSENS\EU\Bassens EU EP.sqlite') ,
                    # os.path.join(mergedir, r'BASSENS\EU\Bassens EU EP.sqlite')  ,
                    os.path.join(mergedir, r'BLAYE\GPMB Blaye.sqlite') ,
                    os.path.join(mergedir, r'Pauillac\GPMB Pauillac.sqlite') ,
                    os.path.join(mergedir, r'POLE NAVAL\EU\Pole naval.sqlite') ,
                    os.path.join(mergedir, r'Verdon port bloc\GPMB Port Bloc.sqlite') ,
                    os.path.join(mergedir, r'Verdon Terminal conteneur\GPMB Verdon Terminal conteneur.sqlite') ,
                    ]

    #AEP part
    if False:
        sourcefile = os.path.join(os.path.dirname(__file__),'c_merge_aep','Bassens-AEP.sqlite')
        sqlitedbasesource = DBaseParserFactory('spatialite').getDbaseParser()
        sqlitedbasesource.loadDBase(dbtype='Spatialite', slfile=sourcefile)


        mergedir = os.path.join(os.path.dirname(__file__),'b_result')
        mergefiles = [
                    os.path.join(mergedir, r'POLE NAVAL\AEP\Pole Naval_AEP.sqlite') ,
                    ]

    for mergefile in mergefiles:
        print('**', mergefile)
        sqlitedbasesource.dbaseofflinemanager.addDBase(slfile=mergefile)

    

def getSpecForNewFile(tomergefiles):
    tempparser = DBaseParserFactory('spatialite').getDbaseParser()
    tempparser.loadDBase(dbtype='Spatialite', slfile=tomergefiles[0])
    spec={}
    spec['crs'] = tempparser.crsnumber
    spec['worktype']   = tempparser.worktype
    spec['variante']  = tempparser.variante
    print('specs : ' , spec)
    return spec

def createNewDB(destfile, spec):
    sqlitedbasedest = DBaseParserFactory('spatialite').getDbaseParser()
    sqlitedbasedest.createDBase(crs=spec['crs'], 
                                worktype=spec['worktype'], 
                                dbaseressourcesdirectory=None, 
                                variante=spec['variante'],
                                slfile=destfile)

    sqlitedbasedest.loadDBase(dbtype='Spatialite', slfile=destfile)
    return sqlitedbasedest

def mergefiles(destparser, fromfiles):

    for mergefile in fromfiles:
        print('Merging : ', mergefile)
        destparser.dbaseofflinemanager.addDBase(slfile=mergefile)

    


def main(argv):
    destfile = os.path.join(argv[0], 'mergeddbase.sqlite')
    fromfiles = [os.path.join(filepath) for filepath in argv[1].split(';') if filepath]

    spec = getSpecForNewFile(fromfiles)

    print('Creating new DB ...')
    destparser = createNewDB(destfile, spec)
    print('New DB created')

    print('Merging files ...')
    mergefiles(destparser, fromfiles)
    print('merged !!!')



if __name__ == "__main__":
    main(sys.argv[1:])


