def Multiples(size):

    result = []
    for i in range(size):
        if i%3==0 or i%5==0:
            result.append(i)
    total = 0
    for x in result:
        total = total+x
    return total

ans = Multiples(10)
print(ans)
