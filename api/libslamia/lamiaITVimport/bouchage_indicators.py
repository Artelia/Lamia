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
        #"BAG"   :[], # branchement penetrant RIEN COMPRIS
        "BAIZ"  :[0, "P"], # joint d'etancheite apparant
        "BAI#"  :[0, "P"],
        #"BAI#"  :[0, "P"], # pas clair la suite des BAI
        "BBAB"  :[0, "P"], # racines
        "BBAA"  :[3, "P"],
        "BBAC"  :[3, "P"],
        #"BBBC"  :[2, "P"], # depots adherents pas clair
        "BBC"   :[2, "P"], # BBC complexe et pas clair
        "BBE"   :[3, "P"], # autres obstacles
        "BBEBBE":[3, "P"], # autres obstacles
    },
}
