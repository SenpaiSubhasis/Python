def binaryMatrix(matrix):
  final = []
  for x in matrix:
    result = x[::-1]
    final.append(result)
  for x in range(len(final)):
    for y in range(len(final[x])):
      if final[x][y] ==0:
        final[x][y]=1
      else:
        final[x][y]=0
  
  return final

ans = binaryMatrix([[1,1,0],[1,0,1],[0,0,0]])
print(ans)

















 