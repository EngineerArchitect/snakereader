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
    def readCommandLine (self) :
        """method docstring"""
        for i in range (0, len(sys.argv)):
            if sys.argv[i] == '-d':
                self.options[0] = sys.argv[i+1]
            if sys.argv[i] == '-s':
                self.options[1] = sys.argv[i+1]
            if sys.argv[i] == '-r':
                self.options[2] = sys.argv[i+1]

sys.argv.append('a2.jpg')
sys.argv.append('a2.txt')
if len(sys.argv)>1:
    commandLine=CommandLine()
    commandLine.readCommandLine()
    picture=commandLine.inputFile(sys.argv[1])
    text=commandLine.textRecognition(picture)
    outputFile=open(sys.argv[2],'w')
    outputFile.write(text)
    outputFile.close()
else:
    pass #using graphic interface
