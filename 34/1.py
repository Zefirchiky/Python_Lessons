class Animal:
    def __init__(self, vid):
        self.species=vid
    def info(self):
        print(self.species)
    def zvuk(self):
        if self.species=="Cat":
            print("Meaw")
        elif self.species=="Dog":
            print("Gav")
        else:
            print("No animal in dictionary")

class Dog(Animal):
    def __init__(self):
        self.species="Dog"
    def zvuk(self):
        print("Gav")

class Cat(Animal):
    def __init__(self):
        self.species="Cat"
    def zvuk(self):
        print("Meaw")

def show_animal_info(a):
    if a.species=="Cat" or a.species=="Dog":
        a.info()
        a.zvuk()
    else:
        print("Book this is not an animal")

a1 = Animal("lll")
a1.info()
a1.zvuk()

a2 = Dog()
show_animal_info(a2)

a3 = Cat()
show_animal_info(a3)
