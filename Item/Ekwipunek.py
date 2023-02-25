from Bron import Bron
from Buty import Buty
from Helm import Helm
from Spodnie import Spodnie
from Zbroja import Zbroja
from Bron import Bron




class Ekwipunek:
    def __init__(self, typ, nazwa, waga, lvl, damage = None):
        self.typ = typ
        if self.typ == "Bron":
            Bron(nazwa=nazwa, waga=waga, lvl=lvl, damage=damage)
            self.EkwipunkeTab = [Bron]



    
test = Ekwipunek("Bron","Miecz", 10, 1, 50)
print(test.EkwipunkeTab)