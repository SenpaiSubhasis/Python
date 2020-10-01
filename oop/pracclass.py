class sellstrock:
    def __init__(self,array):
        self.array = array
    def maxprofit(self):
         if len(self.array)<1:
            return print("YOu are Lucky it just One item")
    diff_array = []
    for x in range(1,len(array)):
        diff_array.append(self.array[x]-self.array[x-1])
    
    max_profit = []
    for y in diff_array:
        if y >0:
            max_profit.append(y)
        
    total = 0
    for z in range(0,len(max_profit)):
        total = total + max_profit[z]
    return total
