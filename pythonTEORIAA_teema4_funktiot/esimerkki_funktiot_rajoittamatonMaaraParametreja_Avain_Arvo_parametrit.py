"""
- Esimerkki rajoittamattomasta määrästä parametrejä
- Esimerkki avain/arvo -parin kautta määritetyistä parametreistä
"""

def palauta_summa(*luvut): #rajoittamaton määrä lukuja
    #def palauta_summa(*args) - kirjataan usein näin
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

def tulosta_isa_lapsi(isa, lapsi):
    print("Isän nimi: ", isa)
    print("Lapsen nimi: ", lapsi)

def tulosta_suku(**suku):
    #def tulosta_suku(*kargs) - kirjataan usein näin
    print("Isän nimi: ", suku["isa"])
    print("Äidin nimi: ", suku["aiti"])
    print("Lapsen nimi", suku["lapsi"])

summa = palauta_summa() #Ei yhtään parametria
print("Lukujen summa on nyt:", summa) #Eli tulostuu 0
print()

luku1 = int(input("Anna luku: "))
luku2 = int(input("Anna luku: "))
luku3 = int(input("Anna luku: "))

lukujensumma = palauta_summa(luku1, luku2, luku3) #3 parametriä
print("Antamiesi lukujen summa on nyt: ", lukujensumma)
print()

# Huomaa parametrien järjestys
# Nimetään kutsussa parametri johon arvo sijoitetaan
tulosta_isa_lapsi(lapsi= "Mikko", isa= "Matti")
print()

#käyttäjän syötteen perusteella
syoteisa = input("Anna isän nimi: ")
syotelapsi = input("Anna lapsen nimi: ")

print("\nAnnettu syöte: ")
tulosta_isa_lapsi(lapsi= syotelapsi, isa=syoteisa)
print()

#Määritellään parametrit nyt dictionary -tyyppisenä listana
tulosta_suku(isa="Pekka", aiti="Hanna", lapsi="Laura")

print()
print("tulosta_suku -funktio käyttäjän syötteellä")
annettuisa = input("Anna isän nimi: ")
annettuaiti = input("Anna äidin nimi: ")
annettulapsi = input("Anna lapsen nimi: ")

print("\nAnnoit tiedot:")
tulosta_suku(isa=annettuisa, aiti=annettuaiti, lapsi=annettulapsi)

