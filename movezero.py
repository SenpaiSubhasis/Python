def MoveZero(array):
    if len(array)<0:
        return print("Error")
    output = []
    final = []
    for x in array:
        if x == 2:
            output.append(x)
        else:
            final.append(x)
    
    for y in output:
        final.append(y)
    #final.append(output)
    return final

x = MoveZero([2,1,2,2,2,3,4,2])
print(x)