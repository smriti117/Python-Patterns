
"""
1
12
123
1234
12345
"""

n=5
for row in range(0,n):
	for col in range(row+1):
		print(col+1,end="")
	print()