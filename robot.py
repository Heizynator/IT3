class Robot:
    def __init__(self, oznaceni:str, baterie:str, ukol:str = "pracuju"):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        pass

    def zvuk(self):
        return "MUHAW"

    def diagnostika(self, oznaceni, baterie):
        return f"Označení {oznaceni} a stav baterie: {baterie}"

    def aktivni_ukol(self, ukol):
        return f"Právě děláte {ukol}"

    def zadej_ukol(self,nUkol):
        self.ukol = nUkol
        return f"Máte nový úkol! {nUkol}"

robot1 = Robot("R2D2", "100%")
robot2 = Robot("T-800", "80%")
robot3 = Robot("C3PO", "60%")
robot4 = Robot("Wall-E", "90%")
robot5 = Robot("Optimus", "75%")

print(robot1.zvuk())
print(robot1.diagnostika(robot1.oznaceni, robot1.baterie))
print(robot1.aktivni_ukol(robot1.ukol))
print(robot1.zadej_ukol("opravit stroj"))

print(robot2.zvuk())
print(robot2.diagnostika(robot2.oznaceni, robot2.baterie))
print(robot2.aktivni_ukol(robot2.ukol))
print(robot2.zadej_ukol("hlídat sklad"))

print(robot3.zvuk())
print(robot3.diagnostika(robot3.oznaceni, robot3.baterie))
print(robot3.aktivni_ukol(robot3.ukol))
print(robot3.zadej_ukol("uklidit místnost"))

print(robot4.zvuk())
print(robot4.diagnostika(robot4.oznaceni, robot4.baterie))
print(robot4.aktivni_ukol(robot4.ukol))
print(robot4.zadej_ukol("sbírat odpadky"))

print(robot5.zvuk())
print(robot5.diagnostika(robot5.oznaceni, robot5.baterie))
print(robot5.aktivni_ukol(robot5.ukol))
print(robot5.zadej_ukol("chránit město"))