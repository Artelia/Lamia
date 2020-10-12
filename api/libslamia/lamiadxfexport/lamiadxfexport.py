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
from lamiaapi.libs.dxfwrite import DXFEngine as dxf


class ExporDxfCore:

    POSTPROTOOLNAME = "exportdxftools"

    def __init__(self, dbaseparser, messageinstance=None):
        # super(ExportShapefileTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
        self.dbase = dbaseparser
        self.messageinstance = messageinstance

    def exportTopography(self, pktopotoexport=None, filename=None):

        exportdir = os.path.join(self.dbase.dbaseressourcesdirectory, "exportdxf")
        if not os.path.isdir(exportdir):
            os.mkdir(exportdir)

        exportfilename = os.path.join(exportdir, filename)

        sql = f"SELECT topographydatatype, x, y , zmngf FROM topographydata WHERE lpk_topography = {pktopotoexport}"
        res = self.dbase.query(sql)

        drawing = dxf.drawing(exportfilename)

        for topographydatatype, x, y, zmngf in res:
            if (
                self.dbase.utils.isAttributeNull(x)
                or self.dbase.utils.isAttributeNull(y)
                or self.dbase.utils.isAttributeNull(zmngf)
            ):
                continue
            if self.dbase.utils.isAttributeNull(topographydatatype):
                topographydatatype = "0"
            drawing.add_layer(topographydatatype)
            point = dxf.point((x, y, zmngf), layer=topographydatatype)
            drawing.add(point)
            # drawing.add(dxf.line((0, 0), (1, 0), color=7, layer="LINES"))

        drawing.save()

        return exportfilename
