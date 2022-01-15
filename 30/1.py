class Car:
    def __init__(self, car_mark, car_model, car_year):
        self.car_mark=car_mark
        self.car_model=car_model
        self.car_year=car_year
        self.car_adometr=0
    def get_discript_name(self):
        print(f"Mark: {self.car_mark}, Model: {self.car_model}, Year: {self.car_year}")
    def read_adometr(self):
        print(f"Adometr: {self.car_adometr}")
    def update_adometr(self, n):
        if n>self.car_adometr:
            self.car_adometr=n
        else:
            print("Izmen nelzya")
    def inkriment_adometr(self, p):
        self.car_adometr+=p
        print(f"Teper adometr: {self.car_adometr}")

class Electrocar(Car):
    def __init__(self, car_mark, car_model, car_year, batary):
        super().__init__(car_mark, car_model, car_year)
        self.batary=batary
    def name_electrocar(self):
        print(f"Mark: {self.car_mark}, Model: {self.car_model}, Year: {self.car_year}, Batary: {self.batary}")
    def new_batary(self,bat):
        self.batary=bat

#my_now_car = Car("Audi", "R8", 2010)
#my_now_car.get_discript_name()
#my_now_car.car_adometr=23
#my_now_car.update_adometr(int(input("Adometr: ")))
#my_now_car.read_adometr()
#my_now_car.inkriment_adometr(int(input("+adometr:")))

car2 = Electrocar("Tesla", "X", 2021, 1000)
car2.new_batary(int(input("Model batary: ")))
car2.name_electrocar()

