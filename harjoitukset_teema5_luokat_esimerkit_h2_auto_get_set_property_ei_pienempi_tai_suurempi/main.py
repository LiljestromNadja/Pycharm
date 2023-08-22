"""
teema 5
h2

Muuta edellistä luokkaa Auto ja määrittele kaikki attribuutit Pythonin get/set Propertyllä.
Huolehdi set propertyllä, että auton vuosimalli ei voi olla pienempi kuin 1900 tai suurempi kuin nykyinen vuosi.
Jos ehto ei täyty, niin aseta attribuuttiin kyseinen raja-arvo.
Luo ko tyyppinen olio pääohjelmassa ja anne arvot sen attribuuteille.
Tulosta olion attribuuttien arvot pääohjelmassa samalle riville käyttäen Auto-luokalle määriteltyä tulosta -metodia.
"""

import datetime

class Auto:
    def __init__(self, rekno="???-000", merkki="Tuntematon", vuosimalli=1900):
        self.rekno = rekno
        self.merkki = merkki
        self.vuosimalli = vuosimalli

    @property
    def rekno(self): # palauttaa rekno muuttujan arvon
        return self._rekno

    @rekno.setter
    def rekno(self, value):
        self._rekno = value

    @property
    def merkki(self): # palauttaa merkki muuttujan arvon
        return self._merkki

    @merkki.setter
    def merkki(self, value):
        self._merkki = value

    @property
    def vuosimalli(self): # palauttaa vuosimalli muuttujan arvon
        return self._vuosimalli

    @vuosimalli.setter
    def vuosimalli(self, value):
        if value < 1900:
            value = 1900
        elif value > datetime.datetime.now().year:
            value = datetime.datetime.now().year
        self._vuosimalli = value

    def tulosta(self):
        print(self.rekno, self.merkki, self.vuosimalli)

if __name__ == "__main__":

    auto1 = Auto("abc-123", "Mersu", 2020)
    auto1.tulosta()
    auto2 = Auto("abc-123", "Mersu", 2024)
    auto2.tulosta()
    auto3 = Auto()
    auto3.tulosta()
    auto4 = Auto("abc-123", "Tesla", 1890)
    auto4.tulosta()
