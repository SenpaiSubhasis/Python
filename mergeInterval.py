def mergeInterval(matrix):
  result = []
  for x in range(len(matrix)-1):
    idxOne = matrix[x]
    x+=1
    idxTwo = matrix[x]
    if idxOne[1]>idxTwo[0] or idxOne[1]==idxTwo[0]:
      q = min(idxOne)
      w = max(idxTwo)
      final = []
      final.append(q)
      final.append(w)
      result.append(final)
      
    else:
      result.append(idxTwo)
    
  return result

    
    
ans = mergeInterval([[1,2],[3,5],[6,7],[8,10],[12,16]])
print(ans)