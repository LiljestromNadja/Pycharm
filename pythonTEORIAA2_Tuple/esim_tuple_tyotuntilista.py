"""  """

viikonpaivat = ("MA", "TI", "KE", "TO", "PE", "LA", "SU")
tyotunnit = (8, 9, 10, 11, 12, 13, 14, 15, 16)  # alkavat täydet tunnit

# Generoidaan kaksiuloitteinen lista, jossa tehtävät tunneittain
# Sisempi indeksi on viikonpäivä, ja ulompi tuntiaika

tehtavat = [["Vapaa" for x in range(len(viikonpaivat))] for x in range(len(tyotunnit))]
tehtavat[0][0] = "palis"    # ma klo 8 palaveri
tehtavat[4][4] = "Tiimi"    # pe klo 12 tiimikokous

print("\t")
for vkpv in viikonpaivat:
    print("\t" + vkpv + "\t", end="")
print()

for i in range(len(tyotunnit)):
    print(tyotunnit[i], end="")
    for j in range(len(viikonpaivat)):
        print("\t" + tehtavat[i][j], end="")
    print()