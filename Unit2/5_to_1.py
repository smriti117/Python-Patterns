
""" 
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 

"""

n = 5
for row in range(0,n):
	for col in range(row+1):
		print(n-col, end="")
	print()

