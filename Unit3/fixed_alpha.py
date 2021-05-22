"""
A A A A A
B B B B
C C C
D D 
E
"""

n = 5 
for row in range(n,0,-1):
	for col in range(row):
		print(chr(70-row), end=" ")
	print()

