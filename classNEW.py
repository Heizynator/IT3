class Zvire:
    def __init__(self, name:str, age:int, misto:str = "bouda"):
        self.name = name
        self.age = age
        self.misto = misto 


    def zvuk(self):
        return "???"

    def predstavse(self):
        return f"Jsem {self.name} a je mi {self.age}"

    def kdejsi(self):
        return f"Jsem v místě {self.misto}"

    def jditam(self, nMisto:str):
        self.misto = nMisto
        return f"Přesunul jsem se na {nMisto}. {self.kdejsi()}"
    
zvire = Zvire("Ludek", 13)
zvire1 = Zvire("Pepa", 18, "Domov")

print(zvire1.name)
print(zvire1.age)
print(zvire1.predstavse())
print(zvire1.kdejsi())
print(zvire1.jditam("Skola"))
