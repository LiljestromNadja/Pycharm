"""
Vakiot enum-tyyppisenä
"""

from enum import Enum
class Viikonpaiva(Enum):
    MAANANTAI = 1
    TIISTAI = 2
    KESKIVIIKKO = 3
    TORSTAI = 4
    PERJANTAI = 5
    LAUANTAI = 6
    SUNNUNTAI = 7

print(Viikonpaiva(2))
print(Viikonpaiva.TORSTAI)

for viikonpaiva in Viikonpaiva:
    print(viikonpaiva)