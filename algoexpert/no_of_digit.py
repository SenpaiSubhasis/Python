def nOf(digit):
    count = 0
    while(digit>0):
        digit = digit//10
        count +=1
    return count
x= nOf(3456)
print(x)