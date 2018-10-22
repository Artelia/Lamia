import zipfile
import os


def unzip(file, targetDir):
    """ Creates directory structure and extracts the zip contents to it.
        file - the zip file to extract
        targetDir - target location
    """

    # create destination directory if doesn't exist
    if not targetDir.endswith(':') and not os.path.exists(targetDir):
        os.makedirs(targetDir)

    zf = zipfile.ZipFile(file)
    for name in zf.namelist():
        # create directory if doesn't exist
        localDir = os.path.split(name)[0]
        fullDir = os.path.normpath(os.path.join(targetDir, localDir))
        if not os.path.exists(fullDir):
            os.makedirs(fullDir)
        # extract file
        if not name.endswith('/'):
            fullPath = os.path.normpath(os.path.join(targetDir, name))
            print(fullPath)
            outfile = open(fullPath, 'wb')
            outfile.write(zf.read(name))
            outfile.flush()
            outfile.close()


filezip = "//arteliagroup.com//Echange_Global//FR//ECH//INF_licences//Qgis//Lamia_0_30.zip"
dest = "C://Users//patrice.verchere//.qgis2//python//plugins"

unzip(filezip, dest)

print('end')