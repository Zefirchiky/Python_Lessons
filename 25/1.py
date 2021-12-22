x = int(input("Years:"))
class Human:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("User created")
    def kek(self):
        print(f"{self.name} {self.surname} {self.age} {self.years()}")
    def years(self):
        return x-self.age

p1 = Human("Artem","Mudruk",15)
p2 = Human("Den","Dmiriev",5)
#p1.name="Artem"
#p1.surname="Mudruk"
#p1.playsofbeard="Muxosransk"
#p1.age=15
p1.kek()
p2.kek()

