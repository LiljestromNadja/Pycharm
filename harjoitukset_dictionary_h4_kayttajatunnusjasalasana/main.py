"""
Dictionary
h4

Luo dictionary, jossa on muutamia käyttäjätunnus ja salasana -pareja. Kysy sen jälkeen käyttäjältä käyttäjätunnusta
ja salasanaa ja kerro käyttäjälle, täsmääkö se vai ei. Jos täsmää, pyydä käyttäjältä uutta salasanaa ja vie se ko
tunnuksen salasanaksi. Kun ohjelma lopetetaan, tulostetaan päivitetty dictionary. Tunnus LOPPU lopettaa tunnusten syötön
"""

tunnukset = {"minna": "abc123", "janne": "qwerty", "kaweri321": "kaweri321"}

while True:
    tunnus = input("Anna käyttäjätunnus")
    if tunnus.upper().strip() == "LOPPU":
        break
    if tunnus not in tunnukset:
        print("Tarkista syöte")
        continue

    salasana = input("Anna salasana: ")

    if tunnus in tunnukset and salasana == tunnukset[tunnus]:
        salasana = input("Syötä uusi salasana")
        tunnukset[tunnus] = salasana
    else:
        print("Salasana / tunnus ei täsmää")

for i in tunnukset:
    print(i, tunnukset[i])
