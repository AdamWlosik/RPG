from Enemies.Smok import Smok


class Atak:
    def __init__(self, damage_ataku):
        self.damage_ataku = damage_ataku

    def oblicz_atak(self):
        return self.damage_ataku