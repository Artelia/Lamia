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
import os, sys, glob
from pathlib import Path
import Lamia
from Lamia.qgisiface.iface.ifaceabstractconnector import LamiaIFaceAbstractConnectors


class AbstractLibsLamia:
    """Base class for postpro modules with conf files
    manage conf datas :
        * POSTPROTOOLNAME : the name of the tools, also the directory within the conf datas are
        * fileext : the files extentions to read, eg ".txt"
        * projectcharacter : spacial caracter to recogize if file is general plugin fle or project spicific file
    and methods to retrieve the conf data files
    """

    POSTPROTOOLNAME = "reporttools"
    fileext = ".txt"
    projectcharacter = "_"

    def __init__(self, dbaseparser, messageinstance=None):
        """Constructor
        :param dbaseparser: the dbaseparser
        :param messageinstance: an output instance, defaults to None
        """
        self.dbase = dbaseparser
        if messageinstance is None:
            self.messageinstance = LamiaIFaceAbstractConnectors()
        else:
            self.messageinstance = messageinstance

        self.confdatadirplugin = os.path.join(
            os.path.dirname(Lamia.__file__),
            "config",
            self.dbase.worktype.lower(),
            self.POSTPROTOOLNAME,
        )

        self.confdatadirproject = os.path.join(
            self.dbase.dbaseressourcesdirectory, "config", self.POSTPROTOOLNAME
        )
        if not os.path.isdir(self.confdatadirproject):
            # os.mkdir(self.confdatadirproject)
            Path(self.confdatadirproject).mkdir(parents=True, exist_ok=True)

        self.names_files = {}
        self.getNamePathFiles()

    def getNamePathFiles(self):
        """Create a dict with {key: conf filename, value: conf file complete path}
        """
        self.names_files = {}
        for workdir in [self.confdatadirplugin, self.confdatadirproject]:
            for filename in glob.glob(os.path.join(workdir, "*" + self.fileext)):
                basename = os.path.basename(filename).split(".")[0]
                if basename != "README":
                    if workdir == self.confdatadirproject:
                        basename = self.projectcharacter + basename
                self.names_files[basename] = os.path.normpath(
                    os.path.join(workdir, filename)
                )

    def getConfFilePath(self, confname):
        """Get the complete path of a conf name

        :param confname: the conffile, either just a name or complete path
        :return: the complete path of file
        """
        if os.path.isfile(confname):
            return confname
        else:
            for namekey in self.names_files.keys():
                if confname == namekey.lstrip("_") or confname == namekey:
                    return self.names_files[namekey]
        return None
