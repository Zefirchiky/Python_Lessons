import User
class Admin(User.User):
    def __init__(self, a, b, age, p):
        super().__init__(a, b, age,)
        self.privileges=p
        priv = Privileges(p)
        self.pr = priv
class Privileges:
    def __init__(self, p):
        self.privileges=p
    def show_privileges(self):
        for i in self.privileges:
            print(i)
