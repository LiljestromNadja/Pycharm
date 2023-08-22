"""
List
h3
Lue käyttäjältä 10 desimaalilukua listaan. Lukua 0 ei hyväksytä vaan sen tilalle pyydetään uusi arvo.
Käy lopuksi lista läpi ja tulosta tieto siitä, kuinka monta positiivista ja negatiivista arvoa syötettiin.
Voit toteuttaa em ratkaisun osalistoilla tai ihan perinteisesti luuppaamalla lista läpi
"""

luvut = []

for indeksi in range(1,11):
    while True:
        luku = float(input("Anna luku nro " + str(indeksi) + ": "))
        if luku != 0:
            break
    luvut.append(luku)

negat_listassa = [x for x in luvut if x < 0]
neg_lkm = len(negat_listassa)
pos_lkm = len(luvut) - neg_lkm

print("Positiivisia oli:", pos_lkm)
print("Negatiivisia oli:", neg_lkm)
