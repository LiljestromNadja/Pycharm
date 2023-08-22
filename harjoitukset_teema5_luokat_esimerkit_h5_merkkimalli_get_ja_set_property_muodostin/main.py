"""
teema 5
h5

Tee luokka MerkkiMalli, jossa atovalmistajan merkki, malli ja tyyppi,, esim "Audi", "A6", "TDI 2.0 Sedan".
Tee getterit ja setterit (Python propertyillä) sekä tarvittava muodostin(konstruktori) ja metodit  __eq__, __str__.
Kaksi luokan oliota ovat tarkoittavat samaa merkkiä, jos kaikki kolme tietoa ovat samat.
Luo pääohjelmassa MerkkiMalli-tyyppinen olio ja testaa, että luokka toimii
"""
class MerkkiMalli:
    def __init__(self, merkki="Tuntematon", malli="Tuntematon", tyyppi="Tuntematon"):
        self.merkki = merkki
        self.malli = malli
        self.tyyppi = tyyppi

    @property
    def merkki(self): # palauttaa _merkki muuttujan arvon
        return self._merkki

    @merkki.setter
    def merkki(self, value):
        self._merkki = value

    @property
    def malli(self): #palauttaa _malli muuttujan arvon
        return self._malli

    @malli.setter
    def malli(self, value):
        self._malli = value

    @property
    def tyyppi(self): #palauttaa _tyyppi muuttujan arvon
        return self._tyyppi

    @tyyppi.setter
    def tyyppi(self, value):
        self._tyyppi = value

    def tulosta(self):
        print(self.merkki, self.malli, self.tyyppi)

    def __str__(self):
        return self.merkki + " " + self.malli + " " + str(self.tyyppi)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, MerkkiMalli):
            return self.merkki == other.merkki and self.malli == other.malli and self.tyyppi == other.tyyppi

if __name__ == '__main__':

    merkkimalli1 = MerkkiMalli("Skoda", "Octavio", "2.0 TD Sedan")
    merkkimalli2 = MerkkiMalli("Skoda", "Octavio", "2.0 TD Sedan")
    merkkimalli3 = MerkkiMalli("Fiat", "Panda", "21.1 GLS")

    print(merkkimalli1)
    if merkkimalli1 == merkkimalli2:
        print("Mallit ovat samoja")
    else:
        print("Ne ovat eri malleja")

