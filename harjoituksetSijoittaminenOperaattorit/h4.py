#h4
"""Lue käyttäjältä neljä kokonaislukuarvoa ja tulosta siihen mennessä syötettyjen lukujen yhteenlaskettu
summa jokaisen luvun lukemisen jälkeen. Käytä apumuuttujaa välituloksen laskennassa."""

luku1 = int(input("Anna ensimmäinen luku "))
valisumma = luku1
print("Yhteensä: ", valisumma)

luku2 = int(input("Anna toinen luku "))
valisumma = valisumma + luku2
print("Yhteensä: ", valisumma)

luku3 = int(input("Anna kolmas luku "))
valisumma = valisumma + luku3
print("Yhteensä: ", valisumma)

luku4 = int(input("Anna neljäs luku "))
valisumma = valisumma + luku4
#print("Yhteensä: ", valisumma)

print("Luvut {0} + {1} + {2} + {3} ovat yhteensä {4}".format(luku1,luku2,luku3,luku4,valisumma))