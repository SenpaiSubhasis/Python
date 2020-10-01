def smallest(array1,array2):
    array1.sort()
    array2.sort()
    idxone = 0
    idxTwo = 0
    default = float("inf")
    diff = float("inf")
    smallestPair = []

    while idxone<len(array1) and idxTwo<len(array2):
        firstnum = array1[idxone]
        secondnum = array2[idxTwo]
        if firstnum < secondnum:
            diff = secondnum - firstnum
            idxone += 1
        elif secondnum < firstnum:
            diff = firstnum - secondnum
            idxTwo += 1
        else:
            return [firstnum,secondnum]
        
        if default > diff:
            default = diff
            smallestPair = [firstnum,secondnum]
    return smallestPair

x = smallest([-1,5,10,20,28,3],[26,134,135,15,17])
print(x)

       
