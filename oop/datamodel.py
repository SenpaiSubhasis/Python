class polynomial:
    def __init__(self ,first,second):
        self.first = first
        self.second = second
  
    def add(self):
        return self.first + self.second 
    def sub(self):
        return self.first + self.second
    def mul(self):
        return self.first + self.second
    def div(self):
        return self.first + self.second
class Advanced(polynomial):
    def __init__(self,first,second,third):
        super().__init__(first,second)
        self.third =third
    def adv_add(self):
        return self.first + self.second +self.third
    



poly_1 = polynomial(3,5)
print(poly_1.add())
poly_advan=Advanced(2,3,6)
print(poly_advan.adv_add())