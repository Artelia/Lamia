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
        logging.getLogger( "Lamia_connector" ).info('normalMessage : %s', text)

    def showErrorMessage(self,text):
        logging.getLogger( "Lamia_connector" ).info('ErrorMessage : %s', text)

    def createProgressBar(self, inittext='', maxvalue=99):
        self.progressbarinittext = inittext
        logging.getLogger( "Lamia_connector" ).info('Creating progress bar : %s', inittext)

    def updateProgressBar(self,val):
        logging.getLogger( "Lamia_connector" ).info('%s : %d', self.progressbarinittext, val)

    def closeProgressBar(self):
        logging.getLogger( "Lamia_connector" ).info('%s : %s', self.progressbarinittext, 'closing')

    def inputMessage(self,listtext, title='Lamia input', withinput=True, parent = None):
        res=[]
        print('*** ' + title + (' ***'))
        if withinput:
            for text in listtext:
                restemp = input(text + '? : ') 
                if restemp:
                    res.append(restemp)
        else:
            for txt in listtext:
                print(txt)
            restemp = input('Yes (y) or No (n) ?') 
            if restemp == 'y':
                res = True
            else:
                res = False
        
        return res