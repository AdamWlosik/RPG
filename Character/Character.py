# from Enemies.Smok import Smok

class Character:
    def __init__(self, nick, lvl):
        self.nick = nick
        self.lvl = lvl
        self.hp = 1000
        self.mana = 100 + (100 * lvl)
        self.atak = 10
        self.obrona = 10


    # def atakuj(self):
    #     self.atakuj = Smok()






#test = Character("Character")
#print(test.nick)
#print(test.mana)


