"""List [] , Listan käsittely

- Lista on joukko alkioita, joilla on järjestys. Listan sisältöä voidaan muuttaa. Listalla voidaan toteuttaa
kaikki ne ratkaisut, jotka toteutettiin ns perinteisellä taulukolla.
- Alkiot voivat olla mitä tahansa tietoja, eli lista ei ole ns tyypitetty. Eli samassa listassa voi olla lukuja,
merkkijonoja, totuusarvoja, olioita. Toki tällainen lista on hankalasti käsiteltävissä. Tyypillisesti listassa on
yhden tyyppisiä arvoja
- Lista esitellään muuttujana jolle annetaan hakasulkeiden sisällä arvot. Jos arvoja ei anneta yhtään, niin kyseinen
lista on aluksi tyhjä"""

nimet = ["Mikko", "Hanna", "Janne"] #Lista jossa merkkijonoja
arvosanat = [1,1,3,3,2,1,3,5,0,5] # Lista jossa kokonaislukuja

"""
Viitattaessa taulukon yksittäiseen, tiettyyn alkioon, käytetään indeksointia. Indeksit lähtevät nollasta, kuten
yleensä kaikissa ohjelmointiympäristöissä. Indeksi pitää viitata listassa olevaan alkioon. Jos ei, niin ohjelma kaatuu"""

print(nimet[1]) #Pitäisi tulostua Hanna
#print(nimet[10]) #kaatuu jos listassa ei ole 11 alkiota / IndexError: list index out of range

"""
Negatiivisella indeksoinnilla voidaan käsitellä alkioita LOPUSTA alkuun"""

print(nimet[-1]) #Pitäisi tulostua Janne
print(nimet)
"""
Listassa oleva arvo voidaan vaihtaa indeksin avulla"""

nimet[2] = "Helena" # Janne vaihtuu Helenaksi
print(nimet[2])
print(nimet)

"""
append() - Listan LOPPUUN voidaan LISÄTÄ ARVO append() -funktiolla"""

nimet.append("Ville") #Ville lisätään listan loppuun
print(nimet)

"""
insert() - Listaan voidaan määritellylle paikalle  lisätä arvo insert() -funktiolla"""

nimet.insert(3,"Kai") #Kai lisätään neljänneksi koska indeksit alkavat nollasta
print(nimet)

"""
Listan osalista saadaan indeksien avulla"""

print("Osalista, alkiot 2 ja 3")
uusilista = nimet[2:4] #Uuteen listaan tulevat alkiot 2 ja 3, ei 4
print(uusilista)

"""
sort() - Lista saadaan järjestettyä sort() -funktiolla. Tällöin merkkijonot menevät a -> ö ja luvut pienimmästä suurimpaan"""
print("sort")
nimet.sort()
print(nimet)

arvosanat.sort()
print(arvosanat)

"""
reverse() - muuttaa järjestyksen käänteiseksi, eli ensimmäinen alkio viimeiseksi ja toisinpäin. ei järjestele arvon mukaan kuten sort().
Jos haluat käänteisen aakkos-tai numerojärjestyksen, käytä ensin sort() -funktiota"""
print("reverse()")
print(nimet)
nimet.reverse()
print(nimet)

print(arvosanat)
arvosanat.reverse()
print(arvosanat)

"""
len() - Funktio len() palauttaa listan alkioiden määrän"""
print("Listan nimet alkioiden määrä")
print(len(nimet))
print("Listan arvosanat alkioiden määrä")
print(len(arvosanat))

"""
Listan läpikäynti alkio kerrallaan for -luupin avulla"""
print("Listan läpikäynti alkio kerrallaan for luupin avulla:\n for nimi in nimet:")
for nimi in nimet: #Lista käydään läpi alkio kerrallaan
    print(nimi)

"""tai"""
print("Listan läpikäynti alkio kerrallaan for luupin avulla:\n for i in range(len(nimet)):")
for i in range(len(nimet)): #Lista käydään läpi indeksien avulla, jos esim täytyy tulostaa monesko jokin on
    print(nimet[i])

"""
List Comprehension on lyhyt tapa muodostaa listasta osalistoja, jos haluaa että alkuperäinen lista säilyy ennallaan"""

"""In -operaatiolla saadaan testattua onko alkio listassa
    if nimi in nimet: #Onko nimi listassa
    If sana in merkkijono: #Onko sana merkkijonossa"""

if "Ville" in nimet:
    print("Kyllä, nimi ville on listassa")
    if "ille" in "Ville":
        print("toimii")

"""
index() - Returns the index of the first element with the specified value"""
paikkanro = nimet.index("Kai")
print("nimet.index, Kai ")
print(paikkanro)


