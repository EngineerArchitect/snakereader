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
        leer=0
        dlugo=0
        #tu trzeba sie dopytać Grzesia o funkcje zwracające wielkość obiektu
        #tj. wysokości i szerokości i dopisać to niżej
        while (position < dlugo and self.hLineHistogram(position)==0):
            position+=1
            leer+=1
        if position == dlugosclini: # sprawdamy czy nie mamy przypadkiem do czynienia ze spacja lub enterem
            return position, "Enter"
        elif leer>=spaceLength:
            return position, "Space"
        else:
            pass

def findSpaceLength(Histogram): #znajduje długość spacji
    pass


        
