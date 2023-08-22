"""
teema 2
h5
Tee ohjelma, joka lukee henkilön iän ja toimii seuraavasti:

jos ikä < 6 , niin tulostetaan "OLETPAS SINÄ NUORI JA TERÄVÄ"
jos ikä > 6 ja ikä <= 80 , niin tulostetaan "SUJUUHAN SE OHJELMOINTI SINULTAKIN"
jos ikä > 80 , niin tulostetaan "OLET IKÄÄSI NÄHDEN TAITAVA OHJELMOIMAAN"
"""

ika = int(input("Anna ikäsi:  "))

if(ika < 6):
    print("Oletpas sinä nuori ja terävä!")
elif(ika >= 6 and ika <= 80):
    print("Sujuuhan se ohjelmointi sinultakin!")
else:
    print("Olet ikääsi nähden taitava ohjelmoimaan!")
