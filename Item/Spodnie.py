from Item.ItemPodstawa import ItemPodstawa


class Spodnie(ItemPodstawa):
    def __init__(self, nazwa, waga, lvl, obrona, szybkosc):
        super().__init__(nazwa, waga, lvl)
        self.nazwa = nazwa
        self.waga = waga
        self.lvl = lvl
        self.obrona = obrona
        self.szybkosc = szybkosc



#test = Spodnie("Skorzane", 25, 1, 20, -5 )
#print(test.nazwa, test.waga, test.szybkosc)