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
import os

nimi = input("Anna nimi:")

if len(nimi) > 18:
    print("Virhe!")
else:
    nimi = nimi[::-1]
    for i in range(0, len(nimi)):
        for x in range(len(nimi)-i, 1, -1):
            print("  ", end="")
        print(nimi[i])

    file = "nimi.txt"
    wfile = open(file, "wt")

    for i in range(0, len(nimi)):
        for x in range(len(nimi)-i, 1, -1):
            wfile.write("  ")
        wfile.write(nimi[i] + "\n")
    wfile.close()

#Huom! Reversing a string
print("\n\nReversing a string")
nimi2 = input("Anna käännettävä teksti")
print("\n Annoit: ", nimi2)
print("Käännetään..")
nimi2 = nimi2[::-1]

print(nimi2)

for o in range(len(nimi2)):
    for a in range(len(nimi2)-o, 1, -1):
        print("-", end="")
    print(nimi2[o])

