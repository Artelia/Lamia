import os, sys
lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), '..','..')
sys.path.append(lamiapath)

from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.iface.qgsconnector.ifaceqgisconnector import QgisConnector


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

print('merged !!!')


