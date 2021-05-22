"""
E E E E E
D D D D
C C C 
B B 
A

"""
n = 5
for row in range(n,0,-1):
	for col in range(row):
		print(chr(64+row),end=" ")
	print()
	