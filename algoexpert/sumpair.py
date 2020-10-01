def pair_sum(array,target):
    if len(array)<0:
        return print("Error")
    
    nums = {}
    
    for x in array:
        if target-x in nums:
            return [target-x,x]
        else:
            nums[x] = True

    return []



x = pair_sum([1,2,334,23],357)
print(x)



 