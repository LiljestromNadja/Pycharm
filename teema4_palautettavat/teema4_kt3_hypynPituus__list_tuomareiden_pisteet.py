"""
KT3
Tee ohjelma, joka laskee mäkihyppääjän yhden kierroksen suorituspisteet. Ensin ohjelma kysyy hypyn pituuden (liukuluku 0.5 metrin välein) jonka jälkeen se kysyy viiden arvostelutuomarin tyylipisteet (0-20 välillä 0.5 välein eli esim. 16.5 tai 17.0 tai 18.5). Hyppääjän pisteet muodostuvat kaavasta.

pisteet = (hypyn pituus - kriittinen piste) * 1.8 + kolmen keskimmäisen tuomarin tyylipisteet + 60.

Tyylipisteissä siis parhain ja huonoin pistemäärä tipahtaa pois.

Ohjelman hyppyrimäen kriittinen piste on 90 metrin kohdalla. Laita kriittinen piste globaaliin vakioon KR_PISTE. Tulosta lopuksi hypyn pituus ja hypyn pisteet. Käytä ohjelmassa funktioita:


KysyHypynPituus - Kysyy hypyn pituuden ja palauttaa sen reaalilukuna
KysyTuomareidenPisteet - Kysyy tuomareiden pisteet yksi kerrallaan. Palauttaa listan jossa on kunkin tuomarin antamat pisteet reaalilukuina.
LaskeHypynPisteet - Saa ensimmäisenä parametrina hypyn pituuden sekä toisena parametrina listan joka sisältää kaikkien tuomareiden antamat tyylipisteet. Palauttaa hypyn pisteet lukuna.


"""
# Write functions and define global variables here!

KR_PISTE = 90

#KysyHypynPituus - Kysyy hypyn pituuden ja palauttaa sen reaalilukuna
def KysyHypynPituus():
    hypynPituus = float(input("Anna hypyn pituus: "))
    return hypynPituus

#KysyTuomareidenPisteet - Kysyy tuomareiden pisteet yksi kerrallaan. Palauttaa listan jossa on kunkin tuomarin antamat pisteet reaalilukuina.
def KysyTuomareidenPisteet():
    tuomareidenpisteet = []
    while len(tuomareidenpisteet) < 5:
        kysyPisteet = float(input("Anna pisteet 0.5:n välein väliltä 0-20: "))
        if kysyPisteet < 0 or kysyPisteet > 20:
            print("Anna pisteet väliltä 0-20!")
            continue
        else:
            tuomareidenpisteet.append(kysyPisteet)

    #for pisteet in tuomareidenpisteet:
        #print(pisteet) #testailua
    #yhteensa = sum(tuomareidenpisteet) # Lisää testailua
    #print(yhteensa) #testailua
    return tuomareidenpisteet

#LaskeHypynPisteet - Saa ensimmäisenä parametrina hypyn pituuden sekä toisena parametrina listan joka sisältää kaikkien tuomareiden antamat tyylipisteet.
# Palauttaa hypyn pisteet lukuna.

def LaskeHypynPisteet(hypynPituus, tuomareidenpisteet):
    tuomareidenpisteet.sort
    #print(tuomareidenpisteet[1], tuomareidenpisteet[2], tuomareidenpisteet[3], end="")#testailua
    pisteet = (hypynPituus - KR_PISTE) * 1.8 + (tuomareidenpisteet[1] + tuomareidenpisteet[2] + tuomareidenpisteet[3]) + 60
    #print("Kokonaispisteet:", pisteet)
    #print(tuomareidenpisteet) #testailua
    #for pisteet in tuomareidenpisteet: #testailua
        #print(pisteet, tuomareidenpisteet[0]) #Nämä kaksi ovat samat!
    return pisteet

if __name__ == "__main__":
# Write main program below this line

    hypynPituus = KysyHypynPituus()
    tuomareidenpisteet = KysyTuomareidenPisteet()
    pisteet = LaskeHypynPisteet(hypynPituus, tuomareidenpisteet)

    print(hypynPituus, pisteet)



