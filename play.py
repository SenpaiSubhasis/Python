def rev(s):
    length = len(s)
    i =0
    word = []
    spaces = [" "]

    while i< length:
        if s[i] not in spaces:
            word_start = i

            while i< length and s[i] not in spaces:
                i+= 1

            word.append(s[word_start:i])

            i+=1

    return "".join(reversed(s))



 