# -*- coding: utf8 -*-
"""Module is controling data flow in program using Control class"""
from blockframe import *
from lineframe import *
from charframe import *
from dictionary import *
from glob import glob

class Control:
        """Control class determines data flow and sets options for inner functions; contains methods that uses other program classes."""
        def __init__(self):
                """Class constructor; assigns atributes: self.options (list of options read from file) and self.dictionaries (list of available dictionaries)."""
                optionFile=open('options.ini','r')
                optionList=optionFile.readlines()
                optionFile.close()
                self.options=[opt[opt.index('=')+1:].strip() for opt in optionList]
                self.dictionaries=[dic[-7:-4] for dic in glob('.\\files\\dict\\*.txt')]
        def saveOptions(self):
                """Saves atribute self.options to options.ini file."""
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
                """Returns binary read picture file."""
                picture=open(filename,'rb')
                return picture
        def textRecognition(self,pic):
                """Main class method; uses methods below to cut picture file to lines and to characters, and to recognize characters."""
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
                """Segmentation of a block of text into list of lines given as LineFrame objects."""
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
                """Segmentation of text line, returns list of lists of CharFrame objects."""
                characters = LineFrame.extractCharacters()
                return characters
        def characterRecognition (self,CharFrame,listOfOptions):
                """Recognition of single character given as an CharFrame object; returns a string."""
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

                '''ListListList=dictionaryObject.tupleListListToListListList(tupleListList)
                word=dictionaryObject.normalize(tupleListList)
                wordpos=dictionaryObject.bestPos(word)

                filenames=[]
                palki=''
                for i in range(wordpos[0],wordpos[1]-1):
                        palki=palki+'_'
                filenames.append(word[wordpos[0]]+palki+word[wordpos[1]])
                #plik=dictionaryObject.loadFiles(filenames)
                plik=filenames[0]
                start=wordpos[0]
                wordpos.remove(wordpos[0])
                wordpos.remove(wordpos[1])

                star=dictionaryObject.createDataStructure(plik)
                permitted=dictionary.permittedWords(star,99-start+wordpos[0],word[wordpos[0]])
                wordpos.remove(wordpos[0])
                while True:
                        if wordpos==[]:
                                break
                        newpermitted=dictionary.permittedWords(star,99-start+wordpos[0],word[wordpos[0]])
                        if newpermitted==[]:
                                break
                        newnewpermitted==[]
                        for i in range(0,len(permitted)):
                                for j in range(0,len(newpermitted)):
                                        if permitted[i]==newpermitted[j]:
                                                newnewpermitted.append(permitted[i])
                        permitted=newnewpermitted
                        if permitted==[]:
                                break
                        wordpos.remove(wordpos[0])
                        
                if wordpos==[]:#jest super
                        while True:
                                slownik=open(filename,'r')
                                a=-1
                                for linijka in slownik:
                                        a+=1
                                        if a==permitted[i]:
                                                if len(word)==len(linijka)-2:
                                                        return linijka[2:]

                if newpermitted==[]:
                        pass#tej literki w ogole nie ma w pliku na tej pozycji
                if permitted==[]:
                        pass#ta literka jest w pliku ale nie pasuje do wczesniej wybranych

##        else:
##            #robi wspaniala strukture drzewiasta
##            word=dictionaryObject.normalize(tupleListList) #normalizuje
##            wordpos=dictionaryObject.bestPos(word) #obliczam pozycje
##            plik=dictionaryObject.loadFiles(wordpos) #wybieram i laduje pliki
##            stars=dictionaryObject.createDataStructure(plik) #tworze SS z pliku
##            #dictionaryObject.StarStruct.has(wordpos)
##            #costam dalej
##            return checkword'''

if __name__ == "__main__":
	a=Control()
	print a.dictionaries
									
