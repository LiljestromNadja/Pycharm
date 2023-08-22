print("Alkaa tästä ", end='')
print("Tulee edellisen rivin perään")
print("Rivinvaihto", "aina", sep=" ")
print("rivinvaihto", "aina")
print("kenomerkin tulostus \\")
print("\\Keno \tabulointi \nUusi rivi ")

arvo = 10
toinenArvo = 99.99
print(arvo, "ja",  toinenArvo)
print("Arvo = " + str(arvo))
print("Arvo = ", arvo)
print("Arvo = ", f"{arvo:10d}")
print(toinenArvo)
print("Toinen arvo= ", f"{toinenArvo:10.4f}")
toinenArvo = toinenArvo + 2.003
print(toinenArvo)
a = toinenArvo
print(a)
print("toinen arvo = ", "{:13.1f}")
if(toinenArvo < 200):
    print("hei")
from datetime import date
nyt = date.today()
print(nyt)

annaIka = input("Anna ikäsi: ")
ika = int(annaIka)
print("Olet syntynyt vuonna ", nyt.year-ika)


#ika = int(input("Anna ikä: "))
#paino = float(input("Anna paino: "))

#print("\n")
#print("Henkilön tiedot: ")
#print("\tikä \tpaino")

#print("\t", f"{ika: d}", "\t", f"{paino: 4.2f}")

mjono = "Tässäpä tämä taas"
print(mjono)