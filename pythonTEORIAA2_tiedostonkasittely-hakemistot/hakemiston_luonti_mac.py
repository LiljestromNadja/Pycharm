"""
- On huomattava että hakemistojen käsittelyperiaatteet vaihtelevat käyttöjärjestelmittäin!
- Tässä hakemiston luonti (mac -kone)"""

import os

#Luotava hakemisto
directory = "MyTempFiles"

#Hakemisto jonka alle luotava tulee. Huom! Mac-kone
parent_dir = "/tmp/"

#Yhdistetään polku
path = os.path.join(parent_dir, directory)

#Luodaan nyt hakemisto jos sitä ei ole
if not os.path.exists(path):
    os.mkdir(path)
    print("Hakemisto", path, "nyt luotu")
else:
    print("Hakemisto", path, "on jo olemassa")
