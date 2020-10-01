def infyTQ(word):
  special_char=["!","@","#","$","%","^","&","*"]
  result = [] 
  for x in word:
    if x not in special_char:
      result.append(x)
  result.reverse()
  
  for y in range(len(word)):
    if word[y].isalpha()==False:
      result.insert(y,word[y])
  
  answer = ""
  return(answer.join(result))

  return answer
  

ans = infyTQ("#ab$is")
print(ans)
