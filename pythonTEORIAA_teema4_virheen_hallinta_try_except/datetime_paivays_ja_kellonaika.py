#esimerkki

import datetime

#paivays = datetime.datetime(2022, 21, 5) #Tämä kaatuu koska 21 ei kelpaa kuukaudeksi (yyyy, mm, dd)

#nyt ei kaadu vaan tuottaa ilmoituksen
try:
    paivays = datetime.datetime(2022, 21,5)
except:
    print("Päiväys väärin")
    paivays = datetime.datetime(2000, 1, 1)
else:
    print("Päiväys ok.")
finally:
    print("Tänään", datetime.date.today())

    now = datetime.datetime.now()
    print("Current date and time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))