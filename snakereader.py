import sys
sys.path.append(sys.path[0]+'/files')
import wxpython
from control import Control

class commandLine(Control):
    ## obsluga linii komend
    def __init__(self,commandList):
	## interpretuje liste polecen, tzn zmienia (odpala metody klasy Control) opcje (atrybuty klasy Control), obczaja pliki, itp. itd.
        pass
    def jakas_metoda(self,moze_cos_jeszcze):
	## odpala po kolei metody klasy Control
        pass
    pass

class GUI(Control):
    def __init__(self):
        ## uruchamia caly interface (MainLoop czy cos w tym stylu)
        pass
    def metoda_zawierajaca_obiekty_okienek(self):
        pass
    def metody_ktore_beda_odpalane_po_przycisnieciu_przyciskow_itp():
        pass
    pass

if len(sys.argv)>1:
    ## tworzy obiekt commandLine i odpala jakas jego metode
    pass
else:
    ## tworzy obiekt klasy GUI
    pass
