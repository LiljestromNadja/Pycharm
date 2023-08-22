"""
teema 2 ehdollinen operaattori ja vakiot
h6
Kysy käyttäjältä väsyttääkö k/e merkkijonotyyppiseen muuttujaan.. Jos käyttäjä vastasi "k", niin tulosta "kohta loppuu"
Jos käyttäjä vastasi "e" niin tulosta "hyvä"

Kun saat nuo toimimaan, niin lisää iso "K" ja "E", "kyllä", "KYLLÄ", "ei" ja "EI" mukaan hyväksyttyihin tapauksiin.
Jos mikään noista ei täsmää, niin tulosta teksti "Vastaus ei kelpaa"
Käytä switch-case tyyppistä rakennetta.
"""

vasyttaako = input("Väsyttääkö? k/e ")
vasyttaako = vasyttaako.strip()

# Luodaan lista vastausvaihtoehdoille
vastaukset = {"k": "Kohta loppuu..", "K": "Kohta loppuu..", "kyllä": "Kohta loppuu..", "KYLLÄ": "Kohta loppuu..",
              "e": "Hyvä!", "E": "Hyvä!", "ei": "Hyvä!", "EI": "Hyvä!"}

tulostettava = vastaukset.get(vasyttaako, "Vastaus ei kelpaa")
#Luodaan muuttuja (tulostettava) vastaukselle,
#etsitään get() -funktiolla vastaukset-listasta käyttäjän syöte (vasyttaako),
#jos sitä ei löydy, tulostetaan "Vastaus ei kelpaa"


# Muistetaan tulostaa vastaus
print(tulostettava)
