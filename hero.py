class Hero:
    def __init__(self, name:str, lvl:int, location :str= "Domov"):
        self.name = name
        self.lvl = lvl
        self.location = location
        pass

    def pokřik(self):
        return "Do boje!"

    def predstavse(self):
        return f"Ahoj jmenuji se {self.name}"

    def kde_jsi(self):
        return f"Jsem {self.location}"

    def presunse(self, nLoc):
        self.location = nLoc
        return f"presunul jsi se na {nLoc}"

hero1 = Hero("Batman", 10)
hero2 = Hero("Superman", 20)
hero3 = Hero("Spiderman", 15)
hero4 = Hero("Thor", 25)
hero5 = Hero("Hulk", 30)

print(hero1.pokřik())
print(hero1.predstavse())
print(hero1.kde_jsi())
print(hero1.presunse("Gotham"))

print(hero2.pokřik())
print(hero2.predstavse())
print(hero2.kde_jsi())
print(hero2.presunse("Metropolis"))

print(hero3.pokřik())
print(hero3.predstavse())
print(hero3.kde_jsi())
print(hero3.presunse("New York"))

print(hero4.pokřik())
print(hero4.predstavse())
print(hero4.kde_jsi())
print(hero4.presunse("Asgard"))

print(hero5.pokřik())
print(hero5.predstavse())
print(hero5.kde_jsi())
print(hero5.presunse("New York"))