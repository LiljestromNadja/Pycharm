"""
Teema 4 funktiot osa 2
h3

Lue arvosanoja Lue -funktiossa ja talleta ne listaan. Arvosana < 0 lopettaa syötön. Palauta arvosanat pääohjelmaan.
Laske arvosanojen keskiarvo ja hylättyjen määrä (arvosana == 0) Laske-funktiossa ja palauta ne tiedot pääohjelmaan (listassa).
Tulosta arvosanojen määrä, hylättyjen määrä ja keskiarvo Tulosta -funktiossa.
"""

def lue_arvosanat():
    arvosanat = []

    while True:
        arvosana = int(input("Anna arvosana: "))
        if arvosana < 0:
            break
        arvosanat.append(arvosana)

    return arvosanat # palautetaan lista jossa arvosanat

def laske_keskiarvo_ja_hylatyt(arvosanat): #Funktiossa käydään lista arvosanat läpi ja lasketaan hylätyt sekä arvosanojen keskiarvo
    hylatyt = 0
    summa = 0 # Summan voi toki laskea suoraan sum -funktiolla sum(arvosanat)
    for arvosana in arvosanat:
        if arvosana == 0:
            hylatyt += 1
        summa += arvosana

    keskiarvo = summa / len(arvosanat)
    return [keskiarvo, hylatyt] # tarvitaan lista, koska kaksi palautuvaa arvoa

def tulosta(lkm, hylatyt, keskiarvo): # parametrit voisi toki välittää listassakin
    print("Arvosanoja oli:", lkm)
    print("Hylättyjä oli:", hylatyt)
    print("Keskiarvo oli:", keskiarvo)

arvosanat = lue_arvosanat()
keskiarvojahylatyt = laske_keskiarvo_ja_hylatyt(arvosanat)
tulosta(len(arvosanat), keskiarvojahylatyt[1], keskiarvojahylatyt[0])
