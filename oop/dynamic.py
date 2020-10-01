fibo_cache={}   # Using Dynamic Programming to decrease time complexcity

def fibo(n):
    if n in fibo_cache:
        return fibo_cache[n]
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
         return fibo(n-1)+fibo(n-2)

    fibo_cache[n] = True
    return value
result = []
for n in range(1,34):
    result.append(fibo(n))

total = 0
for x in result:
    if x%2==0:
        total = total+x
print(total)
    
