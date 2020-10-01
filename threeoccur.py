def threeOccurence(array):
    count = {}
    for x in array:
        if x in count:
            count[x]+=1
        else:
            count[x] = 1
    subarray = 0

    for i in count:
        if count[i] ==1: 
            return 0
        elif count[i]==3:
            subarray=1
        elif count[i]//3:
            subarray+=count[i]//3
        else:
            break
    return subarray

  
ans = threeOccurence([1, 2, 2, 2, 1 ,1 ,2 ,2, 2])
print(ans)