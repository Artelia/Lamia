#!/usr/bin/env python
#coding:utf-8
# Purpose: write DXF R12 files
# Based on the ideas of Stani Michiels(Stani) sdxf.py and
# Remigiusz Fiedler(migius) dxflibrary133.py
# Created: 14.03.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

from .const import *
from .base import *
from .engine import DXFEngine


version = (1, 2, 1)
VERSION = "%d.%d.%d"  % version

CYEAR = "2010-2017"
AUTHOR_NAME = "Manfred Moitzi"
AUTHOR_EMAIL = "mozman@gmx.at"
LICENSE = "MIT License"

__author__ = "mozman <mozman@gmx.at>"
__doc__ = """A Python library to create DXF R12 drawings.

Copyright %s
Version %s
License %s

IMPLEMENTED R12 WRITING:
- POINT
- LINE
- CIRCLE
- ARC
- TEXT
- SOLID
- TRACE
- FACE3D
- POLYLINE (POLYMESH, POLYFACE)
- BLOCK
- INSERT
- ATTDEF
- ATTRIB

NOT IMPLEMENTED:
- DIMENSION (use LinearDimension, AngularDimension, ArcDimension or
             RadialDimension)
""" % (AUTHOR_NAME, VERSION, LICENSE,)
