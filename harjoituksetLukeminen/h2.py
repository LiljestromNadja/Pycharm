#h2

"""Lue nimi, osoite, postinumero ja postitoimipaikka (kaikki merkkijonoja) muuttujien arvot käyttäjältä ja tulosta
tiedot muuttujista seuraavasti:

Jussi Juonio
Vilholantie
71800 Siilinjärvi"""

nimi = input("Anna nimesi: ")
osoite = input("Anna osoitteesi: ")
postinro = input("Anna postinumerosi: ")
toimip = input("Syötä vielä postitoimipaikka: ")

print("{0}\n{1}\n{2}\n{3}".format(nimi,osoite,postinro,toimip))