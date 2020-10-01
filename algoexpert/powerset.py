def powerset(array):
    if len(array)<0:
        return False
    subset = [[]]
    result = []
    for ele in array:
        for i in range(len(subset)):
            currentSubset =subset[i]
            subset.append(currentSubset+[ele])
    for x in  subset:
        if len(x)==1 or len(x)==2:
            result.append(x)
    return result

ans = powerset([1, 12, 23, 34])
print(ans)