class Skill:
    def __init__(self, sila, lvl, damage):
        self.dmg = damage
        self.sila = sila
        self.lvl = lvl

    def oblicz(self):
        return self.sila + self.dmg + self.lvl
