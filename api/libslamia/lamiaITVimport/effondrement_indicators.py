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
    "EFF4":
    {
        "BABA"	:[1, "L"],	# MICRO-FISSURE
        "BABB"	:[1, "L"],	# FISSURE FERMEE
        "BABBA"	:[1, "L"],	# FISSURE FERMEE LONGITUDINALE
        "BABBB"	:[1, "L"],	# FISSURE FERMEE CIRCONFERENTIELLE
        "BABBC"	:[1, "L"],	# FISSURE - FERMEE - COMPLEXE 
        "BABBD"	:[2, "L"],	# FISSURE FERMEE HELICOIDALE
        "BABC"	:[2, "L"],	# FISSURE OUVERTE
        "BABCA"	:[2, "L"],	# FISSURE - OUVERTE - LONGITUDINALE
        "BABCB"	:[2, "L"],	# FISSURE OUVERTE CIRCONFERENTIELLE
        "BABCC"	:[2, "L"],	# FISSURE - OUVERTE - COMPLEXE
        "BABCD"	:[2, "L"],	# FISSURE OUVERTE HELICOIDALE
        "BACA"	:[2, "P"],	# RUPTURE / EFFONDREMENT - RUPTURE
    },
}
