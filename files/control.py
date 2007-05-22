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
        self.options=[opt[opt.index('=')+1:].strip() for opt in optionList]
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
    def textRecognition(self,pic): # jeszcze bez wyjatkow
        """method docstring"""
        text=""
        # try?
        mainList=self.blockSegmentation(pic,[self.options[1],self.options[2]])
        # except?
        dictionaryObject=Dictionary(self.options[0])
##        import pdb
##        pdb.set_trace()
        for line in mainList:
            for word in self.characterSegmentation(line,[]):
                wordRead=[]
                for char in word:
                    wordRead.append(self.characterRecognition(char,[]))
                text+=self.textComposition(wordRead,dictionaryObject)+' '
            text+='\n'
        return text
    def blockSegmentation(self,picture,listOfOptions=[]):
        """segmentation of a block of text into list of lines given as LineFrame objects"""
        block=BlockFrame(picture)
        block.blackWhite()
        block.clear()
        lines=block.extractLines()
        return lines
    def characterSegmentation(self,LineFrame,listOfOptions):
        """segmentation of text line, returns list of lists of CharFrame objects """
        characters = LineFrame.extractCharacters()
        return characters
    def characterRecognition (self,CharFrame,listOfOptions):
        """recognition of one character given as an CharFrame object, returns a string"""
        # zwracasz liste krotek postaci (litera,prawdopodobienstwo)
        return [('a',23),('b',11),('c',8)]
    def textComposition(self,tupleListList,dictionaryObject):
        """method docstring"""
        checkword=''
#        [[(a,23),(b,11),(c,8)],[(d,69),(e,44),(f,29)],[(g,96),(h,77),(i,63)]]
        #buduje slowo z najlepszych i sprawdza je
        for i in range(0,len(tupleListList)):
            checkword=checkword+tupleListList[i][0][0]
##        if dictionaryObject.UniversalDictStruct.has(checkword)==True:
        return checkword
##        else:
##            #robi wspaniala strukture drzewiasta
##            word=dictionaryObject.normalize(tupleListList) #normalizuje
##            wordpos=dictionaryObject.bestPos(word) #obliczam pozycje
##            plik=dictionaryObject.loadFiles(wordpos) #wybieram i laduje pliki
##            stars=dictionaryObject.createDataStructure(plik) #tworze SS z pliku
##            #dictionaryObject.StarStruct.has(wordpos)
##            #costam dalej
##            return checkword

if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
    a=Control()
##    a.saveOptions()
    pict=a.inputFile('200digram2.jpg')
    a.blockSegmentation(pict)
