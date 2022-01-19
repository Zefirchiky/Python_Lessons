class Shop():
    def __init__(self, name, _type):
        self.name=name
        self.type=_type
        self.number_of_units=0
    def describe_shop(self):
        print(f"Name: {self.name}, type: {self.type}")
    def open_shop(self):
        print("Store open")
    def set_number_of_units(self, m):
        self.number_of_units=m
    def increment_number_of_units(self, n):
        self.number_of_units+=n

class Discount(Shop):
    def __init__(self, name, _type, discount_products):
        super().__init__(name, _type)
        self.discount_products=discount_products
    def get_discount_products(self):
        print(self.discount_products)

store = Shop("Kek", "IDN")
print(store.name)
print(store.type)
store.describe_shop()
store.open_shop()
print(store.number_of_units)
store.number_of_units=35
print(store.number_of_units)
store.set_number_of_units(60)
print(store.number_of_units)
store.increment_number_of_units(20)
print(store.number_of_units)

store2 = Shop("Kek2", "IDN2")
store2.describe_shop()

store_discount = Discount("Discount Kek", "Discount IDN", "sdjfhjl")
store_discount.get_discount_products()
