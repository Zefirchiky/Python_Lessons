import Restaurant
import Admin
import User

class IceCreamStand(Restaurant.Restaurant):
    def __init__(self,a,b,sorts):
        super().__init__(a,b)
        self.flavors=sorts
    def all_sorts(self):
        print(self.flavors)

R1 = Restaurant.Restaurant("Vui", "Fast-food")
R1.describe_restaurant()

R2 = Restaurant.Restaurant("Yeay", "Exclusive")
R2.describe_restaurant()

R3 = Restaurant.Restaurant("Vshux", "Homy")
R3.describe_restaurant()

U1 = User.User("Name1", "Surname1", 4)
U1.describe_user()
U1.greet_user()

U2 = User.User("Name2", "Surname2", 55)
U2.describe_user()
U2.greet_user()

U3 = User.User("Name3", "Surname3", 666)
U3.increment_login_attemts()
U3.increment_login_attemts()
U3.increment_login_attemts()
print(U3.login_attemts)
U3.reset_login_attemts()
print(U3.login_attemts)

restauran = Restaurant.Restaurant("Yes","I'm")
print(restauran.number_served)
restauran.number_served=5
print(restauran.number_served)
restauran.set_number_served(100)
print(restauran.number_served)
restauran.increment_number_served(399)

IceCreamStand = IceCreamStand("I","pizza",["banan","plombir"])
IceCreamStand.all_sorts()

A1 = Admin.Admin("Name4", "Surname4", 7777, ["Ban","Kik","Mute"])
A1.pr.show_privileges()
