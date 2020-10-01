def threeLargest(array):
    if len(array)<0:
        return False
    OutputArray = [None,None,None]
    for num in array:
        OperationStep(OutputArray,num)
    return OutputArray

def OperationStep(OutputArray,num):
    if OutputArray[2] is None or num>OutputArray[2]:
        finalOperation(OutputArray,num,2)
    elif OutputArray[1] is None or num>OutputArray[1]:
        finalOperation(OutputArray,num,1)
    elif OutputArray[0] is None or num>OutputArray[0]:
        finalOperation(OutputArray,num,0)

def finalOperation(Array,num,idx):
    for x in range(idx+1):
        if Array[x]==idx:
            Array[x] = num
        else:
            Array[x]=Array[x+1]


x = threeLargest( [1414,56,82000,2077])
print(x)