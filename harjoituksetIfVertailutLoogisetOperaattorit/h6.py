"""
teema 2
h6
Lue käyttäjältä kaksi kokonaislukuarvoa. Tulosta suurempi näytölle. Jos luvut olivat samat, niin tulosta myös tieto siitä.
"""

#käyttäjän syöte

luku1 = int(input("Anna eka luku:  "))
luku2 = int(input("Anna toka luku:  "))

suurempi = 0


if(luku1 == luku2):
    print("Syöttämäsi luvut olivat samanarvoiset")
else:
    if(luku1 > luku2):
        suurempi = luku1
        print("Suurempi oli", suurempi)
    else:
        suurempi = luku2
        print("Suurempi oli", suurempi)


"""
Opettajan malliiratkaisu

luku1 = int(input("Anna eka luku"))
luku2 = int(input("Anna toka luku"))

if luku1 > luku2: # HUOM! pythonissa sulkeet if-lauseessa eivät ole välttämättömät
    print("Suurempi oli ", luku1)
elif luku1 < luku2:
    print("Suurempi oli ", luku2)
else:
    print("Luvut olivat yhtä suuret")"""