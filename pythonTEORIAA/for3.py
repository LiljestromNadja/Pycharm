"""break ja continue -hyppylauseet"""
print("break ja continue -hyppylauseet")

viikonpaivat = [] # Lista on aluksi tyhjä eli ei viikonpäiviä

for a in range(1, 8):
    while True:
        print("Anna viikonpäivän", a, "nimi: ", end=' ')
        viikonpaiva = input().upper() # Muutetaan käyttäjän syöte isoiksi kirjaimiksi
        if(viikonpaiva in viikonpaivat):
            print("Viikonpäivä on jo listassa")
            continue # Hypätään while -luupin ALKUUN
        viikonpaivat.append(viikonpaiva) # Lisätään listaan viikonpäivä joka ei siellä vielä ole
        break # Hypätään while -luupin ULKOPUOLELLE

    for pv in viikonpaivat:
        print(pv)