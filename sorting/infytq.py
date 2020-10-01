def InfyTq(word):    
  if len(word)<0:
    return False
  count = {}
  output = []
  for x in word:
    if x not in output:
      output.append(x)
    else:
      count[x] = True
  
  output.reverse()
  result = ""
  return (result.join(output))

ans = InfyTq("google")
print(ans)