def isVowel(x): 
      
 
    return (x == 'a' or x == 'e' or 
            x == 'i' or x == 'o' or 
            x == 'u'); 
   
def FindSubstring(str): 
  
    hash = set();  
  
    start = 0; 
    for i in range(len(str)): 
          
   
        if (isVowel(str[i]) == True): 
            hash.add(str[i]); 
   
            if (len(hash) == 5): 
                print(str[start : i + 1],  
                              end = " "); 
        else: 
            start = i + 1; 
            hash.clear(); 
  
  
str = "aeoibsddaeiouudb"; 
FindSubstring(str); 