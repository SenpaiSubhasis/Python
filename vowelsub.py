def vowelsub(word,target):
    if len(word)<0:
        return False

    start = 0
    count = set()

    for x in range(len(word)):
        if isVowel(word[x])==True:
            count.add(word[x])
            if (len(count)==target):
                print(word[start:x+1])
        else:
            start = x+1
            count.clear




def isVowel(x):
    return (x =="a" or x =="e" or x =="i" or x=="o" or x=="u")
if __name__ == "__main__":
    vowelsub(" aeoibsddaeiouudb",5)
 