"""Set, {}

- Set on joukko alkioita ja on järjestämätön ja ei ole indeksoitavissa. Ei salli samaa arvoa kahteen kertaan
- Tässäkin tapauksessa toki ratkaisut voidaan aina toteuttaa listalla, mutta joihinkin tilanteisiin set on parempi
ja "suojatumpi", koska sama arvo ei voi olla siinä kahteen kekrtaan. Ei sovi tilanteisiin, joissa järjestyksellä
on väliä
- Setistä voi tavallisen listan tapaan tehdä uusia listoja, ja listoista settejä
- Esim.
    nimet = {"Kalle", "Ville", "Mikko", "Jaana", "Katariina"}
    arvot = set() # tyhjä lista
- Setin alkioiden läpikäynti samaan tapaan kuin listalla. Onko kuitenkaan tarvetta? Indeksiin perustuva läpikäynti ei
onnistu
- Settiä käytetään siis listoissa, joihin laitetaan arvoja talteen ilman että sama arvo voi olla tuplana
- Setille voidaan tehdä tyypillisiä joukko-operaattioita eli yhdistää listoja siten, että esim duplikaatit poistuvat,
duplikaatit eivät tule mukaan, vain duplikaatit tulevat jne"""

nimet = {"Hanna", "Janne"}  # Luodaan set
nimi = input("Annapa nimi: ")
if nimi in nimet:   # Tsekataan onko listassa
    print("Nimi on jo listassa!")
else:
    nimet.add(nimi)
for n in nimet:     # Tulostetaan set
    print(n)
nimet.add(nimi)  # Ei kaadu mutta ei lisää duplikaattia
print(nimet)

toisetNimet = {"Hanna", "Jarkko"}

yhdistetty1 = nimet.union(toisetNimet)  # Yhdistää listat
print(yhdistetty1)

yhdistetty2 = nimet.intersection(toisetNimet)   # Yhdistää listat mutta vain duplikaatit, eli vain ne nimet jotka ovat molemmissa listoissa
print(yhdistetty2)

yhdistetty3 = nimet.difference(toisetNimet)  # Yhdistää listat, vain ei-duplikaatit, eli vain ne nimet joita ei ole toisessa listassa
print(yhdistetty3)
