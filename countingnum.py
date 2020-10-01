def counting_element(array):
    if len(array)<0:
        return print("Error")
    output = []
    count = 0
    for x in range(0,len(array)-1):
        output.append(array[x]+1)
    
    for y in array:
        if y in output:
            count= count+1
    
    return count

x = counting_element( [1,1,2,2])
print(x)
