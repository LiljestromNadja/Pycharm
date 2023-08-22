""""
for arvo in arvojoukko
    tee jotain
    tee jotain muuta

Nyt arvojoukko on käyty läpi eli jatketaan luupin ulkopuolella
"""

"""Tulostetaan luvut 0-5. Huomaa että range() -funktiossa lähdetään oletusarvoisesti nollasta liikkeelle. """
print("Tulostetaan luvut 0-5. Huomaa että range() -funktiossa lähdetään oletusarvoisesti nollasta liikkeelle.")

for luku in range(6):
    print(luku)


"""Tulostetaan syötetyn merkkijonon merkit allekkain"""
print("\n\nTulostetaan syötetyn merkkijonon merkit allekkain")

teksti = input("Annapa hiukan tekstiä: ")
for merkki in teksti:
    print(merkki)


"""Tulostetaan kuukauden numerot. Lähdetään nyt ykkösestä."""
print("\n\nTulostetaan kuukauden numerot. Lähdetään nyt ykkösestä.")

for kuukausi in range(1, 13): # Määritellään ensimmäinen ykköseksi, range() -funktiossa ensimmäinen on oletuksena nolla.
    print(kuukausi) # Kuukaudet 1-12

"""Tulostetaan kuukauden numerot laskevasti eli lähdetään 12:sta"""
print("\n\nTulostetaan kuukauden numerot laskevasti eli lähdetään 12:sta")
for kuukausi in range(12, 0, -1): # Eka 12, viimeinen 1(range() -funktiolle 0 = 1!!!), huomaa -1
    print(kuukausi) # Kuukaudet 12-1

"""Tulostetaan parillisia lukuja."""
print("\n\nTulostetaan parillisia lukuja")
for parillinen in range(0, 11, 2): # Lähdetään nollasta, mennään kymppiin, lisätään kahdella
    print(parillinen) #tulostetaan parilliset 0-10

"""Tulostetaan 10*10 kertotaulu matriisina"""
print("\n\nTulostetaan 10*10 kertotaulu matriisina")
for a in range(1, 11): #Lähdetään ykkösestä, mennään kymppiin
    print(a, end=' ') #end = ei rivinvaihtoa
    for b in range(1,11):
        print(f"{(a*b): 4d}", end=' ') #f=formatointi, 4d= 4 merkin verran tilaa(että jää tyhjää väliin, d=kokonaisluku)
    print()


