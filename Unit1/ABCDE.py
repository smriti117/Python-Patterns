
"""
ABCDEF
ABCDEF
ABCDEF
ABCDEF
ABCDEF
"""

n = int(input("Enter n : "))
for row in range(0,n):
	for column in range(0,n):
		print( (chr(65+column)),end="")
	print()
