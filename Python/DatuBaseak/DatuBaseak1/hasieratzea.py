import mysql.connector

def taulak_sortu(dbConnect):
    konexioa = mysql.connector.connect(**dbConnect)
    kurtsorea = konexioa.cursor()

    kurtsorea.execute('''
        CREATE TABLE IF NOT EXISTS Ikasleak (
            ikasle_kodea INT PRIMARY KEY,
            izena VARCHAR(50),
            abizena VARCHAR(50)
        )
    ''')

    kurtsorea.execute('''
        CREATE TABLE IF NOT EXISTS Ikasgaiak (
            ikasgai_kodea INT PRIMARY KEY,
            izena VARCHAR(50),
            maila VARCHAR(20),
            hizkuntza VARCHAR(20)
        )
    ''')

    kurtsorea.execute('''
        CREATE TABLE IF NOT EXISTS Notak (
            nota FLOAT NOT NULL,
            oharra VARCHAR(100),
            ikasgai_kodea INT,
            ikasle_kodea INT,
            FOREIGN KEY (ikasgai_kodea) REFERENCES Ikasgaiak(ikasgai_kodea),
            FOREIGN KEY (ikasle_kodea) REFERENCES Ikasleak(ikasle_kodea)
        )
    ''')

    konexioa.commit()
    kurtsorea.close()
    konexioa.close()

def datuak_hasieratu(dbConnect):
    konexioa = mysql.connector.connect(**dbConnect)
    kurtsorea = konexioa.cursor()

    kurtsorea.execute("INSERT INTO Ikasleak VALUES (1, 'Asier', 'Ferrero')")
    kurtsorea.execute("INSERT INTO Ikasleak VALUES (2, 'Aritz', 'Arruabarrena')")

    kurtsorea.execute("INSERT INTO Ikasgaiak VALUES (1, 'Web Garapena Zerbitzarian', 2, 'Euskara')")
    kurtsorea.execute("INSERT INTO Ikasgaiak VALUES (2, 'Web Garapena Bezeroan', 2, 'Euskara')")

    kurtsorea.execute("INSERT INTO Notak VALUES (8, 'Oso ongi', 1, 1)")
    kurtsorea.execute("INSERT INTO Notak VALUES (10, 'Bikain', 2, 2)")

    konexioa.commit()
    kurtsorea.close()
    konexioa.close()