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
import os, logging

from qgis.PyQt.QtWidgets import QWidget, QVBoxLayout
from qgis.PyQt import uic, QtCore

from .subwidget_abstract import AbstractSubWidget


class GpsValuesWidget(AbstractSubWidget):

    UIPATH = os.path.join(os.path.dirname(__file__), "subwidget_gpsvalues_ui.ui")

    def __init__(self, parentwdg=None, parentframe=None):
        super(GpsValuesWidget, self).__init__(
            parentwdg=parentwdg, parentframe=parentframe
        )

        self.gpsutil = self.parentwdg.mainifacewidget.gpsutil
        self.gpsutil.GPSConnected.connect(self.displayGPS)

        self.gpswidget = {
            "x": {"widget": self.label_X, "gga": "Xcrs"},
            "y": {"widget": self.label_Y, "gga": "Ycrs"},
            "zmngf": {"widget": self.label_Z, "gga": "zmNGF"},
            "dx": {"widget": self.label_dX, "gst": "xprecision"},
            "dy": {"widget": self.label_dY, "gst": "yprecision"},
            "dz": {"widget": self.label_dZ, "gst": "zprecision"},
            "zgps": {"widget": self.label_zgps, "gga": "elevation"},
            "zwgs84": {"widget": self.label_zwgs84, "gga": "deltageoid"},
            "raf09": {"widget": self.label_raf09, "gga": "RAF09"},
            "hauteurperche": {"widget": self.label_hautperche, "gga": "hauteurperche"},
        }

        # if self.gpsutil is not None and (self.gpswidget is not None or (self.dbasetable is not None and 'geom' in self.dbasetable.keys())):
        #     self.gpsutil.GPSConnected.connect(self.displayGPS)

    def displayGPS(self, active):
        """
        Called on GPs connection
        Print GPS things in widgets defined by self.gpswidget

        :param active: True ig a NMEA sentence is received in less than 5 s, else False

        """
        if active:
            if self.gpswidget is not None:
                for key in self.gpswidget.keys():
                    if self.gpswidget[key]["widget"] is not None:
                        self.gpswidget[key]["widget"].setEnabled(True)
                self.gpsutil.ggasentence.connect(self.displayGGA)
                self.gpsutil.gstsentence.connect(self.displayGST)
            # self.pushButton_rajoutPointGPS.setEnabled(True)
        else:
            # self.pushButton_rajoutPointGPS.setEnabled(False)
            if self.gpswidget is not None:
                try:
                    self.gpsutil.ggasentence.disconnect(self.displayGGA)
                except:
                    pass
                try:
                    self.gpsutil.gstsentence.disconnect(self.displayGST)
                except:
                    pass
                for key in self.gpswidget.keys():
                    if self.gpswidget[key]["widget"] is not None:
                        self.gpswidget[key]["widget"].setText("/")
                        self.gpswidget[key]["widget"].setEnabled(False)

    def displayGGA(self, dictgga):
        """
        Called by displayGPS

        :param dictgga: the dict where widgets to display gga are defined
        """

        for key in self.gpswidget.keys():
            if (
                "gga" in self.gpswidget[key].keys()
                and self.gpswidget[key]["widget"] is not None
            ):
                if dictgga[self.gpswidget[key]["gga"]] is not None:
                    try:
                        self.gpswidget[key]["widget"].setText(
                            str(round(dictgga[self.gpswidget[key]["gga"]], 2))
                        )
                    except KeyError:
                        pass
                else:
                    self.gpswidget[key]["widget"].setText("/")

    def displayGST(self, dictgst):
        """
        Called by displayGPS

        :param dictgst: the dict where widgets to display gst are defined
        """
        for key in self.gpswidget.keys():
            if (
                "gst" in self.gpswidget[key].keys()
                and self.gpswidget[key]["widget"] is not None
            ):
                if dictgst[self.gpswidget[key]["gst"]] is not None:
                    self.gpswidget[key]["widget"].setText(
                        str(round(dictgst[self.gpswidget[key]["gst"]], 2))
                    )
                else:
                    self.gpswidget[key]["widget"].setText("/")

