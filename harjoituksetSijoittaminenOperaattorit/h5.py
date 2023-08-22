#h5
"""Lue kokonaisluku ja desimaalilukuarvot erillisiin muuttujiin. Tulosta niiden summa sellaisenaan,
pyöristettynä kahteen desimaaliin, pyöristettynä lähimpään kokonaislukuun ja pyöristettynä alempaan
kokonaislukuun. """

kokonaisluku = int(input("Anna kokonaisluku: "))
desimaaluku = float(input("Anna desimaaliluku: "))

summa = kokonaisluku + desimaaluku
print("Summa on: ", summa)

#pyöristettynä kahteen desimaaliin
print("Summa pyöristettynä kahteen desimaaliin on: {0:2.2f}".format(summa))#2f tarkoittaa että desimaalipilkun jälkeen tulee kaksi numeroa.

#pyöristettynä lähimpään kokonaislukuun
print("Summa pyöristettynä lähimpään kokonaislukuun on: ", round(summa)) #round-funktio pyöristää LÄHIMPÄÄN kokonaislukuun, eli joko ylös tai alas

#muutettuna/pyöristettynä kokonaisluvuksi (alaspäin)
print("Summa pyöristettynä kokonaisluvuksi: ", int(summa))