from Item.ItemPodstawa import ItemPodstawa


class Zbroja(ItemPodstawa):
    def __init__(self, nazwa, waga, lvl, obrona, szybkosc):
        super().__init__(nazwa, waga, lvl)
        self.nazwa = nazwa
        self.waga = waga
        self.lvl = lvl
        self.obrona = obrona
        self.szybkosc = szybkosc



#test = Zbroja("Plytowa", 100, 1, 50, -10 )
#print(test.nazwa, test.waga, test.szybkosc)