from math import gcd
class Division():
    def __init__(self,licznik,mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    def create_div(self):
        print(self.licznik,'/',self.mianownik)
    def simpler(self):
        print(int((self.licznik/gcd(self.licznik,self.mianownik))),'/',int((self.mianownik/gcd(self.licznik,self.mianownik))))
div = Division(10,300)
div.create_div()
div.simpler()
    