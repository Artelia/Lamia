# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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
from .spatialitedbaseparser import SpatialiteDBaseParser
from .postgisdbaseparser import PostGisDBaseParser


class DBaseParserFactory():

       
    def __init__(self, dbasetype ,connector=None):
        self.dbasetype = dbasetype
        self.connector = connector

    def getDbaseParser(self):
        if self.dbasetype == 'spatialite':
            return SpatialiteDBaseParser(self,messageinstance=self.connector)
        elif self.dbasetype == 'postgis':
            return PostGisDBaseParser(self,messageinstance=self.connector)
        else:
            raise ValueError('DB format not recognized') 


