def attendence(ans):
  count ={"A":0 , "L":0 , "P":0}
  for x in ans:
    if x not in count:
      count[x]=1
    else:
      count[x]+=1
  idxOne = 0
  pointer = 0
  while idxOne<len(ans)-1:
    
    if ans[idxOne]==ans[idxOne+1]:
        idxOne+=1
        pointer+=1
    else:
      idxOne+=1

  if pointer>2:
    return False
  for x in count:
    if count[x]<=1:
      return True

answer = attendence("PPALLP")
print(answer)