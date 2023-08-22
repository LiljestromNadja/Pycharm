"""
teema 5
h4

Tee em luokalle __eq__ -metodi.
Toteuta se niin, että Auto-oliot ovat sama auto, jos rekisterinumero on sama.
Luon pääohjelmassa kaksi eri auto-oliota samalla rekisterinumerolla
(eri merkillä/vuosimallilla) ja vertaa, että onko ne samat.
Tulosta "Auto on sama" tai "Auto on eri", riippuen rekisterinumeron sisällöstä.
Elä siis vertaa pääohjelmassa rekisterinumeroita, vaan vertaa autoja.
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

    def __str__(self):
        #Huomaa että käytettävä str funktiota numeerisen tiedon kohdalla
        return self.rekno + " " + self.merkki + " " + str(self.vuosimalli)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Auto):
            return self.rekno == other.rekno
        return False

if __name__ == "__main__":

    auto1 = Auto("abc-123", "Mersu", 2020)
    auto2 = Auto("abc-123", "Volovo", 1999)

    if auto1 == auto2: # kutsuu luokan __eq__ metodia
        print("Autot ovat samoja vaikka olio eri")
    else:
        print("Eri autot kyseessä")

    auto3 = Auto("abc-122", "Volovo", 1999)
    if auto2 == auto3:
        print("Autot ovat samoja vaikka olio eri")
    else:
        print("Eri autot kyseessä")