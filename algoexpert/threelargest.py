def threeLargest(array):
    threelargest = [None,None,None]
    for num in array:
        updateLargest(threelargest,num)
    return threelargest

def updateLargest(threeLargest,num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest,num,2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest , num ,1)
    elif threeLargest[0] is None or num >threeLargest[0]:
        shiftAndUpdate(threeLargest , num ,0)

def shiftAndUpdate(array,num,idx):
    for i in range(idx+1):
        if i == idx:
            array[i] =num
        else:
            array[i] = array[i+1]

x = threeLargest([1414,56,82000,2077])
print(x)