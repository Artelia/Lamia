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

import re
from datetime import datetime

from xlwt import *

class SodsXls():
	def __init__(self, table, i_max = 30, j_max = 30):
		''' init and set default values for spreadsheet elements '''
		
		self.table = table
		
		self.fonts = {}
		self.borders = {}
		self.fills = {}
		self.styles = {}
		
	def convertXlsFamiliy(self, font_family):
		''' return the font family name '''
		
		return font_family
		
	def convertXlsBorderWidth(self, border):
		''' return the xls border width index '''
		
		# find the width in pt
		try:
			width = float(re.search('(.+)pt', border).group(1))
			
			if width > 0 and width < 1:
				width = 1
			
			width = int(width + 0.5)
		except:
			width = 0
		
		# conver to excel widths
		if width > 3: width = 3
		
		return [Borders.NO_LINE, Borders.HAIR, Borders.MEDIUM, Borders.THICK][width]
	
	def convertXlsBorderColor(self, border):
		''' return the xls border color index '''
		
		return self.convertXlsColor(border)
		
	def convertXlsColor(self, color_str):
		''' return the xls color index '''
		
		#find color #rgb in string
		try:
			color = int(re.search('#(......)', color_str).group(1), 16)
		except:
			return 2 + 7
		
		# convert color
		xlscolor = 0
		
		if color <= 0x000000: xlscolor = 1
		elif color <= 0x000080: xlscolor = 11
		elif color <= 0x000080: xlscolor = 25
		elif color <= 0x0000FF: xlscolor = 5
		elif color <= 0x0000FF: xlscolor = 32
		elif color <= 0x003300: xlscolor = 51
		elif color <= 0x003366: xlscolor = 49
		elif color <= 0x0066CC: xlscolor = 23
		elif color <= 0x008000: xlscolor = 10
		elif color <= 0x008080: xlscolor = 14
		elif color <= 0x008080: xlscolor = 31
		elif color <= 0x00CCFF: xlscolor = 33
		elif color <= 0x00FF00: xlscolor = 4
		elif color <= 0x00FFFF: xlscolor = 8
		elif color <= 0x00FFFF: xlscolor = 28
		elif color <= 0x333300: xlscolor = 52
		elif color <= 0x333333: xlscolor = 56
		elif color <= 0x333399: xlscolor = 55
		elif color <= 0x3366FF: xlscolor = 41
		elif color <= 0x339966: xlscolor = 50
		elif color <= 0x33CCCC: xlscolor = 42
		elif color <= 0x660066: xlscolor = 21
		elif color <= 0x666699: xlscolor = 47
		elif color <= 0x800000: xlscolor = 9
		elif color <= 0x800000: xlscolor = 30
		elif color <= 0x800080: xlscolor = 13
		elif color <= 0x800080: xlscolor = 29
		elif color <= 0x808000: xlscolor = 12
		elif color <= 0x808080: xlscolor = 16
		elif color <= 0x969696: xlscolor = 48
		elif color <= 0x993300: xlscolor = 53
		elif color <= 0x993366: xlscolor = 18
		elif color <= 0x993366: xlscolor = 54
		elif color <= 0x9999FF: xlscolor = 17
		elif color <= 0x99CC00: xlscolor = 43
		elif color <= 0x99CCFF: xlscolor = 37
		elif color <= 0xC0C0C0: xlscolor = 15
		elif color <= 0xCC99FF: xlscolor = 39
		elif color <= 0xCCCCFF: xlscolor = 24
		elif color <= 0xCCFFCC: xlscolor = 35
		elif color <= 0xCCFFFF: xlscolor = 20
		elif color <= 0xCCFFFF: xlscolor = 34
		elif color <= 0xFF0000: xlscolor = 3
		elif color <= 0xFF00FF: xlscolor = 7
		elif color <= 0xFF00FF: xlscolor = 26
		elif color <= 0xFF6600: xlscolor = 46
		elif color <= 0xFF8080: xlscolor = 22
		elif color <= 0xFF9900: xlscolor = 45
		elif color <= 0xFF99CC: xlscolor = 38
		elif color <= 0xFFCC00: xlscolor = 44
		elif color <= 0xFFCC99: xlscolor = 40
		elif color <= 0xFFD400: xlscolor = 44
		elif color <= 0xFFFF00: xlscolor = 6
		elif color <= 0xFFFF00: xlscolor = 27
		elif color <= 0xFFFF99: xlscolor = 36
		elif color <= 0xFFFFCC: xlscolor = 19
		elif color <= 0xFFFFFF: xlscolor = 2
		
		return (xlscolor + 7)
	
	def getFont(self, name, height, color, font_id):
		''' find a font in the fonts disctionary '''
		
		if not font_id in self.fonts.keys():
			fnt = Font()
			fnt.name = name
			fnt.height = height
			fnt.colour_index = color
			self.fonts[font_id] = fnt
		
		return self.fonts[font_id]
	
	def getBorder(self, c, border_id):
		''' find a font in the fonts disctionary '''
		
		if not border_id in self.borders.keys():
			borders = Borders()
			if c.border_left != "none":
				borders.left = self.convertXlsBorderWidth(c.border_left)
				borders.left_colour = self.convertXlsBorderColor(c.border_left)
			if c.border_right != "none":
				borders.right = self.convertXlsBorderWidth(c.border_right)
				borders.right_colour = self.convertXlsBorderColor(c.border_right)
			if c.border_top != "none":
				borders.top = self.convertXlsBorderWidth(c.border_top)
				borders.top_colour = self.convertXlsBorderColor(c.border_top)
			if c.border_bottom != "none":
				borders.bottom = self.convertXlsBorderWidth(c.border_bottom)
				borders.bottom_colour = self.convertXlsBorderColor(c.border_bottom)
			self.borders[border_id] = borders
		
		return self.borders[border_id]
	
	def getFill(self, background_color, fill_id):
		''' find a font in the fonts disctionary '''
		
		if not fill_id in self.fills.keys():
			pattern = Pattern()
			if background_color != "default":
				pattern.pattern = Pattern.SOLID_PATTERN
				pattern.pattern_fore_colour = self.convertXlsColor(background_color)
			self.fills[fill_id] = pattern
		
		return self.fills[fill_id]
	
	def getStyle(self, fnt, borders, pattern, style_id):
		''' find a font in the fonts disctionary '''
		
		if not style_id in self.styles.keys():
			style = XFStyle()
			style.font = fnt
			style.borders = borders
			style.pattern = pattern
			self.styles[style_id] = style 
		
		return self.styles[style_id]
		
	def save(self, filename, i_max = None, j_max = None):
		''' save table in ods format '''
		
		if not i_max: i_max = self.table.i_max
		if not j_max: j_max = self.table.j_max
		
		# update cells text
		self.table.updateTable(i_max, j_max)
		
		# create new xls spreadsheet
		w = Workbook(encoding='utf-8')
		ws = w.add_sheet("sheet 1")
		
		# set table direction
		if self.table.direction == 'rtl':
			ws.cols_right_to_left = True
		
		for j in range(1, j_max):
			colname = "col" + str(j)
			c = self.table.getCellAt(0, j)
			width = float(c.column_width.replace('pt',''))
			width = int(width * 50)
			ws.col(j - 1).width = width 
		
		# make sure values are up to date
		# loop and update the cells value
		for i in range(1, i_max):
			for j in range(1, j_max):
				# update the cell text and condition
				cell = self.table.encodeColName(j) + str(i)
				c = self.table.getCellAt(i, j)
				
				# FIXME: excel output does not support conditional formating,
				# we do fixed formating of the conditional formating
				color = [c.color, c.condition_color][c.condition_state]
				background_color = [c.background_color, c.condition_background_color][c.condition_state]
				name = c.font_family
				height = 18 * int(c.font_size.replace('pt',''))
				
				# set xls style
				
				# get a font style
				font_id = name + str(height) + str(color)
				fnt = self.getFont(name, height, self.convertXlsColor(color), font_id)
				
				# get a border style
				border_id = c.border_left + c.border_right + c.border_top + c.border_bottom
				borders = self.getBorder(c, border_id)
				
				# get a fill style
				fill_id = background_color
				pattern = self.getFill(background_color, fill_id)
				
				# get style
				style_id = font_id + border_id + fill_id + c.format
				style = self.getStyle(fnt, borders, pattern, style_id)
				
				# set xls text
				if (c.formula and c.formula[0] == '=' and c.formula[:4] != '=uni'):
					if c.format == "#,##0.00":
						style.num_format_str = "#,##0.00"
					ws.write(i - 1, j - 1, Formula(c.formula[1:]), style)
				elif c.value_type == 'float' and self.table.isFloat(c.value):
					if c.format == "#,##0.00":
						style.num_format_str = "#,##0.00"
					ws.write(i - 1, j - 1, float(c.value), style)
				elif c.value_type == 'date':
					style.num_format_str = 'YYYY-MM-DD'
					ws.write(i - 1, j - 1, datetime.strptime(c.date_value, "%Y-%m-%d"), style)
				else:
					ws.write(i - 1, j - 1, c.text, style)
		
		w.save(filename)
		
if __name__ == "__main__":
	
	from sodsspreadsheet import SodsSpreadSheet
	
	t = SodsSpreadSheet(200, 200)
	
	print "Test spreadsheet naming:"
	print "-----------------------"
	
	t.setStyle("A1", text = "Hello world")
	t.setStyle("A1:G2", background_color = "#00ff00")
	t.setStyle("A3:G5", background_color = "#ffff00")
	
	t.setValue("A2", 123.4)
	t.setValue("B2", "2010-01-01")
	t.setValue("C2", "0.6")
	
	t.setValue("C5", 0.6)
	t.setValue("C6", 0.6)
	t.setValue("C7", 0.8)
	t.setValue("C8", 0.8)
	t.setValue("C9", "=AVERAGE(C5:C8)")
	t.setValue("C10", "=SUM(C5:C8)")
	
	t.setValue("D2", "= SIN(PI()/2)")
	t.setValue("D10", "=IF(A2>3;C7;C9)")
	
	t.setStyle("A3:D3", border_top = "1pt solid #ff0000")
	t.setValue("C3", "Sum of cells:")
	t.setValue("D3", "=SUM($A$2:D2)")
	
	t.setStyle("D2:D3", condition = "cell-content()<=100")
	t.setStyle("D2:D3", condition_background_color = "#ff0000")
	
	tw = SodsXls(t)
	tw.save("test.xls")
