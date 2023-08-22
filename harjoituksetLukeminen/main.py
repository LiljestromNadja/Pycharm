#h1

"""Esittele kolme muuttujaa ja aseta niihin arvot desimaalilukuna, kokonaislukuna ja merkkijonona.
Lue niihin käyttäjältä arvot ja tulosta ne allekkain yhdellä print -lauseella. """

# Luetaan käyttäjän syöte muuttujien arvoksi

desimaali = 0.0
kokonaisluku = 0
merkkijono = "0"

print("Anna desimaaliluku: ", end= '')
desimaali = float(input())

kokonaisluku = int(input("Anna kokonaisluku: "))

merkkijono = input("Anna merkkijono: ")

print("{0}\n{1}\n{2}".format(desimaali, kokonaisluku, merkkijono))