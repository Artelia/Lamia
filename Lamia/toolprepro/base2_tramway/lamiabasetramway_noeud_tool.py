# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QPushButton)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_noeud_tool import BaseNoeudTool

import os
import qgis
from collections import OrderedDict
import datetime
# from ..base.lamiabase_photo_tool import BasePhotoTool
from .lamiabasetramway_photo_tool import BaseTramwayPhotoTool as BasePhotoTool
from .lamiabasetramway_croquis_tool import BaseTramwayCroquisTool as BaseCroquisTool
#from ..base.lamiabase_croquis_tool import BaseCroquisTool
#from .lamiabaseassainissement_desordre_tool import BaseAssainissementDesordreTool
#from .lamiabaseassainissement_equipement_tool import BaseAssainissementEquipementTool
import sys



class BaseTramwayNoeudTool(BaseNoeudTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseTramwayNoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
