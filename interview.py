import math as mg
def maxgcd(array):
  final =[]
  for x in range(len(array)-1):
    for y in range(len(array)-1):
      result = mg.gcd(array[x],array[y+1])
      final.append(result)
  
  return final

ans = maxgcd([12, 15, 18])
print(ans)




