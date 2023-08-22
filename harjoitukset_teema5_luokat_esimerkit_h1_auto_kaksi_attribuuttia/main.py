"""
Teema 5
h1

Tee Auto, jolla on kaksi attribuuttia reknro ja merkki ja vuosimalli.
Luo ko tyyppinen olio pääohjelmassa ja anna arvot sen attribuuteille muodostimessa.
Tulosta olion attribuuttien arvot pääohjelmassa arvo kerrallaan omille riveilleen.
"""

# Tässä ratkaisussa ei käytetä get/set propertyja

class Auto:
    def __init__(self, rekno, merkki, vuosimalli):
        self.rekno = rekno
        self.merkki = merkki
        self.vuosimalli = vuosimalli

if __name__== "__main__":
    auto = Auto("abc-123", "Mersu", 2020)
    print(auto.rekno)
    print(auto.merkki)
    print(auto.vuosimalli)