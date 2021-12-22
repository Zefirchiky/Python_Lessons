class cercle:
    n=0
    def __init__(self,radius):
        self.radius=radius
        cercle.n+=1
    def p(self):
        return 2*3.14*self.radius**2
    def pr(self):
        print(f"radius {self.radius}, plosh {self.p()}")

c = cercle(int(input("r:")))
c.pr()
c = cercle(int(input("r:")))
c.pr()
print(cercle.n)
