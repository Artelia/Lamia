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

import sys
from xml.sax.saxutils import escape
from xml.sax.saxutils import unescape
import re

from odf.opendocument import OpenDocumentSpreadsheet
from odf.opendocument import load
from odf.table import Table, TableColumn, TableRow, TableCell
from odf.style import Style, TableProperties, TextProperties, TableCellProperties, TableColumnProperties, Map
from odf.number import NumberStyle, DateStyle, CurrencyStyle, TextStyle, Number, Text, Day, Month, Year, Era
from odf.text import P, Date

from sodscell import SodsCell

class SodsOds():
	def __init__(self, table, i_max = 30, j_max = 30):
		''' init and set default values for spreadsheet elements '''
		
		self.table = table
		self.styles = {}
	
	def getStyle(self, c, cell, datastylename, style_id, odfdoc):
		''' get a style_name by style_id '''
		
		if not style_id in self.styles.keys():
			# create new style
			cs = Style(name = cell, family = 'table-cell', datastylename=datastylename)
			cs.addElement(TextProperties(color = c.color, 
				fontsize =c.font_size, fontfamily = c.font_family))
			
			# set backgound and borders
			if c.background_color != "default" and c.background_color != "transparent":
				cs.addElement(TableCellProperties(backgroundcolor = c.background_color))
			if c.border_top != "none":
				cs.addElement(TableCellProperties(bordertop = c.border_top))
			if c.border_bottom != "none":
				cs.addElement(TableCellProperties(borderbottom = c.border_bottom))
			if c.border_left != "none":
				cs.addElement(TableCellProperties(borderleft = c.border_left))
			if c.border_right != "none":
				cs.addElement(TableCellProperties(borderright = c.border_right))
			
			# set ods conditional style
			if (c.condition):
				cns = Style(name = "cns"+cell, family = 'table-cell')
				cns.addElement(TextProperties(color = c.condition_color))
				cns.addElement(TableCellProperties(backgroundcolor = c.condition_background_color))
				odfdoc.styles.addElement(cns)
				
				cs.addElement(Map(condition = c.condition, applystylename = "cns"+cell))
				
			odfdoc.automaticstyles.addElement(cs)
			
			self.styles[style_id] = cell
		
		return self.styles[style_id]
	
	def translateBorderToPt(self, string):
		''' translte inch and cm to pt '''
		
		if not string or string == "none": return "none"
		out = unescape(string)
		
		# translate units
		width = re.search('[0-9.]+((in)|(cm)|(pt))', out)
		if width:
			width = width.group(0)
			width = re.sub('([0-9.]+)in', lambda s: str(float(s.group(1)) * 72.0) + "pt", width)
			width = re.sub('([0-9.]+)cm', lambda s: str(float(s.group(1)) * 72.0 / 2.54) + "pt", width)
		else:
			width = "1pt"
		
		# FIXME: chack style
		style = "solid"
		
		# check color
		color = re.search('#......', out)
		if color:
			color = color.group(0)
		else:
			color = "#000000"
		
		out = "%s %s %s" % (width, style, color)
		
		return out
	
	def translateToPt(self, string):
		''' translte inch and cm to pt '''
		
		if not string: return "12pt"
		width = unescape(string)
		
		# translate units
		width = re.search('[0-9.]+((in)|(cm)|(pt))', width)
		if width:
			width = width.group(0)
			width = re.sub('([0-9.]+)in', lambda s: str(int(float(s.group(1)) * 72.0 + .5)) + "pt", width)
			width = re.sub('([0-9.]+)cm', lambda s: str(int(float(s.group(1)) * 72.0 / 2.54 + .5)) + "pt", width)
		else:
			width = "12pt"
		
		return width

	def cleanFormual(self, string):
		''' clean odf formula '''
		
		if not string: return None
		
		out = string.encode('utf-8')
		out = re.sub("[$]'.+'", lambda s: "", out)
		out = out.replace(' ', '')
		out = out.replace('[.', '')
		out = out.replace(']', '')
		out = out.replace(':.', ':')
		
		return out
	
	def getCellText(self, cell):
		''' extract text from cell '''
		
		text = ''
		for p in cell.getElementsByType(P):
			for p_data in p.childNodes:
				if p_data.tagName == 'Text':
					data = p_data.data
					text += unescape(data.encode('utf-8'))
				if p_data.tagName == 'text:span':
					data = p_data.firstChild
					if data:
						text += unescape(data.data.encode('utf-8'))
		
		return text
	
	def load(self, filename):
		''' load a table in ods format '''
		
		# read the file
		doc = load(filename)
		
		# get table style
		self.table.direction = 'ltr'
		try:
			stylename = doc.getElementsByType(Table)[0].getAttribute('stylename')
			style = doc.getStyleByName(stylename)
			tps = style.getElementsByType(TableProperties)
			for tp in tps:
				if tp.getAttribute('writingmode') == 'rl-tb':
					self.table.direction = 'rtl'
		except:
			pass
		
		# loop on all rows and columns
		i = 0
		for row in doc.getElementsByType(TableRow):
			j = 1
			i += 1
			for cell in row.getElementsByType(TableCell):
				
				# creat a new cell
				c = SodsCell()
				
				try:
					numbercolumnsrepeated = int(cell.getAttribute('numbercolumnsrepeated'))
				except:
					numbercolumnsrepeated = 1
				
				c.text = self.getCellText(cell)
							
				c.value_type = cell.getAttribute('valuetype')
				
				# FIXME: no percentage support, convert to float
				if c.value_type == 'percentage': c.value_type = 'float'
				
				c.formula = cell.getAttribute('formula')
				if c.formula:
					c.formula = self.cleanFormual(c.formula[3:])
				c.date_value = cell.getAttribute('datevalue')
				c.value = cell.getAttribute('value')
				
				stylename = cell.getAttribute('stylename')
				if stylename:
					style = doc.getStyleByName(stylename)
					
					# parse data style
					# this only work on patch'd version of odfpy
					# file:opendocument.py, function:build_caches
					# -if element.qname == (STYLENS, u'style')):
					# +if element.qname in ((STYLENS, u'style'), (NUMBERNS,u'number-style')):
					datastylename = style.getAttribute('datastylename')
					if datastylename:
						datastyle = doc.getStyleByName(datastylename)
						if datastyle:
							p = datastyle.getElementsByType(Number)[0]
							if p:
								decimalplaces = p.getAttribute('decimalplaces')
								grouping = p.getAttribute('grouping')
								
								if decimalplaces == '2' and grouping == 'true':
									c.format = "#,##0.00"
								else:
									c.format = ""
					
					for p in style.getElementsByType(TextProperties):
						c.font_family = p.getAttribute('fontfamily')
						if not c.font_family:
							c.font_family = "Arial"
						c.font_size = self.translateToPt(p.getAttribute('fontsize'))
						c.color = p.getAttribute('color')
						if not c.color:
							c.color = "#000000"
							
					for p in style.getElementsByType(TableCellProperties):
							
						c.background_color = p.getAttribute('backgroundcolor')
						if not c.background_color or c.background_color == "transparent":
							c.background_color = "default"
						border = self.translateBorderToPt(p.getAttribute('border'))
						if border == "none":
							c.border_top = self.translateBorderToPt(p.getAttribute('bordertop'))
							c.border_bottom = self.translateBorderToPt(p.getAttribute('borderbottom'))
							c.border_left = self.translateBorderToPt(p.getAttribute('borderleft'))
							c.border_right = self.translateBorderToPt(p.getAttribute('borderright'))
						else:
							c.border_top = border
							c.border_bottom = border
							c.border_left = border
							c.border_right = border
						
					for p in style.getElementsByType(Map):
						c.condition = p.getAttribute('condition')
						if c.condition:
							c.condition = self.cleanFormual(c.condition)
						
						applystylename = p.getAttribute('applystylename')
						applystyle = doc.getStyleByName(applystylename)
					
						for cp in applystyle.getElementsByType(TextProperties):
							c.condition_color = cp.getAttribute('color')
					
						for cp in applystyle.getElementsByType(TableCellProperties):
							c.condition_background_color = cp.getAttribute('backgroundcolor')
				
				# check for sodsOds formulas (starting with !)
				if len(c.text) > 0 and c.text[0] == '!':
					c.formula = c.text
					c.value_type = "float"
				
				# insert cell to table
				while numbercolumnsrepeated > 0:
					self.table.setCellAt(i, j, c)
					j += 1
					numbercolumnsrepeated -= 1
				
	def save(self, filename, i_max = None, j_max = None):
		''' save table in ods format '''
		
		if not i_max: i_max = self.table.i_max
		if not j_max: j_max = self.table.j_max
		
		# update cells text
		self.table.updateTable(i_max, j_max)
		
		# create new odf spreadsheet
		odfdoc = OpenDocumentSpreadsheet()
		
		# set direction style
		rtl = Style(name = "dir", family = "table")
		if self.table.direction == 'rtl':
			rtl.addElement(TableProperties(writingmode="rl-tb"))
		odfdoc.automaticstyles.addElement(rtl)
		
		# create the table
		table = Table(name = "sheet 1", stylename = 'dir')
		
		# default style
		ts = Style(name = "ts", family = "table-cell")
		ts.addElement(TextProperties(fontfamily = SodsCell().font_family, fontsize = SodsCell().font_size))
		odfdoc.styles.addElement(ts)
		
		# create columns
		for j in range(1, j_max):
			colname = "col" + str(j)
			c = self.table.getCellAt(0, j)
			width = c.column_width
			cs = Style(name = colname, family = "table-column")
			cs.addElement(TableColumnProperties(columnwidth = width, breakbefore = "auto"))
			odfdoc.automaticstyles.addElement(cs)

			table.addElement(TableColumn(stylename = colname, defaultcellstylename = "ts"))
			
		# make sure values are up to date
		# loop and update the cells value
		for i in range(1, i_max):
			# create new ods row
			tr = TableRow()
			table.addElement(tr)
			
			# create default data styles for dates and numbers
			ncs = NumberStyle(name="ncs")
			ncs.addElement(Number(decimalplaces="2", minintegerdigits="1", grouping="true"))
			odfdoc.styles.addElement(ncs)
			
			ncs2 = NumberStyle(name="ncs2")
			ncs2.addElement(Number(decimalplaces="0", minintegerdigits="1", grouping="false"))
			odfdoc.styles.addElement(ncs2)
			
			dcs = DateStyle(name="dcs")
			dcs.addElement(Year(style='long'))
			dcs.addElement(Text(text = u'-'))
			dcs.addElement(Month(style='long'))
			dcs.addElement(Text(text = u'-'))
			dcs.addElement(Day(style='long'))
			odfdoc.styles.addElement(dcs)
			
			for j in range(1, j_max):
				# update the cell text and condition
				cell = self.table.encodeColName(j) + str(i)
				c = self.table.getCellAt(i, j)
				
				# chose datastylename
				if c.value_type == 'date':
					datastylename = "dcs"
				else:
					if c.format == "":
						datastylename = "ncs2"
					if c.format == "#,##0.00":
						datastylename = "ncs"
					
				# get cell style id
				if (c.condition):
					style_id = (datastylename + c.color + c.font_size + c.font_family + 
						c.background_color + c.border_top + c.border_bottom + 
						c.border_left + c.border_right + 
						c.condition_color + c.condition_background_color)
				else:
					style_id = (datastylename + c.color + c.font_size + c.font_family + 
						c.background_color + c.border_top + c.border_bottom + 
						c.border_left + c.border_right)
				
				# set ods style
				style_name = self.getStyle(c, cell, datastylename, style_id, odfdoc)
				
				# create new ods cell
				if (c.formula and c.formula[0] == '=' and c.formula[:4] != '=uni'):
					if self.table.isFloat(c.value):
						tc = TableCell(valuetype = c.value_type, 
							formula = c.formula, value = float(c.value), stylename = style_name)
					else:
						tc = TableCell(valuetype = c.value_type, 
							formula = c.formula, 
							value = 0, stylename = style_name)
				elif (c.value_type == 'date'):
					tc = TableCell(valuetype = c.value_type, 
						datevalue = c.date_value, stylename = style_name)
				elif (c.value_type == 'float') and self.table.isFloat(c.value):
					tc = TableCell(valuetype = c.value_type, 
						value = float(c.value), stylename = style_name)
				else:
					tc = TableCell(valuetype = 'string', stylename = style_name)
				
				# set ods text
				tc.addElement(P(text = unicode(escape(c.text), 'utf-8')))
				
				tr.addElement(tc)

		odfdoc.spreadsheet.addElement(table)
		odfdoc.save(filename)
		
if __name__ == "__main__":
	
	from sodsspreadsheet import SodsSpreadSheet
	
	t = SodsSpreadSheet(12, 12)
	
	print( "Test spreadsheet naming:")
	print( "-----------------------")
	
	t.setStyle("A1", text = "שלום עולם")
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
	
	tw = SodsOds(t)
	tw.save("test.ods")
	
	print( "Test load:")
	print( "----------")
	
	t2 = SodsSpreadSheet(12, 12)
	tw = SodsOds(t2)
	tw.load("test.ods")
	
	print( t2.getCell("A1").text)
	print( t2.getCell("D3").condition_state)
