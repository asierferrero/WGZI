from hasieratzea import taulak_sortu, datuak_hasieratu
from ezabatzea import taulak_ezabatu, datuak_ezabatu
from ikasleaGehitu import ikasleaGehitu

dbConnect = {
    'host': "localhost",
    'user': "root",
    'password': "",
    'database': "ikastetxea"
}

taulak_sortu(dbConnect)
datuak_hasieratu(dbConnect)
print("Taulak eta datuak sortu dira.")

def menu():
    print("1. Ikasle berri bat gehitu")
    print("2. Bukatu")

menu()
option = int(input("Sartu aukera: "))

while option != 2:
    if option == 1:
        ikasleaGehitu(dbConnect)
        print("Ikaslea gehitu da.")
    else:
        print("Aukera baliogabea, saiatu berriro.")

    menu()
    option = int(input("Sartu aukera: "))

erantzuna = int(input("Taulak eta datuak ezabatu nahi dituzu? (Y/N)"))

if erantzuna == 'y':
    datuak_ezabatu(dbConnect)
    taulak_ezabatu(dbConnect)
    print("Taulak eta datuak ezabatu dira.")

