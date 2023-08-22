"""
teema 5
h6

Muokkaa Auto-luokkaa siten, että autollta poistuu jäsenmuuttuja Merkki
ja sen tilalle tulee MerkkiMalli-tyyppinen olio.
Käytä ed. tehtävässä toteutettua MerkkiMalli-luokkaa.
Autosta tulee siis koosteluokka. Luo pääohjelmassa auto, jolla on MerkkiMalli-tyyppinen olio
ja tulosta auton tiedot käyttäen molemmille luokille määriteltyä tulosta()-metodia
esim
Rekno: axz-345, Vuosimalli= 2012, Merkki=Audi, Malli=A6, Tyyppi=TDI 2.0 Sedan

Voit toki kopioida luokan MerkkiMalli koodit samaan .py tiedostoon, jossa sinulla on auto luokka.
Toinen järkevämpi tapa on lisätä  seuraava rivi Auton-luokan sisältävän py-tiedoston alkuun

from LuokkaEsim1_5 import MerkkiMalli

Molempien py-tiedostojen pitää olla samassa hakemistossa.
"""
from MerkkiMalli import MerkkiMalli

import datetime

class Auto:
    def __init__(self, rekno="???-000", merkkimalli=None, vuosimalli=1900):
        self.rekno = rekno
        self.merkkimalli = merkkimalli
        self.vuosimalli = vuosimalli

    @property
    def rekno(self): # palauttaa rekno muuttujan arvon
        return self._rekno

    @rekno.setter
    def rekno(self, value):
        self._rekno = value

    @property
    def merkkimalli(self): # palauttaa merkkimalli muuttujan arvon
        return self._merkkimalli

    @merkkimalli.setter
    def merkkimalli(self, value):
        self._merkkimalli = value

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
        print(self.rekno, self.merkkimalli, self.vuosimalli)

    def __str__(self):
        #Huomaa että käytettävä str funktiota numeerisen tiedon kohdalla
        return self.rekno + " " + self.merkkimalli + " " + str(self.vuosimalli)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Auto):
            return self.rekno == other.rekno
        return False

if __name__ == "__main__":
    merkkimalli1 = MerkkiMalli("Skoda", "Octavio", "2.0 TD Sedan")
    merkkimalli2 = MerkkiMalli("Fiat", "Panda", "21.1 GLS")

    auto1 = Auto("abc-123", merkkimalli1, 2020)
    auto2 = Auto("abc-123", merkkimalli2, 1999)

    if auto1 == auto2: #Kutsuu luoka __eq__ metodia
        print("Autot ovat samoja vaikka olio on eri")
    else:
        print("Eri autot kyseessä.")

    auto3 = Auto("abc-122", merkkimalli2, 1999)
    print(auto3)

    if auto2 == auto3:
        print("Autot ovat samoja, vaikka olio eri")
    else:
        print("Eri autot kyseessä")