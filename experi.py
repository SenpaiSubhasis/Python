def removeVowels(sentence):
  vowels = ["a","i","e","o","u"]
  for x in sentence:
    if x in vowels:
      sentence = sentence.replace(x , "")
  print(sentence)
 
if __name__ == "__main__":
    removeVowels(" welcome to geeksforgeeks")