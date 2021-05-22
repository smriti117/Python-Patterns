""" 
1 1 1 1 1
2 2 2 2
3 3 3 
4 4 
5

"""

n = 6
for row in range(1,n):
	for column in range(n,row,-1):
		print(str(row),end=" ")
	print()