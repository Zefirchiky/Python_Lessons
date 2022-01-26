class User:
    def __init__(self,a,b,c):
        self.first_name=a
        self.last_name=b
        self.age=c
        self.login_attemts=0
    def describe_user(self):
        print(f"{self.last_name} {self.first_name}: {self.age} years old")
    def greet_user(self):
        print(f"Hello, {self.last_name} {self.first_name}")
    def increment_login_attemts(self):
        self.login_attemts+=1
    def reset_login_attemts(self):
        self.login_attemts=0
