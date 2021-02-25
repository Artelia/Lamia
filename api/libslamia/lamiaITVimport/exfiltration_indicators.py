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
all_exfiltration_indicators = {
    "EXF4":
    {
        "BAA"   :[1, "P"], # deformation
        "BAABAA":[1, "P"], # j'ai un doute sur le code, BAA ou BAABAA ?
        "BABB"  :[0, "L"], # fissure
        "BABC"  :[2, "L"],
        "BACA"  :[2, "P"], # rupture/effondrement
        "BACB"  :[3, "P"],
        "BACC"  :[3, "P"],
        "BADA"  :[1, "P"], # briquetage ou elements de maconnerie defectueux
        "BADB"  :[2, "P"],
        "BADC"  :[2, "P"],
        "BADD"  :[3, "P"],
        "BAE"   :[1, "P"], # mortier manquant
        "BAEBAE":[1, "P"], # doute
        "BAFA"  :[0, "L"], # degradation de surface
        "BAFC"  :[0, "L"],
        "BAFD"  :[0, "L"],
        "BAFE"  :[0, "L"],
        "BAFF"  :[0, "L"],
        "BAFG"  :[0, "L"],
        "BAFH"  :[0, "L"],
        "BAFB"  :[2, "L"],
        "BAFI"  :[3, "L"],
        "BAFZ"  :[3, "L"],
        "BAHB"  :[2, "P"], # raccordement defectueux
        "BAHC"  :[2, "P"],
        "BAHD"  :[2, "P"],
        "BAIZ"  :[0, "P"], # joint d'etancheite apparent
        "BAIA"  :[2, "P"],
        "BAI#"  :[2, "P"], # pas compris le #
        "BAJ"   :[2, "P"], # deplacement d'assemblage
        "BAJBAJ":[2, "P"], # doute
        "BAN"   :[0, "L"], # conduite poreuse
        "BANBAN":[0, "L"],
        "BAO"   :[3, "P"], # sol visible par le defaut
        "BAOBAO":[3, "P"], # doute
        "BAP"   :[3, "P"], # vide visible par le defaut
        "BAPBAP":[3, "P"], # doute
        "BBA"   :[2, "P"], # racines
        "BBABBA":[2, "P"], # doute
        "BBBA"  :[2, "P"], # depots adherents
        "BBFA"  :[2, "P"], # infiltration
        "BBFB"  :[2, "P"],
        "BBFC"  :[3, "P"],
        "BBFD"  :[3, "P"],
    },
}
