def SortedMatrix(matrix,target):
 
		
	row = 0
	col = len(matrix[0])-1
	while row <len(matrix) and col>=0:
		if matrix[row][col] > target:
			col -=1
		elif matrix[row][col]<target:
			row+=1
		else:
			return[row,col]
	return [-1,-1]



ans = SortedMatrix([[1,2,3,4]],3)
print(ans)