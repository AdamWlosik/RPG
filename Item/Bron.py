from Item.ItemPodstawa import ItemPodstawa


class Bron(ItemPodstawa):
    def __init__(self, nazwa, waga, lvl, damage):
        super().__init__(nazwa, waga, lvl)
        self.nazwa = nazwa
        self.waga = waga
        self.lvl = lvl
        self.damage = damage


#test = Bron("Miecz", 10, 1, 50)
#print(test.nazwa, test.damage)
