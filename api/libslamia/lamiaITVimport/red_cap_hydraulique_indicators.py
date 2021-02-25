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
all_red_cap_hyfraulique_indicators = {
    "HYD3":
    {
        "BCC#"  :[3, "P"], # courbure du collecteur
        "BCCA"  :[3, "P"],
        "BCCB"  :[3, "P"],
        "BACA"  :[0, "P"], # rupture/effondrement
        "BACC"  :[3, "P"],
        "BADA"  :[0, "P"], # briquetage ou elements de maconnerie defectueux
        "BADC"  :[0, "P"],
        "BADD"  :[3, "P"],
        "BAF"   :[1, "L"], # degradation de surface
        "BAFBAF":[1, "L"],
        "BAG"   :[2, "P"], # branchement penetrant
        "BAGBAG":[2, "P"],
        "BAI#"  :[0, "P"], # joint d'etancheite apparent
        "BAIB"  :[0, "P"],
        "BAIC"  :[0, "P"],
        "BAIE"  :[0, "P"],
        "BAJB"  :[0, "P"], # deplacement d'assemblage
        "BAJC"  :[0, "P"],
        "BAK"   :[[[0.1, 0], [np.inf, 1]], "P"], # defaut de revetement si Q<10% 0, sinon 1.
        "BBAB"  :[0, "P"], # racines
        "BBAA"  :[[[0.5, 2], [np.inf, 3]], "P"],
        "BBAC"  :[[[0.5, 2], [np.inf, 3]], "P"],
        "BBB"   :[[[0.1, 0], [0.5, 1], [np.inf, 3]], "P"], # depots adherents
        "BBCC"  :[[[0.1, 0], [0.5, 1], [np.inf, 3]], "P"], # depots
        "BBD"   :[[[0.1, 0], [0.5, 1], [np.inf, 3]], "P"], # entree de terre
        "BBE"   :[[[0.5, 2], [np.inf, 3]], "P"], # autres obstacles
        "BDC"   :[3, "P"], # progression de la camera impossible
        "BDCBDC":[3, "P"], # progression de la camera impossible
    },
}
