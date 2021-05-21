
"""
1 1 1 1 1
2 2 2 2 2 
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
	
n = int(input("Enter n : "))
for row in range(1,n):
	for column in range(1,n):
		print(row, end=" ")
	print()