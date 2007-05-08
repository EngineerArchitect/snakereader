# -*- coding: utf8 -*-
"""Module docstring"""
from blockframe import *
from lineframe import *
from charframe import *
from dictionary import *
class Control:
    def __init__(self):
        optionFile=open('options.ini','r')
        optionList=optionFile.readlines()
        optionFile.close()
        self.options=[int(opt[opt.index('=')+1:]) for opt in optionList]
    def saveOptions(self):
        """method docstring"""
        optionFile=open('options.ini','r')
        optionList=optionFile.readlines()
        optionFile.close()
        optionFile=open('options.ini','w')
        for i in range(len(optionList)):
            optionList[i]=optionList[i][:optionList[i].index('=')+1]+str(self.options[i])+'\n'
        print optionList
        optionFile.writelines(optionList)
        optionFile.close()
    def changeOption(self):
        """method docstring"""
        # returns 
        pass
    def inputFile(self,filename):
        """method docstring"""
        picture=open(filename,'rb')
        return picture
        pass
    def textRecognition(self):
        """method docstring"""
        # returns 
        pass
    def blockSegmentation(self,BlockFrame):
        """methot docstring"""
        # returns 
        pass
    def characterSegmentation(self,LineFrame):
        """method docstring"""
        # returns 
        pass
    def characterRecognition (self,CharFrame):
        """recognition of one character given as an CharFrame object, returns a string"""
        # returns 
        pass
    def textComposition(self,word):
        """method docstring"""
        # returns 
        pass
		
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
    a=Control()
    a.saveOptions()
