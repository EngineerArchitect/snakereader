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
        # PAWEL!!!!! usedDictionary=          tworzenie obiektu klasy Dictionary na wybranym slowniku (czyli self.options[0])
        usedDictionary=""
##        import pdb
##        pdb.set_trace()
        for line in mainList:
            for word in self.characterSegmentation(line,[]):
                wordRead=[]
                for char in word:
                    wordRead.append(self.characterRecognition(char,[]))
                text+=self.textComposition(wordRead,usedDictionary)+' '
            text+='\n'
        return text
    def blockSegmentation(self,picture,listOfOptions):
        """methot docstring"""
        # picture to obrazek wczytany binarnie do zmiennej
        # listOfOptions to lista opcji, narazie to [wielkosc czcionki, rozdzielczosc skanu]
        # ta metoda zwraca liste linijek w postaci obiektow LineFrame
        pass
    def characterSegmentation(self,LineFrame,listOfOptions):
        """method docstring"""
        # zwracasz liste list obiektow CharFrame
        pass
    def characterRecognition (self,CharFrame,listOfOptions):
        """recognition of one character given as an CharFrame object, returns a string"""
        # zwracasz liste krotek postaci (litera,prawdopodobienstwo)
        pass
    def textComposition(self,tupleListList,dictionaryObject):
        """method docstring"""
        # na poczatku metody textRecognition stworz sobie obiekt klasy Dictionary
        # zeby pozniej, w tej metodzie (ktora ma jako argument ten wlasnie obiekt - dictionaryObject)
        # z niego korzystac a nie za kazdym razem tworzyc nowy obiekt
        # ta metoda na wejsciu ma liste list ktorek, a zwraca slowo		
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
    a=Control()
    a.saveOptions()
