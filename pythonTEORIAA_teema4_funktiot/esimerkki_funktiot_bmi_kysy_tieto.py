def laske_bmi(pituus, paino):
    bmi = paino / (pituus ** 2) #laskee painoindeksin
    return bmi

def tulosta_bmi(nimi, bmi):
    print("Hei {0}, sinun BMI on {1:.2f}".format(nimi, bmi))

def kysy_tieto(tieto):
    vastaus = input("Anna {0}:".format(tieto))
    return vastaus

nimi = kysy_tieto("nimi") #kutsutaan samaa funktiota kolmesti
pituus = float(kysy_tieto("pituus metreinä"))
paino = float(kysy_tieto("paino"))
bmi = laske_bmi(pituus, paino)
tulosta_bmi(nimi, bmi)