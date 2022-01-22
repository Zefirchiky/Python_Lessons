import User

u1 = User.User("Artem", "Mudruk", 15, 175)
u1.describe_user()
u1.greeting_user()
u1.increment_login_attemts()
u1.increment_login_attemts()
u1.increment_login_attemts()
print(u1.login_attemts)
u1.reset_login_attemts()
print(u1.login_attemts)
