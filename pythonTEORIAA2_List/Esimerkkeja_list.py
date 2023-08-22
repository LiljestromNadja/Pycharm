nimet = ["Mikko", "Hanna", "Janne"] # Lista jossa merkkijonoja
arvosanat = [1,1,3,3,2,1,3,5,0,5]

print("Koko listan tulostus\n")
print(nimet) #Koko listan tulostus
print(arvosanat)

print("\nViittaus listan alkioon indeksin avulla. Indeksointi lähtee nollasta")
print(nimet[1])
print("\nViimeinen alkio")
print(nimet[-1])
#print(nimet[10]) #Kaatuu koska viitataan listan ulkopuolelle

print("\nLisätään Ville listan loppuun")
nimet.append("Ville")
print(nimet)

print("\nVille lisätään uudelleen, nyt listassa kaksi Villeä")
nimet.append("Ville")
print(nimet)

print("\nLisätään Mari listan toiseksi alkioksi")
nimet.insert(1, "Mari")
print(nimet)

print("\nVaihdetaan kolmas alkio (Hanna) Helenaksi")
nimet[2] = "Helena"
print(nimet)

print("\nTehdään tyhjä lista")
toinennimilista = [] # tehdään tyhjä lista
print("toinen nimilista, jossa alkiot 2 ja 3")
toinennimilista = nimet[2:4] #viedään toiseen listaan nimet
print(toinennimilista)

print("\nTyhjennetään toinennimilista-lista")
toinennimilista.clear()
print(toinennimilista)

#On huomattava että kun listaa järjestellään niin alkuperäinen järjestys menetetään

print("\nLajitellaan nimet -lista sort() -funktiolla")
nimet.sort()
print(nimet)

#Jos halutaan että nyt lajiteltu järjestys säilyy, niin muodostetaan uusi lista
print("\nJos halutaan että nyt lajiteltu järjestys säilyy, niin muodostetaan uusi lista")
kopio = list(nimet) #muodostetaan uusi lista
kopio.reverse() #lista käännetään
print("\nAlkuperäinen, järjestetty lista")
print(nimet)
print("\nKäännetty, lajiteltu lista")
print(kopio)

print("\nTyhjennetään kopio -lista")
kopio.clear() #Listan tyhjennys
print(kopio)

print("\nLista käydään läpi alkio kerrallaan")
for nimi in nimet:
    print(nimi)

print("\nLista käydään läpi indeksien avulla")
for i in range(len(nimet)):
    print(nimet[i])