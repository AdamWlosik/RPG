import json
from Character.Character import Character
from Skills.SzamanSkil import Skill


class Szaman(Character):
    def __init__(self, nick, lvl, inteligencja, damage):
        super().__init__(nick, lvl)
        self.inteligencja = inteligencja
        self.damage = damage
        self.skill = Skill(inteligencja, lvl, damage)

    def Skill1(self):
        return self.skill.oblicz()

    def Skill2(self):
        return self.skill.oblicz() + 1

    def Skill3(self):
        return self.skill.oblicz() + 2

    def Skill4(self):
        return self.skill.oblicz() + 3

    def to_Json_Szaman(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


#test = Szaman("Szaman", 1, 1, 1)
#print(test.nick)
#print(test.Skill4())
#print(test.mana + 2)
