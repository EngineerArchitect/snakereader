# -*- coding: utf8 -*-
"""Module docstring"""
from blockframe import BlockFrame
from lineframe import LineFrame
from charframe import CharFrame
from dictionary import Dictionary
class Control :
	""" class docstring"""
	def __init__(self) :#Krzysiek
		self.options = None # 
		pass
	def saveOptions (self) :#Krzysiek
		"""method docstring"""
		# returns 
		pass	
	def changeOption (self) :#Krzysiek
		"""method docstring"""
		# returns 
		pass
	def inputFile (self, filename) :#Krzysiek?Grzesiek
		"""method docstring"""
		# returns 
		pass

	def textRecognition (self) :#Pawel
		"""method docstring"""
		# returns 
		pass
	def blockSegmentation (self, BlockFrame) :#Grzesiek
		"""methot docstring"""
		# returns 
		pass
	def characterSegmentation (self, LineFrame) :#Maciek
		"""method docstring"""
		# returns 
		pass
	def characterRecognition (self, CharFrame) :#Lisu
		"""recognition of one character given as an CharFrame object, returns a string"""
		# returns 
		pass

	def textComposition (self, word) :#?
		"""method docstring"""
		# returns 
		pass
		
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
	pass
	
