#x = [ 2,3,4,5]
#total = 1
#output = []
#for y in range(0,len(x)):
    #total = total * x[y]

#for z in range(0,len(x)):
    #output.append( total / x[z])

#print(total)
#print(output)
#################################################################

num = [ 1,2,3,4]
def selfe(num):
    left = [1]*len(num)
    right = [1]*len(num)
    for x in range(1,len(num)):
        left[x] = left[x-1]*num[x-1]
    for y in range(len(num)-2,-1,-1):
        right[y] = right[y+1]*num[y+1]

    res = [1]*len(num)
    for i in range(len(num)):
        res[i] = left[i]*right[i]
    print(res)
num = [ 1,2,3,4]
ans = selfe(num)
print(ans)