def string_mal(str1,str2):
    a = []
    b = []

    for x in range(len(str1)):
        if str1[x]!="#":
            a.append(str1[x])
        else:
            if a!=[]:
                a.pop()
    
    for y in range(len(str2)):
        if str2[y]!="#":
            b.append(str2[y])
        else:
            if b!=[]:
                b.pop()
    
    return a==b

x = string_mal("ab#c","ad#c")
print(x)