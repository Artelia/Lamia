import os
import sys
import qgis
import qgis.gui
import qgis.utils
import shutil

from Lamia.Lamia.main.DBaseParser import DBaseParser


parser = DBaseParser(None)
parser.createDBDictionary('Base_digue')

print('*********** Basedonnees **********************')
print(parser.dbasetables['Basedonnees'])


print('*********** Zonegeo **********************')
print(parser.dbasetables['Zonegeo'])


print('*********** Infralineaire **********************')
print(parser.dbasetables['Infralineaire'])

print('*********** Desordre **********************')
print(parser.dbasetables['Desordre'])
