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
                #print sys.argv
		
                for i in range (0, len(sys.argv)):
                if sys.argv[i] == '-d':
                        self.options[0] = sys.argv[i+1]
                if sys.argv[i] == '-s':
                        self.options[1] = sys.argv[i+1]
                if sys.argv[i] == '-r':
                        self.options[2] = sys.argv[i+1]

		
if len(sys.argv)>0:
        pass #using command line
else:
        pass #using graphic interface
