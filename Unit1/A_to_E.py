

"""
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E 
"""

n = int(input("Enter n : "))
for row in range(0,n):
	print( (chr(65+row)*n),end="")
	print()