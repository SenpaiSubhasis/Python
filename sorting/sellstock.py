def sell_strock(array):
    if len(array)<1:
        return print("YOu are Lucky it just One item")
    diff_array = []
    for x in range(1,len(array)):
        diff_array.append(array[x]-array[x-1])
    
    max_profit = []
    for y in diff_array:
        if y >0:
            max_profit.append(y)
        
    total = 0
    for z in range(0,len(max_profit)):
        total = total + max_profit[z]
    return total


        
    
    #return max_profit
    #return total

x = sell_strock([ 7,6,4,3,1])
print(x)