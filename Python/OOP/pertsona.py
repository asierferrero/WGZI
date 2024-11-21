class Pertsona:
    def __init__(self, izena, adina):
        if not isinstance(izena, str):
            raise ValueError("Izena string bat izan behar da")
        if not isinstance(adina, int):
            raise ValueError("Adina zenbaki bat izan behar da")
        self.izena = izena
        self.adina = adina

    def adinNagusikoa(self):
        if self.adina > 18:
            print(f"{self.izena} adina nagusikoa da, {self.adina} urte ditu")
        else:
            print(f"{self.izena} ez da adin nagusikoa, {self.adina} urte ditu")
            
pertsona = Pertsona("Asier", 19)
pertsona.adinNagusikoa()