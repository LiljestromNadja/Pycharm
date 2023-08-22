"""
Funktio joka laskee ympyrän alan ja palauttaa sen

laske_ala() - funktion nimi jota käytetään kun funktiota kutsutaan
sade - parametri funktiolle, parametrilla välitetään tietoa funktiolle
ala - funktion sisäinen muuttuja (apumuuttuja)
return - lause jolla palautetaan jokin arvo kutsuneeseen ohjelmaan
"""

import math

def laske_ala(sade):
    ala = math.pi * (sade**2)
    return ala

sade = int(input("Anna säde"))
pintaAla = laske_ala(sade)
print("Pinta-ala on {0:.2f}".format(pintaAla))