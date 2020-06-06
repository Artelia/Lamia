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


import os, sys, datetime
import xlrd


class SubObservationParser():

    def __init__(self, filetoparse):
        self.filetoparse = filetoparse


    def createDictionnary(self):
        """
        dict : { ..., 1.1 : {'name' : 'Tranchée,
                            'datas' : {..., index : {'description' :  description
                                                    , 'type' : type
                                                    }
                                      }
                            }
                }

        :return:
        """


        pathxls = os.path.join(os.path.dirname(__file__), 'subsheet', self.filetoparse + '.xlsx')
        xlsbook = xlrd.open_workbook(pathxls)

        sousfichesdict = {}
        firstcolcode = None

        sheet = xlsbook.sheets()[0]
        for row in range(sheet.nrows):
            firstcol =  sheet.cell_value(row, 0)

            if firstcol == '':
                if sheet.cell_value(row, 1) == '' and sheet.cell_value(row, 2) == '':
                    break

            else:
                firstcolname = firstcol
                firstcolcode = firstcolname.split(' ')[0]
                sousfichesdict[firstcolcode] = {}
                sousfichesdict[firstcolcode]['name'] = ' '.join(firstcolname.split(' ')[1:])
                sousfichesdict[firstcolcode]['datas'] = {}

            sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)] = {}
            #sousfichesdict[firstcolcode]['datas'].append([sheet.cell_value(row, 1) , sheet.cell_value(row, 2), sheet.cell_value(row, 3)])

            if sheet.cell_value(row, 2) != '':
                sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)]['description'] = sheet.cell_value(row, 2)
            else:
                sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)]['description'] = None

            if sheet.cell_value(row, 3) != '':
                sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)]['type'] = sheet.cell_value(row,3)
            else:
                sousfichesdict[firstcolcode]['datas'][sheet.cell_value(row, 1)]['type'] = None

        return sousfichesdict
