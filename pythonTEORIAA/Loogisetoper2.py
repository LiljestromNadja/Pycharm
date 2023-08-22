"""
Loogiset operaattorit - sulkuparit

Sulkupareilla voi luonnollisesti selventää loogisia lausekkeita
"""

luku1 = 1
luku2 = 2

# AND -koko ehto on tosi jos molemmat ovat tosia
if(luku1 > 0 and luku2 < 0):
    print("Luku1 on suurempi kuin nolla JA luku2 on pienempi kuin nolla.")

#(sisäehto) OR (sisäehto) -koko ehto on tosi jos jompi kumpi sisäehdoista on tosi
if((luku1 > 0 and luku1 < 5) or (luku2 > 0 and luku2 < 5)):
    print("(\nsisäehto 1 \n(luku1 on suurempi kuin nolla JA luku1 on pienempi kuin 5) "
          "\nTAI sisäehto 2 \n(luku2 on suurempi kuin nolla JA luku2 on pienempi kuin 5)\n) ")

#(sisäehto) AND (sisäehto) -koko ehto on tosi jos molemmat sisäehdot ovat tosia

if(not(luku1 == 0) and (luku2 < 0 or luku2 >= 100)):
    print("Sisäehto 1: jos luku1 on yhtäsuuri kuin nolla \n"
          "JA\n"
          "sisäehto 2 \n"
          "luku2 on pienempi kuin nolla tai luku2 on suurempi tai yhtäsuuri kuin 100")