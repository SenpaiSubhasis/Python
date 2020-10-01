def maximun_freq(list_ok):
    count = {}
    max_count = 0
    max_item = None

    for i in list_ok:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        
        if count[i] > max_count:
            max_count = count[i]
            max_item = i
        
    return max_item

x = maximun_freq([1,2,7,3,7,3,7,23,7])
print(x)