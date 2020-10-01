#myList = [23,11,9,43,52,12]
#y = len(myList)-1
#print(y)
#for x in range(0,len(myList)-1):
    #print(x)
    
def bubblesort(myList):
    for i in range(len(myList)-1):
        for j in range(len(myList)-1-i):
            if myList[j] > myList[j+1]:
                myList[j] , myList[j+1] = myList[j+1] , myList[j]
    return myList

myList = [23,11,9,43,52,98,200,65,2,3]
bubblesort(myList)
print(myList)
