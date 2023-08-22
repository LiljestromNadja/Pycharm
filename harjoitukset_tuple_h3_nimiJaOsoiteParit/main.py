"""
Tuple
h3

Tee tuple, jossa on henkilöiden nimi+osoite -pareja. Nimi + osoite toteutetaan listana. Toisin sanoen siis yksi tuplen alkio
on lista, jossa on nimi ja osoite erillisenä. Tuplea luotaessa laita neljä nimi+osoitetietoa ja lopuksi tulosta luupin avulla
tuplen sisältö siten että yhden henkilön tiedot (nimi+osoite) tulee yhdelle riville
"""

nimet = tuple() #näin tehdään tyhjä tuple

nimet = (["Minna Muikku", "Ahvenkuja 12 Virtasalmi"],
         ["Matti Mainio", "Katujenkatu 1 Stadi"],
         ["Pertti Eräreikä", "metsä kaukana"],
         ["Hara Hirmuinen", "Sörkkä osasto 3"])

for henkilo in nimet:
    for tiedot in henkilo:
        print(tiedot, end=" ")
    print()