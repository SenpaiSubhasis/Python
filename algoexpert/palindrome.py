def palindrome(stringOne):
	if len(stringOne)<0:	
		return print("Error")
	oneidx = 0
	twoidx = len(stringOne)-1
	
	while oneidx < twoidx:
		if stringOne[oneidx]!= stringOne[twoidx]:
			return False
		oneidx+=1
		twoidx-=1
	return True
x =palindrome("aba")
print(x)