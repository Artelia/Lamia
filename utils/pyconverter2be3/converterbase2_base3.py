import os, sys, shutil

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)

import Lamia
from Lamia.libs.odsreader.ODSReader import ODSReader
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory


def readingConf(conffilename, confdict={}):
    """
    condict :
    {...namesourcetable:[namedestdate,
                        {...{fieldsource:fielddest}...}]
    """
    print("ok", conffilename)
    filepath = os.path.join(os.path.dirname(__file__), conffilename)
    odsdoc = ODSReader(filepath, clonespannedcolumns=False)

    finalsql = []

    for sheetname in odsdoc.SHEETS.keys():
        if not len(sheetname.split("_")) == 3:
            continue

        sheetdatas = odsdoc.SHEETS[sheetname]
        if not sheetname.split("_")[1] in confdict.keys():
            confdict[sheetname.split("_")[1]] = [sheetname.split("_")[2], {}]

        for row, rowcontent in enumerate(sheetdatas):
            if len(sheetdatas[row]) < 3:
                continue
            if (
                sheetdatas[row][0]
                and sheetdatas[row][0] != ""
                and sheetdatas[row][0][0] != "#"
                and sheetdatas[row][3]
                and sheetdatas[row][3] != ""
            ):

                confdict[sheetname.split("_")[1]][1][sheetdatas[row][0]] = sheetdatas[
                    row
                ][3]

    return confdict


def generateSql(sqlitedbasesource, confdict):
    sqllist = []
    for sourcetable, (destable, fieldconf) in confdict.items():
        realtablecolumns = sqlitedbasesource.getColumns(sourcetable)

        for fieldname in list(fieldconf.keys()):
            if not fieldname.strip() in realtablecolumns:
                print(fieldname, " not found in ", sourcetable)
                del fieldconf[fieldname]

        sql = f"INSERT INTO {destable}({', '.join(list(fieldconf.values()))}) \
                SELECT {', '.join(list(fieldconf.keys()))} FROM dbasesource.{sourcetable}"

        sqllist.append(sql)
    return sqllist


def attachDB(dbasedest, dbasesourcefile):
    # ATTACH DATABASE file_name AS database_name;
    sql = f"ATTACH DATABASE '{dbasesourcefile}' AS dbasesource"
    print(sql)
    dbasedest.query(sql)


def concertScript(dbasedest, sqllist):
    for sql in sqllist:
        print(sql)
        dbasedest.query(sql)


def doPostScript(sqlitedbasedest):
    worktype = sqlitedbasedest.worktype

    if worktype == "base3_urbandrainage":
        sql = "UPDATE descriptionsystem SET networktype = \
                (SELECT sourceinfra.typeReseau FROM dbasesource.Infralineaire as sourceinfra\
                 WHERE sourceinfra.lpk_descriptionsystem = descriptionsystem.pk_descriptionsystem) \
                WHERE (SELECT sourceinfra.typeReseau FROM dbasesource.Infralineaire as sourceinfra\
                 WHERE sourceinfra.lpk_descriptionsystem = descriptionsystem.pk_descriptionsystem) IS NOT NULL"
        print(sql)
        sqlitedbasedest.query(sql)
        sql = "UPDATE descriptionsystem SET networktype = \
                (SELECT sourcenoeud.typeReseau FROM dbasesource.Noeud as sourcenoeud\
                 WHERE sourcenoeud.lpk_descriptionsystem = descriptionsystem.pk_descriptionsystem)\
                WHERE (SELECT sourcenoeud.typeReseau FROM dbasesource.Noeud as sourcenoeud\
                 WHERE sourcenoeud.lpk_descriptionsystem = descriptionsystem.pk_descriptionsystem) IS NOT NULL"
        print(sql)
        sqlitedbasedest.query(sql)

        sql = "UPDATE edge SET pipetype = (CASE WHEN pipesubtype IN ('CIR', 'AQU', 'OVO') THEN 'COL' \
                                                WHEN pipesubtype IN ('FOS') THEN 'FOS' \
                                                WHEN pipesubtype IN ('FOB') THEN 'CAN' \
                                                ELSE NULL \
                                            END)"
        print(sql)
        sqlitedbasedest.query(sql)

    elif worktype == "base3_waterdistribution":
        sql = "UPDATE descriptionsystem SET networktype = \
                (SELECT sourceinfra.type_eau FROM dbasesource.Infralineaire as sourceinfra\
                 WHERE sourceinfra.lpk_descriptionsystem = descriptionsystem.pk_descriptionsystem) \
                WHERE (SELECT sourceinfra.type_eau FROM dbasesource.Infralineaire as sourceinfra\
                 WHERE sourceinfra.lpk_descriptionsystem = descriptionsystem.pk_descriptionsystem) IS NOT NULL"
        print(sql)
        sqlitedbasedest.query(sql)

        sql = "UPDATE descriptionsystem SET networktype = \
                (SELECT sourcenoeud.nature_reseau FROM dbasesource.Noeud as sourcenoeud\
                 WHERE sourcenoeud.lpk_descriptionsystem = descriptionsystem.pk_descriptionsystem)\
                WHERE (SELECT sourcenoeud.nature_reseau FROM dbasesource.Noeud as sourcenoeud\
                 WHERE sourcenoeud.lpk_descriptionsystem = descriptionsystem.pk_descriptionsystem) IS NOT NULL"
        print(sql)
        sqlitedbasedest.query(sql)


def DoPostResources(sqlitedbasedest, sourcefile, destfile):
    srcdir = os.path.join(os.path.dirname(sourcefile), "DBspatialite", "Photos")
    if os.path.isdir(srcdir):
        destdir = os.path.join(os.path.dirname(destfile), "DBspatialite", "media")
        if os.path.exists(destdir):
            shutil.rmtree(destdir)
        destination = shutil.copytree(srcdir, destdir)

    srcdir = os.path.join(os.path.dirname(sourcefile), "DBspatialite", "Photo")
    if os.path.isdir(srcdir):
        destdir = os.path.join(os.path.dirname(destfile), "DBspatialite", "media")
        if os.path.exists(destdir):
            shutil.rmtree(destdir)
        destination = shutil.copytree(srcdir, destdir)

    srcdir = os.path.join(os.path.dirname(sourcefile), "DBspatialite", "Rapport")
    if os.path.isdir(srcdir):
        destdir = os.path.join(os.path.dirname(destfile), "DBspatialite", "report")
        if os.path.exists(destdir):
            shutil.rmtree(destdir)
        destination = shutil.copytree(srcdir, destdir)

    srcdir = os.path.join(os.path.dirname(sourcefile), "DBspatialite", "Rasters")
    if os.path.isdir(srcdir):
        destdir = os.path.join(os.path.dirname(destfile), "DBspatialite", "rasters")
        if os.path.exists(destdir):
            shutil.rmtree(destdir)
        destination = shutil.copytree(srcdir, destdir)

    sql = "SELECT pk_resource, file FROM resource"
    result = sqlitedbasedest.query(sql)
    for pk_resource, filename in result:  # Photos Rapport
        newfilename = None
        if not filename:
            continue
        if ".\\Photos\\" in filename:
            newfilename = filename.replace(".\\Photos\\", ".\\media\\")
        elif ".\\Photo\\" in filename:
            newfilename = filename.replace(".\\Photo\\", ".\\media\\")
        elif ".\\Rapport\\" in filename:
            newfilename = filename.replace(".\\Rapport\\", ".\\report\\")
        if newfilename:
            sqlreplace = f"UPDATE resource SET file = '{newfilename}' WHERE pk_resource = {pk_resource}"
            sqlitedbasedest.query(sqlreplace)


def main(argv):

    sourcereldirname = None
    odstoread = []

    print(argv)

    worktypeconv = {
        "Base2_eaupotable": "base3_waterdistribution",
        "Base2_assainissement": "base3_urbandrainage",
        "Base2_digue": "base3_levee",
    }

    if argv:
        # workingdir = os.path.join(argv[0])
        sourcefile = os.path.join(argv[0])
        # sourcereldirname = argv[1]
        destdir = argv[1]
        odstoread = argv[2].split(" ")
        if not isinstance(odstoread, list):
            odstoread = [odstoread]
    else:
        print("no args !!")
        return

    # sourcefile = os.path.join(workingdir, "a_source", sourcereldirname)
    sourcefile = os.path.join(sourcefile)
    # destdir = os.path.join(os.path.dirname(__file__),'b_result')
    # destfile = os.path.join(workingdir, "b_result", sourcereldirname)
    sourcefilename = os.path.basename(sourcefile)
    destfile = os.path.join(destdir, sourcefilename)

    if not os.path.isdir(os.path.dirname(destfile)):
        os.makedirs(os.path.dirname(destfile))

    # sys.exit()
    print("Source file is :", os.path.abspath(sourcefile))
    print("Dest   file is :", os.path.abspath(destfile))

    print("Loading source...")
    sqlitedbasesource = DBaseParserFactory("spatialite").getDbaseParser()
    sqlitedbasesource.loadDBase(dbtype="Spatialite", slfile=sourcefile)
    print("Source loaded...")
    print("Creating dest...")
    sqlitedbasedest = DBaseParserFactory("spatialite").getDbaseParser()
    sqlitedbasedest.createDBase(
        crs=sqlitedbasesource.crsnumber,
        worktype=worktypeconv[sqlitedbasesource.worktype],
        dbaseressourcesdirectory=None,
        variante=sqlitedbasesource.variante,
        slfile=destfile,
    )
    print("Dest created...")

    print("Readingconf and create sql")
    confdict = {}
    for odsfilename in odstoread:
        confdict = readingConf(odsfilename, confdict)
        # confdict = readingConf('Base_assainissement_base2_0_6_to_base3_0_1.ods', confdict)

    # print(confdict)

    sqllist = generateSql(sqlitedbasesource, confdict)
    print("Conf read")

    print("Converting ...")

    attachDB(sqlitedbasedest, sourcefile)
    concertScript(sqlitedbasedest, sqllist)
    doPostScript(sqlitedbasedest)
    DoPostResources(sqlitedbasedest, sourcefile, destfile)

    print("Converted !!!")

    # DETACH DATABASE 'Alias-Name';
    # warning edge networktype -> descriptionsystem  formecanalisation


if __name__ == "__main__":
    main(sys.argv[1:])
