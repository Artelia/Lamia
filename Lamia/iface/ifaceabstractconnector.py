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



class LamiaIFaceAbstractConnectors():

    def __init__(self):
        pass

    def showNormalMessage(self,msg):
        raise NotImplementedError

    def showErrorMessage(self,msg):
        raise NotImplementedError

    def createProgressBar(self):
        raise NotImplementedError

    def updateProgressBar(self,int):
        raise NotImplementedError

    def closeProgressBar(self,int):
        raise NotImplementedError
