"""IF-ELSE"""

ekaluku = int(input("Anna eka luku: "))
tokaluku = int(input("Anna toka luku: "))

summa = ekaluku + tokaluku
tulo = ekaluku * tokaluku

# summa
if(summa >= 100):
    print("Lukujen summa on suurempi tai yhtä suuri kuin 100, yhteensä", summa)
else:
    print("Lukujen summa on alle 100, yhteensä", summa)

# tulo
if(tulo >= 100):
    print("Lukujen tulo on suurempi tai yhtä suuri kuin 100, yhteensä", tulo) #Tässä If-lohkossa on kaksi lausetta
    print("Lukujen tulo on aina suurempi kuin lukujen summa.")
else:
    print("Lukujen tulo on alle 100, yhteensä", tulo) # Tässä else-lohkossa on kaksi lausetta
    print("Kuinka sujuu kertotaulu?")