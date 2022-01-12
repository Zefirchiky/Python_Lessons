class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("person created")
    def hello(self):
        print(f"{self.name} says hello")
        
class Student(Human):
    def __init__(self, name, age, course, mark):
        Human.__init__(self,name,age)
        self.course=course
        self.mark=mark
    def hello(self):
        print(f"lalala {self.name}")
    def study(self):
        print(f"{self.name} - studing")
    def mark_1(self):
        print(f"Student {self.name}, study on {self.course} have mark {self.mark}")

class Teacher(Human):
    def teach(self):
        print(f"{self.name} - teach, age - {self.age}")

s1 = Student("Artem", 15, "XZ", 10)
#t1 = Teacher("Sasha", 16)
#s2 = Student("Vlad", 16)
#t2 = Teacher("Vova", 15)
#s1.hello()
#s2.hello()
#t1.hello()
#t2.hello()
#t1.teach()
#t2.teach()
#s1.study()
#s2.study()

s1.hello()
s1.mark_1()
