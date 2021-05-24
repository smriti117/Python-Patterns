""" 

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""
n = 5 
for row in range(1,n+1):
	for column in range(1,row+1):
		print(str(column), end=" ")
	print()
	
for row in range(1,n):
	for column in range(1,n-row+1):
		print(str(column), end=" ")
	print()