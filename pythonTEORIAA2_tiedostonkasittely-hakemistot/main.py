"""
Tiedostonkäsittely -hakemistot

- Hakemistojen käsittelyyn tarvitaan os-moduuli
- Hakemistoja käsitellään samoin kuin tiedostoja

    import os
    directory_contents =os.listdir("/") # Juurihakemiston tiedostot

- Moduulin path -luokka on kätevä tsekattaessa hakemiston sisältöä
"""

import os

tiedostot = os.listdir("/") # Juurihakemiston tiedostot

print(os.path.abspath("/")) # Tulostetaan testimielessä juuren polku(mac -kone)
print(tiedostot) # Tulostetaan tiedot listasta

for tiedosto in tiedostot:
    if os.path.isdir(os.path.abspath("/") + tiedosto): # Jos kyseessä on hakemisto niin tulostetaan
        print(tiedosto)

for tiedosto in tiedostot:
    if os.path.isfile(os.path.abspath("/") + tiedosto):  # Jos kyseessä on tiedosto niin tulostetaan
        print(tiedosto)

if os.path.exists("./main.py"): # Tsekataan onko tiedosto ajohakemistossa
    print("Tiedosto löytyi")



