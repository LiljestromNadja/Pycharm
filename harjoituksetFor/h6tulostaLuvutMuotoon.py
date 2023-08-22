"""Teema 2 - FOR
h6
Tulosta for -silmukassa seuraavasti:
1
    2
        3
            4
                5
                    6
                        7"""

for luku in range(0, 7):
    for tyhjia in range(1,luku +1):
        print(" ", end="")
    print(luku + 1)