def firstmissing(arr):
    arr = set(arr)
    for x in range(1,len(arr)+2):
        if x not in arr:
            return x

ans = firstmissing([7,8,9,11,12])
print(ans)