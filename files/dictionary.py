#-*- coding: utf8 -*-
"""Module docstring"""
class Dictionary :
        """class docstring"""
        def __init__(self,filename) :
                self.filename = filename 
                pass
        
        def normalize (self, word) :
                """method docstring"""
                #[[(a,23),(b,11),(c,8)],[(d,69),(e,44),(f,29)],[(g,96),(h,77),(i,63)]]
                for i in range(0,len(word)):
                        suma=0
                        for j in range(0,3):
                                suma=suma+word[i][j][1]
                        for j in range(0,3):
                                word[i][j][1]=trunc(100*(word[i][j][1])/suma)
                        
        def loadFiles (self, filenames) :
                """method docstring"""
                pass
        
        def bestPos (self, normalizedWord) :
                """method docstring"""
                poszeregowane=[]
                for i in range(0,len(normalizedWord)):
                        poszeregowane.append(normalizedWord[i][1][2])
                poszeregowane.sort()
                pass
        
        def createDataStructure (filename) :
                struktura=[]
                """method docstring"""
                slownik=open(filename,'r')
                numerwyrazu=-1
                miejsceostatniego=1
                for linijka in slownik:
                        numerwyrazu+=1
                        if miejsceostatniego==linijka[0]:
                                for i in range(1,len(linijka)):
                                        struktura[i][ord(linijka[i])-97].append(numerwyrazu)
                        else:
                                struktura.insert(0,[ord(linijka[1])][numerwyrazu])
                                for i in range(2,len(linijka)):
                                        struktura[i-1][ord(linijka[i])-97].append(numerwyrazu)
                                
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
