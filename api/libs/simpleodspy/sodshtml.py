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
from xml.sax.saxutils import escape

class SodsHtml():
	def __init__(self, table, i_max = 30, j_max = 30):
		''' init and set default values for spreadsheet elements '''
		
		self.table = table
		
		# set default css table cell border
		self.default_border = 'none;'
		
		# takes table
		self.html_format = '''<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
%s
</head><body>
%s
</body></html>'''
	
	def fancyNumber(self, f, sep = ",", neg = "-", pos = ""):
		''' format a fancy string for a number '''
		
		# check if number is float ?
		if not self.table.isFloat(f):
			try:
				out = eval(f)
			except:
				out = f
			return out
		
		# split number
		n_parts = str(f).split(".")
		
		if len(n_parts) == 2:
			n, m = n_parts
		else:
			n, m = n_parts[0], "00"
		
		sign = False
		if n[0] == "-":
			n = n[1:]
			sign = True
		
		# call the positive int formater
		return [pos, neg][sign] + self.fancyIntNumber(n, sep) + "." + m[:2]
		
	def fancyIntNumber(self, n, sep = ","):
		''' format a fancy string for int number '''
		
		# we have string, continue
		if len(n) < 4: return n
		return self.fancyIntNumber(n[:-3]) + sep + n[-3:]
	
	def translateWidthToPx(self, string):
		''' translte inch and cm to pt '''
		
		if not string or string == "none": return "120px"
		
		# translate units
		width = re.search('([0-9.]+)((in)|(cm)|(pt))', string)
		if width:
			unit = width.group(2)
			width = float(width.group(1))
			
			if unit == 'in':
				width *= 72.0 * 2.54 
			elif unit == 'cm':
				width *= 72.0
			elif unit == 'pt':
				width = width * 2.54 
			else:
				width = 120
			
			width = str(int(width + 0.5)) + "px"
		else:
			width = "120px"
				
		return width
		
	def translateBorderToPx(self, string):
		''' translte inch and cm to pt '''
		
		if not string or string == "none": return "none"
		
		# translate units
		width = re.search('([0-9.]+)((in)|(cm)|(pt))', string)
		if width:
			unit = width.group(2)
			width = float(width.group(1))
			
			if unit == 'in':
				width *= 72.0
			elif unit == 'cm':
				width *= 72.0 / 2.54
			elif unit == 'pt':
				width = width
			else:
				width = 0
			
			if width > 0 and width < 0.5:
				width = 1
			
			width = str(int(width + 0.5)) + "px"
		else:
			width = "0px"
		
		# FIXME: chack style
		style = "solid"
		
		# check color
		color = re.search('#......', string)
		if color:
			color = color.group(0)
		else:
			color = "#000000"
		
		out = "%s %s %s" % (width, style, color)
		
		return out
		
	def exportCellCss (self, c, i = 0, j = 0):
		''' export cell data as html table cell '''
		
		# if condition state is true use condition style
		# we assume condition_state is up to date
		color = [c.color, c.condition_color][c.condition_state == True]
		background_color = [c.background_color, c.condition_background_color][c.condition_state == True]
		
		# check for default backround color
		if background_color == "default":
			background_color = "#ffffff"
		
		# adjust values for html
		cell_name = self.table.encodeCellName(i, j)
		font_size = c.font_size.replace('pt', 'px')
		border_top = self.translateBorderToPx(c.border_top)
		border_bottom = self.translateBorderToPx(c.border_bottom)
		border_left = self.translateBorderToPx(c.border_left)
		border_right = self.translateBorderToPx(c.border_right)
		text_align = c.text_align.replace('start', 'right').replace('end', 'left')
		
		direction = 'ltr'
		if self.table.direction == 'rtl':
			direction = 'rtl'
			border = border_left
			border_left = border_right
			border_right = border
		
		if c.value_type == 'float':
			direction = 'ltr'
		
		# create cell string
		# we assume text is up to date
		out = '''#%s {
	white-space: nowrap;
	padding: 2px 10px; 
	color: %s; 
	font-family: %s; 
	font-size: %s; 
	background-color: %s;
	text-align: %s;
	direction: %s;\n''' % (cell_name, color, c.font_family, font_size,
				background_color, 
				text_align, direction)
	
		if border_top != 'none':
			out += "	border-top: %s;\n" % border_top
		if border_bottom != 'none':
			out += "	border-bottom: %s;\n" % border_bottom
		if border_left != 'none':
			out += "	border-left: %s;\n" % border_left
		if border_right != 'none':
			out += "	border-right: %s;\n" % border_right
		out += "}\n"
		
		return out
	
	def exportTableCss (self, i_max = None, j_max = None):
		''' export table in html format '''
		
		if not i_max: i_max = self.table.i_max
		if not j_max: j_max = self.table.j_max
		
		# update cells text
		self.table.updateTable(i_max, j_max)
		
		# create the table element of the html page
		out = "<style type='text/css'>\n"

		#self.table.direction
		# table
		out += '''
body { direction: %s; }
table { border-collapse: collapse; }
td.header { background-color: lightgray; text-align: center; width: 50px; }
td { border: %s; }
a.info {
    position:relative;
    z-index:24;
    text-decoration:none;
    white-space: nowrap;
}
a.info:hover { z-index: 25; background-color: #efefef; }
a.info span { display: none; }
a.info:hover span {
    display: block;
    position: absolute;
    padding: 5px;
    border: 1px solid #1f1f1f;
    background-color: #efefef;
    color: #000000;
    text-align: center;
}
''' % (self.table.direction, self.default_border)
		
		# columns
		for j in range(1, j_max):
			# adjust values for html
			col_name = self.table.encodeColName(j)
			c = self.table.getCellAt(0, j)
				
			# printout
			out += "col.%s { width: %s; }\n" % (col_name, c.column_width.replace('pt','px'))
					
		# rows
		for i in range(1, i_max):
			for j in range(1, j_max):
				# adjust values for html
				cell_name = self.table.encodeCellName(i, j)
				c = self.table.getCellAt(i, j)
					
				# printout
				out += self.exportCellCss(c, i, j)
		out += "</style>"
		
		return out.encode('utf-8')
	
	def exportTableHtml(self, i_max = None, j_max = None, headers = False, tip = False):
		''' export table in html format '''
		
		if not i_max: i_max = self.table.i_max
		if not j_max: j_max = self.table.j_max
		
		# update cells text
		self.table.updateTable(i_max, j_max)
		
		# create the table element of the html page
		out = "<table>\n"
		
		# columns
		if headers:
			out += "<col class='%s' />\n" % "header"
		for j in range(1, j_max):
			width = self.translateWidthToPx(self.table.getCellAt(0, j).column_width)
			out += "<col class='%s' />\n" % self.table.encodeColName(j)
		
		if headers:
			out += "<tr>\n"
			out += "<td class='%s'></td>\n" % "header"
			for j in range(1, j_max):
				out += "<td class='%s'>%s</td>\n" % ("header", self.table.encodeColName(j))
			out += "</tr>\n"
		
		# rows
		for i in range(1, i_max):
			out += "<tr>\n"
			if headers:
				out += "<td class='%s'>%d</td>\n" % ("header", i)
			for j in range(1, j_max):
				# adjust values for html
				cell_name = self.table.encodeCellName(i, j)
				c = self.table.getCell(cell_name)
				
				# get cell text
				if c.value_type == 'float':
					if c.format == "":
						text = str(c.value)
					if c.format == "#,##0.00":
						text = self.fancyNumber(c.value)
				else:
					text = escape(c.text)
				
				# clean up empty cells
				text = text.strip()
				if text == "": text = '&nbsp;'
				
				# add tooltip
				if tip:
					tip = cell_name
					if c.formula:
						tip += "&nbsp;=&nbsp;" + escape(c.formula[1:])
					else:
						tip += "&nbsp;=&nbsp;" + text
				
					text = "<a class='info'>%s<span>%s</span></a>" % (text, tip)
				
				# printout
				out += "<td id = '%s'>%s</td>\n" % (cell_name, text)
			out += "</tr>\n"
		out += "</table>"
		
		return out
	
	def exportHtml(self, i_max = None, j_max = None, headers = False, tip = False):
		''' export table in html format '''
		
		return self.html_format % (self.exportTableCss(i_max, j_max),
			self.exportTableHtml(i_max, j_max, headers, tip))
	
	def save(self, filename, i_max = None, j_max = None, headers = False, tip = False):
		''' save table in xml format '''
		
		# if filename is - print to stdout
		if filename == '-':
			print self.exportHtml(i_max, j_max, headers, tip)
		else:
			file(filename,"w").write(self.exportHtml(i_max, j_max, headers, tip))
		
if __name__ == "__main__":
	
	from sodsspreadsheet import SodsSpreadSheet
	
	t = SodsSpreadSheet(20,6)
	
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
	
	tw = SodsHtml(t)
	tw.save("test.html")
	
