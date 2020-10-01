def subarray(array):
    if len(array)<0:
        print("Error")
    max_current = 0
    max_global = array[0]
    for x in range(1,len(array)-1):
        max_current = (max(array[x],max_current+array[x]))

    if max_current > max_global:
        max_global = max_current
    
    return max_global
     

x=  [-11, 22, 33, -44]
print(subarray(x))
