"""
A B C D E 
A B C D 
A B C 
A B 
A 

"""

n = 5
for row in range(0,n):
	for column in range(n-row):
		print(chr(65+column), end=" ")
	print()

