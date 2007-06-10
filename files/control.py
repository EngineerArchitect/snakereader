# -*- coding: utf8 -*-
"""Module is controling data flow in program using Control class. It is separated from Interface module for making it more universal and evolutionable."""
from blockframe import *
from lineframe import *
from charframe import *
from dictionary import *
from neuralnetwork import *
from glob import glob

class Control:
        """Control class determines data flow and sets options for inner functions; contains methods that uses other program classes.
        There's no instance of this class in program. Instead of that, it is inheritated to GUI and CommandLine classes in Interface module."""
        def __init__(self):
                """Class constructor; assigns atributes: self.options (list of options read from file) and self.dictionaries (list of available dictionaries)."""
                optionFile=open('options.ini','r')
                optionList=optionFile.readlines()
                optionFile.close()
                self.options=[opt[opt.index('=')+1:].strip() for opt in optionList]
                self.dictionaries=[dic[-7:-4] for dic in glob('.\\files\\dict\\*.txt')]+["None"]
        def saveOptions(self):
                """Saves atribute self.options to options.ini file."""
                optionFile=open('options.ini','r')
                optionList=optionFile.readlines()
                optionFile.close()
                optionFile=open('options.ini','w')
                for i in range(len(optionList)):
                        optionList[i]=optionList[i][:optionList[i].index('=')+1]+str(self.options[i])+'\n'
                optionFile.writelines(optionList)
                optionFile.close()
        def inputFile(self,filename):
                """Returns binary read picture file."""
                picture=open(filename,'rb')
                return picture
        def textRecognition(self,pic):
                """Main class method; uses methods below to cut picture file to lines and to characters, and to recognize characters; also composites whole text after recognition."""
                text=""
                mainList=self.blockSegmentation(pic,[self.options[1],self.options[2],self.options[3]])
                dictionaryObject=Dictionary(self.options[0])
                for line in mainList:
                        for word in self.characterSegmentation(line,[]):
                                wordRead=[]
                                for char in word:
                                        wordRead.append(self.characterRecognition(char,[]))
                                text+=self.textComposition(wordRead,dictionaryObject)+' '
                        text+='\n'
                return text
        def blockSegmentation(self,picture,listOfOptions=[]):
                """Segmentation of a block of text into list of lines given as instance of LineFrame class."""
                block=BlockFrame(picture)
                if listOfOptions[2]=='poor':
                
                        block.blackWhite('poor')
                        block.clear('poor')
                else:
                        block.blackWhite()
                        block.clear()
                        
                lines=block.extractLines()
                return lines
        def characterSegmentation(self,LineFrame,listOfOptions):
                """Segmentation of text line, returns list of lists of instances of CharFrame class. Elements of outer list are words, which are lists of charakters."""
                characters = LineFrame.extractCharacters()
                return characters
        def characterRecognition (self,CharFrame,listOfOptions):
                """Recognition of single character using implementation of neural network. Returns list of tuples, where single tuple is a pair: a letter and probability of it's appearance."""
                return [('a',23),('b',11),('c',8)]
        def textComposition(self,tupleListList,dictionaryObject):
                """Searches for a recognized word in a dictionary and returns a word which suits the recognized one most, or optionally composes one from letters with biggest probability of appearance"""
                checkword=''
#        [[(a,23),(b,11),(c,8)],[(d,69),(e,44),(f,29)],[(g,96),(h,77),(i,63)]]
		
		#buduje slowo z najlepszych i sprawdza je'''
                for i in range(0,len(tupleListList)):
                        checkword=checkword+tupleListList[i][0][0]
##        if dictionaryObject.UniversalDictStruct.has(checkword)==True:
                return checkword



if __name__ == "__main__":
	a=Control()
	print a.dictionaries
									
