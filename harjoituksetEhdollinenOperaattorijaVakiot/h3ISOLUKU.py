"""
teema 2 ehdollinen operaattori ja vakiot
h3
Lue käyttäjältä kokonaisluku. Jos annettu luku oli suurempi kuin 100, niin tulostus -muuttuja saa arvokseen tekstin
"iso luku", muussa tapauksessa se saa arvokseen "pieni luku"
Tulosta lopuksi tulosta -muuttujan arvo. Käytä ehdollista operaattoria if elsen sijaan. Arvo 100 on sijoitettu vakioon
ISO_LUKU
"""

def ISO_LUKU():
    return 100

luku = int(input("Anna kokonaisluku: "))

# EHDOLLINEN OPERAATTORI
# tulostus - muuttujaan tulee teksti iso luku jos luku on suurempi kuin 100 muuten siihen tulee teksti pieni luku
tulostus = "Iso luku" if luku > ISO_LUKU() else "Pieni luku"

print(tulostus)
