"""
teema 2 ehdollinen operaattori ja vakiot
h4
Anna itsellesi arvosana 0-5 ohjelmoinnin osaamisesta tällä hetkellä
Jos arvosana oli suurempi tai yhtäkuin 3, niin tulostus -muuttuja saa arvokseen "hyvä homma"
Muussa tapauksessa tulostus -muuttuja saa arvokseen "lisää reeniä"
Käytä ehdollista operaattoria
Tulosta lopuksi tulostus -muuttujan arvo
"""

"""Opettajan ratkaisu :

taso = int(input("Anna ohjelmoinnin taso: "))

tulostus = "Hyvä homma! " if taso >= 3 else "Lisää reeniä.."
print(tulostus)"""

# Oma viritys vakion kanssa
def HYVA_HOMMA():
    return 3

arvosana = int(input("Anna itsellesi arvosana välillä 0-5: "))

tulostus = "Hyvä homma! " if arvosana >= HYVA_HOMMA() else "Lisää reeniä.."

print(tulostus)