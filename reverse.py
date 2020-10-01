def rev(s):
    length = len(s)
    i = 0
    spaces =[" "]
    word_rev = []

    while i<length:
        if s[i] not in spaces:
            word_start = i
        while i<length and s[i] not in spaces:
            i+=1
        word_rev.append(s[word_start:i])
        
        i+=1
    return " ".join(reversed(s))


x = rev("I am the Best")
print(x)