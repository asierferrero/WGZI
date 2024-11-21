class Kontaktoa:
    def __init__(self, izena, telefonoa, posta_elektronikoa):
        self.izena = izena
        self.telefonoa = telefonoa
        self.posta_elektronikoa = posta_elektronikoa

    def __str__(self):
        return f"{self.izena}: {self.telefonoa}, {self.posta_elektronikoa}"

class Agenda(Kontaktoa):
    def __init__(self):
        super().__init__("Agenda", "", "")
        self.kontaktuak = []

    def gehitu_kontaktoa(self, kontaktoa):
        self.kontaktuak.append(kontaktoa)

    def inprimatu_kontaktuak(self):
        for kontaktoa in self.kontaktuak:
            print(kontaktoa)

    def bilatu_kontaktoa(self, izena):
        for kontaktoa in self.kontaktuak:
            if kontaktoa.izena.lower() == izena.lower():
                return kontaktoa
        return None

    def editatu_kontaktoa(self, izena):
        kontaktoa = self.bilatu_kontaktoa(izena)
        if kontaktoa:
            print("Aukeratu atributua aldatzeko:")
            print("1. Izena")
            print("2. Telefonoa")
            print("3. Posta elektronikoa")
            aukera = input("Aukera: ")
            if aukera == "1":
                kontaktoa.izena = input("Sartu izen berria: ")
            elif aukera == "2":
                kontaktoa.telefonoa = input("Sartu telefonoa berria: ")
            elif aukera == "3":
                kontaktoa.posta_elektronikoa = input("Sartu posta elektronikoa berria: ")
            else:
                print("Aukera ez da baliozkoa.")
        else:
            print("Kontaktu hori ez dago agendan.")

def main():
    agenda = Agenda()
    while True:
        print("Agenda menua:")
        print("1. Gehitu kontaktua")
        print("2. Inprimatu harremanetarako zerrenda")
        print("3. Bilatu kontaktua")
        print("4. Editatu kontaktua")
        print("5. Irten")
        aukera = input("Aukera: ")
        if aukera == "1":
            izena = input("Sartu izena: ")
            telefonoa = input("Sartu telefonoa: ")
            posta_elektronikoa = input("Sartu posta elektronikoa: ")
            kontaktoa = Kontaktoa(izena, telefonoa, posta_elektronikoa)
            agenda.gehitu_kontaktoa(kontaktoa)
        elif aukera == "2":
            agenda.inprimatu_kontaktuak()
        elif aukera == "3":
            izena = input("Sartu izena bilatzeko: ")
            kontaktoa = agenda.bilatu_kontaktoa(izena)
            if kontaktoa:
                print(kontaktoa)
            else:
                print("Kontaktu hori ez dago agendan.")
        elif aukera == "4":
            izena = input("Sartu izena editatzeko: ")
            agenda.editatu_kontaktoa(izena)
        elif aukera == "5":
            break
        else:
            print("Aukera ez da baliozkoa.")

main()