def int_k(n):
    print("Первый перебор")
    yield n
    print("Второй перебор")
    yield n+1

m = int(input("m="))
c = int_k(m)
print(next(c))
print(next(c))
print(next(c))
