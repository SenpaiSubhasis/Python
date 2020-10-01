def rotate(array,k):
    array_1 = list(reversed(array)) # Reverse the Original Array
    array_2 = array_1[0:k] # Extracting the value from Original Array from index 0 to k
    array_3 = list(reversed(array_2)) # Reverse the Element of Array from index 0 to k
    array_4 = array_1[k:len(array)] # Extracting the value from k to len(array) from Original Array
    array_5 = list(reversed(array_4))#Reverse  the element from k to len(array)
    for i in array_5:
        array_3.append(i)
    return array_3







x = rotate([1,2,3,4,5,6,7,8,9,8],3)
print(x)