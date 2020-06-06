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



from ..base3.lamiabase_facility_tool import BaseFacilityTool

from .lamiabase_ud_node_tool import BaseUrbandrainageNodeTool
from .lamiabase_ud_edge_tool import BaseUrbandrainageEdgeTool
from .lamiabase_ud_surface_tool import BaseUrbandrainageSurfaceTool

class BaseUrbandrainageFacilityTool(BaseFacilityTool):

    def __init__(self, **kwargs):
        super(BaseUrbandrainageFacilityTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        super().initMainToolWidget()

        # self.dbasechildwdgfield=[]
        # self.instancekwargs['parentwidget'] = self

        self.propertieswdgNode = BaseUrbandrainageNodeTool(**self.instancekwargsforchildwdg)
        self.dbasechildwdgfield.insert(0,self.propertieswdgNode)

        self.propertieswdgEdge = BaseUrbandrainageEdgeTool(**self.instancekwargsforchildwdg)
        self.dbasechildwdgfield.insert(1,self.propertieswdgEdge)

        self.propertieswdgSurface = BaseUrbandrainageSurfaceTool(**self.instancekwargsforchildwdg)
        self.dbasechildwdgfield.insert(2,self.propertieswdgSurface)





