print("S=1+2+3+4+...+n")
n=int(input("Ведите конечное значение суммы n"))

s=0
i=1
while i<=n:
    s+=i
    i+=1
print(s)
