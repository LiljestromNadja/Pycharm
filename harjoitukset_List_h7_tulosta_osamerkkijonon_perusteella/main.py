"""
List
h7
Esittele merkkijonoja sisältävä lista. Kysy siihen nimiä, jotka muodostuvat etunimestä, välilyönnistä ja sukunimestä.
Teksti LOPPU päättää syötön.

Kysy sitten merkkijono, ja tulosta kaikki ne nimet kokonaisuudessaan, joissa kyseinen merkkijono esiintyy PELKÄSTÄÄN
sukunimessä

"""

nimet = []
# tai nimet = list()

while True:
    nimi = input("Anna etu- ja sukunimi välilyönnillä erotettuna (LOPPU päättää): ")
    if nimi.upper().strip() == "LOPPU":
        break
    if " " in nimi:
        nimet.append(nimi)

etsittava = input("Anna etsittävä nimi: ")
loydetyt = []
for nimi in nimet:
    nimiosina = nimi.split(" ")
    if etsittava in nimiosina[1]:   #Jos etsittäisiin etunimeä, indeksiin tulisi [0]
        loydetyt.append(nimi)

print("Haulla löydettiin seuraavat henkilöt")
for loydetty in loydetyt:
    print(loydetty)

