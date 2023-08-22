"""Teema 2 - FOR
h5
Lue käyttäjältä 5 kokonaislukua for -silmukassa väliltä 1-20. Luku on kysyttävä uudestaan jos se annettiin väärin.
Tulosta lopuksi pienin ja suurin syötetyistä luvuista. """

pienin = 21
suurin = 0

for monesko in range(1,6):
    while True:
        print("Anna", monesko, ".luku: ", end="")
        luku = int(input())
        if (luku >= 1) and (luku <=20):
            break
    pienin = luku if luku < pienin else pienin      #Muista sisennykset oikeaan kohtaan, muuten käy hassuja...
    suurin = luku if luku > suurin else luku

print("Pienin oli", pienin)
print("Suurin oli", suurin)