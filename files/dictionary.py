#-*- coding: utf8 -*-
"""Module is verifying neural network output with supported dictionary."""
class Dictionary :
	"""Overall class which is controlling dictionary and might be extended in any possible way in case of implementating other methods of veryfying word with dictionary."""
#	def __init__(self):#,filename) :
#               self.filename = filename 
#		pass
	
	def tupleListListToListListList(self,tupleListList):
		"""Simple method converting tuple list list to list list list."""
		word=[]
		for i in range(0,len(tupleListList)):
			word.append([])
			for j in range(0,len(tupleListList[i])):
				word[i].append([tupleListList[i][j][0],tupleListList[i][j][1]])
		return word
	
	def normalize (self, word) :
		"""It takes probabilities of every letter in one place and normalizes their value, so it is very easy to direct point at the letter which has the most probability of beign correctly indicated."""
		#[[(a,23),(b,11),(c,8)],[(d,69),(e,44),(f,29)],[(g,96),(h,77),(i,63)]]
		for i in range(0,len(word)):
			suma=0
			for j in range(0,3):
				suma=suma+word[i][j][1]
			for j in range(0,3):
				word[i][j][1]=100*(word[i][j][1])/suma
		return word
			
	def loadFiles (self, filenames) :
		"""This method loads necessary files so they will be faster used in the rest of the program. (not implemented yet)"""
		filenames
		pass

	def bestPos (self, normalizedWord) :
		"""Uses normalized values and directly points at the most and the least likelihood letters in word given in input. It returns order from the most to the least probability."""
		#zwraca kolejnosc w jakiej literki sa prawdopodobne od najbardziej do najmniej
		najlepsze=[]
		for i in range(0,len(normalizedWord)):
			najlepsze.append((normalizedWord[i][0][1],i))
		tylkonajlepsze=[]
		for i in range (0,len(najlepsze)):
			tylkonajlepsze.append(najlepsze[i][0])
		tylkonajlepsze.sort()
		bestPosy=[]
		for i in range(0,len(tylkonajlepsze)):
			for j in range(0,len(najlepsze)):
				if najlepsze[j][0]==tylkonajlepsze[i]:
					bestPosy.append(j)
		bestPosy.reverse()
		return bestPosy

	def createDataStructure (self, filename) :
		"""The most important method in dictionary module. Creates the star structure, which is tuple list tuple list. Bounded by maximal length of 99 letters in word (as the dictionary does) allows to take any letters and check if a word exist in the dictionary. It creates the star structure reading whole file and writes down in lists numbers of appearance every word in lines."""
		struktura=([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
		slownik=open(filename,'r')
		a=-1
		for linijka in slownik:
			a+=1
			start=99-int(linijka[0])*10-int(linijka[1])
			for i in range(0,len(linijka)-3):
				jest=0
				for j in range(0,len(struktura[start+i])):
					if struktura[start+i][j][0]==linijka[i+2]:
						struktura[start+i][j][1].append(a)
						jest=1
				if jest==0:
					struktura[start+i].append((linijka[i+2],[a]))
					jest=0
		slownik.close()
		return struktura

	def permittedWords (self,star,place,letter) :
		"""It uses the star structure and checks if at specified place is a specified letter permitted to be (if with the two most possible letters this letter can exist in the dictionary."""
		j=-1
		for i in range(0,len(star[place])):
			if star[place][i][0]==letter:
				j=i
		if j>-1:
			wyrazy=star[place][j][1]
			wyrazy.sort()
		if j==-1:
			wyrazy=[]
		return wyrazy

	def has (self, word) :
		"""Checks if the word exists in the star structure. (not implemented yet)"""
		pass

##class StarStruct :
##        """class docstring"""
##        def __init__(self) :
##                pass
##        
##        def get (self) :
##                """method docstring"""
##                pass
##
##        def has (self, word) :
##                """method docstring"""
##                pass
##
##        def size (self) :
##                """method docstring"""
##                pass
##
##class UniversalDictStruct : #w ogole nie wiem jak to zrobic ;f w ogole nie wiem czy to potrzebne tak na prawde
##        """class docstring"""
##        def __init__(self,data) :
##                self.data=data
##                self.children=[]
##
##        def insert (self, word) :
##                """method docstring"""
##                for i in range(1,len(word)):
##                        self.children.append(word[i])
##                
##        def has (self, word) :
##                """method docstring"""
##                pass

if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
	#you can use this section to test your module

	tupleListList=[
		[('s',93),('b',71),('c',68)],
		[('p',69),('a',44),('f',29)],
		[('a',96),('g',77),('i',55)],
		[('g',99),('a',16),('j',10)],
		[('h',99),('e',13),('a',11)],
		[('e',88),('l',74),('b',71)],
		[('t',88),('l',74),('j',63)],
		[('t',41),('h',33),('l',16)],
		[('i',59),('h',43),('i',16)]
		]
		
	dictionaryObject=Dictionary()
	
	ListListList=dictionaryObject.tupleListListToListListList(tupleListList)
#	tupleListList=[[['-',23],['b',11],['c',8]],[['p',69],['e',44],['f',29]],[['g',96],['h',77],['i',63]]]        
	word=dictionaryObject.normalize(ListListList)
	print word
	wordpos=dictionaryObject.bestPos(word)
	
	filenames=[]
	palki=''
	for i in range(wordpos[0],wordpos[1]-1):
		palki=palki+'_'
	if wordpos[0]<wordpos[1]:
		print word[wordpos[0]][0][0]+palki+word[wordpos[1]][0][0]
		filenames.append("dict/slo/"+word[wordpos[0]][0][0]+palki+word[wordpos[1]][0][0]+".txt")
	else:
		print word[wordpos[1]][0][0]+palki+word[wordpos[0]][0][0]
		filenames.append("dict/slo/"+word[wordpos[1]][0][0]+palki+word[wordpos[0]][0][0]+".txt")
	#plik=dictionaryObject.loadFiles(filenames)
	plik=filenames[0]
	print "wordpos: "
	print wordpos	

	star=dictionaryObject.createDataStructure(plik)
	if wordpos[0]<wordpos[1]:
		permitted=dictionaryObject.permittedWords(star,99,word[wordpos[0]][0][0])
		start=wordpos[0]
	else:
		permitted=dictionaryObject.permittedWords(star,99,word[wordpos[1]][0][0])
		start=wordpos[1]
	wordpos.remove(wordpos[0])
	wordpos.remove(wordpos[0])
	print "slownik wczytany, elo"

	wyraz=''

	while wordpos<>[]:
		print "wordpos: "
		print wordpos
		print "permitted: "
		print permitted
		newpermitted=[]
		for i in range(0,3):
			if newpermitted<>[]:
				break			
			for j in range(0,len(star[99-start+wordpos[0]])):
				if word[wordpos[0]][i][0]==star[99-start+wordpos[0]][j][0]:
					newpermitted=dictionaryObject.permittedWords(star,99-start+wordpos[0],word[wordpos[0]][0][0])
					print "newpermitted: "
					print newpermitted
					break
				
		if newpermitted==[]:
			print "wszystkich trzech nie ma w strukturze"
			wordpos.remove(wordpos[0])
			
		elif len(newpermitted)==1:
			print "jest jedno słowo z tą literką w pliku na tym miejscu (super)"
			slownik=open(plik,'r')
			a=-1
			for linijka in slownik:
				a+=1
				if a==newpermitted[0]:
					print linijka[2:]
					wyraz=linijka[2:]
					wordpos=[]
		else:
			print "jest kilka propozycji"
			newnewpermitted=[]
			for i in range(0,len(permitted)):
				for j in range(0,len(newpermitted)):
					if permitted[i]==newpermitted[j]:
						newnewpermitted.append(permitted[i])
			if newnewpermitted==[]:
				print "ta literka jest w pliku ale nie pasuje do wczesniej wybranych"
				wordpos.remove(wordpos[0])

			elif len(newnewpermitted)==1:
				print "jest jedno słowo z tą literką w pliku na tym miejscu (super) 2"
				slownik=open(plik,'r')
				a=-1
				for linijka in slownik:
					a+=1
					if a==newnewpermitted[0]:
						print linijka[2:]
						wyraz=linijka[2:]
						wordpos=[]
						
			else:
				print "normalka"
				permitted=newnewpermitted
				wordpos.remove(wordpos[0])
