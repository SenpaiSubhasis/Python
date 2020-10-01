def line(cordinate):
    if len(cordinate)==2:
        return True
    x0,y0 = cordinate[1]
    x1,y1 = cordinate[2]
    for i in range(2,len(cordinate)):
        x,y = cordinate[i]
        if (y1-y0)*(x-x0)!=(y-y0)*(x1-x0):
            return False
    return True

points = line([[2,3][4,5],[2,4]])
print(points)