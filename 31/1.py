class S:
    def __init__(self, d, v):
        self.dlina = d
        self.visota = v
    def obch_S(self):
        print(f"Plosha = {self.dlina*self.visota}")

P1 = S(int(input("Dlina:")),int(input("Visota:")))
P1.obch_S()
