def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    
    pivot = sequence.pop()
    item_lower = []
    item_greater = []

    for item in sequence:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)
    return quick_sort(item_lower) + [pivot] + quick_sort(item_greater)

print(quick_sort([23,97,12,106,233,90,8,54,17]))
