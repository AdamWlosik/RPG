import json
from Character.Character import Character
from Skills.WojownikSkil import Skill


class Wojownik(Character):
    def __init__(self, nick, lvl, sila, damage):
        super().__init__(nick, lvl)
        self.sila = sila
        self.damage = damage
        self.skill = Skill(sila, lvl, damage)

    def Skill1(self):
        return self.skill.oblicz()

    def Skill2(self):
        return self.skill.oblicz() + 1

    def Skill3(self):
        return self.skill.oblicz() + 2

    def Skill4(self):
        return self.skill.oblicz() + 3

    def to_Json_Wojownik(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

# test = Wojownik("Wojownik", 1, 1, 1)
# print(test.Skill1())
# print(test.Skill2())
# print(test.Skill3())
# print(test.Skill4())
# print(test.nick)
