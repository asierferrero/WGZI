import mysql.connector

dbConnect = {
    'host': "localhost",
    'user': "root",
    'password': "",
    'database': "denda"
}

konexioa = mysql.connector.connect(dbConnect)
kurtsorea = konexioa.cursor()

kurtsorea.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            CodCliente INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(100) NOT NULL,
            Apellidos VARCHAR(100) NOT NULL,
            Empresa VARCHAR(100),
            Puesto VARCHAR(50),
            CP VARCHAR(10) DEFAULT '20600',
            Provincia VARCHAR(50) DEFAULT 'Eibar',
            Telefono VARCHAR(15),                        
            FechaNacimiento DATE                        
    ''')

kurtsorea.execute('''
        CREATE TABLE ARTICULOS (
            CodArticulo INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(100) NOT NULL,
            Descripcion TEXT NOT NULL,
            Precio DECIMAL(10, 2) NOT NULL,
            UnidadesEnStock INT DEFAULT 0,
            StockDeSeguridad INT DEFAULT 0,
            Imagen VARCHAR(255)
    ''')

kurtsorea.execute('''
        CREATE TABLE COMPRA (
            CodCliente INT,
            CodArticulo INT,
            Fecha DATE DEFAULT CURRENT_DATE,
            Unidades INT NOT NULL,
            PRIMARY KEY (CodCliente, CodArticulo, Fecha),
            FOREIGN KEY (CodCliente) REFERENCES CLIENTES(CodCliente)
                ON DELETE CASCADE,
            FOREIGN KEY (CodArticulo) REFERENCES ARTICULOS(CodArticulo)
                ON DELETE CASCADE
    ''')

konexioa.commit()
kurtsorea.close()
konexioa.close()
