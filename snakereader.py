import sys
sys.path.append(sys.path[0]+'/files')
import wxpython
from control import Control

class commandLine(Control):
    ## obsluga linii komend
    def jakas_metoda(self,commandList):
	## interpretuje liste polecen, tzn zmienia (odpala metody klasy Control) opcje (atrybuty klasy Control), obczaja pliki, itp. itd.
        pass
    def jakas_inna_metoda(self,moze_cos_jeszcze):
	## odpala metode klasy Control ktora odpala reszte modulow
        pass
    pass

class GUI(Control):
    def metoda_zawierajaca_obiekty_okienek(self):
        pass
    def metody_ktore_beda_odpalane_po_przycisnieciu_przyciskow_itp(self):
        pass
    pass

if len(sys.argv)>1:
    ## tworzy obiekt commandLine i odpala jakies jego metody
    pass
else:
    ## tworzy obiekt klasy GUI i na nim
    ## uruchamia caly interface (MainLoop czy cos w tym stylu)
    pass
