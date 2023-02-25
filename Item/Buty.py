from Item.ItemPodstawa import ItemPodstawa


class Buty(ItemPodstawa):
    def __init__(self, nazwa, waga, lvl, obrona, szybkosc):
        super().__init__(nazwa, waga, lvl)
        self.nazwa = nazwa
        self.waga = waga
        self.lvl = lvl
        self.obrona = obrona
        self.szybkosc = szybkosc


#test = Buty("Trzewiki", 10, 1, 50, 5)
#print(test.nazwa, test.szybkosc)