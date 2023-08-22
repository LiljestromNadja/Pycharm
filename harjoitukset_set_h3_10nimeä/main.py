"""
Set
h3
Lue käyttäjältä 10 nimeä. Samaa nimeä ei hyväksytä vaan sen tilalle pyydetään uusi nimi. Huomaa, että nimi on
sama, olipa se kirjoitettu isoitlla tai pienillä kirjaimilla. Käy lopuksi nimet läpi ja tulosta nimet alkuperäisessä
syöttöasussa ja järjestyksessä. Tarvitset siis listan, koska alkuperäiset pitää pitää jossain tallessa. Setin avulla tsekkaat
että nimi ei ole jo syötetty.
"""

nimet = list()

tarkistusnimet = set()

while len(nimet) < 10:
    nimi = input("Anna nimi: ")
    if nimi.upper() not in tarkistusnimet:
        tarkistusnimet.add(nimi.upper())    #Viedään nimi isona tarkistus settiin
        nimet.append(nimi)      #Viedään nimi alkuperäisessä muodossaan talteen nimet -listaan
    else:
        print("Nimi oli jo listassa")

for n in nimet: #Tulostetaan nimet -lista
    print(n)