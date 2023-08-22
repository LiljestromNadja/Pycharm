"""
Teema 2
h2
Lue käyttäjältä kokonaisluku. Jos luku on parillinen, niin tulosta "parillinen", muuten pariton.
"""

luku = int(input("Anna kokonaisluku: "))
if(luku % 2 == 0):
    print("Antamasi luku on parillinen.")
else:
    print("Antamasi luku on pariton.")