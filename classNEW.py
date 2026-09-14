class Zvire:
    def __init__(self, name:str, age:int, misto:str = "bouda"):
        self.name = name
        self.age = age
        self.misto = misto 

    def zvuk(self):
        return "???"

    def predstavse(self):
        return f"Jsem {self.name} a je mi {self.age}"




zvire = Zvire("Ludek", 13)
zvire1 = Zvire("Pepa", 18, "Domov")

print(zvire1.name)
print(zvire1.age)
print(zvire1.predstavse())
