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
import math
from datetime import datetime


from .sodstable import SodsTable

class SodsSpreadSheet(SodsTable):
	def __init__(self, i_max = 30, j_max = 30):
		''' init and set default values for spreadsheet elements '''
		
		SodsTable.__init__(self, i_max, j_max)
		
		# init function list
		self.registered_functions = []
		
		# do not recalculate automaticaly all cells
		self.fast = False
		
		# add functions
		self.registerFunction('AVERAGE', self.averageCallback)
		self.registerFunction('IF', self.ifCallback)
		self.registerFunction('CUT', self.cutCallback)
		
	def registerFunction(self, function_name, function_callback):
		''' register a spreadsheet function '''
		
		self.registered_functions.append((function_name, function_callback))
		
	def parseColName(self, name):
		''' parse a col name "A" or "BC" to the col number 1.. '''
		
		if name == '':
			return 0
		
		return (ord(name[-1:]) - ord('A') + 1) + 26 * self.parseColName(name[:-1])
	
	def encodeColName(self, n):
		''' encode a col number 1.. to a name "A" or "BC" '''
		
		n1 = (n - 1) % 26
		n2 = int((n - 1) / 26)
		
		if n2 == 0:
			return chr(ord('A') + n1)
		
		return chr(ord('A') + n2 - 1) + chr(ord('A') + n1)
		
	def encodeCellName(self, i, j, i2 = None, j2 = None):
		''' encode a cell i, j coordinates to a name "A1" or "BC23" '''
		
		if (i2 and not j2): j2 = j
		if (not i2 and j2): i2 = i
		
		if i2:
			return self.encodeCellName(i, j) + ":" + self.encodeCellName(i2, j2)
		
		return self.encodeColName(j) + str(i)
		
	def parseOneCellName(self, name):
		''' parse a cell name "A2" or "BC43" to the row and col numbers (2,3) '''
		
		# A..ZZ part is columns numbers (j) and the number part is rows (i)
		p = re.search('([A-Z]+)([0-9]+)', name)
		if p:
			return (int(p.group(2)), self.parseColName(p.group(1)))
			
		return None
	
	def parseCellName(self, name):
		''' parse a cell name or a range name
		
		parse "B3", "A2:A4" or "A1:BC43" to the row and col ranges ([2,3,4],[3]) 
		'''
		names = name.split(':')
		
		# if this is one cell return the cell
		if len(names) == 1:
			return self.parseOneCellName(names[0])
		
		# if this is a range, get the two cells
		if len(names) == 2:
			a1 = self.parseOneCellName(names[0])
			a2 = self.parseOneCellName(names[1])
			
			if a1 and a2:
				return (range(a1[0], a2[0] + 1), range(a1[1], a2[1] + 1))
			
		return None
	
	def parseCellRangeToCells(self, name):
		''' parse a range name "A2:A4" or "A1:BC43" to array of cells '''
		
		cell_list = []
		
		# loop and create the cells list
		for cell in self.rangeIterator(name):
			cell_list.append(cell)
		
		return cell_list
	
	def rangeIterator(self, range_str):
		''' parse a range name "A2:A4" or "A1:BC43" to array of cells '''
		
		# parse the rnage
		i_range, j_range = self.parseCellName(range_str)
		
		# we want ranges
		if type(i_range) != type(list()):
			i_range = [i_range]
		
		if type(j_range) != type(list()):
			j_range = [j_range]
		
		# loop and yield cells 
		for i in i_range:
			for j in j_range:
				yield self.encodeCellName(i, j)
		
	def isFloat(self, x):
		''' return true if x represent float '''
		
		try:
			y = float(x)
			return True
		except:
			return False
		
		return False
	
	def isDate(self, x):
		''' return true if x represent date '''
		
		try:
			y = datetime.strptime(x, "%Y-%m-%d")
			return True
		except:
			return False
		
		return False
	
	def setCell(self, name, cell):
		''' insert a cell in cell name '''
		
		i, j = self.parseCellName(name)
		self.setCellAt(i, j, c)
		
	def getCell(self, name):
		''' get the cell in cell name '''
		
		i, j = self.parseCellName(name)
		return self.getCellAt(i, j)
		
	def setValue(self, name, value):
		''' set cell/s value and type automatically '''
		
		# parse i,j from cell name
		i_range, j_range = self.parseCellName(name)
		
		# we want ranges
		if type(i_range) != type(list()):
			i_range = [i_range]
		
		if type(j_range) != type(list()):
			j_range = [j_range]
		
		# loop on cell range
		for i in i_range:
			for j in j_range:
				# get the cell
				c = self.getCellAt(i, j)
		
				# delete old value
				c.text = ""
				c.value_type = "string"
				c.value = None
				c.formula = None
				c.date_value = None
			
				# check cell type
				if type(value) == type(str()) and len(value) > 0 and value[0] in ['=', '!']:
					c.value_type = "float"
					c.formula = value
				elif self.isFloat(value):
					c.value_type = "float"
					c.value = float(value)
					c.text = str(value)
				elif self.isDate(value):
					c.value_type = "date"
					c.date_value = str(value)
					c.text = str(value)
				else:
					c.value_type = "string"
					c.text = str(value)
			
				# set the cell
				self.setCellAt(i, j, c)
	
	def setStyle(self, name, 
			font_size = None, font_family = None, color = None, 
			background_color = None, border_top = None,
			border_bottom = None, border_left = None, border_right = None,
			text = None, value_type = None,
			value = None, formula = None,
			date_value = None,
			condition = None, condition_state = None,
			condition_color = None, condition_background_color = None):
		''' set values of cell object range in i, j ranges '''
		
		# parse i,j from cell name
		i, j = self.parseCellName(name)
		
		# set at can handle i,j ranges
		self.setAt(i, j, 
			font_size, font_family, color, 
			background_color, border_top,
			border_bottom, border_left, border_right,
			text, value_type,
			value, formula,
			date_value,
			condition, condition_state,
			condition_color, condition_background_color)
		
	def getRangeString(self, cells):
		''' create a string of cells from range '''
		
		# we work with a string, 
		# get the re.group string
		cell_range = cells.group(0)
			
		# get the cell list
		cell_list = self.parseCellRangeToCells(cell_range)
		
		out = "(" + ",".join(cell_list) + ")"
			
		# return the sum as string
		return out
	
	def functionCallbackWrapper(self, f, args_string):
		''' return the updated float value of a cell input name is re group '''
		
		# we work with a string, 
		# get the re.group args string
		args = args_string.group(1)
		
		# return a string that represents the function value
		try:
			ans = f(args)
		except:
			ans = args_string.group(0)
		
		return ans
		
	def averageCallback(self, args_string):
		''' return the average value of cell group '''
		
		# return a string that represents the function value
		return "(sum(" + args_string + ")/len(" + args_string + "))"
	
	def ifCallback(self, args_string):
		''' return the result of an if function '''
		
		# get the if funtion args: IF(condion, val_true, val_false)
		args = args_string.replace(';',',')
		args_list = args.split(',')
		
		if len(args_list) == 3:
			try:
				if self.evaluateFormula(args_list[0]):
					return str(self.evaluateFormula(args_list[1]))
				else:
					return str(self.evaluateFormula(args_list[2]))
			except:
				pass
		
		return "!ERR"
	
	def cutCallback(self, args_string):
		''' return the result of a cut function '''
		
		# get the cut funtion args: cut(string, field number, delimeter = ',')
		args = args_string.replace(';',',')
		args_list = args.split(',')
		args_len = len(args_list)
		
		if args_len in [2, 3]:
			try:
				string = self.evaluateFormula(args_list[0])
				field = int(self.evaluateFormula(args_list[1]))
				if args_len == 3:
					# get the value inside quotes
					delimeter = re.search("'(.*)'", args_list[2]).group(1)
				else:
					delimeter = ','
				return string.split(delimeter)[field]
			except:
				pass
		
		return "!ERR"
	
	def getOneCellValueRe(self, name):
		''' return the updated float value of a cell input name is re group '''
		
		# we work with a string, 
		# get the re.group string
		name = name.group(0)
		
		return self.getOneCellValue(name)
	
	def getOneCellValue(self, name):
		''' return the updated float value of a cell '''
		
		# parse i,j from cell name
		i, j = self.parseCellName(name)
		
		c = self.getCellAt(i, j)
		
		# if this is not a float cell return 0
		if  c.text == "":
			return "0.0"
		elif c.value_type == 'string' and c.text != "":
			return "'%s'" % c.text
		
		# this is a date
		# FIXME: cacultae date number, julian ?
		elif c.value_type == 'date':
			return "0.0"
		
		# if this is just a value, return it
		elif not c.formula:
			return str(c.value)
		
		# this is a formula, we need to update it's value
		self.updateOneCell(name)
		
		# re-get the cell
		c = self.getCellAt(i, j)
		
		return str(c.value)
	
	def evaluateFormula(self, formula):
		''' evaluate the value of a formula '''
		
		# remove white noise
		formula = formula.upper()
		formula = formula.replace('!', '')
		formula = formula.replace('$', '')
		formula = formula.replace('PI()', 'PI')
		
		# to to simply evalute the formula as is
		try:
			return eval(fromula)
		except:
			pass
		
		# look for user defined functions and replace them with user data
		for f_name, f_callback in self.registered_functions:
			formula = re.sub(f_name + '[(](.+)[)]', lambda f: self.functionCallbackWrapper(f_callback, f), formula)
			
		# check for ranges e.g. 'A2:G3' and replace them with (A2,A3 ... G3) tupple
		formula = re.sub('[A-Z]+[0-9]+:[A-Z]+[0-9]+', 
			self.getRangeString, formula)
		
		# replce spreadsheet function names to python function
		formula = formula.replace('SUM(', 'sum(')
		formula = formula.replace('MIN(', 'min(')
		formula = formula.replace('MAX(', 'max(')
		formula = formula.replace('ABS(', 'abs(')
		
		formula = formula.replace('POWER(', 'math.pow(')
		formula = formula.replace('SQRT(', 'math.sqrt(')
		
		formula = formula.replace('PI', 'math.pi')
		formula = formula.replace('SIN(', 'math.sin(')
		formula = formula.replace('COS(', 'math.cos(')
		formula = formula.replace('TAN(', 'math.cos(')
		formula = formula.replace('ASIN(', 'math.asin(')
		formula = formula.replace('ACOS(', 'math.acos(')
		formula = formula.replace('ATAN(', 'math.atan(')
		
		# get all the cell names in this formula and replace them with values
		formula = formula.replace(';', '')
		try:
			value = eval(re.sub('[A-Z]+[0-9]+', self.getOneCellValueRe, formula))
		except:
			# FIXME: is this a good thing ?
			value = re.sub('[A-Z]+[0-9]+', self.getOneCellValueRe, formula)
			
		return value
		
	def updateOneCell(self, name):
		''' update one cell text '''
		
		# parse i,j from cell name
		i, j = self.parseCellName(name)
		
		c = self.getCellAt(i, j)
		
		# in fast mode, if we have a value, do not re-calculate
		if self.fast and c.value != None: 
			return
		
		# check if the cell has formula
		if c.formula:
			# try to calculate the formula
			try:
				# remove the '=' prefix
				formula = c.formula[1:]
				
				value = self.evaluateFormula(formula)
				
				# if answer is string encapsulte
				if not self.isFloat(value):
					c.value = "'%s'" % value
					c.text = value
				else:
					# update cell value and text string
					c.value = value
					c.text = str(value)
			except:
				c.value = 0
				c.text = "!ERR"
			
		# check if the cell has condition
		if c.condition:
			# replace the cell-content() function with the cells value
			if (c.value != None):
				value = c.value
			else:
				value = self.getOneCellValue(name)
			formula = c.condition.replace("cell-content()", str(value))
		
			# evaluate the condition formula
			try:
				value = self.evaluateFormula(formula)
			except:
				value = False
			
			# update condition state
			c.condition_state = value
		
		self.setCellAt(i, j, c)
		
	def updateCell(self, name):
		''' update cell text value '''
		
		# parse i,j from cell name
		i_range, j_range = self.parseCellName(name)
		
		# we want ranges
		if type(i_range) != type(list()):
			i_range = [i_range]
		
		if type(j_range) != type(list()):
			j_range = [j_range]
		
		# clear old caculations
		# loop and clear the cells value
		if self.fast:
			for i in i_range:
				for j in j_range:
					c = self.getCellAt(i, j)
					if c.formula: c.value = None
					self.setCellAt(i, j, c)
					
		# loop and update the cells value
		for i in i_range:
			for j in j_range:
				cell = self.encodeCellName(i, j)
				self.updateOneCell(cell)
	
	def updateTable(self, i_max = None, j_max = None):
		''' update table texts values '''
		
		if not i_max: i_max = self.i_max
		if not j_max: j_max = self.j_max
		
		self.fast = True
		
		# clear old caculations
		# loop and clear the cells value
		for i in range(1, i_max):
			for j in range(1, j_max):
				c = self.getCellAt(i, j)
				if c.formula: c.value = None
				self.setCellAt(i, j, c)
				
		# recalculate values
		# loop and update the cells value
		for i in range(1, i_max):
			for j in range(1, j_max):
				cell = self.encodeCellName(i, j)
				self.updateOneCell(cell)
		
		self.Fast = False
		
if __name__ == "__main__":
	
	t = SodsSpreadSheet()
	
	print( "Test spreadsheet naming:")
	print( "-----------------------")
	
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
	
	t.setValue("D2", "=SIN(PI()/2)")
	t.setValue("D10", "=IF(A2>3,C7,C9)")
	
	t.setValue("D11", "Hello world, ")
	t.setValue("D12", "=D11 * 2")
	t.setValue("D13", "=CUT(D12,2, ' ')")
	
	t.setStyle("A3:D3", border_top = "1pt solid #ff0000")
	t.setValue("C3", "Sum of cells:")
	t.setValue("D3", "=SUM($A$2:D2)")
	
	t.setStyle("D2:D3", condition = "cell-content()<=100")
	t.setStyle("D2:D3", condition_background_color = "#ff0000")
	
	t.updateTable()
	
	print( t.getCell("D3").text)
	print( t.getCell("D3").condition_state)
	print( t.getCell("D11").text)
	print( t.getCell("D13").text)
	
	
