""" 
A
BB
CCC
DDDD
EEEEE
DDDD
CCC
BB
A

"""
n = 5 

for row in range(0,n+1):
	print(chr(64+row)*row, end=" ")
	print()
	
for row in range(1,n):
	print(chr(69-row)*(n-row), end=" ")
	print()