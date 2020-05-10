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

 


"""
Class
"""

import os.path
import qgis
from .iface.qgiswidget.lamia_dockwidget import InspectiondigueDockWidget


from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QDockWidget, QToolBar


# Initialize Qt resources from file resources.py
from . import resources_rc


"""
Created on 29 July 2012
@author: Lisa Simpson
"""


class Lamia:
    """
    QGIS Plugin Implementation

    aussi
    """

    

    
    def __init__(self, iface):
        """
        blblblb
        :param iface <String> : An interface instance that will be passed to this class
        :return Bool Return somethong
        """

        
        ## Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Lamia_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Lamia')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'Lamia')
        self.toolbar.setObjectName(u'Lamia')

        #print "** INITIALIZING InspectionDigue"

        # self.dockwidget = None
        self.lamiadocks={}

        self.toolbarsvisibility={}


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """
        Get the translation for a string using Qt translation API.

        Args:
           message (str): We all know what foo does.
        
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Lamia', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """
        Add a toolbar icon to the toolbar.

        
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action


    def initGui(self):
        """
        Create the menu entries and toolbar icons inside the QGIS GUI
        """

        icon_path = ':/plugins/Lamia/icons/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Lamia'),
            callback=self.run,
            parent=self.iface.mainWindow())

    #--------------------------------------------------------------------------

    def onClosePlugin(self, dockindex):
        """
        Cleanup necessary items here when plugin dockwidget is closed
        """
        self.lamiadocks[dockindex]['active'] = False
        self.lamiadocks[dockindex]['widget'].closingPlugin.disconnect(self.onClosePlugin)


    def unload(self):
        """
        Removes the plugin menu item and icon from QGIS GUI.
        """

        #print "** UNLOAD InspectionDigue"

        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Lamia'),
                action)
            self.iface.removeToolBarIcon(action)
        self.lamiadocks = {}
        # remove the toolbar
        del self.toolbar

    #--------------------------------------------------------------------------

    def run(self):
        """
        Run method that loads and starts the plugin
        """

        dockindex = len(self.lamiadocks)
        self.lamiadocks[dockindex]={}
        self.lamiadocks[dockindex]['active'] = True
        self.lamiadocks[dockindex]['widget'] = InspectiondigueDockWidget(qgis.utils.iface.mapCanvas(),
                                                                         dockorder=dockindex)
        # self.lamiadocks.append(InspectiondigueDockWidget(qgis.utils.iface.mapCanvas(),dockorder = len(self.lamiadocks)))
        wdg = self.lamiadocks[dockindex]['widget']
        self.iface.addDockWidget(Qt.RightDockWidgetArea, wdg)
        wdg.show()
        wdg.closingPlugin.connect(self.onClosePlugin)


