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

import logging, sys

class LamiaIFaceAbstractConnectors():

    def __init__(self):
        pass
        # logging.basicConfig( stream=sys.stderr )
        # logging.getLogger("Lamia_connector").setLevel( logging.INFO )

    def showNormalMessage(self, text):
        pass

    def showErrorMessage(self,text):
        pass

    def createProgressBar(self, inittext='', maxvalue=99):
        self.progressbarinittext = inittext
        pass

    def updateProgressBar(self,val):
        pass

    def closeProgressBar(self):
        pass

    def inputMessage(self,listtext, title='Lamia input', withinput=True, parent = None):
        pass