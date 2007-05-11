# -*- coding: utf8 -*-
"""Module docstring"""
from blockframe import *
from lineframe import *
from charframe import *
from dictionary import *
class Control:
    def __init__(self): # jeszcze bez szukania slownikow
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
    def inputFile(self,filename):
        """method docstring"""
        picture=open(filename,'rb')
        return picture
        pass
    def textRecognition(self,pic): # jeszcze bez wyjatkow
        """method docstring"""
        text=""
        # try?
        mainList=self.blockSegmentation(pic,[self.options[0],self.options[1]])
        # except?
        for line in mainList:
            mainList[mainList.index(line)]=self.characterSegmentation(line,[])
            for word in line:
                wordRead=[]
                for char in word:
                    wordRead.append(self.characterRecognition(char,[]))
                text+=self.textComposition(wordRead,[self.options[2]])+' '
            text+='\n'
        return text
    def blockSegmentation(self,BlockFrame,listOfOptions):
        """methot docstring"""
        # returns 
        pass
    def characterSegmentation(self,LineFrame,listOfOptions):
        """method docstring"""
        # returns 
        pass
    def characterRecognition (self,CharFrame,listOfOptions):
        """recognition of one character given as an CharFrame object, returns a string"""
        # returns 
        pass
    def textComposition(self,tupleList,listOfOptions):
        """method docstring"""
        # returns 
        pass
		
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
    a=Control()
    a.saveOptions()
