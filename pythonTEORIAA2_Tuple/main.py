"""
Tuple, ()

- Tuple on joukko alkioita ja on järjestetty ja ei ole muutettavissa. Sallii saman arvon kahteen kertaan.
- Toki ratkaisut voidaan aina toteuttaa listalla, mutta joihinkin tilanteisiin tuple on parempi ja "suojatumpi", koska
sen sisältöä ei voi luonnin jälkeen muuttaa
- Tuplesta voi tavallisen listan tapaan tehdä uusia listoja
- Esim. arkipaivat  = ("Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai")
- Tuplen alkioiden läpikäynti samaan tapaan kuin listalla
- Tuplea käytetään siis listoissa, joiden ei ole tarkoitus muuttua luonnin jälkeen, esim. viikonpäivät, kuukaudet jne
- Tuple voidaan toki generoida uudelleen tai siihen lisätä uusia arvoja listan kautta
- On huomattava että yhden alkion sisältävässä tuplessa alkion perään on laitettava pilkku, koska muuten python ei tunnista sitä
tupleksi
    esim.
        eiplaneetat = ("Pluto",)
        planeetat = ("Merkurius", "Mars")
- Tupleen voidaan liittää tuple eli "laskea yhteen"
"""

talvikuukaudet = ("Joulu", "Tammi")
apulista = list(talvikuukaudet)
apulista.append("Helmi")
talvikuukaudet = tuple(apulista)
print(talvikuukaudet)

planeetat = ("Pluto",)
uusiplaneetta = ("Mars",)
planeetat = planeetat + uusiplaneetta # voidaan merkitä myös planeetat += uusiplaneetta
print(planeetat)