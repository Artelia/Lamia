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
import os, importlib
import numpy as np
import pandas as pd
import csv

import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt

font = {"family": "normal", "weight": "bold", "size": 8}
matplotlib.rc("font", **font)
# matplotlib.rc('xtick', labelsize=20)
# matplotlib.rc('ytick', labelsize=20)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)


from .lamiagraph import GraphMaker


class GraphMakerCsv(GraphMaker):
    def __init__(self, dbaseparser):
        self.dbase = dbaseparser

        self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111)

        if self.dbase.base3version:
            strtoexec = (
                f"lamiaconf.{self.dbase.worktype.lower()}.lamiagraph.lamiagraphfunc"
            )
        else:
            strtoexec = f"..{self.dbase.worktype.lower()}.lamiagraphfunc"
        self.graphmodule = importlib.import_module(strtoexec, package=self.__module__)
        self.graphspec = self.graphmodule.getGraphSpec()

    def getGraphData(self, graphpk):

        filegraphique = self.dbase.getValuesFromPk("graph_qgis", "file", graphpk)

        if filegraphique is None or filegraphique == "":
            return None
        filegraphique = self.dbase.completePathOfFile(filegraphique)
        datas = []
        if os.path.isfile(filegraphique):
            with open(filegraphique, newline="") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=";", quotechar="|")
                for row in csvreader:
                    datas.append([])
                    for elem in row:
                        if self.isfloat(elem):
                            datas[-1].append(float(elem))
                        else:
                            datas[-1].append(elem)
        else:
            datas = None

        return datas

    def saveGraphData(self, featurepk, datas):

        csvpath = self.dbase.getValuesFromPk("graph_qgis", "file", featurepk)
        csvpath = self.dbase.completePathOfFile(csvpath)
        with open(csvpath, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=";", quoting=csv.QUOTE_MINIMAL)
            for data in datas:
                print(data)
                csvwriter.writerow(data)

