#h1

"""Lue kaksi arvoa kokonaislukumuuttujiin ja laske niiden osamäärä erilliseen muuttujaan.
Tulosta jakolaskun tulos kolmen desimaalin tarkkuudella.
HUOM! Ei tarvitse tutkia nollalla jakoa, koska ei vielä osata. """

jaettava = int(input("Anna jaettava luku: "))
jakaja = int(input("Anna jakava luku: "))

osamaara = jaettava/jakaja

print("Osamäärä = {0:2.3f}".format(osamaara))