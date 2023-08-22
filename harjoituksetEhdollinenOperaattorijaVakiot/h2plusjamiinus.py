"""
teema 2 ehdollinen operaattori ja vakiot
h2

Lue käyttäjältä kaksi kokonaislukua ja lisäksi lue operaatio (+ tai -), joka luvuille tehdään. Jos operaatio oli
annettu väärin, niin laskutoimitusta ei saa tehdä, vaan annetaan virheilmoitus.

Esittele myös vastaus -muuttuja, joka saa arvon ehdollisessa operaattorissa käyttäjän syöttämän operaation perusteella.
Tulosta koko laskutoimitus lopuksi.
"""

luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))

oper = input("Anna operaatio (+/-): ")

if (oper != "+") and (oper != "-"):
    print("Virheellinen operaattori!")
else:
    vastaus = (luku1 + luku2) if oper == "+" else (luku1 - luku2)
    print(luku1, oper, luku2, "=", vastaus)