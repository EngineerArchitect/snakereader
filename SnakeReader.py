# -*- coding: utf8 -*-
"""Module docstring"""
import sys
sys.path.append(sys.path[0]+"/files")
from control import *
class GUI(Control) :
	"""Class docstring"""
	def showInterface (self) :
		"""method docstring"""
		pass
class CommandLine(Control) :
	"""Class docstring"""
	def readCommandLine (self, systemargs) :
		"""method docstring"""
		pass
		
if len(sys.argv)>0:
        pass #using command line
else:
        pass #using graphic interface
