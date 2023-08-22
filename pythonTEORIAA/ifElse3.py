"""IF-ELSE"""

vastaus = input("Onko ohjelmointi kivaa? k/e  ")
vastaus = vastaus.upper() # Muutetaan käyttäjän syöte isoiksi, joten sillä ei ole väliä syöttääkö käyttäjä tekstin isolla vai pienellä

if(vastaus == "K"):
    print("Mahtavaa, olet siis oikealla kurssilla!")
else:
    print("Harmi, koeta kuitenkin löytää koodaamisen into.")

vastaus2 = input("Onko materiaaleista ollut apua? kyllä/ei  ")
vastaus2 =vastaus2.upper() # Muutetaan taas käyttäjän syöte isoksi

if(vastaus2 == "KYLLÄ"):
    print("Hieno juttu!")
    print("Onhan tässä materiaalia tuotettukin!")
else:
    print("Kurja, jos materiaaleista ei ole ollut hyötyä.")
    print("Kerro, mitä haluaisit muutettavan, ja muista GOOGLE!")

