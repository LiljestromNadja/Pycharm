"""
teema 4
h2

Lue käyttäjältä nimi, ikä ja hetu muuttujiin pääohjelmassa. Kutsu sen jälkeen tulosta -funktiota, jossa tulostetaan
näiden kaikkien muuttujien arvot
"""

def tulosta(nimi, ika, hetu):
    print("Nimi:", nimi)
    print("Ikä: ", ika)
    print("Hetu: ", hetu)

nimi = input("Anna nimi: ")
ika = input("Anna ikä: ")
hetu = input("Anna hetu: ")

tulosta(nimi, ika, hetu)