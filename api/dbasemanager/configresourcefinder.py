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

import os
import Lamia


class ConfigResourcefinder:
    def __init__(self, dbaseparser):
        self.dbaseparser = dbaseparser

    def findResource(self, resourcecategory, resourcename):
        """find a resource in different config dirs :
            * first is project config dir
            * second is lamia worktype config dir
            * last is lamia base config dir

        :param resourcecategory: Directory of particulary module
        :type resourcecategory: string
        :param resourcename: filename of particulary module
        :type resourcename: string
        :return: complete filepath
        :rtype: string
        """
        dirs = [
            os.path.join(
                self.dbaseparser.completePathOfFile(
                    self.dbaseparser.dbaseressourcesdirectory
                ),
                "config",
            ),
            os.path.join(
                os.path.dirname(Lamia.config.__file__), self.dbaseparser.worktype
            ),
            os.path.join(
                os.path.dirname(Lamia.config.__file__),
                self.dbaseparser.worktype.split("_")[0],
            ),
        ]

        for dirpath in dirs:
            tempath = os.path.join(dirpath, resourcecategory, resourcename)
            print("tempath", tempath)
            if os.path.isfile(tempath):
                return tempath

        return None

