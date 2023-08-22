#h6
"""Esittele kaksi muuttujaa ja anna niille kokonaislukualkuarvot. Tulosta lukujen summa laskutoimituksineen + -tavalla
ja lukujen erotus laskutoimituksineen {} -tavalla. Vinkki: Voitte käyttää kolmatta muuttujaa johon laskette tuloksen. """

# + -tapa, summa

luku1 = 18
luku2 = 21
summa = luku1 + luku2

print(str(luku1) + " + " + str(luku2) + " = " + str(summa))
# HUOM!! VOI TEHDÄ MYÖS NÄIN
print(str(luku1) + " + " + str(luku2) + " = " + str(luku1 + luku2))

#{} -tapa, erotus

erotus = luku1 - luku2
print("{0} - {1} = {2}".format(luku1,luku2,erotus))