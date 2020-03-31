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



class LamiaIFaceAbstractWidget():

    def __init__(self):
        self.preprotools = {}
        # list containing the menu tools classes
        self.postprotools = {}
        # the pick maptool
        # self.pointEmitter = None
        # The DBaseParser
        self.dbase = None
        self.connector = None
        self.canvas = None
        #list of recent dbase loaded
        self.recentsdbase = []

    # ***********************************************************
    # **************** File menu actions ***********************
    # ***********************************************************

    def newDBase(self):
        raise NotImplementedError

    def loadDBase(self):
        raise NotImplementedError

    def pullDBase(self):    #for offline mode
        raise NotImplementedError

    def pushDBase(self):    #for offline mode
        raise NotImplementedError

    def addDBase(self):
        raise NotImplementedError


