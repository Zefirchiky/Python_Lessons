class Druk:
    def vvod(self,v):
        self.v=v
    def vivod(self):
        print(str.upper(self.v))

st = Druk()
st.vvod(input("Vvod: "))
st.vivod()
