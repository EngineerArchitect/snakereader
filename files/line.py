# -*- coding: cp1250 -*-

import picture.py
import cPickle
 
class LineFrame(Frame): #Klasa linijka dziedzicząca po klasie obraz

    def extractCharacters(self): #główna metoda wywołujaca pozostałe
        hHisto = self.hLinesHistogram()
        spaceLength = findSpaceLength(hHisto)
        position = 0
        Line={}
        Word={}
        End = False
        while not end: #dopuki nie doszliśmy do końca linijki wyszukujemy znaków
            position, char, correction = self.findChar(position, spaceLength+correction)
            if type(char) == str: #sprawdzenie czy nadano komunikat, czy zwrócono obiekt
                if char == Space:
                    Line.append(Word)
                    Word={}
                elif char == Enter:
                    Line.append(Word)
                    return Line
            else: # zwrócono obiekt typu znak
                Word.append(char)

    def findChar(self, position, spaceLength, ): 
        leer=0 # int, licznik pustych kolumn
        Queue=[] #kolejka, bedzie słuzyć do wyszukiwania i przechowywania sąsiadów
        PiksList=[] #lista bedzie zawireała wynikową liste pikseli.
        
        #tu trzeba sie dopytać Grzesia o funkcje zwracające wielkość obiektu
        #tj. wysokości i szerokości i dopisać to niżej
        
        while (position < length and self.hLineHistogram(position,high)==0):
            position+=1
            leer+=1
        if position == length: # sprawdamy czy nie mamy przypadkiem do czynienia ze spacja lub enterem
            return position, "Enter", 0
        elif leer>=spaceLength:
            return position, "Space", 0
        else:
            for i in range(0,High-1): #wpisujemy wszystkie piksele z pierwszej czarnej linijki do kolejki
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
            position1,High1=PiksList[0]
            position2,High2=PiksList[len(PiksList)-1]  # wten sposób uzyskamy numery skrajnych kolumn
            charLength=position2-position1
            
            if charLength<=High: #sprawdzamy czy nie wykryliśmy sklejki dłuższej niż długość kafelki
                newPositon= position+(charLength/2) #nowa pozycja w środku wykrytego znaku by wyeliminować przypadek gdy jeden znak nakryje drugi
                Char=CharFrame() #tworzymy obiekt typu Charframe, ale jeszcze nie wiem jak go wywołać
                
                for el in PiksList: #jeśli nie wymyślimy efektywniejszego sposobu
                    Char.putPiksel(position-el[0],el[1])
                    self.makeWhite(el[0],el[1])
                    
                Char.reScale(20,20)
                return position, Char, charLength/2

            else: #czyli gdy wykryto za długą sklejke
                PiksList, Char = reconChar(Pikslist)
                position1,High1=PiksList[0]
                position2,High2=PiksList[len(PiksList)-1]  # wten sposób uzyskamy numery skrajnych kolumn
                charLength=position2-position1
                newPositon= position+(charLength/2) #nowa pozycja w środku wykrytego znaku by wyeliminować przypadek gdy jeden znak nakryje drugi

                return position, Char, charLength/2

            
#pisze tą metode bo chyba mi sie przyda, a nie ma jej w projekcie.
#ma ona za zadanie dodać do PiksList piksele nad tymi już wybranymi
#na razie zakładam że najwyższy wiersz ma numer 0, dopuki mi Grześ nie odpisze

    def addHigherPiks(PiksList):
        position1,High1=PiksList[0]
        position2,High2=PiksList[len(PiksList)-1]
        for kol in range(position1, position2): #dla każedj kolumnt sprawdzamy piksele nad znalezionymi
            line=0
            while ((kol, line) in PiksList):
                if self.getPiksel(kol,line): #jeżeli czarne, to dodajemy je do listy
                    PiksList.append((kol,line))
                line+=1
        PiksList.sort()# na koniec sortujemy liste ponownie by miała taki sam format jak na wejsciu, przyda sie to zaraz w findChar
        return PiksList

#######################################################################################################################

def reconChar(PiksList, high):
    position, h=PiksList[0]
    for piks in PiksList: #usówamy wszystkie piksele które nie mieszczą sie w kafelce
        if piks[0]>=position+high-1:
            PiksList.remove(piks)
            
    Char=CharFrame() #tworzymy obiekt typu Charframe, ale jeszcze nie wiem jak go wywołać      
    for el in PiksList: #jeśli nie wymyślimy efektywniejszego sposobu
        Char.putPiksel(position-el[0],el[1])

    CharScaled=copy.deepcopy(Char)    
    CharScaled.reScale(20,20)
    if CharScaled.getOutput():
        return PiksList, CharScaled
    else:
        prop=[[],[],[]]
        histo=Char.hLinesHistogram()
        for i in range(0, len(histo):
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
        return PiksList, Char # gdyby to nić nie dało by zwrócić cokolwiek
                
                            
def findSpaceLength(Histogram, High): #znajduje długość spacji
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
    return summ/number      
