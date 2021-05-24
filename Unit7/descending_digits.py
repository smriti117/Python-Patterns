""" 
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

"""
n = 5 
for row in range(1,n+1):
	for column in range(0,row):
		print(n-column, end=" ")
	print()
	
for row in range(1,n):
	for column in range(0,n-row):
		print(n-column, end=" ")
	print()