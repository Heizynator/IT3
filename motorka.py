class motorka:
    def __init__(self, znacka:str, kategorie:str, stav_nadrze:int = 20):
        self.znacka = znacka
        self.kategorie = kategorie
        self.stav_nadrze = stav_nadrze
        pass

    def stav_stojánku(self):
        self.stav_stojánku = "Dole"
        return f"Stojánek je {self.stav_stojánku}"

    def zatoc_plyn(self):
        return "VRRUUM"

    def popisMOTO(self):
        return f"{self.znacka}, {self.kategorie}, {self.stav_nadrze}"

    def popojed(self, palivo:str = 30):
        if palivo >= self.stav_nadrze:
            return f"Jdi natankovat, nemáš dostatek paliva, chybí ti {(palivo-self.stav_nadrze)}"
        else:
            self.stav_nadrze -= palivo
            return f"Využil jste {palivo}, váš nový stav paliva je {self.stav_nadrze}"
    
    def natankuj(self,stav_nadrze):
        self.stav_nadrze += (100-stav_nadrze)
        return("Máte natankováno naplno.")

    def stojanek_navic(self):

        if self.stav_stojánku == "Dole":
            self.stav_stojánku = "Zvednutej"
            return "Zvednutej"
        else:
            self.stav_stojánku = "Dole"
            return "Dole"
    
moto1 = motorka("Honda", "Sport")
moto2 = motorka("Yamaha", "Cross")
moto3 = motorka("Kawasaki", "Naked")
moto4 = motorka("BMW", "Touring")
moto5 = motorka("Ducati", "Sport")

print(moto1.stav_stojánku())
print(moto1.zatoc_plyn())
print(moto1.popisMOTO())
print(moto1.popojed())
print(moto1.natankuj(moto1.stav_nadrze))
print(moto1.stojanek_navic())
print(moto1.stojanek_navic())
print(moto1.stojanek_navic())
print(moto1.stojanek_navic())