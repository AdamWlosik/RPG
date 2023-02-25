class Mob:
    def __init__(self, nazwa, agresja, lvl):
        self.nazwa = nazwa
        self.hp = 100
        self.atak = 5 * lvl
        self.obrona = 5 * lvl
        self.agresja = agresja


# test = Mob("Moby", "Tak", 10)
# print(test.hp)