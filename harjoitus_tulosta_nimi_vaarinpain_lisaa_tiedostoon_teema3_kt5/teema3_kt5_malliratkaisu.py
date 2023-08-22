# -*- coding: utf-8 -*-

"""
KT 5

Kirjoita Python-kielinen ohjelma, joka kysyy käyttäjän nimeä, kuitenkin enintään 18 merkkiä.
Merkeissä saa olla tyhjeitä. Jos merkkejä > 18, tulostuu teksti "Virhe!".
Ohjelma tulostaa nimen alla kuvatusti laskevana ja pituudesta riippumatta sivusuunnassa alkaen oikeasta reunasta.
Jotta teksti hahmottuisi riviksi, lisää kaksi välilyöntiä perättäisten merkkien väliin. Kirjoita tämä myös nimi.txt-tiedostoon samassa muodossa.

Esimerkkiajo:
Anna nimesi:Jukka
        a
      k
    k
  u
J

"""


nimi = input("Anna nimesi:")
if len(nimi) > 18:
    print("Virhe!")
else:
    for i in range(0, len(nimi)):
        for j in range (len(nimi) - i, 1, -1):
            print ("  ", end = "") # Tulostetaan rivin alkuun tyhjeitä
        print(nimi[len(nimi)-i-1]) # Ja rivin loppuun oikea merkki

    # Ja sama tulostus tiedostoon
    file = "nimi.txt"
    wfile = open(file, "wt")

    for i in range(0, len(nimi)):
        for j in range (len(nimi) - i, 1, -1):
            wfile.write("  ") # Tulostetaan rivin alkuuan tyhjeitä
        wfile.write(nimi[len(nimi)-i-1] + "\n") # Ja rivin loppuun oikea merkki

    wfile.close()


