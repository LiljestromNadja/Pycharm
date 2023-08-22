"""
teema 2 ehdollinen operaattori ja vakiot
h5
Lue käyttäjältä viikonpäivän numero 1-7. Tulosta numeroa vastaava viikonpäivän nimi switch-case
tyyppisellä rakenteella. Jos käyttäjä syötti jonkun väärän numeron, niin anna joku virheilmoitus defaultissa.
"""

viikonpaivat = {1: "Maanantai", 2: "Tiistai", 3: "Keskiviikko", 4: "torstai", 5: "perjantai", 6: "lauantai", 7: "sunnuntai"}
vkonpaivanro = int(input("Anna viikonpäivän numero 1-7: "))

viikonpaiva = viikonpaivat.get(vkonpaivanro, "Outo päivä") #Suluissa ensimmäinen on muuttuja jossa käyttäjän syöte
                                                            # Jälkimmäinen tulostetaan jos haettavaa numeroa ei löydy

print(viikonpaiva)




