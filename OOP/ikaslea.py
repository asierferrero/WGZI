class Ikaslea:
    def __init__(self, izena, nota):
        if not isinstance(izena, str):
            raise ValueError("Izena string bat izan behar da")
        if not isinstance(nota, (int, float)):
            raise ValueError("Nota zenbaki bat izan behar da")
        self.izena = izena
        self.nota = nota
        
    def inprimatu(self):
        print(f"{self.izena} ikaslearen nota: {self.nota}")
    
ikaslea = Ikaslea("Asier", "g")
ikaslea.inprimatu()