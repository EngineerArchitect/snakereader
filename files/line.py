# -*- coding: cp1250 -*-

import picture.py
 
class LineFrame(Frame): #Klasa linijka dziedzicząca po klasie obraz

    def extractCharacters(self): #główna metoda wywołujaca pozostałe
        hHisto = self.hLinesHistogram()
        spaceLength = findSpaceLength(hHisto)
        position = 0
        Line={}
        Word={}
        End = False
        while not end: #dopuki nie doszliśmy do końca linijki wyszukujemy znaków
            Position, char = self.findChar(position, spaceLength)
            if type(char) == str: #sprawdzenie czy nadano komunikat, czy zwrócono obiekt
                if char == Space:
                    Line.append(Word)
                    Word={}
                elif char == Enter:
                    Line.append(Word)
                    return Line
            else: # zwrócono obiekt typu znak
                char.reScale(20,20)
                Word.append(char)

    def findChar(self, position, spaceLength):
        leer=0 # int, licznik pustych kolumn
        Queue=[] #kolejka, bedzie słuzyć do wyszukiwania i przechowywania sąsiadów
        PiksList=[] #lista bedzie zawireała wynikową liste pikseli.
        
        #tu trzeba sie dopytać Grzesia o funkcje zwracające wielkość obiektu
        #tj. wysokości i szerokości i dopisać to niżej
        
        while (position < Length and self.hLineHistogram(position)==0):
            position+=1
            leer+=1
        if position == length: # sprawdamy czy nie mamy przypadkiem do czynienia ze spacja lub enterem
            return position, "Enter"
        elif leer>=spaceLength:
            return position, "Space"
        else:
            for i in range(0, wysokosc-1): #wpisujemy wszystkie piksele z pierwszej czarnej linijki do kolejki
                if self.getPiksel(positon, i)==1: #sprawdzić czy na pewno taka kolejność współżędnych
                    Queue.append((position, i))
                    PiksList.append((position, i))
            while len(Queue)>0:
                Piksel=Queue.pop(0) #krotka zawierająca współrzędne piksela
                neighbourhood=[(Piksel[0]-1, Piksel[1]+1),(Piksel[0]-1, Piksel[1]),(Piksel[0]-1, Piksel[1]-1),(Piksel[0], Piksel[1]+1),(Piksel[0], Piksel[1]-1),(Piksel[0]+1, Piksel[1]+1),(Piksel[0]+1, Piksel[1]),(Piksel[0]+1, Piksel[1]-1)]
                #to co wyzej to lista współrzędnych sąsiadów Piksela
                for neighbour in neighbourhood: #sprawdzamy sąsiedztwo
                    if not(neighbour in PiksList) and self.getPiksel(neighbour[0],neighbour[1])==1:
                        Queue.append(neighbour)
                        PiksList.append(neighbour)
            PiksList.sort() # soruje liste w ten sposób, że najpierw piksele z pierwszej kolumny potem z drugiej itd
            PiksList=self.addHigherPiks(PiksList) #dodajemy wszystkie piksele nad grupą
            

            
#pisze tą metode bo chyba mi sie przyda, a nie ma jej w projekcie.
#ma ona za zadanie dodać do PiksList piksele nad tymi już wybranymi
#na razie zakładam że najwyższy wiersz ma numer 0, dopuki mi Grześ nie odpisze
    def addHigherPiks(PiksList):
        position1,High1=PiksList[0]
        position2,High2=PiksList[len(PiksList)-1]
        for kol in range(position1, position2):
            line=0
            while ((kol, line) in PiksList):
                if self.getPiksel(kol,line):
                    PiksList.append((kol,line))
                line+=1
        PiksList.sort()
        return PiksList
                
                            
def findSpaceLength(Histogram, High): #znajduje długość spacji
    pass



        
