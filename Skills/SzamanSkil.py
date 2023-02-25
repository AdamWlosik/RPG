class Skill:
    def __init__(self, inteligencja, lvl, damage):
        self.dmg = damage
        self.int = inteligencja
        self.lvl = lvl




    def oblicz(self):
        return 2.5 * self.int + self.dmg + 2.5 * self.lvl