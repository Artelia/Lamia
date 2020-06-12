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

import winreg
import datetime
import platform


def updateWinReg(**kwargs):

    datemodif = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if platform.system() == "Windows":
        try:
            key = winreg.CreateKey(
                winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Artelia\\Lamia"
            )
        except PermissionError:
            return

        winreg.SetValueEx(key, "laststart", 0, winreg.REG_SZ, datemodif)

        try:
            opencount, regtype = winreg.QueryValueEx(key, "lamiaopencount")
        except FileNotFoundError:
            opencount = None
        if not opencount:
            opencount = 0
        winreg.SetValueEx(key, "lamiaopencount", 0, winreg.REG_DWORD, opencount + 1)

        for k, v in kwargs.items():
            winreg.SetValueEx(key, k, 0, winreg.REG_SZ, str(v))
