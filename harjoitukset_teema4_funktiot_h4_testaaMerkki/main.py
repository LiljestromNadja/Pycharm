"""
teema 4
h4

Tee funktio testaaMerkki(...) joka ottaa parametrina yhden merkin (char)

funktio palauttaa kokonaisluvun seuraavasti:
0 jos merkki on numero 0...9
1 jos merkki on 'a'....'z' tai 'A'....'Z'
2 jos merkki ei ole numero eikä kirjain

Tulosta paluuarvoa käyttäen seuraava ilmoitus
jos paluuarvo on 0, tulosta "Numero"
jos paluuarvo on 1, tulosta "Kirjain"
jos paluuarvo on 2, tulosta "Ei numero eikä kirjain"
"""

def testaaMerkki(x):
    if x.isdigit():
        return 0
    elif x.isalpha():
        return 1
    else:
        return 2



merkki = input("Anna merkki: ").upper()
testaamerkki = testaaMerkki(merkki)

if testaamerkki == 0:
    print("Numero")
elif testaamerkki == 1:
    print("Kirjain")
else:
    print("Ei numero eikä kirjain")
