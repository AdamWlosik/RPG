from Enemies.Mob import Mob


class Smok(Mob):

    def __init__(self, nazwa, agresja, lvl):
        super().__init__(nazwa, agresja, lvl)
        self.level = lvl
        print(self.hp)

    def atakuj(self, character):
        character.hp = character.hp - 5

        pass


test = Smok("Smok", 5, 5)
print(test.nazwa)
print(test.level)
print(test.atak)
