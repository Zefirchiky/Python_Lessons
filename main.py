# def hallo(a):
#     print(f"Hallo, {a}")
#
# hallo("Artem")

# def ntext(n, a):
#     print(a*n)
#
# ntext(5,"fsdlkfj")

# def max1(a,b):
#     if a>b:
#         print(a)
#     elif a==b:
#         print("equal")
#     else:
#         print(b)
#
# max1(6,6)

# def max1(a,b,c):
#     print(max(a,b,c))
#
# max1(7, 10, 9)

# def sush(a,b,c):
#     x = [a,b,c]
#     sorted(x)
#     if x[0]>=x[1]+x[2]:
#         print("ne sush")
#     else:
#         print("sush")
#
# sush(9,4,5)

# def dublstr(a,b):
#     print(a+b)
#
# dublstr("djf","djf")

# def deystv(a,b,c):
#     if c=="+":
#         print(round(a+b, 2))
#     elif c=="-":
#         print(round(a-b, 2))
#     elif c=="/":
#         print(round(a/b, 2))
#     elif c=="*":
#         print(round(a*b, 2))
#     else:
#         print("Unknown operation")
#
# deystv(5,6,"/")

# def tegs(a,b):
#     print(f"<{a}>{b}</{a}>")
#
# tegs("p","kek")

# def yearp(a):
#     if a==12 or a==1 or a==2:
#         print("Winter")
#     elif a>2 and a<6:
#         print("Autumn")
#     elif a>5 and a<9:
#         print("Summer")
#     else:
#         print("Vesna")
#
# yearp(2)

# x=[]
# def mnogatochek(a):
#     for i in a:
#         print("*"*i)
#
#
# for i in range(7):
#     x.append(int(input()))
#
# mnogatochek(x)

# def parn(a):
#     if a%2==0:
#         print("parn")
#     else:
#         print("neparn")
#
# parn(20)

# x=[]
# def spisok(a):
#     print(a[0], a[-1])
#
# for i in range(7):
#     x.append(int(input()))
#
# spisok(x)

# def fact(a):
#     x=1
#     for i in range(1,a+1):
#         x*=i
#     print(x)
#
# fact(int(input()))

def sush(a,b,c):
    g=0
    x = [a,b,c]
    sorted(x)
    if x[0]>=x[1]+x[2]:
        print("ne sush")
    else:
        print("sush")
        g=1

def triug(a,b,c):
    sush(a,b,c)
    if g==1:
        p=(a+b+c)/2
        S=(p*(p-a)*(p-b)*(p-c))**(1/2)
        print(S)
triug(5,7,6)

def circle(r):
    S=2*3.14*r**2
    print(S)
circle(5)

def pryamocut(a,b):
    S=a*b
    print(S)
pryamocut(3,4)

def SFiguri(a):
    if a=="triugolnik":
        triug(int(input()),int(input()),int(input()))
    elif a=="circle":
        circle(int(input()))
    elif a=="pryamocut":
        pryamocut(int(input()),int(input()))

SFiguri("triugolnik")
