class User:
    def __init__(self, a, b, age, growth):
        self.first_name=a
        self.second_name=b
        self.age=age
        self.growth=growth
        self.login_attemts=0
    def describe_user(self):
        print(f"{self.first_name} {self.second_name}")
    def greeting_user(self):
        print(f"Hello {self.second_name} {self.first_name}")
    def increment_login_attemts(self):
        self.login_attemts+=1
    def reset_login_attemts(self):
        self.login_attemts=0
