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
import Lamia
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


class GraphMaker:
    def __init__(self, dbaseparser):
        self.dbase = dbaseparser

        self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111)

        if self.dbase.base3version:
            strtoexec = f"Lamia.worktypeconf.{self.dbase.worktype.lower()}.lamiagraph.lamiagraphfunc"
        else:
            strtoexec = f"..{self.dbase.worktype.lower()}.lamiagraphfunc"
        self.graphmodule = importlib.import_module(strtoexec, package=self.__module__)
        self.graphspec = self.graphmodule.getGraphSpec()

    def getGraphData(self, graphpk):

        graphtype = self.dbase.getValuesFromPk("graph", "graphsubtype", graphpk)
        graphiquedatafields = list(self.graphspec[graphtype].keys())
        fieldstorequest = ", ".join(graphiquedatafields)

        sql = (
            "SELECT "
            + fieldstorequest
            + " FROM graphdata WHERE lpk_graph = "
            + str(graphpk)
        )
        sql += " ORDER BY pk_graphdata"
        query = self.dbase.query(sql)
        if not query:
            return None

        result = [list(row) for row in query]
        lenrowresult = len(graphiquedatafields)
        resultfinal = []

        if len(result) > 0:
            for elem in result:
                resultfinal.append([None] * lenrowresult)
                for i, field in enumerate(graphiquedatafields):
                    dbasefield = self.dbase.dbasetables["graphdata"]["fields"][field]
                    if "Cst" in dbasefield.keys():
                        if elem[i] is None:
                            valuetoset = ""
                        else:
                            valuetoset = elem[i]
                        resultfinal[-1][i] = self.dbase.getConstraintTextFromRawValue(
                            "graphdata", field, valuetoset
                        )
                    elif (
                        dbasefield["PGtype"] == "INT"
                        or dbasefield["PGtype"] == "NUMERIC"
                    ):
                        if elem[i] is not None:
                            resultfinal[-1][i] = round(elem[i], 2)
                        else:
                            resultfinal[-1][i] = None

        return resultfinal

    def saveGraphData(self, featurepk, datas):

        graphtype = self.dbase.getValuesFromPk("graph", "graphsubtype", featurepk)

        sql = "DELETE FROM graphdata WHERE lpk_graph = " + str(featurepk)
        self.dbase.query(sql)

        fieldlist = list(self.graphspec[graphtype].keys())

        for data in datas:
            sql = f"INSERT INTO graphdata ( {', '.join(fieldlist)}, lpk_graph) \
                    VALUES( {', '.join(data)}, {featurepk} )   "
            self.dbase.query(sql)

    def showGraph(self, graphpk):
        self.figuretype.clf(keep_observers=True)

        if graphpk is None:
            self.figuretype.canvas.draw()
            return

        graphtype = self.dbase.getValuesFromPk("graph", "graphsubtype", graphpk)

        graphdata = self.getGraphData(graphpk)
        if graphdata is None:
            self.figuretype.canvas.draw()
            return

        pdgraphdata = pd.DataFrame(graphdata)
        headersname = list(self.graphspec[graphtype].values())
        if len(pdgraphdata.columns) == len(headersname):
            pdgraphdata.columns = headersname

        if hasattr(self.graphmodule, graphtype):
            func = getattr(self.graphmodule, graphtype)
            func(self.figuretype, pdgraphdata)

        self.figuretype.canvas.draw()

    def exportgraph(self, featurepk, exportfile, width, height):
        self.showGraph(featurepk)
        self.figuretype.set_size_inches(width / 25.4, height / 25.4)
        self.figuretype.savefig(exportfile, bbox_inches="tight", dpi=150)

    def isfloat(self, txt):
        try:
            float(txt)
            return True
        except:
            return False
