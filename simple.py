def ass(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    count = {}
    for letters in s1:
        if letters  in count:
            count[letters] += 1
        else:
            count[letters] = 1
    for letterts in s2:
        if letters in count:
            count[letters] -= 1
        else:
            count[letters] = 1
    for k in count:
        if k[count]!= 0:
            return False
        else:
            return True
x = ass("God" , "Dog")
print(x)