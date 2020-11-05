#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# Copyright (C) 2010 Yaacov Zamir (2010) <kzamir@walla.co.il>
# Author: Yaacov Zamir (2010) <kzamir@walla.co.il>

from xml.sax.saxutils import escape

class SodsCell:
	def __init__(self):
		''' init and set default values for cell elements '''
		
		# TextProperties
		self.font_size = "12pt"
		self.font_family = "Arial"
		self.color = "#000000"
		
		# ParagraphProperties
		self.text_align = "start"
		
		# TableColumnProperties
		self.column_width = "100pt"
		
		# TableCellProperties
		self.background_color = "default"
		self.border_top = "none"
		self.border_bottom = "none"
		self.border_left = "none"
		self.border_right = "none"
		
		# TableCell
		self.text = ""
		self.value_type = "string"
		self.value = None
		self.formula = None
		self.date_value = None
		self.format = ""
		
		# Map
		self.condition = None
		self.condition_state = False
		self.condition_color = "#000000"
		self.condition_background_color = "#ffffff"
	
	def set(self, font_size = None, font_family = None, color = None, 
			background_color = None, border_top = None,
			border_bottom = None, border_left = None, border_right = None,
			text = None, value_type = None,
			value = None, formula = None,
			date_value = None,
			condition = None, condition_state = None,
			condition_color = None, condition_background_color = None,
			text_align = None, format = None,
			column_width = None):
		''' set values of one cell object '''
		
		if font_size:
			self.font_size = font_size
		if font_family:
			self.font_family = font_family
		if color:
			self.color = color
			if not condition:
				self.condition_color = color
				
		if background_color:
			self.background_color = background_color
			if not condition:
				self.condition_background_color = background_color
		if border_top:
			self.border_top = border_top
		if border_bottom:
			self.border_bottom = border_bottom
		if border_left:
			self.border_left = border_left
		if border_right:
			self.border_right = border_right
		
		if text_align:
			self.text_align = text_align
		if column_width:
			self.column_width = column_width
			
		if text:
			self.text = text
		if value_type:
			self.value_type = value_type
		if value:
			self.value = value
		if formula:
			self.formula = formula
		if date_value:
			self.date_value = date_value
		if format:
			self.format = format
		
		if condition:
			self.condition = condition
		if condition_state:
			self.condition_state = condition_state
		if condition_color:
			self.condition_color = condition_color
		if condition_background_color:
			self.condition_background_color = condition_background_color
		
if __name__ == "__main__":
	c = SodsCell()

	print( "Test html export:")
	print( "-----------------")
	
	c.text = "hello world"
	c.condition_state = True
	c.text = "hello world"
	c.value = 123.3
	c.condition_state = False

