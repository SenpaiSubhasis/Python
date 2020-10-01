import math
import os
import random
import re
import sys

def avg(*num):

    result = float(sum(nums)/len(nums))
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)