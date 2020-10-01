def firstNonRepeating(word):
    if len(word)<0:
        return False
    count = {}
    for i in word:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    
    for x in count:
        if count[x]==1:
            return x
x = firstNonRepeating("aaabcccdeeef")
print(x)
