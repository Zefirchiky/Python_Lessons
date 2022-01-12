class Human:
    def __init__(self,name,surname,bir,yob):
        self.name=name
        self.surname=surname
        self.placeofbirth=bir
        self.yearofbith=yob
    def hello(self):
        print(f"{self.name} seys hello")
    def info_age(self,years):
        return years-self.yearofbith
p1 = Human("Artem", "Mudruk", "Ua", 2006)
p1.hello()
print(p1.info_age(2022))
