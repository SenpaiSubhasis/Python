def TwoCity(matrix):
    if len(matrix)<0:
        return False
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x = min(matrix[i][j],matrix[i][j+1])
            result.append(x)
            break
    
    total = 0
    for sum in result:
        total = total + sum

    return total

x = TwoCity([[10,20],[30,200],[400,50],[30,20]])
print("The total Minimum Cost is"""+str(x))
    