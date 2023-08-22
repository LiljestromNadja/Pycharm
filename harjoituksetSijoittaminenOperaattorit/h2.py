#h2
"""Lue käyttäjältä kaksi arvoa ja tulosta lukujen jakojäännös seuraavasta:
Lukujen 9 ja 4 jakojäännös on 1."""

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))

jakojaannos = luku1 % luku2

#print(jakojaannos)

print("Lukujen {0} ja {1} jakojäännös on {2}".format(luku1,luku2,jakojaannos))