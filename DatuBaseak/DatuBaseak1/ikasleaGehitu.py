import mysql.connector

def ikasleaGehitu(dbConnect):
    konexioa = mysql.connector.connect(**dbConnect)
    kurtsorea = konexioa.cursor()

    ikasle_kodea = int(input("Sartu ikaslearen kodea: "))
    izena = input("Sartu ikaslearen izena: ")
    abizena = input("Sartu ikaslearen abizena: ")

    values = (ikasle_kodea, izena, abizena)
    kurtsorea.execute("INSERT INTO ikasleak (ikasle_kodea, izena, abizena) VALUES (%s, %s, %s)", values)

    konexioa.commit()

    kurtsorea.close()
    konexioa.close()