import zipfile
import os, sys

MAINDIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


CONF = {
    "Lamia/qgisiface/qgispluginroot": "Lamia",
    "Lamia/api": None,
    "Lamia/qgisiface/config": None,
    "Lamia/qgisiface/DBASE": None,
    "Lamia/qgisiface/i18n": None,
    "Lamia/qgisiface/icons": None,
    "Lamia/qgisiface/iface": None,
    "Lamia/config": None,
    "Lamia/doc/schemas": None,
}


def readVersion():
    filevers = os.path.join(
        MAINDIR, "Lamia", "qgisiface", "qgispluginroot", "metadata.txt"
    )
    version = ""
    with open(filevers, "r") as reader:
        # Read and print the entire file line by line
        line = reader.readline()
        while line.split("=")[0] != "version":  # The EOF char is an empty string
            # print(line, end="")
            line = reader.readline()
        print(line)
        version = line.split("=")[-1]
    return version


def get_all_file_paths(conf, zipf):

    # initializing empty file paths list
    file_paths = []
    base, dest = conf, CONF[conf]

    # crawling through directory and subdirectories
    walpkpath = os.path.normpath(os.path.join(MAINDIR, base))
    for root, directories, files in os.walk(walpkpath):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            if dest:
                relpath = filepath.replace(root, dest)
            else:
                relpath = os.path.relpath(filepath, MAINDIR)
            zipf.write(filepath, relpath)

    

def main():
    print("zipping...")
    version = readVersion()
    version = version.replace(".", "_")

    FILENAME = os.path.join(
        MAINDIR, "Lamia", "utils", "Lamia_" + version.strip() + ".zip"
    )

    zipf = zipfile.ZipFile(FILENAME, "w", zipfile.ZIP_DEFLATED)
    for conf in CONF:
        file_paths = get_all_file_paths(conf, zipf)
    #otherfiles
    initpath = os.path.join(MAINDIR,"Lamia","qgisiface","__init__.py")
    zipf.write(initpath, os.path.relpath(initpath, MAINDIR))
    
    zipf.close()
    print("zipping done")


if __name__ == "__main__":
    main()

