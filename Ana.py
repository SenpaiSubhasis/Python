def ana(s1,s2):
    s1 =s1.replace(" ",'').lower()
    s2 =s2.replace(" ", '').lower()
    if len(s1)!= len(s2):
        return print("Length is Not Equal")
    
    count = {}
    for letters in s1:
        if letters in count:
            count[letters] += 1
        else:
            count[letters] = 1
    for letters in s2:
        if letters in count:
            count[letters] -= 1
        else:
            count[letters] =1

    for k in count:
        if count[k]!=0:
            return False
    else:
        return True

#x = ana("CLient EastWoof" , "Old HollyWood Action")
y  = ana("CLient EastWood" , "Old West Action")
#print(x)
print(y)