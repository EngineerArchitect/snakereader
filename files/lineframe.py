# -*- coding: utf8 -*-
"""Module for segmentation of single characters from line of text. Use Frame class, as a base, and adds methods for segmentation"""

import copy
from PIL import Image, ImageEnhance
from frame import Frame
from charframe import CharFrame
from neuralnetwork import NeuralNetwork


class LineFrame(Frame) :
    """The same class like Frame, but adds methods for segmentation of single character from line of text"""
    def __init__(self,f=None,new=False) :
        """Create LineFrame object. If new is False create new empty object, if new is True create obcject from file f"""
        if new:
            self.matrix=Image.new('1',(1,1))
        else:
            self.matrix=Image.open(f)

    def extractCharacters(self):
        """Steering method for character segmentation. Extract all single characters from line of text (LineFrame object).
        Returns list of lists of CharFrame objets, where each CharFrame object is in size of 30x30 and contain single character.
        Ineer list correspond to single word in text"""
        
        length, high=self.getSize() ##geting size of LineFrame object - high and length
        vHisto = self.vLinesHistogram()
        spaceLength = findSpaceLength(vHisto,high) ##finding of expected length of Space in line
        position = 0 ##position, from where findChar is serching for character
        Line=[] ##list of words in line
        Word=[] ##list of characters in word
        correction=0
        End = False
        while not End: ##while not End of the line, search for characters
            position, char, correction = self.findChar(position, spaceLength+correction)
            if type(char) == str: #check if returned CharFrame object or repor
                if char == "Space": #Space was finded in line, end of word, Word list append to Line list, and new Word list started
                    Line.append(Word)
                    Word=[]
                elif char == "Enter": ##Finden end of line, Wor list closed and appened to Line list, end of method, returned Line list
                    Line.append(Word)
                    for i in range(0,len(Line)):
                        for j in range(0, len(Line[i])):
                            Line[i][j].savePicture(str(i)+"kafel"+str(j)+".bmp","BMP")
                    return Line
            else: ## Character finden in line, append CharFrame object to Word list
                Word.append(char)
                

    def findChar(self, position, spaceLength ):
        """Method find first single character in text starting from given position, finds Spaces too.
        Returns CharFrame object in size of 30x30 which contain single character, and position, where it end to search."""
        leer=0 ## numeator of empty column
        Queue=[] ##this will help in serching for neighbours of pixels
        PiksList=[] ##list of balck piksels, of with consist the charakter
        length, high = self.getSize()
 
        while (position < length and self.vLineHistogram(position)==0): #serching for a first not empty line, for given position
            position+=1
            leer+=1
        if position == length: ## check if it is Space or it is End of line
            return position, "Enter", 0
        elif leer>=spaceLength:
            return position, "Space", 0
        else:
            for i in range(0,high): ##extracting all black pixels from this line
                if self.getPixel(position, i)==0:
                    Queue.append((position, i))
                    PiksList.append((position, i))

            while len(Queue)>0:
                Piksel=Queue.pop(0) ##geting firs element from Queue
                neighbourhood=[(Piksel[0]-1, Piksel[1]+1),(Piksel[0]-1, Piksel[1]),(Piksel[0]-1, Piksel[1]-1),(Piksel[0], Piksel[1]+1),(Piksel[0], Piksel[1]-1),(Piksel[0]+1, Piksel[1]+1),(Piksel[0]+1, Piksel[1]),(Piksel[0]+1, Piksel[1]-1)]
                ##to co wyzej to lista współrzędnych sąsiadów Piksela

                for neighbour in neighbourhood: ##cheking neighbourhood of each pixel
                    if not(neighbour in PiksList) and (neighbour[0] in range(0,length)) and (neighbour[1] in range(0,high)) and self.getPixel(neighbour[0],neighbour[1])==0:
                        Queue.append(neighbour)
                        PiksList.append(neighbour)
            
            PiksList.sort() ##sorts list with number of column

            
            PiksList=self.addHigherPiks(PiksList) ##adds all piksel over finden pixels
            PiksList.sort()
            position1,High1=PiksList[0]
            position2,High2=PiksList[len(PiksList)-1]  ## geting number of smalest and biggest column in group
            charLength=position2-position1
            if len(PiksList)>5: ##checkin if there are more then 5 piksels in group to eliminate case, when there are single pixels not eliminated by initial fomating
                if charLength<high: ##check if the length of finden group of pixels isn't bigger then length of tile
                    newPosition= position1+(charLength/2) ##new position in the center of finden char to eliminate case, when one char is over the second
                    Char=CharFrame(high,high) ##create new CrarFrame object
    
                    for el in PiksList: ##making all pixels in PiksList black in ChatFrame object and white in self(LineFrame object)
                        Char.putPixel(el[0]-position1,el[1])
                        self.makeWhite(el[0],el[1])
                            
                    Char.reScale(30,30) #scaling CharFrame to the ening size
                    
                    return newPosition, Char, charLength/2

                else: ##length of goup of pixels is too big
                    PiksList, Char = reconChar(PiksList,high) ## finding where to divide group of pixels
                    for Piks in PiksList:
                        self.makeWhite(Piks[0],Piks[1])
                    position1,High1=PiksList[0]
                    position2,High2=PiksList[len(PiksList)-1]  ## geting number of smalest and biggest column in group
                    charLength=position2-position1
                    newPosition= position1+(charLength/2) ##new position in the center of finden char to eliminate case, when one char is over the second
                    return newPosition, Char, charLength/2
            else: ##if there is less then 5 pixels in group
                for el in PiksList: ##making all pixels in PiksList white in self(LineFrame object)
                        self.makeWhite(el[0],el[1])
                newPosition= position1+(charLength/2)
                return newPosition, "None", charLength/2

    def addHigherPiks(self, PiksList):
        """Add all pixels over already segmented character, this adds dots to character"""
        position1,High1=PiksList[0]
        position2,High2=PiksList[len(PiksList)-1]
        for kol in range(position1, position2): ##for each column checking all pixels over finden group
            line=0
            while not((kol, line) in PiksList):
                if self.getPixel(kol,line)==0: ##if they are black add them to PiksList
                    PiksList.append((kol,line))
                line+=1
        PiksList.sort()## at the end sort the PiksList with number of column
        return PiksList

######################################################################################################################

def reconChar(PiksList, high):
    """If segmented character is too long, ask NeuralNetwork where to divide it"""
    position, h=PiksList[0]
    NewPiksList=[]
    
    for piks in PiksList: ##delete all pixels that can not be in tile
        if piks[0]<position+high-1:
            NewPiksList.append(piks)
            
    PiksList=NewPiksList
    
    Char=CharFrame(high,high) ##create new CharFrame object       
    for el in PiksList: 
        Char.putPixel(el[0]-position,el[1])
    CharScaled=Char
    CharScaled.reScale(30,30) ##skale CharFrame object to the ending size
    return PiksList, CharScaled
    ##this is not testet yet because of not working neuralNetwork
    """if CharScaled.getOutput():
        return PiksList, CharScaled
    else:
        prop=[[],[],[]]
        histo=Char.vLinesHistogram()
        for i in range(0, len(histo)):
            if histo[i]<=3:
                prop[histo[i]-1].append(i)
        for proposition in prop:
            proposition.reverse()
            CharPro=copy.deepcopy(Char)
            PiksListPro=copy.deepcopy(PiksList)
            for kolumn in proposition:
                for el in PiksList: #jeśli nie wymyślimy efektywniejszego sposobu
                    if el[1]>=proposition:
                        CharPro.makeWhite(position-el[0],el[1])
                        PiksListPro.remove(el)
                CharProScaled=copy.deepcopy(CharPro)
                CharProScaled.reScale(20,20)
                if CharProScaled.getOutput():
                    return PiksListPro, CharProSlaled
        return PiksList, Char # gdyby to nić nie dało by zwrócić cokolwiek"""

def findSpaceLength(Histogram, High): 
    """function search expected length of space in line, based on empty columns in histogram, its a simple arithmetic mean of length of empty space"""
    summ=0
    length=0
    number=0
    for kol in Histogram:
        if kol==0:
            length+=1
        elif kol>0 and length>0:
            if length<High:
                summ+=length
                length=0
                number+=1
            else:length=0
    if number<>0:    return max(summ/number, (1/5)*High) ## in a case if there is no space in line
    else: return (1/5)*High
    
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
	#you can use this section to test your module

	f=open("line1.bmp","rb")
	Image=LineFrame(f)
	Image.blackWhite()
	kafels=Image.extractCharacters()
	for i in range(0,len(kafels)):
            for j in range(0, len(kafels[i])):
                kafels[i][j].savePicture(str(i)+"kafel"+str(j)+".bmp","BMP")
       # im=LineFrame(new=True)
        #im.showPicture()

