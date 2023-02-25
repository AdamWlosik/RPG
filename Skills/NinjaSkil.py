class Skill:
    def __init__(self, zrecznosc, lvl, damage):
        self.dmg = damage
        self.zrecznosc = zrecznosc
        self.lvl = lvl

    def oblicz(self):
        return self.zrecznosc + self.dmg + self.lvl