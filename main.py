from Item.Bron import Bron
from Item.Buty import Buty
from Item.Helm import Helm
from Item.Spodnie import Spodnie
from Item.Zbroja import Zbroja
from Player.Player import Player
from PlayerTypes.Wojownik import Wojownik
from PlayerTypes.Ninja import Ninja
from PlayerTypes.Szaman import Szaman

p = Player()

h = Helm("Helm", 1, 1, 1, -1)
b = Bron("Bron", 10, 1, 50)
bu = Buty("Trzewiki", 10, 1, 50, 5)
s = Spodnie("Skorzane", 25, 1, 20, -5)
z = Zbroja("Plytowa", 100, 1, 50, -10)

#p.ubierz_helm(h)
p.ubierz_bron(b)
p.ubierz_buty(bu)
p.ubierz_spodnie(s)
p.ubierz_zbroje(z)

oi = p.obrona_itemow()  # 121
si = p.szybkosc_itemow()  # -11
ai = p.atak_itemow()  # 50

ninja = Ninja("Ninja", 2, 1, ai)
skil1n = ninja.Skill1()
p.klasa_ninja(ninja)
oln = p.obroan_laczna_ninja()
aln = p.atak_laczna_ninja()
#print(ninja.to_Json_Ninja())
file = open(r"C:\Users\adamw\OneDrive\Pulpit\zapis.txt", mode="w")
file.write(ninja.to_Json_Ninja())

wojownik = Wojownik("Wojownik", 2, 1, ai)
skil1w = wojownik.Skill1()
p.klasa_wojownik(wojownik)
olw = p.obroan_laczna_wojownik()
alw = p.atak_laczna_wojownik()
#print(wojownik.to_Json_Wojownik())
file.write(wojownik.to_Json_Wojownik())

szaman = Szaman("Szaman", 2, 1, ai)
skil1s = szaman.Skill1()  ##57.5
p.klasa_szaman(szaman)
ols = p.obroan_laczna_szaman()
als = p.atak_laczna_szaman()
#print(szaman.to_Json_Szaman())
file.write(szaman.to_Json_Szaman())
file.close()

"""zninja = {"nick": ninja.nick, "lvl": ninja.lvl, "hp": ninja.hp, "mana": ninja.mana, "atak": ninja.atak,
          "obrona": ninja.obrona, "zrecznosc": ninja.zrecznosc, "damage": ninja.damage}""" # Zapis.py

i = 5
