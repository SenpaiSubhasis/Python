def is_leap(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    else:
        return False
x = is_leap(1990)
print(x)