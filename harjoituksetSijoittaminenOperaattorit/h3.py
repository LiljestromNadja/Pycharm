#h3
"""Lue kolme desimaalilukua muuttujiin. Laske näiden kolmen muuttujan tulo erilliseen muuttujaan ja
tulosta tulo muuttujasta näytölle 2 desimaalin tarkkuudella."""

luku1 = float(input("Anna ensimmäinen desimaaliluku: "))
luku2 = float(input("Anna toinen desimaaliluku: "))
luku3 = float(input("Anna kolmas desimaaliluku: "))

tulo = luku1 * luku2 * luku3

print("Tulo on: {0:2.2f}".format(tulo)) #määritellään tulostettavat desimaalit