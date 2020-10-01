def lps(string):
    finallongest = [0,1]
    for i in range(1,len(string)):
        odd = getlongestPalindrome(string,i-1,i+1)
        even = getlongestPalindrome(string,i-1,i)
        templongest = max(odd,even, key = lambda x:x[1]-x[0])
        finallongest =max(templongest,finallongest, key= lambda x:x[1]-x[0])
    return string[finallongest[0]:finallongest[1]]
def getlongestPalindrome(string,leftidx,rightidx):
    while leftidx >=0 and rightidx <len(string):
        if string[leftidx]!=string[rightidx]:
            break
        leftidx -=1
        rightidx+=1
    
    return [leftidx+1 , rightidx]
x = lps("abaxyzzyxf")
print(x)
