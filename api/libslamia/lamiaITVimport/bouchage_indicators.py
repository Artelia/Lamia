# -*- coding: utf-8 -*-

"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """


import os, importlib, tempfile, pprint, shutil
from collections import OrderedDict
import sys, glob, inspect, logging, textwrap
import Lamia
from ..abstractlibslamia import AbstractLibsLamia

import qgis
from qgis.PyQt import QtGui, uic, QtCore, QtXml

import pandas as pd
import numpy as np

# dictionary with code of deformations as key
# first value is the factor or alpha parameter
# second value is L if you multiply by observated length or P if you multiply by P parameter
# we sum and threshold to defined a value in [1, 2, 3, 4]
all_bouchage_indicators = {
    "BOU4":
    {
        "BAG" 	:[3, "P"],	# BRANCHEMENT PENETRANT
        "BAIA"	:[0, "P"],	# ANNEAU D'ETANCHEITE
        "BAIAA"	:[3, "P"],	# JOINT D'ETANCHEITE APPARENT - ANNEAU D'ETANCHEITE AVEC BOUCLE DEPLACEE MAIS NE DEPASSANT PAS DANS LA CANALISATION
        "BAIAB"	:[3, "P"],	# JOINT D'ETANCHEITE APPARENT - PENETRANT MAIS NON ROMPU (AU-DESSUS DE LA MEDIANE)
        "BAIAC"	:[3, "P"],	# JOINT D'ETANCHEITE APPARENT - PENETRANT MAIS NON ROMPU (AU-DESSOUS DE LA MEDIANE)
        "BAIAD"	:[3, "P"],	# JOINT D'ETANCHEITE APPARENT - PENETRANT - ROMPU
        "BAIZ"	:[0, "P"],	# AUTRE ELEMENT D'ETANCHEITE
        "BBAA"	:[0, "P"],	# GROSSE RACINE ISOLEE
        "BBAB"	:[0, "P"],	# RADICELLES
        "BBAC"	:[3, "P"],	# ENSEMBLE COMPLEXE DE RACINES
        "BBBA"	:[0, "P"],	# DEPOTS ADHERENTS - CONCRETION
        "BBBB"	:[3, "P"],	# DEPOTS ADHERENTS - GRAISSE
        "BBBC"	:[0, "P"],	# DEPOTS ADHERENTS - ENCRASSEMENT
        "BBBZ"	:[3, "P"],	# DEPOTS ADHERENTS - AUTRE
        "BBCC"	:[1, "P"],	# DEPOTS - DURS OU COMPACTES
        "BBEA"	:[3, "P"],	# AUTRES OBSTABLES - BRIQUETAGE OU MACONNERIE GISANT SUR LE RADIER
        "BBEB"	:[3, "P"],	# AUTRES OBSTABLES - FRAGMENT DE CONDUITE BRISEE GISANT SUR LE RADIER
        "BBEC"	:[3, "P"],	# AUTRES OBSTACLES - OBJET SUR LE RADIER
        "BBED"	:[3, "P"],	# AUTRES OBSTABLES - OBSTACLE DEPASSANT DE LA PAROI
        "BBEE"	:[3, "P"],	# AUTRES OBSTACLES - OBSTACLE COINCE DANS L'ASSEMBLAGE
        "BBEF"	:[3, "P"],	# AUTRES OBSTABLES - OBSTACLE TRAVERSANT UN RACCORDEMENT OU UNE CONDUITE DE RACCORDEMENT
        "BBEG"	:[3, "P"],	# AUTRES OBSTACLES - CONDUITE EXTERNE OU CABLES INSERES DANS LA CANALISATION
        "BBEH"	:[3, "P"],	# AUTRES OBSTABLES - OBSTACLE INTEGRE A LA STRUCTURE
        "BBEZ"	:[3, "P"],	# AUTRES OBSTACLES - AUTRE
        "D"   	:[2, "P"],	# CONTRE PENTE
        "DACB"	:[2, "P"],	# EFFONDREMENT PARTIEL
    },
}