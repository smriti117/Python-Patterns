""" 
1 2 3 4 5
1 2 3 4 
1 2 3 
1 2 
1 

"""

n = 6
for row in range(1,n):
	for column in range(n-row):
		print(column+1, end=" ")
	print()