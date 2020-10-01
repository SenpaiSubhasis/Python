def keden(array):
    maxCurrentEnding = array[0]
    maxSofar = array[0]
    final = []
    for x in array[1:]:
        maxCurrentEnding = max(x,maxCurrentEnding+x)
        maxSofar = max(maxSofar,maxCurrentEnding)
 
    return maxSofar 


y = keden([4,2,-3,1,8])
print(y)