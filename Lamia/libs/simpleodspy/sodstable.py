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

from .sodscell import SodsCell

class SodsTable:
	def __init__(self, i_max = 30, j_max = 30):
		''' init and set default values for table elements '''
		
		# the data table
		self.rows = {}
		
		self.i_max = i_max
		self.j_max = j_max
		
		# table style
		self.direction = 'ltr'
		
	def getCellAt(self, i, j):
		''' get the cell object in i,j '''
		
		# try to get the row i
		row = self.rows.get(i, {})
		
		# try to get the cell j
		return row.get(j, SodsCell())
	
	def setCellAt(self, i, j, new_cell):
		''' set the cell object in i, j '''
		
		# try to get the row i, if row is empty create new one
		row = self.rows.get(i, {})
		
		# if the value is Null, delete cell
		if new_cell:
			row[j] = new_cell
			self.rows[i] = row
		else:
			del row[j]
			# if we deleted the last cell in the row delete it
			if len(row) < 1:
				del self.rows[i]
		
	def setAt(self, i_range, j_range, 
			font_size = None, font_family = None, color = None, 
			background_color = None, border_top = None,
			border_bottom = None, border_left = None, border_right = None,
			text = None, value_type = None,
			value = None, formula = None,
			date_value = None,
			condition = None, condition_state = None,
			condition_color = None, condition_background_color = None,
			text_align = None, format = None,
			column_width = None):
		''' set values of cell object range in i, j ranges '''
		
		# we want ranges
		if type(i_range) != type(list()):
			i_range = [i_range]
		
		if type(j_range) != type(list()):
			j_range = [j_range]
		
		# loop on cell range
		for i in i_range:
			for j in j_range:
				# get the cell in i,j
				c = self.getCellAt(i, j)
				
				# set cell data
				c.set(font_size, font_family, color, 
					background_color, border_top,
					border_bottom, border_left, border_right,
					text, value_type, value, formula, date_value,
					condition, condition_state,
					condition_color, condition_background_color,
					text_align, format, column_width)
		
				# return cell to table
				self.setCellAt(i, j, c)
	
if __name__ == "__main__":
	
	t = SodsTable()
	
	t.setAt(1,1, text = "hello world")
	t.setAt(1,range(1,3), background_color = "#00ff00")
	
	
