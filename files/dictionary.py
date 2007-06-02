#-*- coding: utf8 -*-
"""Module docstring"""
class Dictionary :
        """class docstring"""
        def __init__(self,filename) :
                self.filename = filename 
                pass
        
        def normalize (self, word) :
                """method docstring"""
                #potrzebuje listy listy list a nie listy listy krotek!
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
                struktura=[]
                slownik=open(filename,'r')
                numerwyrazu=-1
                miejsceostatniego=0
                for linijka in slownik:
                        numerwyrazu+=1
                        if miejsceostatniego==linijka[0]:
                                for i in range(1,len(linijka)):
                                        struktura[i][ord(linijka[i])-97].append(numerwyrazu)
                        else:
                                for j in range(miejsceostatniego,linijka[0]):
                                        struktura.insert(0,[ord(linijka[1])][numerwyrazu])
                                for i in range(1,len(linijka)):
                                        struktura[i][ord(linijka[i])-97].append(numerwyrazu)
                slownik=close(filename)
                return struktura

                                
        def has (self, word) :
                """method docstring"""
                pass

class StarStruct :
        """class docstring"""
        def __init__(self) :
                pass
        
        def get (self) :
                """method docstring"""
                pass

        def has (self, word) :
                """method docstring"""
                pass

        def size (self) :
                """method docstring"""
                pass

class UniversalDictStruct : #w ogole nie wiem jak to zrobic ;f w ogole nie wiem czy to potrzebne tak na prawde
        """class docstring"""
        def __init__(self,data) :
                self.data=data
                self.children=[]

        def insert (self, word) :
                """method docstring"""
                for i in range(1,len(word)):
                        self.children.append(word[i])
                
        def has (self, word) :
                """method docstring"""
                pass

if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
        #you can use this section to test your module
        pass
