class experi:
    def __init__(self,first_name,second_name,third_name):
        self.first_name = first_name
        self.second_name = second_name
        self.third_name = third_name

    def email(self):
        return self.first_name + self.second_name +self.third_name+"@myAss.com"
    
class experi_2:
     super().__init__(self,first_name ,second_name,third_name)
     self.fourth_name = fourth_name

     def discord(self):
         return self.first_name + self.second_name +self.third_name+self.fourth_name+"@myAss.com"

exp_1 = experi("Subhasis","Kalia","Bitch")
exp_2 = experi_2("Subhasis","Kalia","BItch","Cunt")
print(exp_1.email())
print(exp_2.discord())