def insertion_sort(list_a):
    for i in range(1,len(list_a)):
        value_sort = list_a[i]
        while list_a[i-1] > value_sort and i>0:
            list_a[i],list_a[i-1] = list_a[i-1],list_a[i]
            i= i-1

list_a = [23,97,12,106,233,90,8,54,17]
insertion_sort(list_a)
print(list_a)
