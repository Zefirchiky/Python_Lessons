n=int(input("Введите значение n"))

s=0
i=1
a=1/2
while i<=n:
    s+=a
    i+=1
    a/=2
    print(s)
print(s)
