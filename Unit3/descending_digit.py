""" 
5 4 3 2 1
5 4 3 2 
5 4 3 
5 4
5


"""

n = 5
for row in range(n,0,-1):
	for col in range(row):
		print(row,end=" ")
	print()