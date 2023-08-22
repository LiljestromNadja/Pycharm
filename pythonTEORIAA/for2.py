"""While + for + if yhdessä"""
print("While + for + if yhdessä")

# Pyydetään 12 kuukauden sadesummat
choices = {1: "tammikuu", 2: "helmikuu", 3: "maaliskuu", 4: "huhtikuu", 5: "toukokuu", 6: "kesäkuu", 7: "heinäkuu", 8: "elokuu", 9: "syyskuu", 10: "lokakuu", 11: "marraskuu", 12: "joulukuu"}

sadesummayht = 0

for a in range(1,13):
    kuukausi = choices.get(a, "Unknown")
    while True:
        try:
            print("Anna kuukauden", kuukausi, "sadesumma: ", end=' ')
            sadesumma = float(input())
            if(sadesumma >= 0 and sadesumma <10000):
                sadesummayht += sadesumma
                break
        except:
            pass # tyhjä lause

        #tänne tullaan aina, olipa arvoaluevirhe tai syöttövirhe
        print("Virhe syötteessä, anna uudelleen")

print("Sadesumma yhteensä vuodelle on: ", sadesummayht)