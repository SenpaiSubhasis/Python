def threePair(array,targetSum):
    allpairsum = {}
    quadruplets = []

    for i in range(1,len(array)-1):
        for j in range(i+1,len(array)):
            currentsum = array[i]+array[j]
            difference = targetSum-currentsum
            if difference in allpairsum:
                for pair in allpairsum[difference]:
                    quadruplets.append(pair+[array[i]+array[j]])
        for k in range(0,i):
            currentsum = array[i]+array[k]
            if currentsum not in allpairsum:
                allpairsum[currentsum] = [[array[k],array[i]]]
            else:
                allpairsum[currentsum].append([array[k],array[i]])
    return quadruplets

ans = threePair([7,6,4,-1,1,2],16)
print(ans)
