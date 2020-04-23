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
from xml.etree import ElementTree
from xml.sax.saxutils import unescape

from sodscell import SodsCell

class SodsXml():
	def __init__(self, table, i_max = 30, j_max = 30):
		''' init and set default values for spreadsheet elements '''
		
		self.table = table
		
		# dtd for the xml import/export
		# TODO: add dtd or scheme
		self.dtd= ''' '''
		
		# takes dtd, cells
		self.xml_format = '''<?xml version="1.0" encoding="UTF-8"?>
%s
<table>
%s</table>'''
	
	def exportCellXml(self, c, i = 0, j = 0):
		''' export cell data as xml table cell '''
		
		text = escape(c.text)
		
		if c.formula:
			formula = escape(c.formula)
		else:
			formula = 'None'
		if c.condition:
			condition = escape(c.condition)
		else:
			condition = 'None'
		if c.format:
			format = escape(format)
		else:
			format = 'None'
			
		# create cell string
		out = '''
<cell>
	<i>{0}</i>
	<j>{1}</j>
	
	<color>{2}</color>
	<font_family>{3}</font_family>
	<font_size>{4}</font_size>
	
	<background_color>{5}</background_color>
	<border_top>{6}</border_top>
	<border_bottom>{7}</border_bottom>
	<border_left>{8}</border_left>
	<border_right>{9}</border_right>
	
	<text>{10}</text>
	<value_type>{11}</value_type>
	<value>{12}</value>
	<formula>{13}</formula>
	<date_value>{14}</date_value>
	
	<condition>{15}</condition>
	<condition_state>{16}</condition_state>
	<condition_color>{17}</condition_color>
	<condition_background_color>{18}</condition_background_color>
	
	<text_align>{19}</text_align>
	<column_width>{20}</column_width>
	<format>{21}</format>
</cell>'''.format(i, j,
				c.color, c.font_family, c.font_size,
				c.background_color, 
				c.border_top, c.border_bottom, 
				c.border_left, c.border_right,
				text, c.value_type, c.value, 
				formula, c.date_value, 
				condition, c.condition_state, 
				c.condition_color, c.condition_background_color,
				c.text_align, c.column_width, format)
		
		return out
	
	
	def exportXml(self, i_max = None, j_max = None):
		''' export table in xml format '''
		
		if not i_max: i_max = self.table.i_max
		if not j_max: j_max = self.table.j_max
		
		# update cells text
		self.table.updateTable(i_max, j_max)
		
		out = ""
		
		for i in range(1, i_max):
			for j in range(1, j_max):
				out += self.exportCellXml(self.table.getCellAt(i,j), i,j)
		
		return self.xml_format % (self.dtd, out)
	
	def importXml(self, xml_text):
		''' load cells from text in xml format '''
		
		# get the cells elements from our xml file
		xml_table = ElementTree.XML(xml_text)
		
		# loop on all the cells in xml file
		for xml_cell in xml_table:
			# FIXME: we assume that all the cell element are in the right
			# order
			
			# get i, j
			i, j = int(xml_cell[0].text), int(xml_cell[1].text)
			
			# get cell
			c = SodsCell()
			
			c.color = xml_cell[2].text
			c.font_family = xml_cell[3].text
			c.font_size = xml_cell[4].text
			
			c.background_color = xml_cell[5].text
			c.border_top = xml_cell[6].text
			c.border_bottom = xml_cell[7].text
			c.border_left = xml_cell[8].text
			c.border_right = xml_cell[9].text
	
			if xml_cell[10].text:
				c.text = unescape(xml_cell[10].text)
			c.value_type = xml_cell[11].text
			c.value = [None, xml_cell[12].text][xml_cell[12].text != 'None']
			c.formula = [None, unescape(xml_cell[13].text)][xml_cell[13].text != 'None']
			c.date_value = [None, xml_cell[14].text][xml_cell[14].text != 'None']
	
			c.condition = [None, unescape(xml_cell[15].text)][xml_cell[15].text != 'None']
			c.condition_state = eval(xml_cell[16].text)
			c.condition_color = xml_cell[17].text
			c.condition_background_color = xml_cell[18].text
			
			text_align = xml_cell[19].text
			c.column_width = xml_cell[20].text
			c.format = [None, unescape(xml_cell[21].text)][xml_cell[21].text != 'None']
			
			# insert cell to table
			self.table.setCellAt(i, j, c)
		
	def save(self, filename, i_max = None, j_max = None):
		''' save table in xml format '''
		
		# if filename is - print to stdout
		if filename == '-':
			print self.exportXml(i_max, j_max)
		else:
			file(filename,"w").write(self.exportXml(i_max, j_max))
		
	def load(self, filename):
		''' load table in xml format '''
		
		self.importXml(file(filename).read())
		
if __name__ == "__main__":
	
	from sodsspreadsheet import SodsSpreadSheet
	
	t = SodsSpreadSheet()
	
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
	
	tw = SodsXml(t)
	tw.save("test.xml")
	
