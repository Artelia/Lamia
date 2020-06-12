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


import os
import datetime

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (
    QWidget,
    QGroupBox,
    QGridLayout,
    QLabel,
    QTableWidgetItem,
)

from ..base3.lamiabase_geoarea_tool import BaseGeoareaTool


class BaseUrbandrainagegeoareaTool(BaseGeoareaTool):

    def __init__(self, **kwargs):
        super(BaseUrbandrainagegeoareaTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        super().initMainToolWidget()

        """
        self.stats = [[self.tr('Sewage - gravity pipe lenght'), 
                        ''' SELECT SUM(ST_Length(edge_now.geom)) 
                        FROM edge_now, geoarea 
                        WHERE ST_WITHIN(edge_now.geom, geoarea.geom)
                            AND edge_now.sewertype = 'USE' AND edge_now.flowtype = 1 
                            AND lateral = 0 '''],

                        [self.tr('Sewage - pressure pipe lenght'), 
                        ''' SELECT SUM(ST_Length(edge_now.geom)) 
                        FROM edge_now, geoarea 
                        WHERE ST_WITHIN(edge_now.geom, geoarea.geom)
                            AND edge_now.sewertype = 'USE' AND edge_now.flowtype = 2 
                            AND lateral = 0  '''],

                        [self.tr('Sewage - manholes '), 
                        ''' SELECT COUNT(*) 
                            FROM node_now, geoarea 
                            WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                                AND node_now.nodetype = '60' AND node_now.sewertype = 'USE' '''],

                        [self.tr('Sewage - laterals ')
                        , ''' SELECT COUNT(*) 
                        FROM node_now, geoarea 
                        WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                        AND node_now.nodetype = '61'  AND node_now.sewertype = 'USE'  '''],

                        [self.tr('Sewage - Pumping stations '), 
                        ''' SELECT COUNT(*) 
                            FROM node_now, geoarea 
                            WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                            AND node_now.nodetype = '10'  AND node_now.sewertype = 'USE'   '''],


                        [self.tr('Sewage - Stormwater overflows ')
                        , ''' SELECT COUNT(*) 
                            FROM node_now, geoarea 
                            WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                            AND node_now.nodetype = '40'  AND node_now.sewertype = 'USE'  '''],

                        [self.tr('Sewage - Water treatment plant '), 
                        ''' SELECT COUNT(*) 
                        FROM node_now, geoarea 
                        WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                            AND node_now.nodetype = '20' '''],

                        [self.tr('Storm water - pipe lenght'), 
                        ''' SELECT SUM(ST_Length(edge_now.geom)) 
                            FROM edge_now, geoarea 
                            WHERE ST_WITHIN(edge_now.geom, geoarea.geom)
                                AND edge_now.sewertype = 'PLU' AND lateral = 0  
                                AND edge_now.pipeshape IN ('CIR', 'AQU', 'OVO') '''],

                        [self.tr('Storm water - open channel lenght'), 
                        ''' SELECT SUM(ST_Length(edge_now.geom)) 
                            FROM edge_now, geoarea 
                            WHERE ST_WITHIN(edge_now.geom, geoarea.geom)
                            AND edge_now.sewertype = 'PLU' AND lateral = 0  
                            AND edge_now.pipeshape IN ('FOS', 'FOB') '''],


                        [self.tr('Storm water - manholes '), 
                        ''' SELECT COUNT(*) 
                        FROM node_now, geoarea 
                        WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                        AND node_now.nodetype = '60'  AND node_now.sewertype = 'PLU'  '''],

                        [self.tr('Storm water - laterals '), 
                        ''' SELECT COUNT(*) 
                            FROM node_now, geoarea 
                            WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                            AND node_now.nodetype = '61'  AND node_now.sewertype = 'PLU'  '''],

                        [self.tr('Storm water - inlet grates '), 
                        ''' SELECT COUNT(*) 
                        FROM node_now, geoarea 
                        WHERE ST_WITHIN(ST_MakeValid(node_now.geom), ST_MakeValid(geoarea.geom))
                            AND node_now.nodetype IN ('70','71','72')  AND node_now.sewertype = 'PLU'  '''],


                        [self.tr('Combined - gravity pipe lenght'), 
                        ''' SELECT SUM(ST_Length(edge_now.geom)) 
                            FROM edge_now, geoarea 
                            WHERE ST_WITHIN(edge_now.geom, geoarea.geom)
                            AND edge_now.sewertype = 'UNI' AND edge_now.flowtype = 1 
                            AND lateral = 0  '''],

                        [self.tr('Combined - pressure pipe lenght'), 
                        ''' SELECT SUM(ST_Length(edge_now.geom)) 
                            FROM edge_now, geoarea 
                            WHERE ST_WITHIN(edge_now.geom, geoarea.geom)
                                AND edge_now.sewertype = 'UNI' AND edge_now.flowtype = 2 
                                AND lateral = 0  '''],

                        [self.tr('Combined - manholes '), 
                        ''' SELECT COUNT(*) 
                            FROM node_now, geoarea 
                            WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                                AND node_now.nodetype = '60'  AND node_now.sewertype = 'UNI'  '''],

                        [self.tr('Combined - mixed manholes'), 
                        ''' SELECT COUNT(*) /2 
                            FROM node_now, geoarea 
                            WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                            AND node_now.nodetype = '62'   '''],


                        [self.tr('Combined - laterals '), 
                        ''' SELECT COUNT(*) 
                            FROM node_now, geoarea 
                            WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                                AND node_now.nodetype = '61'  AND node_now.sewertype = 'UNI'  '''],

                        [self.tr('Combined - Pumping stations '), 
                        ''' SELECT COUNT(*) 
                            FROM node_now, geoarea 
                            WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                                AND node_now.nodetype = '10'  AND node_now.sewertype = 'UNI'   '''],

                        [self.tr('Combined - Stormwater overflows'), 
                        ''' SELECT COUNT(*) 
                            FROM node_now, geoarea 
                            WHERE ST_WITHIN(node_now.geom, geoarea.geom)
                            AND node_now.nodetype = '40'  AND node_now.sewertype = 'UNI'  '''],

                        ]

        self.loadStats()
        """
