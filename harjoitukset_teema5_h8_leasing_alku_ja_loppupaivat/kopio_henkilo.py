"""

Kopio

"""

from MerkkiMalli import MerkkiMalli
from kopio_Auto import Auto

class Henkilo:
    # Muodostin jossa annetaan kaikkien tiedot
    # Tämä on selkein tapa
    def __init__(self, etunimi="", sukunimi=""):

        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.autot = list()

    @property
    def etunimi(self): #palauttaa _etunimi muuttujan arvon
        return self._etunimi

    @etunimi.setter
    def etunimi(self, value):
        self._etunimi = value

    @property
    def sukunimi(self): #palauttaa _sukunimi muuttujan arvon
        return self._sukunimi

    @sukunimi.setter
    def sukunimi(self, value):
        self._sukunimi = value

    @property
    def autot(self): #palauttaa _autot muuttujan arvon
        return self._autot

    @autot.setter
    def autot(self, value):
        self._autot = value

    def lisaa_auto(self, auto):
        self.autot.append(auto)

    def tulosta_tiedot(self):
        print(self.etunimi, self.sukunimi)
        for auto in self.autot:
            print("\t", end="")
            auto.tulosta()

    def __str__(self):
        return self.etunimi + " " + self.sukunimi

if __name__ == "__main__":

    merkkimalli1 = MerkkiMalli("Skoda", "Octavia", "2.0 TD Sedan")
    merkkimalli2 = MerkkiMalli("Fiat", "Panda", "21.1 GLS")
    merkkimalli3 = MerkkiMalli("Volvo", "V70", "D4 2.0")

    auto1 = Auto("abc-123", merkkimalli1, 2020)
    auto2 = Auto("abc-123", merkkimalli2, 1999)
    auto3 = Auto("hhi-891", merkkimalli3, 2013)

    henkilo1 = Henkilo(etunimi="Jukka", sukunimi="Makkonen")
    henkilo1.lisaa_auto(auto1)
    henkilo1.lisaa_auto(auto2)

    henkilo2 = Henkilo(etunimi="Jukka", sukunimi="Kakkonen")
    henkilo2.lisaa_auto(auto3)

    henkilo1.tulosta_tiedot()
    henkilo2.tulosta_tiedot()

