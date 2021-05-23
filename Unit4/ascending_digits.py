"""
 
 	1
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5


"""

n = 5 
for row in range(0,n):
	print((n-row)*" ", end=" ")
	for col in range(row+1):
		print(col+1,end=" ")
	print()
