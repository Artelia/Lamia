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

import winreg, sys
import datetime
import platform, os
import pandas as pd

import zipfile

# sys.path.append(os.path.join(os.path.dirname(__file__),'..','..','libs'))
import Lamia
from Lamia.libs.odsreader.ODSReader import ODSReader


class TabCatalog:

    _instances = set()

    def __init__(self, worktype):
        self.worktype = worktype
        self.pddatas = self.loadPandasDatas()

        self._instances.add(self)

    def getInstance(worktype):
        inst = None
        for obj in __class__._instances:
            # print (obj.worktype) # prints 'a' and 'c'
            if obj.worktype == worktype:
                inst = obj
        if inst is None:
            inst = TabCatalog(worktype)

        return inst

    def loadPandasDatas(self):

        # f = []
        pddatas = {}
        # mypath = os.path.join(os.path.dirname(__file__), self.worktype)

        mypath = os.path.join(
            os.path.dirname(Lamia.__file__),
            "worktypeconf",
            self.worktype,
            "lamiatabcatalog",
        )

        for (dirpath, dirnames, filenames) in os.walk(mypath):
            # print (filenames)
            for filename in filenames:
                basefilename, file_extension = os.path.splitext(filename)
                # print(basefilename,file_extension )
                if file_extension == ".ods":
                    filepath = os.path.join(dirpath, filename)
                    xls = pd.ExcelFile(filepath, engine="odf")
                    odsdocsheets = xls.sheet_names
                    pddatas[basefilename] = {}
                    for sheetname in odsdocsheets:
                        # print(sheetname)
                        pddatas[basefilename][sheetname] = pd.read_excel(
                            xls, sheet_name=sheetname, engine="odf"
                        )

        # print(pddatas["LISTE_faune_2019"]["oiseaux"])

        return pddatas


# print('1')
# tabp = TabParser.getinstance('faunaflora')
# print('2')
# tabp2 = TabParser.getinstance('faunaflora')
# print('3')
# # tabp.loadPandasDatas()
