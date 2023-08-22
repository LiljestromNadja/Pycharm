"""
List
h1
Lue käyttäjältä kolme kokonaislukua listaan. Tulosta sen jälkeen lukujen summa näytölle. ÄLÄ KÄYTÄ SILMUKKAA.
"""

# Luodaan lista luvut

luvut = []
#Toinen vaihtoehto luoda lista # luvut = list()

luvut.append(int(input("Anna eka luku: ")))
luvut.append(int(input("Anna toka luku: ")))
luvut.append(int(input("Anna kolmas luku: ")))

print("Lukujen summa on", luvut[0] + luvut[1] + luvut[2])
