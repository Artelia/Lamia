import os, sys

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..", "..")
sys.path.append(lamiapath)

from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

# from Lamia.iface.qgsconnector.ifaceqgisconnector import QgisConnector


def merger():

    # Ass part
    if True:
        sourcefile = os.path.join(
            os.path.dirname(__file__), "c_merge_ass", "GPMB Bacalan.sqlite"
        )
        sqlitedbasesource = DBaseParserFactory("spatialite").getDbaseParser()
        sqlitedbasesource.loadDBase(dbtype="Spatialite", slfile=sourcefile)

        mergedir = os.path.join(os.path.dirname(__file__), "b_result")
        mergefiles = [
            os.path.join(mergedir, r"BASSENS\EU\Bassens EU EP.sqlite"),
            # os.path.join(mergedir, r'BASSENS\EU\Bassens EU EP.sqlite')  ,
            os.path.join(mergedir, r"BLAYE\GPMB Blaye.sqlite"),
            os.path.join(mergedir, r"Pauillac\GPMB Pauillac.sqlite"),
            os.path.join(mergedir, r"POLE NAVAL\EU\Pole naval.sqlite"),
            os.path.join(mergedir, r"Verdon port bloc\GPMB Port Bloc.sqlite"),
            os.path.join(
                mergedir,
                r"Verdon Terminal conteneur\GPMB Verdon Terminal conteneur.sqlite",
            ),
        ]

    # AEP part
    if False:
        sourcefile = os.path.join(
            os.path.dirname(__file__), "c_merge_aep", "Bassens-AEP.sqlite"
        )
        sqlitedbasesource = DBaseParserFactory("spatialite").getDbaseParser()
        sqlitedbasesource.loadDBase(dbtype="Spatialite", slfile=sourcefile)

        mergedir = os.path.join(os.path.dirname(__file__), "b_result")
        mergefiles = [
            os.path.join(mergedir, r"POLE NAVAL\AEP\Pole Naval_AEP.sqlite"),
        ]

    for mergefile in mergefiles:
        print("**", mergefile)
        sqlitedbasesource.dbaseofflinemanager.addDBase(slfile=mergefile)


def getSpecForNewFile(tomergefiles):
    tempparser = DBaseParserFactory("spatialite").getDbaseParser()
    tempparser.loadDBase(dbtype="Spatialite", slfile=tomergefiles[0])
    spec = {}
    spec["crs"] = tempparser.crsnumber
    spec["worktype"] = tempparser.worktype
    spec["variante"] = tempparser.variante
    print("specs : ", spec)
    return spec


def createNewDB(destfile, spec):
    sqlitedbasedest = DBaseParserFactory("spatialite").getDbaseParser()

    sqlitedbasedest.raiseexceptions = False  # False True
    sqlitedbasedest.printsql = False  # False True
    sqlitedbasedest.printorm = True  # False True

    sqlitedbasedest.createDBase(
        crs=spec["crs"],
        worktype=spec["worktype"],
        dbaseressourcesdirectory=None,
        variante=spec["variante"],
        slfile=destfile,
    )

    sqlitedbasedest.loadDBase(dbtype="Spatialite", slfile=destfile)
    return sqlitedbasedest


def mergefiles(destparser, fromfiles):

    for mergefile in fromfiles:
        print("Merging : ", mergefile)
        # destparser.dbaseofflinemanager.addDBase(slfile=mergefile)

        toimportparser = DBaseParserFactory("spatialite").getDbaseParser()
        toimportparser.loadDBase(dbtype="Spatialite", slfile=mergefile)

        destparser.dbaseofflinemanager.importDBase(
            toimportparser,
            typeimport="append",
            createnewversion=True,
            ressourcesimport="None",
            dobackup=False,
    )


def main(argv):

    if argv:
        destfile = os.path.join(argv[0], "mergeddbase.sqlite")
        fromfiles = [
            os.path.join(filepath) for filepath in argv[1].split(";") if filepath
        ]
    else:
        destfile = r"M:\FR\BOR\VT\FLUVIAL\4353036_85_SMVSA_Definition_SE\05_ETUDES\Lamia\Traitement\BdD_traitement\PVR\mergeddbase.sqlite"

        fromfiles = [
            r"C:\01_WORKINGDIR\herve\herve1_v3\terrain.sqlite",
            r"C:\01_WORKINGDIR\herve\herve2_v3\terrain epis_Troncon.sqlite",
            r"C:\01_WORKINGDIR\herve\herve3_v3\terrain epis_Troncon2.sqlite",
        ]
        fromfiles = [
            r"C:\01_WORKINGDIR\reims\AST\BDD_REIMS_J1_AST.sqlite",
            r"C:\01_WORKINGDIR\reims\BER\BDD LAMIA BER\BDD_REIMS_BER_20200915.sqlite",
            r"C:\01_WORKINGDIR\reims\CLE\BDD LAMIA CLE\BDD LAMIA\TERRAIN_CLE_semaine_2_mardi.sqlite",
        ]

        fromfiles = [
            # r"M:\FR\BOR\VT\FLUVIAL\4353036_85_SMVSA_Definition_SE\05_ETUDES\Lamia\Traitement\BdD_traitement\Bordeaux\Terrain_Marais_Poitevin.sqlite",
            r"M:\FR\BOR\VT\FLUVIAL\4353036_85_SMVSA_Definition_SE\05_ETUDES\Lamia\Traitement\Nantes\VTA_SMVSA_SGU\Nantes.sqlite"
        ]

    spec = getSpecForNewFile(fromfiles)

    print("Creating new DB ...")
    destparser = createNewDB(destfile, spec)
    print("New DB created")

    print("Merging files ...")
    mergefiles(destparser, fromfiles)
    print("merged !!!")


if __name__ == "__main__":
    main(sys.argv[1:])

