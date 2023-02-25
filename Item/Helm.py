from Item.ItemPodstawa import ItemPodstawa


class Helm(ItemPodstawa):



    def __init__(self, nazwa, waga, lvl, obrona, szybkosc):
        super().__init__(nazwa, waga, lvl)
        self.nazwa = nazwa
        self.waga = waga
        self.lvl = lvl
        self.obrona = obrona
        self.szybkosc = szybkosc



#test = Helm("Zelazny", 10, 1, 10, -1 )
#print(test.nazwa, test.waga, test.szybkosc)