# -*- coding: utf-8 -*-
"""
MainModule core
"""

from .InspectionDigue import *


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load InspectionDigue class from file InspectionDigue.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .InspectionDigue import InspectionDigue
    return InspectionDigue(iface)
