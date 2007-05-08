# -*- coding: utf8 -*-
"""Module docstring"""
import sys
sys.path.append(sys.path[0]+"/files")
from control import *
class GUI(Control) :
	"""Class docstring"""
	def __init__(self) :
		pass
	def showInterface (self) :
		"""method docstring"""
		pass
	def inputFile (self, filename) :
		"""method docstring"""
		pass
class CommandLine(Control) :
	"""Class docstring"""
	def __init__(self) :
		pass
	def readCommandLine (self, systemargs) :
		"""method docstring"""
		pass
		
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
        a=LineFrame()
        pass
