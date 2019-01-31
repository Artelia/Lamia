# -*- coding: utf-8 -*-

"""
Class
"""


import qgis
from .dialog.InspectionDigue_dockwidget import InspectiondigueDockWidget




from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon
try:
    from qgis.PyQt.QtGui import QAction, QDockWidget
except:
    from qgis.PyQt.QtWidgets import QAction, QDockWidget



# Initialize Qt resources from file resources.py
from . import resources_rc



# Import the code for the DockWidget
#from .GPS2Point_dockwidget import GPS2PointDockWidget



import os.path


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
            'Lamia{}.qm'.format(locale))

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

        self.pluginIsActive = False
        self.dockwidget = None
        self.lamiadocks=[]


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

    def onClosePlugin(self):
        """
        Cleanup necessary items here when plugin dockwidget is closed
        """

        #print "** CLOSING InspectionDigue"
        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)

        # remove this statement if dockwidget is to remain
        # for reuse if plugin is reopened
        # Commented next statement since it causes QGIS crashe
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False


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
        # remove the toolbar
        del self.toolbar

    #--------------------------------------------------------------------------

    def run(self):
        """
        Run method that loads and starts the plugin
        """
        self.lamiadocks.append(InspectiondigueDockWidget(qgis.utils.iface.mapCanvas()))
        #self.dockwidget = InspectiondigueDockWidget(qgis.utils.iface.mapCanvas())

        #self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.lamiadocks[-1])
        self.lamiadocks[-1].show()


        if False:
            if True and not self.pluginIsActive:
                self.pluginIsActive = True

                #print "** STARTING GPS2Point"

                # dockwidget may not exist if:
                #    first run of plugin
                #    removed on close (see self.onClosePlugin method)
                if False:
                    if self.dockwidget == None:
                        # Create the dockwidget (after translation) and keep reference
                        #self.dockwidget = GPS2PointDockWidget()
                        self.dockwidget = InspectiondigueDockWidget(qgis.utils.iface.mapCanvas())
                        if True:
                            path = os.path.normpath('C://00_Affaires//travail_fiches//test//test2.sqlite')
                            self.dockwidget.windowwidget.dbase.loadDbase(path)

                self.dockwidget = InspectiondigueDockWidget(qgis.utils.iface.mapCanvas())


                # connect to provide cleanup on closing of dockwidget
                #self.dockwidget.closingPlugin.connect(self.onClosePlugin)
                self.dockwidget.closingPlugin.connect(self.onClosePlugin)

                # show the dockwidget
                # TODO: fix to allow choice of dock location
                self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)
                self.dockwidget.show()

