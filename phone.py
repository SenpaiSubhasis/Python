def PhoneCombination(User_input):
    if len(User_input)>3:
        return False
    info = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
    output = []
    for x in User_input:
        if x in info:
            output.append(info[x])
    i = output[0]
    j = output[1]
    combination = []    
    combination = [f'{a}{b}' for a in i for b in j]                                
    #for w in i:
        #for q in j:
            #combination.append(w+q)

    return combination

ans = PhoneCombination("23")
print(ans)