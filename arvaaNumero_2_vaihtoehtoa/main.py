"""
Laita vakioon ARVATTAVA_LUKU jonka arvo on 124
Määritä vakio funktion avulla.

Tee ohjelma, joka pyytää arvaamaan lukua.
Jos käyttäjä syötti isomman luvun kuin muuttujassa, niin tulosta "Annoit liian suuren luvun"
Jos taas käyttäjän syöttämä luku oli pienempi kuin vakion luku  niin tulosta: "Annoin liian pienen luvun"

Kun käyttäjä arvaa luvun oikein, niin tulosta: "Oikein, arvasit luvun 27 kerralla!"
Missä siis arvo 27 kertoo montako kierrosta meni ennen kuin käyttäjä arvasi oikein.

TÄSSÄ RATKAISU 2, meni läpi testauksessa
"""
def ARVATTAVA_LUKU():
    return 124

kerrat = 0
arvattava = int(input("Anna luku: "))

while arvattava != ARVATTAVA_LUKU():
    kerrat = kerrat + 1
    if arvattava < ARVATTAVA_LUKU():
        print("Annoit liian pienen luvun")
        arvattava = int(input())
    else:
        print("Annoit liian suuren luvun")
        arvattava = int(input())

print("Oikein, arvasit luvun", kerrat + 1, "kerralla!")

