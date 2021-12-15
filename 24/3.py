import random
p = [random.randint(1,9) for i in range(10)]
f = list(map(lambda x: x**3, p))
print(f)
