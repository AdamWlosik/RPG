import json
from Character.Character import Character
from Skills.NinjaSkil import Skill


class Ninja(Character):
    def __init__(self, nick, lvl, zrecznosc, damage):
        super().__init__(nick, lvl)
        self.zrecznosc = zrecznosc
        self.damage = damage
        self.skill = Skill(zrecznosc, lvl, damage)

    def Skill1(self):
        return self.skill.oblicz()

    def Skill2(self):
        return self.skill.oblicz() + 1

    def Skill3(self):
        return self.skill.oblicz() + 2

    def Skill4(self):
        return self.skill.oblicz() + 3

    def to_Json_Ninja(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


#test = Ninja("Ninja", 1, 1, 1)
#print(test.zrecznosc)
#print(test.mana)
#print(test.Skill1())
