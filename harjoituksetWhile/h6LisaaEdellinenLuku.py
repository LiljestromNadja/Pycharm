"""
teema 2 while
h6
Tulosta while -silmukassa allekkain seuraavasti:
2       eli tässä lisätään 1
3       tässä lisätään 2
5       tässä lisätään 3
8       tässä lisätään 4
12      tässä lisätään 5
17      tässä lisätään 6
23      tässä lisätään 7
Ja ei saa tulostaa niin, että whilen sisällä on if-viidakk, jossa vain tietyillä arvoilla tulostetaan..
"""

laskuri = 2 #alkuarvo
kasvatus = 1 #"kierrokset"

while laskuri <= 23:
    print(laskuri)
    laskuri = laskuri + kasvatus
    kasvatus = kasvatus + 1