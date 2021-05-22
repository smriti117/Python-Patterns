""" 
A
B B 
C C C 
D D D D 
E E E E E

"""

n = 5 

for row in range(0,n):
	for col in range(row+1):
		print(chr(65+row),end=" ")

	print()