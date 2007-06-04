#-*- coding: utf8 -*-
"""Module docstring"""
class Dictionary :
	"""class docstring"""
	def __init__(self,filename) :
		self.filename = filename 
		pass
	
	def tupleListListToListListList(tupleListList):
		word=[]
		for i in range(0,len(tupleListList)):
			word.append([])
			for j in range(0,len(tupleListList[i])):
				word[i].append([tupleListList[i][j][0],tupleListList[i][j][1]])
		return word
	
	def normalize (self, word) :
		"""method docstring"""
		
		#[[(a,23),(b,11),(c,8)],[(d,69),(e,44),(f,29)],[(g,96),(h,77),(i,63)]]
	
		for i in range(0,len(word)):
			suma=0
			for j in range(0,3):
				suma=suma+word[i][j][1]
			for j in range(0,3):
				word[i][j][1]=100*(word[i][j][1])/suma
		return word
			
	def loadFiles (self, filenames) :
		"""method docstring"""
		filenames
		pass

	def bestPos (normalizedWord) :
		"""method docstring"""
		#zwraca kolejnosc w jakiej literki sa prawdopodobne od najbardziej do najmniej
		poszeregowane=[]
		bestPosy=[]
		for i in range(0,len(normalizedWord)):
			poszeregowane.append(normalizedWord[i][0][1])
		for j in range(0,len(normalizedWord)):
			najlepszy=0
			najlepszymiejsce=0
			for i in range(0,len(normalizedWord)-j):
				if poszeregowane[i]>najlepszy:
					najlepszy=poszeregowane[i]
					najlepszymiejsce=i
			bestPosy.append(i)
			poszeregowane.remove(najlepszy)
		bestPosy.reverse()
		return bestPosy

	def createDataStructure (filename) :
		"""method docstring"""
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

	def permittedWords (struktura,miejsce,litera) :
		"""method docstring"""
		j=-1
		for i in range(0,len(struktura[miejsce])):
			if struktura[miejsce][i][0]==litera:
				j=i
		if j>-1:
                        wyrazy=struktura[miejsce][j][1]
                        wyrazy.sort()
                if j=-1:
                        wyrazy=[]
                return wyrazy

	def has (self, word) :
		"""method docstring"""
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
	pass
