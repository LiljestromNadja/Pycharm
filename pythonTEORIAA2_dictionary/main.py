"""
Dictionary {}

- Dictionary on joukko avain-arvo -pareja, jotka on järjestetty sekä muutettavissa. Ei salli samaa AVAINTA kahteen
kertaan. Avain ja arvo erotetaan kaksoispisteellä (:) ja eri parit pilkulla (,)
- Avaimen ja arvon ei tarvitse olla samaa tyyppiä eli avain voi ola vaikkapa luku ja arvo merkkijono
esim.
    #Autot, jossa rekisterinumero on avain
    autot = {"abc-123" : "Volvo V70", "xyz-321" : "Audi A6", "cba-987", "Skoda Octavia"}
    print(autot)

    #Käyttäjätunnus/salasanatiedot
    tunnukset = {"mikke12" : "mikkis", "sari45" : "sari123", "jupero" : "abc100"}

- Arvoon viitataan avaimen perusteella
esim.
    print(tunnukset["sari45"]) #Avainta vastaavan arvon haku

- Dictionaryn alkioiden määrä len() -funktiolla
- Avainten/arvojen läpikäynti for-luupilla

esim.
    for arvo in tunnukset:
        print(arvo) # Tulostaa avaimen
        print(tunnukset[arvo]) #Tulostaa arvon
"""

tunnukset = {"mikke12": "mikkis", "sari45": "sari123", "jupero": "abc100"}

for lapikaynti in tunnukset:
        print(lapikaynti, end=",") # Tulostaa avaimen
        print(tunnukset[lapikaynti]) #Tulostaa arvon


""" Täysin sama kyin yllä
for i in tunnukset:
        print(i, end=",")
        print(tunnukset[i])"""

"""JOS AVAINTA EI LÖYDY, ohjelma kaatuu"""

# print(tunnukset["Jepulis"])  # Kaatuu koska avainta "Jepulis" ei ole

#Tsekataan ensin onko avainta
if "jepulis" not in tunnukset:
        print("Avainta ei löydy")
else:
        print(tunnukset["jepulis"])


"""testailua, funktioita"""

print("Funktioiden testailua")
numeeriset = {1: 11, 2: 12, 3: 13}

for numerot in numeeriset:
        print("Avain:", numerot, end=",")
        print("Arvo:", numeeriset[numerot])

print("sum()", sum(numeeriset))
print("max()", max(numeeriset))
print("min()", min(numeeriset))
print("sorted()", sorted(numeeriset))
