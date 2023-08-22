"""
Teema 5
h 8

Luo uusi LeasingAuto-luokka, joka periytyy luokasta Auto.
Uutena attribuuttina luokalla on leasing-sopimuksen alkupäivä ja loppupäivät.
Tee luokalle tarvittavat metodit (getterit ja setterit).
Luo myös muodostin sekä metodi tulosta. Edelleen testaa luokkaa pääohjelmasta

Yhdistä tehtävät 6 ja 7 siten, että henkilön omistama auto voi olla ns normaaliauto tai leasing-auto.
Jos kyseessä on leasing-auto, niin tulostetaan auton tietojen perään leasing-sopimuksen aloitus- ja lopetuspäivät seuraavasti:

 Jukka Makkonen
	abc-123 Skoda Octavio 2.0 TD Sedan 2020

	abc-123 Fiat Panda 21.1. GLS 1999

		Leasing alkaa:  31.10.2021 ja päättyy: 31.10.2021

	hhi-891 Volvo V70 D4 2.0 2013

Jukka Kakkonen

	abc-123 Skoda Octavio 2.0 TD Sedan 2020

	abc-123 Fiat Panda 21.1. GLS 1999

		Leasing alkaa:  31.10.2021 ja päättyy: 31.10.2021

	hhi-891 Volvo V70 D4 2.0 2013
"""

from MerkkiMalli import MerkkiMalli
from kopio_Auto import Auto
from kopio_henkilo import Henkilo

import datetime

class LeasingAuto(Auto):
    def __init__(self, rekno="???-000", merkkimalli=None, vuosimalli=1900, leasingAlkaa=datetime.datetime.now(),
                 leasingPaattyy=datetime.datetime.now()):
        Auto.__init__(self, rekno, merkkimalli, vuosimalli)
        self.leasingAlkaa = leasingAlkaa
        self.leasingPaattyy = leasingPaattyy

    @property
    def leasingAlkaa(self): #palauttaa leasingAlkaa muuttujan arvon
        return self._leasingAlkaa

    @leasingAlkaa.setter
    def leasingAlkaa(self, value):
        self._leasingAlkaa = value

    @property
    def leasingPaattyy(self): #palauttaa leasingPaattyy muuttujan arvon
        return self._leasingPaattyy

    @leasingPaattyy.setter
    def leasingPaattyy(self, value):
        self._leasingPaattyy = value

    def tulosta(self):
        super().tulosta()
        print("\t\t Leasing alkaa:", datetime.datetime.strftime(self.leasingAlkaa, "%d.%m.%Y.")), "ja päättyy:", datetime.datetime.strftime(self.leasingPaattyy,"%d.%m.%Y")

if __name__ == "__main__":
    merkkimalli1 = MerkkiMalli("Skoda", "Octavio", "2.0 TD Sedan")
    merkkimalli2 = MerkkiMalli("Fiat", "Panda", "21.1 GLS")
    merkkimalli3 = MerkkiMalli("Volvo", "V70", "D4 2.0")

    auto1 = Auto("abc-123", merkkimalli1, 2020)
    auto2 = LeasingAuto("abc-123", merkkimalli2, 1999, datetime.datetime.now())
    auto3 = Auto("hhi-891", merkkimalli3, 2013)

    henkilo1 = Henkilo(etunimi="Jukka", sukunimi="Makkonen")
    henkilo1.lisaa_auto(auto1)
    henkilo1.lisaa_auto(auto2)

    henkilo2 = Henkilo(etunimi="Jukka", sukunimi="Kakkonen")
    henkilo2.lisaa_auto(auto3)

    henkilo1.tulosta_tiedot()
    henkilo2.tulosta_tiedot()






