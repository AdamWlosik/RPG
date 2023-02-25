from Item.EwkipunekUbrany import EkwipunekUbrany
from PlayerTypes.KlasaPostaci import KlasaPostaci

class Player:
    def __init__(self):
        self.ekwipunek_ubrany = EkwipunekUbrany()
        self.klasa_postaci = KlasaPostaci()

    def ubierz_helm(self, helm):
        self.ekwipunek_ubrany.helm = helm

    def ubierz_bron(self, bron):
        self.ekwipunek_ubrany.bron = bron

    def ubierz_buty(self, buty):
        self.ekwipunek_ubrany.buty = buty

    def ubierz_spodnie(self, spodnie):
        self.ekwipunek_ubrany.spodnie = spodnie

    def ubierz_zbroje(self, zbroja):
        self.ekwipunek_ubrany.zborja = zbroja

    def obrona_itemow(self, obrona_item=0):
        if self.ekwipunek_ubrany.helm is not None:
            obrona_item += self.ekwipunek_ubrany.helm.obrona
        if self.ekwipunek_ubrany.zborja is not None:
            obrona_item += self.ekwipunek_ubrany.zborja.obrona
        if self.ekwipunek_ubrany.buty is not None:
            obrona_item += self.ekwipunek_ubrany.buty.obrona
        if self.ekwipunek_ubrany.spodnie is not None:
            obrona_item += self.ekwipunek_ubrany.spodnie.obrona
        return obrona_item

    def szybkosc_itemow(self, szybkosc_item=0):
        if self.ekwipunek_ubrany.helm is not None:
            szybkosc_item += self.ekwipunek_ubrany.helm.szybkosc
        if self.ekwipunek_ubrany.zborja is not None:
            szybkosc_item += self.ekwipunek_ubrany.zborja.szybkosc
        if self.ekwipunek_ubrany.buty is not None:
            szybkosc_item += self.ekwipunek_ubrany.buty.szybkosc
        if self.ekwipunek_ubrany.spodnie is not None:
            szybkosc_item += self.ekwipunek_ubrany.spodnie.szybkosc
        return szybkosc_item

    def atak_itemow(self, atak_item=0):
        if self.ekwipunek_ubrany.bron is not None:
            atak_item = self.ekwipunek_ubrany.bron.damage
        return atak_item

    def klasa_ninja(self, ninja):
        self.klasa_postaci.ninja = ninja

    def obroan_laczna_ninja(self):
        return self.obrona_itemow() + self.klasa_postaci.ninja.zrecznosc + self.klasa_postaci.ninja.lvl + \
               self.klasa_postaci.ninja.obrona

    def atak_laczna_ninja(self):
        return self.klasa_postaci.ninja.damage + 2 * self.klasa_postaci.ninja.zrecznosc + 2 * \
               self.klasa_postaci.ninja.lvl + self.klasa_postaci.ninja.atak

    def klasa_wojownik(self, wojownik):
        self.klasa_postaci.wojownik = wojownik

    def obroan_laczna_wojownik(self):
        return self.obrona_itemow() + 2 * self.klasa_postaci.wojownik.sila + 2 * self.klasa_postaci.wojownik.lvl + \
               self.klasa_postaci.wojownik.obrona

    def atak_laczna_wojownik(self):
        return self.klasa_postaci.wojownik.damage + self.klasa_postaci.wojownik.sila + self.klasa_postaci.wojownik.lvl \
               + self.klasa_postaci.wojownik.atak

    def klasa_szaman(self, szaman):
        self.klasa_postaci.szaman = szaman

    def obroan_laczna_szaman(self):
        return self.obrona_itemow() + self.klasa_postaci.szaman.inteligencja + self.klasa_postaci.szaman.lvl \
               + self.klasa_postaci.szaman.obrona

    def atak_laczna_szaman(self):
        return self.klasa_postaci.szaman.damage + self.klasa_postaci.szaman.inteligencja \
               + self.klasa_postaci.szaman.lvl + self.klasa_postaci.szaman.atak
