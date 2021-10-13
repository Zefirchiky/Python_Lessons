t = input("text:")
k = 0
n = 0
for i in t:
    k+=1
    if i==" ":
        n+=1
print ("С пробелом", k)
print ("Без пробела:", k-n)
print ("Кол-во слов:", n+1)
