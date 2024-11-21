import mysql.connector

dbConnect = {
    'host': "localhost",
    'user': "root",
    'password': "",
    'database': "ikastetxea"
}

def taulak_ezabatu(dbConnect):
    konexioa = mysql.connector.connect(**dbConnect)
    kurtsorea = konexioa.cursor()

    kurtsorea.execute("DROP TABLE Ikasleak")
    kurtsorea.execute("DROP TABLE Ikasgaiak")
    kurtsorea.execute("DROP TABLE Notak")

    konexioa.commit()
    kurtsorea.close()
    konexioa.close()

def datuak_ezabatu(dbConnect):
    konexioa = mysql.connector.connect(**dbConnect)
    kurtsorea = konexioa.cursor()

    kurtsorea.execute("ALTER TABLE notak DROP FOREIGN KEY notak_ibfk_1")

    kurtsorea.execute("DELETE FROM Ikasleak")
    kurtsorea.execute("DELETE FROM Ikasgaiak")
    kurtsorea.execute("DELETE FROM Notak")

    konexioa.commit()
    kurtsorea.close()
    konexioa.close()