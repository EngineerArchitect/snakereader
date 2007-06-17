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
		dictionaryObject=Dictionary()
		for line in mainList:
			for word in self.characterSegmentation(line,[]):
				wordRead=[]
				for char in word:
					wordRead.append(self.characterRecognition(char,[int(self.options[4]),self.options[5]]))
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
		listOfInputs=[]
		for i1 in CharFrame.vLinesHistogram():
		    listOfInputs.append(i1)
		for i1 in CharFrame.hLinesHistogram():
		    listOfInputs.append(i1)
##                for i1 in range(30):
##                    for i2 in range(30):
##                        listOfInputs.append((float(CharFrame.getPixel(i1,i2)==255))/2.0)
		neur=NeuralNetwork(60,100,60,[(n,n) for n in range(0,5)])
		neur.loadFactors('learnHistogramXX.bin')
		outputList=neur.getOutput(array(listOfInputs))
		result=[]
		stringi='aąbcćdeęfghijklłmnńoóprtsśtuvwxyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUVWXYZŹŻ'
		charList=list(stringi)+['_' for i in range(100)]
		for i in range(len(outputList)):
		    result.append((outputList[i],charList[i]))
		result.sort()
		result.reverse()
		print result #uncomment this line to see the recognition process
		return [(a[1],a[0]) for a in result]
	def textComposition(self,tupleListList,dictionaryObject):
		"""Searches for a recognized word in a dictionary and returns a word which suits the recognized one most, or optionally composes one from letters with biggest probability of appearance"""
		checkword=''
		for i in range(0,len(tupleListList)):
			checkword=checkword+tupleListList[i][0][0]
		return checkword
		ListListList=dictionaryObject.tupleListListToListListList(tupleListList)
		word=dictionaryObject.normalize(ListListList)
		wordpos=dictionaryObject.bestPos(word)
		filenames=[]
		
		palki=''
		for i in range(wordpos[0],wordpos[1]-1):
			palki=palki+'_'
		if forbidden(word,wordpos,palki)==True:
			wordpos.remove(wordpos[1])
			palki=''
			for i in range(wordpos[0],wordpos[1]-1):
				palki=palki+'_'
			if forbidden(word,wordpos,palki)==True:
				wordpos.remove(wordpos[1])
				palki=''
				for i in range(wordpos[0],wordpos[1]-1):
					palki=palki+'_'

		if wordpos[0]<wordpos[1]:
			filenames.append("dict/slo/"+word[wordpos[0]][0][0]+palki+word[wordpos[1]][0][0]+".txt")
		else:
			filenames.append("dict/slo/"+word[wordpos[1]][0][0]+palki+word[wordpos[0]][0][0]+".txt")
			plik=filenames[0]

		star=dictionaryObject.createDataStructure(plik)
		if wordpos[0]<wordpos[1]:
			permitted=dictionaryObject.permittedWords(star,99,word[wordpos[0]][0][0])
			start=wordpos[0]
		else:
			permitted=dictionaryObject.permittedWords(star,99,word[wordpos[1]][0][0])
			start=wordpos[1]
		wordpos.remove(wordpos[0])
		wordpos.remove(wordpos[0])
	
		wyraz=''
		while wordpos<>[]:
			newpermitted=[]
			for i in range(0,3):
				if newpermitted<>[]:
					break			
				for j in range(0,len(star[99-start+wordpos[0]])):
					if word[wordpos[0]][i][0]==star[99-start+wordpos[0]][j][0]:
						newpermitted=dictionaryObject.permittedWords(star,99-start+wordpos[0],word[wordpos[0]][0][0])
						break
					
			if newpermitted==[]:
				#print "wszystkich trzech nie ma w strukturze"
				wordpos.remove(wordpos[0])
				
			elif len(newpermitted)==1:
				#print "jest jedno słowo z tą literką w pliku na tym miejscu (super)"
				slownik=open(plik,'r')
				a=-1
				for linijka in slownik:
					a+=1
					if a==newpermitted[0]:
						wyraz=linijka[2:]
						wordpos=[]
			else:
				#print "jest kilka propozycji"
				newnewpermitted=[]
				for i in range(0,len(permitted)):
					for j in range(0,len(newpermitted)):
						if permitted[i]==newpermitted[j]:
							newnewpermitted.append(permitted[i])
				if newnewpermitted==[]:
					#print "ta literka jest w pliku ale nie pasuje do wczesniej wybranych"
					wordpos.remove(wordpos[0])
	
				elif len(newnewpermitted)==1:
					#print "jest jedno słowo z tą literką w pliku na tym miejscu (super) 2"
					slownik=open(plik,'r')
					a=-1
					for linijka in slownik:
						a+=1
						if a==newnewpermitted[0]:
							wyraz=linijka[2:]
							wordpos=[]
						
				else:
					#print "normalka"
					permitted=newnewpermitted
					wordpos.remove(wordpos[0])
		if len(permitted)>1:
                        i=-1
                        for linijka in slownik:
                                i+=1
                                for j in range(0,len(permitted)):
                                        if i==permitted[j]:
                                                if len(word)==len(linijka)-2:
                                                        wyraz=linijka[2:]
                                                        break
                if wyraz=='' and len(permitted)>1:
                        i=-1
                        for linijka in slownik:
                                i+=1
                                if i==permitted[0]:
                                        wyraz=linijka[2:]
                                        
                return wyraz


if __name__ == "__main__":
	a=Control()
	print a.dictionaries
									
