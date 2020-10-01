def ari(a,b):  #returning Multiple Values from a fuction
     x = a+b
     y = a-b
     z = a*b
     return {'add' : x , "Sub": y , "Mul":z}
x = ari(2,3)
print(x)